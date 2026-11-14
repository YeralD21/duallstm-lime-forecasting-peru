"""R2-T11 (obs. 10a): Figura 7 reducida (test 2025) en 13_revision_r2/figuras/. POSTERIOR AL PROTOCOLO.

fig20_real_vs_pred_2025_main_{sutil,dulce}: serie observada (linea negra gruesa con halo), GC3 como media de las 10
semillas, Chronos, SARIMA y Seasonal Naive; meses de shock MoM P75 (historia hasta el origen) en gris.
Reutiliza sin modificarlo 02_scripts/14_fig20_reducida_2025.py (mismo estilo que fig20 de 10_figuras.py): solo cambia
la carpeta de destino. No escribe en 08_graficos/.
Control: el CSV con los datos dibujados debe ser identico (bytes, CRLF -> LF) al publicado en
08_graficos/predicciones/ (registrado en expected_outputs_sha256.json).
Uso: python 13_revision_r2/scripts/t11_fig20_main.py
"""
import hashlib
import importlib.util
import sys
from pathlib import Path

R2 = Path(__file__).resolve().parents[1]
BR = R2.parent
S = BR / "02_scripts"
sys.path.insert(0, str(S))
from lib.entorno import preparar_entorno  # noqa: E402

preparar_entorno()

_spec = importlib.util.spec_from_file_location("fig20_reducida", S / "14_fig20_reducida_2025.py")
M = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(M)  # carga 10_figuras.py (datos y estilo); no ejecuta main()

DESTINO = R2 / "figuras"
_guardar_original = M.F._guardar


def _guardar_r2(fig, carpeta, base, datos, pie, lectura):
    return _guardar_original(fig, DESTINO, base, datos, pie, lectura)


M.F._guardar = _guardar_r2


def sha_lf(p: Path) -> str:
    return hashlib.sha256(p.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def main() -> None:
    for c in M.F.CULT:
        rutas = M.fig20_main(c)
        nuevo = Path(rutas["csv"])
        publicado = BR / "08_graficos" / "predicciones" / nuevo.name
        if sha_lf(nuevo) != sha_lf(publicado):
            raise SystemExit(f"{nuevo.name}: los datos dibujados no coinciden con el CSV publicado en 08_graficos/predicciones/")
        print(f"{c}: {rutas['pdf']} (datos identicos a 08_graficos/predicciones/{nuevo.name})")


if __name__ == "__main__":
    main()
