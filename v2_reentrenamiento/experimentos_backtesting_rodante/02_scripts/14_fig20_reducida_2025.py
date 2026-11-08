"""Revisión G7, Fase 5 (C): fig20 reducida para el texto principal, test 2025.

fig20_real_vs_pred_2025_main_{sutil,dulce}: solo Observed, GC3, Chronos, SARIMA y Seasonal Naive, con el estilo
de fig20 (10_figuras.py): serie observada negra gruesa con halo, meses de shock P75 mensual sombreados, color y
marcador fijos por modelo, Seasonal Naive discontinuo con cuadrados huecos. GC3 (con semillas) se dibuja como
la MEDIA de las 10 semillas por mes (una línea). No calcula métricas: lee los mismos CSV que fig20.
No modifica la fig20 original ni el índice indice_figuras.csv (la figura nueva se registra en el informe de la Fase 5).

Uso: python 02_scripts/14_fig20_reducida_2025.py
"""
import importlib.util
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
_spec = importlib.util.spec_from_file_location("figuras_d2", AQUI / "10_figuras.py")
F = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(F)  # carga datos y estilo de 10_figuras.py; no ejecuta su main()

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402

ANIO = 2025
MODELOS_MAIN = ("GC3", "Chronos", "SARIMA", "Seasonal Naive")


def fig20_main(c: str) -> dict:
    p = F.PRED[(F.PRED.cultivar == c) & (F.PRED.anio_test == ANIO) & (F.PRED.particion == "test") & F.PRED.modelo.isin(MODELOS_MAIN)]
    obs = F.ERR[(F.ERR.cultivar == c) & (F.ERR.anio_test == ANIO)].drop_duplicates("fecha").set_index("fecha").y_true.sort_index()
    sh = F.meses_shock(c, ANIO)
    meses = list(obs.index)
    x = np.arange(len(meses))
    fig, axs = plt.subplots(1, 4, figsize=(F.W2, 2.1), sharex=True, sharey=True)
    filas = []
    for ax, m in zip(axs, MODELOS_MAIN):
        for i, f in enumerate(meses):
            if f in sh:
                ax.axvspan(i - 0.5, i + 0.5, color=F.SOMBRA, alpha=0.5, lw=0)
        ax.plot(x, obs.to_numpy(), color="black", lw=1.8, zorder=2, path_effects=F.HALO)
        s = p[p.modelo == m]
        if m in F.CON_SEMILLA:
            n_sem = s.semilla.nunique()
            if n_sem != 10:
                raise SystemExit(f"{m} {c} {ANIO}: {n_sem} semillas (se esperaban 10)")
            g = s.groupby("fecha").y_pred.mean().reindex(meses)
            estilo = dict(ms=2, ls="-")
        else:
            n_sem = 1
            g = s.set_index("fecha").y_pred.reindex(meses)
            sn = m == "Seasonal Naive"
            estilo = dict(ms=2.6, mfc="white", mec=F.COLORES[m], mew=0.6, ls=(0, (3, 1.5))) if sn else dict(ms=2, ls="-")
        if g.isna().any():
            raise SystemExit(f"Faltan predicciones de {m} {c} {ANIO}")
        ax.plot(x, g.to_numpy(), color=F.COLORES[m], marker=F.MARCADORES[m], lw=0.9, zorder=3, **estilo)
        F.etiqueta_panel(ax, m + (" (mean of 10 seeds)" if m in F.CON_SEMILLA else ""))
        ax.tick_params(labelsize=6)
        ax.yaxis.set_major_formatter(F.MILES)
        ax.set_xticks(x[::2], [f[5:] for f in meses][::2])
        ax.set_xlabel(f"Month ({ANIO})", fontsize=7)
        filas += [{"modelo": m, "fecha": f, "y_pred": float(v), "n_semillas_promediadas": n_sem} for f, v in g.items()]
    axs[0].set_ylabel("Production (t)", fontsize=7)
    fig.legend(handles=[Line2D([], [], color="black", lw=1.8, path_effects=F.HALO, label="Observed"),
                        Line2D([], [], color="0.4", lw=0.9, label="Forecast (GC3: mean of 10 seeds)"),
                        plt.Rectangle((0, 0), 1, 1, fc=F.SOMBRA, alpha=0.5, label="Shock month (monthly P75)" + ("" if sh else " (none this year)"))],
               loc="upper center", bbox_to_anchor=(0.5, -0.06), ncol=3, frameon=False)
    datos = pd.DataFrame(filas).merge(obs.rename("y_observed").reset_index(), on="fecha")
    datos["shock_P75_mensual"] = datos.fecha.isin(sh)
    lec = (f"Test year {ANIO}: {len(sh)} shock month(s) at monthly P75 ({', '.join(f[5:] for f in sh) or 'none'}), computed with the history up to December {ANIO - 1}.\n"
           "Reduced version of fig20 for the main text: four models; the full ten-model figure is in the supplementary material.")
    base = f"fig20_real_vs_pred_{ANIO}_main_{c}"
    return F._guardar(fig, F.G / "predicciones", base, datos,
                      f"Observed national production and one-step-ahead forecasts of GC3, Chronos, SARIMA and Seasonal Naive, test year {ANIO}, "
                      f"{F.CULT_EN[c]}. Grey: shock months (monthly P75, history to origin). GC3: mean of the 10 seed forecasts in each month. "
                      "Observed: thick black line; Seasonal Naive: dashed black line with open squares.", lec)


def main() -> None:
    for c in F.CULT:
        print(fig20_main(c))


if __name__ == "__main__":
    main()
