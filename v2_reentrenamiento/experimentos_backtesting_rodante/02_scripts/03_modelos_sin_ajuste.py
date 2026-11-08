"""Etapa 03 (Fase C): Naive, Seasonal Naive y Chronos-Bolt-tiny zero-shot (D-BR2), ventanas 2018-2025.

Una unidad por modelo, cultivo y ventana (lib/reanudacion.py). Salidas por unidad en
04_modelos/<modelo>/<cultivo>/<anio>/: predicciones.csv (toneladas) e info.json.
  - Naive / Seasonal Naive: todos los meses con y_(t-1) / y_(t-12) hasta el test (train y val sirven para D-BR8).
  - Chronos: solo test; contexto = serie desde 2016-01 hasta t-1, mediana, sin red.

Uso:  python 03_modelos_sin_ajuste.py [--anios 2021 ...] [--cultivares sutil] [--modelos Naive Chronos] [--salida DIR]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.entorno import preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import argparse  # noqa: E402

import pandas as pd  # noqa: E402

from lib.datos import ConstructorDatosVentana  # noqa: E402
from lib.modelos_series import ingenuos_todas_particiones, naive, seasonal_naive  # noqa: E402
from lib.reanudacion import argumentos_comunes, correr_etapa, escribir_csv, escribir_json  # noqa: E402

MODELOS = ("Naive", "Seasonal Naive", "Chronos")
_datos: ConstructorDatosVentana | None = None
_chronos = None


def trabajo(u, v, tmp: Path) -> dict:
    global _datos, _chronos
    _datos = _datos or ConstructorDatosVentana()
    s = _datos.serie(u.cultivar)
    if u.modelo in ("Naive", "Seasonal Naive"):
        rezago = 1 if u.modelo == "Naive" else 12
        pred = ingenuos_todas_particiones(s, v, rezago)
        control = (naive if rezago == 1 else seasonal_naive)(s, v)
        t = pred[pred.particion == "test"].reset_index(drop=True)
        if not (t[["fecha", "y_true", "y_pred"]].equals(control[["fecha", "y_true", "y_pred"]])):
            raise AssertionError(f"{u.nombre}: el test no coincide con la definicion de lib.modelos_series.")
        info = {"rezago": rezago, "n_por_particion": pred.particion.value_counts().to_dict()}
    else:
        if _chronos is None:
            from lib.modelo_chronos import ChronosZeroShot
            _chronos = ChronosZeroShot()
        filas = []
        for m in v.meses_test:
            ctx = s[s.index < m]
            filas.append({"particion": "test", "fecha": m, "y_true": float(s[m]), "y_pred": _chronos.predecir(ctx.to_numpy()),
                          "contexto_inicio": ctx.index[0], "contexto_fin": ctx.index[-1]})
        pred = pd.DataFrame(filas)
        info = {"modulo_chronos": _chronos.modulo, "n_contexto_primer_mes": int((s.index < v.meses_test[0]).sum())}
    escribir_csv(pred, tmp / "predicciones.csv")
    escribir_json({"unidad": u.__dict__, "ventana": v.como_dict(), **info}, tmp / "info.json")
    return {"n_test": int((pred.particion == "test").sum())}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    argumentos_comunes(ap)
    correr_etapa("03_modelos_sin_ajuste", __file__, ap.parse_args(), MODELOS, (), trabajo)
