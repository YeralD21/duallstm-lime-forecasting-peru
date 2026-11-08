"""Definicion de ventanas rolling-origin y su viabilidad por modelo (DA1, DA2)."""
from __future__ import annotations

import json
from dataclasses import dataclass

import pandas as pd

from lib.entorno import CONFIG

_CFG = json.loads((CONFIG / "ventanas.json").read_text(encoding="utf-8"))
MINIMO_TRAIN = int(_CFG["minimo_train_meses"])
ANIOS_TEST = tuple(_CFG["anios_test"])
VENTANAS_RANKING = tuple(_CFG["ventanas_ranking"])
VENTANAS_SENSIBILIDAD = tuple(_CFG["ventanas_sensibilidad_DA2"])

MODELOS_SIN_AJUSTE = ("Naive", "Seasonal Naive", "Chronos")
MODELOS_ENTRENADOS = ("SARIMA", "SARIMA-sel", "Ridge", "ElasticNet", "XGB-37", "GC3", "GE", "XGB-43")


def _mes(fecha: str) -> pd.Timestamp:
    return pd.Timestamp(f"{fecha}-01")


def _n_meses(inicio: str, fin: str) -> int:
    a, b = _mes(inicio), _mes(fin)
    return (b.year - a.year) * 12 + (b.month - a.month) + 1


@dataclass(frozen=True)
class Ventana:
    """Ventana con test = ano Y, validacion = Y-1 y train hasta diciembre de Y-2."""

    anio: int

    def __post_init__(self) -> None:
        if self.anio not in ANIOS_TEST:
            raise ValueError(f"Ano de test fuera del preregistro: {self.anio}")

    @property
    def origen(self) -> str:
        return f"{self.anio - 1}-12"

    @property
    def fin_train(self) -> str:
        return f"{self.anio - 2}-12"

    @property
    def anio_fin_train(self) -> int:
        return self.anio - 2

    @property
    def val(self) -> tuple[str, str]:
        return (f"{self.anio - 1}-01", f"{self.anio - 1}-12")

    @property
    def test(self) -> tuple[str, str]:
        return (f"{self.anio}-01", f"{self.anio}-12")

    @property
    def meses_test(self) -> list[str]:
        return [f"{self.anio}-{m:02d}" for m in range(1, 13)]

    # n de observaciones de entrenamiento por familia
    def n_train(self, modelo: str) -> int:
        if modelo in MODELOS_SIN_AJUSTE:
            return 0
        if modelo in ("GC3", "GE"):
            inicio = _CFG["primer_objetivo_lstm"]
        elif modelo in ("Ridge", "ElasticNet", "XGB-37", "XGB-43"):
            inicio = _CFG["primer_objetivo_tabular"]
        else:
            inicio = _CFG["inicio_train_sarima"]
        return max(0, _n_meses(inicio, self.fin_train))

    def viable(self, modelo: str) -> bool:
        return modelo in MODELOS_SIN_AJUSTE or self.n_train(modelo) >= MINIMO_TRAIN

    def como_dict(self) -> dict:
        return {"anio_test": self.anio, "origen": self.origen, "fin_train": self.fin_train,
                "val_inicio": self.val[0], "val_fin": self.val[1], "test_inicio": self.test[0], "test_fin": self.test[1],
                "en_ranking": self.anio in VENTANAS_RANKING, "en_sensibilidad_2023_2025": self.anio in VENTANAS_SENSIBILIDAD}


def todas() -> list[Ventana]:
    return [Ventana(a) for a in ANIOS_TEST]
