"""Metricas en toneladas reales y bootstrap pareado sobre meses (D-BR5, DA7, DA8)."""
from __future__ import annotations

import numpy as np
import pandas as pd


def error_abs_promedio(pred: pd.DataFrame) -> pd.Series:
    """DA8: promedio mensual del error absoluto entre semillas. pred: fecha, seed, y_true, y_pred."""
    e = pred.assign(ae=(pred["y_true"] - pred["y_pred"]).abs())
    return e.groupby("fecha")["ae"].mean().sort_index()


def condicionales(ae: pd.Series, meses_shock) -> dict[str, float]:
    """MAE global/normal/shock, Delta_s oficial v2 y razon shock/normal."""
    ae = ae.astype(float)
    es = ae.index.isin(list(meses_shock))
    mg = float(ae.mean())
    ms = float(ae[es].mean()) if es.any() else np.nan
    mn = float(ae[~es].mean()) if (~es).any() else np.nan
    ds = (ms - mg) / mg * 100.0 if es.any() else np.nan
    return {"MAE_global": mg, "MAE_shock": ms, "MAE_normal": mn, "n_shock": int(es.sum()), "n_normal": int((~es).sum()),
            "Delta_s": ds, "razon_shock_normal": (ms / mn) if (es.any() and (~es).any()) else np.nan}


def delta_s_sin_un_mes(ae: pd.Series, meses_shock) -> dict[str, float]:
    meses = list(meses_shock)
    return {m: condicionales(ae, [x for x in meses if x != m])["Delta_s"] for m in meses}


def bootstrap_pareado(errores: dict[str, np.ndarray], estratos: np.ndarray, B: int = 10000, semilla: int = 42,
                      estadistico=np.mean) -> dict[str, np.ndarray]:
    """Remuestrea meses (mismos indices para todos los modelos) dentro de cada estrato (ventana)."""
    rng = np.random.default_rng(semilla)
    estratos = np.asarray(estratos)
    grupos = [np.flatnonzero(estratos == g) for g in pd.unique(estratos)]
    out = {k: np.empty(B) for k in errores}
    for b in range(B):
        idx = np.concatenate([rng.choice(g, size=len(g), replace=True) for g in grupos])
        for k, v in errores.items():
            out[k][b] = estadistico(v[idx])
    return out
