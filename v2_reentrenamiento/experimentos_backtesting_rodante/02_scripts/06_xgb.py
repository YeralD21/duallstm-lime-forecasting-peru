"""Etapa 06 (Fase C): XGB-37 y XGB-43 exploratorio (D-BR2), ventanas 2021-2025, semillas 0..9.

Configuracion oficial OFFICIAL_GC2_XGB_CONFIG.xgb_params(semilla), sin cambios. X e y escalados con el
StandardScaler ajustado en el TRAIN de la ventana; pares X_t -> y_(t+1); ajuste solo en TRAIN; predicciones
desescaladas a toneladas con el mismo scaler. XGB-43 = los 37 predictores + avg_sentiment_lag1/3/6 +
n_noticias_lag1/3/6 (extensiones_posthoc/xgboost_nlp/src/pipeline_xgb43.py:47-48), POST-HOC, fuera del ranking.

Una unidad por modelo, cultivo, ventana y semilla. Salidas en 04_modelos/xgb37|exploratorios/xgb43/<cultivo>/<anio>/seed_XX/:
predicciones.csv (train, val, test), info.json y model.ubj (excluido de git).

Uso:  python 06_xgb.py [--anios 2021 ...] [--cultivares sutil] [--modelos XGB-37 XGB-43] [--semillas 0 1] [--salida DIR]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.entorno import preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import argparse  # noqa: E402

import pandas as pd  # noqa: E402

from lib.datos import ConstructorDatosVentana  # noqa: E402
from lib.preparacion import EscaladorVentana, pares_tabulares  # noqa: E402
from lib.reanudacion import argumentos_comunes, correr_etapa, escribir_csv, escribir_json  # noqa: E402
from v2_reentrenamiento.src.models.features_gc2_xgboost import build_gc2_feature_spec  # noqa: E402
from v2_reentrenamiento.src.training.config_gc2_xgboost import OFFICIAL_GC2_XGB_CONFIG, validate_gc2_config  # noqa: E402

MODELOS = ("XGB-37", "XGB-43")
NLP_XGB43 = ("avg_sentiment_lag1", "avg_sentiment_lag3", "avg_sentiment_lag6", "n_noticias_lag1", "n_noticias_lag3", "n_noticias_lag6")
_datos: ConstructorDatosVentana | None = None
_preparado: dict = {}


def preparar(cultivar: str, v, modelo: str):
    """Escalado de la ventana y pares tabulares; se reutiliza entre semillas."""
    global _datos
    clave = (cultivar, v.anio, modelo)
    if clave not in _preparado:
        _datos = _datos or ConstructorDatosVentana()
        spec = build_gc2_feature_spec(cultivar)
        predictores = tuple(spec.predictors) + (NLP_XGB43 if modelo == "XGB-43" else ())
        esc = EscaladorVentana(v)
        escalado = esc.ajustar_transformar(_datos.features(cultivar, v.anio_fin_train))
        _preparado[clave] = (spec, predictores, esc, pares_tabulares(escalado, predictores, spec.target, v))
    return _preparado[clave]


def trabajo(u, v, tmp: Path) -> dict:
    import xgboost
    from xgboost import XGBRegressor

    validate_gc2_config(OFFICIAL_GC2_XGB_CONFIG)
    spec, predictores, esc, p = preparar(u.cultivar, v, u.modelo)
    if len(predictores) != {"XGB-37": 37, "XGB-43": 43}[u.modelo]:
        raise AssertionError(f"{u.nombre}: {len(predictores)} predictores.")
    params = OFFICIAL_GC2_XGB_CONFIG.xgb_params(u.semilla)
    modelo = XGBRegressor(**params)
    modelo.fit(p["train"].X, p["train"].y)
    filas = []
    for parte in ("train", "val", "test"):
        q = p[parte]
        yt, yp = esc.invertir(spec.target, q.y), esc.invertir(spec.target, modelo.predict(q.X))
        filas += [{"particion": parte, "fecha": f"{f:%Y-%m}", "x_fecha": f"{x:%Y-%m}", "y_true": float(a), "y_pred": float(b)}
                  for f, x, a, b in zip(q.fechas_objetivo, q.fechas_contexto_max, yt, yp)]
    pred = pd.DataFrame(filas)
    modelo.save_model(tmp / "model.ubj")
    escribir_csv(pred, tmp / "predicciones.csv")
    escribir_json({"unidad": u.__dict__, "ventana": v.como_dict(), "params": params, "xgboost": xgboost.__version__,
                   "predictores": list(predictores), "n": {k: int(len(p[k].y)) for k in ("train", "val", "test")},
                   "scaler_fechas_ajuste": esc.fechas_ajuste, "exploratorio_posthoc": u.modelo == "XGB-43"}, tmp / "info.json")
    return {"n_test": int((pred.particion == "test").sum())}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    argumentos_comunes(ap)
    correr_etapa("06_xgb", __file__, ap.parse_args(), MODELOS, MODELOS, trabajo)
