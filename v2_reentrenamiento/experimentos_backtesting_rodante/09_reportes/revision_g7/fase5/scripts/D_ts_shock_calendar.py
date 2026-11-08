"""Fase 5 (D): tabla suplementaria del calendario de shocks P75 (inglés, LaTeX booktabs + longtable).

Entrada: 09_reportes/revision_g7/fase1/B1_calendario_shocks_P75.csv (solo lectura).
Salida:  09_reportes/revision_g7/fase5/TS_shock_calendar.tex
No calcula cifras nuevas: solo redondea a 1 decimal cambio_pct y umbral_ventana_pct.
"""
from pathlib import Path

import pandas as pd

AQUI = Path(__file__).resolve().parent
ENTRADA = AQUI.parents[1] / "fase1" / "B1_calendario_shocks_P75.csv"
SALIDA = AQUI.parent / "TS_shock_calendar.tex"

CULT = {"sutil": "Sour lime", "dulce": "Sweet lime"}
DEF = {"P75 MoM": "MoM", "P75 YoY": "YoY"}
EPI = {"inicio": "Onset", "continuacion": "Continuation"}
MESES = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def fecha(s: str) -> str:
    a, m = s.split("-")
    return f"{MESES[int(m) - 1]} {a}"


def signo(x: float) -> str:
    s = f"{abs(x):.1f}"
    return ("$-$" if x < 0 else "$+$") + s


def main() -> None:
    d = pd.read_csv(ENTRADA, dtype={"fecha": str, "fecha_ref": str})
    assert set(d.cultivo) <= set(CULT) and set(d.definicion) <= set(DEF) and set(d.episodio) <= set(EPI)
    d["_c"] = d.cultivo.map({"sutil": 0, "dulce": 1})
    d = d.sort_values(["_c", "fecha", "definicion"])
    ncol = 6
    cab = (r"Date & Definition & Reference month & Change (\%) & Threshold (\%) & Episode \\")
    L = [
        "% Generado por 09_reportes/revision_g7/fase5/scripts/D_ts_shock_calendar.py desde fase1/B1_calendario_shocks_P75.csv",
        r"% Requiere \usepackage{booktabs} y \usepackage{longtable}",
        r"\begin{longtable}{llcrrl}",
        r"\caption{Calendar of shock months at the 75th percentile (P75), test windows 2021--2025, by cultivar. "
        r"Change: signed relative change of national production, $(y_t - y_{t-k})/y_{t-k}$ in \%, with $k = 1$ for the "
        r"month-on-month (MoM) definition and $k = 12$ for the year-on-year (YoY) definition; the reference month is $t-k$. "
        r"A month is a shock when the absolute change $|y_t - y_{t-k}|/y_{t-k}$ is strictly greater than the threshold: the 75th "
        r"percentile of the same absolute change over the history up to the forecast origin of its window (December of $Y-1$). "
        r"Onset: the previous month was not a shock under the same definition (for January, the mask of window $Y-1$ is used); "
        r"Continuation: the previous month was also a shock. Changes and thresholds are rounded to one decimal.}\label{tab:shock_calendar}\\",
        r"\toprule", cab, r"\midrule", r"\endfirsthead",
        rf"\multicolumn{{{ncol}}}{{l}}{{\small\itshape Table~\ref{{tab:shock_calendar}} (continued)}}\\",
        r"\toprule", cab, r"\midrule", r"\endhead",
        rf"\midrule \multicolumn{{{ncol}}}{{r}}{{\small\itshape Continued on next page}}\\", r"\endfoot",
        r"\bottomrule", r"\endlastfoot",
    ]
    for i, (c, g) in enumerate(d.groupby("_c", sort=True)):
        nombre = CULT[g.cultivo.iloc[0]]
        res = ", ".join(f"{DEF[k]} {v}" for k, v in g.definicion.value_counts().sort_index().items())
        if i:
            L.append(r"\midrule")
        L.append(rf"\multicolumn{{{ncol}}}{{l}}{{\textbf{{{nombre}}} ({len(g)} shock months: {res})}}\\")
        L.append(r"\midrule")
        for r in g.itertuples():
            L.append(f"{fecha(r.fecha)} & {DEF[r.definicion]} & {fecha(r.fecha_ref)} & {signo(r.cambio_pct)} & "
                     f"{r.umbral_ventana_pct:.1f} & {EPI[r.episodio]} \\\\")
    L.append(r"\end{longtable}")
    SALIDA.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"{SALIDA.name}: {len(d)} filas ({d.groupby(['cultivo', 'definicion']).size().to_dict()})")


if __name__ == "__main__":
    main()
