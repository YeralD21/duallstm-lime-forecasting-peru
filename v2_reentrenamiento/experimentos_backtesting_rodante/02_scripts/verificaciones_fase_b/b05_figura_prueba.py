"""Fase B: verifica la cadena de figuras (PNG 300 dpi + PDF + CSV + TXT) con la mini corrida 2025.

Salida: 10_logs/verificaciones/fase_b/figura_prueba/ (no es una figura de resultados).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lib.entorno import BR, preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import json  # noqa: E402

import pandas as pd  # noqa: E402

from lib.datos import ConstructorDatosVentana  # noqa: E402
from lib.figuras import COLORES, ESTILO, MARCADORES, aplicar_estilo, guardar  # noqa: E402
from lib.shocks import mascara  # noqa: E402
from lib.ventanas import Ventana  # noqa: E402

SAL = BR / "10_logs" / "verificaciones" / "fase_b" / "figura_prueba"


def main() -> None:
    aplicar_estilo()
    import matplotlib.pyplot as plt
    from PIL import Image

    v = Ventana(2025)
    datos = ConstructorDatosVentana()
    pred = pd.read_csv(BR / "10_logs" / "verificaciones" / "fase_b" / "mini_corrida_predicciones.csv")
    res = {}
    for c in ("sutil", "dulce"):
        mk = mascara(datos.serie(c), v, "mensual", 75)
        g = pred[pred.cultivar == c].copy()
        tabla = g.pivot_table(index="fecha", columns="modelo", values="y_pred").reset_index()
        tabla.insert(1, "y_true", g.groupby("fecha").y_true.first().to_numpy())
        tabla["shock_P75"] = tabla.fecha.isin(mk.meses_shock)
        fig, ax = plt.subplots(figsize=(ESTILO["ancho_columna_pulg"], 2.3))
        x = range(len(tabla))
        for i, es in zip(x, tabla.shock_P75):
            if es:
                ax.axvspan(i - 0.5, i + 0.5, color=ESTILO["sombreado_shock"], alpha=0.5, lw=0)
        ax.plot(x, tabla.y_true, color="black", lw=1.4, label="Observed")
        for m in ("SARIMA", "GC3"):
            ax.plot(x, tabla[m], color=COLORES[m], marker=MARCADORES[m], ms=3, lw=1, label=m)
        ax.set_xticks(list(x), [f[5:] for f in tabla.fecha])
        ax.set_xlabel("Month (2025)")
        ax.set_ylabel("Production (t)")
        ax.legend(frameon=False, ncol=3)
        rutas = guardar(fig, SAL, f"figB01_pipeline_test_real_vs_pred_2025_{c}", tabla,
                        pie=f"PIPELINE TEST ONLY. Observed vs one-step forecasts, {c} lime, 2025; grey = P75 shock months (history to origin).",
                        lectura="Pipeline check: SARIMA and GC3 seed 0 reproduce the official v2 forecasts. Not a result figure.")
        with Image.open(rutas["png"]) as im:
            dpi = im.info.get("dpi")
        res[c] = {"archivos": rutas, "existen": all(Path(p).exists() for p in rutas.values()), "dpi_png": [round(d) for d in dpi] if dpi else None,
                  "csv_filas": int(len(pd.read_csv(rutas["csv"]))), "pdf_bytes": Path(rutas["pdf"]).stat().st_size}
    (SAL / "verificacion_figuras.json").write_text(json.dumps(res, indent=2), encoding="utf-8")
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
