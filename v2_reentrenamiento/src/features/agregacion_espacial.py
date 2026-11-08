"""
Agregacion provincia -> nacional con pesos historicos FIJOS y crop-aware.

Sustituye a la agregacion anterior, que ponderaba por la produccion provincial
del MISMO mes t:

    ANTES (look-ahead):  C_t = sum_p( C_{p,t} * Y_{p,t} ) / sum_p( Y_{p,t} )
    AHORA (ex ante):     C_t = sum_p( w_p * C_{p,t} ),  w_p fijo, ajustado en TRAIN

`w_p` proviene de `PesosGeograficos` (D14/D15/D16/D17) y no depende de t, por lo
que la serie agregada ya no requiere conocer la produccion del mes objetivo.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass
class AgregadorEspacial:
    """Aplica un vector de pesos fijo a un panel provincial mensual."""

    pesos: pd.Series           # indice 'DEPARTAMENTO|PROVINCIA' -> peso
    nombre: str = 'fuente'

    CLAVE_TIEMPO = ['año', 'mes']

    def _preparar(self, panel: pd.DataFrame) -> pd.DataFrame:
        df = panel.copy()
        if 'key' not in df.columns:
            df['key'] = df['departamento'] + '|' + df['provincia']
        df['w'] = df['key'].map(self.pesos).fillna(0.0)
        return df

    def diagnostico_cobertura(self, panel: pd.DataFrame) -> dict:
        """Masa de peso cubierta por las provincias presentes en la fuente."""
        df = self._preparar(panel)
        presentes = set(df['key'].unique())
        cubierta = float(self.pesos[self.pesos.index.isin(presentes)].sum())
        sin_cobertura = self.pesos[~self.pesos.index.isin(presentes)]
        sin_cobertura = sin_cobertura[sin_cobertura > 0].sort_values(ascending=False)
        por_mes = df.groupby(self.CLAVE_TIEMPO)['w'].sum()
        return {
            'fuente': self.nombre,
            'provincias_en_fuente': int(len(presentes)),
            'provincias_con_peso': int((self.pesos > 0).sum()),
            'masa_peso_cubierta': cubierta,
            'provincias_con_peso_sin_datos': {k: float(v) for k, v in sin_cobertura.items()},
            'masa_no_cubierta': float(sin_cobertura.sum()),
            'masa_por_mes_min': float(por_mes.min()),
            'masa_por_mes_max': float(por_mes.max()),
            'panel_balanceado': bool(np.isclose(por_mes.min(), por_mes.max())),
        }

    def agregar(self, panel: pd.DataFrame, variables: list[str]) -> pd.DataFrame:
        """
        Media ponderada por mes, renormalizada sobre la masa de peso realmente
        presente ese mes. Con panel balanceado el denominador es constante.
        """
        df = self._preparar(panel)
        num = pd.DataFrame({v: df[v].astype(float) * df['w'] for v in variables})
        num['__w'] = df['w']
        num[self.CLAVE_TIEMPO] = df[self.CLAVE_TIEMPO].to_numpy()
        g = num.groupby(self.CLAVE_TIEMPO).sum()
        den = g['__w'].replace(0, np.nan)
        out = g[variables].divide(den, axis=0)
        return out.reset_index().sort_values(self.CLAVE_TIEMPO).reset_index(drop=True)
