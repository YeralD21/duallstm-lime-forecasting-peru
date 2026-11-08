"""Fase 5 (E): verificación celda a celda de %USERPROFILE%/Downloads/tablas_revision_g7.tex frente a los CSV.

Solo lectura de los CSV; no calcula métricas nuevas salvo: rangos por MAE (ordenar una columna de T1) y la
cifra 3,183 de la nota (a), que es la media de 5 MAE por ventana, como en INFORME_FASE3.md l. 117.
Criterio: la cifra del .tex coincide si |csv - tex| <= 0,5 * 10^-d (d = decimales mostrados en el .tex) + 1e-9.
Salida: 09_reportes/revision_g7/fase5/E_verificacion_tablas.csv
"""
from __future__ import annotations

import os
import re
from pathlib import Path

import pandas as pd

AQUI = Path(__file__).resolve().parent
BR = AQUI.parents[3]
TEX = Path(os.environ.get("USERPROFILE", str(Path.home()))) / "Downloads" / "tablas_revision_g7.tex"
SAL = AQUI.parent / "E_verificacion_tablas.csv"

F_T1 = "12_revision_g7/resultados/T1_metricas_P75_MoM_YoY.csv"
F_T5 = "12_revision_g7/resultados/T5_DM_HLN_vs_mejor_univariado.csv"
F_E2 = "09_reportes/revision_g7/fase1/E2_razon_val_train_gt2.csv"
F_ERR = "12_revision_g7/resultados/errores_test_promediados_semillas_g7.csv"
F_T06 = "06_metricas/agregadas/T06_agregadas_IC.csv"
ORIG = ["Naive", "Seasonal Naive", "Chronos", "SARIMA", "SARIMA-sel", "Ridge", "ElasticNet", "XGB-37", "GC3", "GE"]
CUL = ["sutil", "dulce"]

T1 = pd.read_csv(BR / F_T1)
T5 = pd.read_csv(BR / F_T5)
E2 = pd.read_csv(BR / F_E2)
ERR = pd.read_csv(BR / F_ERR)
T06 = pd.read_csv(BR / F_T06)
FILAS: list[dict] = []


def t1(c, m, col, pool="principal_2021_2025"):
    r = T1[(T1.cultivo == c) & (T1.pool == pool) & (T1.modelo == m)]
    assert len(r) == 1, (c, m, pool)
    return float(r[col].iloc[0])


def num(s: str) -> tuple[float | None, int, str]:
    """Valor, decimales y marca de una celda: '\\textbf{4,784}' -> (4784, 0, 'bold'); '$<$0.001' -> (0.001, 3, '<')."""
    marca = "bold" if "textbf" in s else ""
    s2 = re.sub(r"\\textbf\{(.*?)\}", r"\1", s).replace("$^{a}$", "").replace("$-$", "-").replace("$<$", "<").strip()
    if s2.startswith("<"):
        marca, s2 = "<", s2[1:]
    s2 = s2.replace(",", "").replace("+", "")
    if s2 in ("", "--", "-"):
        return None, 0, marca
    d = len(s2.split(".")[1]) if "." in s2 else 0
    return float(s2), d, marca


def chequear(tabla, fila, columna, celda_tex, valor_csv, archivo, nota=""):
    v, d, marca = num(celda_tex)
    if marca == "<":
        ok = valor_csv < v
    elif v is None:
        ok = None
    else:
        ok = abs(valor_csv - v) <= 0.5 * 10 ** (-d) + 1e-9
    FILAS.append({"tabla": tabla, "fila": fila, "columna": columna, "valor_tex": celda_tex.strip(),
                  "valor_csv": valor_csv, "archivo": archivo, "coincide": ok, "nota": nota})


def celdas(linea: str) -> list[str]:
    return [x.strip() for x in linea.split("\\\\")[0].split("&")]


def tabla_por_label(txt: str, label: str) -> list[str]:
    i = txt.index(label)
    ini = txt.rfind(r"\begin{table}", 0, i)
    fin = txt.index(r"\end{table}", i)
    return txt[ini:fin].splitlines()


def tab_shock_scaled(txt):
    L = tabla_por_label(txt, "tab:shock_scaled")
    cols = [(c, dfn, met) for c in CUL for dfn in ("MoM", "YoY") for met in ("MAE_shock", "MASE_shock", "MAE_shock_rel_SNaive")]
    filas = [l for l in L if l.split("&")[0].strip() in ORIG]
    assert len(filas) == 10
    for l in filas:
        cs = celdas(l)
        m = cs[0]
        for (c, dfn, met), celda in zip(cols, cs[1:]):
            chequear("tab:shock_scaled", m, f"{c} {dfn} {met}", celda, t1(c, m, f"{met}_{dfn}"), F_T1)
    # negritas = mínimo de la columna (MAE_sh y MASE_sh)
    for c in CUL:
        for dfn in ("MoM", "YoY"):
            for met in ("MAE_shock", "MASE_shock"):
                j = cols.index((c, dfn, met)) + 1
                tex_bold = [celdas(l)[0] for l in filas if "textbf" in celdas(l)[j]]
                mejor = min(ORIG, key=lambda m: t1(c, m, f"{met}_{dfn}"))
                FILAS.append({"tabla": "tab:shock_scaled", "fila": "(negrita)", "columna": f"{c} {dfn} {met}",
                              "valor_tex": ",".join(tex_bold), "valor_csv": mejor, "archivo": F_T1,
                              "coincide": tex_bold == [mejor], "nota": "negrita = mínimo de la columna"})
    # n de shocks del pie
    cap = "\n".join(L)
    for c, nombre in (("sutil", "sour lime"), ("dulce", "sweet lime")):
        m = re.search(nombre + r" (\d+) \(MoM\) and (\d+) \(YoY\)", cap)
        for k, dfn in enumerate(("MoM", "YoY")):
            chequear("tab:shock_scaled", "(pie)", f"n shocks {c} {dfn}", m.group(k + 1), t1(c, "Naive", f"n_shock_{dfn}"), F_T1)


def tab_diag(txt):
    L = tabla_por_label(txt, "tab:diag_experiments")
    ref = {"sutil": "Chronos", "dulce": "SARIMA-sel"}
    for l in L:
        if "&" not in l or "Model" in l or "Sour lime" in l:
            continue
        cs = celdas(l)
        if len(cs) != 6:
            continue
        mod = cs[1]
        if mod == "Chronos / SARIMA-sel":
            for c, celda in zip(CUL, (cs[2], cs[4])):
                chequear("tab:diag_experiments", f"Reference {ref[c]}", f"{c} MAE", celda, t1(c, ref[c], "MAE"), F_T1)
            continue
        for c, cm, cd in (("sutil", cs[2], cs[3]), ("dulce", cs[4], cs[5])):
            chequear("tab:diag_experiments", mod, f"{c} MAE", cm, t1(c, mod, "MAE"), F_T1)
            if cd:
                r = T5[(T5.cultivo == c) & (T5.pool == "principal_2021_2025") & (T5.modelo == mod) & (T5.alcance == "global")]
                assert len(r) == 1 and r.referencia.iloc[0] == ref[c], (c, mod)
                mm = re.match(r"(.*)\((.*)\)", cd)
                chequear("tab:diag_experiments", mod, f"{c} d_media vs {ref[c]}", mm.group(1), float(r.d_media.iloc[0]), F_T5)
                chequear("tab:diag_experiments", mod, f"{c} p (DM-HLN)", mm.group(2), float(r.p.iloc[0]), F_T5)
    # nota (a)
    nota = "\n".join(L[L.index(next(l for l in L if "$^{a}$ The" in l)):]) if any("$^{a}$ The" in l for l in L) else ""
    if not nota:
        nota = next(l for l in open(TEX, encoding="utf-8") if "$^{a}$ The reestimation" in l)
    e = ERR[(ERR.cultivar == "sutil")]
    mae_w = e.groupby(["modelo", "anio_test"]).ae.mean()
    m1 = re.search(r"MAE ([\d,]+)~t\)", nota).group(1)
    chequear("tab:diag_experiments", "nota (a)", "MAE SARIMA-sel-Y1 sutil 2021", m1, float(mae_w.loc[("SARIMA-sel-Y1", 2021)]), F_ERR)
    alt = (mae_w.loc[("SARIMA-sel", 2021)] + sum(mae_w.loc[("SARIMA-sel-Y1", y)] for y in range(2022, 2026))) / 5
    m2 = re.search(r"would be ([\d,]+)~t", nota).group(1)
    chequear("tab:diag_experiments", "nota (a)", "MAE pool con SARIMA-sel original en 2021", m2, float(alt), F_ERR,
             "media de 5 MAE por ventana (INFORME_FASE3 l. 117)")


def tab_supp(txt):
    L = tabla_por_label(txt, "tab:supp_metrics")
    c = None
    rank = {}
    for cc in CUL:
        for pool, k in (("principal_2021_2025", "R1"), ("sensibilidad_2023_2025", "R2")):
            s = T1[(T1.cultivo == cc) & (T1.pool == pool) & T1.modelo.isin(ORIG)].set_index("modelo").MAE
            rank[(cc, k)] = s.rank(method="min").astype(int)
    for l in L:
        if "Sour lime" in l:
            c = "sutil"; continue
        if "Sweet lime" in l:
            c = "dulce"; continue
        if c is None or "&" not in l:
            continue
        cs = celdas(l)
        m = cs[0]
        if m not in ORIG:
            continue
        chequear("tab:supp_metrics", m, f"{c} MAE", cs[1], t1(c, m, "MAE"), F_T1)
        lo, hi = cs[2].split("--")
        chequear("tab:supp_metrics", m, f"{c} IC iid lo", lo, t1(c, m, "IC_iid_lo"), F_T1)
        chequear("tab:supp_metrics", m, f"{c} IC iid hi", hi, t1(c, m, "IC_iid_hi"), F_T1)
        lo, hi = cs[3].split("--")
        chequear("tab:supp_metrics", m, f"{c} IC bloques lo", lo, t1(c, m, "IC_bloques_lo"), F_T1)
        chequear("tab:supp_metrics", m, f"{c} IC bloques hi", hi, t1(c, m, "IC_bloques_hi"), F_T1)
        chequear("tab:supp_metrics", m, f"{c} RMSE", cs[4], t1(c, m, "RMSE"), F_T1)
        chequear("tab:supp_metrics", m, f"{c} MASE", cs[5], t1(c, m, "MASE"), F_T1)
        r1, r2 = cs[6].split("/")
        chequear("tab:supp_metrics", m, f"{c} rango R1 (MAE 2021-2025)", r1, float(rank[(c, "R1")][m]), F_T1, "rango de la columna MAE")
        chequear("tab:supp_metrics", m, f"{c} rango R2 (MAE 2023-2025)", r2, float(rank[(c, "R2")][m]), F_T1, "rango de la columna MAE, pool sensibilidad")
        if cs[7] != "--":
            a, b = cs[7].split("/")
            r = E2[(E2.cultivar == c) & (E2.modelo == m)]
            chequear("tab:supp_metrics", m, f"{c} sobreajuste n>2", a, float(r.n_razon_gt_2.iloc[0]), F_E2)
            chequear("tab:supp_metrics", m, f"{c} sobreajuste n unidades", b, float(r.n_unidades.iloc[0]), F_E2)
        else:
            FILAS.append({"tabla": "tab:supp_metrics", "fila": m, "columna": f"{c} sobreajuste", "valor_tex": "--",
                          "valor_csv": "(sin fila en E2: modelo sin entrenamiento)", "archivo": F_E2,
                          "coincide": not ((E2.cultivar == c) & (E2.modelo == m)).any(), "nota": ""})


def control_t06():
    """T1 (12_revision_g7) frente a T06 (06_metricas) para los 10 modelos originales: mismas cifras."""
    t = T06[(T06.tipo == "mensual") & (T06.percentil == 75)]
    dif = 0.0
    for _, r in t.iterrows():
        if r.modelo not in ORIG:
            continue
        a = T1[(T1.cultivo == r.cultivar) & (T1.pool == r.conjunto) & (T1.modelo == r.modelo)]
        for x, y in (("MAE", "MAE"), ("RMSE", "RMSE"), ("MASE", "MASE"), ("iid_global_lo", "IC_iid_lo"), ("iid_global_hi", "IC_iid_hi"),
                     ("bloq_global_lo", "IC_bloques_lo"), ("bloq_global_hi", "IC_bloques_hi"), ("MAE_shock", "MAE_shock_MoM")):
            dif = max(dif, abs(float(r[x]) - float(a[y].iloc[0])))
    return dif


def main():
    txt = TEX.read_text(encoding="utf-8")
    tab_shock_scaled(txt)
    tab_diag(txt)
    tab_supp(txt)
    d = pd.DataFrame(FILAS)
    d.to_csv(SAL, index=False, encoding="utf-8")
    print(f"{len(d)} celdas; coinciden {int((d.coincide == True).sum())}; no coinciden {int((d.coincide == False).sum())}")  # noqa: E712
    print(d[d.coincide == False].to_string())  # noqa: E712
    print("control T1 vs T06 (10 modelos originales, P75 mensual), max |dif| =", control_t06())


if __name__ == "__main__":
    main()
