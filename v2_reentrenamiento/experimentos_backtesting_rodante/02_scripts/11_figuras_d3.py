"""Etapa 11 (Fase D3): figuras independientes y tabla suplementaria, solo a partir de datos ya guardados.

- fig24_series_with_shocks_{c}: serie nacional 2016-2025 con los meses de shock P75 mensual de cada ventana de test
  2021-2025 (03_ventanas/umbrales_y_mascaras.csv, umbral calculado con la historia hasta el origen).
- fig25_architecture_dual_lstm: GC3 y GE dibujados desde el codigo oficial v2 (parametros por capa con Keras).
- fig29_study_area_map: provincias productoras, un panel por cultivar, % sobre el total de cada cultivar.
- fig30_rolling_origin_scheme: ventanas 2018-2025 desde 03_ventanas/ventanas_viabilidad.csv y D-BR1.
- TS1_provinces: las 109 provincias con toneladas, % por cultivar y meses con produccion (2016-01..2025-12).

Geometria: 11_geometria_externa/ (geoBoundaries gbOpen PER ADM1, dominio publico; Natural Earth 1:10m admin 0).
Salida: 08_graficos/figuras_independientes/ (PNG 300 dpi + PDF + CSV + TXT). No toca las figuras de la Fase D2.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.entorno import BR, V2, preparar_entorno  # noqa: E402

preparar_entorno()

import json  # noqa: E402
import re  # noqa: E402
import unicodedata  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from lib.datos import ruta  # noqa: E402
from lib.figuras import COLORES, ESTILO, aplicar_estilo, guardar  # noqa: E402

aplicar_estilo()
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import FancyBboxPatch, Patch  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

CM = 1 / 2.54
W_PAG = 17 * CM
SALIDA = BR / "08_graficos" / "figuras_independientes"
GEO = BR / "11_geometria_externa"
COORDS = V2 / "data" / "interim" / "coordenadas_provincias_completo.csv"
CULT = ("sutil", "dulce")
CULT_EN = {"sutil": "sour lime (limón sutil)", "dulce": "sweet lime (limón dulce)"}
CULT_CORTO = {"sutil": "Sour lime", "dulce": "Sweet lime"}
VENTANAS = (2021, 2022, 2023, 2024, 2025)
SOMBRA = ESTILO["sombreado_shock"]
MILES = FuncFormatter(lambda v, _: f"{v:,.0f}")
FECHA_CONSULTA_MIDAGRI = ""  # no documentada en el repositorio: se deja en blanco a pedido del autor
CITA_MIDAGRI = f"MIDAGRI–SISAGRI (accessed {FECHA_CONSULTA_MIDAGRI or '[____]'})"
KEY = ["departamento", "provincia"]
REG: list[dict] = []
VERIF: dict = {}


def reg(base: str, pregunta: str, fuentes: list[str]) -> None:
    REG.append({"figura": base, "carpeta": "08_graficos/figuras_independientes", "pregunta": pregunta, "fuentes": "; ".join(fuentes)})


def norm(s: str) -> str:
    """Mayusculas sin tildes (la Ñ se conserva) para emparejar nombres de MIDAGRI y geoBoundaries."""
    s = s.upper().replace("Ñ", "\0")
    s = "".join(ch for ch in unicodedata.normalize("NFD", s) if unicodedata.category(ch) != "Mn")
    return s.replace("\0", "Ñ")


# ============================================================================ datos comunes

def serie_nacional(c: str) -> pd.Series:
    d = pd.read_csv(ruta("produccion_nacional", c), encoding="utf-8-sig")
    idx = [f"{int(a):04d}-{int(m):02d}" for a, m in zip(d["año"], d["mes"])]
    return pd.Series(d["produccion_t_nacional"].astype(float).to_numpy(), index=idx, name=c)


def provincial(c: str) -> pd.DataFrame:
    return pd.read_csv(ruta("produccion_provincial", c), encoding="utf-8-sig")


def tabla_provincias() -> pd.DataFrame:
    """Una fila por provincia (109): coordenadas, categoria, toneladas, % por cultivar y meses con produccion."""
    co = pd.read_csv(COORDS, encoding="utf-8-sig")
    t = co.copy()
    for c in CULT:
        p = provincial(c)
        g = p.groupby(KEY).produccion_t.agg(total="sum", meses=lambda s: int((s > 0).sum()))
        t = t.merge(g.add_prefix(f"{c}_").reset_index(), on=KEY, how="left")
        t[[f"{c}_total", f"{c}_meses"]] = t[[f"{c}_total", f"{c}_meses"]].fillna(0)
        VERIF[f"total_{c}_t"] = float(p.produccion_t.sum())
        VERIF[f"meses_{c}"] = int(p.groupby(["año", "mes"]).ngroups)
        # toda provincia con produccion debe tener coordenadas
        sin_coord = set(map(tuple, g[g.total > 0].reset_index()[KEY].values)) - set(map(tuple, co[KEY].values))
        if sin_coord:
            raise SystemExit(f"Provincias con produccion sin coordenadas ({c}): {sin_coord}")
        t[f"{c}_pct"] = 100 * t[f"{c}_total"] / t[f"{c}_total"].sum()
    s, d = t.sutil_total > 0, t.dulce_total > 0
    t["categoria"] = np.select([s & d, s, d], ["Both cultivars", "Sour lime only", "Sweet lime only"], "No harvest recorded")
    t["coordenada_departamento"] = t.fuente == "departamento_fallback"
    return t


# ============================================================================ fig24

def fig24(c: str) -> None:
    y = serie_nacional(c)
    m = pd.read_csv(BR / "03_ventanas/umbrales_y_mascaras.csv")
    m = m[(m.cultivar == c) & (m.tipo == "mensual") & (m.percentil == 75) & m.anio_test.isin(VENTANAS)].set_index("anio_test")
    sh = sorted(f for v in VENTANAS if isinstance(m.loc[v, "meses_shock"], str) for f in m.loc[v, "meses_shock"].split(";"))
    if len(sh) != int(m.n_shock.sum()):
        raise SystemExit("meses_shock y n_shock no coinciden")
    VERIF[f"shocks_{c}"] = len(sh)
    meses = list(y.index)
    x = np.arange(len(meses))
    pos = {f: i for i, f in enumerate(meses)}
    fig, ax = plt.subplots(figsize=(W_PAG, 6.2 * CM))
    i0 = pos["2021-01"]
    ax.axvspan(i0 - 0.5, len(meses) - 0.5, color="#56B4E9", alpha=0.10, lw=0, zorder=0)
    for f in sh:
        ax.axvspan(pos[f] - 0.5, pos[f] + 0.5, color=SOMBRA, alpha=0.75, lw=0, zorder=1)
    ax.plot(x, y.to_numpy(), color="black", lw=1.0, zorder=3)
    ax.plot([pos[f] for f in sh], y[sh].to_numpy(), "o", ms=3.2, mfc="#D55E00", mec="black", mew=0.4, zorder=4)
    for v in VENTANAS:
        ax.axvline(pos[f"{v}-01"] - 0.5, color="0.6", lw=0.5, ls=":", zorder=0)
        ax.text(pos[f"{v}-01"] + 5.5, 1.015, f"{100 * m.loc[v, 'umbral']:.1f}%", transform=ax.get_xaxis_transform(),
                ha="center", va="bottom", fontsize=6.5, color="0.2")
    ax.text(i0 - 1, 1.015, "Shock threshold (monthly P75 of |Δy/y|):", transform=ax.get_xaxis_transform(), ha="right", va="bottom",
            fontsize=6.5, color="0.2")
    ax.set_xticks([pos[f"{a}-01"] for a in range(2016, 2026)], [str(a) for a in range(2016, 2026)])
    ax.set_xlim(-1, len(meses))
    ax.set_ylabel("National production (t)")
    ax.yaxis.set_major_formatter(MILES)
    ax.set_ylim(bottom=0)
    fig.legend(handles=[Line2D([], [], color="black", lw=1.0, label="Observed monthly production"),
                        Line2D([], [], ls="", marker="o", ms=3.5, mfc="#D55E00", mec="black", mew=0.4, label="Shock month (monthly P75)"),
                        Patch(fc="#56B4E9", alpha=0.25, label="Test years 2021–2025")],
               loc="upper center", bbox_to_anchor=(0.5, 0.0), ncol=3, frameon=False)
    ene_mar = sum(f[5:] in ("01", "02", "03") for f in sh)
    VERIF[f"shocks_ene_mar_{c}"] = ene_mar
    sin = [str(v) for v in VENTANAS if m.loc[v, "n_shock"] == 0]
    frase_estacional = (f" {ene_mar} of the {len(sh)} shock months fall in January–March." if c == "dulce" else "")
    pie = (f"Monthly national production of {CULT_EN[c]} in Peru, January 2016–December 2025 ({CITA_MIDAGRI}). "
           "Grey bands and markers: shock months in the test years 2021–2025, i.e. months whose absolute month-on-month relative change "
           "|Δy/y| exceeds the 75th percentile of the changes observed up to the forecast origin (December of the previous year); "
           "the threshold of each test year is shown above the panel."
           + (f" No month exceeded the threshold in {' or '.join(sin)}." if sin else "") + frase_estacional)
    por_anio = ", ".join(f"{v}: {int(m.loc[v, 'n_shock'])}" for v in VENTANAS)
    lec = (f"{len(sh)} shock months in 2021–2025 ({por_anio}); "
           f"thresholds range from {100 * m.umbral.min():.1f}% to {100 * m.umbral.max():.1f}%.\n"
           "Shock months are defined only for the test years; the series before 2021 is shown as context.")
    datos = pd.DataFrame({"fecha": meses, "produccion_t": y.to_numpy()})
    datos["anio_test"] = [int(f[:4]) if int(f[:4]) in VENTANAS else pd.NA for f in meses]
    datos["umbral_P75_mensual"] = [m.loc[int(f[:4]), "umbral"] if int(f[:4]) in VENTANAS else np.nan for f in meses]
    datos["shock_P75_mensual"] = datos.fecha.isin(sh)
    base = f"fig24_series_with_shocks_{c}"
    guardar(fig, SALIDA, base, datos, pie, lec)
    reg(base, f"When do shock months occur in the {CULT_CORTO[c].lower()} series?",
        [f"{ruta('produccion_nacional', c).relative_to(V2.parent)}", "03_ventanas/umbrales_y_mascaras.csv"])


# ============================================================================ fig30

def fig30() -> None:
    v = pd.read_csv(BR / "03_ventanas/ventanas_viabilidad.csv")
    conf = v[~v.exploratorio]
    viables, no_aplica = 2 * int(conf.viable.sum()), 2 * int((~conf.viable).sum())  # el CSV es comun a los dos cultivares
    VERIF["ventanas_viables"], VERIF["ventanas_no_aplica"] = viables, no_aplica
    w = v.drop_duplicates("anio_test").set_index("anio_test")
    ntr = v.pivot(index="anio_test", columns="modelo", values="n_train")
    anios = list(w.index)
    t0 = pd.Period("2016-07", "M")
    mes = lambda s: (pd.Period(s, "M") - t0).n  # noqa: E731
    fig, ax = plt.subplots(figsize=(W_PAG, 7.4 * CM))
    col = {"train": "#BBBBBB", "val": "#56B4E9", "test": "#E69F00"}
    trama = {"train": "", "val": "////", "test": "...."}
    for k, a in enumerate(anios):
        r = w.loc[a]
        yk = len(anios) - 1 - k
        tenue = not r.en_ranking
        alfa = 0.35 if tenue else 1.0
        for parte, ini, fin in (("train", "2016-07", r.fin_train), ("val", r.val_inicio, r.val_fin), ("test", r.test_inicio, r.test_fin)):
            ax.barh(yk, mes(fin) - mes(ini) + 1, left=mes(ini), height=0.62, color=col[parte], alpha=alfa,
                    hatch=trama[parte], edgecolor="white" if parte != "train" else "0.5", lw=0.4)
        ax.plot(mes(r.origen) + 1, yk, marker="D", ms=3.2, color="black", alpha=alfa, zorder=4)
        if tenue:
            txt = "trained models n/a (< 36 months); only Naive, Seasonal Naive, Chronos"
        else:
            txt = f"train: {int(ntr.loc[a, 'GC3'])} mo (LSTM), {int(ntr.loc[a, 'XGB-37'])} mo (tabular)"
        ax.text(mes("2026-01") + 1.5, yk, txt, va="center", ha="left", fontsize=6.3, color="0.45" if tenue else "black")
    ax.set_yticks(range(len(anios)), [f"Y = {a}" for a in reversed(anios)])
    for lab in ax.get_yticklabels():
        if int(lab.get_text()[-4:]) < 2021:
            lab.set_color("0.5")
    ax.set_xticks([mes(f"{a}-01") for a in range(2017, 2026)], [str(a) for a in range(2017, 2026)])
    ax.set_xlim(-1, mes("2026-01") + 1)
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0)
    # llaves: ranking 2021-2025 y sensibilidad 2023-2025
    _llave(ax, 2021, 2025, anios, -0.105, "Primary ranking 2021–2025")
    _llave(ax, 2023, 2025, anios, -0.145, "Sensitivity 2023–2025")
    h = [Patch(fc=col["train"], ec="0.5", lw=0.4, label="Training (to Dec Y−2)"),
         Patch(fc=col["val"], ec="white", hatch=trama["val"], label="Validation (Y−1): tuning, early stopping"),
         Patch(fc=col["test"], ec="white", hatch=trama["test"], label="Test (Y): 12 one-step-ahead forecasts"),
         Line2D([], [], ls="", marker="D", ms=3.5, color="black", label="Forecast origin (Dec Y−1)")]
    fig.legend(handles=h, loc="upper center", bbox_to_anchor=(0.55, 0.0), ncol=2, frameon=False)
    pie = ("Rolling-origin evaluation design. For each test year Y (2018–2025) the forecast origin is December of Y−1; trained models use data "
           "up to December of Y−2 (features from 2016-07; tabular targets from 2016-08; LSTM targets from 2017-01), are tuned and early-stopped "
           "on year Y−1, and produce twelve one-step-ahead forecasts for year Y. Trained models require at least 36 training months, so windows "
           "2018–2020 (faded) include only the untrained models (Naive, Seasonal Naive, Chronos). The primary ranking pools the windows 2021–2025; "
           "a sensitivity analysis specified in the protocol repeats all conclusions on 2023–2025.")
    lec = (f"{viables} viable and {no_aplica} not-applicable model-window-cultivar combinations (10 models × 8 windows × 2 cultivars; "
           "the exploratory XGB-43 is excluded from the count), as specified in the protocol.\n"
           "Training lengths on the right are the LSTM (GC3/GE) and tabular (XGB-37) training months of each window; no forecast results are shown.")
    datos = w.reset_index()[["anio_test", "origen", "fin_train", "val_inicio", "val_fin", "test_inicio", "test_fin", "en_ranking", "en_sensibilidad_2023_2025"]]
    datos = datos.merge(ntr[["GC3", "XGB-37", "SARIMA"]].rename(columns=lambda s: f"n_train_{s}").reset_index(), on="anio_test")
    base = "fig30_rolling_origin_scheme"
    guardar(fig, SALIDA, base, datos, pie, lec)
    reg(base, "How are the rolling-origin training, validation and test windows defined?", ["03_ventanas/ventanas_viabilidad.csv", "D-BR1"])


def _llave(ax, a1: int, a2: int, anios: list, x: float, lab: str) -> None:
    """Corchete vertical a la izquierda del eje (coordenadas: x en fraccion de ejes, y en datos)."""
    y1, y2 = len(anios) - 1 - anios.index(a1) + 0.36, len(anios) - 1 - anios.index(a2) - 0.36
    tr = ax.get_yaxis_transform()
    ax.plot([x + 0.012, x, x, x + 0.012], [y1, y1, y2, y2], color="black", lw=0.7, transform=tr, clip_on=False)
    ax.text(x - 0.006, (y1 + y2) / 2, lab, transform=tr, ha="right", va="center", fontsize=6.0, rotation=90, clip_on=False)


# ============================================================================ fig25

def fig25() -> None:
    from v2_reentrenamiento.src.models.dual_lstm_attention import (ATTENTION_UNITS, DENSE_UNITS, DROPOUT, LOOKBACK, LSTM_UNITS,
                                                                  build_gc3_ge_model, expected_parameter_count)
    from v2_reentrenamiento.src.models.features_gc3_ge import NLP_LAGGED, build_feature_spec

    filas = []
    for mod in ("GC3", "GE"):
        spec = build_feature_spec("sutil", mod)
        modelo = build_gc3_ge_model(mod, len(spec.rama_a), len(spec.rama_b), compile_model=False)
        total = int(modelo.count_params())
        if total != expected_parameter_count(len(spec.rama_a), len(spec.rama_b)):
            raise SystemExit(f"{mod}: count_params y expected_parameter_count no coinciden")
        VERIF[f"parametros_{mod}"] = total
        for capa in modelo.layers:
            filas.append({"modelo": mod, "capa": capa.name, "parametros": int(capa.count_params())})
        filas.append({"modelo": mod, "capa": "TOTAL", "parametros": total})
        VERIF[f"rama_a_{mod}"], VERIF[f"rama_b_{mod}"] = len(spec.rama_a), len(spec.rama_b)
    P = pd.DataFrame(filas)
    p = {(r.modelo, r.capa): r.parametros for r in P.itertuples()}
    rama_a = build_feature_spec("sutil", "GC3").rama_a

    fig, ax = plt.subplots(figsize=(W_PAG, 8.6 * CM))
    ax.set_xlim(0, 101)
    ax.set_ylim(0, 52)
    ax.axis("off")

    def caja(x, y, w, h, txt, fc="white", ec="black", ls="-", fs=5.8, bold=False):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=0.8", fc=fc, ec=ec, lw=0.7, ls=ls))
        ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center", fontsize=fs, fontweight="bold" if bold else "normal", linespacing=1.25)

    def flecha(x1, y1, x2, y2):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="-|>", lw=0.7, color="black", shrinkA=0, shrinkB=0))

    # rama A
    caja(0.3, 33, 24, 13, f"Branch A input\n{LOOKBACK} months × {len(rama_a)} features:\nproduction and its\nlags 1, 3, 6", fc="#F2F2F2")
    caja(27.5, 35.5, 15, 8, f"LSTM ({LSTM_UNITS})\n{p[('GC3', 'lstm_a')]:,} param.")
    caja(46.5, 35.5, 15, 8, f"Bahdanau\nattention ({ATTENTION_UNITS})\n{p[('GC3', 'attention_a')]:,} param.")
    flecha(24.9, 39.5, 27.1, 39.5)
    flecha(42.9, 39.5, 46.1, 39.5)
    # rama B
    caja(0.3, 9, 24, 19, f"Branch B input\n{LOOKBACK} months × 33 features\n(GC3): month sin/cos,\ntime index; NASA POWER (5)\nand INDECI (5) covariates,\neach at lags 1, 3, 6", fc="#F2F2F2", fs=5.5)
    ax.add_patch(FancyBboxPatch((0.3, 0.6), 24, 6.4, boxstyle="round,pad=0.25,rounding_size=0.8", fc="white", ec=COLORES["GE"], lw=1.0, ls=(0, (3, 2))))
    ax.text(12.3, 3.8, f"GE only: + {len(NLP_LAGGED)} NLP features\n(news sentiment and\nnews count; lags 1, 3, 6)", ha="center", va="center",
            fontsize=5.5, color=COLORES["GE"], linespacing=1.2)
    ax.annotate("", xy=(12, 8.6), xytext=(12, 7.3), arrowprops=dict(arrowstyle="-|>", lw=0.7, color=COLORES["GE"], shrinkA=0, shrinkB=0))
    caja(27.5, 13.5, 15, 8, f"LSTM ({LSTM_UNITS})\nGC3 {p[('GC3', 'lstm_b')]:,} param.\nGE {p[('GE', 'lstm_b')]:,} param.")
    caja(46.5, 13.5, 15, 8, f"Bahdanau\nattention ({ATTENTION_UNITS})\n{p[('GC3', 'attention_b')]:,} param.")
    flecha(24.9, 17.5, 27.1, 17.5)
    flecha(42.9, 17.5, 46.1, 17.5)
    # cabeza comun
    caja(65.5, 24.5, 8.5, 6, f"Concat.\n({2 * LSTM_UNITS})")
    flecha(62, 39.5, 68.5, 31)
    flecha(62, 17.5, 68.5, 24.3)
    caja(76.5, 31, 13, 7, f"Dense {DENSE_UNITS[0]}, ReLU\n{p[('GC3', 'dense_16')]:,} param.")
    caja(76.5, 23, 13, 5.5, f"Dropout {DROPOUT:.2f}")
    caja(76.5, 13.5, 13, 7, f"Dense {DENSE_UNITS[1]}, ReLU\n{p[('GC3', 'dense_8')]:,} param.")
    caja(92, 13.5, 8.5, 7, f"Output ŷ(t)\nDense 1\n{p[('GC3', 'output')]:,} param.", fc="#F2F2F2")
    flecha(74.4, 27.5, 76.1, 33.5)
    flecha(83, 30.8, 83, 28.7)
    flecha(83, 22.8, 83, 20.7)
    flecha(89.8, 17, 91.6, 17)
    ax.text(83, 45.5, f"Trainable parameters\nGC3: {p[('GC3', 'TOTAL')]:,}\nGE: {p[('GE', 'TOTAL')]:,}  (+{p[('GE', 'TOTAL')] - p[('GC3', 'TOTAL')]:,}, branch B LSTM)",
            ha="center", va="center", fontsize=6.0, linespacing=1.3,
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="0.6", lw=0.5))
    ax.text(31, 49.5, f"Input window: months t−{LOOKBACK} … t−1 → forecast of month t", ha="center", va="center", fontsize=6.0, style="italic")
    pie = (f"Dual-LSTM with additive (Bahdanau) temporal attention used by GC3 and GE (v2 official implementation). Each branch receives the "
           f"previous {LOOKBACK} months: branch A the production series and its lags 1, 3 and 6; branch B calendar terms, a time index and lagged "
           "climate (NASA POWER) and disaster (INDECI) covariates. GE adds six lagged news features to branch B (dashed box): the monthly mean "
           "sentiment score of agricultural news, computed with the pysentimiento RoBERTuito sentiment model, and the monthly number of news "
           f"items. GC3 and GE are otherwise identical. Trainable parameters: GC3 {p[('GC3', 'TOTAL')]:,}; GE {p[('GE', 'TOTAL')]:,}.")
    lec = (f"Branch A: {VERIF['rama_a_GC3']} features; branch B: {VERIF['rama_b_GC3']} (GC3) and {VERIF['rama_b_GE']} (GE) features; "
           f"the only parameter difference is the branch-B LSTM ({p[('GC3', 'lstm_b')]:,} vs {p[('GE', 'lstm_b')]:,}).\n"
           "Parameter counts are read from the Keras model built by the official build_gc3_ge_model and checked against expected_parameter_count.")
    base = "fig25_architecture_dual_lstm"
    guardar(fig, SALIDA, base, P, pie, lec)
    reg(base, "What is the architecture of GC3 and GE, and how do they differ?",
        ["v2_reentrenamiento/src/models/dual_lstm_attention.py", "v2_reentrenamiento/src/models/features_gc3_ge.py"])


# ============================================================================ fig29 y TS1

ETIQUETA = {"MORROPON": "Morropón", "JAEN": "Jaén", "SAN IGNACIO": "San Ignacio"}
# desplazamiento de rotulos (grados lon, lat) para que no se pisen; solo presentacion
DESPL = {"sutil": {"ZARUMILLA": (-0.9, 1.1), "SULLANA": (-0.9, 0.9), "PIURA": (-0.95, -0.45), "MORROPON": (1.7, 0.9),
                   "LAMBAYEQUE": (-0.85, -0.65)},
         "dulce": {"CHANCHAMAYO": (-3.4, 0.6), "SATIPO": (1.5, -0.9), "UTCUBAMBA": (5.45, -1.25), "JAEN": (-2.9, -1.6),
                   "SAN IGNACIO": (2.5, 1.65)}}
CAT_ESTILO = {"Sour lime only": dict(marker="o", c="#009E73"), "Both cultivars": dict(marker="s", c="#0072B2"),
              "Sweet lime only": dict(marker="^", c="#E69F00"), "No harvest recorded": dict(marker="x", c="#555555")}
LON_LIM, LAT_LIM = (-84.4, -68.4), (-18.6, 0.6)


def geometria():
    import geopandas as gpd

    adm1 = gpd.read_file(GEO / "geoboundaries_PER_ADM1" / "geoBoundaries-PER-ADM1_simplified.geojson")
    VERIF["adm1_unidades"] = len(adm1)
    # MIDAGRI usa un solo departamento LIMA: se unen "Lima" (region) y "Municipalidad Metropolitana de Lima". El Callao queda aparte.
    adm1["departamento"] = adm1.shapeName.map(norm).replace({"MUNICIPALIDAD METROPOLITANA DE LIMA": "LIMA", "EL CALLAO": "CALLAO"})
    deps = adm1.dissolve(by="departamento", as_index=False)[["departamento", "geometry"]]
    ne = gpd.read_file(f"zip://{GEO / 'natural_earth_10m_admin0' / 'ne_10m_admin_0_countries.zip'}")
    vecinos = ne[ne.ADM0_A3.isin(["ECU", "COL", "BRA", "BOL", "CHL"])]
    return deps, vecinos


def comprobar_departamento(t: pd.DataFrame, deps) -> pd.DataFrame:
    """Punto en poligono: el departamento que contiene cada coordenada frente al departamento de MIDAGRI."""
    import geopandas as gpd

    pts = gpd.GeoDataFrame(t[KEY + ["fuente"]].copy(), geometry=gpd.points_from_xy(t.lon, t.lat), crs="EPSG:4326")
    j = gpd.sjoin(pts, deps.rename(columns={"departamento": "dep_geo"}), how="left", predicate="within")
    j = j[~j.index.duplicated()]
    t = t.copy()
    t["departamento_geometria"] = j.dep_geo.reindex(t.index)
    t["dentro_de_su_departamento"] = t.departamento_geometria == t.departamento.map(norm)
    return t


def fig29_y_ts1() -> None:
    deps, vecinos = geometria()
    t = comprobar_departamento(tabla_provincias(), deps)
    cuenta = t.categoria.value_counts().to_dict()
    VERIF["categorias"] = cuenta
    fuera = t[~t.dentro_de_su_departamento]
    VERIF["fuera_de_departamento"] = fuera[KEY + ["fuente", "departamento_geometria"]].astype(str).values.tolist()
    VERIF["fuera_no_fallback"] = int((~fuera.coordenada_departamento).sum())
    VERIF["nombres_con_enie"] = sorted(t[t.provincia.str.contains("Ñ")].provincia.unique().tolist())
    peru = deps.dissolve()

    fig, axs = plt.subplots(1, 2, figsize=(W_PAG, 11.0 * CM))
    for ax, c, lab in zip(axs, CULT, ("(a)", "(b)")):
        vecinos.plot(ax=ax, facecolor="#E9E9E9", edgecolor="#BBBBBB", lw=0.3, zorder=0)
        deps.plot(ax=ax, facecolor="#FAFAFA", edgecolor="#BBBBBB", lw=0.35, zorder=1)
        peru.boundary.plot(ax=ax, color="#555555", lw=0.6, zorder=2)
        tot, s = t[f"{c}_total"], t[f"{c}_total"] > 0
        smax = 330.0
        area = smax * tot / tot.max()  # area del circulo proporcional a las toneladas del cultivar
        ax.scatter(t.lon[s], t.lat[s], s=area[s], facecolors="#56B4E9", edgecolors="#0072B2", alpha=0.35, lw=0.5, zorder=3)
        for cat, st in CAT_ESTILO.items():
            u = t[t.categoria == cat]
            kw = dict(marker=st["marker"], s=7 if st["marker"] != "^" else 9, zorder=5)
            if st["marker"] == "x":
                ax.scatter(u.lon, u.lat, c=st["c"], lw=0.7, **kw)
            else:
                ax.scatter(u.lon, u.lat, c=st["c"], edgecolors="black", lw=0.3, **kw)
        fb = t[t.coordenada_departamento]
        ax.scatter(fb.lon, fb.lat, s=34, facecolors="none", edgecolors="black", lw=0.6, linestyle=(0, (2, 1.5)), zorder=6)
        top = t[s].nlargest(5, f"{c}_total")
        for r in top.itertuples():
            dx, dy = DESPL[c][r.provincia]
            nombre = ETIQUETA.get(r.provincia, r.provincia.title())
            ax.annotate(f"{nombre}\n{getattr(r, c + '_pct'):.1f}%", (r.lon, r.lat), xytext=(r.lon + dx, r.lat + dy), fontsize=6.0,
                        ha="right" if dx < 0 else "left", va="center", zorder=7,
                        arrowprops=dict(arrowstyle="-", lw=0.45, color="0.25", shrinkA=0, shrinkB=1.5))
        # leyenda de tamanos (area proporcional)
        ref = [x for x in ((500_000, 100_000, 20_000) if c == "sutil" else (20_000, 5_000, 1_000))]
        h = [plt.scatter([], [], s=smax * v / tot.max(), facecolors="#56B4E9", edgecolors="#0072B2", alpha=0.35, lw=0.5, label=f"{v:,} t") for v in ref]
        ax.legend(handles=h, loc="lower left", title=f"{CULT_CORTO[c]}, 2016–2025", title_fontsize=6.3, fontsize=6.2, frameon=True,
                  framealpha=1, edgecolor="0.7", borderpad=0.8, labelspacing=1.1, handletextpad=0.9, scatterpoints=1).get_frame().set_linewidth(0.5)
        ax.text(0.03, 0.985, f"{lab} {CULT_CORTO[c]}", transform=ax.transAxes, ha="left", va="top", fontsize=7, fontweight="bold")
        ax.text(0.03, 0.945, f"{int(s.sum())} provinces with harvest\n{tot.sum():,.0f} t in 2016–2025", transform=ax.transAxes,
                ha="left", va="top", fontsize=6.2, linespacing=1.25)
        ax.set_xlim(*LON_LIM)
        ax.set_ylim(*LAT_LIM)
        ax.set_aspect(1.0 / np.cos(np.deg2rad(9.0)))
        ax.set_xticks(np.arange(-82, -68, 4), [f"{abs(v)}°W" for v in range(-82, -68, 4)])
        ax.set_yticks(np.arange(-18, 1, 3), [f"{abs(v)}°S" if v else "0°" for v in range(-18, 1, 3)])
        if c == "dulce":
            ax.tick_params(labelleft=False)
        ax.tick_params(labelsize=6, length=2)
        for sp in ax.spines.values():
            sp.set_visible(True)
            sp.set_linewidth(0.6)
    # flecha norte y barra de escala (200 km a 15.5 S) en el panel (a)
    ax = axs[0]
    ax.annotate("", xy=(0.93, 0.95), xytext=(0.93, 0.89), xycoords="axes fraction",
                arrowprops=dict(arrowstyle="-|>,head_width=0.2,head_length=0.4", color="black", lw=0.8))
    ax.text(0.93, 0.955, "N", transform=ax.transAxes, ha="center", va="bottom", fontsize=7, fontweight="bold")
    lat_b, lon_b = -15.2, -77.0
    dlon = 200 / (111.32 * np.cos(np.deg2rad(abs(lat_b))))
    ax.plot([lon_b, lon_b + dlon], [lat_b - 2.4, lat_b - 2.4], color="black", lw=1.4, solid_capstyle="butt", zorder=8)
    ax.text(lon_b + dlon / 2, lat_b - 2.15, "200 km", ha="center", va="bottom", fontsize=6.2, zorder=8)
    hcat = [Line2D([], [], ls="", marker=st["marker"], ms=4, mfc=st["c"], mec="black" if st["marker"] != "x" else st["c"], mew=0.4,
                   color=st["c"], label=f"{cat} ({cuenta.get(cat, 0)})") for cat, st in CAT_ESTILO.items()]
    hcat.append(Line2D([], [], ls="", marker="o", ms=6.5, mfc="none", mec="black", mew=0.6, label="Department reference coordinate (10)"))
    fig.legend(handles=hcat, loc="upper center", bbox_to_anchor=(0.5, 0.06), ncol=3, frameon=False, fontsize=6.6)
    fig.subplots_adjust(wspace=0.04)
    pie = (f"Lime-producing provinces of Peru and their cumulative production, January 2016–December 2025: (a) sour lime, (b) sweet lime "
           f"({CITA_MIDAGRI}). Circle area is proportional to each province's cumulative production of that cultivar; labels give the five largest "
           "provinces and their share of the national total of that cultivar. Symbols show whether a province recorded sour lime only, both "
           "cultivars, sweet lime only or no harvest in the period (109 provinces). Dashed rings: ten provinces placed at their department's "
           "reference coordinate, including the two sweet-lime-only and the four no-harvest provinces. Boundaries: geoBoundaries gbOpen "
           "(Runfola et al., 2020), Public Domain, 2008 vintage; neighbouring countries: Natural Earth 1:10m.")
    lec = (f"Categories: {', '.join(f'{k} {v}' for k, v in cuenta.items())}; totals {VERIF['total_sutil_t']:,.0f} t (sour) and {VERIF['total_dulce_t']:,.0f} t (sweet).\n"
           f"Points outside their department polygon: {len(fuera)}, of which {VERIF['fuera_no_fallback']} have a province-level coordinate.")
    cols = KEY + ["lat", "lon", "fuente", "categoria", "sutil_total", "sutil_pct", "dulce_total", "dulce_pct", "departamento_geometria", "dentro_de_su_departamento"]
    base = "fig29_study_area_map"
    guardar(fig, SALIDA, base, t[cols], pie, lec)
    reg(base, "Where is lime produced in Peru, and how concentrated is production of each cultivar?",
        ["v2_reentrenamiento/data/interim/coordenadas_provincias_completo.csv", "v2_reentrenamiento/data/interim/limon_{c}_provincia.csv",
         "11_geometria_externa/ (geoBoundaries PER ADM1; Natural Earth 10m admin 0)"])

    # --- TS1
    ts = t.sort_values(["sutil_total", "dulce_total"], ascending=False)
    ts = pd.DataFrame({
        "Department": ts.departamento, "Province": ts.provincia, "Latitude": ts.lat.round(4), "Longitude": ts.lon.round(4),
        "Coordinate": np.where(ts.coordenada_departamento, "department reference", "province"), "Category": ts.categoria,
        "Sour lime 2016-2025 (t)": ts.sutil_total.round(1), "Sour lime share (%)": ts.sutil_pct.round(2),
        "Months with sour lime > 0 (of 120)": ts.sutil_meses.astype(int),
        "Sweet lime 2016-2025 (t)": ts.dulce_total.round(1), "Sweet lime share (%)": ts.dulce_pct.round(2),
        "Months with sweet lime > 0 (of 120)": ts.dulce_meses.astype(int)})
    total = {"Department": "TOTAL", "Province": "", "Latitude": np.nan, "Longitude": np.nan, "Coordinate": "", "Category": "",
             "Sour lime 2016-2025 (t)": round(t.sutil_total.sum(), 1), "Sour lime share (%)": round(t.sutil_pct.sum(), 2),
             "Months with sour lime > 0 (of 120)": np.nan, "Sweet lime 2016-2025 (t)": round(t.dulce_total.sum(), 1),
             "Sweet lime share (%)": round(t.dulce_pct.sum(), 2), "Months with sweet lime > 0 (of 120)": np.nan}
    ts = pd.concat([ts, pd.DataFrame([total])], ignore_index=True)
    VERIF["TS1_filas_provincia"] = len(ts) - 1
    ts.to_csv(SALIDA / "TS1_provinces.csv", index=False, encoding="utf-8-sig")
    ts.to_latex(SALIDA / "TS1_provinces.tex", index=False, longtable=True, na_rep="", float_format=lambda v: f"{v:,.2f}",
                caption=(f"Lime-producing provinces of Peru, January 2016–December 2025 ({CITA_MIDAGRI}). Shares are relative to the national "
                         "total of each cultivar; months with production count the months with production > 0 out of 120."),
                label="tab:S1_provinces")
    tex = SALIDA / "TS1_provinces.tex"  # to_latex no escapa el "%" de las cabeceras "share (%)"
    tex.write_text(re.sub(r"(?<!\\)%", r"\\%", tex.read_text(encoding="utf-8")), encoding="utf-8")
    (SALIDA / "TS1_provinces.txt").write_text(
        f"Caption (suggested): Lime-producing provinces of Peru (109), January 2016–December 2025 ({CITA_MIDAGRI}). Tonnes are cumulative "
        "production 2016–2025; shares are relative to the national total of each cultivar (sour lime "
        f"{VERIF['total_sutil_t']:,.0f} t; sweet lime {VERIF['total_dulce_t']:,.0f} t); months with production count the months with "
        "production > 0 out of 120. 'department reference' marks provinces located at their department's reference coordinate.\n\n"
        "Reading: sorted by sour-lime production; the last row gives the national totals.\n", encoding="utf-8")
    reg("TS1_provinces", "Which provinces produce each cultivar, how much, and how regularly?",
        ["v2_reentrenamiento/data/interim/coordenadas_provincias_completo.csv", "v2_reentrenamiento/data/interim/limon_{c}_provincia.csv"])


def main() -> None:
    for c in CULT:
        fig24(c)
    fig30()
    fig25()
    fig29_y_ts1()
    idx = SALIDA / "indice_figuras_d3.csv"
    nuevo = pd.DataFrame(REG)
    if idx.exists():  # conserva las filas de figuras que no genera este script (p. ej. fig_workflow, de 13_figura_workflow.py)
        previo = pd.read_csv(idx)
        nuevo = pd.concat([nuevo, previo[~previo.figura.isin(nuevo.figura)]], ignore_index=True)
    nuevo.to_csv(idx, index=False)
    print(json.dumps(VERIF, indent=1, ensure_ascii=False, default=str))


if __name__ == "__main__":
    main()
