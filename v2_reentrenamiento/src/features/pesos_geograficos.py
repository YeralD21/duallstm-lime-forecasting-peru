"""
Ponderacion espacial crop-aware con pesos historicos fijos.

Decisiones metodologicas implementadas (aprobadas 2026-09-07):
  D14  base del ponderador = `verde_actual_ha` (superficie en produccion activa).
       NO se usa produccion como ponderador: produccion_{p,t} pertenece al mismo
       periodo que el target y su uso constituia look-ahead operacional.
  D15  resumen temporal = media aritmetica sobre TRAIN 2016-01..2023-12.
       Validation (2024) y test (2025) quedan EXCLUIDOS del calculo.
  D16  vectores INDEPENDIENTES por cultivar. Queda PROHIBIDO el vector combinado
       Sutil+Dulce usado en la version anterior (en el que Dulce pesaba 1.65%).
  D17  ninguna provincia se excluye, no hay piso minimo ni suavizado.
       Toda provincia con area historica positiva recibe su peso natural.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import pandas as pd

TOLERANCIA_SUMA = 1e-9


@dataclass(frozen=True)
class VentanaTrain:
    """Ventana temporal de ajuste. Congelada: nunca incluye val ni test."""

    anio_inicio: int = 2016
    mes_inicio: int = 1
    anio_fin: int = 2023
    mes_fin: int = 12

    @property
    def inicio(self) -> str:
        return f'{self.anio_inicio}-{self.mes_inicio:02d}'

    @property
    def fin(self) -> str:
        return f'{self.anio_fin}-{self.mes_fin:02d}'

    def filtrar(self, df: pd.DataFrame) -> pd.DataFrame:
        clave = df['año'] * 100 + df['mes']
        lo = self.anio_inicio * 100 + self.mes_inicio
        hi = self.anio_fin * 100 + self.mes_fin
        return df[(clave >= lo) & (clave <= hi)]


@dataclass
class PesosGeograficos:
    """
    Construye el vector de pesos provinciales fijos de un cultivar.

        area_media_train_p = mean(verde_actual_ha[p, t]),  t in TRAIN
        w_p                = area_media_train_p / sum_j(area_media_train_j)
    """

    cultivar: str
    variable_base: str = 'verde_actual_ha'
    unidad: str = 'ha'
    resumen_temporal: str = 'media'
    metodo: str = 'area_media_train_v1'
    version: str = 'v1'
    ventana: VentanaTrain = field(default_factory=VentanaTrain)

    tabla: pd.DataFrame | None = field(default=None, init=False, repr=False)

    CLAVE = ['departamento', 'provincia']

    # ---------------------------------------------------------------- ajuste
    def ajustar(self, provincial: pd.DataFrame) -> 'PesosGeograficos':
        faltan = {'año', 'mes', *self.CLAVE, self.variable_base} - set(provincial.columns)
        if faltan:
            raise ValueError(f'Faltan columnas en el panel provincial: {sorted(faltan)}')

        train = self.ventana.filtrar(provincial)
        if train.empty:
            raise ValueError(f'La ventana {self.ventana.inicio}..{self.ventana.fin} no selecciona filas.')

        # Guarda dura de D15: ni una sola observacion posterior al fin de train.
        clave_max = int((train['año'] * 100 + train['mes']).max())
        limite = self.ventana.anio_fin * 100 + self.ventana.mes_fin
        if clave_max > limite:
            raise AssertionError(f'Se colo informacion posterior a {self.ventana.fin} (max={clave_max}).')

        agg = (train.groupby(self.CLAVE, as_index=False)
                    .agg(valor_historico=(self.variable_base, 'mean'),
                         n_meses_observados=(self.variable_base, 'size')))
        agg['valor_historico'] = agg['valor_historico'].clip(lower=0.0)

        total = float(agg['valor_historico'].sum())
        if total <= 0:
            raise ValueError(f'Suma de {self.variable_base} nula en train para {self.cultivar}.')
        agg['peso'] = agg['valor_historico'] / total

        agg = agg.sort_values('peso', ascending=False).reset_index(drop=True)
        agg.insert(0, 'cultivar', self.cultivar)
        agg['ranking'] = np.arange(1, len(agg) + 1)
        agg['peso_acumulado'] = agg['peso'].cumsum()
        agg['variable_base'] = self.variable_base
        agg['unidad'] = self.unidad
        agg['periodo_inicio'] = self.ventana.inicio
        agg['periodo_fin'] = self.ventana.fin
        agg['resumen_temporal'] = self.resumen_temporal
        agg['metodo'] = self.metodo
        agg['version'] = self.version

        self.tabla = agg[['cultivar', 'departamento', 'provincia', 'variable_base',
                          'periodo_inicio', 'periodo_fin', 'resumen_temporal',
                          'valor_historico', 'unidad', 'n_meses_observados',
                          'peso', 'ranking', 'peso_acumulado', 'metodo', 'version']]
        self.validar()
        return self

    # ------------------------------------------------------------ validacion
    def validar(self) -> None:
        t = self.tabla
        if t is None:
            raise RuntimeError('Llama a ajustar() primero.')
        s = float(t['peso'].sum())
        assert abs(s - 1.0) <= TOLERANCIA_SUMA, f'sum(peso)={s!r} fuera de tolerancia'
        assert (t['peso'] >= 0).all(), 'Hay pesos negativos'
        assert not t.duplicated(['cultivar', *self.CLAVE]).any(), 'Claves duplicadas'
        assert t['periodo_fin'].eq(self.ventana.fin).all(), 'periodo_fin inconsistente'

    # ------------------------------------------------------------------ uso
    @property
    def serie(self) -> pd.Series:
        """Serie peso indexada por 'DEPARTAMENTO|PROVINCIA'."""
        t = self.tabla
        return pd.Series(t['peso'].to_numpy(),
                         index=(t['departamento'] + '|' + t['provincia']).to_numpy(),
                         name=f'w_{self.cultivar}')

    def resumen_concentracion(self) -> dict:
        w = self.tabla['peso'].to_numpy()
        c = np.cumsum(w)
        hhi = float((w ** 2).sum())
        need = lambda q: int((c < q).sum() + 1)
        return {'n_provincias': int(len(w)),
                'n_provincias_peso_positivo': int((w > 0).sum()),
                'top1': float(w[0]), 'top5': float(w[:5].sum()), 'top10': float(w[:10].sum()),
                'hhi': hhi, 'n_efectivo': float(1.0 / hhi),
                'n_para_50pct': need(.50), 'n_para_80pct': need(.80),
                'n_para_90pct': need(.90), 'n_para_95pct': need(.95)}

    def guardar(self, ruta: str | Path) -> Path:
        ruta = Path(ruta)
        ruta.parent.mkdir(parents=True, exist_ok=True)
        self.tabla.to_csv(ruta, index=False, encoding='utf-8-sig')
        return ruta

    @staticmethod
    def concatenar(pesos: list['PesosGeograficos']) -> pd.DataFrame:
        return pd.concat([p.tabla for p in pesos], ignore_index=True)
