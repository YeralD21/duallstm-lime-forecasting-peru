"""
Escalado de Fase 2 v2: StandardScaler ajustado EXCLUSIVAMENTE sobre TRAIN.

Split congelado (114 filas tras el dropna de lag6):
    TRAIN  2016-07..2023-12   n = 90
    VAL    2024-01..2024-12   n = 12
    TEST   2025-01..2025-12   n = 12

`fit` se hace solo con las 90 filas de train; val y test unicamente se
transforman. Se excluyen del escalado `año`/`mes` (claves de fila) y
`mes_sin`/`mes_cos` (ya en [-1,1] por construccion ciclica).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

N_TRAIN, N_VAL, N_TEST = 90, 12, 12
COL_EXCLUIDAS = ('año', 'mes', 'mes_sin', 'mes_cos')

RANGOS = {'train': ('2016-07', '2023-12'), 'val': ('2024-01', '2024-12'), 'test': ('2025-01', '2025-12')}


@dataclass
class EscaladorTrain:
    """Ajusta y aplica el StandardScaler respetando el split cronologico."""

    scaler: StandardScaler = field(default_factory=StandardScaler, init=False)
    columnas: list[str] = field(default_factory=list, init=False)

    # ------------------------------------------------------------- particion
    @staticmethod
    def _clave(df: pd.DataFrame) -> pd.Series:
        return df['año'].astype(str) + '-' + df['mes'].astype(str).str.zfill(2)

    @classmethod
    def particionar(cls, df: pd.DataFrame) -> dict[str, pd.DataFrame]:
        df = df.sort_values(['año', 'mes']).reset_index(drop=True)
        k = cls._clave(df)
        partes = {n: df[(k >= lo) & (k <= hi)].reset_index(drop=True) for n, (lo, hi) in RANGOS.items()}
        assert [len(partes[n]) for n in ('train', 'val', 'test')] == [N_TRAIN, N_VAL, N_TEST], \
            f"Split inesperado: {[len(partes[n]) for n in ('train','val','test')]}"
        return partes

    @staticmethod
    def columnas_a_escalar(df: pd.DataFrame) -> list[str]:
        return [c for c in df.columns if c not in COL_EXCLUIDAS]

    # --------------------------------------------------------------- ajuste
    def ajustar_transformar(self, df: pd.DataFrame) -> pd.DataFrame:
        partes = self.particionar(df)
        self.columnas = self.columnas_a_escalar(df)

        # fit SOLO sobre train (nunca val/test)
        self.scaler.fit(partes['train'][self.columnas])
        assert self.scaler.n_samples_seen_ == N_TRAIN, \
            f'n_samples_seen_={self.scaler.n_samples_seen_} (esperado {N_TRAIN})'

        salidas = []
        for nombre in ('train', 'val', 'test'):
            p = partes[nombre].copy()
            p[self.columnas] = self.scaler.transform(p[self.columnas])
            p['__particion'] = nombre
            salidas.append(p)
        out = pd.concat(salidas, ignore_index=True).sort_values(['año', 'mes']).reset_index(drop=True)
        return out.drop(columns='__particion')

    # ---------------------------------------------------------- verificacion
    def verificar(self, escalado: pd.DataFrame) -> dict:
        partes = self.particionar(escalado)
        tr, va, te = partes['train'], partes['val'], partes['test']
        media_tr = tr[self.columnas].mean()
        std_tr = tr[self.columnas].std(ddof=0)
        return {
            'n_features_escaladas': len(self.columnas),
            'train_abs_media_max': float(media_tr.abs().max()),
            'train_std_min': float(std_tr.min()),
            'train_std_max': float(std_tr.max()),
            'val_abs_media_max': float(va[self.columnas].mean().abs().max()),
            'test_abs_media_max': float(te[self.columnas].mean().abs().max()),
            'columnas_no_escaladas': [c for c in COL_EXCLUIDAS if c in escalado.columns],
            'nan_total': int(escalado.isna().sum().sum()),
            'inf_total': int(np.isinf(escalado.select_dtypes(include=[np.number]).to_numpy()).sum()),
            'fit_solo_train_ok': bool(media_tr.abs().max() < 1e-9
                                      and abs(std_tr.min() - 1) < 1e-9
                                      and va[self.columnas].mean().abs().max() > 1e-3),
        }

    def parametros(self) -> pd.DataFrame:
        return pd.DataFrame({'feature': self.columnas,
                            'mean_train': self.scaler.mean_,
                            'scale_train': self.scaler.scale_,
                            'var_train': self.scaler.var_})

    def guardar(self, ruta: str | Path) -> Path:
        ruta = Path(ruta)
        ruta.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(self.scaler, ruta)
        return ruta
