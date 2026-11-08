"""
Utilidades de trazabilidad por SHA-256.

CONVENCION NUEVA INTRODUCIDA EN v2 (decision D19, 2026-09-07).
Ni v1 ni la Fase 2 v2 original registraban checksums de sus artefactos.
"""
from __future__ import annotations

import hashlib
import os
from pathlib import Path


class Hasher:
    """Calcula y formatea checksums SHA-256 de artefactos del pipeline."""

    ALGORITMO = 'sha256'
    _CHUNK = 1 << 20

    @classmethod
    def sha256(cls, ruta: str | Path) -> str:
        h = hashlib.sha256()
        with open(ruta, 'rb') as f:
            for bloque in iter(lambda: f.read(cls._CHUNK), b''):
                h.update(bloque)
        return h.hexdigest()

    @classmethod
    def describir(cls, ruta: str | Path) -> dict:
        """Devuelve {ruta, sha256, bytes} para incrustar en metadata JSON."""
        ruta = Path(ruta)
        return {
            'ruta': ruta.as_posix(),
            'sha256': cls.sha256(ruta),
            'bytes': os.path.getsize(ruta),
        }

    @classmethod
    def describir_varios(cls, rutas) -> list[dict]:
        return [cls.describir(r) for r in rutas if Path(r).exists()]
