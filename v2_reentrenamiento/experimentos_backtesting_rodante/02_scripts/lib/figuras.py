"""Estilo MDPI y guardado de figuras: PNG 300 dpi + PDF + CSV con los numeros + TXT con pie y lectura."""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from lib.entorno import CONFIG

ESTILO = json.loads((CONFIG / "estilo_figuras.json").read_text(encoding="utf-8"))
COLORES = ESTILO["colores_modelo"]
MARCADORES = ESTILO["marcadores_modelo"]


def aplicar_estilo() -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    plt.rcParams.update({
        "font.family": ESTILO["fuente"], "font.size": ESTILO["tamano_base"], "axes.titlesize": ESTILO["tamano_base"],
        "axes.labelsize": ESTILO["tamano_base"], "legend.fontsize": ESTILO["tamano_base"] - 1,
        "xtick.labelsize": ESTILO["tamano_base"] - 1, "ytick.labelsize": ESTILO["tamano_base"] - 1,
        "axes.spines.top": False, "axes.spines.right": False, "pdf.fonttype": 42, "svg.fonttype": "none",
        "savefig.bbox": "tight", "savefig.dpi": ESTILO["dpi_png"],
    })


def guardar(fig, carpeta: Path, base: str, datos: pd.DataFrame, pie: str, lectura: str) -> dict:
    """Escribe base.png, base.pdf, base.csv y base.txt. Sin titulo dentro de la imagen (va en el pie)."""
    import matplotlib.pyplot as plt

    if fig.axes and any(ax.get_title() for ax in fig.axes) and not ESTILO["titulo_en_imagen"]:
        raise ValueError("La figura tiene titulo dentro de la imagen; va en el pie de figura.")
    carpeta.mkdir(parents=True, exist_ok=True)
    rutas = {ext: carpeta / f"{base}.{ext}" for ext in ("png", "pdf", "csv", "txt")}
    fig.savefig(rutas["png"], dpi=ESTILO["dpi_png"])
    fig.savefig(rutas["pdf"])
    plt.close(fig)
    datos.to_csv(rutas["csv"], index=False)
    rutas["txt"].write_text(f"Caption (suggested): {pie}\n\nReading: {lectura}\n", encoding="utf-8")
    return {k: str(v) for k, v in rutas.items()}
