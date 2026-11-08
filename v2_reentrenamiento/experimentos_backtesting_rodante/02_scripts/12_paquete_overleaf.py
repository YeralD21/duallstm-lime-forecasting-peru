"""Etapa 12: paquete LaTeX para Overleaf con la selección de figuras y tablas del artículo MDPI (aprobada por el autor).

No calcula ninguna cifra: copia PDF, pies y tablas ya guardados, y escribe las tablas del texto principal leyendo los CSV
de 06_metricas/ (solo selección de columnas y formato). Escribe en 08_graficos/paper_mdpi/overleaf/: figures/ (PDF con su
nombre original), tables/ (.tex), captions.tex (un pie por figura, del TXT, sin referencias internas), figures_main.tex,
figures_supp.tex, tables_main.tex, tables_supp.tex y test_article.tex; además resultados_v2_completo.tex (todo en un archivo,
sin \\input), figures_overleaf.zip (solo los PDF) y lista_figuras.md. El README.md se escribe a mano.
Cada pareja Sutil/Dulce va en un entorno figure con dos subfiguras sin letra ("Sour lime", "Sweet lime"), para no chocar con
las letras de los paneles internos; apiladas si la figura es ancha.
Al final verifica: \\includegraphics e \\input apuntan a archivos existentes, nombres y etiquetas sin repetir, pies iguales a
los TXT (salvo los reemplazos declarados), marca EXPLORATORY en fig18b y fig19b, sin referencias internas, y 5 celdas de las
tablas principales elegidas al azar comparadas con su CSV.
"""
import random
import re
import shutil
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.entorno import BR  # noqa: E402

import pandas as pd  # noqa: E402

G = BR / "08_graficos"
M = BR / "06_metricas"
OUT = G / "paper_mdpi" / "overleaf"
ANCHA_PULG = 4.0  # una figura más ancha que esto va apilada (las dos subfiguras una sobre otra)
SUB = {"sutil": "Sour lime", "dulce": "Sweet lime"}
CULTIVARES = ("sutil", "dulce")
MODELOS = ("Naive", "Seasonal Naive", "Chronos", "SARIMA", "SARIMA-sel", "Ridge", "ElasticNet", "XGB-37", "GC3", "GE")
VENTANAS = (2021, 2022, 2023, 2024, 2025)

# (archivo sutil, archivo dulce) para parejas; (archivo,) para figuras únicas. Orden = orden de aparición.
PRINCIPAL = [
    ("figuras_independientes/fig29_study_area_map",),
    ("figuras_independientes/fig24_series_with_shocks_sutil", "figuras_independientes/fig24_series_with_shocks_dulce"),
    ("figuras_independientes/fig_workflow",),  # 13_figura_workflow.py; XGB-43 como caja exploratoria discontinua (DESV-08, 30)
    ("figuras_independientes/fig30_rolling_origin_scheme",),
    ("figuras_independientes/fig25_architecture_dual_lstm",),
    ("comparacion_modelos/fig13_mae_normal_vs_shock_bars_sutil", "comparacion_modelos/fig13_mae_normal_vs_shock_bars_dulce"),
    ("sensibilidad_umbral/fig07_rank_heatmap_model_percentile_sutil", "sensibilidad_umbral/fig07_rank_heatmap_model_percentile_dulce"),
    ("sensibilidad_umbral/fig05_mae_shock_vs_percentile_sutil", "sensibilidad_umbral/fig05_mae_shock_vs_percentile_dulce"),
    ("sensibilidad_umbral/fig04_delta_s_vs_percentile_sutil", "sensibilidad_umbral/fig04_delta_s_vs_percentile_dulce"),
    ("sensibilidad_umbral/fig10_n_shock_heatmap_window_percentile_sutil", "sensibilidad_umbral/fig10_n_shock_heatmap_window_percentile_dulce"),
    ("predicciones/fig20_real_vs_pred_2025_sutil", "predicciones/fig20_real_vs_pred_2025_dulce"),
    ("comparacion_modelos/fig18_nlp_ablation_paired_sutil", "comparacion_modelos/fig18_nlp_ablation_paired_dulce"),
    ("diagnostico_ajuste/fig02_train_val_gap_sutil", "diagnostico_ajuste/fig02_train_val_gap_dulce"),
]
SUPLEMENTARIO = [
    ("predicciones/fig20_real_vs_pred_2023_sutil", "predicciones/fig20_real_vs_pred_2024_dulce"),  # año con más shocks P75 de cada cultivar
    ("comparacion_modelos/fig19_dm_pvalue_matrix_sutil", "comparacion_modelos/fig19_dm_pvalue_matrix_dulce"),
    ("comparacion_modelos/fig19b_dm_pvalue_matrix_holm_sutil", "comparacion_modelos/fig19b_dm_pvalue_matrix_holm_dulce"),
    ("comparacion_modelos/fig18b_xgb43_vs_xgb37_exploratory_sutil", "comparacion_modelos/fig18b_xgb43_vs_xgb37_exploratory_dulce"),
    ("diagnostico_ajuste/fig01_loss_curves_gc3_sutil", "diagnostico_ajuste/fig01_loss_curves_gc3_dulce"),
    ("diagnostico_ajuste/fig01_loss_curves_ge_sutil", "diagnostico_ajuste/fig01_loss_curves_ge_dulce"),
    ("diagnostico_ajuste/fig03_early_stopping_epoch_sutil", "diagnostico_ajuste/fig03_early_stopping_epoch_dulce"),
    ("sensibilidad_umbral/fig06_ratio_shock_normal_vs_percentile_sutil", "sensibilidad_umbral/fig06_ratio_shock_normal_vs_percentile_dulce"),
    ("sensibilidad_umbral/fig08_rank_bump_chart_sutil", "sensibilidad_umbral/fig08_rank_bump_chart_dulce"),
    ("sensibilidad_umbral/fig09_n_shock_vs_percentile_sutil", "sensibilidad_umbral/fig09_n_shock_vs_percentile_dulce"),
    ("sensibilidad_umbral/fig11_bootstrap_ci_mae_shock_report_points_sutil", "sensibilidad_umbral/fig11_bootstrap_ci_mae_shock_report_points_dulce"),
    ("sensibilidad_umbral/fig12_yoy_vs_mom_threshold_sutil", "sensibilidad_umbral/fig12_yoy_vs_mom_threshold_dulce"),
    ("comparacion_modelos/fig14_mae_shock_heatmap_model_window_sutil", "comparacion_modelos/fig14_mae_shock_heatmap_model_window_dulce"),
    ("comparacion_modelos/fig15_seed_boxplots_sutil", "comparacion_modelos/fig15_seed_boxplots_dulce"),
    ("comparacion_modelos/fig16_mae_by_change_quartile_sutil", "comparacion_modelos/fig16_mae_by_change_quartile_dulce"),
    ("comparacion_modelos/fig17_leave_one_shock_out_delta_s_sutil", "comparacion_modelos/fig17_leave_one_shock_out_delta_s_dulce"),
    ("errores/fig21_abs_error_monthly_sutil", "errores/fig21_abs_error_monthly_dulce"),
]
EXPLORATORIAS = ("fig18b_", "fig19b_")
PNG_EXTRA = ["figuras_independientes/fig_workflow"]  # el main.tex antiguo de Overleaf busca fig_workflow.png
UNICO, ZIP_FIG, LISTA = "resultados_v2_completo.tex", "figures_overleaf.zip", "lista_figuras.md"

# Referencias internas que no van al artículo: se reemplazan en los pies del paquete (los TXT originales no cambian).
REEMPLAZOS = {
    " (D-BR8).": " (pre-registered).",
    " (D-BR6).": " (pre-registered).",
    "(exploratory, DESV-07; family": "(exploratory; family",
    " (v2 official implementation).": ".",
}
INTERNAS = ("D-BR", "DESV", "v2 official")

# Tablas suplementarias copiadas, en orden: (origen relativo a BR, cambios en la copia)
T16_EN = {
    "EXPLORATORIO (post-hoc): XGB-43 frente a XGB-37, 2021-2025, P75 mensual (t)":
        "EXPLORATORY (post-hoc): XGB-43 versus XGB-37, 2021-2025, monthly P75 (t)",
    "cultivar & alcance & n\\_meses & MAE\\_XGB37 & MAE\\_XGB43 & dif\\_43\\_menos\\_37 & IC95\\_lo & IC95\\_hi \\\\":
        "Cultivar & Scope & Months & MAE XGB-37 & MAE XGB-43 & XGB-43 $-$ XGB-37 & 95\\% CI lower & 95\\% CI upper \\\\",
}
TABLAS_SUPLEMENTARIO = [
    ("08_graficos/figuras_independientes/TS1_provinces.tex", {}),
    ("06_metricas/tablas_latex/T16_exploratorio_xgb43.tex", T16_EN),
    ("06_metricas/tablas_latex/T05_MAE_P75_por_ventana_sutil.tex", {}),
    ("06_metricas/tablas_latex/T05_MAE_P75_por_ventana_dulce.tex", {}),
    ("06_metricas/tablas_latex/T05_MAE_shock_P75_por_ventana_sutil.tex", {}),
    ("06_metricas/tablas_latex/T05_MAE_shock_P75_por_ventana_dulce.tex", {}),
    ("06_metricas/tablas_latex/T09_DM_matriz_principal_2021_2025_sutil.tex", {}),
    ("06_metricas/tablas_latex/T09_DM_matriz_principal_2021_2025_dulce.tex", {}),
    ("06_metricas/tablas_latex/T11_ablacion_sutil.tex", {}),
    ("06_metricas/tablas_latex/T11_ablacion_dulce.tex", {}),
]
APAISADAS = {"TS1_provinces"}  # 12 columnas: en landscape (pdflscape)
TABLAS_PRINCIPAL = ["TM1_descriptive_series", "TM2_aggregate_accuracy_P75", "TM3_robust_ranking"]

MIDAGRI_TXT, MIDAGRI_TEX = "accessed [____]", "accessed \\midagridate{}"
A_TEX = {"_": "\\_", "%": "\\%", "&": "\\&", "#": "\\#", "$": "\\$", "{": "\\{", "}": "\\}", "~": "\\textasciitilde{}",
         "^": "\\textasciicircum{}", "\\": "\\textbackslash{}", "|": "\\textbar{}", ">": "\\textgreater{}", "<": "\\textless{}",
         "Δ": "$\\Delta$", "−": "\\textminus{}", "†": "\\dag{}"}
CELDAS: list[dict] = []  # registro de celdas de las tablas principales, para la verificación por muestreo


def pie_txt(rel: str) -> str:
    t = (G / f"{rel}.txt").read_text(encoding="utf-8")
    m = re.match(r"Caption \(suggested\): (.*?)\n\nReading:", t, re.S)
    if not m:
        raise ValueError(f"TXT sin pie: {rel}")
    return m.group(1).strip()


def pie_articulo(rel: str) -> str:
    """Pie del TXT con las referencias internas reemplazadas (REEMPLAZOS)."""
    p = pie_txt(rel)
    for a, b in REEMPLAZOS.items():
        p = p.replace(a, b)
    return p


def a_tex(s: str) -> str:
    partes = s.split(MIDAGRI_TXT)
    return MIDAGRI_TEX.join("".join(A_TEX.get(ch, ch) for ch in p) for p in partes)


def de_tex(s: str) -> str:
    """Inversa exacta de a_tex (para verificar que el pie de captions.tex es el del TXT)."""
    partes = s.split(MIDAGRI_TEX)
    inv = sorted(((v, k) for k, v in A_TEX.items()), key=lambda x: -len(x[0]))
    pat = re.compile("|".join(re.escape(v) for v, _ in inv))
    d = dict(inv)
    return MIDAGRI_TXT.join(pat.sub(lambda m: d[m.group(0)], p) for p in partes)


def ancho_pulg(pdf: Path) -> float:
    m = re.search(rb"/MediaBox\s*\[\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)", pdf.read_bytes())
    return (float(m.group(3)) - float(m.group(1))) / 72


def nombre(rel: str) -> str:
    return rel.split("/")[-1]


def etiqueta_fig(grupo: tuple) -> str:
    n = nombre(grupo[0])
    if len(grupo) == 1:
        return n
    a, b = n, nombre(grupo[1])
    return a[:-len("_sutil")] if a.endswith("_sutil") and b == a[:-len("_sutil")] + "_dulce" else f"{a}__{b}"


def entorno(grupo: tuple) -> str:
    lab = etiqueta_fig(grupo)
    marca = "\\textbf{EXPLORATORY.} " if any(nombre(grupo[0]).startswith(e) for e in EXPLORATORIAS) and not pie_txt(grupo[0]).startswith("EXPLORATORY") else ""
    if len(grupo) == 1:
        n = nombre(grupo[0])
        return ("\\begin{figure}[htbp]\n\\centering\n"
                f"\\includegraphics[width=\\linewidth,height=0.8\\textheight,keepaspectratio]{{{n}.pdf}}\n"
                f"\\caption{{{marca}\\figcap{{{n}}}}}\n\\label{{fig:{lab}}}\n\\end{{figure}}\n")
    ancha = max(ancho_pulg(G / f"{r}.pdf") for r in grupo) > ANCHA_PULG
    sub_w, sep = ("\\linewidth", "\n\\par\\medskip\n") if ancha else ("0.49\\linewidth", "\\hfill\n")
    alto = ",height=0.36\\textheight,keepaspectratio" if ancha else ""
    anios = [re.search(r"_(20\d\d)_", nombre(r)) for r in grupo]
    con_anio = all(anios) and anios[0].group(1) != anios[1].group(1)  # fig20 suplementaria: años distintos por cultivar
    subs, pie = [], marca
    for rel in grupo:
        n, c = nombre(rel), nombre(rel).rsplit("_", 1)[1]
        sub = SUB[c] + (f", {re.search(r'_(20[0-9][0-9])_', n).group(1)}" if con_anio else "")
        subs.append(f"\\begin{{subfigure}}{{{sub_w}}}\n\\centering\n\\includegraphics[width=\\linewidth{alto}]{{{n}.pdf}}\n"
                    f"\\caption{{{sub}}}\n\\label{{fig:{n}}}\n\\end{{subfigure}}")
        pie += f"\\textit{{{sub}:}} \\figcap{{{n}}} "
    return ("\\begin{figure}[htbp]\n\\centering\n" + sep.join(subs) + "\n"
            f"\\caption{{{pie.strip()}}}\n\\label{{fig:{lab}}}\n\\end{{figure}}\n")


# ---------------------------------------------------------------- tablas del texto principal (solo formato de CSV)
def num(v: float, dec: int) -> str:
    return f"{v:,.{dec}f}"


def dec_t(c: str) -> int:
    return 0 if c == "sutil" else 1  # toneladas: Sutil en miles de t, Dulce en decenas


def p_txt(p: float) -> str:
    return "$<$0.001" if p < 0.001 else f"{p:.3f}"


def anotar(tabla: str, c: str, fila: str, col: int, parte: str, texto: str, csv: str, consulta: str, valor: float, dec: int) -> None:
    CELDAS.append(dict(tabla=tabla, cultivar=c, fila=fila, col=col, parte=parte, texto=texto, csv=csv, consulta=consulta, valor=valor, dec=dec))


def tabla_latex(etiqueta: str, caption: str, cols: str, cabecera: str, bloques: list[tuple[str, list[list[str]]]]) -> str:
    n = len(cols)
    filas = []
    for i, (titulo, rows) in enumerate(bloques):
        if i:
            filas.append("\\addlinespace")
        filas.append(f"\\multicolumn{{{n}}}{{l}}{{{titulo}}} \\\\")
        filas += [" & ".join(r) + " \\\\" for r in rows]
    return ("\\begin{table}[htbp]\n\\centering\n\\small\n"
            f"\\caption{{{caption}}}\n\\label{{tab:{etiqueta}}}\n\\begin{{tabular}}{{{cols}}}\n\\toprule\n{cabecera} \\\\\n\\midrule\n"
            + "\n".join(filas) + "\n\\bottomrule\n\\end{tabular}\n\\end{table}\n")


def tm1() -> str:
    """Series descriptivas por ventana 2021-2025: año de test (T03) y partición de entrenamiento (T04)."""
    f3, f4 = "06_metricas/descripcion_series/T03_descripcion_particiones.csv", "06_metricas/descripcion_series/T04_acf_adf_kpss_train.csv"
    t3, t4 = pd.read_csv(BR / f3), pd.read_csv(BR / f4)
    bloques = []
    for c in CULTIVARES:
        rows = []
        for v in VENTANAS:
            a = t3[(t3.cultivar == c) & (t3.anio_test == v) & (t3.particion == "test")].iloc[0]
            b = t4[(t4.cultivar == c) & (t4.anio_test == v)].iloc[0]
            kp = ("$>$0.10" if b.KPSS_nivel_p >= 0.1 else "$<$0.01") if bool(b.KPSS_nivel_p_acotado) else f"{b.KPSS_nivel_p:.3f}"
            r = [str(v), str(int(b.n_train)), num(a.media, dec_t(c)), num(a.DE, dec_t(c)), f"{a.CV:.2f}", f"{b.ACF1:.2f}", f"{b.ACF12:.2f}",
                 p_txt(b.ADF_nivel_p), kp]
            for col, campo, src, dec in ((2, "media", f3, dec_t(c)), (3, "DE", f3, dec_t(c)), (4, "CV", f3, 2), (5, "ACF1", f4, 2), (6, "ACF12", f4, 2)):
                fuente = a if src == f3 else b
                q = f"cultivar={c}, anio_test={v}" + (", particion=test" if src == f3 else "") + f", columna {campo}"
                anotar("TM1_descriptive_series", c, str(v), col, "valor", r[col], src, q, float(fuente[campo]), dec)
            rows.append(r)
        bloques.append((f"\\textit{{{SUB[c]}}}", rows))
    cab = "Test year & Train months & Mean (t) & SD (t) & CV & ACF(1) & ACF(12) & ADF $p$ & KPSS $p$"
    cap = ("Descriptive statistics of the national monthly production series for each rolling-origin window, 2021--2025. "
           "Mean, standard deviation (SD) and coefficient of variation (CV) refer to the 12 months of the test year. "
           "Train months, autocorrelation (ACF at lags 1 and 12) and unit-root tests refer to the training partition of each window, "
           "series in levels with a constant: ADF (null hypothesis: unit root) and KPSS (null hypothesis: level stationarity) $p$-values; "
           "KPSS $p$-values outside the tabulated range are shown as bounds.")
    return tabla_latex("main_descriptive_series", cap, "lrrrrrrrr", cab, bloques)


def tm2() -> str:
    """Agregados 2021-2025, P75 mensual (T06): MAE y MAE_shock con IC bootstrap iid (principal), Δs. Sin XGB-43."""
    f6 = "06_metricas/agregadas/T06_agregadas_IC.csv"
    t6 = pd.read_csv(BR / f6)
    t6 = t6[(t6.conjunto == "principal_2021_2025") & (t6.tipo == "mensual") & (t6.percentil == 75) & ~t6.exploratorio]
    bloques = []
    for c in CULTIVARES:
        d = t6[t6.cultivar == c].set_index("modelo").loc[list(MODELOS)]
        ns, nn = d.n_shock.unique(), d.n_normal.unique()
        if len(ns) != 1 or len(nn) != 1:
            raise AssertionError(f"n distinto entre modelos: {c}")
        k = dec_t(c)
        rows = []
        for m, r in d.iterrows():
            fila = [m, f"{num(r.MAE, k)} ({num(r.iid_global_lo, k)}--{num(r.iid_global_hi, k)})",
                    f"{num(r.MAE_shock, k)} ({num(r.iid_shock_lo, k)}--{num(r.iid_shock_hi, k)})", num(r.Delta_s, 1)]
            q = f"conjunto=principal_2021_2025, cultivar={c}, tipo=mensual, percentil=75, modelo={m}, columna "
            for col, parte, campo, dec in ((1, "valor", "MAE", k), (1, "lo", "iid_global_lo", k), (1, "hi", "iid_global_hi", k),
                                           (2, "valor", "MAE_shock", k), (2, "lo", "iid_shock_lo", k), (2, "hi", "iid_shock_hi", k),
                                           (3, "valor", "Delta_s", 1)):
                anotar("TM2_aggregate_accuracy_P75", c, m, col, parte, fila[col], f6, q + campo, float(r[campo]), dec)
            rows.append(fila)
        bloques.append((f"\\textit{{{SUB[c]}}} ({int(ns[0] + nn[0])} test months; {int(ns[0])} shock months)", rows))
    cab = "Model & MAE, all months (t) (95\\% CI) & MAE, shock months (t) (95\\% CI) & $\\Delta_s$ (\\%)"
    cap = ("Aggregated forecast accuracy, pooled test windows 2021--2025, by cultivar. Shock months: monthly P75 threshold of the "
           "month-on-month change (history up to each origin). MAE in tonnes with 95\\% bootstrap confidence intervals in parentheses "
           "(months resampled within windows, B = 10,000); $\\Delta_s = (\\mathrm{MAE}_{\\mathrm{shock}} - \\mathrm{MAE})/\\mathrm{MAE} \\times 100$. "
           "Errors of seeded models (XGB-37, GC3, GE) are averaged over 10 seeds per month. The exploratory XGB-43 is not included.")
    return tabla_latex("main_aggregate_accuracy", cap, "lccr", cab, bloques)


def tm3() -> str:
    """Ranking por MAE_shock en P50/P60/P75/P90 y robustez E-BR1 (T08, conjunto principal, criterio shock)."""
    bloques = []
    for c in CULTIVARES:
        f8 = f"06_metricas/agregadas/T08_ranking_shock_principal_2021_2025_{c}.csv"
        d = pd.read_csv(BR / f8, dtype=str).set_index("modelo").loc[list(MODELOS)]
        rows = []
        for m, r in d.iterrows():
            pos = [r[f"sh-men-P{p}"].replace("*", "$^{*}$") for p in (50, 60, 75, 90)]
            fila = [m] + pos + [r["sh-men primero en"], "Yes" if r["robusto men"] == "True" else "No",
                                r["sh-int primero en"], "Yes" if r["robusto int"] == "True" else "No"]
            for col, campo in ((1, "sh-men-P50"), (3, "sh-men-P75"), (5, "sh-men primero en"), (7, "sh-int primero en")):
                anotar("TM3_robust_ranking", c, m, col, "valor", fila[col], f8, f"modelo={m}, columna {campo}", float(r[campo].rstrip("*")), 0)
            rows.append(fila)
        bloques.append((f"\\textit{{{SUB[c]}}}", rows))
    cab = ("Model & P50 & P60 & P75 & P90 & First or tied, MoM (of 4) & Robust, MoM & First or tied, YoY (of 4) & Robust, YoY")
    cap = ("Rank of each model by MAE in shock months, pooled test windows 2021--2025, at the reporting thresholds P50, P60, P75 and P90 "
           "of the month-on-month (MoM) change. $^{*}$ = first or statistically tied with the first (the 95\\% paired bootstrap CI of the "
           "difference in MAE with the best model contains 0). A model is robust if it is first or tied in at least 3 of the 4 thresholds; "
           "the year-on-year (YoY) definition is evaluated separately and its ranks are not shown.")
    return tabla_latex("main_robust_ranking", cap, "lccccrcrc", cab, bloques)


def main() -> None:
    for sub in ("figures", "tables"):  # se regeneran completas, sin restos de una versión anterior (README.md se conserva)
        if (OUT / sub).exists():
            shutil.rmtree(OUT / sub)
        (OUT / sub).mkdir(parents=True)
    todas = [r for g in PRINCIPAL + SUPLEMENTARIO for r in g]
    if len(set(map(nombre, todas))) != len(todas):
        raise AssertionError("Nombre de figura repetido en la selección")
    for rel in todas:
        shutil.copy2(G / f"{rel}.pdf", OUT / "figures" / f"{nombre(rel)}.pdf")
    for rel in PNG_EXTRA:  # PNG para el main.tex antiguo; no entra en el zip ni en el .tex
        shutil.copy2(G / f"{rel}.png", OUT / "figures" / f"{nombre(rel)}.png")

    cab = ("% Figure captions, taken from the .txt file of each figure (08_graficos/) with internal references removed.\n"
           "% Generated by 02_scripts/12_paquete_overleaf.py.\n"
           "% Date of access to MIDAGRI-SISAGRI: fill in ONCE here; it is used by every caption and by Table S1.\n"
           "\\newcommand{\\midagridate}{[____]}\n\n"
           "% One \\newcommand per figure, named after the figure file: \\figcap{<file name>} prints its caption.\n"
           "\\newcommand{\\defcap}[2]{\\expandafter\\newcommand\\csname figcap-#1\\endcsname{#2}}\n"
           "\\newcommand{\\figcap}[1]{\\ifcsname figcap-#1\\endcsname\\csname figcap-#1\\endcsname\\else\\PackageError{captions}{No caption for #1}{}\\fi}\n\n")
    (OUT / "captions.tex").write_text(cab + "".join(f"\\defcap{{{nombre(r)}}}{{{a_tex(pie_articulo(r))}}}\n" for r in todas), encoding="utf-8")

    for archivo, grupos, titulo in (("figures_main.tex", PRINCIPAL, "main text"), ("figures_supp.tex", SUPLEMENTARIO, "supplementary material")):
        (OUT / archivo).write_text(f"% Figures, {titulo}, in order of appearance. Requires captions.tex and \\graphicspath{{{{figures/}}}}.\n"
                                   "% Subfigures carry no letter, so that (a), (b), (c) inside the figures keep their meaning.\n"
                                   "\\captionsetup[subfigure]{labelformat=empty}\n\n"
                                   + "\n".join(entorno(g) for g in grupos), encoding="utf-8")

    for nombre_t, f in zip(TABLAS_PRINCIPAL, (tm1, tm2, tm3)):
        (OUT / "tables" / f"{nombre_t}.tex").write_text(f(), encoding="utf-8")
    for rel, cambios in TABLAS_SUPLEMENTARIO:
        t = (BR / rel).read_text(encoding="utf-8")
        for a, b in cambios.items():
            if t.count(a) != 1:
                raise AssertionError(f"Texto a reemplazar no encontrado en {rel}: {a[:50]}")
            t = t.replace(a, b)
        t = re.sub(r"(?<!\\)%", r"\\%", t).replace(MIDAGRI_TXT, MIDAGRI_TEX)
        (OUT / "tables" / Path(rel).name).write_text(t, encoding="utf-8")

    def tabla_input(n: str) -> str:
        cuerpo = f"\\input{{tables/{n}}}"
        return f"\\begin{{landscape}}\n\\scriptsize\n\\setlength{{\\tabcolsep}}{{3pt}}\n{cuerpo}\n\\end{{landscape}}\n" if n in APAISADAS else cuerpo + "\n"

    (OUT / "tables_main.tex").write_text("% Tables, main text, in order of appearance (generated from the CSV files of 06_metricas/).\n\n"
                                         + "\n".join(tabla_input(n) for n in TABLAS_PRINCIPAL), encoding="utf-8")
    (OUT / "tables_supp.tex").write_text("% Tables, supplementary material, in order of appearance.\n\n"
                                         + "\n".join(tabla_input(Path(r).stem) for r, _ in TABLAS_SUPLEMENTARIO), encoding="utf-8")

    (OUT / "test_article.tex").write_text(
        "% Minimal test document (article class, not the MDPI template): compiles the whole package.\n"
        "\\documentclass[11pt]{article}\n\\usepackage[margin=2cm]{geometry}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n"
        "\\usepackage{graphicx}\n\\usepackage{caption}\n\\usepackage{subcaption}\n\\usepackage{booktabs}\n\\usepackage{longtable}\n"
        "\\usepackage{float}\n\\usepackage{pdflscape}\n"
        "\\graphicspath{{figures/}}\n\\input{captions}\n\n\\begin{document}\n\\section*{Main text}\n\\input{figures_main}\n\\input{tables_main}\n"
        "\\clearpage\n\\section*{Supplementary material}\n\\input{figures_supp}\n\\input{tables_supp}\n\\end{document}\n", encoding="utf-8")
    verificar()
    archivo_unico()


# ---------------------------------------------------------------- archivo único, zip de figuras y lista de figuras
def _sin_comentarios(t: str) -> str:
    return re.sub(r"(?m)(?<!\\)%.*$", "", t)


def _expandir(archivo: str) -> str:
    """Contenido de `archivo` con cada \\input{tables/X} sustituido por el texto de tables/X.tex."""
    def sub(m):
        n = m.group(1)
        cuerpo = (OUT / f"{n}.tex").read_text(encoding="utf-8").rstrip("\n")
        if Path(n).name == "TS1_provinces":  # "> 0" en texto: con fontenc OT1 se imprime "¡"; en modo matemático vale siempre
            cuerpo = cuerpo.replace(" > 0 ", " $>$ 0 ")
        return f"% --- {n}.tex\n{cuerpo}"
    return re.sub(r"\\input\{([^}]+)\}", sub, (OUT / archivo).read_text(encoding="utf-8")).rstrip("\n")


def archivo_unico() -> None:
    """resultados_v2_completo.tex (todo el paquete en un archivo, sin \\input ni \\usepackage), figures_overleaf.zip
    (solo los PDF, dentro de figures/) y lista_figuras.md (figura, PDF, label y pie en una línea)."""
    partes = ["% resultados_v2_completo.tex: whole Overleaf package in one file (body of the document, after \\begin{document}).\n"
              "% Generated by 02_scripts/12_paquete_overleaf.py.\n"
              "% Packages needed in the preamble of main.tex: graphicx, caption, subcaption, booktabs, longtable, float, pdflscape.\n"
              "% Figures: \\graphicspath{{figuras/}{figures/}} in main.tex; \\includegraphics uses only the file name.\n"
              "% Fill in the MIDAGRI-SISAGRI access date once, in \\midagridate below."]
    for archivo in ("captions.tex", "tables_main.tex", "figures_main.tex", None, "tables_supp.tex", "figures_supp.tex"):
        partes.append("\n\n% ===== SUPLEMENTARIO =====" if archivo is None else f"\n\n% ===== {archivo} =====\n{_expandir(archivo)}")
    texto = "".join(partes) + "\n"
    (OUT / UNICO).write_text(texto, encoding="utf-8")

    pdfs = sorted((OUT / "figures").glob("*.pdf"))
    with zipfile.ZipFile(OUT / ZIP_FIG, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(OUT / "figures", "figures/")
        for p in pdfs:
            z.write(p, f"figures/{p.name}")

    errores = []
    nombres_zip = [n for n in zipfile.ZipFile(OUT / ZIP_FIG).namelist() if not n.endswith("/")]
    errores += [f"en el zip algo que no es un PDF de figures/: {n}" for n in nombres_zip if not (n.startswith("figures/") and n.endswith(".pdf"))]
    en_zip = {Path(n).name for n in nombres_zip}
    inc = re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", texto)
    errores += [f"\\includegraphics con carpeta: {f}" for f in inc if "/" in f]
    errores += [f"\\includegraphics sin PDF en el zip: {f}" for f in inc if f not in en_zip]
    errores += [f"PDF del zip sin usar: {f}" for f in sorted(en_zip - set(inc))]
    errores += [f"{x} presente (línea {i + 1})" for i, l in enumerate(texto.splitlines()) for x in ("\\input", "\\usepackage") if x in l]
    errores += [f"referencia interna '{x}'" for x in INTERNAS if x in texto]
    sin_esc = re.sub(r"\\.", "", _sin_comentarios(texto))
    if sin_esc.count("{") != sin_esc.count("}"):
        errores.append("llaves desbalanceadas")
    for env in ("figure", "subfigure", "table", "tabular", "longtable", "landscape"):
        if texto.count(f"\\begin{{{env}}}") != texto.count(f"\\end{{{env}}}"):
            errores.append(f"entorno {env} desbalanceado")
    defs = dict(re.findall(r"^\\defcap\{([^}]+)\}\{(.*)\}$", texto, re.M))
    errores += [f"\\figcap sin \\defcap: {u}" for u in re.findall(r"\\figcap\{([^}]+)\}", _sin_comentarios(texto)) if u not in defs]
    if not (0 <= texto.find("\\newcommand{\\figcap}") < texto.find("\\defcap{") < texto.find("\\figcap{fig")):
        errores.append("las macros no están antes de su primer uso")
    if errores:
        raise SystemExit("ERRORES (archivo único):\n" + "\n".join(errores))

    planos = (("\\textminus{}", "−"), ("$\\Delta$", "Δ"), ("\\textbar{}", "|"), ("\\dag{}", "†"), ("\\textgreater{}", ">"),
              ("\\_", "_"), ("\\%", "%"), ("\\midagridate{}", "[____]"), ("\\textbf{", ""), ("\\textit{", ""))

    def plano(s: str) -> str:
        s = re.sub(r"\\figcap\{([^}]+)\}", lambda m: defs[m.group(1)], s)
        for a, b in planos:
            s = s.replace(a, b)
        return s.replace("}", "")

    md = ["# Lista de figuras de resultados_v2_completo.tex", "", "| # | Parte | Archivo(s) PDF | Label | Pie (una línea) |", "|---|---|---|---|---|"]
    sup, k = False, 0
    for m in re.finditer(r"% ===== SUPLEMENTARIO =====|\\begin\{figure\}.*?\\end\{figure\}", texto, re.S):
        if m.group(0).startswith("%"):
            sup = True
            continue
        b, k = m.group(0), k + 1
        lab = re.findall(r"\\label\{(fig:[^}]+)\}\n\\end\{figure\}", b)[0]
        cap = re.findall(r"\\caption\{(.*)\}\n\\label\{" + re.escape(lab) + r"\}", b)[0]
        pdf = "<br>".join(re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", b))
        md.append(f"| {k} | {'Supl.' if sup else 'Principal'} | {pdf} | `\\label{{{lab}}}` | {plano(cap)} |")
    (OUT / LISTA).write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"{UNICO}: {len(texto.splitlines())} líneas, {len(inc)} includegraphics; {ZIP_FIG}: {len(en_zip)} PDF; {LISTA}: {k} figuras. "
          "Verificación del archivo único OK")


def celda_tex(c: dict) -> str:
    """Lee de nuevo la celda en el .tex escrito: bloque del cultivar, fila por su primera columna, columna por posición."""
    lineas = (OUT / "tables" / f"{c['tabla']}.tex").read_text(encoding="utf-8").splitlines()
    i = next(k for k, l in enumerate(lineas) if l.startswith("\\multicolumn") and f"\\textit{{{SUB[c['cultivar']]}}}" in l)
    for l in lineas[i + 1:]:
        if l.startswith("\\multicolumn") or l.startswith("\\bottomrule"):
            break
        partes = [p.strip() for p in l.rstrip("\\ ").split(" & ")]
        if partes[0] == c["fila"]:
            t = partes[c["col"]]
            if c["parte"] == "valor":
                return t.split(" (")[0].replace("$^{*}$", "")
            lo, hi = t.split(" (")[1].rstrip(")").split("--")
            return lo if c["parte"] == "lo" else hi
    raise KeyError(c)


def verificar() -> None:
    errores = []
    tex = {p.name: p.read_text(encoding="utf-8") for p in OUT.glob("*.tex") if p.name != UNICO}  # el archivo único se verifica aparte
    tablas = {p.name: p.read_text(encoding="utf-8") for p in (OUT / "tables").glob("*.tex")}
    inc = [m for f in ("figures_main.tex", "figures_supp.tex") for m in re.findall(r"\\includegraphics\[[^\]]*\]\{([^}]+)\}", tex[f])]
    errores += [f"falta figures/{f}" for f in inc if not (OUT / "figures" / f).exists()]
    errores += [f"includegraphics repetido: {f}" for f in set(inc) if inc.count(f) > 1]
    errores += [f"PDF sin usar: {f}" for f in sorted({p.name for p in (OUT / "figures").glob("*.pdf")} - set(inc))]
    inputs = [m for t in tex.values() for m in re.findall(r"\\input\{([^}]+)\}", t)]
    errores += [f"\\input sin archivo: {i}" for i in inputs if not (OUT / f"{i}.tex").exists()]
    errores += [f"tabla sin \\input: {n}" for n in tablas if f"tables/{Path(n).stem}" not in inputs]
    labs = [m for t in list(tex.values()) + list(tablas.values()) for m in re.findall(r"\\label\{([^}]+)\}", t)]
    errores += [f"label repetido: {l}" for l in set(labs) if labs.count(l) > 1]
    pies = dict(re.findall(r"^\\defcap\{([^}]+)\}\{(.*)\}$", tex["captions.tex"], re.M))
    usados = [m for f in ("figures_main.tex", "figures_supp.tex") for m in re.findall(r"\\figcap\{([^}]+)\}", tex[f])]
    errores += [f"pie sin definir: {u}" for u in usados if u not in pies]
    errores += [f"pie definido y no usado: {u}" for u in pies if u not in usados]
    rel = {nombre(r): r for g in PRINCIPAL + SUPLEMENTARIO for r in g}
    errores += [f"pie distinto del TXT (tras los reemplazos): {n}" for n, t in pies.items() if de_tex(t) != pie_articulo(rel[n])]
    n_reemp = sum(pie_txt(r) != pie_articulo(r) for r in rel.values())
    for f in ("figures_main.tex", "figures_supp.tex"):
        for bloque in re.findall(r"\\begin\{figure\}.*?\\end\{figure\}", tex[f], re.S):
            lab = re.search(r"\\label\{fig:([^}]+)\}\n\\end\{figure\}", bloque).group(1)
            if lab.startswith(EXPLORATORIAS):
                principal = re.findall(r"\\caption\{(.*)\}\n\\label\{fig:" + re.escape(lab) + r"\}", bloque)[0]
                if "EXPLORATORY" not in re.sub(r"\\figcap\{([^}]+)\}", lambda m: pies[m.group(1)], principal):
                    errores.append(f"sin marca EXPLORATORY: {lab}")
    for n, t in [("captions.tex", tex["captions.tex"])] + list(tablas.items()):
        errores += [f"referencia interna '{x}' en {n}" for x in INTERNAS if x in t]
    for n, t in list(tex.items()) + list(tablas.items()):
        sin_esc = re.sub(r"\\.", "", t)
        if sin_esc.count("{") != sin_esc.count("}"):
            errores.append(f"llaves desbalanceadas en {n}")
        if n in tablas and re.search(r"(?<!\\)%", t):
            errores.append(f"'%' sin escapar en tables/{n}")
    # celdas de las tablas principales: todas contra el CSV, y 5 al azar mostradas
    for c in CELDAS:
        if celda_tex(c) != c["texto"].split(" (")[0].replace("$^{*}$", "") and c["parte"] == "valor":
            errores.append(f"celda distinta: {c['tabla']} {c['fila']}")
        leido = float(celda_tex(c).replace(",", ""))
        if abs(leido - round(c["valor"], c["dec"])) > 10 ** -(c["dec"] + 3):
            errores.append(f"celda no coincide con el CSV: {c['tabla']} {c['cultivar']} {c['fila']} col {c['col']} {c['parte']}")
    muestra = random.Random(20261029).sample(CELDAS, 5)
    print("Muestra de 5 celdas (valor en la tabla | valor en el CSV):")
    for c in muestra:
        print(f"  {c['tabla']} [{SUB[c['cultivar']]}, fila {c['fila']}, col {c['col']}, {c['parte']}]: {celda_tex(c)} | "
              f"{c['valor']!r}  <- {c['csv']} ({c['consulta']})")
    n_fig = sum(len(re.findall(r"\\begin\{figure\}", tex[f])) for f in ("figures_main.tex", "figures_supp.tex"))
    print(f"figure: {n_fig}; includegraphics: {len(inc)}; PDF: {len(list((OUT / 'figures').glob('*.pdf')))}; pies: {len(pies)} "
          f"({n_reemp} con reemplazos); labels: {len(labs)}; tablas: {len(tablas)}; \\input: {len(inputs)}; celdas comprobadas: {len(CELDAS)}")
    if errores:
        raise SystemExit("ERRORES:\n" + "\n".join(errores))
    print("Verificación OK")


if __name__ == "__main__":
    main()
