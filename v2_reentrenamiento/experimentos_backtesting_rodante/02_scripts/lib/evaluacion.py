"""Fase D1: errores promediados entre semillas (D-BR6), metricas (D-BR5), bootstrap pareado, DM-HLN y tablas.

Todas las metricas en toneladas reales. y_true canonico = serie nacional (lib.datos); se verifica que el y_true
guardado por cada modelo coincida con el (tolerancia 1e-6 t; los modelos escalados lo reconstruyen con el scaler).
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from lib.datos import ConstructorDatosVentana
from lib.entorno import BR
from lib.shocks import mascara
from lib.ventanas import Ventana

MODELOS_RANKING = ("Naive", "Seasonal Naive", "Chronos", "SARIMA", "SARIMA-sel", "Ridge", "ElasticNet", "XGB-37", "GC3", "GE")
EXPLORATORIOS = ("XGB-43",)
SIN_AJUSTE = ("Naive", "Seasonal Naive", "Chronos")
CON_SEMILLA = ("XGB-37", "XGB-43", "GC3", "GE")
CULTIVARES = ("sutil", "dulce")
VENTANAS_PRINCIPAL = (2021, 2022, 2023, 2024, 2025)
VENTANAS_SENSIBILIDAD = (2023, 2024, 2025)
VENTANAS_DESCRIPTIVAS = (2018, 2019, 2020)
PUNTOS_REPORTE = (50, 60, 75, 90)
B = 10_000
SEMILLA_BOOT = 42
TOL_Y_TRUE = 1e-6


# ----------------------------------------------------------------------------- carga

def cargar_predicciones() -> pd.DataFrame:
    partes = []
    for p in sorted((BR / "05_predicciones").glob("0[3-7]_*.csv")):
        df = pd.read_csv(p, dtype={"fecha": str})
        partes.append(df[["modelo", "cultivar", "anio_test", "semilla", "particion", "fecha", "y_true", "y_pred"]])
    pred = pd.concat(partes, ignore_index=True)
    pred["semilla"] = pred["semilla"].astype("Int64")
    return pred


def series() -> dict[str, pd.Series]:
    d = ConstructorDatosVentana()
    return {c: d.serie(c) for c in CULTIVARES}


def denominadores_mase() -> pd.DataFrame:
    return pd.read_csv(BR / "03_ventanas" / "denominador_mase_por_ventana.csv")[["anio_test", "cultivar", "D_mase"]]


def errores_por_semilla(pred: pd.DataFrame, s: dict[str, pd.Series], particion: str = "test") -> pd.DataFrame:
    """Una fila por modelo, cultivo, ventana, semilla y mes con el error con signo (y_pred - y_true canonico)."""
    e = pred[pred.particion == particion].copy()
    e["y_canonico"] = [float(s[c][f]) for c, f in zip(e.cultivar, e.fecha)]
    dif = (e.y_true - e.y_canonico).abs().max()
    if dif > TOL_Y_TRUE:
        raise AssertionError(f"y_true de algun modelo difiere de la serie en {dif} t ({particion}).")
    e["e"] = e.y_pred - e.y_canonico
    e["ae"] = e.e.abs()
    return e.drop(columns=["y_true"]).rename(columns={"y_canonico": "y_true"})


def promediar_semillas(es: pd.DataFrame) -> pd.DataFrame:
    """D-BR6: error absoluto mensual promediado entre las semillas (modelos sin semilla: su unico error)."""
    g = es.groupby(["modelo", "cultivar", "anio_test", "fecha"], sort=True)
    out = g.agg(y_true=("y_true", "first"), ae=("ae", "mean"), ae_sd_semillas=("ae", "std"), e_medio=("e", "mean"),
                se_medio=("e", lambda x: float(np.mean(np.asarray(x) ** 2))), n_semillas=("ae", "size")).reset_index()
    return out


def mascaras(s: dict[str, pd.Series], anios, percentiles, tipos=("mensual", "interanual")) -> dict:
    return {(c, a, t, p): set(mascara(s[c], Ventana(a), t, p).meses_shock)
            for c in CULTIVARES for a in anios for t in tipos for p in percentiles}


# ----------------------------------------------------------------------------- metricas

def matriz(err: pd.DataFrame, modelos, cultivar: str, anios) -> pd.DataFrame:
    """Error absoluto promediado entre semillas: filas (anio_test, fecha), columnas = modelos, sin huecos."""
    sub = err[(err.cultivar == cultivar) & err.anio_test.isin(list(anios)) & err.modelo.isin(list(modelos))]
    pv = sub.pivot_table(index=["anio_test", "fecha"], columns="modelo", values="ae", aggfunc="first").sort_index()
    pv = pv[list(modelos)]
    if pv.isna().any().any() or len(pv) != 12 * len(list(anios)):
        raise AssertionError(f"Matriz incompleta {cultivar} {list(anios)}: {pv.shape}, NaN={int(pv.isna().sum().sum())}")
    return pv


def vector_shock(claves, M: dict, cultivar: str, tipo: str, p: int) -> np.ndarray:
    return np.array([f in M[(cultivar, a, tipo, p)] for a, f in claves])


def rmse_semillas(es: pd.DataFrame, modelo: str, cultivar: str, anios) -> float:
    """RMSE de cada semilla sobre los meses del conjunto y media entre semillas (DESV-06)."""
    sub = es[(es.modelo == modelo) & (es.cultivar == cultivar) & es.anio_test.isin(list(anios))]
    return float(sub.groupby(sub.semilla.fillna(-1))["e"].apply(lambda x: np.sqrt(np.mean(np.asarray(x) ** 2))).mean())


def metricas(ae: np.ndarray, es_shock: np.ndarray, D: np.ndarray, rmse: float) -> dict:
    """D-BR5 sobre un vector de errores absolutos (promediados entre semillas). D: D_w de la ventana de cada mes."""
    mg = float(ae.mean())
    ms = float(ae[es_shock].mean()) if es_shock.any() else np.nan
    mn = float(ae[~es_shock].mean()) if (~es_shock).any() else np.nan
    return {"MAE": mg, "RMSE": rmse, "MASE": float(np.mean(ae / D)), "MAE_normal": mn, "MAE_shock": ms,
            "n_shock": int(es_shock.sum()), "n_normal": int((~es_shock).sum()),
            "Delta_s": (ms - mg) / mg * 100 if es_shock.any() else np.nan,
            "razon_shock_normal": ms / mn if (es_shock.any() and (~es_shock).any()) else np.nan}


def ranking(AE: np.ndarray, nombres, estratos: np.ndarray, subconj: np.ndarray, tipo_boot: str = "iid") -> pd.DataFrame:
    """D-BR7: ranking por MAE en los meses `subconj`. Empate con el mejor = IC 95 % del bootstrap pareado de
    (MAE_modelo - MAE_mejor) contiene 0. "primero" = el mejor y los que empatan con el. Mismos indices para todos.
    tipo_boot "iid": remuestreo dentro de `subconj` estratificado por ventana (principal).
    tipo_boot "bloques": bloques de 3 meses de toda la ventana; MAE del subconjunto como cociente (sensibilidad)."""
    if not subconj.any():
        return pd.DataFrame({"modelo": list(nombres), "MAE": np.nan, "posicion": pd.NA, "dif_vs_mejor_lo": np.nan,
                             "dif_vs_mejor_hi": np.nan, "primero": False, "n_meses": 0})
    rng = np.random.default_rng(SEMILLA_BOOT)
    if tipo_boot == "iid":
        est = AE[:, indices_iid(estratos, subconj, rng)].mean(axis=2)
    else:
        est = remuestrear(AE, subconj, indices_bloques(estratos, rng))
    mae = AE[:, subconj].mean(axis=1)
    mejor = int(np.argmin(mae))
    filas = []
    for i, m in enumerate(nombres):
        lo, hi = ic(est[i] - est[mejor])
        filas.append({"modelo": m, "MAE": float(mae[i]), "dif_vs_mejor_lo": lo, "dif_vs_mejor_hi": hi,
                      "primero": bool(i == mejor or (lo <= 0 <= hi)), "n_meses": int(subconj.sum())})
    out = pd.DataFrame(filas)
    out.insert(2, "posicion", out.MAE.rank(method="min").astype(int))
    return out


def delta_s_loo(ae: np.ndarray, es_shock: np.ndarray) -> np.ndarray:
    """Δs quitando un mes de shock a la vez (el mes sale de los shocks y del global)."""
    out = []
    for i in np.flatnonzero(es_shock):
        keep = np.ones(len(ae), bool)
        keep[i] = False
        a, s = ae[keep], es_shock[keep]
        mg = a.mean()
        out.append((a[s].mean() - mg) / mg * 100 if s.any() else np.nan)
    return np.array(out)


# ----------------------------------------------------------------------------- bootstrap

def indices_iid(estratos: np.ndarray, subconjunto: np.ndarray, rng: np.random.Generator, b: int = B) -> np.ndarray:
    """Remuestreo iid pareado, estratificado por ventana, dentro de los meses de `subconjunto` (bool)."""
    cols = []
    for g in pd.unique(estratos):
        pos = np.flatnonzero((estratos == g) & subconjunto)
        if len(pos):
            cols.append(pos[rng.integers(0, len(pos), size=(b, len(pos)))])
    return np.concatenate(cols, axis=1)


def indices_bloques(estratos: np.ndarray, rng: np.random.Generator, largo: int = 3, b: int = B) -> np.ndarray:
    """Bloques moviles circulares de `largo` meses dentro de cada ventana (sensibilidad D-BR5)."""
    cols = []
    for g in pd.unique(estratos):
        pos = np.flatnonzero(estratos == g)
        n = len(pos)
        k = int(np.ceil(n / largo))
        inicios = rng.integers(0, n, size=(b, k))
        rel = (inicios[:, :, None] + np.arange(largo)[None, None, :]) % n
        cols.append(pos[rel.reshape(b, -1)[:, :n]])
    return np.concatenate(cols, axis=1)


def remuestrear(AE: np.ndarray, peso: np.ndarray, idx: np.ndarray) -> np.ndarray:
    """Media ponderada (peso 0/1) de cada modelo en cada remuestreo: (modelos, B). NaN si el peso total es 0."""
    w = peso[idx].astype(float)                       # (B, n)
    num = np.einsum("mbn,bn->mb", AE[:, idx], w)
    den = w.sum(axis=1)
    with np.errstate(invalid="ignore", divide="ignore"):
        return num / den[None, :]


def ic(x: np.ndarray) -> tuple[float, float]:
    x = x[np.isfinite(x)]
    return (float(np.percentile(x, 2.5)), float(np.percentile(x, 97.5))) if len(x) else (np.nan, np.nan)


# ----------------------------------------------------------------------------- Diebold-Mariano

def dm_hln(ae_a: np.ndarray, ae_b: np.ndarray, h: int = 1) -> dict:
    """DM con correccion HLN, perdida absoluta, h=1 (varianza = autocovarianza de orden 0). Bilateral, t(n-1)."""
    d = np.asarray(ae_a, float) - np.asarray(ae_b, float)
    n = len(d)
    g0 = float(np.mean((d - d.mean()) ** 2))
    if n < 3 or g0 == 0:
        return {"n": n, "d_media": float(d.mean()) if n else np.nan, "DM": np.nan, "HLN": np.nan, "p": np.nan}
    dm = d.mean() / np.sqrt(g0 / n)
    hln = dm * np.sqrt((n + 1 - 2 * h + h * (h - 1) / n) / n)
    p = 2 * (1 - stats.t.cdf(abs(hln), df=n - 1))
    return {"n": n, "d_media": float(d.mean()), "DM": float(dm), "HLN": float(hln), "p": float(p)}


# ----------------------------------------------------------------------------- salida de tablas

def _fmt(v, dec: int) -> str:
    if v is None or (isinstance(v, float) and np.isnan(v)) or (v is pd.NA):
        return "—"
    if isinstance(v, (bool, np.bool_)):
        return "sí" if v else "no"
    if isinstance(v, (int, np.integer)):
        return str(int(v))
    if isinstance(v, (float, np.floating)):
        return f"{v:,.{dec}f}" if abs(v) >= 1000 else f"{v:.{dec}f}"
    return str(v)


def dec_columna(nombre: str, dec: int) -> int:
    """Decimales minimos por tipo de columna: razones, MASE, CV, ACF y p-valores con 2-3; Δs con 1."""
    n = str(nombre)
    if any(k in n for k in ("_p", "ACF")):
        return max(dec, 3)
    if any(k in n for k in ("MASE", "razon", "/normal", "CV", "Naive_razon")):
        return max(dec, 2)
    if any(k in n for k in ("Δs", "Delta_s")):
        return max(dec, 1)
    return dec


def a_texto(df: pd.DataFrame, dec: int = 2) -> str:
    cab = [str(c) for c in df.columns]
    decs = [dec_columna(c, dec) for c in df.columns]
    filas = [[_fmt(v, d) for v, d in zip(r, decs)] for r in df.itertuples(index=False)]
    return "\n".join(["| " + " | ".join(cab) + " |", "|" + "|".join("---" for _ in cab) + "|"] +
                     ["| " + " | ".join(f) + " |" for f in filas])


def _tex(s: str) -> str:
    for a, b in (("\\", r"\textbackslash{}"), ("&", r"\&"), ("%", r"\%"), ("_", r"\_"), ("#", r"\#"), ("Δ", r"$\Delta$"),
                 ("—", "--"), ("−", "-"), ("≥", r"$\geq$"), ("×", r"$\times$")):
        s = s.replace(a, b)
    return s


def a_latex(df: pd.DataFrame, titulo: str, etiqueta: str, dec: int = 2) -> str:
    cab = " & ".join(_tex(str(c)) for c in df.columns) + r" \\"
    decs = [dec_columna(c, dec) for c in df.columns]
    filas = [" & ".join(_tex(_fmt(v, d)) for v, d in zip(r, decs)) + r" \\" for r in df.itertuples(index=False)]
    return "\n".join([r"\begin{table}[H]", r"\centering", r"\small", rf"\caption{{{_tex(titulo)}}}", rf"\label{{{etiqueta}}}",
                      r"\begin{tabular}{" + "l" * len(df.columns) + "}", r"\toprule", cab, r"\midrule", *filas,
                      r"\bottomrule", r"\end{tabular}", r"\end{table}"])


class Tablas:
    """Guarda cada tabla en CSV (completa, precision total), LaTeX y texto (redondeados)."""

    def __init__(self) -> None:
        self.texto: list[str] = []
        self.indice: list[dict] = []
        self.latex_dir = BR / "06_metricas" / "tablas_latex"
        self.latex_dir.mkdir(parents=True, exist_ok=True)

    def guardar(self, df: pd.DataFrame, carpeta: str, nombre: str, titulo: str, vista: pd.DataFrame | None = None,
                dec: int = 2, mostrar: bool = True) -> None:
        destino = BR / carpeta
        destino.mkdir(parents=True, exist_ok=True)
        df.to_csv(destino / f"{nombre}.csv", index=False, float_format="%.10g")
        v = df if vista is None else vista
        (self.latex_dir / f"{nombre}.tex").write_text(a_latex(v, titulo, f"tab:{nombre}", dec), encoding="utf-8")
        bloque = f"### {nombre} — {titulo}\n\n{a_texto(v, dec)}\n"
        self.indice.append({"nombre": nombre, "titulo": titulo, "csv": f"{carpeta}/{nombre}.csv",
                            "tex": f"06_metricas/tablas_latex/{nombre}.tex", "texto": bloque})
        if mostrar:
            self.texto.append(bloque)

    def escribir_texto(self, ruta: Path) -> None:
        """Vista resumida (.md) e indice completo (.indice.json, con el texto de todas las tablas, para el reporte)."""
        import json

        ruta.write_text("\n".join(self.texto), encoding="utf-8")
        ruta.with_suffix(".indice.json").write_text(json.dumps(self.indice, indent=1, ensure_ascii=False), encoding="utf-8")
