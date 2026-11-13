"""R2-T1 (obs. 4): ETS y Theta bajo el protocolo rolling-origin de SARIMA-sel, ventanas 2021-2025, dos cultivos.

POSTERIOR AL PROTOCOLO: robustez/diagnostico; no cambia el ranking principal.
Salidas: 13_revision_r2/resultados/unidades/{ETS,Theta}/<cultivo>/<anio>/predicciones.csv + info.json
(ETS: ademas rejilla_ets.csv con AICc y convergencia de las 12 especificaciones).

Uso: python 13_revision_r2/scripts/t1_ets_theta.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import r2lib as R  # noqa: E402
from lib.entorno import preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import numpy as np  # noqa: E402

from lib.datos import ConstructorDatosVentana  # noqa: E402
from lib.ventanas import Ventana  # noqa: E402


def main() -> None:
    datos = ConstructorDatosVentana()
    for c in R.CULTIVARES:
        s = datos.serie(c)
        for a in R.VENTANAS:
            v = Ventana(a)
            pred, info, rejilla = R.ets_rolling(s, v)
            d = R.UNI / "ETS" / c / str(a)
            R.escribir(pred, d / "predicciones.csv")
            R.escribir(rejilla, d / "rejilla_ets.csv")
            R.escribir_json({"modelo": "ETS", "cultivar": c, "anio_test": a, "semilla": None, "ventana": v.como_dict(), **info},
                            d / "info.json")
            t = pred[pred.particion == "test"]
            print(f"ETS   {c:5s} {a}: {info['especificacion']:12s} conv={info['convergio']} "
                  f"MAE_test={np.mean(np.abs(t.y_true - t.y_pred)):.3f}")
            pred, info = R.theta_rolling(s, v)
            d = R.UNI / "Theta" / c / str(a)
            R.escribir(pred, d / "predicciones.csv")
            R.escribir_json({"modelo": "Theta", "cultivar": c, "anio_test": a, "semilla": None, "ventana": v.como_dict(), **info},
                            d / "info.json")
            t = pred[pred.particion == "test"]
            print(f"Theta {c:5s} {a}: desest={info['desestacionaliza']} ({info['metodo_estacional']}) alpha={info['alpha']:.4f} "
                  f"MAE_test={np.mean(np.abs(t.y_true - t.y_pred)):.3f}")


if __name__ == "__main__":
    main()
