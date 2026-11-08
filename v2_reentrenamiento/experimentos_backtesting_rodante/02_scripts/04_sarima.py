"""Etapa 04 (Fase C): SARIMA con orden congelado y SARIMA-sel (D-BR2, D-BR10), ventanas 2021-2025.

Una unidad por modelo, cultivo y ventana (lib/reanudacion.py). Salidas por unidad en
04_modelos/sarima_rolling|sarima_sel/<cultivo>/<anio>/:
  - predicciones.csv: validacion y test a 1 paso (toneladas), con los parametros fijos del ajuste en train;
  - info.json: orden, convergencia, AIC, invariancia de parametros;
  - SARIMA-sel ademas: rejilla.csv (576 ordenes: AIC, convergencia, error) y candidatos.csv (top-5 por AIC).
Si el modelo no converge se marca en info.json y en el log; no se fuerza otro orden.

Uso:  python 04_sarima.py [--anios 2021 ...] [--cultivares sutil] [--modelos SARIMA SARIMA-sel] [--salida DIR]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.entorno import CONFIG, preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import argparse  # noqa: E402
import json  # noqa: E402

import numpy as np  # noqa: E402

from lib.datos import ConstructorDatosVentana  # noqa: E402
from lib.modelos_series import sarima_rolling, sarima_sel  # noqa: E402
from lib.reanudacion import argumentos_comunes, correr_etapa, escribir_csv, escribir_json  # noqa: E402

MODELOS = ("SARIMA", "SARIMA-sel")
HP = json.loads((CONFIG / "hiperparametros_congelados.json").read_text(encoding="utf-8"))
_datos: ConstructorDatosVentana | None = None


def trabajo(u, v, tmp: Path) -> dict:
    global _datos
    _datos = _datos or ConstructorDatosVentana()
    s = _datos.serie(u.cultivar)
    if u.modelo == "SARIMA":
        hp = HP["sarima_congelado"][u.cultivar]
        pred, info = sarima_rolling(s, v, hp["order"], hp["seasonal_order"], con_validacion=True)
        info = {"order": hp["order"], "seasonal_order": hp["seasonal_order"], **info}
        elegido = f"{tuple(hp['order'])}{tuple(hp['seasonal_order'])}"
    else:
        pred, info, rejilla, cand = sarima_sel(s, v)
        escribir_csv(rejilla, tmp / "rejilla.csv")
        escribir_csv(cand, tmp / "candidatos.csv")
        elegido = f"{tuple(info['order'])}{tuple(info['seasonal_order'])}[AIC#{info['posicion_aic_elegido']}]"
    if not info["parametros_invariantes"]:
        raise AssertionError(f"{u.nombre}: los parametros cambiaron durante append(refit=False).")
    escribir_csv(pred, tmp / "predicciones.csv")
    escribir_json({"unidad": u.__dict__, "ventana": v.como_dict(), **info}, tmp / "info.json")
    return {"elegido": elegido, "MAE_val": round(float(np.mean(np.abs(pred.y_true - pred.y_pred)[pred.particion == "val"])), 4),
            "convergio": info["convergio"]}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    argumentos_comunes(ap)
    correr_etapa("04_sarima", __file__, ap.parse_args(), MODELOS, (), trabajo)
