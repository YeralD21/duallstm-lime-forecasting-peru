"""Etapa 05 (Fase C): Ridge y ElasticNet (D-BR2, DA4 revisada), ventanas 2021-2025.

En cada ventana: 37 predictores de XGB-37 sin escalar, X estandarizado con media y desviacion poblacional del
TRAIN, y en toneladas. Cada candidato de la rejilla de v3 se ajusta solo con TRAIN y se elige el de menor MAE de
validacion (Y-1); el modelo final es ese ajuste en TRAIN (sin reajuste con validacion).
En la ventana 2025 se agrega el control preregistrado contra los valores de v3: si coinciden con los elegidos y
la diferencia de MAE de test.

Una unidad por modelo, cultivo y ventana. Salidas en 04_modelos/ridge|elasticnet/<cultivo>/<anio>/:
predicciones.csv (train, val, test), rejilla.csv (MAE de validacion de cada candidato) e info.json.

Uso:  python 05_lineales.py [--anios 2021 ...] [--cultivares sutil] [--modelos Ridge ElasticNet] [--salida DIR]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.entorno import CONFIG, preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import argparse  # noqa: E402
import json  # noqa: E402
import warnings  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from lib.datos import ConstructorDatosVentana  # noqa: E402
from lib.modelos_lineales import EstandarizadorV3, elasticnet_sklearn, predecir, ridge_sklearn, seleccionar_por_validacion  # noqa: E402
from lib.preparacion import pares_tabulares  # noqa: E402
from lib.reanudacion import argumentos_comunes, correr_etapa, escribir_csv, escribir_json  # noqa: E402
from v2_reentrenamiento.src.models.features_gc2_xgboost import gc2_predictors  # noqa: E402

MODELOS = ("Ridge", "ElasticNet")
HP = json.loads((CONFIG / "hiperparametros_congelados.json").read_text(encoding="utf-8"))
_datos: ConstructorDatosVentana | None = None


def trabajo(u, v, tmp: Path) -> dict:
    global _datos
    _datos = _datos or ConstructorDatosVentana()
    feats = _datos.features(u.cultivar, v.anio_fin_train)
    p = pares_tabulares(feats, gc2_predictors(u.cultivar), f"produccion_t_{u.cultivar}", v)
    sc = EstandarizadorV3().ajustar(p["train"].X)
    X = {k: sc.transformar(p[k].X) for k in ("train", "val", "test")}
    rejilla = HP["rejilla_v3_lineales"]
    with warnings.catch_warnings(record=True) as avisos:
        warnings.simplefilter("always")
        mejor, tabla = seleccionar_por_validacion(u.modelo, X["train"], p["train"].y, X["val"], p["val"].y,
                                                  rejilla["alphas"], rejilla["l1_ratios"])
    filas = []
    for parte in ("train", "val", "test"):
        yp = predecir(mejor["b"], mejor["w"], X[parte])
        filas += [{"particion": parte, "fecha": f"{f:%Y-%m}", "y_true": float(yt), "y_pred": float(yh)}
                  for f, yt, yh in zip(p[parte].fechas_objetivo, p[parte].y, yp)]
    pred = pd.DataFrame(filas)
    t = pred[pred.particion == "test"]
    mae_test = float(np.mean(np.abs(t.y_true - t.y_pred)))
    info = {"unidad": u.__dict__, "ventana": v.como_dict(), "alpha": mejor["alpha"], "l1_ratio": mejor["l1_ratio"],
            "MAE_val_elegido": mejor["MAE_val"], "orden_rejilla_elegido": mejor["orden_rejilla"],
            "n": {k: int(len(p[k].y)) for k in ("train", "val", "test")},
            "train_objetivos": [f"{p['train'].fechas_objetivo.min():%Y-%m}", f"{p['train'].fechas_objetivo.max():%Y-%m}"],
            "intercepto": mejor["b"], "coeficientes": dict(zip(gc2_predictors(u.cultivar), mejor["w"].tolist())),
            "avisos": sorted({a.category.__name__ for a in avisos}), "n_avisos": len(avisos)}
    if v.anio == 2025:
        clave = "ridge" if u.modelo == "Ridge" else "elasticnet"
        ctl = HP[clave]["control_2025_v3"][u.cultivar]
        b, w = (ridge_sklearn(X["train"], p["train"].y, ctl["alpha"]) if u.modelo == "Ridge"
                else elasticnet_sklearn(X["train"], p["train"].y, ctl["alpha"], ctl["l1_ratio"]))
        mae_ctl = float(np.mean(np.abs(p["test"].y - predecir(b, w, X["test"]))))
        info["control_2025_v3"] = {"valores_v3": ctl, "coincide_con_elegido": ctl["alpha"] == mejor["alpha"]
                                   and ctl.get("l1_ratio") == mejor["l1_ratio"],
                                   "MAE_test_con_valores_v3": mae_ctl, "MAE_test_elegido_menos_v3": mae_test - mae_ctl}
    escribir_csv(pred, tmp / "predicciones.csv")
    escribir_csv(pd.DataFrame(tabla), tmp / "rejilla.csv")
    escribir_json(info, tmp / "info.json")
    elegido = f"a={mejor['alpha']}" + (f",l1={mejor['l1_ratio']}" if mejor["l1_ratio"] is not None else "")
    return {"elegido": elegido, "MAE_val": round(mejor["MAE_val"], 4)}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    argumentos_comunes(ap)
    correr_etapa("05_lineales", __file__, ap.parse_args(), MODELOS, (), trabajo)
