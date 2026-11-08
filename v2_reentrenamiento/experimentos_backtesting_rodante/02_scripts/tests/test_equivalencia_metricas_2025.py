"""Fase D1, paso previo: la ventana 2025 del backtesting reproduce las metricas oficiales de resultados_v2_final.

Modelos: GC3, GE y XGB-37 (por semilla, 0..9) y SARIMA rolling. Se recalculan con las predicciones de la Fase C y
las definiciones oficiales (src/evaluation/metrics_d35.py): MAE, RMSE, R2, MASE_1 y RMSSE_1 con los denominadores
D35 del manifest oficial, RelMAE_N1 con el Naive t-1 del mismo test, y MAE_shock/MAE_nonshock/Delta_s con los meses
de shock OFICIALES de 2025 (OFFICIAL_TEST_SHOCKS_2025), no con la mascara del backtesting.
Criterio: diferencia relativa <= 1e-6 en todas las metricas salvo Delta_s, y diferencia absoluta <= 1e-4 puntos
porcentuales en Delta_s (DESV-05: fijado despues de ver que Delta_s, cercano a 0, superaba 1e-6 relativo por la
diferencia conocida de float32 de GC3/GE; el veredicto con el criterio original tambien se guarda). Si falla, la Fase D1 no sigue.
Salidas: 06_metricas/reproducibilidad/metricas_2025_vs_oficial.csv y .json
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lib.entorno import BR, RAIZ_REPO, preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import json  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from lib.evaluacion import cargar_predicciones, errores_por_semilla, series  # noqa: E402
from lib.integridad import Integridad, sha256_normalizado  # noqa: E402
from lib.shocks import mascara  # noqa: E402
from lib.ventanas import Ventana  # noqa: E402
from v2_reentrenamiento.src.evaluation import metrics_d35 as d35  # noqa: E402

OF = RAIZ_REPO / "v2_reentrenamiento" / "resultados_v2_final"
ARCHIVOS = {
    "gc3_ge_test": OF / "evaluacion_test_gc3_ge" / "metricas_test_por_seed_gc3_ge.csv",
    "gc3_ge_manifest": OF / "evaluacion_test_gc3_ge" / "manifest_evaluacion_test_gc3_ge.json",
    "xgb_test": OF / "evaluacion_test_gc2_xgboost" / "metricas_test_por_seed_gc2_xgboost.csv",
    "xgb_shock": OF / "evaluacion_test_gc2_xgboost" / "metricas_shock_por_seed_gc2_xgboost.csv",
    "sarima_test": OF / "evaluacion_test_sarima_rolling" / "metricas_test_sarima_rolling.csv",
    "sarima_shock": OF / "evaluacion_test_sarima_rolling" / "metricas_shock_sarima_rolling.csv",
}
METRICAS = ("MAE", "RMSE", "R2", "MASE_1", "RMSSE_1", "RelMAE_N1", "MAE_shock", "MAE_nonshock", "Delta_s")
SAL = BR / "06_metricas" / "reproducibilidad"


def oficiales() -> pd.DataFrame:
    g = pd.read_csv(ARCHIVOS["gc3_ge_test"]).rename(columns={"modelo": "modelo"})
    g = g[["cultivar", "modelo", "seed", *[m for m in METRICAS if m in g.columns]]]
    x = pd.read_csv(ARCHIVOS["xgb_test"]).merge(pd.read_csv(ARCHIVOS["xgb_shock"]), on=["cultivar", "model", "seed"])
    x = x.assign(modelo="XGB-37")[["cultivar", "modelo", "seed", *[m for m in METRICAS if m in x.columns]]]
    s = pd.read_csv(ARCHIVOS["sarima_test"]).merge(pd.read_csv(ARCHIVOS["sarima_shock"]), on=["cultivar", "model"])
    s = s.assign(modelo="SARIMA", seed=-1)[["cultivar", "modelo", "seed", *[m for m in METRICAS if m in s.columns]]]
    return pd.concat([g, x, s], ignore_index=True)


def main() -> None:
    Integridad().verificar()
    man = json.loads(ARCHIVOS["gc3_ge_manifest"].read_text(encoding="utf-8"))
    dm, dr = man["d35_denominators"]["D_MASE1"], man["d35_denominators"]["D_RMSSE1"]
    shocks_of = man["shock_protocol"]["OFFICIAL_TEST_SHOCKS_2025"]
    s = series()
    es = errores_por_semilla(cargar_predicciones(), s)
    es = es[es.anio_test == 2025]
    filas = []
    for c in ("sutil", "dulce"):
        nv = es[(es.modelo == "Naive") & (es.cultivar == c)].sort_values("fecha")
        mae_naive = float(nv.ae.mean())
        for m in ("GC3", "GE", "XGB-37", "SARIMA"):
            sub = es[(es.modelo == m) & (es.cultivar == c)]
            for sem, g in sub.groupby(sub.semilla.fillna(-1)):
                g = g.sort_values("fecha")
                yt, yp = g.y_true.to_numpy(), g.y_pred.to_numpy()
                k = d35.conditional_shock_metrics(yt, yp, g.fecha.isin(shocks_of[c]).to_numpy())
                mae = d35.mae(yt, yp)
                rm = d35.rmse(yt, yp)
                filas.append({"cultivar": c, "modelo": m, "seed": int(sem), "MAE": mae, "RMSE": rm, "R2": d35.r2_score_d35(yt, yp),
                              "MASE_1": d35.mase1(mae, dm[c]), "RMSSE_1": d35.rmsse1(rm, dr[c]),
                              "RelMAE_N1": d35.relmae_n1(mae, mae_naive), "MAE_shock": k["MAE_shock"],
                              "MAE_nonshock": k["MAE_nonshock"], "Delta_s": k["Delta_s"], "MAE_Naive_t1": mae_naive})
    nuevo = pd.DataFrame(filas)
    of = oficiales()
    comp = nuevo.merge(of, on=["cultivar", "modelo", "seed"], suffixes=("", "_oficial"), validate="one_to_one")
    resumen = []
    for (c, m), g in comp.groupby(["cultivar", "modelo"], sort=False):
        fila = {"cultivar": c, "modelo": m, "n_corridas": len(g)}
        peor, peor_sin_ds = 0.0, 0.0
        for k in METRICAS:
            if f"{k}_oficial" not in g:
                continue
            dif = (g[k] - g[f"{k}_oficial"]).abs()
            rel = dif / g[f"{k}_oficial"].abs().clip(lower=1e-12)
            fila[f"maxdif_{k}"] = float(dif.max())
            peor = max(peor, float(rel.max()))
            if k != "Delta_s":
                peor_sin_ds = max(peor_sin_ds, float(rel.max()))
        fila["max_dif_relativa"] = peor
        fila["OK_criterio_original_rel_1e-6"] = peor <= 1e-6
        fila["OK"] = peor_sin_ds <= 1e-6 and fila["maxdif_Delta_s"] <= 1e-4
        resumen.append(fila)
    res = pd.DataFrame(resumen)
    # Informativo: mascara P75 del backtesting (historia hasta el origen) frente a los meses oficiales de 2025
    p75 = {c: list(mascara(s[c], Ventana(2025), "mensual", 75).meses_shock) for c in ("sutil", "dulce")}
    naive_of = pd.read_csv(ARCHIVOS["gc3_ge_test"]).groupby("cultivar")["MAE_Naive_t1"].first().to_dict()
    SAL.mkdir(parents=True, exist_ok=True)
    comp.to_csv(SAL / "metricas_2025_vs_oficial_por_corrida.csv", index=False, float_format="%.12g")
    res.to_csv(SAL / "metricas_2025_vs_oficial.csv", index=False, float_format="%.6g")
    info = {"OK": bool(res.OK.all()), "OK_criterio_original": bool(res["OK_criterio_original_rel_1e-6"].all()),
            "criterio": "relativa <= 1e-6 en cada metrica salvo Delta_s; Delta_s absoluta <= 1e-4 pp (DESV-05)",
            "meses_shock_oficiales_2025": shocks_of, "mascara_P75_backtesting_2025": p75,
            "coincide_mascara": {c: sorted(p75[c]) == sorted(shocks_of[c]) for c in p75},
            "MAE_Naive_t1": {c: {"nuevo": float(nuevo[nuevo.cultivar == c].MAE_Naive_t1.iloc[0]), "oficial": naive_of[c]} for c in p75},
            "sha256_archivos_oficiales": {k: sha256_normalizado(v) for k, v in ARCHIVOS.items()},
            "resumen": res.to_dict("records")}
    (SAL / "metricas_2025_vs_oficial.json").write_text(json.dumps(info, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({k: info[k] for k in ("OK", "OK_criterio_original", "meses_shock_oficiales_2025", "mascara_P75_backtesting_2025", "coincide_mascara", "MAE_Naive_t1")}, indent=1))
    print(res.to_string())
    if not info["OK"]:
        raise SystemExit("La ventana 2025 NO reproduce las metricas oficiales: se detiene la Fase D1.")


if __name__ == "__main__":
    main()
