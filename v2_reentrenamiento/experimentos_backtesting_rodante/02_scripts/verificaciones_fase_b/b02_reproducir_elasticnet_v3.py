"""Fase B: ElasticNet.

Paso 1 (validar el pipeline): protocolo v3 = rejilla alpha x l1 (config_robustez.json), seleccion por MAE en VAL 2024,
        reajuste con train+val y nuevo estandarizador, test 2025. Con sklearn y con el port exacto de v3.
        Se compara con lo registrado (Sutil 3117.64, Dulce 39.70) y con los coeficientes de v3.
Paso 2 (version nueva, DA4): alpha/l1 de v3 (control_2025_v3; DESV-03), ajuste final solo con TRAIN, test 2025.
Salidas: 06_metricas/reproducibilidad/elasticnet_*.csv/.json
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lib.entorno import BR, CONFIG, preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from lib.datos import ConstructorDatosVentana, ruta  # noqa: E402
from lib.integridad import Integridad  # noqa: E402
from lib.metricas import condicionales  # noqa: E402
from lib.modelos_lineales import EstandarizadorV3, elasticnet_sklearn, elasticnet_v3, predecir  # noqa: E402
from lib.preparacion import pares_tabulares  # noqa: E402
from lib.shocks import mascara  # noqa: E402
from lib.ventanas import Ventana  # noqa: E402
from v2_reentrenamiento.src.models.features_gc2_xgboost import gc2_predictors  # noqa: E402

SAL = BR / "06_metricas" / "reproducibilidad"
HP = json.loads((CONFIG / "hiperparametros_congelados.json").read_text(encoding="utf-8"))
REGISTRADO = {"sutil": 3117.6377232467908, "dulce": 39.696222627495665}
MESES_OFICIALES = {"sutil": ("2025-01", "2025-07", "2025-11"), "dulce": ("2025-01", "2025-02", "2025-03")}


def mae(a, b) -> float:
    return float(np.mean(np.abs(np.asarray(a) - np.asarray(b))))


def protocolo_v3(parts, ajustar) -> dict:
    tr, va, te = parts["train"], parts["val"], parts["test"]
    sc = EstandarizadorV3().ajustar(tr.X)
    mejor = None
    for a in HP["rejilla_v3_lineales"]["alphas"]:
        for l1 in HP["rejilla_v3_lineales"]["l1_ratios"]:
            b, w = ajustar(sc.transformar(tr.X), tr.y, a, l1)
            s = mae(va.y, predecir(b, w, sc.transformar(va.X)))
            if mejor is None or s < mejor["score_val"]:
                mejor = {"alpha": a, "l1": l1, "score_val": s, "b_train": [b, *w.tolist()]}
    Xtv, ytv = np.vstack([tr.X, va.X]), np.concatenate([tr.y, va.y])
    sc2 = EstandarizadorV3().ajustar(Xtv)
    b2, w2 = ajustar(sc2.transformar(Xtv), ytv, mejor["alpha"], mejor["l1"])
    mejor["pred_test"] = predecir(b2, w2, sc2.transformar(te.X))
    return mejor


def main() -> None:
    Integridad().verificar()
    datos = ConstructorDatosVentana()
    v = Ventana(2025)
    v3 = pd.read_csv(ruta("metricas_v3", oficial=True))
    res, filas_pred = {}, []
    for c in ("sutil", "dulce"):
        feats = datos.features(c, v.anio_fin_train)  # sin escalar: y en toneladas
        parts = pares_tabulares(feats, gc2_predictors(c), f"produccion_t_{c}", v)
        fila_v3 = v3[(v3.dataset == "TEST_2025") & (v3.cultivar == c) & (v3.model == "ElasticNet")].iloc[0]
        sel_v3 = json.loads(fila_v3.selection)
        meses = parts["test"].fechas_objetivo.dt.strftime("%Y-%m").to_numpy()
        r = {"registrado_v3": {"MAE": float(fila_v3.MAE_global), "alpha": sel_v3["a"], "l1": sel_v3["l1"], "score_val": sel_v3["score"]}}
        for nombre, fn in (("sklearn_protocolo_v3", elasticnet_sklearn), ("port_v3_protocolo_v3", elasticnet_v3)):
            t0 = time.perf_counter()
            m = protocolo_v3(parts, fn)
            seg = time.perf_counter() - t0
            ae = pd.Series(np.abs(parts["test"].y - m["pred_test"]), index=meses)
            r[nombre] = {"alpha": m["alpha"], "l1": m["l1"], "score_val": m["score_val"], "MAE_test": float(ae.mean()),
                         "dif_MAE_vs_registrado": float(ae.mean() - REGISTRADO[c]),
                         "max_abs_dif_coef_train_vs_v3": float(np.max(np.abs(np.array(m["b_train"]) - np.array(sel_v3["b"])))),
                         "segundos_rejilla_completa": seg, **{k: v_ for k, v_ in condicionales(ae, MESES_OFICIALES[c]).items() if k in ("MAE_shock", "Delta_s")}}
            filas_pred += [{"cultivar": c, "version": nombre, "fecha": f, "y_true": yt, "y_pred": yp}
                           for f, yt, yp in zip(meses, parts["test"].y, m["pred_test"])]
        # Paso 2: version nueva (DA4): hiperparametros congelados, ajuste final solo con TRAIN
        hp = HP["elasticnet"]["control_2025_v3"][c]  # DESV-03: clave tras la revision de DA4
        t0 = time.perf_counter()
        sc = EstandarizadorV3().ajustar(parts["train"].X)
        b, w = elasticnet_sklearn(sc.transformar(parts["train"].X), parts["train"].y, hp["alpha"], hp["l1_ratio"])
        pred = predecir(b, w, sc.transformar(parts["test"].X))
        seg = time.perf_counter() - t0
        ae = pd.Series(np.abs(parts["test"].y - pred), index=meses)
        mk = mascara(datos.serie(c), v, "mensual", 75)
        r["nueva_DA4_solo_train"] = {"alpha": hp["alpha"], "l1": hp["l1_ratio"], "MAE_test": float(ae.mean()),
                                     "dif_MAE_vs_registrado_v3": float(ae.mean() - REGISTRADO[c]),
                                     "dif_MAE_vs_sklearn_protocolo_v3": float(ae.mean() - r["sklearn_protocolo_v3"]["MAE_test"]),
                                     "segundos_un_ajuste": seg,
                                     "mascara_P75_hasta_origen": list(mk.meses_shock),
                                     **{k: v_ for k, v_ in condicionales(ae, mk.meses_shock).items() if k in ("MAE_shock", "MAE_normal", "Delta_s")}}
        filas_pred += [{"cultivar": c, "version": "nueva_DA4_solo_train", "fecha": f, "y_true": yt, "y_pred": yp}
                       for f, yt, yp in zip(meses, parts["test"].y, pred)]
        res[c] = r
    SAL.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(filas_pred).to_csv(SAL / "elasticnet_predicciones_2025.csv", index=False)
    (SAL / "elasticnet_reproduccion.json").write_text(json.dumps(res, indent=2), encoding="utf-8")
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
