"""Fase B: mide tiempos de SARIMA (congelado y rejilla DA9), Ridge, ElasticNet, XGB-37 y bootstrap.

No guarda predicciones. Salida: 10_logs/verificaciones/tiempos_fase_b.json
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lib.entorno import BR, CONFIG, preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import itertools  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402
import warnings  # noqa: E402

import numpy as np  # noqa: E402

from lib.datos import ConstructorDatosVentana  # noqa: E402
from lib.integridad import Integridad  # noqa: E402
from lib.metricas import bootstrap_pareado  # noqa: E402
from lib.modelos_lineales import EstandarizadorV3, elasticnet_sklearn, ridge_sklearn  # noqa: E402
from lib.modelos_series import sarima_rolling  # noqa: E402
from lib.preparacion import EscaladorVentana, pares_tabulares  # noqa: E402
from lib.ventanas import VENTANAS_RANKING, Ventana  # noqa: E402

HP = json.loads((CONFIG / "hiperparametros_congelados.json").read_text(encoding="utf-8"))
SAL = BR / "10_logs" / "verificaciones" / "tiempos_fase_b.json"


def cronometrar(fn, repeticiones: int = 1) -> float:
    t0 = time.perf_counter()
    for _ in range(repeticiones):
        fn()
    return (time.perf_counter() - t0) / repeticiones


def main() -> None:
    Integridad().verificar()
    from statsmodels.tsa.statespace.sarimax import SARIMAX
    from v2_reentrenamiento.src.models.features_gc2_xgboost import build_gc2_feature_spec
    from v2_reentrenamiento.src.training.config_gc2_xgboost import OFFICIAL_GC2_XGB_CONFIG
    from xgboost import XGBRegressor

    datos = ConstructorDatosVentana()
    rep: dict = {}
    # SARIMA congelado en las 5 ventanas del ranking
    sar = {}
    for c in ("sutil", "dulce"):
        for a in VENTANAS_RANKING:
            v = Ventana(a)
            sar[f"{c}/{a}"] = cronometrar(lambda: sarima_rolling(datos.serie(c), v, HP["sarima_congelado"][c]["order"], HP["sarima_congelado"][c]["seasonal_order"]))
    rep["sarima_congelado_segundos"] = {"por_ventana": sar, "total_10": float(sum(sar.values()))}
    # Rejilla DA9: muestra determinista de 24 de las 576 combinaciones, maxiter=200 (02_gc1 celda 7)
    g = HP["sarima_seleccion_por_ventana_DA9"]["rejilla"]
    combos = list(itertools.product(g["p"], g["d"], g["q"], g["P"], g["D"], g["Q"]))
    muestra = combos[::24]
    rejilla = {}
    for c in ("sutil", "dulce"):
        for a in (2021, 2025):
            v = Ventana(a)
            s = datos.serie(c)
            y = s[(s.index >= "2016-07") & (s.index <= v.fin_train)].to_numpy()
            tiempos = []
            for p, d, q, P, D, Q in muestra:
                t0 = time.perf_counter()
                try:
                    with warnings.catch_warnings():
                        warnings.simplefilter("ignore")
                        SARIMAX(y, order=(p, d, q), seasonal_order=(P, D, Q, 12), enforce_stationarity=False, enforce_invertibility=False,
                                initialization="approximate_diffuse", trend="c").fit(disp=False, maxiter=200)
                except Exception:
                    pass
                tiempos.append(time.perf_counter() - t0)
            rejilla[f"{c}/{a}"] = {"n_muestra": len(muestra), "media_s": float(np.mean(tiempos)), "estimado_576_s": float(np.mean(tiempos) * len(combos))}
    est = float(np.mean([r["estimado_576_s"] for r in rejilla.values()]))
    rep["sarima_rejilla_DA9"] = {"muestra": rejilla, "estimado_por_ventana_cultivar_s": est, "estimado_10_ventana_cultivar_min": est * 10 / 60}
    # Ridge, ElasticNet y XGB-37 (un ajuste en la ventana 2025)
    v = Ventana(2025)
    lin, xgb = {}, {}
    for c in ("sutil", "dulce"):
        feats = datos.features(c, v.anio_fin_train)
        spec = build_gc2_feature_spec(c)
        pt = pares_tabulares(feats, spec.predictors, spec.target, v)
        sc = EstandarizadorV3().ajustar(pt["train"].X)
        Xt = sc.transformar(pt["train"].X)
        lin[f"ridge/{c}"] = cronometrar(lambda: ridge_sklearn(Xt, pt["train"].y, HP["ridge"]["control_2025_v3"][c]["alpha"]), 20)
        lin[f"elasticnet/{c}"] = cronometrar(lambda: elasticnet_sklearn(Xt, pt["train"].y, HP["elasticnet"]["control_2025_v3"][c]["alpha"], HP["elasticnet"]["control_2025_v3"][c]["l1_ratio"]), 20)
        esc = EscaladorVentana(v)
        pe = pares_tabulares(esc.ajustar_transformar(feats), spec.predictors, spec.target, v)
        xgb[c] = cronometrar(lambda: XGBRegressor(**OFFICIAL_GC2_XGB_CONFIG.xgb_params(0)).fit(pe["train"].X, pe["train"].y), 3)
    rep["lineales_segundos_por_ajuste"] = lin
    rep["xgb37_segundos_por_ajuste"] = xgb
    # Bootstrap B=10000: 11 modelos x 60 meses (5 ventanas x 12), estratificado por ventana
    rng = np.random.default_rng(0)
    errores = {f"m{k}": rng.gamma(2.0, 1000.0, 60) for k in range(11)}
    estratos = np.repeat(np.arange(5), 12)
    t_boot = cronometrar(lambda: bootstrap_pareado(errores, estratos, B=10000, semilla=42))
    errores_s = {k: v_[:15] for k, v_ in errores.items()}
    t_boot_s = cronometrar(lambda: bootstrap_pareado(errores_s, np.repeat(np.arange(5), 3), B=10000, semilla=42))
    n_llamadas = 2 * 2 * 19 * 3 * 3  # cultivares x tipos x percentiles x (global, shock, normal) x (principal, bloques, 2023-2025)
    rep["bootstrap"] = {"segundos_por_llamada_60_meses_11_modelos": t_boot, "segundos_por_llamada_15_meses": t_boot_s,
                        "llamadas_estimadas_fase_D": n_llamadas, "estimado_fase_D_min": n_llamadas * t_boot / 60}
    SAL.write_text(json.dumps(rep, indent=2), encoding="utf-8")
    print(json.dumps(rep, indent=2))


if __name__ == "__main__":
    main()
