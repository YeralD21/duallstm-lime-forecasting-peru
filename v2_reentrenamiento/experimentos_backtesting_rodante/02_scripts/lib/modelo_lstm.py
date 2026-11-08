"""Una corrida GC3/GE (ventana, cultivar, modelo, semilla) con la arquitectura y callbacks oficiales.

Debe ejecutarse en un proceso nuevo: configure_determinism(seed) se llama ANTES de importar TensorFlow,
como en src/training/official_runner_gc3_ge.py:563-566. Prediccion con checkpoint_best.keras
(como auditorias/evaluar_test_gc3_ge.py:379-391) y desescalado con el scaler de la ventana.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
import pandas as pd


def entrenar_y_predecir(anio: int, cultivar: str, modelo: str, semilla: int, destino: Path) -> dict:
    from v2_reentrenamiento.src.training.determinism import configure_determinism

    determinismo = configure_determinism(semilla)

    from tensorflow import keras

    from lib.datos import ConstructorDatosVentana
    from lib.preparacion import EscaladorVentana, secuencias
    from lib.ventanas import Ventana
    from v2_reentrenamiento.src.models.dual_lstm_attention import EXPECTED_PARAMS, BahdanauAttention, build_gc3_ge_model
    from v2_reentrenamiento.src.models.features_gc3_ge import build_feature_spec
    from v2_reentrenamiento.src.training.callbacks_gc3_ge import build_callbacks
    from v2_reentrenamiento.src.training.config_gc3_ge import OFFICIAL_TRAINING_CONFIG as CFG

    v = Ventana(anio)
    if not v.viable(modelo):
        raise ValueError(f"{modelo} no aplica en {anio} (n_train={v.n_train(modelo)}).")
    datos = ConstructorDatosVentana()
    esc = EscaladorVentana(v)
    escalado = esc.ajustar_transformar(datos.features(cultivar, v.anio_fin_train))
    spec = build_feature_spec(cultivar, modelo)
    p = secuencias(escalado, spec.rama_a, spec.rama_b, spec.target, v, lookback=CFG.lookback)

    destino.mkdir(parents=True, exist_ok=True)
    red = build_gc3_ge_model(modelo, len(spec.rama_a), len(spec.rama_b))
    n_params = int(red.count_params())
    if n_params != EXPECTED_PARAMS[modelo]:
        raise ValueError(f"Parametros {n_params} != {EXPECTED_PARAMS[modelo]}")
    t0 = time.perf_counter()
    hist = red.fit([p["train"].X_a, p["train"].X_b], p["train"].y,
                   validation_data=([p["val"].X_a, p["val"].X_b], p["val"].y),
                   epochs=CFG.max_epochs, batch_size=CFG.batch_size, shuffle=CFG.shuffle,
                   callbacks=build_callbacks(destino), verbose=0)
    seg = time.perf_counter() - t0
    h = pd.DataFrame(hist.history)
    h.insert(0, "epoch", np.arange(1, len(h) + 1))
    h.to_csv(destino / "history.csv", index=False)
    mejor = keras.models.load_model(destino / "checkpoint_best.keras", custom_objects={"BahdanauAttention": BahdanauAttention}, compile=False)

    filas = []
    for parte in ("train", "val", "test"):
        q = p[parte]
        yp = mejor.predict([q.X_a, q.X_b], verbose=0).reshape(-1)
        for f, yt, yh in zip(q.fechas_objetivo, esc.invertir(spec.target, q.y), esc.invertir(spec.target, yp)):
            filas.append({"particion": parte, "fecha": f"{f:%Y-%m}", "y_true": float(yt), "y_pred": float(yh)})
    pred = pd.DataFrame(filas)
    pred.to_csv(destino / "predicciones.csv", index=False)
    estado = {"anio_test": anio, "cultivar": cultivar, "modelo": modelo, "semilla": semilla, "n_params": n_params,
              "n_train": int(len(p["train"].y)), "n_val": int(len(p["val"].y)), "fit_seconds": seg,
              "epocas_corridas": int(len(h)), "mejor_epoca": int(h.loc[h["val_loss"].idxmin(), "epoch"]),
              "determinismo": determinismo.__dict__, "scaler_fechas_ajuste": esc.fechas_ajuste}
    (destino / "estado_final.json").write_text(json.dumps(estado, indent=2, default=str), encoding="utf-8")
    return estado
