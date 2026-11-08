"""Fase B: reproduce Chronos-Bolt-tiny de v4 en TEST 2025 y verifica determinismo (dos pasadas).

Salidas: 06_metricas/reproducibilidad/chronos_v4_reproduccion.csv y .json
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lib.entorno import BR, preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from lib.datos import ConstructorDatosVentana, ruta  # noqa: E402
from lib.integridad import Integridad  # noqa: E402
from lib.modelo_chronos import ChronosZeroShot  # noqa: E402

SAL = BR / "06_metricas" / "reproducibilidad"


def main() -> None:
    Integridad().verificar()
    datos = ConstructorDatosVentana()
    t0 = time.perf_counter()
    modelo = ChronosZeroShot()
    t_carga = time.perf_counter() - t0
    v4 = pd.read_csv(ruta("pred_chronos_v4", oficial=True))
    filas, tiempos = [], []
    for c in ("sutil", "dulce"):
        s = datos.serie(c)
        for mes in [f"2025-{m:02d}" for m in range(1, 13)]:
            ctx = s[s.index < mes].to_numpy()
            t = time.perf_counter()
            p1 = modelo.predecir(ctx)
            tiempos.append(time.perf_counter() - t)
            p2 = modelo.predecir(ctx)
            ref = v4[(v4.cultivar == c) & (v4.date == mes)].iloc[0]
            filas.append({"cultivar": c, "fecha": mes, "contexto_inicio": s.index[0], "contexto_fin": s[s.index < mes].index[-1],
                          "y_true": float(s[mes]), "y_pred_nuevo": p1, "y_pred_repeticion": p2, "y_pred_v4": float(ref.y_pred_ton),
                          "dif_vs_v4": p1 - float(ref.y_pred_ton), "dif_repeticion": p2 - p1})
    df = pd.DataFrame(filas)
    SAL.mkdir(parents=True, exist_ok=True)
    df.to_csv(SAL / "chronos_v4_reproduccion.csv", index=False)
    res = {"modulo_chronos": modelo.modulo, "segundos_carga": t_carga, "segundos_por_pronostico_media": float(np.mean(tiempos)),
           "max_abs_dif_vs_v4": float(df.dif_vs_v4.abs().max()), "identico_v4": bool((df.dif_vs_v4 == 0).all()),
           "determinista": bool((df.dif_repeticion == 0).all()),
           "MAE": {c: {"nuevo": float((g.y_true - g.y_pred_nuevo).abs().mean()), "v4": float((g.y_true - g.y_pred_v4).abs().mean())}
                   for c, g in df.groupby("cultivar")}}
    (SAL / "chronos_v4_reproduccion.json").write_text(json.dumps(res, indent=2), encoding="utf-8")
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
