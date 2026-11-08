"""Generate tab:shock_scaled and tab:diag_experiments from the CSV files, and compare them cell by cell with a .tex.

    python tablas_g7_tex.py                         # only writes the generated tables
    python tablas_g7_tex.py --tex tablas_revision_g7.tex   # also compares, cell by cell, with that file

Sources (12_revision_g7/resultados/):
  T1_metricas_P75_MoM_YoY.csv            MAE, MAE_sh, MASE_sh, Rel. SN and number of shock months (pool 2021-2025)
  T5_DM_HLN_vs_mejor_univariado.csv      d (MAE difference with the reference) and DM-HLN p-value (scope "global")
  errores_test_promediados_semillas_g7.csv   note (a): per-window MAE of SARIMA-sel-Y1 and the alternative pooled MAE

Formatting rules (the ones used in the manuscript): sour lime MAE in tonnes without decimals and a thousands comma;
sweet lime MAE with 1 decimal; MASE and Rel. SN with 2 decimals; d with sign and the MAE format of the cultivar;
p with 3 decimals, or "<0.001". Bold = column minimum for MAE_sh and MASE_sh. Python rounding (format()).
Outputs: 09_reportes/revision_g7/fase6/tablas_g7_desde_csv.tex and, with --tex, comparacion_celdas.csv.
Nothing is written to the .tex given with --tex.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import pandas as pd

G7 = Path(__file__).resolve().parents[1]
RES = G7 / "resultados"
OUT = G7.parent / "09_reportes" / "revision_g7" / "fase6"
ORIG = ["Naive", "Seasonal Naive", "Chronos", "SARIMA", "SARIMA-sel", "Ridge", "ElasticNet", "XGB-37", "GC3", "GE"]
CUL = ["sutil", "dulce"]
POOL = "principal_2021_2025"
REF = {"sutil": "Chronos", "dulce": "SARIMA-sel"}
DIAG = [  # (experiment label, model)
    ("E1 (refit $Y-1$)", ["GC3-Y1", "GE-Y1", "XGB-37-Y1", "Ridge-Y1", "ElasticNet-Y1", "SARIMA-Y1", "SARIMA-sel-Y1"]),
    ("E2 (univariate LSTM)", ["LSTM-U", "LSTM-U-Y1"]),
    ("E3 (seasonal residual)", ["GC3-R", "GC3-R-Y1"]),
    ("E4 (larger Chronos)", ["Chronos-small", "Chronos-base"]),
]

T1 = pd.read_csv(RES / "T1_metricas_P75_MoM_YoY.csv")
T5 = pd.read_csv(RES / "T5_DM_HLN_vs_mejor_univariado.csv")
ERR = pd.read_csv(RES / "errores_test_promediados_semillas_g7.csv")


def t1(c: str, m: str, col: str) -> float:
    r = T1[(T1.cultivo == c) & (T1.pool == POOL) & (T1.modelo == m)]
    assert len(r) == 1, (c, m)
    return float(r[col].iloc[0])


def t5(c: str, m: str) -> tuple[float, float]:
    r = T5[(T5.cultivo == c) & (T5.pool == POOL) & (T5.modelo == m) & (T5.alcance == "global")]
    assert len(r) == 1 and r.referencia.iloc[0] == REF[c], (c, m)
    return float(r.d_media.iloc[0]), float(r.p.iloc[0])


def f_mae(c: str, x: float) -> str:
    return f"{x:,.0f}" if c == "sutil" else f"{x:.1f}"


def f_d(c: str, x: float) -> str:
    s = f"{x:+,.0f}" if c == "sutil" else f"{x:+.1f}"
    return s.replace("-", "$-$")


def f_p(p: float) -> str:
    return "$<$0.001" if p < 0.001 else f"{p:.3f}"


def bold(s: str, on: bool) -> str:
    return f"\\textbf{{{s}}}" if on else s


# ------------------------------------------------------------------ generation (cells with their CSV value)
def celdas_shock() -> dict:
    cols = [(c, d, m) for c in CUL for d in ("MoM", "YoY") for m in ("MAE_shock", "MASE_shock", "MAE_shock_rel_SNaive")]
    mejor = {(c, d, m): min(ORIG, key=lambda mo: t1(c, mo, f"{m}_{d}")) for c, d, m in cols if m != "MAE_shock_rel_SNaive"}
    cel = {}
    for mo in ORIG:
        for c, d, m in cols:
            v = t1(c, mo, f"{m}_{d}")
            s = f_mae(c, v) if m == "MAE_shock" else f"{v:.2f}"
            cel[(mo, f"{c} {d} {m}")] = (bold(s, mejor.get((c, d, m)) == mo), v)
    for c in CUL:
        for d in ("MoM", "YoY"):
            v = t1(c, "Naive", f"n_shock_{d}")
            cel[("(caption)", f"n shock months {c} {d}")] = (f"{v:.0f}", v)
    return cel


def nota_a() -> tuple[float, float]:
    e = ERR[ERR.cultivar == "sutil"]
    w = e.groupby(["modelo", "anio_test"]).ae.mean()
    alt = (w.loc[("SARIMA-sel", 2021)] + sum(w.loc[("SARIMA-sel-Y1", y)] for y in range(2022, 2026))) / 5
    return float(w.loc[("SARIMA-sel-Y1", 2021)]), float(alt)


def celdas_diag() -> dict:
    cel = {}
    for c in CUL:
        cel[("Reference", f"{c} MAE")] = (f_mae(c, t1(c, REF[c], "MAE")), t1(c, REF[c], "MAE"))
        cel[("GC3 (protocol)", f"{c} MAE")] = (f_mae(c, t1(c, "GC3", "MAE")), t1(c, "GC3", "MAE"))
    for _, modelos in DIAG:
        for m in modelos:
            for c in CUL:
                v = t1(c, m, "MAE")
                cel[(m, f"{c} MAE")] = (f_mae(c, v) + ("$^{a}$" if (m, c) == ("SARIMA-sel-Y1", "sutil") else ""), v)
                d, p = t5(c, m)
                cel[(m, f"{c} d")] = (f_d(c, d), d)
                cel[(m, f"{c} p")] = (f_p(p), p)
    w2021, alt = nota_a()
    cel[("note (a)", "MAE SARIMA-sel-Y1 sour lime 2021")] = (f"{w2021:,.0f}", w2021)
    cel[("note (a)", "pooled MAE with original SARIMA-sel in 2021")] = (f"{alt:,.0f}", alt)
    return cel


def tex_shock(cel: dict) -> str:
    n = {k[1]: v[0] for k, v in cel.items() if k[0] == "(caption)"}
    filas = []
    for mo in ORIG:
        vals = [v[0] for (m, _), v in cel.items() if m == mo]
        filas.append(f"{mo:<14} & " + " & ".join(vals) + "\\\\")
    cab = " & ".join(["MAE$_{\\text{sh}}$ & MASE$_{\\text{sh}}$ & Rel.~SN"] * 4)
    return "\n".join([
        "\\begin{table}[htbp]",
        "\\caption{Shock-month errors under the month-on-month (MoM) and year-on-year (YoY) definitions, P75 threshold, "
        "pooled test windows 2021--2025. MAE$_{\\text{sh}}$: MAE in shock months (t); MASE$_{\\text{sh}}$: MASE restricted "
        "to shock months, with the same denominator per window as the MASE; Rel.~SN: MAE$_{\\text{sh}}$ divided by that of "
        f"the Seasonal Naive. Shock months: sour lime {n['n shock months sutil MoM']} (MoM) and {n['n shock months sutil YoY']} (YoY); "
        f"sweet lime {n['n shock months dulce MoM']} (MoM) and {n['n shock months dulce YoY']} (YoY). Errors of seeded models are "
        "averaged over 10 seeds per month.\\label{tab:shock_scaled}}",
        "\\begin{adjustwidth}{-\\extralength}{0cm}", "\\centering", "\\scriptsize", "\\setlength{\\tabcolsep}{3pt}",
        "\\begin{tabular}{lrrrrrrrrrrrr}", "\\toprule",
        " & \\multicolumn{6}{c}{Sour lime} & \\multicolumn{6}{c}{Sweet lime}\\\\",
        "\\cmidrule(lr){2-7}\\cmidrule(lr){8-13}",
        " & \\multicolumn{3}{c}{MoM} & \\multicolumn{3}{c}{YoY} & \\multicolumn{3}{c}{MoM} & \\multicolumn{3}{c}{YoY}\\\\",
        "\\cmidrule(lr){2-4}\\cmidrule(lr){5-7}\\cmidrule(lr){8-10}\\cmidrule(lr){11-13}",
        f"Model & {cab}\\\\", "\\midrule", *filas, "\\bottomrule", "\\end{tabular}", "\\end{adjustwidth}", "\\end{table}"])


def tex_diag(cel: dict) -> str:
    g = lambda f, col: cel[(f, col)][0]  # noqa: E731
    dp = lambda m, c: f"{g(m, c + ' d')} ({g(m, c + ' p')})"  # noqa: E731
    filas = [f"Reference & Chronos / SARIMA-sel & {g('Reference', 'sutil MAE')} & -- & {g('Reference', 'dulce MAE')} & --\\\\",
             f"Protocol & GC3 & {g('GC3 (protocol)', 'sutil MAE')} & & {g('GC3 (protocol)', 'dulce MAE')} & \\\\"]
    for exp, modelos in DIAG:
        filas.append("\\addlinespace")
        for i, m in enumerate(modelos):
            filas.append(f"{exp if i == 0 else ''} & {m} & {g(m, 'sutil MAE')} & {dp(m, 'sutil')} & {g(m, 'dulce MAE')} & {dp(m, 'dulce')}\\\\")
    nota = (f"\\noindent{{\\footnotesize $^{{a}}$ The reestimation did not converge in the 2021 window (MAE "
            f"{g('note (a)', 'MAE SARIMA-sel-Y1 sour lime 2021')}~t); with the original SARIMA-sel fit in that window, the pooled "
            f"MAE would be {g('note (a)', 'pooled MAE with original SARIMA-sel in 2021')}~t (rule chosen after the fact).}}")
    return "\n".join([
        "\\begin{table}[htbp]",
        "\\caption{Diagnostic experiments added after the protocol (outside the ranking), pooled test windows 2021--2025. MAE in "
        "tonnes; $\\bar d$: difference in MAE with the reference model (Chronos-Bolt-tiny in sour lime, SARIMA-sel in sweet lime) "
        "and two-sided Diebold--Mariano--HLN $p$-value (absolute loss, seed-averaged errors, not adjusted for multiplicity). "
        "``-Y1'': final fit with data up to December of $Y-1$. Original models are shown for reference.\\label{tab:diag_experiments}}",
        "\\begin{adjustwidth}{-\\extralength}{0cm}", "\\centering", "\\footnotesize", "\\setlength{\\tabcolsep}{5pt}",
        "\\begin{tabular}{llrrrr}", "\\toprule",
        " & & \\multicolumn{2}{c}{Sour lime} & \\multicolumn{2}{c}{Sweet lime}\\\\", "\\cmidrule(lr){3-4}\\cmidrule(lr){5-6}",
        "Experiment & Model & MAE & $\\bar d$ ($p$) & MAE & $\\bar d$ ($p$)\\\\", "\\midrule", *filas,
        "\\bottomrule", "\\end{tabular}", "\\end{adjustwidth}", nota, "\\end{table}"])


# ------------------------------------------------------------------ parsing of the manuscript .tex
def bloque(txt: str, label: str) -> list[str]:
    i = txt.index(label)
    return txt[txt.rfind("\\begin{table}", 0, i):txt.index("\\end{table}", i)].splitlines()


def partes(linea: str) -> list[str]:
    return [x.strip() for x in linea.split("\\\\")[0].split("&")]


def leer_shock(txt: str) -> dict:
    L = bloque(txt, "tab:shock_scaled")
    cols = [f"{c} {d} {m}" for c in CUL for d in ("MoM", "YoY") for m in ("MAE_shock", "MASE_shock", "MAE_shock_rel_SNaive")]
    out = {}
    for linea in L:
        cs = partes(linea)
        if cs[0] in ORIG:
            out.update({(cs[0], col): v for col, v in zip(cols, cs[1:])})
    cap = "\n".join(L)
    for c, nombre in (("sutil", "sour lime"), ("dulce", "sweet lime")):
        m = re.search(nombre + r" (\d+) \(MoM\) and (\d+) \(YoY\)", cap)
        out[("(caption)", f"n shock months {c} MoM")], out[("(caption)", f"n shock months {c} YoY")] = m.group(1), m.group(2)
    return out


def leer_diag(txt: str) -> dict:
    L = bloque(txt, "tab:diag_experiments")
    out = {}
    for linea in L:
        cs = partes(linea)
        if len(cs) != 6 or cs[1] in ("Model", ""):
            continue
        fila = {"Chronos / SARIMA-sel": "Reference", "GC3": "GC3 (protocol)"}.get(cs[1], cs[1])
        out[(fila, "sutil MAE")], out[(fila, "dulce MAE")] = cs[2], cs[4]
        for c, cd in (("sutil", cs[3]), ("dulce", cs[5])):
            mm = re.match(r"(.*?)\s*\((.*)\)$", cd)
            if mm:
                out[(fila, f"{c} d")], out[(fila, f"{c} p")] = mm.group(1).strip(), mm.group(2).strip()
    nota = next((linea for linea in txt[txt.index("tab:diag_experiments"):].splitlines() if "$^{a}$ The" in linea), "")
    m1, m2 = re.search(r"MAE ([\d,]+)~t\)", nota), re.search(r"would be ([\d,]+)~t", nota)
    out[("note (a)", "MAE SARIMA-sel-Y1 sour lime 2021")] = m1.group(1) if m1 else None
    out[("note (a)", "pooled MAE with original SARIMA-sel in 2021")] = m2.group(1) if m2 else None
    return out


def comparar(tex_path: Path, gen: dict[str, dict]) -> pd.DataFrame:
    txt = tex_path.read_text(encoding="utf-8")
    leido = {"tab:shock_scaled": leer_shock(txt), "tab:diag_experiments": leer_diag(txt)}
    filas = []
    for tabla, cel in gen.items():
        claves = list(cel) + [k for k in leido[tabla] if k not in cel]
        for k in claves:
            g, v = cel.get(k, (None, None))
            t = leido[tabla].get(k)
            filas.append({"tabla": tabla, "fila": k[0], "columna": k[1], "valor_tex": t, "valor_generado": g,
                          "valor_csv": v, "coincide": t is not None and g is not None and t.replace(" ", "") == g.replace(" ", "")})
    return pd.DataFrame(filas)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    gen = {"tab:shock_scaled": celdas_shock(), "tab:diag_experiments": celdas_diag()}
    (OUT / "tablas_g7_desde_csv.tex").write_text(
        "% Generated by 12_revision_g7/scripts/tablas_g7_tex.py from 12_revision_g7/resultados/*.csv\n\n"
        + tex_shock(gen["tab:shock_scaled"]) + "\n\n" + tex_diag(gen["tab:diag_experiments"]) + "\n", encoding="utf-8")
    print(f"written {OUT / 'tablas_g7_desde_csv.tex'}")
    if "--tex" in sys.argv:
        tex = Path(sys.argv[sys.argv.index("--tex") + 1])
        d = comparar(tex, gen)
        d.to_csv(OUT / "comparacion_celdas.csv", index=False, encoding="utf-8")
        for t, g in d.groupby("tabla", sort=False):
            print(f"{t}: {len(g)} cells, {int(g.coincide.sum())} equal, {int((~g.coincide).sum())} different")
        dif = d[~d.coincide]
        if len(dif):
            print(dif[["tabla", "fila", "columna", "valor_tex", "valor_generado", "valor_csv"]].to_string(index=False))
        sys.exit(1 if len(dif) else 0)


if __name__ == "__main__":
    main()
