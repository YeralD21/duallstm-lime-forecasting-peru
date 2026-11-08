"""Revision G7 - Fase 3. Codigo nuevo que reutiliza lib/ del pipeline sin modificarlo.

Experimentos:
  E1  reajuste final con train + validacion (datos hasta dic Y-1): Ridge-Y1, ElasticNet-Y1, XGB-37-Y1, SARIMA-Y1,
      SARIMA-sel-Y1, GC3-Y1, GE-Y1.
  E2  LSTM-U: una rama (arquitectura de la rama A de GC3) con 6 entradas; protocolo original y -Y1.
  E3  GC3-R: GC3 con objetivo r_t = y_t - y_(t-12) estandarizado con el train; protocolo original y -Y1.
  E4  Chronos-Bolt small y base, zero-shot (sensibilidad).

Este modulo NO importa TensorFlow al cargarse: las corridas LSTM llaman configure_determinism(semilla) antes.
"""
from __future__ import annotations

import json
import sys
import time
from dataclasses import dataclass
from pathlib import Path

G7 = Path(__file__).resolve().parents[1]
BR = G7.parent
LIB = BR / "02_scripts"
RAIZ = BR.parents[1]
for p in (str(RAIZ), str(LIB)):
    if p not in sys.path:
        sys.path.insert(0, p)

RES = G7 / "resultados"
UNI = RES / "unidades"
ORIG = BR / "04_modelos"
HP = json.loads((BR / "01_configuracion" / "hiperparametros_congelados.json").read_text(encoding="utf-8"))

VENTANAS_ENTRENADOS = (2021, 2022, 2023, 2024, 2025)
VENTANAS_CHRONOS = (2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025)
SEMILLAS = tuple(range(10))
CHRONOS_EXTRA = {
    "Chronos-small": ("amazon/chronos-bolt-small", "772f3d25d38aec6d914c8949dab4462e2d46f5d8"),
    "Chronos-base": ("amazon/chronos-bolt-base", "5d9f166d69f47aef3401367a7b842e78fe97b121"),
}
# modelo -> (familia, con_semilla, protocolo, base de la mejor epoca)
MODELOS = {
    "Ridge-Y1": ("lineal", False, "Y1", None),
    "ElasticNet-Y1": ("lineal", False, "Y1", None),
    "XGB-37-Y1": ("xgb", True, "Y1", None),
    "SARIMA-Y1": ("sarima", False, "Y1", None),
    "SARIMA-sel-Y1": ("sarima", False, "Y1", None),
    "GC3-Y1": ("lstm", True, "Y1", ("orig", "gc3_lstm_sin_nlp")),
    "GE-Y1": ("lstm", True, "Y1", ("orig", "ge_lstm_con_nlp")),
    "LSTM-U": ("lstm", True, "orig", None),
    "LSTM-U-Y1": ("lstm", True, "Y1", ("g7", "LSTM-U")),
    "GC3-R": ("lstm", True, "orig", None),
    "GC3-R-Y1": ("lstm", True, "Y1", ("g7", "GC3-R")),
    "Chronos-small": ("chronos", False, "zero-shot", None),
    "Chronos-base": ("chronos", False, "zero-shot", None),
}


@dataclass(frozen=True)
class VentanaY1:
    """Misma ventana de test Y, pero con 'train' = todo hasta dic Y-1 (E1). Interfaz compatible con lib/preparacion."""

    anio: int

    @property
    def origen(self) -> str:
        return f"{self.anio - 1}-12"

    @property
    def fin_train(self) -> str:
        return f"{self.anio - 1}-12"

    @property
    def anio_fin_train(self) -> int:
        return self.anio - 1

    @property
    def val(self) -> tuple[str, str]:  # no se usa para ajustar; se deja para la interfaz
        return (f"{self.anio - 1}-01", f"{self.anio - 1}-12")

    @property
    def test(self) -> tuple[str, str]:
        return (f"{self.anio}-01", f"{self.anio}-12")

    @property
    def meses_test(self) -> list[str]:
        return [f"{self.anio}-{m:02d}" for m in range(1, 13)]


def destino(modelo: str, cultivar: str, anio: int, semilla: int | None) -> Path:
    d = UNI / modelo / cultivar / str(anio)
    return d / f"seed_{semilla:02d}" if semilla is not None else d


def ventana(anio: int, protocolo: str):
    from lib.ventanas import Ventana

    return VentanaY1(anio) if protocolo == "Y1" else Ventana(anio)


def _filas(particion: str, fechas, y_true, y_pred, contexto=None) -> list[dict]:
    out = []
    for i, (f, a, b) in enumerate(zip(fechas, y_true, y_pred)):
        fila = {"particion": particion, "fecha": f"{f:%Y-%m}" if hasattr(f, "strftime") else str(f), "y_true": float(a), "y_pred": float(b)}
        if contexto is not None:
            fila["x_fecha"] = f"{contexto[i]:%Y-%m}"
        out.append(fila)
    return out


def _rango(fechas) -> list[str]:
    import pandas as pd

    s = pd.Series(list(fechas))
    return [f"{s.min():%Y-%m}", f"{s.max():%Y-%m}"] if len(s) else [None, None]


# ----------------------------------------------------------------------------- E1 tabulares
def correr_lineal(modelo: str, cultivar: str, anio: int):
    import pandas as pd

    from lib.datos import ConstructorDatosVentana
    from lib.modelos_lineales import EstandarizadorV3, elasticnet_sklearn, predecir, ridge_sklearn
    from lib.preparacion import pares_tabulares
    from v2_reentrenamiento.src.models.features_gc2_xgboost import gc2_predictors

    base = "ridge" if modelo == "Ridge-Y1" else "elasticnet"
    info0 = json.loads((ORIG / base / cultivar / str(anio) / "info.json").read_text(encoding="utf-8"))
    w = VentanaY1(anio)
    datos = ConstructorDatosVentana()
    feats = datos.features(cultivar, w.anio_fin_train)
    p = pares_tabulares(feats, gc2_predictors(cultivar), f"produccion_t_{cultivar}", w)
    sc = EstandarizadorV3().ajustar(p["train"].X)
    Xtr, Xte = sc.transformar(p["train"].X), sc.transformar(p["test"].X)
    b, wv = (ridge_sklearn(Xtr, p["train"].y, info0["alpha"]) if modelo == "Ridge-Y1"
             else elasticnet_sklearn(Xtr, p["train"].y, info0["alpha"], info0["l1_ratio"]))
    filas = _filas("test", p["test"].fechas_objetivo, p["test"].y, predecir(b, wv, Xte), p["test"].fechas_contexto_max)
    info = {"alpha": info0["alpha"], "l1_ratio": info0["l1_ratio"], "hiperparametros_de": f"04_modelos/{base}/{cultivar}/{anio}/info.json (validacion Y-1)",
            "pesos_geograficos_fin": datos.pesos(cultivar, w.anio_fin_train).tabla["periodo_fin"].iloc[0],
            "estandarizador_filas": int(len(p["train"].y)), "train_objetivos": _rango(p["train"].fechas_objetivo),
            "test_objetivos": _rango(p["test"].fechas_objetivo), "test_x_fecha": _rango(p["test"].fechas_contexto_max)}
    return pd.DataFrame(filas), info


def correr_xgb(cultivar: str, anio: int, semilla: int):
    import pandas as pd
    from xgboost import XGBRegressor

    from lib.datos import ConstructorDatosVentana
    from lib.preparacion import EscaladorVentana, pares_tabulares
    from v2_reentrenamiento.src.models.features_gc2_xgboost import build_gc2_feature_spec
    from v2_reentrenamiento.src.training.config_gc2_xgboost import OFFICIAL_GC2_XGB_CONFIG

    w = VentanaY1(anio)
    datos = ConstructorDatosVentana()
    spec = build_gc2_feature_spec(cultivar)
    esc = EscaladorVentana(w)
    esc_df = esc.ajustar_transformar(datos.features(cultivar, w.anio_fin_train))
    p = pares_tabulares(esc_df, spec.predictors, spec.target, w)
    m = XGBRegressor(**OFFICIAL_GC2_XGB_CONFIG.xgb_params(semilla))
    m.fit(p["train"].X, p["train"].y)
    q = p["test"]
    filas = _filas("test", q.fechas_objetivo, esc.invertir(spec.target, q.y), esc.invertir(spec.target, m.predict(q.X)), q.fechas_contexto_max)
    info = {"params": OFFICIAL_GC2_XGB_CONFIG.xgb_params(semilla), "scaler_fechas_ajuste": esc.fechas_ajuste,
            "pesos_geograficos_fin": datos.pesos(cultivar, w.anio_fin_train).tabla["periodo_fin"].iloc[0],
            "train_objetivos": _rango(p["train"].fechas_objetivo), "test_objetivos": _rango(q.fechas_objetivo),
            "test_x_fecha": _rango(q.fechas_contexto_max)}
    return pd.DataFrame(filas), info


# ----------------------------------------------------------------------------- E1 SARIMA
def correr_sarima(modelo: str, cultivar: str, anio: int):
    import numpy as np
    import pandas as pd

    from lib.datos import ConstructorDatosVentana
    from lib.modelos_series import _a_un_paso, _ajustar

    s = ConstructorDatosVentana().serie(cultivar).sort_index().astype(float)
    w = VentanaY1(anio)
    train = s[(s.index >= "2016-07") & (s.index <= w.fin_train)]
    if modelo == "SARIMA-Y1":
        cfg = HP["sarima_congelado"]
        o, so, op = cfg[cultivar]["order"], cfg[cultivar]["seasonal_order"], dict(cfg["opciones"])
        fuente = "hiperparametros_congelados.json: sarima_congelado"
    else:
        i0 = json.loads((ORIG / "sarima_sel" / cultivar / str(anio) / "info.json").read_text(encoding="utf-8"))
        o, so = i0["order"], i0["seasonal_order"]
        hp = HP["sarima_seleccion_por_ventana_DA9"]
        op = {**hp["opciones_ajuste"], "maxiter": hp["maxiter_candidatos_y_final"]}
        fuente = f"04_modelos/sarima_sel/{cultivar}/{anio}/info.json (orden elegido con train Y-2 y validacion Y-1)"
    fit, avisos = _ajustar(train.to_numpy(), o, so, op)
    p0 = np.asarray(fit.params, float).copy()
    filas, estado = _a_un_paso(fit, w.meses_test, [s[m] for m in w.meses_test])
    pred = pd.DataFrame([{"particion": "test", **f} for f in filas])
    info = {"order": list(o), "seasonal_order": list(so), "orden_de": fuente, "train_inicio": str(train.index.min()),
            "train_fin": str(train.index.max()), "n_train": int(len(train)), "avisos": avisos,
            "convergio": bool(fit.mle_retvals.get("converged", False)) if isinstance(fit.mle_retvals, dict) else None,
            "parametros_invariantes_en_test": bool(np.allclose(np.asarray(estado.params, float), p0, rtol=0, atol=1e-10))}
    return pred, info


# ----------------------------------------------------------------------------- E4 Chronos small/base
def correr_chronos(modelo: str, cultivar: str, anio: int):
    import os

    import numpy as np
    import pandas as pd

    from lib.datos import ConstructorDatosVentana
    from lib.entorno import RAIZ_REPO

    if os.environ.get("HF_HUB_OFFLINE") != "1":
        raise RuntimeError("HF_HUB_OFFLINE debe ser 1")
    vendor = str(RAIZ_REPO / HP["chronos"]["vendor"])
    if vendor not in sys.path:
        sys.path.insert(0, vendor)
    import torch
    from chronos import BaseChronosPipeline

    torch.set_num_threads(int(HP["chronos"]["torch_threads"]))
    mid, rev = CHRONOS_EXTRA[modelo]
    pipe = BaseChronosPipeline.from_pretrained(mid, revision=rev, device_map="cpu", torch_dtype=torch.float32)
    q = [float(x) for x in (getattr(pipe, "quantiles", None) or pipe.model.quantiles)]
    im = q.index(0.5)
    s = ConstructorDatosVentana().serie(cultivar)
    filas = []
    for m in [f"{anio}-{k:02d}" for k in range(1, 13)]:
        ctx = s[s.index < m]
        x = torch.tensor(np.asarray(ctx.to_numpy(), float), dtype=torch.float32)
        with torch.inference_mode():
            arr = pipe.predict(x, prediction_length=1).detach().cpu().numpy()
        yp = float(arr[0, im, 0] if arr.ndim == 3 else arr[im, 0])
        filas.append({"particion": "test", "fecha": m, "y_true": float(s[m]), "y_pred": yp,
                      "contexto_inicio": ctx.index[0], "contexto_fin": ctx.index[-1]})
    return pd.DataFrame(filas), {"model_id": mid, "revision": rev, "modulo_chronos": sys.modules["chronos"].__file__}


# ----------------------------------------------------------------------------- LSTM (E1, E2, E3)
LSTM_U_EXTRA = ("mes_sin", "mes_cos")


def construir_lstm_u(n_features: int):
    from tensorflow import keras
    from tensorflow.keras import layers

    from v2_reentrenamiento.src.models.dual_lstm_attention import (ATTENTION_UNITS, DENSE_UNITS, DROPOUT, LEARNING_RATE, LOOKBACK, LOSS,
                                                                  LSTM_UNITS, METRICS, BahdanauAttention)

    x_in = keras.Input(shape=(LOOKBACK, n_features), name="rama_a")
    h = layers.LSTM(LSTM_UNITS, return_sequences=True, name="lstm_a")(x_in)
    ctx = BahdanauAttention(ATTENTION_UNITS, name="attention_a")(h[:, -1, :], h)
    x = layers.Dense(DENSE_UNITS[0], activation="relu", name="dense_16")(ctx)
    x = layers.Dropout(DROPOUT, name="dropout_020")(x)
    x = layers.Dense(DENSE_UNITS[1], activation="relu", name="dense_8")(x)
    out = layers.Dense(1, name="output")(x)
    m = keras.Model(inputs=x_in, outputs=out, name="LSTM_U_BahdanauAttention")
    m.compile(optimizer=keras.optimizers.Adam(learning_rate=LEARNING_RATE), loss=LOSS, metrics=list(METRICS))
    return m


def parametros_lstm_u(n: int = 6) -> int:
    lstm = 4 * 16 * (n + 16 + 1)
    att = 2 * 16 * 16 + 16
    return lstm + att + (16 * 16 + 16) + (16 * 8 + 8) + (8 + 1)


def mejor_epoca_y_lr(base: tuple[str, str], cultivar: str, anio: int, semilla: int) -> tuple[int, list[float], str]:
    import pandas as pd

    tipo, nombre = base
    d = (ORIG / nombre / cultivar / str(anio) / f"seed_{semilla:02d}") if tipo == "orig" else destino(nombre, cultivar, anio, semilla)
    est = json.loads((d / "estado_final.json").read_text(encoding="utf-8")) if tipo == "orig" else json.loads((d / "info.json").read_text(encoding="utf-8"))
    h = pd.read_csv(d / "history.csv")
    e = int(est["mejor_epoca"])
    if int(h.loc[h["val_loss"].idxmin(), "epoch"]) != e:
        raise AssertionError(f"mejor_epoca de {d} no coincide con argmin(val_loss)")
    return e, [float(x) for x in h["learning_rate"].iloc[:e]], str(d.relative_to(BR))


def correr_lstm(modelo: str, cultivar: str, anio: int, semilla: int, carpeta: Path):
    """Debe llamarse en un proceso nuevo DESPUES de configure_determinism(semilla)."""
    import numpy as np
    import pandas as pd
    from tensorflow import keras

    from lib.datos import ConstructorDatosVentana
    from lib.preparacion import EscaladorVentana, secuencias
    from v2_reentrenamiento.src.models.dual_lstm_attention import EXPECTED_PARAMS, BahdanauAttention, build_gc3_ge_model
    from v2_reentrenamiento.src.models.features_gc3_ge import build_feature_spec
    from v2_reentrenamiento.src.training.callbacks_gc3_ge import build_callbacks
    from v2_reentrenamiento.src.training.config_gc3_ge import OFFICIAL_TRAINING_CONFIG as CFG

    fam, _, protocolo, base = MODELOS[modelo]
    raiz = modelo.replace("-Y1", "")
    w = ventana(anio, protocolo)
    datos = ConstructorDatosVentana()
    serie = datos.serie(cultivar)
    feats = datos.features(cultivar, w.anio_fin_train)
    esc = EscaladorVentana(w)
    df = esc.ajustar_transformar(feats)
    target_y = f"produccion_t_{cultivar}"
    if raiz in ("GC3", "GE", "GC3-R"):
        spec = build_feature_spec(cultivar, "GE" if raiz == "GE" else "GC3")
        rama_a, rama_b = spec.rama_a, spec.rama_b
    else:  # LSTM-U
        spec = build_feature_spec(cultivar, "GC3")
        rama_a = tuple(spec.rama_a) + LSTM_U_EXTRA
        rama_b = rama_a
    info_obj = {}
    if raiz == "GC3-R":
        clave = df["año"].astype(int).astype(str) + "-" + df["mes"].astype(int).map("{:02d}".format)
        y12 = clave.map(lambda f: serie.get(str(pd.Period(f, "M") - 12), np.nan))
        r = clave.map(serie) - y12
        en_train = (clave >= "2017-01") & (clave <= w.fin_train)
        mu, sd = float(r[en_train].mean()), float(r[en_train].std(ddof=0))
        df["r12_esc"] = (r - mu) / sd
        objetivo = "r12_esc"
        info_obj = {"objetivo": "r_t = y_t - y_(t-12) estandarizado", "r_media_train": mu, "r_sd_train": sd,
                    "r_estadisticas_meses": [str(clave[en_train].min()), str(clave[en_train].max())]}
    else:
        objetivo = target_y
    p = secuencias(df, rama_a, rama_b, objetivo, w, lookback=CFG.lookback)
    if raiz == "LSTM-U":
        red = construir_lstm_u(len(rama_a))
        n_esp = parametros_lstm_u(len(rama_a))
        X = {k: p[k].X_a for k in p}
    else:
        red = build_gc3_ge_model("GE" if raiz == "GE" else "GC3", len(rama_a), len(rama_b))
        n_esp = EXPECTED_PARAMS["GE" if raiz == "GE" else "GC3"]
        X = {k: [p[k].X_a, p[k].X_b] for k in p}
    n_params = int(red.count_params())
    if n_params != n_esp:
        raise ValueError(f"parametros {n_params} != {n_esp}")
    carpeta.mkdir(parents=True, exist_ok=True)
    t0 = time.perf_counter()
    if protocolo == "orig":
        hist = red.fit(X["train"], p["train"].y, validation_data=(X["val"], p["val"].y), epochs=CFG.max_epochs, batch_size=CFG.batch_size,
                       shuffle=CFG.shuffle, callbacks=build_callbacks(carpeta), verbose=0)
        red = keras.models.load_model(carpeta / "checkpoint_best.keras", custom_objects={"BahdanauAttention": BahdanauAttention}, compile=False)
        h = pd.DataFrame(hist.history)
        h.insert(0, "epoch", np.arange(1, len(h) + 1))
        mejor = int(h.loc[h["val_loss"].idxmin(), "epoch"])
        extra = {"mejor_epoca": mejor, "epocas_corridas": int(len(h))}
        partes = ("train", "val", "test")
    else:
        e, lrs, fuente = mejor_epoca_y_lr(base, cultivar, anio, semilla)
        sched = keras.callbacks.LearningRateScheduler(lambda ep, lr: lrs[ep])
        hist = red.fit(X["train"], p["train"].y, epochs=e, batch_size=CFG.batch_size, shuffle=CFG.shuffle, callbacks=[sched], verbose=0)
        h = pd.DataFrame(hist.history)
        h.insert(0, "epoch", np.arange(1, len(h) + 1))
        extra = {"epocas_fijas": e, "epocas_de": fuente, "lr_por_epoca_de": fuente + "/history.csv (columna learning_rate)",
                 "lr_primera_ultima": [lrs[0], lrs[-1]]}
        partes = ("train", "test")
    seg = time.perf_counter() - t0
    h.to_csv(carpeta / "history.csv", index=False)
    filas = []
    for parte in partes:
        q = p[parte]
        yhat = red.predict(X[parte], verbose=0).reshape(-1)
        fechas = [f"{f:%Y-%m}" for f in q.fechas_objetivo]
        y_true = np.array([serie[f] for f in fechas])
        if raiz == "GC3-R":
            base12 = np.array([serie[str(pd.Period(f, "M") - 12)] for f in fechas])
            y_pred = base12 + yhat * info_obj["r_sd_train"] + info_obj["r_media_train"]
        else:
            y_pred = esc.invertir(target_y, yhat)
        filas += _filas(parte, q.fechas_objetivo, y_true, y_pred, q.fechas_contexto_max)
    pred = pd.DataFrame(filas)
    info = {"n_params": n_params, "entradas_rama_a": list(rama_a), "entradas_rama_b": list(rama_b) if raiz != "LSTM-U" else None,
            "protocolo": protocolo, "scaler_fechas_ajuste": esc.fechas_ajuste,
            "pesos_geograficos_fin": datos.pesos(cultivar, w.anio_fin_train).tabla["periodo_fin"].iloc[0],
            "train_objetivos": _rango(p["train"].fechas_objetivo), "train_contexto_max": _rango(p["train"].fechas_contexto_max),
            "val_objetivos": _rango(p["val"].fechas_objetivo) if protocolo == "orig" else None,
            "test_objetivos": _rango(p["test"].fechas_objetivo), "test_contexto_max": _rango(p["test"].fechas_contexto_max),
            "fit_seconds": seg, **extra, **info_obj}
    for f in carpeta.glob("checkpoint_best.keras"):
        f.unlink()  # pesos no se versionan (regenerables)
    return pred, info
