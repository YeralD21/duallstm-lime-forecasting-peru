"""Etapa 10 (Fase D2): figuras MDPI del backtesting, solo a partir de CSV ya guardados (Fases C y D1).

No recalcula metricas ni mascaras: lee 07_barrido_umbral/, 06_metricas/, 05_predicciones/, 03_ventanas/ y los
history.csv de 04_modelos/. Cada figura: PNG 300 dpi + PDF vectorial + CSV con los datos exactos que dibuja + TXT con
pie sugerido y lectura en dos lineas. Etiquetas en ingles, sin titulo dentro de la imagen, un archivo por cultivo,
color y marcador fijos por modelo (01_configuracion/estilo_figuras.json). XGB-43 (exploratorio) solo entra en fig18b, marcada como EXPLORATORY; en ninguna otra figura.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.entorno import BR, preparar_entorno  # noqa: E402

preparar_entorno()

import json  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from lib.figuras import COLORES, ESTILO, MARCADORES, aplicar_estilo  # noqa: E402
from lib.figuras import guardar as _guardar  # noqa: E402

aplicar_estilo()
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import patheffects  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402
from matplotlib.ticker import FixedLocator, FuncFormatter, MaxNLocator, NullFormatter  # noqa: E402

MODELOS = ("Naive", "Seasonal Naive", "Chronos", "SARIMA", "SARIMA-sel", "Ridge", "ElasticNet", "XGB-37", "GC3", "GE")
CON_SEMILLA = ("XGB-37", "GC3", "GE")
ENTRENADOS_D8 = ("Ridge", "ElasticNet", "XGB-37", "GC3", "GE")
VENTANAS = (2021, 2022, 2023, 2024, 2025)
REPORTE = (50, 60, 75, 90)
CULT = {"sutil": "Sutil", "dulce": "Dulce"}
CULT_EN = {"sutil": "sour lime (limón sutil)", "dulce": "sweet lime (limón dulce)"}
G = BR / "08_graficos"
W1, W2 = ESTILO["ancho_columna_pulg"], ESTILO["ancho_doble_pulg"]
SOMBRA = ESTILO["sombreado_shock"]
REG: list[dict] = []
SOLO: tuple[str, ...] = ()  # prefijos de figuras a escribir (--solo); vacio = todas. El indice se registra completo igual.
MILES = FuncFormatter(lambda v, _: f"{v:,.0f}")  # un solo formato de miles (coma) en ejes y celdas


def leer(rel: str) -> pd.DataFrame:
    return pd.read_csv(BR / rel, dtype={"fecha": str, "ventana": str})


SW = {t: leer(f"07_barrido_umbral/{t}/barrido_por_modelo.csv") for t in ("mensual", "interanual")}
NV = {t: leer(f"07_barrido_umbral/{t}/n_shock_por_ventana.csv") for t in ("mensual", "interanual")}
EST = leer("07_barrido_umbral/estabilizacion.csv")
T05 = leer("06_metricas/por_ventana/T05_metricas_por_ventana.csv")
T06 = leer("06_metricas/agregadas/T06_agregadas_IC.csv")
T07 = leer("06_metricas/por_semilla/T07_metricas_por_semilla.csv")
T12 = leer("06_metricas/agregadas/T12_delta_s_quitando_un_shock.csv")
T13 = leer("06_metricas/agregadas/T13_mae_por_cuartil_cambio.csv")
T15 = leer("06_metricas/por_semilla/T15_diagnostico_ajuste.csv")
T03 = leer("06_metricas/descripcion_series/T03_descripcion_particiones.csv")
T11 = pd.read_csv(BR / "06_metricas/ablacion_nlp/T11_ablacion_GE_menos_GC3.csv", dtype={"conjunto": str})
T09 = leer("06_metricas/significancia/T09_diebold_mariano_hln.csv")
T16 = leer("06_metricas/agregadas/T16_exploratorio_xgb43.csv")
ERR = leer("05_predicciones/errores_test_promediados_semillas.csv")
PRED = leer("05_predicciones/predicciones_consolidadas.csv")
MASK = leer("03_ventanas/umbrales_y_mascaras.csv")
PCTS = sorted(SW["mensual"].percentil.unique())


def reg(base: str, carpeta: str, c: str, pregunta: str, fuentes: list[str]) -> None:
    REG.append({"figura": base, "carpeta": f"08_graficos/{carpeta}", "cultivar": c, "pregunta": pregunta, "fuentes": "; ".join(fuentes)})


def guardar(fig, carpeta: Path, base: str, datos: pd.DataFrame, pie: str, lectura: str) -> dict:
    if SOLO and not base.startswith(SOLO):
        plt.close(fig)
        return {}
    return _guardar(fig, carpeta, base, datos, pie, lectura)


def color_texto(rgba) -> str:
    """Texto negro o blanco segun la luminancia relativa (WCAG) del color de la celda."""
    lin = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in rgba[:3]]
    return "black" if 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2] > 0.18 else "white"


def ticks_log(eje, vmin: float, vmax: float) -> None:
    """Marcas 1-2-5 legibles en un eje logaritmico (10, 20, 50, 100...), miles con coma."""
    v = [x for x in (m * 10.0 ** k for k in range(-3, 7) for m in (1, 2, 5)) if vmin <= x <= vmax]
    if len(v) < 3:  # rango estrecho (menos de una decada): marcas mas densas
        v = [x for x in (m * 10.0 ** k for k in range(-3, 7) for m in (1, 2, 3, 4, 5, 6, 8)) if vmin <= x <= vmax]
    eje.set_major_locator(FixedLocator(v))
    eje.set_major_formatter(FuncFormatter(lambda x, _: f"{x:,.0f}" if x >= 1 else f"{x:g}"))
    eje.set_minor_formatter(NullFormatter())


def marcar_reporte(ax) -> None:
    for p in REPORTE:
        ax.axvline(p, color="0.6", lw=0.6, ls=(0, (3, 2)), zorder=0)
    ax.set_xticks(sorted(set(range(0, 100, 10)) | set(REPORTE) | {95}))


def leyenda_modelos(fig, modelos=MODELOS, ncol=5, y=-0.02, extra=()) -> None:
    h = [Line2D([], [], color=COLORES[m], marker=MARCADORES[m], ms=4, lw=1.1, label=m) for m in modelos] + list(extra)
    fig.legend(handles=h, loc="upper center", bbox_to_anchor=(0.5, y), ncol=ncol, frameon=False)


def leyenda_cajas(fig, modelos, alpha: float, ncol: int, y: float) -> None:
    h = [Patch(facecolor=COLORES[m], alpha=alpha, edgecolor="black", lw=0.6, label=m) for m in modelos]
    fig.legend(handles=h, loc="upper center", bbox_to_anchor=(0.5, y), ncol=ncol, frameon=False)


def etiqueta_panel(ax, txt: str) -> None:
    ax.text(0.0, 1.02, txt, transform=ax.transAxes, ha="left", va="bottom", fontsize=ESTILO["tamano_base"] - 1, fontweight="bold")


def meses_shock(c: str, anio: int, tipo="mensual", p=75) -> list[str]:
    r = MASK[(MASK.cultivar == c) & (MASK.anio_test == anio) & (MASK.tipo == tipo) & (MASK.percentil == p)].iloc[0]
    return [] if pd.isna(r.meses_shock) or r.meses_shock == "" else str(r.meses_shock).split(";")


# ============================================================================ sensibilidad al umbral

def lineas_vs_percentil(c: str, col: str, ylabel: str, base: str, pie: str, lectura_fn, logy=False, marcas_log=False, miles=False) -> None:
    d = SW["mensual"][SW["mensual"].cultivar == c]
    fig, ax = plt.subplots(figsize=(W2, 3.0))
    for m in MODELOS:
        s = d[d.modelo == m].sort_values("percentil")
        ax.plot(s.percentil, s[col], color=COLORES[m], marker=MARCADORES[m], ms=3, lw=1.0)
    marcar_reporte(ax)
    if col == "Delta_s":
        ax.axhline(0, color="black", lw=0.6)
    if col == "razon_shock_normal":
        ax.axhline(1, color="black", lw=0.6)
    if logy:
        ax.set_yscale("log")
    if marcas_log:  # sin set_ylim: el rango sale de los datos, no se recorta ningun punto
        v = d[col][d[col] > 0]
        ticks_log(ax.yaxis, v.min() * 0.9, v.max() * 1.1)
    if miles:  # solo fig05 Sutil (toneladas en miles); fig04 y fig06 no se tocan
        ax.yaxis.set_major_formatter(MILES)
    ax.set_xlabel("Shock threshold percentile (monthly |Δy/y|, history to origin)")
    ax.set_ylabel(ylabel)
    leyenda_modelos(fig)
    datos = d[["percentil", "modelo", "n_shock", col]].sort_values(["modelo", "percentil"])
    guardar(fig, G / "sensibilidad_umbral", base, datos, pie, lectura_fn(d))


def fig04(c):
    def lec(d):
        p = d[d.percentil == 75].set_index("modelo")["Delta_s"]
        return (f"At P75, Δs ranges from {p.min():.1f}% ({p.idxmin()}) to {p.max():.1f}% ({p.idxmax()}); at P0 it is 0 for every model by construction.\n"
                "A low Δs alone is not evidence of resilience (amendment E-BR1): read it together with MAE_shock in tonnes (Fig. 5).")
    base = f"fig04_delta_s_vs_percentile_{c}"
    lineas_vs_percentil(c, "Delta_s", "Δs (%) = (MAE_shock − MAE) / MAE", base,
                        f"Relative shock penalty Δs versus shock-threshold percentile (P0–P95), {CULT_EN[c]}, pooled test windows 2021–2025. "
                        "Dashed lines mark the reporting points P50, P60, P75 (primary) and P90.", lec)
    reg(base, "sensibilidad_umbral", c, "How does the relative shock penalty Δs of each model change with the shock threshold?",
        ["07_barrido_umbral/mensual/barrido_por_modelo.csv"])


def fig05(c):
    def lec(d):
        p = d[d.percentil == 75].set_index("modelo")["MAE_shock"]
        e = EST[(EST.cultivar == c) & (EST.tipo == "mensual")].iloc[0]
        return (f"At P75 the lowest MAE_shock is {p.idxmin()} ({p.min():,.1f} t) and the highest {p.idxmax()} ({p.max():,.1f} t).\n"
                f"The first place (lowest MAE_shock) does not change from P{int(e.primer_lugar_estable_desde)} onwards ({e.modelo_estable}); ties are in Table T08 and Fig. 7.")
    base = f"fig05_mae_shock_vs_percentile_{c}"
    log = c == "dulce"
    lineas_vs_percentil(c, "MAE_shock", "MAE in shock months (t, log scale)" if log else "MAE in shock months (t)", base,
                        f"Mean absolute error in shock months (tonnes) versus shock-threshold percentile, {CULT_EN[c]}, 2021–2025 pooled. "
                        "Errors of seeded models are averaged over 10 seeds per month. Dashed lines: P50, P60, P75, P90."
                        + (" Logarithmic y-axis." if log else ""), lec,
                        logy=log, marcas_log=log, miles=not log)
    reg(base, "sensibilidad_umbral", c, "Which model has the lowest absolute error in shock months, and does it depend on the threshold?",
        ["07_barrido_umbral/mensual/barrido_por_modelo.csv", "07_barrido_umbral/estabilizacion.csv"])


def fig06(c):
    def lec(d):
        p = d[d.percentil == 75].set_index("modelo")["razon_shock_normal"]
        return (f"At P75 the shock/normal ratio goes from {p.min():.2f} ({p.idxmin()}) to {p.max():.2f} ({p.idxmax()}); a ratio below 1 means smaller errors in shock months.\n"
                "The ratio is undefined at P0 (no normal months) and, like Δs, must be read with MAE_shock in tonnes.")
    base = f"fig06_ratio_shock_normal_vs_percentile_{c}"
    lineas_vs_percentil(c, "razon_shock_normal", "MAE ratio, shock / normal months\n(log scale)", base,
                        f"Ratio of shock-month to normal-month MAE versus threshold percentile, {CULT_EN[c]}, 2021–2025. Undefined at P0. "
                        "Horizontal line: ratio = 1. Logarithmic y-axis, so ratios r and 1/r are equally far from 1.", lec, logy=True, marcas_log=True)
    reg(base, "sensibilidad_umbral", c, "Do models make larger errors in shock months than in normal months, and how does that change with the threshold?",
        ["07_barrido_umbral/mensual/barrido_por_modelo.csv"])


def fig07(c):
    fig, axs = plt.subplots(1, 2, figsize=(W2, 3.6), sharey=True)
    datos = []
    for ax, tipo, lab in zip(axs, ("mensual", "interanual"), ("(a) Month-on-month", "(b) Year-on-year")):
        d = SW[tipo][SW[tipo].cultivar == c]
        pos = d.pivot(index="modelo", columns="percentil", values="posicion").reindex(MODELOS)
        pri = d.pivot(index="modelo", columns="percentil", values="primero").reindex(MODELOS)
        im = ax.imshow(pos.to_numpy(float), cmap="cividis_r", vmin=1, vmax=len(MODELOS), aspect="auto")
        for i in range(pos.shape[0]):
            for j in range(pos.shape[1]):
                v = pos.iloc[i, j]
                if pd.notna(v):
                    ax.text(j, i, f"{int(v)}{'*' if pri.iloc[i, j] else ''}", ha="center", va="center", fontsize=5.5,
                            color="black" if v <= 5 else "white")
        ax.set_xticks(range(len(PCTS)), [str(p) for p in PCTS], rotation=90)
        ax.set_yticks(range(len(MODELOS)), MODELOS)
        ax.set_xlabel("Threshold percentile")
        ax.text(0.0, 1.02, lab, transform=ax.transAxes, fontsize=ESTILO["tamano_base"] - 1, fontweight="bold")
        datos.append(d[["percentil", "modelo", "posicion", "primero", "n_shock"]].assign(tipo=tipo))
    fig.colorbar(im, ax=axs, shrink=0.8, label="Rank by MAE in shock months (1 = lowest)")
    dd = pd.concat(datos)
    cuenta = dd[dd.tipo == "mensual"].groupby("modelo").primero.sum()
    lec = (f"Month-on-month: {cuenta.idxmax()} is first or tied with the first in {int(cuenta.max())} of {len(PCTS)} percentiles; "
           f"models never in the first group: {', '.join(m for m in MODELOS if cuenta.get(m, 0) == 0)}.\n"
           "Asterisk = first or tied with the first (paired bootstrap 95% CI of the MAE difference with the best contains 0).")
    base = f"fig07_rank_heatmap_model_percentile_{c}"
    guardar(fig, G / "sensibilidad_umbral", base, dd,
            f"Rank of each model by MAE_shock at every threshold percentile (P0–P95), {CULT_EN[c]}, 2021–2025: (a) month-on-month and "
            "(b) year-on-year change. Numbers are ranks; * marks the first place and statistical ties with it.", lec)
    reg(base, "sensibilidad_umbral", c, "Is the model ranking in shock months stable across thresholds, and which models tie with the best?",
        ["07_barrido_umbral/mensual/barrido_por_modelo.csv", "07_barrido_umbral/interanual/barrido_por_modelo.csv"])


def fig08(c):
    d = SW["mensual"][SW["mensual"].cultivar == c]
    fig, ax = plt.subplots(figsize=(W2, 3.2))
    for m in MODELOS:
        s = d[d.modelo == m].sort_values("percentil")
        ax.plot(s.percentil, s.posicion, color=COLORES[m], marker=MARCADORES[m], ms=3.5, lw=1.1)
        ax.scatter(s.percentil[s.primero], s.posicion[s.primero], s=28, facecolors="none", edgecolors="black", lw=0.6, zorder=3)
    marcar_reporte(ax)
    ax.invert_yaxis()
    ax.set_yticks(range(1, len(MODELOS) + 1))
    ax.set_xlabel("Shock threshold percentile (monthly)")
    ax.set_ylabel("Rank by MAE in shock months\n(1 = lowest)")
    leyenda_modelos(fig, ncol=6, extra=[Line2D([], [], marker="o", ls="", ms=6, mfc="none", mec="black", mew=0.6,
                                               label="First or tied with first")])
    lideres = d[d.posicion == 1].sort_values("percentil")
    lec = (f"Models ranked first at some percentile: {', '.join(dict.fromkeys(lideres.modelo))} "
           f"(rank-1 model at P50/P60/P75/P90: {', '.join(lideres.set_index('percentil').modelo.reindex(REPORTE).fillna('—'))}).\n"
           "Open circles mark the first place and models statistically tied with it; rank changes between adjacent percentiles are a result, not a choice of threshold.")
    base = f"fig08_rank_bump_chart_{c}"
    guardar(fig, G / "sensibilidad_umbral", base, d[["percentil", "modelo", "posicion", "primero"]].sort_values(["modelo", "percentil"]),
            f"Rank trajectories by MAE_shock across monthly threshold percentiles, {CULT_EN[c]}, 2021–2025. "
            "Open circles: first place or tied with it (paired bootstrap). Dashed lines: P50, P60, P75, P90.", lec)
    reg(base, "sensibilidad_umbral", c, "How do model ranks move as the shock threshold becomes stricter?", ["07_barrido_umbral/mensual/barrido_por_modelo.csv"])


def fig09(c):
    fig, ax = plt.subplots(figsize=(W1, 2.6))
    filas = []
    for tipo, ls, lab in (("mensual", "-", "Month-on-month"), ("interanual", "--", "Year-on-year")):
        d = SW[tipo][(SW[tipo].cultivar == c)].drop_duplicates("percentil").sort_values("percentil")
        ax.plot(d.percentil, d.n_shock, ls=ls, color="black", marker="o", ms=2.5, lw=1, label=lab)
        filas.append(d[["percentil", "n_shock"]].assign(tipo=tipo))
    marcar_reporte(ax)
    ax.tick_params(axis="x", labelrotation=90)  # 70/75/80 y 90/95 se superponian en ancho de columna
    ax.set_xlabel("Threshold percentile")
    ax.set_ylabel("Shock months, 2021–2025 (of 60)")
    ax.legend(frameon=False, loc="upper right")
    dd = pd.concat(filas)
    m75 = dd[(dd.percentil == 75)].set_index("tipo").n_shock
    m95 = dd[(dd.percentil == 95)].set_index("tipo").n_shock
    lec = (f"At P75 there are {int(m75['mensual'])} monthly and {int(m75['interanual'])} year-on-year shock months out of 60; "
           f"at P95 only {int(m95['mensual'])} and {int(m95['interanual'])}.\n"
           "Results at high percentiles rest on very few months and have wide uncertainty.")
    base = f"fig09_n_shock_vs_percentile_{c}"
    guardar(fig, G / "sensibilidad_umbral", base, dd,
            f"Number of shock months in the pooled 2021–2025 test set versus threshold percentile, {CULT_EN[c]}; "
            "solid: month-on-month change, dashed: year-on-year change.", lec)
    reg(base, "sensibilidad_umbral", c, "How many shock months support each threshold?", ["07_barrido_umbral/*/barrido_por_modelo.csv"])


def fig10(c):
    fig, axs = plt.subplots(1, 2, figsize=(W2, 2.4), sharey=True)
    filas = []
    for ax, tipo, lab in zip(axs, ("mensual", "interanual"), ("(a) Month-on-month", "(b) Year-on-year")):
        d = NV[tipo][NV[tipo].cultivar == c]
        piv = d.pivot(index="anio_test", columns="percentil", values="n_shock").reindex(VENTANAS)
        im = ax.imshow(piv.to_numpy(float), cmap="Blues", vmin=0, vmax=12, aspect="auto")
        for i in range(piv.shape[0]):
            for j in range(piv.shape[1]):
                v = int(piv.iloc[i, j])
                ax.text(j, i, f"{v}{'' if v >= 2 else '†'}", ha="center", va="center", fontsize=5.5, color=color_texto(im.cmap(im.norm(v))))
        ax.set_xticks(range(len(PCTS)), [str(p) for p in PCTS], rotation=90)
        ax.set_yticks(range(len(VENTANAS)), [str(v) for v in VENTANAS])
        ax.set_xlabel("Threshold percentile")
        ax.text(0.0, 1.03, lab, transform=ax.transAxes, fontsize=ESTILO["tamano_base"] - 1, fontweight="bold")
        filas.append(d.assign(tipo=tipo))
    axs[0].set_ylabel("Test year")
    fig.colorbar(im, ax=axs, shrink=0.85, label="Shock months (of 12)")
    dd = pd.concat(filas)
    no_inf = dd[(dd.tipo == "mensual") & (dd.percentil == 75) & (~dd.informativa)].anio_test.tolist()
    lec = (f"At the primary threshold (monthly P75) the non-informative windows (fewer than 2 shocks) are: {', '.join(map(str, no_inf)) or 'none'}.\n"
           "† marks fewer than 2 shocks; such windows are flagged in per-window tables but their shock months still count in pooled results (DA5).")
    base = f"fig10_n_shock_heatmap_window_percentile_{c}"
    guardar(fig, G / "sensibilidad_umbral", base, dd,
            f"Shock months per test window and threshold percentile, {CULT_EN[c]}: (a) month-on-month, (b) year-on-year. "
            "Thresholds are computed with the history up to each origin. † = fewer than 2 shocks (non-informative window).", lec)
    reg(base, "sensibilidad_umbral", c, "In which windows and thresholds are there enough shocks to evaluate?", ["07_barrido_umbral/*/n_shock_por_ventana.csv"])


def fig11(c):
    d = T06[(T06.conjunto == "principal_2021_2025") & (T06.cultivar == c) & (T06.tipo == "mensual") & T06.modelo.isin(MODELOS)]
    fig, axs = plt.subplots(1, 4, figsize=(W2, 3.0), sharey=True)
    for ax, p in zip(axs, REPORTE):
        s = d[d.percentil == p].set_index("modelo").reindex(MODELOS)
        y = np.arange(len(MODELOS))
        for i, m in enumerate(MODELOS):
            ax.errorbar(s.MAE_shock[m], i, xerr=[[s.MAE_shock[m] - s.iid_shock_lo[m]], [s.iid_shock_hi[m] - s.MAE_shock[m]]],
                        fmt=MARCADORES[m], color=COLORES[m], ms=4, capsize=2, lw=1)
        ax.set_yticks(y, MODELOS)
        ax.set_xlabel("MAE in shock months\n(t, log scale)" if c == "dulce" else "MAE in shock months\n(t)")  # dos lineas: no se tocan entre paneles
        etiqueta_panel(ax, f"P{p} (n={int(s.n_shock.iloc[0])})")
        if c == "dulce":
            ax.set_xscale("log")
            ticks_log(ax.xaxis, s.iid_shock_lo.min() * 0.9, s.iid_shock_hi.max() * 1.1)  # marcas 5, 10, 20, 50, 100 (sin 10^n)
        else:
            ax.xaxis.set_major_formatter(MILES)
    axs[0].invert_yaxis()  # ejes y compartidos: se invierte una sola vez
    datos = d[d.percentil.isin(REPORTE)][["percentil", "modelo", "n_shock", "MAE_shock", "iid_shock_lo", "iid_shock_hi", "bloq_shock_lo", "bloq_shock_hi"]]
    p75 = d[d.percentil == 75].set_index("modelo")
    lec = (f"At P75 the lowest point estimate is {p75.MAE_shock.idxmin()} ({p75.MAE_shock.min():,.1f} t, 95% CI {p75.iid_shock_lo[p75.MAE_shock.idxmin()]:,.1f}–"
           f"{p75.iid_shock_hi[p75.MAE_shock.idxmin()]:,.1f}).\nThese are marginal intervals; ties are decided with paired CIs of differences (Table T08), not by overlap of these bars.")
    base = f"fig11_bootstrap_ci_mae_shock_report_points_{c}"
    guardar(fig, G / "sensibilidad_umbral", base, datos,
            f"MAE in shock months with paired bootstrap 95% confidence intervals (i.i.d. over months, stratified by window, B = 10,000) at the "
            f"reporting thresholds P50, P60, P75 and P90 (monthly), {CULT_EN[c]}, 2021–2025." + (" Logarithmic x-axis." if c == "dulce" else ""), lec)
    reg(base, "sensibilidad_umbral", c, "How uncertain are the shock-month errors at the reporting thresholds?", ["06_metricas/agregadas/T06_agregadas_IC.csv"])


def fig12(c):
    fig, axs = plt.subplots(2, 5, figsize=(W2, 3.6), sharex=True)
    filas = []
    for ax, m in zip(axs.ravel(), MODELOS):
        for tipo, ls in (("mensual", "-"), ("interanual", "--")):
            s = SW[tipo][(SW[tipo].cultivar == c) & (SW[tipo].modelo == m)].sort_values("percentil")
            ax.plot(s.percentil, s.MAE_shock, color=COLORES[m], ls=ls, lw=1)
            filas.append(s[["percentil", "modelo", "n_shock", "MAE_shock"]].assign(tipo=tipo))
        etiqueta_panel(ax, m)
        ax.tick_params(labelsize=6)
        ax.yaxis.set_major_formatter(MILES)
        for p in REPORTE:
            ax.axvline(p, color="0.75", lw=0.4, ls=":")
    for ax in axs[1]:
        ax.set_xlabel("Percentile", fontsize=7)
    for ax in axs[:, 0]:
        ax.set_ylabel("MAE in shock\nmonths (t)", fontsize=7)
    fig.subplots_adjust(wspace=0.55, hspace=0.35)  # cada panel tiene su eje y: espacio para sus etiquetas
    fig.legend(handles=[Line2D([], [], color="black", ls="-", label="Month-on-month"), Line2D([], [], color="black", ls="--", label="Year-on-year")],
               loc="upper center", bbox_to_anchor=(0.5, 0.0), ncol=2, frameon=False)
    dd = pd.concat(filas)
    a = dd[(dd.tipo == "mensual") & (dd.percentil == 75)].set_index("modelo").MAE_shock
    b = dd[(dd.tipo == "interanual") & (dd.percentil == 75)].set_index("modelo").MAE_shock
    lec = (f"At P75 the lowest MAE_shock is {a.idxmin()} with month-on-month shocks and {b.idxmin()} with year-on-year shocks.\n"
           "The two shock definitions select different months, so model comparisons can differ; the year-on-year results are reported separately.")
    base = f"fig12_yoy_vs_mom_threshold_{c}"
    guardar(fig, G / "sensibilidad_umbral", base, dd,
            f"MAE in shock months versus threshold percentile for each model, month-on-month (solid) versus year-on-year (dashed) shock definition, "
            f"{CULT_EN[c]}, 2021–2025. Each panel has its own y-axis.", lec)
    reg(base, "sensibilidad_umbral", c, "Do conclusions change if shocks are defined by year-on-year instead of month-on-month change?",
        ["07_barrido_umbral/mensual/barrido_por_modelo.csv", "07_barrido_umbral/interanual/barrido_por_modelo.csv"])


# ============================================================================ comparacion de modelos

def fig13(c):
    d = T06[(T06.conjunto == "principal_2021_2025") & (T06.cultivar == c) & (T06.tipo == "mensual") & (T06.percentil == 75)].set_index("modelo").reindex(MODELOS)
    fig, ax = plt.subplots(figsize=(W2, 2.8))
    x = np.arange(len(MODELOS))
    w = 0.38
    ax.bar(x - w / 2, d.MAE_normal, w, color=[COLORES[m] for m in MODELOS], alpha=0.45, edgecolor="black", lw=0.4, label="Normal months")
    ax.bar(x + w / 2, d.MAE_shock, w, color=[COLORES[m] for m in MODELOS], edgecolor="white", lw=0, hatch="////", label="Shock months, monthly P75 (MoM)")
    ax.bar(x + w / 2, d.MAE_shock, w, fill=False, edgecolor="black", lw=0.4)
    # bigotes encima de las barras con borde blanco: visibles tambien sobre la barra negra de Seasonal Naive
    for xx, y_, lo, hi in ((x - w / 2, d.MAE_normal, d.iid_normal_lo, d.iid_normal_hi), (x + w / 2, d.MAE_shock, d.iid_shock_lo, d.iid_shock_hi)):
        eb = ax.errorbar(xx, y_, yerr=[y_ - lo, hi - y_], fmt="none", ecolor="black", elinewidth=0.7, capsize=2, capthick=0.7, zorder=5)
        for art in list(eb.lines[1]) + list(eb.lines[2]):
            art.set_path_effects([patheffects.withStroke(linewidth=2.0, foreground="white")])
    ax.set_xticks(x, MODELOS, rotation=30, ha="right")
    ax.set_ylabel("MAE (t)")
    ax.yaxis.set_major_formatter(MILES)
    ax.legend(frameon=False, loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2, handles=[plt.Rectangle((0, 0), 1, 1, fc="0.8", ec="black", lw=0.4, label="Normal months"),
                                                       plt.Rectangle((0, 0), 1, 1, fc="0.45", ec="white", lw=0, hatch="////", label="Shock months, monthly P75 (MoM)")])
    datos = d.reset_index()[["modelo", "n_normal", "MAE_normal", "iid_normal_lo", "iid_normal_hi", "n_shock", "MAE_shock", "iid_shock_lo", "iid_shock_hi"]]
    lec = (f"Lowest MAE in normal months: {d.MAE_normal.idxmin()} ({d.MAE_normal.min():,.1f} t); lowest in shock months: {d.MAE_shock.idxmin()} ({d.MAE_shock.min():,.1f} t).\n"
           f"Shock months: {int(d.n_shock.iloc[0])} of 60; error bars are paired bootstrap 95% CIs (resampling within normal or shock months).")
    base = f"fig13_mae_normal_vs_shock_bars_{c}"
    guardar(fig, G / "comparacion_modelos", base, datos,
            f"MAE in normal months (light) and in shock months (hatched; monthly P75 threshold) for each model, {CULT_EN[c]}, pooled 2021–2025, "
            "with paired bootstrap 95% CIs.", lec)
    reg(base, "comparacion_modelos", c, "Which models are best in normal months and which in shock months?", ["06_metricas/agregadas/T06_agregadas_IC.csv"])


def fig14(c):
    d = T05[(T05.cultivar == c) & (T05.tipo == "mensual") & (T05.percentil == 75) & T05.anio_test.isin(VENTANAS) & T05.modelo.isin(MODELOS)]
    piv = d.pivot(index="modelo", columns="anio_test", values="MAE_shock").reindex(MODELOS)[list(VENTANAS)]
    ns = d.drop_duplicates("anio_test").set_index("anio_test").n_shock.reindex(VENTANAS)
    fig, ax = plt.subplots(figsize=(W1 * 1.35, 3.2))
    arr = piv.to_numpy(float)
    im = ax.imshow(arr, cmap="cividis_r", aspect="auto", norm=plt.matplotlib.colors.LogNorm(vmin=np.nanmin(arr), vmax=np.nanmax(arr)))
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if np.isfinite(arr[i, j]):
                ax.text(j, i, f"{arr[i, j]:,.0f}", ha="center", va="center", fontsize=5.5, color=color_texto(im.cmap(im.norm(arr[i, j]))))
            else:
                ax.text(j, i, "n/a", ha="center", va="center", fontsize=5.5, color="0.4")
    ax.set_xticks(range(len(VENTANAS)), [f"{v}\n(n={int(ns[v])})" for v in VENTANAS])
    ax.set_yticks(range(len(MODELOS)), MODELOS)
    ax.set_xlabel("Test year (n = shock months, monthly P75 (MoM))")
    cb = fig.colorbar(im, ax=ax, shrink=0.85, label="MAE in shock months (t, log scale)")
    ticks_log(cb.ax.yaxis, np.nanmin(arr), np.nanmax(arr))
    vacias = [str(v) for v in VENTANAS if ns[v] == 0]
    lec = (f"Windows without P75 shock months (cells n/a): {', '.join(vacias) or 'none'}; the best model per informative window varies: "
           f"{', '.join(f'{v}: {piv[v].idxmin()}' for v in VENTANAS if ns[v] > 0)}.\n"
           "Per-window values rest on 2–4 months and are descriptive; the ranking uses the pooled months (Table T08).")
    base = f"fig14_mae_shock_heatmap_model_window_{c}"
    guardar(fig, G / "comparacion_modelos", base, d[["anio_test", "modelo", "n_shock", "MAE_shock", "informativa"]],
            f"MAE in shock months (monthly P75) by model and test window, {CULT_EN[c]}. n/a = no shock month in that window.", lec)
    reg(base, "comparacion_modelos", c, "Is a model's shock-month performance consistent across test years?", ["06_metricas/por_ventana/T05_metricas_por_ventana.csv"])


def fig15(c):
    d = T07[(T07.cultivar == c) & T07.modelo.isin(CON_SEMILLA)]
    fig, axs = plt.subplots(1, 2, figsize=(W2, 2.8))
    for ax, col, lab, ylab in zip(axs, ("MAE", "MAE_shock"), ("(a) MAE, all months", "(b) MAE in shock months, monthly P75 (MoM)"),
                                  ("MAE (t)", "MAE in shock months (t)")):
        pos, cajas, cols = [], [], []
        etiquetas = list(VENTANAS) + ["Pooled"]
        for k, v in enumerate(etiquetas):
            clave = "agregado_2021_2025" if v == "Pooled" else str(v)
            if d[(d.ventana == clave)][col].dropna().empty:  # ventana sin meses de shock: hueco rotulado
                ax.text(k * 4 + 1, 0.5, "n/a", transform=ax.get_xaxis_transform(), ha="center", va="center", fontsize=6, color="0.4")
            for j, m in enumerate(CON_SEMILLA):
                vals = d[(d.ventana == clave) & (d.modelo == m)][col].dropna().to_numpy()
                if len(vals):
                    pos.append(k * 4 + j)
                    cajas.append(vals)
                    cols.append(COLORES[m])
        bp = ax.boxplot(cajas, positions=pos, widths=0.7, patch_artist=True, showfliers=True,
                        medianprops={"color": "black", "lw": 0.8}, flierprops={"ms": 2})
        for patch, col_ in zip(bp["boxes"], cols):
            patch.set_facecolor(col_)
            patch.set_alpha(0.75)
        ax.set_xticks([k * 4 + 1 for k in range(len(etiquetas))], [str(e) for e in etiquetas])
        ax.set_xlim(-1, (len(etiquetas) - 1) * 4 + 3)
        ax.set_ylabel(ylab)
        ax.yaxis.set_major_formatter(MILES)
        ax.text(0.0, 1.02, lab, transform=ax.transAxes, fontsize=ESTILO["tamano_base"] - 1, fontweight="bold")
    fig.subplots_adjust(wspace=0.32)
    leyenda_cajas(fig, CON_SEMILLA, alpha=0.75, ncol=3, y=-0.02)
    agg = d[d.ventana == "agregado_2021_2025"].groupby("modelo").MAE.std()
    sin_shock = sorted(d[(d.ventana != "agregado_2021_2025") & (d.n_shock == 0)].ventana.unique())
    nota = f" Panel (b) has no boxes for {' and '.join(sin_shock)} (no P75 shock month)." if sin_shock else ""
    lec = (f"Between-seed SD of pooled MAE: {', '.join(f'{m} {agg[m]:,.1f} t' for m in CON_SEMILLA)}.\n"
           f"Seed dispersion is reported separately and does not enter the bootstrap intervals.{nota}")
    base = f"fig15_seed_boxplots_{c}"
    guardar(fig, G / "comparacion_modelos", base, d[["modelo", "ventana", "semilla", "MAE", "MAE_shock", "n_shock"]],
            f"Distribution over the 10 training seeds of (a) MAE and (b) shock-month MAE (monthly P75) per test window and pooled 2021–2025, "
            f"for the seeded models, {CULT_EN[c]}.", lec)
    reg(base, "comparacion_modelos", c, "How much do results of the stochastic models depend on the random seed?", ["06_metricas/por_semilla/T07_metricas_por_semilla.csv"])


def fig16(c):
    d = T13[(T13.cultivar == c) & (T13.agrupacion == "cuartil") & T13.modelo.isin(MODELOS)]
    rangos = d.drop_duplicates("grupo").set_index("grupo").rango_cambio
    fig, ax = plt.subplots(figsize=(W2, 2.8))
    for m in MODELOS:
        s = d[d.modelo == m].sort_values("grupo")
        ax.plot(s.grupo, s.MAE, color=COLORES[m], marker=MARCADORES[m], ms=3.5, lw=1)
    ax.set_xticks([1, 2, 3, 4], [f"Q{g}\n{rangos[g]}" for g in (1, 2, 3, 4)])
    ax.set_xlabel("Quartile of monthly |Δy/y| in the test months (15 months each)")
    ax.set_ylabel("MAE (t)")
    if c == "dulce":
        ax.set_yscale("log")
        ticks_log(ax.yaxis, d.MAE.min() * 0.9, d.MAE.max() * 1.1)
    leyenda_modelos(fig, y=-0.1)  # las etiquetas del eje x ocupan dos lineas
    q1 = d[d.grupo == 1].set_index("modelo").MAE
    q4 = d[d.grupo == 4].set_index("modelo").MAE
    lec = (f"In the calmest quartile (Q1) the lowest MAE is {q1.idxmin()} ({q1.min():,.1f} t); in the most volatile (Q4) it is {q4.idxmin()} ({q4.min():,.1f} t).\n"
           "Quartiles are cut on the pooled 60 test months of each cultivar; tercile results are in Table T13.")
    base = f"fig16_mae_by_change_quartile_{c}"
    guardar(fig, G / "comparacion_modelos", base, d[["grupo", "rango_cambio", "n_meses", "modelo", "MAE"]],
            f"MAE by quartile of the absolute month-on-month relative change |Δy/y| of the test months, {CULT_EN[c]}, pooled 2021–2025.", lec)
    reg(base, "comparacion_modelos", c, "How does each model's error grow as month-to-month changes become larger?", ["06_metricas/agregadas/T13_mae_por_cuartil_cambio.csv"])


def fig17(c):
    d = T12[(T12.cultivar == c) & (T12.ventana == "agregado_2021_2025") & T12.modelo.isin(MODELOS)].set_index("modelo").reindex(MODELOS)
    fig, ax = plt.subplots(figsize=(W1 * 1.35, 3.0))
    y = np.arange(len(MODELOS))
    for i, m in enumerate(MODELOS):
        ax.plot([d.Delta_s_loo_min[m], d.Delta_s_loo_max[m]], [i, i], color=COLORES[m], lw=2.2, solid_capstyle="butt")
        ax.plot(d.Delta_s[m], i, marker=MARCADORES[m], color="black", ms=4)
    ax.axvline(0, color="black", lw=0.6)
    ax.set_yticks(y, MODELOS)
    ax.invert_yaxis()
    ax.set_xlabel("Δs (%), pooled 2021–2025, monthly P75")
    ancho = (d.Delta_s_loo_max - d.Delta_s_loo_min)
    lec = (f"Dropping one shock month at a time, the widest Δs range is {ancho.idxmax()} ({d.Delta_s_loo_min[ancho.idxmax()]:.1f}% to {d.Delta_s_loo_max[ancho.idxmax()]:.1f}%); "
           f"the narrowest is {ancho.idxmin()}.\nModels whose range crosses 0 can change the sign of Δs by removing a single month.")
    base = f"fig17_leave_one_shock_out_delta_s_{c}"
    guardar(fig, G / "comparacion_modelos", base, d.reset_index()[["modelo", "n_shock", "Delta_s", "Delta_s_loo_min", "Delta_s_loo_max", "mes_que_mas_cambia"]],
            f"Δs with all shock months (marker) and its range when one shock month is removed at a time (bar), {CULT_EN[c]}, pooled 2021–2025, monthly P75.", lec)
    reg(base, "comparacion_modelos", c, "Does Δs depend on a single shock month?", ["06_metricas/agregadas/T12_delta_s_quitando_un_shock.csv"])


# ============================================================================ diagnostico de ajuste

def aviso_nivel(c: str) -> str:
    t = T03[T03.cultivar == c].pivot(index="anio_test", columns="particion", values="media")
    altos = [str(a) for a in VENTANAS if t.loc[a, "val"] > t.loc[a, "train"]]
    return altos


def fig01(c, modelo):
    carpeta = {"GC3": "gc3_lstm_sin_nlp", "GE": "ge_lstm_con_nlp"}[modelo]
    fig, axs = plt.subplots(1, 5, figsize=(W2, 2.3), sharey=True)
    filas = []
    for ax, v in zip(axs, VENTANAS):
        for s in range(10):
            h = pd.read_csv(BR / "04_modelos" / carpeta / c / str(v) / f"seed_{s:02d}" / "history.csv")
            ax.plot(h.epoch, h.loss, color=COLORES[modelo], lw=0.6, alpha=0.55)
            ax.plot(h.epoch, h.val_loss, color="black", lw=0.6, alpha=0.55)
            b = int(h.loc[h.val_loss.idxmin(), "epoch"])
            ax.plot(b, h.val_loss.min(), "o", color="black", ms=2)
            filas.append(h[["epoch", "loss", "val_loss"]].assign(ventana=v, semilla=s, mejor_epoca=b))
        ax.set_yscale("log")
        ax.set_xlabel("Epoch")
        etiqueta_panel(ax, str(v))
    axs[0].set_ylabel("MSE loss (standardized target)")
    fig.legend(handles=[Line2D([], [], color=COLORES[modelo], lw=1, label="Training"), Line2D([], [], color="black", lw=1, label="Validation (year Y−1)"),
                        Line2D([], [], color="black", marker="o", ls="", ms=3, label="Best epoch (restored)")],
               loc="upper center", bbox_to_anchor=(0.5, -0.06), ncol=3, frameon=False)
    dd = pd.concat(filas)
    med = dd.drop_duplicates(["ventana", "semilla"]).groupby("ventana").mejor_epoca.median()
    lec = (f"Median best epoch per window: {', '.join(f'{v} {med[v]:.1f}' for v in VENTANAS)}; no run reached the 300-epoch cap (early stopping, patience 15).\n"
           "Loss is on the standardized target of each window's scaler, so absolute levels are not comparable across windows.")
    base = f"fig01_loss_curves_{modelo.lower()}_{c}"
    guardar(fig, G / "diagnostico_ajuste", base, dd,
            f"Training and validation loss curves of {modelo} for each test window and the 10 seeds (one line per seed), {CULT_EN[c]}. "
            "Dots: epoch with minimum validation loss, whose weights are restored for forecasting.", lec)
    reg(base, "diagnostico_ajuste", c, f"How does {modelo} train in each window, and when does early stopping act?", ["04_modelos/*_lstm_*/<cultivo>/<anio>/seed_XX/history.csv"])


def fig02(c):
    d = T15[(T15.cultivar == c) & T15.modelo.isin(ENTRENADOS_D8)]
    fig, ax = plt.subplots(figsize=(W2, 3.0))
    off = dict(zip(ENTRENADOS_D8, np.linspace(-0.32, 0.32, len(ENTRENADOS_D8))))
    for m in ENTRENADOS_D8:
        s = d[d.modelo == m]
        x = s.anio_test.map({v: i for i, v in enumerate(VENTANAS)}) + off[m]
        ax.scatter(x, s.razon_val_train, color=COLORES[m], marker=MARCADORES[m], s=10, alpha=0.8, lw=0.3, edgecolors="black")
    nv = d.drop_duplicates(["anio_test", "modelo"]).groupby("anio_test").Naive_razon.first().reindex(VENTANAS)
    for i, v in enumerate(VENTANAS):
        ax.plot([i - 0.42, i + 0.42], [nv[v], nv[v]], color=COLORES["Naive"], lw=1.6)
    ax.axhline(2.0, color="0.3", ls="--", lw=0.8)
    ax.set_yscale("log")
    ticks_log(ax.yaxis, min(d.razon_val_train.min(), nv.min()) * 0.9, max(d.razon_val_train.max(), nv.max()) * 1.1)
    ax.set_xticks(range(len(VENTANAS)), [str(v) for v in VENTANAS])
    ax.set_xlabel("Test year (train ≤ Y−2, validation = Y−1)")
    ax.set_ylabel("MAE_val / MAE_train (log scale)")
    altos = aviso_nivel(c)
    if c == "sutil":
        ax.text(1.0, 1.02, f"Note: validation-year mean level above training mean in {', '.join(altos)}; ratios are inflated by the level shift.",
                transform=ax.transAxes, ha="right", va="bottom", fontsize=6, color="0.25")
    h = [Line2D([], [], color=COLORES[m], marker=MARCADORES[m], ls="", ms=4, label=m) for m in ENTRENADOS_D8]
    h += [Line2D([], [], color=COLORES["Naive"], lw=1.6, label="Naive ratio (same months)"), Line2D([], [], color="0.3", ls="--", lw=0.8, label="Overfitting flag (2.0)")]
    fig.legend(handles=h, loc="upper center", bbox_to_anchor=(0.5, 0.0), ncol=4, frameon=False)
    cuenta = d.groupby("modelo").sobreajuste_razon_gt_2.agg(["sum", "size"])
    txt_cuenta = ", ".join(f"{m} {int(cuenta.loc[m, 'sum'])}/{int(cuenta.loc[m, 'size'])}" for m in ENTRENADOS_D8)
    lec = (f"Runs with ratio > 2: {txt_cuenta}; "
           f"the Naive ratio in the same months ranges {nv.min():.2f}–{nv.max():.2f}.\n"
           "As specified in the protocol, the 2.0 flag marks almost all XGB runs; it must be read against the Naive ratio, not on its own.")
    base = f"fig02_train_val_gap_{c}"
    nv_fam = d.drop_duplicates(["anio_test", "modelo"]).pivot(index="anio_test", columns="modelo", values="Naive_razon")
    dif_nv = float((nv_fam[["GC3", "GE"]].max(axis=1) - nv_fam[["Ridge", "ElasticNet", "XGB-37"]].min(axis=1)).abs().max())
    guardar(fig, G / "diagnostico_ajuste", base, d[["modelo", "anio_test", "semilla", "MAE_train", "MAE_val", "razon_val_train", "Naive_razon", "sobreajuste_razon_gt_2"]],
            f"Validation/training MAE ratio for each trained model, window and seed (points), {CULT_EN[c]}; grey bars: same ratio for the Naive forecast "
            f"on the training and validation months of the tabular models (on the LSTM months, which start in 2017-01, it differs by at most {dif_nv:.3f}); "
            "dashed line: overfitting flag at 2.0, specified in the protocol." + (" In Sutil the validation year has a higher mean level than the "
                                                                                     f"training period in {', '.join(altos)}, which inflates the ratio." if c == "sutil" else ""), lec)
    reg(base, "diagnostico_ajuste", c, "Do trained models overfit (validation error much larger than training error) compared with the Naive reference?",
        ["06_metricas/por_semilla/T15_diagnostico_ajuste.csv", "06_metricas/descripcion_series/T03_descripcion_particiones.csv"])


def fig03(c):
    d = T15[(T15.cultivar == c) & T15.modelo.isin(("GC3", "GE"))]
    fig, ax = plt.subplots(figsize=(W1 * 1.35, 2.6))
    for j, m in enumerate(("GC3", "GE")):
        cajas = [d[(d.modelo == m) & (d.anio_test == v)].mejor_epoca.to_numpy() for v in VENTANAS]
        pos = [i * 3 + j for i in range(len(VENTANAS))]
        bp = ax.boxplot(cajas, positions=pos, widths=0.8, patch_artist=True, medianprops={"color": "black", "lw": 0.8}, flierprops={"ms": 2})
        for p_ in bp["boxes"]:
            p_.set_facecolor(COLORES[m])
            p_.set_alpha(0.7)
    ax.set_xticks([i * 3 + 0.5 for i in range(len(VENTANAS))], [str(v) for v in VENTANAS])
    ax.set_xlabel("Test year")
    ax.set_ylabel("Best epoch (min. validation loss)")
    leyenda_cajas(fig, ("GC3", "GE"), alpha=0.7, ncol=2, y=0.0)
    med = d.groupby(["modelo", "anio_test"]).mejor_epoca.median()
    txt_med = {m: ", ".join(f"{v} {med[m][v]:.1f}" for v in VENTANAS) for m in ("GC3", "GE")}
    lec = (f"Median best epoch, GC3: {txt_med['GC3']}; GE: {txt_med['GE']}.\n"
           "Very early best epochs (e.g. below 10) mean that validation loss stopped improving almost immediately in that window.")
    base = f"fig03_early_stopping_epoch_{c}"
    guardar(fig, G / "diagnostico_ajuste", base, d[["modelo", "anio_test", "semilla", "mejor_epoca", "epocas_corridas"]],
            f"Distribution over 10 seeds of the best (restored) epoch of GC3 and GE per test window, {CULT_EN[c]}; early stopping on validation year Y−1, patience 15, maximum 300 epochs.", lec)
    reg(base, "diagnostico_ajuste", c, "When does early stopping select the weights of the LSTM models in each window?", ["06_metricas/por_semilla/T15_diagnostico_ajuste.csv"])


# ============================================================================ predicciones y errores

HALO = [patheffects.withStroke(linewidth=3.2, foreground="white")]


def fig20(c, v):
    p = PRED[(PRED.cultivar == c) & (PRED.anio_test == v) & (PRED.particion == "test") & PRED.modelo.isin(MODELOS)]
    obs = ERR[(ERR.cultivar == c) & (ERR.anio_test == v)].drop_duplicates("fecha").set_index("fecha").y_true.sort_index()
    sh = meses_shock(c, v)
    meses = list(obs.index)
    x = np.arange(len(meses))
    fig, axs = plt.subplots(2, 5, figsize=(W2, 3.4), sharex=True, sharey=True)
    for ax, m in zip(axs.ravel(), MODELOS):
        for i, f in enumerate(meses):
            if f in sh:
                ax.axvspan(i - 0.5, i + 0.5, color=SOMBRA, alpha=0.5, lw=0)
        ax.plot(x, obs.to_numpy(), color="black", lw=1.8, zorder=2, path_effects=HALO)
        s = p[p.modelo == m]
        if m in CON_SEMILLA:
            for sem, g in s.groupby("semilla"):
                g = g.set_index("fecha").reindex(meses)
                ax.plot(x, g.y_pred, color=COLORES[m], lw=0.5, alpha=0.5, zorder=3)
        else:
            g = s.set_index("fecha").reindex(meses)
            # Seasonal Naive comparte el negro con Observed: discontinuo con cuadrados huecos (relleno blanco, borde negro)
            sn = m == "Seasonal Naive"
            hueco = dict(ms=2.6, mfc="white", mec=COLORES[m], mew=0.6, ls=(0, (3, 1.5))) if sn else dict(ms=2, ls="-")
            ax.plot(x, g.y_pred, color=COLORES[m], marker=MARCADORES[m], lw=0.9, zorder=3, **hueco)
        etiqueta_panel(ax, m)
        ax.tick_params(labelsize=6)
        ax.yaxis.set_major_formatter(MILES)
    for ax in axs[1]:
        ax.set_xticks(x[::2], [f[5:] for f in meses][::2])
        ax.set_xlabel(f"Month ({v})", fontsize=7)
    for ax in axs[:, 0]:
        ax.set_ylabel("Production (t)", fontsize=7)
    fig.legend(handles=[Line2D([], [], color="black", lw=1.8, path_effects=HALO, label="Observed"),
                        Line2D([], [], color="0.4", lw=0.9, label="Forecast (one line per seed for XGB-37, GC3, GE)"),
                        plt.Rectangle((0, 0), 1, 1, fc=SOMBRA, alpha=0.5, label="Shock month (monthly P75)" + ("" if sh else " (none this year)"))],
               loc="upper center", bbox_to_anchor=(0.5, 0.0), ncol=3, frameon=False)
    datos = p[["modelo", "semilla", "fecha", "y_pred"]].merge(obs.rename("y_observed").reset_index(), on="fecha")
    datos["shock_P75_mensual"] = datos.fecha.isin(sh)
    lec = (f"Test year {v}: {len(sh)} shock month(s) at monthly P75 ({', '.join(f[5:] for f in sh) or 'none'}), computed with the history up to December {v - 1}.\n"
           "One-step-ahead forecasts use the observed value of the previous month; seed lines show the spread of the stochastic models.")
    base = f"fig20_real_vs_pred_{v}_{c}"
    guardar(fig, G / "predicciones", base, datos,
            f"Observed national production and one-step-ahead forecasts of each model, test year {v}, {CULT_EN[c]}. "
            "Grey: shock months (monthly P75, history to origin). Seeded models: one line per seed (10 seeds). "
            "Observed: thick black line; Seasonal Naive: dashed black line with open squares.", lec)
    reg(base, "predicciones", c, f"How do forecasts track the observed series in {v}, and what happens in shock months?",
        ["05_predicciones/predicciones_consolidadas.csv", "05_predicciones/errores_test_promediados_semillas.csv", "03_ventanas/umbrales_y_mascaras.csv"])


def fig21(c):
    e = ERR[(ERR.cultivar == c) & ERR.anio_test.isin(VENTANAS) & ERR.modelo.isin(MODELOS)]
    piv = e.pivot_table(index="modelo", columns=["anio_test", "fecha"], values="ae", aggfunc="first").reindex(MODELOS)
    cols = list(piv.columns)
    fig, ax = plt.subplots(figsize=(W2, 3.0))
    arr = piv.to_numpy(float)
    vmin = float(np.nanpercentile(arr, 2))  # solo escala de color: errores menores se pintan con el color minimo (extend="min")
    im = ax.imshow(arr, cmap="cividis_r", aspect="auto", norm=plt.matplotlib.colors.LogNorm(vmin=vmin, vmax=np.nanmax(arr)))
    sh = [(a, f) for a, f in cols if f in meses_shock(c, a)]
    for j, k in enumerate(cols):
        if k in sh:
            ax.plot(j, -0.9, marker="v", color="black", ms=3, clip_on=False)
    for j, (a, f) in enumerate(cols):
        if f.endswith("-01") and j:
            ax.axvline(j - 0.5, color="white", lw=0.8)
    ax.set_xticks([j for j, (a, f) in enumerate(cols) if f.endswith("-01")], [str(a) for a, f in cols if f.endswith("-01")])
    ax.set_yticks(range(len(MODELOS)), MODELOS)
    ax.set_xlabel("Test month (2021–2025); ▼ = shock month (monthly P75)")
    cb = fig.colorbar(im, ax=ax, shrink=0.85, extend="min", label="Absolute error (t, log scale; seed mean)")
    ticks_log(cb.ax.yaxis, vmin, np.nanmax(arr))
    i, j = np.unravel_index(np.nanargmax(arr), arr.shape)
    lec = (f"The largest seed-averaged absolute error is {MODELOS[i]} in {cols[j][1]} ({arr[i, j]:,.1f} t); "
           f"{len(sh)} of 60 months are shocks at monthly P75.\nVertical white lines separate test years; colour is on a log scale.")
    base = f"fig21_abs_error_monthly_{c}"
    datos = e[["modelo", "anio_test", "fecha", "y_true", "ae", "n_semillas"]].assign(shock_P75_mensual=[(a, f) in set(sh) for a, f in zip(e.anio_test, e.fecha)])
    guardar(fig, G / "errores", base, datos,
            f"Month-by-month absolute forecast error of each model (mean over seeds for seeded models), {CULT_EN[c]}, test months 2021–2025.", lec)
    reg(base, "errores", c, "In which months and for which models are the errors largest?", ["05_predicciones/errores_test_promediados_semillas.csv", "03_ventanas/umbrales_y_mascaras.csv"])


def fig18(c):
    """Ablacion NLP: GE - GC3 emparejado por semilla (T11). Solo dibuja valores guardados."""
    d = T11[T11.cultivar == c].copy()
    orden = [str(v) for v in VENTANAS] + ["principal_2021_2025", "sensibilidad_2023_2025"]
    etiquetas = [str(v) for v in VENTANAS] + ["Pooled 2021–25", "Pooled 2023–25"]
    alcances = (("global", "(a) All months"), ("shock_P75", "(b) Shock months (monthly P75)"), ("normal_P75", "(c) Normal months"))
    semillas = [f"seed_{s:02d}" for s in range(10)]
    fig, axs = plt.subplots(1, 3, figsize=(W2, 2.9), sharey=False)
    for ax, (alc, lab) in zip(axs, alcances):
        etq = list(etiquetas)
        for i, conj in enumerate(orden):
            r = d[(d.conjunto == conj) & (d.alcance == alc)]
            if alc == "shock_P75":  # panel (b): n de meses de shock en cada etiqueta
                etq[i] = f"{etiquetas[i]} (n={0 if r.empty else int(r.n_meses.iloc[0])})"
            if r.empty or int(r.n_meses.iloc[0]) == 0:
                ax.annotate("n/a", (i, 0), xytext=(0, 7), textcoords="offset points", ha="center", va="bottom", fontsize=6, color="0.4")
                continue
            r = r.iloc[0]
            vals = r[semillas].to_numpy(float)
            ax.scatter(i + np.linspace(-0.22, 0.22, len(vals)), vals, s=6, color=COLORES["GE"], alpha=0.55, lw=0)
            ax.errorbar(i, r.dif_media_GE_menos_GC3, yerr=[[r.dif_media_GE_menos_GC3 - r.IC95_lo], [r.IC95_hi - r.dif_media_GE_menos_GC3]],
                        fmt="D", color="black", ms=3.5, capsize=2, lw=1)
        ax.axhline(0, color="black", lw=0.6)
        ax.axvline(len(VENTANAS) - 0.5, color="0.7", lw=0.6, ls=":")
        ax.set_xticks(range(len(orden)), etq, fontsize=6, rotation=45, ha="right")
        sin0 = d[(d.conjunto == orden[0]) & (d.alcance == alc)]
        if sin0.empty or int(sin0.n_meses.iloc[0]) == 0:  # "n/a" en la primera posicion: margen para que no pise el eje y (Sutil 2021)
            ax.set_xlim(-0.8, len(orden) - 0.5)
        ax.yaxis.set_major_formatter(MILES)
        ax.text(0.0, 1.02, lab, transform=ax.transAxes, fontsize=ESTILO["tamano_base"] - 1, fontweight="bold")
    axs[0].set_ylabel("MAE(GE) − MAE(GC3) (t)\nnegative = NLP features help")
    fig.subplots_adjust(wspace=0.35)
    fig.legend(handles=[Line2D([], [], color=COLORES["GE"], marker="o", ls="", ms=3, alpha=0.6, label="One seed: MAE(GE, seed k) − MAE(GC3, seed k)"),
                        Line2D([], [], color="black", marker="D", ls="-", ms=3.5, label="Mean over 10 seeds, paired bootstrap 95% CI")],
               loc="upper center", bbox_to_anchor=(0.5, -0.27), ncol=2, frameon=False)  # bajo las etiquetas con n del panel (b)
    datos = d[["conjunto", "alcance", "n_meses", "dif_media_GE_menos_GC3", "IC95_lo", "IC95_hi", "semillas_GE_mejor"] + semillas]
    p = d[(d.conjunto == "principal_2021_2025")].set_index("alcance")
    g, s_ = p.loc["global"], p.loc["shock_P75"]
    lec = (f"Pooled 2021–2025: GE − GC3 = {g.dif_media_GE_menos_GC3:,.1f} t (95% CI {g.IC95_lo:,.1f} to {g.IC95_hi:,.1f}) in all months and "
           f"{s_.dif_media_GE_menos_GC3:,.1f} t ({s_.IC95_lo:,.1f} to {s_.IC95_hi:,.1f}) in shock months; GE is better in {int(g.semillas_GE_mejor)} of 10 seed pairs overall.\n"
           "Positive values mean that adding the six lagged NLP features (GE) increases the error relative to the same architecture without them (GC3).")
    base = f"fig18_nlp_ablation_paired_{c}"
    guardar(fig, G / "comparacion_modelos", base, datos,
            f"NLP ablation: difference in MAE between GE (Dual-LSTM with NLP features) and GC3 (same architecture without NLP), paired by seed, "
            f"{CULT_EN[c]}, per test window and pooled; (a) all months, (b) shock months (monthly P75), (c) normal months. "
            "Dots: individual seed pairs; diamonds: mean with paired bootstrap 95% CI (months resampled within windows, B = 10,000). n/a = no shock month.", lec)
    reg(base, "comparacion_modelos", c, "Do the NLP features improve the Dual-LSTM (GE vs GC3), overall and in shock months?",
        ["06_metricas/ablacion_nlp/T11_ablacion_GE_menos_GC3.csv"])


def fig18b(c):
    """EXPLORATORIO (post-hoc): XGB-43 - XGB-37 emparejado por semilla. Puntos = restas simples de T07 por ventana y en el
    agregado 2021-2025; rombo con IC solo en el agregado, con los valores guardados en T16. Sin medias ni IC nuevos por ventana."""
    t7 = T07[(T07.cultivar == c) & T07.modelo.isin(["XGB-37", "XGB-43"]) & T07.ventana.isin([str(v) for v in VENTANAS])]
    t16 = T16[T16.cultivar == c].set_index("alcance")
    agr = T07[(T07.cultivar == c) & T07.modelo.isin(["XGB-37", "XGB-43"]) & (T07.ventana == "agregado_2021_2025")]
    alcances = (("global", "MAE", "(a) All months"), ("shock_P75", "MAE_shock", "(b) Shock months (monthly P75)"),
                ("normal_P75", "MAE_normal", "(c) Normal months"))
    semillas = [f"seed_{s:02d}" for s in range(10)]
    etiquetas = [str(v) for v in VENTANAS] + ["Pooled 2021–25"]
    filas = []
    fig, axs = plt.subplots(1, 3, figsize=(W2, 2.9), sharey=False)
    for ax, (alc, col, lab) in zip(axs, alcances):
        etq = list(etiquetas)
        for i, v in enumerate(VENTANAS):
            w = t7[t7.ventana == str(v)].pivot(index="semilla", columns="modelo", values=col).sort_index()
            nn = t7[t7.ventana == str(v)][["n_shock", "n_normal"]].drop_duplicates()
            if len(nn) != 1:
                raise AssertionError(f"n de meses distinto entre semillas o modelos: {c} {v}")
            n = {"global": int(nn.n_shock.iloc[0] + nn.n_normal.iloc[0]), "shock_P75": int(nn.n_shock.iloc[0]), "normal_P75": int(nn.n_normal.iloc[0])}[alc]
            if alc == "shock_P75":
                etq[i] = f"{v} (n={n})"
            if list(w.index) != list(range(10)):
                raise AssertionError(f"T07 sin las 10 semillas emparejadas: {c} {v}")
            fila = {"conjunto": str(v), "alcance": alc, "n_meses": n, "dif_43_menos_37": np.nan, "IC95_lo": np.nan, "IC95_hi": np.nan}
            if n == 0:
                ax.annotate("n/a", (i, 0), xytext=(0, 7), textcoords="offset points", ha="center", va="bottom", fontsize=6, color="0.4")
                filas.append(fila | {s: np.nan for s in semillas})
                continue
            vals = (w["XGB-43"] - w["XGB-37"]).to_numpy(float)
            filas.append(fila | dict(zip(semillas, vals)))
            ax.scatter(i + np.linspace(-0.22, 0.22, len(vals)), vals, s=9, marker=MARCADORES["XGB-43"], color=COLORES["XGB-43"], alpha=0.75, lw=0)
        r, i = t16.loc[alc], len(VENTANAS)
        if alc == "shock_P75":
            etq[i] = f"{etiquetas[i]} (n={int(r.n_meses)})"
        w = agr.pivot(index="semilla", columns="modelo", values=col).sort_index()
        if list(w.index) != list(range(10)):
            raise AssertionError(f"T07 sin las 10 semillas emparejadas: {c} agregado_2021_2025")
        vals = (w["XGB-43"] - w["XGB-37"]).to_numpy(float)
        filas.append({"conjunto": "principal_2021_2025", "alcance": alc, "n_meses": int(r.n_meses), "dif_43_menos_37": r.dif_43_menos_37,
                      "IC95_lo": r.IC95_lo, "IC95_hi": r.IC95_hi} | dict(zip(semillas, vals)))
        ax.scatter(i + np.linspace(-0.22, 0.22, len(vals)), vals, s=9, marker=MARCADORES["XGB-43"], color=COLORES["XGB-43"], alpha=0.75, lw=0)
        ax.errorbar(i, r.dif_43_menos_37, yerr=[[r.dif_43_menos_37 - r.IC95_lo], [r.IC95_hi - r.dif_43_menos_37]],
                    fmt="D", color="black", ms=3.5, capsize=2, lw=1)
        ax.axhline(0, color="black", lw=0.6)
        ax.axvline(len(VENTANAS) - 0.5, color="0.7", lw=0.6, ls=":")
        ax.set_xticks(range(len(etq)), etq, fontsize=6, rotation=45, ha="right")
        if filas[-len(VENTANAS) - 1]["n_meses"] == 0:  # "n/a" en la primera posicion: margen para que no pise el eje y
            ax.set_xlim(-0.8, len(etq) - 0.5)
        ax.yaxis.set_major_locator(MaxNLocator(nbins=7, steps=[1, 2, 5, 10]))  # marcas 1-2-5: sin 2.5 redondeado a "2" (Dulce)
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:,.0f}" if float(v).is_integer() else f"{v:,.1f}"))
        ax.text(0.0, 1.02, lab, transform=ax.transAxes, fontsize=ESTILO["tamano_base"] - 1, fontweight="bold")
    axs[0].set_ylabel("MAE(XGB-43) − MAE(XGB-37) (t)\nnegative = NLP features help")
    fig.subplots_adjust(wspace=0.35, top=0.84)
    fig.text(0.01, 0.985, "EXPLORATORY (post-hoc; not part of the ranking specified in the protocol)", ha="left", va="top", fontsize=7, fontweight="bold",
             color="#AA3377", bbox=dict(boxstyle="square,pad=0.25", fc="white", ec="#AA3377", lw=0.8))
    fig.text(0.99, 0.985, "CI shown for pooled 2021–2025 only", ha="right", va="top", fontsize=6.5, color="0.25")
    fig.legend(handles=[Line2D([], [], color=COLORES["XGB-43"], marker=MARCADORES["XGB-43"], ls="", ms=4, alpha=0.75,
                               label="One seed: MAE(XGB-43, seed k) − MAE(XGB-37, seed k)"),
                        Line2D([], [], color="black", marker="D", ls="-", ms=3.5, label="Pooled 2021–2025: mean over 10 seeds, paired bootstrap 95% CI")],
               loc="upper center", bbox_to_anchor=(0.5, -0.27), ncol=2, frameon=False)
    datos = pd.DataFrame(filas)[["conjunto", "alcance", "n_meses", "dif_43_menos_37", "IC95_lo", "IC95_hi"] + semillas].round(6)
    g, s_ = t16.loc["global"], t16.loc["shock_P75"]
    lec = (f"Pooled 2021–2025 (T16): XGB-43 − XGB-37 = {g.dif_43_menos_37:,.1f} t (95% CI {g.IC95_lo:,.1f} to {g.IC95_hi:,.1f}) in all months and "
           f"{s_.dif_43_menos_37:,.1f} t ({s_.IC95_lo:,.1f} to {s_.IC95_hi:,.1f}) in shock months.\n"
           "Positive values mean that adding the six lagged NLP features to XGB-37 increases the error. Exploratory, post-hoc comparison; it is not used for any conclusion of the analysis specified in the protocol.")
    base = f"fig18b_xgb43_vs_xgb37_exploratory_{c}"
    guardar(fig, G / "comparacion_modelos", base, datos,
            f"EXPLORATORY (post-hoc) comparison: difference in MAE between XGB-43 and XGB-37, paired by seed, {CULT_EN[c]}; "
            "(a) all months, (b) shock months (monthly P75, MoM), (c) normal months. XGB-43 uses the 37 predictors of XGB-37 plus six lagged NLP features "
            "(avg_sentiment and n_noticias at lags 1, 3 and 6) with the same hyperparameters. "
            "Dots: individual seed pairs per test window (2021–2025) and pooled 2021–2025; diamond: mean over 10 seeds for the pooled 2021–2025 set with paired bootstrap 95% CI "
            "(months resampled within windows, B = 10,000). No mean or CI is shown per window. n/a = no shock month. "
            "XGB-43 was added post hoc: it is not part of the ranking specified in the protocol and is not included in the Diebold–Mariano tests or the Holm correction.", lec)
    reg(base, "comparacion_modelos", c, "Exploratory (post-hoc): do six lagged NLP features change the error of XGB-37 (XGB-43 vs XGB-37)?",
        ["06_metricas/por_semilla/T07_metricas_por_semilla.csv", "06_metricas/agregadas/T16_exploratorio_xgb43.csv"])


def fig19(c, holm: bool):
    """Matriz DM-HLN (T09): bajo la diagonal todos los meses, sobre la diagonal solo shocks P75. Holm: version exploratoria aparte."""
    col = "p_holm_exploratorio" if holm else "p"
    d = T09[(T09.conjunto == "principal_2021_2025") & (T09.cultivar == c)]
    n = len(MODELOS)
    P = np.full((n, n), np.nan)
    S = np.full((n, n), "", dtype=object)
    for r in d.itertuples():
        i, j = MODELOS.index(r.modelo_A), MODELOS.index(r.modelo_B)
        pv = getattr(r, col)
        if r.alcance == "global":     # fila = B, columna = A; d = A - B -> "+" si la fila tiene mas error
            P[j, i], S[j, i] = pv, "+" if r.d_media < 0 else "−"
        else:                         # fila = A, columna = B
            P[i, j], S[i, j] = pv, "+" if r.d_media > 0 else "−"
    cortes = [0, 0.01, 0.05, 0.10, 1.0001]
    colores = ["#08306B", "#2171B5", "#9ECAE1", "#F7F7F7"]
    cmap = plt.matplotlib.colors.ListedColormap(colores)
    norm = plt.matplotlib.colors.BoundaryNorm(cortes, cmap.N)
    fig, ax = plt.subplots(figsize=(W2 * 0.8, W2 * 0.68))
    ax.imshow(np.where(np.isnan(P), 1.0, P), cmap=cmap, norm=norm)
    for i in range(n):
        ax.add_patch(plt.Rectangle((i - 0.5, i - 0.5), 1, 1, color="0.55"))
        for j in range(n):
            if i != j and np.isfinite(P[i, j]):
                ax.text(j, i, f"{'<0.001' if P[i, j] < 0.001 else f'{P[i, j]:.3f}'}\n{S[i, j]}", ha="center", va="center", fontsize=5,
                        color="white" if P[i, j] < 0.05 else "black")
    ax.plot([-0.5, n - 0.5], [-0.5, n - 0.5], color="black", lw=0.8)
    ax.set_xticks(range(n), MODELOS, rotation=45, ha="right")
    ax.set_yticks(range(n), MODELOS)
    ax.text(0.5, 1.01, "Above the diagonal: shock months only (monthly P75)   |   Below the diagonal: all months",
            transform=ax.transAxes, ha="center", va="bottom", fontsize=6)
    h = [plt.Rectangle((0, 0), 1, 1, fc=colores[k], ec="0.6", lw=0.4, label=l) for k, l in enumerate(("p < 0.01", "0.01 ≤ p < 0.05", "0.05 ≤ p < 0.10", "p ≥ 0.10"))]
    fig.legend(handles=h, loc="upper center", bbox_to_anchor=(0.55, 0.0), ncol=4, frameon=False,
               title=("Holm-adjusted p-value (EXPLORATORY)" if holm else "Unadjusted p-value"), title_fontsize=7)
    n_g = int(d[d.alcance == "global"].n.iloc[0])
    n_s = int(d[d.alcance != "global"].n.iloc[0])
    sig_g = int((d[d.alcance == "global"][col] < 0.05).sum())
    sig_s = int((d[d.alcance != "global"][col] < 0.05).sum())
    datos = d[["alcance", "modelo_A", "modelo_B", "n", "d_media", "HLN", "p", "p_holm_exploratorio"]]
    etiqueta = "Holm-adjusted (exploratory, DESV-07; family = 45 pairs per triangle)" if holm else "unadjusted"
    lec = (f"With {'Holm-adjusted (exploratory)' if holm else 'unadjusted'} p-values, {sig_g} of 45 pairs differ at the 5% level over all months (n = {n_g}) and {sig_s} of 45 in shock months only (n = {n_s}).\n"
           "Signs: '+' means the row model has a larger mean absolute error than the column model; the shock-only test has low power.")
    base = f"fig19{'b' if holm else ''}_dm_pvalue_matrix{'_holm' if holm else ''}_{c}"
    guardar(fig, G / "comparacion_modelos", base, datos,
            f"Diebold–Mariano tests with the Harvey–Leybourne–Newbold correction (h = 1, absolute loss, seed-averaged errors, pooled windows 2021–2025), "
            f"{CULT_EN[c]}: {etiqueta} p-values. Lower triangle: all test months (n = {n_g}); upper triangle: shock months only (monthly P75, n = {n_s}). "
            "'+' = row model has larger error than column model." + (" Holm correction is an exploratory addition, not part of the protocol." if holm else ""), lec)
    reg(base, "comparacion_modelos", c, ("Which pairwise differences survive a multiple-comparison (Holm) correction? (exploratory)" if holm else
                                         "Which pairs of models differ significantly in forecast accuracy, overall and in shock months?"),
        ["06_metricas/significancia/T09_diebold_mariano_hln.csv"])


def main() -> None:
    global SOLO
    if "--solo" in sys.argv:  # p. ej. --solo fig20 fig14 fig16_mae_by_change_quartile_dulce
        SOLO = tuple(sys.argv[sys.argv.index("--solo") + 1:])
    for c in CULT:
        for f in (fig04, fig05, fig06, fig07, fig08, fig09, fig10, fig11, fig12, fig13, fig14, fig15, fig16, fig17, fig02, fig03, fig21):
            f(c)
        fig18(c)
        fig18b(c)
        fig19(c, holm=False)
        fig19(c, holm=True)
        for m in ("GC3", "GE"):
            fig01(c, m)
        for v in VENTANAS:
            fig20(c, v)
    r = pd.DataFrame(REG).sort_values(["carpeta", "figura"])
    r.to_csv(G / "indice_figuras.csv", index=False)
    faltan = [f"{x.carpeta}/{x.figura}.{e}" for x in r.itertuples() for e in ("png", "pdf", "csv", "txt") if not (BR / x.carpeta / f"{x.figura}.{e}").exists()]
    print(json.dumps({"figuras": len(r), "archivos_faltantes": faltan}, indent=1))
    if faltan:
        raise SystemExit("Faltan archivos de figuras.")


if __name__ == "__main__":
    main()
