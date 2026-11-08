"""Etapa 00: entorno, semillas, hashes congelados y manifest.json.

Uso:
  python 00_verificar_entorno.py --congelar   # solo la primera vez (Fase B): fija los hashes de referencia
  python 00_verificar_entorno.py --normalizar-hashes  # una sola vez: hash con CRLF -> LF en texto (DESV-01)
  python 00_verificar_entorno.py              # verifica; aborta si algun archivo congelado cambio
  python 00_verificar_entorno.py --fase C     # idem y guarda HEAD y git status --porcelain (registro de version)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.entorno import BR, preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import json  # noqa: E402
import os  # noqa: E402

from lib.integridad import HASHES_CONGELADOS, Integridad, escribir_manifest  # noqa: E402


def main() -> None:
    integ = Integridad()
    if "--congelar" in sys.argv:
        if HASHES_CONGELADOS.exists():
            raise SystemExit("hashes_congelados.json ya existe; no se sobrescribe (borrarlo exige aprobacion).")
        h = integ.congelar()
        estado = {"accion": "congelado", "n_archivos": {k: len(v) for k, v in h.items() if not k.startswith("_")}}
    elif "--normalizar-hashes" in sys.argv:
        estado = {"accion": "normalizado (DESV-01)", **integ.normalizar_una_vez()}
        estado["verificacion_posterior"] = integ.verificar()
    else:
        estado = {"accion": "verificado", **integ.verificar()}
    faltan = [k for k, v in {"TF_ENABLE_ONEDNN_OPTS": "0", "TF_DETERMINISTIC_OPS": "1", "PYTHONHASHSEED": "42", "HF_HUB_OFFLINE": "1"}.items()
              if os.environ.get(k) != v]
    if faltan:
        raise SystemExit(f"Variables de entorno incorrectas: {faltan}")
    fase = sys.argv[sys.argv.index("--fase") + 1] if "--fase" in sys.argv else None
    m = escribir_manifest({"integridad": estado, "fase": fase})
    if fase == "C":
        # Registro de version del arranque de la Fase C: una copia por arranque (las reanudaciones agregan otra)
        copia = BR / "10_logs" / "ejecucion" / "manifiestos_faseC" / f"manifest_{m['generado_utc'][:19].replace(':', '')}.json"
        copia.parent.mkdir(parents=True, exist_ok=True)
        copia.write_text(json.dumps(m, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"[manifest Fase C] HEAD {m['git_commit']} | {len(m['git_status_porcelain'] or [])} lineas en git status | copia {copia.name}")
    print(json.dumps({"integridad": estado, "variables_entorno": m["variables_entorno"], "librerias": m["librerias"]}, indent=2))


if __name__ == "__main__":
    main()
