"""Prueba P0: con la mascara P0 (todos los meses son shock) Delta_s debe ser exactamente 0 en todos los modelos.

Usa (1) predicciones reales ya guardadas en Fase B y oficiales de TEST 2025, y (2) predicciones sinteticas
en todas las ventanas y cultivares, mensual e interanual, para recorrer la ruta de codigo completa.
Escribe 10_logs/verificaciones/p0.json.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lib.entorno import BR, preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import json  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from lib.datos import CULTIVARES, ConstructorDatosVentana, ruta  # noqa: E402
from lib.metricas import condicionales, error_abs_promedio  # noqa: E402
from lib.shocks import mascara  # noqa: E402
from lib.ventanas import Ventana, todas  # noqa: E402

SAL = BR / "10_logs" / "verificaciones" / "p0.json"


def predicciones_reales_2025() -> dict[tuple[str, str], pd.DataFrame]:
    out = {}
    mini = pd.read_csv(BR / "10_logs" / "verificaciones" / "fase_b" / "mini_corrida_predicciones.csv")
    for (m, c), g in mini.groupby(["modelo", "cultivar"]):
        out[(f"{m} (Fase B)", c)] = g[["fecha", "seed", "y_true", "y_pred"]]
    gc = pd.read_csv(ruta("pred_gc3_ge_2025", oficial=True))
    for (m, c), g in gc.groupby(["modelo", "cultivar"]):
        out[(f"{m} oficial 10 seeds", c)] = pd.DataFrame({"fecha": g.fecha.str[:7], "seed": g.seed, "y_true": g.y_true_ton, "y_pred": g.y_pred_ton})
    xg = pd.read_csv(ruta("pred_xgb37_2025", oficial=True))
    for c, g in xg.groupby("cultivar"):
        out[("XGB-37 oficial 10 seeds", c)] = pd.DataFrame({"fecha": g.date, "seed": g.seed, "y_true": g.y_true_ton, "y_pred": g.y_pred_ton})
    ch = pd.read_csv(BR / "06_metricas" / "reproducibilidad" / "chronos_v4_reproduccion.csv")
    for c, g in ch.groupby("cultivar"):
        out[("Chronos (Fase B)", c)] = pd.DataFrame({"fecha": g.fecha, "seed": 0, "y_true": g.y_true, "y_pred": g.y_pred_nuevo})
    return out


def main() -> None:
    datos = ConstructorDatosVentana()
    rep = {"reales_2025": {}, "sinteticos": {}}
    fallos = []
    v25 = Ventana(2025)
    for (m, c), pred in predicciones_reales_2025().items():
        mk = mascara(datos.serie(c), v25, "mensual", 0)
        r = condicionales(error_abs_promedio(pred), mk.meses_shock)
        rep["reales_2025"][f"{m}/{c}"] = {"n_shock": r["n_shock"], "Delta_s": r["Delta_s"]}
        if r["Delta_s"] != 0.0 or r["n_shock"] != 12:
            fallos.append(f"{m}/{c}: Delta_s={r['Delta_s']} n_shock={r['n_shock']}")
    rng = np.random.default_rng(42)
    for v in todas():
        for c in CULTIVARES:
            s = datos.serie(c)
            for tipo in ("mensual", "interanual"):
                mk = mascara(s, v, tipo, 0)
                pred = pd.DataFrame([{"fecha": f, "seed": k, "y_true": s[f], "y_pred": s[f] * (1 + rng.normal(0, 0.2))}
                                     for f in v.meses_test for k in range(10)])
                r = condicionales(error_abs_promedio(pred), mk.meses_shock)
                rep["sinteticos"][f"{v.anio}/{c}/{tipo}"] = r["Delta_s"]
                if r["Delta_s"] != 0.0 or r["n_shock"] != 12:
                    fallos.append(f"sintetico {v.anio}/{c}/{tipo}: Delta_s={r['Delta_s']}")
    rep["fallos"] = fallos
    rep["OK"] = not fallos
    SAL.write_text(json.dumps(rep, indent=2), encoding="utf-8")
    print(json.dumps({"OK": rep["OK"], "n_reales": len(rep["reales_2025"]), "n_sinteticos": len(rep["sinteticos"]), "fallos": fallos}, indent=2))
    sys.exit(0 if rep["OK"] else 1)


if __name__ == "__main__":
    main()
