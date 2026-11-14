"""R2-T16: lista de cifras clave para el texto del manuscrito (en ingles), una por linea, con su tabla de origen.
POSTERIOR AL PROTOCOLO. Solo lee CSV de 13_revision_r2/resultados/ (y, para el contexto, los CSV publicados que esos
analisis reproducen); no calcula metricas nuevas. Mismo formato numerico que las tablas LaTeX (t15_latex.py).
Salida: 13_revision_r2/CIFRAS_CLAVE.md
Uso: python 13_revision_r2/scripts/t16_cifras_clave.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import r2lib as R  # noqa: E402
from lib.entorno import preparar_entorno  # noqa: E402

preparar_entorno()

import math  # noqa: E402

import pandas as pd  # noqa: E402

DEC = {"sutil": 0, "dulce": 1}
CROP = {"sutil": "Sour lime", "dulce": "Sweet lime"}
SCOPE = {"todos": "all months", "shock_MoM_P75": "MoM P75 shock months", "shock_YoY_P75": "YoY P75 shock months"}
L: list[str] = []


def leer(n: str) -> pd.DataFrame:
    return pd.read_csv(R.RES / n, dtype={"fecha": str})


def nan(x) -> bool:
    return x is None or (isinstance(x, float) and math.isnan(x))


def f(x, d: int) -> str:
    if nan(x):
        return "n/a"
    s = f"{abs(float(x)):,.{d}f}"
    return ("−" if float(x) < 0 and float(s.replace(",", "")) != 0 else "") + s


def ci(lo, hi, d) -> str:
    return "" if nan(lo) else f" [95% CI {f(lo, d)}; {f(hi, d)}]"


def p(x) -> str:
    return "n/a" if nan(x) else ("p < 0.001" if float(x) < 0.001 else f"p = {float(x):.3f}")


def sec(t: str) -> None:
    L.extend(["", f"## {t}", ""])


def add(txt: str, fuente: str) -> None:
    L.append(f"- {txt} — *{fuente}*")


# ---------------------------------------------------------------------------- T1
sec("ETS and Theta added to the 2021–2025 comparison (obs. R2-T1)")
src = "tab_r2_accuracy; T1_metricas_12_modelos_2021_2025.csv"
d = leer("T1_metricas_12_modelos_2021_2025.csv")
for c in DEC:
    x = d[(d.cultivo == c) & (d.definicion_shock == "MoM")].set_index("modelo")
    y = d[(d.cultivo == c) & (d.definicion_shock == "YoY")].set_index("modelo")
    k = DEC[c]
    for m in ("Chronos", "SARIMA", "SARIMA-sel", "ETS", "Theta"):
        r = x.loc[m]
        add(f"{CROP[c]}, {m}, all months (n = {int(r.n_shock + r.n_normal)}): MAE = {f(r.MAE, k)} t{ci(r.IC_MAE_lo, r.IC_MAE_hi, k)}", src)
        add(f"{CROP[c]}, {m}, MoM P75 shock months (n = {int(r.n_shock)}): MAE = {f(r.MAE_shock, k)} t{ci(r.IC_shock_lo, r.IC_shock_hi, k)}; "
            f"Δs = {f(r.Delta_s, 1)}%; MASE_shock = {f(r.MASE_shock, 2)}", src)
        r = y.loc[m]
        add(f"{CROP[c]}, {m}, YoY P75 shock months (n = {int(r.n_shock)}): MAE = {f(r.MAE_shock, k)} t{ci(r.IC_shock_lo, r.IC_shock_hi, k)}", src)
src = "T1_DM_HLN_vs_mejor.csv"
dm = leer("T1_DM_HLN_vs_mejor.csv")
TIPO_REF = {"referencia_G7": "reference model of the first-round review", "menor_MAE_10_modelos": "lowest all-month MAE among the ten models"}
for r in dm.itertuples(index=False):
    add(f"{CROP[r.cultivo]}, {r.modelo} vs. {r.referencia} ({TIPO_REF.get(r.tipo_referencia, r.tipo_referencia)}),{SCOPE.get(r.alcance, r.alcance)} (n = {int(r.n)}): "
        f"mean loss difference = {f(r.d_media, DEC[r.cultivo])} t, DM-HLN = {f(r.HLN, 2)}, {p(r.p)}", src)
src = "tab_r2_ranking; T1_robustez_3de4.csv"
rob = leer("T1_robustez_3de4.csv")
for c in DEC:
    for dfn in ("MoM", "YoY"):
        for g in ("10_modelos", "12_modelos"):
            z = rob[(rob.grupo == g) & (rob.cultivo == c) & (rob.definicion == dfn) & rob.consistently_top_ranked]
            add(f"{CROP[c]}, {dfn}, consistently top-ranked among {g[:2]} models: "
                f"{', '.join(f'{a} ({int(b)}/4)' for a, b in zip(z.modelo, z.n_primero_de_4)) or 'none'}", src)

# ---------------------------------------------------------------------------- T2
sec("Ranking in 2025 only (obs. R2-T2)")
src = "tab_r2_2025; T2_ranking_2025.csv"
t2 = leer("T2_ranking_2025.csv")
for c in DEC:
    for cr in SCOPE:
        x = t2[(t2.cultivo == c) & (t2.criterio == cr)]
        if int(x.n_meses.iloc[0]) == 0:
            add(f"{CROP[c]}, 2025: no {SCOPE[cr]} (n = 0); no ranking", src)
            continue
        top = x[x.primero_o_empate_2025]
        first = x.sort_values("posicion_2025").iloc[0]
        add(f"{CROP[c]}, 2025, {SCOPE[cr]} (n = {int(first.n_meses)}): first = {first.modelo}, MAE = {f(first.MAE_2025, DEC[c])} t"
            f"{ci(first.IC_lo, first.IC_hi, DEC[c])}; {len(top)} of 12 models first or tied", src)

# ---------------------------------------------------------------------------- T3
sec("SARIMA constant (obs. R2-T3)")
src = "T3_2_sin_constante_pool.csv"
for r in leer("T3_2_sin_constante_pool.csv").itertuples(index=False):
    k = DEC[r.cultivo]
    add(f"{CROP[r.cultivo]}, fixed SARIMA without vs. with constant, {SCOPE.get(r.alcance, r.alcance)} (n = {int(r.n_meses)}): "
        f"MAE {f(r.MAE_sin_c, k)} vs. {f(r.MAE_original_con_c, k)} t; difference = {f(r.dif_sin_menos_con, k)} t{ci(r.IC95_dif_lo, r.IC95_dif_hi, k)}", src)

# ---------------------------------------------------------------------------- T5 / E1
sec("SARIMA-sel fallback rule in experiment E1 (obs. R2-T5)")
src = "tab_r2_sarima_sel_fallback; T5_SARIMA_sel_Y1_pool.csv, T3_3_SARIMA_sel_Y1_con_regla_pool.csv"
t5 = leer("T5_SARIMA_sel_Y1_pool.csv")
t3 = leer("T3_3_SARIMA_sel_Y1_con_regla_pool.csv")
nombre = {"SARIMA-sel": "SARIMA-sel (protocol)", "SARIMA-sel-Y1": "SARIMA-sel-Y1 (E1, published)", "SARIMA-sel-Y1-R": "SARIMA-sel-Y1 + rule 2 (validation MAE)"}
for r in t5[t5.alcance.isin(["todos", "shock_MoM_P75"])].itertuples(index=False):
    k = DEC[r.cultivo]
    add(f"{CROP[r.cultivo]}, {nombre[r.modelo]}, {SCOPE[r.alcance]} (n = {int(r.n_meses)}): MAE = {f(r.MAE, k)} t{ci(r.IC_lo, r.IC_hi, k)}; "
        f"DM-HLN vs. {r.mejor} = {f(r.DM_HLN, 2)}, {p(r.DM_p)}", src)
r = t3[(t3.cultivo == "sutil") & (t3.alcance == "todos")].iloc[0]
add(f"Sour lime, SARIMA-sel-Y1 + rule 1 (next by AIC), all months (n = 60): MAE = {f(r.MAE_SARIMA_sel_Y1_con_regla, 0)} t (no CI)", src)
add(f"Sour lime, 2021 window (n = 12), SARIMA-sel-Y1: published {f(r.MAE_2021_publicado, 0)} t; rule 1 {f(r.MAE_2021_con_regla, 0)} t; "
    f"rule 2 {f(r.MAE_2021_alternativa_B, 0)} t", src)

# ---------------------------------------------------------------------------- T6 / T7
sec("Seasonal lag y(T−12) in the tabular models, E5 (obs. R2-T6)")
src = "tab_r2_e5_ablation (Table E5); T6_E5_y12_tabulares.csv"
for r in leer("T6_E5_y12_tabulares.csv").itertuples(index=False):
    if r.alcance == "shock_YoY_P75":
        continue
    k = DEC[r.cultivo]
    sem = "" if nan(r.semillas_E5_mejoran_de_10) else f"; {int(r.semillas_E5_mejoran_de_10)}/10 seeds improve"
    add(f"{CROP[r.cultivo]}, {r.modelo}, {SCOPE[r.alcance]} (n = {int(r.n_meses)}): MAE {f(r.MAE_original, k)} → {f(r.MAE_E5, k)} t; "
        f"E5 − original = {f(r.dif_E5_menos_orig, k)} t{ci(r.IC_dif_lo, r.IC_dif_hi, k)}; y(T−12) only = {f(r.dif_y12_mismas_filas, k)} t"
        f"{ci(r.IC_dif_y12_lo, r.IC_dif_y12_hi, k)}{sem}; E5 vs. {r.mejor}: {p(r.DM_E5_vs_mejor_p)}", src)
sec("Block ablation (obs. R2-T7.1)")
src = "tab_r2_e5_ablation (block ablation); T7_ablacion_bloques.csv"
for r in leer("T7_ablacion_bloques.csv").itertuples(index=False):
    if nan(r.dif_vs_anterior):
        continue
    k = DEC[r.cultivo]
    add(f"{CROP[r.cultivo]}, {r.modelo}, adding block {r.conjunto[:3]} ({r.conjunto[4:]}), {SCOPE[r.alcance]} (n = {int(r.n_meses)}): "
        f"difference = {f(r.dif_vs_anterior, k)} t{ci(r.IC_dif_lo, r.IC_dif_hi, k)}", src)
sec("SARIMAX (obs. R2-T7.2)")
src = "tab_r2_sarimax; T7_sarimax_vs_sarima.csv"
for r in leer("T7_sarimax_vs_sarima.csv").itertuples(index=False):
    if r.modelo == "SARIMA" or r.alcance == "shock_YoY_P75":
        continue
    k = DEC[r.cultivo]
    add(f"{CROP[r.cultivo]}, {r.modelo}, {SCOPE[r.alcance]} (n = {int(r.n_meses)}): MAE = {f(r.MAE, k)} t{ci(r.IC_lo, r.IC_hi, k)}; "
        f"vs. SARIMA {f(r.dif_vs_SARIMA, k)} t{ci(r.IC_dif_lo, r.IC_dif_hi, k)}, {p(r.DM_p)}", src)

# ---------------------------------------------------------------------------- T8
sec("Ex-ante large-change months and El Niño costero months (obs. R2-T8)")
src = "tab_r2_exante; T8_metricas_ex_ante.csv, T8_robustez_ex_ante.csv"
t8 = leer("T8_metricas_ex_ante.csv")
r8 = leer("T8_robustez_ex_ante.csv")
DEF = {"A_SN_anticipado": "A (seasonal-naive anticipated, P75)", "B_SARIMA_anticipado": "B (SARIMA anticipated, P75)", "C_Nino_costero": "C (El Niño costero)"}
for c in DEC:
    for dfn, nom in DEF.items():
        x = t8[(t8.cultivo == c) & (t8.definicion == dfn) & ((t8.percentil == 75) if dfn[0] != "C" else t8.percentil.isna())]
        b = x.sort_values("posicion").iloc[0]
        add(f"{CROP[c]}, definition {nom}: {int(b.n_meses)} months, {int(b.coinciden_con_shock_MoM_P75_real)} of them among the "
            f"{int(b.n_shock_MoM_P75_real)} ex-post MoM P75 shock months; first = {b.modelo}, MAE = {f(b.MAE, DEC[c])} t{ci(b.IC_lo, b.IC_hi, DEC[c])}", src)
        if dfn[0] != "C":
            z = r8[(r8.cultivo == c) & (r8.definicion == dfn) & r8.consistently_top_ranked]
            add(f"{CROP[c]}, definition {nom[:1]}: consistently top-ranked = {', '.join(z.modelo) or 'none'}", src)

# ---------------------------------------------------------------------------- T9
sec("Two-step-ahead horizon, h = 2 (obs. R2-T9)")
src = "tab_r2_h2; T9_metricas_h2.csv, T9_robustez_h2.csv"
t9 = leer("T9_metricas_h2.csv")
r9 = leer("T9_robustez_h2.csv")
for c in DEC:
    for a in ("todos", "shock_MoM_P75"):
        for r in t9[(t9.cultivo == c) & (t9.alcance == a)].itertuples(index=False):
            if r.modelo not in ("Chronos", "SARIMA", "SARIMA-sel", "Seasonal Naive", "ETS", "Theta"):
                continue
            k = DEC[c]
            add(f"{CROP[c]}, {r.modelo}, h = 2, {SCOPE[a]} (n = {int(r.n_meses)}): MAE = {f(r.MAE, k)} t{ci(r.IC_lo, r.IC_hi, k)} "
                f"(h = 1: {f(r.MAE_h1, k)} t); rank {int(r.posicion)}{'*' if r.primero_o_empate else ''}", src)
    z = r9[(r9.cultivo == c) & r9.consistently_top_ranked]
    add(f"{CROP[c]}, h = 2, consistently top-ranked (MoM): {', '.join(z.modelo) or 'none'}", src)

# ---------------------------------------------------------------------------- T10
sec("CRPS and threshold-weighted CRPS (obs. R2-T10)")
src = "tab_r2_crps; T10_crps_resumen.csv, T10_crps_por_mes.csv"
for r in leer("T10_crps_resumen.csv").itertuples(index=False):
    if r.metrica == "CRPS_normal_exacto":
        continue
    k = DEC[r.cultivo]
    extra = "" if nan(r.dif_vs_SARIMA) else f"; vs. SARIMA {f(r.dif_vs_SARIMA, k)} t{ci(r.IC_dif_lo, r.IC_dif_hi, k)}, {p(r.DM_p)}"
    add(f"{CROP[r.cultivo]}, {r.modelo}, {r.metrica.replace('_Q', '')}, {SCOPE[r.alcance]} (n = {int(r.n_meses)}): "
        f"{f(r.media, k)} t{ci(r.IC_lo, r.IC_hi, k)}{extra}", src)
pm = leer("T10_crps_por_mes.csv")
for (c, m), g in pm.groupby(["cultivar", "modelo"], sort=False):
    add(f"{CROP[c]}, {m}: empirical coverage of the 10–90% interval = {100 * g.cobertura_80.mean():.1f}% (n = {len(g)}; nominal 80%)", src)

# ---------------------------------------------------------------------------- T12
sec("Descriptive windows 2018–2020 (obs. R2-T12)")
src = "tab_r2_2018_2020; T12_ventanas_2018_2020.csv"
for r in leer("T12_ventanas_2018_2020.csv").itertuples(index=False):
    k = DEC[r.cultivo]
    add(f"{CROP[r.cultivo]}, {r.ventana}, {r.modelo}, {SCOPE[r.meses]} (n = {int(r.n_meses)}): MAE = {f(r.MAE, k)} t{ci(r.IC_lo, r.IC_hi, k)}"
        f"{'' if nan(r.MASE) else f'; MASE = {f(r.MASE, 2)}'}{'; first or tied' if r.primero_o_empate is True or str(r.primero_o_empate) == 'True' else ''}", src)

# ---------------------------------------------------------------------------- T13
sec("Data coverage of the frozen input tables (obs. R2-T13)")
src = "T13_cobertura_datos.csv"
FUENTE_EN = {"produccion nacional sutil": "National production, sour lime (MIDAGRI–SISAGRI)",
             "produccion distrital sutil": "District production, sour lime (MIDAGRI–SISAGRI, after the ETL year filter)",
             "produccion nacional dulce": "National production, sweet lime (MIDAGRI–SISAGRI)",
             "produccion distrital dulce": "District production, sweet lime (MIDAGRI–SISAGRI, after the ETL year filter)",
             "clima NASA POWER": "Climate, NASA POWER (109 provinces)",
             "emergencias INDECI/SINPAD": "Emergencies, INDECI/SINPAD (province × month panel)",
             "noticias Agraria.pe": "News, Agraria.pe (monthly sentiment; value = number of articles)"}
for r in leer("T13_cobertura_datos.csv").itertuples(index=False):
    r = r._replace(fuente=next(v for k, v in FUENTE_EN.items() if r.fuente.startswith(k)))
    pos = "" if nan(r.primer_mes_con_valor_positivo) else f"; first month with a positive value {r.primer_mes_con_valor_positivo}"
    cero = "" if nan(r.meses_con_valor_0) else f"; months with value 0: {r.meses_con_valor_0}"
    add(f"{r.fuente}: {r.primer_mes}–{r.ultimo_mes}, {int(r.n_meses)} months{pos}{cero}", src)

cab = ["# Key figures for the manuscript text (review round 2)", "",
       "<!-- generated by scripts/t16_cifras_clave.py; do not edit by hand -->", "",
       "Every figure below is copied from a CSV in `13_revision_r2/resultados/` (named after each line, with the LaTeX table "
       "in `latex/` that shows it). MAE in tonnes (t); sour lime without decimals, sweet lime with one; 95% CI: paired "
       "bootstrap of months within each test window (B = 10,000, seed 42); DM: Diebold–Mariano with HLN correction, absolute "
       "loss. Unless stated otherwise: pool of test windows 2021–2025 (60 months per crop). All analyses in this list are "
       "post-protocol (second review round) and do not modify the pre-registered ten-model ranking. * = first or tied with the first."]
(R.R2 / "CIFRAS_CLAVE.md").write_text("\n".join(cab + L) + "\n", encoding="utf-8", newline="\n")
print(f"CIFRAS_CLAVE.md: {sum(1 for x in L if x.startswith('- '))} figures")
