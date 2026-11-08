"""
Features temporales de Fase 2 v2: codificacion ciclica, lags, t_index.

Protocolo temporal (decision D6, aprobada 2026-09-07):
FORECAST ROLLING ONE-STEP-AHEAD — informacion hasta el cierre de t predice y[t+1].

Consecuencia implementada aqui: NINGUNA variable exogena del mes objetivo entra
en la matriz predictiva. Toda exogena aparece exclusivamente rezagada
(lag1 / lag3 / lag6). Las columnas exogenas contemporaneas se eliminan tras
generar sus rezagos.

Orden obligatorio (fijado por decision):
    1. codificacion ciclica        (mes_sin, mes_cos)
    2. generacion de lags          (sobre la serie completa de 120 meses)
    3. eliminacion de contemporaneas exogenas
    4. dropna de lags              (-> 114 filas, 2016-07..2025-12)
    5. t_index                     (DESPUES del dropna, ANTES del split/scaler)
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

LAGS_POR_DEFECTO = (1, 3, 6)

# t_index = 12*(anio - ANIO_BASE) + (mes - 1) - DESPLAZAMIENTO
# Con ANIO_BASE=2016 y DESPLAZAMIENTO=6:  2016-07 -> 0 ; 2025-12 -> 113
ANIO_BASE = 2016
DESPLAZAMIENTO = 6


@dataclass
class FeaturesTemporales:
    """Construye el conjunto de features temporales de un cultivar."""

    target: str
    exogenas: list[str]
    lags: tuple[int, ...] = LAGS_POR_DEFECTO
    columnas_lag: list[str] = field(default_factory=list, init=False)

    CLAVES = ['año', 'mes']

    # ------------------------------------------------------------ 1. ciclica
    @staticmethod
    def codificacion_ciclica(df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df['mes_sin'] = np.sin(2 * np.pi * df['mes'] / 12)
        df['mes_cos'] = np.cos(2 * np.pi * df['mes'] / 12)
        return df

    # --------------------------------------------------------------- 2. lags
    def generar_lags(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.sort_values(self.CLAVES).reset_index(drop=True).copy()
        self.columnas_lag = []
        for col in [self.target, *self.exogenas]:
            for k in self.lags:
                nueva = f'{col}_lag{k}'
                df[nueva] = df[col].shift(k)
                self.columnas_lag.append(nueva)
        return df

    # ------------------------------------------- 3. quitar exogenas de mes t
    def eliminar_contemporaneas(self, df: pd.DataFrame) -> pd.DataFrame:
        """Elimina toda exogena del mes objetivo. El target se conserva."""
        return df.drop(columns=[c for c in self.exogenas if c in df.columns])

    # ------------------------------------------------------------- 4. dropna
    def aplicar_dropna(self, df: pd.DataFrame) -> pd.DataFrame:
        antes = len(df)
        out = df.dropna(subset=self.columnas_lag).reset_index(drop=True)
        assert out[self.columnas_lag].isna().sum().sum() == 0, 'Quedan NaN en columnas lag'
        self.filas_eliminadas = antes - len(out)
        return out

    # ------------------------------------------------------------ 5. t_index
    @staticmethod
    def calcular_t_index(df: pd.DataFrame) -> pd.DataFrame:
        """
        Definicion CALENDARIO (decision aprobada):
            t_index = 12*(anio - 2016) + (mes - 1) - 6

        `t_posicional = np.arange(len(df))` se calcula solo como CHECK, nunca
        como definicion: la forma calendario es robusta ante huecos futuros en
        la serie, la posicional no.
        """
        df = df.sort_values(FeaturesTemporales.CLAVES).reset_index(drop=True).copy()
        df['t_index'] = (12 * (df['año'] - ANIO_BASE) + (df['mes'] - 1) - DESPLAZAMIENTO).astype(int)

        t_posicional = np.arange(len(df))
        assert np.array_equal(df['t_index'].to_numpy(), t_posicional), (
            't_index calendario != t_posicional: la serie no es contigua mes a mes.')
        assert df['t_index'].min() == 0, f"t_index.min()={df['t_index'].min()} (esperado 0)"
        assert df['t_index'].max() == len(df) - 1, f"t_index.max()={df['t_index'].max()}"
        return df

    @staticmethod
    def verificar_valores_obligatorios(df: pd.DataFrame) -> dict:
        esperado = {(2016, 7): 0, (2023, 12): 89, (2024, 1): 90, (2025, 12): 113}
        obtenido = {}
        for (a, m), v in esperado.items():
            fila = df[(df['año'] == a) & (df['mes'] == m)]
            assert len(fila) == 1, f'Falta o duplicada la fila {a}-{m:02d}'
            real = int(fila['t_index'].iloc[0])
            assert real == v, f't_index({a}-{m:02d})={real}, esperado {v}'
            obtenido[f'{a}-{m:02d}'] = real
        return obtenido

    # ----------------------------------------------------------- orquestacion
    def construir(self, maestro: pd.DataFrame) -> pd.DataFrame:
        df = self.codificacion_ciclica(maestro)
        df = self.generar_lags(df)
        df = self.eliminar_contemporaneas(df)
        df = self.aplicar_dropna(df)
        df = self.calcular_t_index(df)
        return self.ordenar_columnas(df)

    def ordenar_columnas(self, df: pd.DataFrame) -> pd.DataFrame:
        cabeza = [*self.CLAVES, self.target, 'mes_sin', 'mes_cos', 't_index']
        resto = [c for c in df.columns if c not in cabeza]
        return df[cabeza + resto]

    # ---------------------------------------------------------- verificacion
    def verificar_anti_fuga(self, maestro: pd.DataFrame, features: pd.DataFrame) -> dict:
        """
        Comprueba celda a celda que cada `X_lagk[t]` es exactamente `X[t-k]` en
        el maestro original, y que ninguna exogena contemporanea sobrevivio.
        """
        base = maestro.sort_values(self.CLAVES).reset_index(drop=True)
        base['__clave'] = base['año'] * 100 + base['mes']
        idx = {int(k): i for i, k in enumerate(base['__clave'])}
        fallos = []
        for _, fila in features.iterrows():
            pos = idx[int(fila['año'] * 100 + fila['mes'])]
            for col in self.columnas_lag:
                var, k = col.rsplit('_lag', 1)
                esperado = base.loc[pos - int(k), var]
                if not np.isclose(fila[col], esperado, rtol=0, atol=1e-9):
                    fallos.append((int(fila['año']), int(fila['mes']), col))
        contemporaneas = [c for c in self.exogenas if c in features.columns]
        return {'celdas_verificadas': int(len(features) * len(self.columnas_lag)),
                'fallos': fallos[:10],
                'n_fallos': len(fallos),
                'exogenas_contemporaneas_presentes': contemporaneas,
                'anti_fuga_ok': (len(fallos) == 0 and len(contemporaneas) == 0)}
