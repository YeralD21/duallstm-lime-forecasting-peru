"""Umbrales de shock por ventana, calculados solo con la historia hasta el origen (D-BR3/D-BR4)."""
from __future__ import annotations

import json
from dataclasses import dataclass

import numpy as np
import pandas as pd

from lib.entorno import CONFIG
from lib.ventanas import Ventana

_CFG = json.loads((CONFIG / "umbrales.json").read_text(encoding="utf-8"))
PERCENTILES = tuple(_CFG["percentiles_barrido"])
PUNTOS_REPORTE = tuple(_CFG["puntos_reporte"])
MIN_INFORMATIVA = int(_CFG["minimo_shocks_ventana_informativa"])


def cambios(serie: pd.Series, tipo: str) -> pd.Series:
    """|y_t - y_(t-k)| / y_(t-k) con k=1 (mensual) o 12 (interanual). Indice 'YYYY-MM'."""
    k = {"mensual": 1, "interanual": 12}[tipo]
    s = serie.sort_index().astype(float)
    return (s - s.shift(k)).abs().div(s.shift(k)).dropna()


@dataclass(frozen=True)
class Mascara:
    tipo: str
    percentil: int
    umbral: float
    meses_shock: tuple[str, ...]
    n_historia: int
    historia_inicio: str
    historia_fin: str

    @property
    def n_shock(self) -> int:
        return len(self.meses_shock)

    @property
    def informativa(self) -> bool:
        return self.n_shock >= MIN_INFORMATIVA


def mascara(serie: pd.Series, ventana: Ventana, tipo: str, percentil: int) -> Mascara:
    r = cambios(serie, tipo)
    historia = r[r.index <= ventana.origen]
    if historia.index.max() != ventana.origen:
        raise AssertionError(f"La historia del umbral no termina en el origen {ventana.origen}.")
    test = r.reindex(ventana.meses_test)
    if test.isna().any():
        raise ValueError(f"Faltan cambios de test en {ventana.anio}.")
    if percentil == 0:
        # Regla P0 preregistrada: todos los meses de test son shock (umbral 0, comparacion >=).
        umbral = 0.0
        meses = tuple(m for m in ventana.meses_test if test[m] >= 0.0)
    else:
        umbral = float(np.percentile(historia.to_numpy(), percentil, method="linear"))
        meses = tuple(m for m in ventana.meses_test if test[m] > umbral)
    return Mascara(tipo, percentil, umbral, meses, len(historia), str(historia.index.min()), str(historia.index.max()))
