"""Etapa 01: ventanas, viabilidad, umbrales P0..P95 (mensual e interanual), pesos por ventana y denominador MASE.

Salidas en 03_ventanas/ (solo indices, fechas y parametros derivados; ningun dato copiado).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.entorno import BR, preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from lib.datos import CULTIVARES, ConstructorDatosVentana  # noqa: E402
from lib.integridad import Integridad  # noqa: E402
from lib.shocks import PERCENTILES, mascara  # noqa: E402
from lib.ventanas import MODELOS_ENTRENADOS, MODELOS_SIN_AJUSTE, todas  # noqa: E402

SALIDA = BR / "03_ventanas"


def denominador_mase(serie: pd.Series, ventana) -> dict:
    """D_w = media |y_t - y_(t-12)| para t en 2017-01..fin_train (train de la ventana con y_(t-12) disponible)."""
    s = serie.sort_index()
    d = (s - s.shift(12)).abs().dropna()
    d = d[(d.index >= "2017-01") & (d.index <= ventana.fin_train)]
    return {"D_mase": float(d.mean()) if len(d) else np.nan, "n_meses_denominador": int(len(d)),
            "inicio": str(d.index.min()) if len(d) else None, "fin": str(d.index.max()) if len(d) else None}


def main() -> None:
    Integridad().verificar()
    datos = ConstructorDatosVentana()
    filas_v, filas_u, filas_p, filas_d = [], [], [], []
    for v in todas():
        base = v.como_dict()
        for m in (*MODELOS_SIN_AJUSTE, *MODELOS_ENTRENADOS):
            filas_v.append({**base, "modelo": m, "n_train": v.n_train(m), "viable": v.viable(m),
                            "estado": "aplica" if v.viable(m) else "no aplica",
                            "exploratorio": m in ("XGB-43",)})
        for c in CULTIVARES:
            serie = datos.serie(c)
            for tipo in ("mensual", "interanual"):
                for p in PERCENTILES:
                    mk = mascara(serie, v, tipo, p)
                    filas_u.append({"anio_test": v.anio, "cultivar": c, "tipo": tipo, "percentil": p, "umbral": mk.umbral,
                                    "n_shock": mk.n_shock, "informativa": mk.informativa, "meses_shock": ";".join(mk.meses_shock),
                                    "n_historia": mk.n_historia, "historia_inicio": mk.historia_inicio, "historia_fin": mk.historia_fin})
            pw = datos.pesos(c, v.anio_fin_train).tabla
            filas_p.append(pw.assign(anio_test=v.anio)[["anio_test", "cultivar", "departamento", "provincia", "periodo_inicio", "periodo_fin", "peso"]])
            filas_d.append({"anio_test": v.anio, "cultivar": c, **denominador_mase(serie, v)})
    SALIDA.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(filas_v).to_csv(SALIDA / "ventanas_viabilidad.csv", index=False)
    pd.DataFrame(filas_u).to_csv(SALIDA / "umbrales_y_mascaras.csv", index=False)
    pd.concat(filas_p, ignore_index=True).to_csv(SALIDA / "pesos_geograficos_por_ventana.csv", index=False)
    pd.DataFrame(filas_d).to_csv(SALIDA / "denominador_mase_por_ventana.csv", index=False)
    u = pd.DataFrame(filas_u)
    p75 = u[(u.tipo == "mensual") & (u.percentil == 75)].pivot(index="anio_test", columns="cultivar", values="n_shock")
    print("n_shock P75 mensual por ventana:\n", p75.to_string())
    vv = pd.DataFrame(filas_v)
    print("\nCombinaciones viables (x2 cultivares):", int(vv[vv.viable & ~vv.exploratorio].shape[0]) * 2,
          "| no aplica:", int(vv[~vv.viable & ~vv.exploratorio].shape[0]) * 2)


if __name__ == "__main__":
    main()
