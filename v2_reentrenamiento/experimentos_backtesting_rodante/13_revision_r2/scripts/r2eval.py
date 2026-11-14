"""Evaluacion comun de la ronda 2 (Dia 2): misma metodologia que 08_metricas.py / lib/evaluacion.py.

Error absoluto promediado entre semillas; bootstrap iid pareado estratificado por ventana, B = 10 000, semilla 42
(un generador nuevo por remuestreo); empate con el primero = IC 95 % de la diferencia con el mejor contiene 0;
"consistently top-ranked" = primero o empatado en >= 3 de 4 umbrales; DM con correccion HLN, perdida absoluta, h = 1.
Importar despues de preparar_entorno().
"""
from __future__ import annotations

import glob
import json
from pathlib import Path

import numpy as np
import pandas as pd

import r2lib as R
from lib import evaluacion as ev

ORIG10 = list(ev.MODELOS_RANKING)
MOD12 = ORIG10 + list(R.NUEVOS)
CULT = list(R.CULTIVARES)
POOL = list(R.VENTANAS)
PCTS = [50, 60, 75, 90]
TIPOS = {"mensual": "MoM", "interanual": "YoY"}
DEC = {"sutil": 0, "dulce": 1}
# mejor modelo de cada cultivo = menor MAE en todos los meses entre los 10 del articulo (T06 publicado)
MEJOR = {"sutil": "Chronos", "dulce": "SARIMA"}
COLS = ["modelo", "cultivar", "anio_test", "semilla", "particion", "fecha", "y_true", "y_pred"]
S = ev.series()
D = ev.denominadores_mase().set_index(["cultivar", "anio_test"]).D_mase


def originales() -> pd.DataFrame:
    p = pd.read_csv(ev.BR / "05_predicciones" / "predicciones_consolidadas.csv", dtype={"fecha": str})
    return p[COLS]


def r2_dia1() -> pd.DataFrame:
    out = []
    for ruta in sorted(glob.glob(str(R.UNI / "*" / "*" / "*" / "predicciones.csv"))):
        info = json.loads((Path(ruta).parent / "info.json").read_text(encoding="utf-8"))
        p = pd.read_csv(ruta, dtype={"fecha": str})
        p["modelo"], p["cultivar"], p["anio_test"], p["semilla"] = info["modelo"], info["cultivar"], int(info["anio_test"]), None
        out.append(p[COLS])
    return pd.concat(out, ignore_index=True)


def errores(*frames: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """ES (por semilla) y ERR (promediado entre semillas) de la union de los frames; verifica y_true contra la serie."""
    pred = pd.concat([f[COLS] for f in frames], ignore_index=True)
    pred["semilla"] = pd.to_numeric(pred["semilla"], errors="coerce").astype("Int64")
    pred["anio_test"] = pred["anio_test"].astype(int)
    es = ev.errores_por_semilla(pred, S, "test")
    return es, ev.promediar_semillas(es)


def matriz(err, modelos, c, anios=POOL):
    pv = ev.matriz(err, modelos, c, anios)
    claves = list(pv.index)
    return pv, claves, np.array([a for a, _ in claves]), np.array([D[(c, a)] for a, _ in claves])


def vec(claves, meses) -> np.ndarray:
    meses = set(meses)
    return np.array([f in meses for _, f in claves])


def rng():
    return np.random.default_rng(ev.SEMILLA_BOOT)


def resumen(pv, est, Dv, sub, modelos=None) -> pd.DataFrame:
    """MAE, IC 95 % bootstrap y MASE de cada modelo en los meses `sub`."""
    modelos = list(pv.columns) if modelos is None else modelos
    AE = pv[modelos].to_numpy().T
    filas = []
    b = AE[:, ev.indices_iid(est, sub, rng())].mean(axis=2) if sub.any() else None
    for i, m in enumerate(modelos):
        lo, hi = ev.ic(b[i]) if b is not None else (np.nan, np.nan)
        filas.append({"modelo": m, "n_meses": int(sub.sum()), "MAE": float(AE[i][sub].mean()) if sub.any() else np.nan,
                      "IC_lo": lo, "IC_hi": hi, "MASE": float(np.mean(AE[i][sub] / Dv[sub])) if sub.any() else np.nan})
    return pd.DataFrame(filas)


def dif(pv, a, b, est, sub) -> dict:
    """Diferencia pareada MAE_a - MAE_b con IC 95 % bootstrap (mismos indices)."""
    d = (pv[a] - pv[b]).to_numpy()
    if not sub.any():
        return {"dif": np.nan, "IC_lo": np.nan, "IC_hi": np.nan}
    bs = d[ev.indices_iid(est, sub, rng())].mean(axis=1)
    lo, hi = ev.ic(bs)
    return {"dif": float(d[sub].mean()), "IC_lo": lo, "IC_hi": hi}


def dm(pv, a, b, sub) -> dict:
    return ev.dm_hln(pv[a].to_numpy()[sub], pv[b].to_numpy()[sub])


def ranking(pv, est, sub, modelos=None) -> pd.DataFrame:
    modelos = list(pv.columns) if modelos is None else modelos
    return ev.ranking(pv[modelos].to_numpy().T, modelos, est, sub, "iid")


def robustez(pv, est, subs: dict, modelos=None) -> pd.DataFrame:
    """Posicion y primero/empate en cada umbral de `subs` (p -> vector) y regla >= 3 de 4."""
    modelos = list(pv.columns) if modelos is None else modelos
    out = pd.DataFrame({"modelo": modelos})
    cuenta = np.zeros(len(modelos), int)
    for p, sub in subs.items():
        r = ranking(pv, est, sub, modelos).set_index("modelo").reindex(modelos)
        out[f"P{p}"] = ["—" if pd.isna(x) else f"{int(x)}{'*' if y else ''}" for x, y in zip(r.posicion, r.primero)]
        out[f"n_P{p}"] = int(sub.sum())
        cuenta += r.primero.to_numpy(int)
    out["primero_o_empate_de_4"] = cuenta
    out["consistently_top_ranked"] = cuenta >= 3
    return out


def semillas_mejoran(es, a, b, c, anios, meses=None) -> int:
    """Numero de semillas en que el MAE de `a` es menor que el de `b` (misma semilla), en los meses dados."""
    x = es[(es.cultivar == c) & es.anio_test.isin(anios)]
    if meses is not None:
        x = x[x.fecha.isin(set(meses))]
    ma = x[x.modelo == a].groupby("semilla").ae.mean()
    mb = x[x.modelo == b].groupby("semilla").ae.mean()
    d = (ma - mb).dropna()
    return int((d < 0).sum())


def mascara_mom(c, anios=POOL, p=75, tipo="mensual") -> set:
    M = ev.mascaras(S, anios, [p], (tipo,))
    return {m for a in anios for m in M[(c, a, tipo, p)]}


def num(x, d=0) -> str:
    return "—" if x is None or (isinstance(x, float) and not np.isfinite(x)) else f"{x:,.{d}f}"


def ic_txt(v, lo, hi, d) -> str:
    return f"{num(v, d)} ({num(lo, d)}–{num(hi, d)})"


def md(df: pd.DataFrame) -> str:
    cab = [str(c) for c in df.columns]
    return "\n".join(["| " + " | ".join(cab) + " |", "|" + "|".join("---" for _ in cab) + "|"]
                     + ["| " + " | ".join(str(v) for v in r) + " |" for r in df.itertuples(index=False)])
