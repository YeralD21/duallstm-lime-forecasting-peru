"""Revision G7, ronda 2. Codigo nuevo que reutiliza lib/ del pipeline sin modificarlo.

ETS y Theta bajo el mismo protocolo rolling-origin que SARIMA / SARIMA-sel (lib/modelos_series.py):
  - train = 2016-07..dic Y-2 (lib.modelos_series._particiones), validacion = Y-1, test = Y;
  - parametros estimados UNA vez en train;
  - validacion y test a 1 paso: se pronostica el mes t con los datos hasta t-1 y luego se incorpora el valor real
    de t como estado, SIN reestimar parametros (equivalente a append(refit=False) de SARIMAX).
ETS: statsmodels ETSModel; el estado se actualiza con ETSModel(y_hasta_t-1).smooth(params_de_train), que filtra
la serie extendida con los mismos parametros (incluidos los estados iniciales estimados en train).
Theta: statsmodels ThetaModel no tiene append; la actualizacion con parametros fijos (b0, alpha, factores
estacionales) se programa aqui con las formulas de statsmodels (theta.py, forecast_components) y se verifica que,
sin datos nuevos, reproduce ThetaModelResults.forecast(1).
"""
from __future__ import annotations

import itertools
import json
import sys
import warnings
from pathlib import Path

R2 = Path(__file__).resolve().parents[1]
BR = R2.parent
LIB = BR / "02_scripts"
RAIZ = BR.parents[1]
for _p in (str(RAIZ), str(LIB)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

RES = R2 / "resultados"
UNI = RES / "unidades"
G7 = BR / "12_revision_g7"
VENTANAS = (2021, 2022, 2023, 2024, 2025)
CULTIVARES = ("sutil", "dulce")
NUEVOS = ("ETS", "Theta")
PERIODO = 12
# 2 errores x 3 tendencias (ninguna, aditiva, aditiva amortiguada) x 2 estacionalidades = 12 especificaciones
REJILLA_ETS = [dict(error=e, trend=t, damped_trend=d, seasonal=s)
               for e, (t, d), s in itertools.product(("add", "mul"), ((None, False), ("add", False), ("add", True)), ("add", "mul"))]
MAXITER_ETS = 1000  # valor por defecto de ETSModel.fit en statsmodels 0.14.6


def nombre_ets(spec: dict) -> str:
    t = "N" if spec["trend"] is None else ("Ad" if spec["damped_trend"] else "A")
    return f"ETS({spec['error'][0].upper()},{t},{spec['seasonal'][0].upper()})"


def particiones(serie: pd.Series, ventana):
    from lib.modelos_series import _particiones

    return _particiones(serie, ventana)


def _filas(particion: str, fechas, y_true, y_pred) -> list[dict]:
    return [{"particion": particion, "fecha": f, "y_true": float(a), "y_pred": float(b)} for f, a, b in zip(fechas, y_true, y_pred)]


# ----------------------------------------------------------------------------- ETS
def _ajustar_ets(y: np.ndarray, spec: dict):
    from statsmodels.tsa.exponential_smoothing.ets import ETSModel

    with warnings.catch_warnings(record=True) as avisos:
        warnings.simplefilter("always")
        mod = ETSModel(y, seasonal_periods=PERIODO, initialization_method="estimated", **spec)
        fit = mod.fit(disp=False, maxiter=MAXITER_ETS)
    conv = bool(fit.mle_retvals.get("converged", False)) if isinstance(fit.mle_retvals, dict) else None
    return fit, conv, sorted({a.category.__name__ for a in avisos})


def _pronostico_ets(y_hasta: np.ndarray, spec: dict, params: np.ndarray, h: int = 1) -> float:
    from statsmodels.tsa.exponential_smoothing.ets import ETSModel

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        r = ETSModel(y_hasta, seasonal_periods=PERIODO, initialization_method="estimated", **spec).smooth(params)
        return float(np.asarray(r.forecast(h), dtype=float)[-1])


def seleccionar_ets(y: np.ndarray):
    """Minimo AICc en train entre las 12 especificaciones (empate: orden de la rejilla)."""
    filas, ajustes = [], {}
    for i, spec in enumerate(REJILLA_ETS):
        fila = {"indice": i, "modelo": nombre_ets(spec), **{k: str(v) for k, v in spec.items()}, "aicc": np.nan, "aic": np.nan,
                "convergio": None, "avisos": "", "error_ajuste": ""}
        try:
            fit, conv, av = _ajustar_ets(y, spec)
            fila.update(aicc=float(fit.aicc), aic=float(fit.aic), convergio=conv, avisos=";".join(av))
            ajustes[i] = fit
        except Exception as exc:  # noqa: BLE001 - una especificacion que falla se descarta y se registra
            fila["error_ajuste"] = f"{type(exc).__name__}: {exc}"[:300]
        filas.append(fila)
    rejilla = pd.DataFrame(filas)
    validos = rejilla[np.isfinite(rejilla.aicc)]
    elegido = validos.sort_values(["aicc", "indice"], kind="mergesort").iloc[0]
    spec, fit = REJILLA_ETS[int(elegido.indice)], ajustes[int(elegido.indice)]
    return spec, fit, rejilla, elegido


def ets_rolling(serie: pd.Series, ventana) -> tuple[pd.DataFrame, dict, pd.DataFrame]:
    """Seleccion por AICc en train entre las 12 especificaciones; val y test a 1 paso con parametros fijos."""
    s, train, val = particiones(serie, ventana)
    y = train.to_numpy()
    spec, fit, rejilla, elegido = seleccionar_ets(y)
    params = np.asarray(fit.params, dtype=float).copy()
    # control: smooth con los parametros de train reproduce el pronostico del ajuste
    f0 = float(np.asarray(fit.forecast(1), dtype=float)[0])
    if not np.isclose(_pronostico_ets(y, spec, params), f0, rtol=1e-9, atol=1e-6):
        raise AssertionError("ETS: smooth(params) no reproduce forecast(1) del ajuste en train")
    meses = list(val.index) + list(ventana.meses_test)
    pos = {m: i for i, m in enumerate(s.index)}
    pred = []
    for m in meses:
        hist = s[(s.index >= "2016-07") & (s.index < m)].to_numpy()
        pred.append(_pronostico_ets(hist, spec, params))
        assert len(hist) == pos[m] - pos["2016-07"]
    nv = len(val)
    out = pd.DataFrame(_filas("val", meses[:nv], [s[m] for m in meses[:nv]], pred[:nv])
                       + _filas("test", meses[nv:], [s[m] for m in meses[nv:]], pred[nv:]))
    info = {"especificacion": nombre_ets(spec), **{k: spec[k] for k in spec}, "aicc": float(elegido.aicc),
            "convergio": bool(elegido.convergio) if elegido.convergio is not None else None,
            "parametros": dict(zip(fit.param_names, params.tolist())), "n_train": int(len(train)),
            "train_inicio": str(train.index.min()), "train_fin": str(train.index.max()),
            "n_especificaciones": len(REJILLA_ETS), "n_fallidas": int((rejilla.error_ajuste != "").sum()),
            "n_no_convergidas": int((rejilla.convergio == False).sum()),  # noqa: E712
            "seleccion": "minimo AICc en train (empate: orden de la rejilla)"}
    return out, info, rejilla


# ----------------------------------------------------------------------------- Theta
class ThetaFijo:
    """Theta (theta=2) con b0, alpha y factores estacionales fijados en train; el estado SES se actualiza con cada dato."""

    def __init__(self, y_train: np.ndarray):
        from statsmodels.tsa.forecasting.theta import ThetaModel

        self.mod = ThetaModel(y_train, period=PERIODO)
        self.res = self.mod.fit()
        self.b0, self.alpha = float(self.res.params["b0"]), float(self.res.params["alpha"])
        self.estacional = np.asarray(self.res._seasonal, dtype=float)
        self.metodo = self.mod.method
        self.desestacionaliza = bool(self.mod.deseasonalize and self.estacional.shape[0])
        self.n = 0
        self.nivel = np.nan
        for v in y_train:
            self.agregar(float(v))
        if not np.isclose(self.nivel, float(np.asarray(self.res._one_step)[0]), rtol=1e-9, atol=1e-6):
            raise AssertionError("Theta: la recursion SES no reproduce el one_step de statsmodels")
        if not np.isclose(self.pronostico(), float(np.asarray(self.res.forecast(1))[0]), rtol=1e-9, atol=1e-6):
            raise AssertionError("Theta: el pronostico manual no reproduce ThetaModelResults.forecast(1)")

    def _factor(self, i: int) -> float:
        return float(self.estacional[i % PERIODO])

    def agregar(self, y: float) -> None:
        if self.desestacionaliza:
            x = y / self._factor(self.n) if self.metodo.startswith("mul") else y - self._factor(self.n)
        else:
            x = y
        if self.n == 0:  # nivel inicial conocido = primer dato desestacionalizado (initial_level=y[0] en statsmodels)
            self.nivel = x
        self.nivel = self.alpha * x + (1 - self.alpha) * self.nivel
        self.n += 1

    def pronostico(self, h: int = 1) -> float:
        """Pronostico a h pasos desde el estado actual (theta.py: forecast_components y forecast)."""
        hh = (h - 1) + (1 / self.alpha - (1 - self.alpha) ** self.n / self.alpha if self.alpha > 0 else 0.0)
        f = 0.5 * self.b0 * hh + self.nivel
        i = self.n + h - 1
        if self.desestacionaliza:
            f = f * self._factor(i) if self.metodo.startswith("mul") else f + self._factor(i)
        return float(f)


def theta_rolling(serie: pd.Series, ventana) -> tuple[pd.DataFrame, dict]:
    s, train, val = particiones(serie, ventana)
    th = ThetaFijo(train.to_numpy())
    p0 = (th.b0, th.alpha, th.estacional.copy())
    meses = list(val.index) + list(ventana.meses_test)
    pred = []
    for m in meses:
        pred.append(th.pronostico())
        th.agregar(float(s[m]))
    if not (p0[0] == th.b0 and p0[1] == th.alpha and np.array_equal(p0[2], th.estacional)):
        raise AssertionError("Theta: los parametros cambiaron durante la actualizacion")
    nv = len(val)
    out = pd.DataFrame(_filas("val", meses[:nv], [s[m] for m in meses[:nv]], pred[:nv])
                       + _filas("test", meses[nv:], [s[m] for m in meses[nv:]], pred[nv:]))
    info = {"b0": th.b0, "alpha": th.alpha, "theta": 2.0, "desestacionaliza": th.desestacionaliza, "metodo_estacional": th.metodo,
            "factores_estacionales": th.estacional.tolist(), "n_train": int(len(train)), "train_inicio": str(train.index.min()),
            "train_fin": str(train.index.max()), "opciones": "ThetaModel(period=12) por defecto: deseasonalize=True, use_test=True, "
            "method='auto'; fit(use_mle=False)"}
    return out, info


def escribir(df: pd.DataFrame, ruta: Path) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(ruta, index=False, float_format="%.10g", lineterminator="\n")


def escribir_json(d: dict, ruta: Path) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(d, indent=1, ensure_ascii=False, default=float), encoding="utf-8", newline="\n")


# ============================================================================= Dia 2
def per(f: str, k: int) -> str:
    """Mes 'YYYY-MM' desplazado k meses hacia atras."""
    return str(pd.Period(f, "M") - k)


# ----------------------------------------------------------------------------- horizonte h (T9)
def ets_h(serie: pd.Series, ventana, h: int) -> tuple[pd.DataFrame, dict]:
    """ETS elegido por AICc en train (igual que T1); pronostico del mes t con datos hasta t-h, parametros fijos."""
    s, train, _ = particiones(serie, ventana)
    spec, fit, _, _ = seleccionar_ets(train.to_numpy())
    params = np.asarray(fit.params, dtype=float).copy()
    filas = []
    for m in ventana.meses_test:
        hist = s[(s.index >= "2016-07") & (s.index <= per(m, h))].to_numpy()
        filas.append({"particion": "test", "fecha": m, "origen": per(m, h), "y_true": float(s[m]),
                      "y_pred": _pronostico_ets(hist, spec, params, h)})
    return pd.DataFrame(filas), {"especificacion": nombre_ets(spec)}


def theta_h(serie: pd.Series, ventana, h: int) -> tuple[pd.DataFrame, dict]:
    """Theta con parametros fijos de train; el estado incorpora los datos hasta t-h antes de pronosticar t."""
    s, train, _ = particiones(serie, ventana)
    th = ThetaFijo(train.to_numpy())
    if not np.isclose(th.pronostico(h), float(np.asarray(th.res.forecast(h))[-1]), rtol=1e-9, atol=1e-6):
        raise AssertionError("Theta: el pronostico manual a h pasos no reproduce ThetaModelResults.forecast(h)")
    pend = [m for m in s.index if m > train.index.max()]
    filas = []
    for m in ventana.meses_test:
        while pend and pend[0] <= per(m, h):
            th.agregar(float(s[pend.pop(0)]))
        filas.append({"particion": "test", "fecha": m, "origen": per(m, h), "y_true": float(s[m]), "y_pred": th.pronostico(h)})
    return pd.DataFrame(filas), {"alpha": th.alpha, "b0": th.b0}


# ----------------------------------------------------------------------------- regla de respaldo de SARIMA-sel (T5)
REGLA_RESPALDO = ("Si el orden elegido por MAE de validacion entre los 5 de menor AIC no converge en el ajuste final, se usa el "
                  "siguiente con menor MAE de validacion (empate: menor AIC de la rejilla, luego orden de la rejilla) entre los "
                  "que convergen. Si ninguno converge se conserva el elegido y se marca.")


def _orden(txt: str) -> list:
    return json.loads(txt.replace("(", "[").replace(")", "]"))


def elegir_con_respaldo(candidatos: pd.DataFrame, ajustar_final) -> dict:
    """Regla general para cualquier ventana y protocolo.

    candidatos: candidatos.csv de SARIMA-sel (posicion_aic, order, seasonal_order, aic_rejilla_maxiter200, indice_rejilla, MAE_val).
    ajustar_final(order, seasonal_order) -> (fit, convergio): el ajuste final del protocolo (original: el mismo ajuste de
    train con maxiter 500; E1: reajuste con datos hasta Y-1).
    """
    orden = candidatos.sort_values(["MAE_val", "aic_rejilla_maxiter200", "indice_rejilla"], kind="mergesort")
    intentos = []
    for r in orden.itertuples():
        o, so = _orden(r.order), _orden(r.seasonal_order)
        fit, conv = ajustar_final(o, so)
        intentos.append({"posicion_aic": int(r.posicion_aic), "orden": f"{tuple(o)}{tuple(so)}", "MAE_val": float(r.MAE_val),
                         "convergio": conv})
        if conv:
            return {"fit": fit, "order": o, "seasonal_order": so, "posicion_aic": int(r.posicion_aic), "intentos": intentos,
                    "respaldo_usado": len(intentos) > 1, "sin_convergencia": False}
    r = orden.iloc[0]
    o, so = _orden(r.order), _orden(r.seasonal_order)
    return {"fit": ajustar_final(o, so)[0], "order": o, "seasonal_order": so, "posicion_aic": int(r.posicion_aic),
            "intentos": intentos, "respaldo_usado": False, "sin_convergencia": True}


# ----------------------------------------------------------------------------- tabulares (T6, T7, T9)
BLOQUES = {
    "produccion": lambda c: (f"produccion_t_{c}", f"produccion_t_{c}_lag1", f"produccion_t_{c}_lag3", f"produccion_t_{c}_lag6"),
    "calendario": lambda c: ("mes_sin", "mes_cos", "t_index"),
    "clima": lambda c: tuple(f"{v}_lag{k}" for v in ("T2M", "T2M_MAX", "WS2M", "PRECTOTCORR", "RH2M") for k in (1, 3, 6)),
    "emergencias": lambda c: tuple(f"{v}_lag{k}" for v in ("num_emergencias", "personas_afectadas", "personas_damnificadas",
                                                            "hectareas_cultivo_perdidas", "hectareas_cultivo_afectadas") for k in (1, 3, 6)),
    "noticias": lambda c: tuple(f"{v}_lag{k}" for v in ("avg_sentiment", "n_noticias") for k in (1, 3, 6)),
}


def col_y12(c: str) -> str:
    return f"produccion_t_{c}_y12"


def con_y12(feats: pd.DataFrame, serie: pd.Series, c: str, h: int) -> pd.DataFrame:
    """Agrega la columna y_(T-12) para el par fila t -> objetivo T = t+h: su valor en la fila t es y_(t+h-12)."""
    f = feats.copy()
    clave = f["año"].astype(int).astype(str) + "-" + f["mes"].astype(int).map("{:02d}".format)
    f[col_y12(c)] = [float(serie[per(k, 12 - h)]) if per(k, 12 - h) in serie.index else np.nan for k in clave]
    return f


def pares_h(frame: pd.DataFrame, predictores, objetivo: str, ventana, h: int = 1, filtro_col: str | None = None) -> dict:
    """Pares X_t -> y_(t+h) (lib/preparacion.pares_tabulares con h); particion por el anio del objetivo.

    Se descartan los pares con NaN en los predictores (o en filtro_col, para comparar con las mismas filas)."""
    from lib.datos import con_fecha
    from lib.preparacion import Particion

    df = con_fecha(frame)
    P = df.loc[:, list(predictores)].to_numpy(dtype=float)
    F = df.loc[:, [filtro_col]].to_numpy(dtype=float) if filtro_col else np.zeros((len(df), 1))
    Y = df.loc[:, objetivo].to_numpy(dtype=float)
    fechas = df["fecha"].reset_index(drop=True)
    xs, ys, xd, yd = [], [], [], []
    for i in range(len(df) - h):
        a, b = fechas.iloc[i], fechas.iloc[i + h]
        if b != a + pd.DateOffset(months=h):
            raise ValueError(f"Par no consecutivo: {a} -> {b}")
        if not (np.isfinite(P[i]).all() and np.isfinite(F[i]).all()):
            continue
        xs.append(P[i]); ys.append(float(Y[i + h])); xd.append(a); yd.append(b)
    X, y = np.stack(xs).astype(float), np.asarray(ys, dtype=float)
    xd_s, yd_s = pd.Series(xd, name="x_fecha"), pd.Series(yd, name="fecha")
    if not ((yd_s.dt.year * 12 + yd_s.dt.month) - (xd_s.dt.year * 12 + xd_s.dt.month) == h).all():
        raise AssertionError("Fuga: algun par no tiene exactamente h meses entre predictores y objetivo")
    anio = yd_s.dt.year

    def parte(m):
        m = np.asarray(m)
        return Particion(None, None, X[m], y[m], yd_s[m].reset_index(drop=True), xd_s[m].reset_index(drop=True))

    return {"train": parte(anio <= ventana.anio_fin_train), "val": parte(anio == ventana.anio - 1), "test": parte(anio == ventana.anio)}


def correr_tabular(datos, c: str, ventana, familia: str, predictores, h: int = 1, semillas=tuple(range(10)),
                   filtro_y12: bool = False, nombre: str | None = None) -> tuple[pd.DataFrame, list[dict]]:
    """Ridge / ElasticNet (05_lineales.py) o XGB (06_xgb.py) con otro conjunto de predictores y/o horizonte h.

    Ridge/EN: X sin escalar -> EstandarizadorV3 del train; alpha (y l1) por MAE de validacion en la rejilla de v3.
    XGB: features escaladas con EscaladorVentana (train de la ventana), parametros oficiales, semillas 0..9.
    Devuelve predicciones de test (toneladas) e info por unidad."""
    from lib.modelos_lineales import EstandarizadorV3, predecir, seleccionar_por_validacion
    from lib.preparacion import EscaladorVentana

    nombre = nombre or familia
    y = f"produccion_t_{c}"
    serie = datos.serie(c)
    feats = datos.features(c, ventana.anio_fin_train)
    if col_y12(c) in predictores or filtro_y12:
        feats = con_y12(feats, serie, c, h)
    filtro = col_y12(c) if filtro_y12 else None
    filas, infos = [], []
    if familia in ("Ridge", "ElasticNet"):
        HPL = json.loads((BR / "01_configuracion" / "hiperparametros_congelados.json").read_text(encoding="utf-8"))["rejilla_v3_lineales"]
        p = pares_h(feats, predictores, y, ventana, h, filtro)
        sc = EstandarizadorV3().ajustar(p["train"].X)
        X = {k: sc.transformar(p[k].X) for k in ("train", "val", "test")}
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            mejor, _ = seleccionar_por_validacion(familia, X["train"], p["train"].y, X["val"], p["val"].y, HPL["alphas"], HPL["l1_ratios"])
        yp = predecir(mejor["b"], mejor["w"], X["test"])
        filas += [{"modelo": nombre, "cultivar": c, "anio_test": ventana.anio, "semilla": None, "particion": "test",
                   "fecha": f"{f:%Y-%m}", "x_fecha": f"{x:%Y-%m}", "y_true": float(a), "y_pred": float(b)}
                  for f, x, a, b in zip(p["test"].fechas_objetivo, p["test"].fechas_contexto_max, p["test"].y, yp)]
        infos.append({"modelo": nombre, "cultivar": c, "anio_test": ventana.anio, "alpha": mejor["alpha"], "l1_ratio": mejor["l1_ratio"],
                      "MAE_val": mejor["MAE_val"], "n_train": len(p["train"].y), "n_pred": len(predictores),
                      "train_objetivos": f"{p['train'].fechas_objetivo.min():%Y-%m}..{p['train'].fechas_objetivo.max():%Y-%m}"})
    else:
        from xgboost import XGBRegressor

        from v2_reentrenamiento.src.training.config_gc2_xgboost import OFFICIAL_GC2_XGB_CONFIG

        esc = EscaladorVentana(ventana)
        df = esc.ajustar_transformar(feats)
        p = pares_h(df, predictores, y, ventana, h, filtro)
        q = p["test"]
        for sem in semillas:
            m = XGBRegressor(**OFFICIAL_GC2_XGB_CONFIG.xgb_params(sem))
            m.fit(p["train"].X, p["train"].y)
            yt, yp = esc.invertir(y, q.y), esc.invertir(y, m.predict(q.X))
            filas += [{"modelo": nombre, "cultivar": c, "anio_test": ventana.anio, "semilla": sem, "particion": "test",
                       "fecha": f"{f:%Y-%m}", "x_fecha": f"{x:%Y-%m}", "y_true": float(a), "y_pred": float(b)}
                      for f, x, a, b in zip(q.fechas_objetivo, q.fechas_contexto_max, yt, yp)]
        infos.append({"modelo": nombre, "cultivar": c, "anio_test": ventana.anio, "n_train": len(p["train"].y), "n_pred": len(predictores),
                      "semillas": list(semillas),
                      "train_objetivos": f"{p['train'].fechas_objetivo.min():%Y-%m}..{p['train'].fechas_objetivo.max():%Y-%m}"})
    return pd.DataFrame(filas), infos


# ----------------------------------------------------------------------------- Chronos con la revision fijada (T9, T10)
class ChronosFijo:
    """Como lib/modelo_chronos.ChronosZeroShot, pero cargando la revision fijada en hiperparametros_congelados.json
    (snapshot del cache de Hugging Face), igual que 12_revision_g7/scripts/g7lib.correr_chronos."""

    def __init__(self) -> None:
        import os

        hp = json.loads((BR / "01_configuracion" / "hiperparametros_congelados.json").read_text(encoding="utf-8"))["chronos"]
        if os.environ.get("HF_HUB_OFFLINE") != "1":
            raise RuntimeError("HF_HUB_OFFLINE debe ser 1")
        vendor = str(RAIZ / hp["vendor"])
        if vendor not in sys.path:
            sys.path.insert(0, vendor)
        import torch
        from chronos import BaseChronosPipeline

        self.torch = torch
        torch.set_num_threads(int(hp["torch_threads"]))
        self.pipeline = BaseChronosPipeline.from_pretrained(hp["model_id"], revision=hp["snapshot"], device_map="cpu", torch_dtype=torch.float32)
        q = getattr(self.pipeline, "quantiles", None) or getattr(getattr(self.pipeline, "model", None), "quantiles", None)
        self.cuantiles = [float(x) for x in q]
        self.i_mediana = self.cuantiles.index(float(hp["cuantil"]))

    def cuantiles_h(self, contexto: np.ndarray, h: int) -> np.ndarray:
        """Cuantiles (todos los niveles) del paso h."""
        x = self.torch.tensor(np.asarray(contexto, dtype=float), dtype=self.torch.float32)
        with self.torch.inference_mode():
            arr = self.pipeline.predict(x, prediction_length=h).detach().cpu().numpy()
        return np.asarray(arr[0, :, h - 1] if arr.ndim == 3 else arr[:, h - 1], dtype=float)
