"""Fase B: mini corrida = ventana 2025, semilla 0, dos modelos (GC3 y SARIMA congelado), ambos cultivares.

Compara con las predicciones oficiales v2 de TEST 2025. GC3 corre en un subproceso nuevo (07_lstm.py).
Salidas: 10_logs/verificaciones/fase_b/ (no toca 04_modelos ni 05_predicciones).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lib.entorno import BR, preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import json  # noqa: E402
import subprocess  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from lib.datos import ConstructorDatosVentana, ruta  # noqa: E402
from lib.integridad import Integridad  # noqa: E402
from lib.modelos_series import sarima_rolling  # noqa: E402
from lib.ventanas import Ventana  # noqa: E402

SAL = BR / "10_logs" / "verificaciones" / "fase_b"
HP = json.loads((BR / "01_configuracion" / "hiperparametros_congelados.json").read_text(encoding="utf-8"))


def main() -> None:
    Integridad().verificar()
    v = Ventana(2025)
    datos = ConstructorDatosVentana()
    sar_of = pd.read_csv(ruta("pred_sarima_2025", oficial=True))
    gc_of = pd.read_csv(ruta("pred_gc3_ge_2025", oficial=True))
    gc_of["fecha"] = gc_of["fecha"].str[:7]
    res, filas = {}, []
    for c in ("sutil", "dulce"):
        # SARIMA congelado
        t0 = time.perf_counter()
        pred, info = sarima_rolling(datos.serie(c), v, HP["sarima_congelado"][c]["order"], HP["sarima_congelado"][c]["seasonal_order"])
        seg = time.perf_counter() - t0
        of = sar_of[sar_of.cultivar == c].set_index("date")["y_pred_ton"]
        d = pred.set_index("fecha")["y_pred"] - of.reindex(pred.fecha).to_numpy()
        res[f"SARIMA/{c}"] = {"max_abs_dif_vs_oficial": float(d.abs().max()), "MAE_nuevo": float((pred.y_true - pred.y_pred).abs().mean()),
                              "segundos": seg, **info}
        filas += [{"modelo": "SARIMA", "cultivar": c, "seed": 0, **r} for r in pred.to_dict("records")]
        # GC3 semilla 0 en subproceso nuevo
        t0 = time.perf_counter()
        cmd = [sys.executable, str(BR / "02_scripts" / "07_lstm.py"), "--anio", "2025", "--cultivar", c, "--modelo", "GC3",
               "--semilla", "0", "--salida", str(SAL / "04_modelos_prueba")]
        r = subprocess.run(cmd, capture_output=True, text=True)
        seg = time.perf_counter() - t0
        if r.returncode != 0:
            raise SystemExit(r.stderr[-3000:])
        estado = json.loads(r.stdout.strip().splitlines()[-1])
        p = pd.read_csv(SAL / "04_modelos_prueba" / "gc3_lstm_sin_nlp" / c / "2025" / "seed_00" / "predicciones.csv")
        pt = p[p.particion == "test"].set_index("fecha")
        of = gc_of[(gc_of.cultivar == c) & (gc_of.modelo == "GC3") & (gc_of.seed == 0)].set_index("fecha")
        res[f"GC3/{c}/seed0"] = {"max_abs_dif_pred_vs_oficial_t": float((pt.y_pred - of.y_pred_ton.reindex(pt.index)).abs().max()),
                                 "max_abs_dif_ytrue_vs_oficial_t": float((pt.y_true - of.y_true_ton.reindex(pt.index)).abs().max()),
                                 "MAE_nuevo": float((pt.y_true - pt.y_pred).abs().mean()),
                                 "MAE_oficial": float((of.y_true_ton - of.y_pred_ton).abs().mean()),
                                 "segundos_subproceso": seg, "fit_seconds": estado["fit_seconds"],
                                 "mejor_epoca": estado["mejor_epoca"], "epocas_corridas": estado["epocas_corridas"]}
        filas += [{"modelo": "GC3", "cultivar": c, "seed": 0, "fecha": f, "y_true": row.y_true, "y_pred": row.y_pred} for f, row in pt.iterrows()]
    SAL.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(filas).to_csv(SAL / "mini_corrida_predicciones.csv", index=False)
    (SAL / "mini_corrida.json").write_text(json.dumps(res, indent=2), encoding="utf-8")
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
