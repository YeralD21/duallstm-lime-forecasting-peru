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


def _pronostico_ets(y_hasta: np.ndarray, spec: dict, params: np.ndarray) -> float:
    from statsmodels.tsa.exponential_smoothing.ets import ETSModel

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        r = ETSModel(y_hasta, seasonal_periods=PERIODO, initialization_method="estimated", **spec).smooth(params)
        return float(np.asarray(r.forecast(1), dtype=float)[0])


def ets_rolling(serie: pd.Series, ventana) -> tuple[pd.DataFrame, dict, pd.DataFrame]:
    """Seleccion por AICc en train entre las 12 especificaciones; val y test a 1 paso con parametros fijos."""
    s, train, val = particiones(serie, ventana)
    y = train.to_numpy()
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

    def pronostico(self) -> float:
        h = 1 / self.alpha - (1 - self.alpha) ** self.n / self.alpha if self.alpha > 0 else 0.0
        f = 0.5 * self.b0 * h + self.nivel
        if self.desestacionaliza:
            f = f * self._factor(self.n) if self.metodo.startswith("mul") else f + self._factor(self.n)
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
