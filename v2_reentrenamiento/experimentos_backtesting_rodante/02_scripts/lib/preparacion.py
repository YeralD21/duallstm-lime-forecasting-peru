"""Escalado, secuencias LSTM y pares tabulares por ventana.

Reimplementa, con fechas parametrizadas, tres piezas oficiales que tienen fechas fijas:
  - src/features/escalado.py (RANGOS, l. 26; ajuste, l. 55-63)
  - src/training/sequences_gc3_ge.py (bucle l. 71-80 con guarda anti-fuga; mascaras l. 88-90)
  - src/training/tabular_gc2_xgboost.py (pares X_t -> y_t+1, l. 66-118)
Con Y=2025 deben reproducir exactamente los artefactos oficiales (tests/test_equivalencia_2025.py).
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

from lib.datos import con_fecha, ida_y_vuelta_csv
from lib.ventanas import Ventana

COL_EXCLUIDAS = ("año", "mes", "mes_sin", "mes_cos")  # escalado.py:24
INICIO_FEATURES = "2016-07"


def _clave(df: pd.DataFrame) -> pd.Series:
    return df["año"].astype(str) + "-" + df["mes"].astype(str).str.zfill(2)


class EscaladorVentana:
    """StandardScaler ajustado solo con las filas de train de la ventana (2016-07..fin_train)."""

    def __init__(self, ventana: Ventana) -> None:
        self.ventana = ventana
        self.scaler = StandardScaler()
        self.columnas: list[str] = []
        self.fechas_ajuste: tuple[str, str] | None = None

    def ajustar_transformar(self, features: pd.DataFrame) -> pd.DataFrame:
        df = features.sort_values(["año", "mes"]).reset_index(drop=True)
        k = _clave(df)
        self.columnas = [c for c in df.columns if c not in COL_EXCLUIDAS]
        train = df[(k >= INICIO_FEATURES) & (k <= self.ventana.fin_train)]
        self.scaler.fit(train[self.columnas])
        self.fechas_ajuste = (str(_clave(train).min()), str(_clave(train).max()))
        out = df.copy()
        out[self.columnas] = self.scaler.transform(df[self.columnas])
        return ida_y_vuelta_csv(out)

    def media_escala(self, columna: str) -> tuple[float, float]:
        i = self.columnas.index(columna)
        return float(self.scaler.mean_[i]), float(self.scaler.scale_[i])

    def invertir(self, columna: str, valores: np.ndarray) -> np.ndarray:
        mu, sd = self.media_escala(columna)
        return np.asarray(valores, dtype=float) * sd + mu


@dataclass(frozen=True)
class Particion:
    X_a: np.ndarray | None
    X_b: np.ndarray | None
    X: np.ndarray | None
    y: np.ndarray
    fechas_objetivo: pd.Series
    fechas_contexto_max: pd.Series


def _particion_secuencias(X_a, X_b, y, objetivos, contexto_max, mascara) -> Particion:
    m = np.asarray(mascara)
    return Particion(X_a[m], X_b[m], None, y[m], objetivos[m].reset_index(drop=True), contexto_max[m].reset_index(drop=True))


def secuencias(escalado: pd.DataFrame, rama_a, rama_b, objetivo: str, ventana: Ventana, lookback: int = 6) -> dict[str, Particion]:
    """Secuencias con lookback; objetivo en t, contexto t-lookback..t-1 (sequences_gc3_ge.py:71-80)."""
    df = con_fecha(escalado)
    va = df.loc[:, list(rama_a)].to_numpy(dtype=float)
    vb = df.loc[:, list(rama_b)].to_numpy(dtype=float)
    vy = df.loc[:, objetivo].to_numpy(dtype=float)
    fechas = df["fecha"].reset_index(drop=True)
    xa, xb, yy, obj, ctx = [], [], [], [], []
    for i in range(lookback, len(df)):
        c = fechas.iloc[i - lookback:i]
        t = fechas.iloc[i]
        if not (c < t).all():
            raise ValueError("Fuga: fecha de contexto >= fecha objetivo.")
        xa.append(va[i - lookback:i]); xb.append(vb[i - lookback:i]); yy.append(float(vy[i]))
        obj.append(t); ctx.append(c.max())
    X_a, X_b, y = np.stack(xa), np.stack(xb), np.asarray(yy, dtype=float)
    obj_s, ctx_s = pd.Series(obj, name="fecha"), pd.Series(ctx, name="contexto_max")
    anio = obj_s.dt.year
    return {
        "train": _particion_secuencias(X_a, X_b, y, obj_s, ctx_s, anio <= ventana.anio_fin_train),
        "val": _particion_secuencias(X_a, X_b, y, obj_s, ctx_s, anio == ventana.anio - 1),
        "test": _particion_secuencias(X_a, X_b, y, obj_s, ctx_s, anio == ventana.anio),
    }


def pares_tabulares(frame: pd.DataFrame, predictores, objetivo: str, ventana: Ventana) -> dict[str, Particion]:
    """Pares X_t -> y_(t+1) con meses consecutivos (tabular_gc2_xgboost.py:66-118)."""
    df = con_fecha(frame)
    P = df.loc[:, list(predictores)].to_numpy(dtype=float)
    Y = df.loc[:, objetivo].to_numpy(dtype=float)
    fechas = df["fecha"].reset_index(drop=True)
    xs, ys, xd, yd = [], [], [], []
    for i in range(len(df) - 1):
        a, b = fechas.iloc[i], fechas.iloc[i + 1]
        if b != a + pd.DateOffset(months=1):
            raise ValueError(f"Par no consecutivo: {a} -> {b}")
        xs.append(P[i]); ys.append(float(Y[i + 1])); xd.append(a); yd.append(b)
    X, y = np.stack(xs).astype(float), np.asarray(ys, dtype=float)
    xd_s, yd_s = pd.Series(xd, name="x_fecha"), pd.Series(yd, name="fecha")
    anio = yd_s.dt.year

    def parte(m) -> Particion:
        m = np.asarray(m)
        return Particion(None, None, X[m], y[m], yd_s[m].reset_index(drop=True), xd_s[m].reset_index(drop=True))

    return {"train": parte(anio <= ventana.anio_fin_train), "val": parte(anio == ventana.anio - 1), "test": parte(anio == ventana.anio)}
