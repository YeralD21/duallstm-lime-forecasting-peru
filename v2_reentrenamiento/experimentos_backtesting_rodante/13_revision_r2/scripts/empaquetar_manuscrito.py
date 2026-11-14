"""R2, Dia 3: arma 13_revision_r2/paquete_manuscrito.zip con el material para el manuscrito.

Contenido: latex/ (tablas de T15), las 2 figuras de T11 (PDF, y PNG/TXT de apoyo), CIFRAS_CLAVE.md, INFORME_DIA1.md,
INFORME_DIA2.md, INFORME_DIA3.md y HISTORIAL_PROTOCOLO.md. Zip determinista: orden fijo de entradas y fecha fija
(1980-01-01), para que dos ejecuciones con los mismos archivos den el mismo zip. Antes, comprueba que existen todos.
Uso: python 13_revision_r2/scripts/empaquetar_manuscrito.py
"""
import hashlib
import zipfile
from pathlib import Path

R2 = Path(__file__).resolve().parents[1]
ZIP = R2 / "paquete_manuscrito.zip"
ARCH = (sorted((R2 / "latex").glob("*.tex"))
        + [R2 / "figuras" / f"fig20_real_vs_pred_2025_main_{c}.{e}" for c in ("sutil", "dulce") for e in ("pdf", "png", "txt")]
        + [R2 / n for n in ("CIFRAS_CLAVE.md", "INFORME_DIA1.md", "INFORME_DIA2.md", "INFORME_DIA3.md", "HISTORIAL_PROTOCOLO.md")])


def main() -> None:
    falta = [str(p.relative_to(R2)) for p in ARCH if not p.exists()]
    if falta or not any(p.parent.name == "latex" for p in ARCH):
        raise SystemExit(f"Faltan archivos: {falta or 'latex/*.tex'}")
    with zipfile.ZipFile(ZIP, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for p in ARCH:
            info = zipfile.ZipInfo(p.relative_to(R2).as_posix(), date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, p.read_bytes())
    print(f"{ZIP.name}: {len(ARCH)} archivos, {ZIP.stat().st_size:,} bytes, SHA-256 {hashlib.sha256(ZIP.read_bytes()).hexdigest()}")
    for p in ARCH:
        print("  ", p.relative_to(R2).as_posix())


if __name__ == "__main__":
    main()
