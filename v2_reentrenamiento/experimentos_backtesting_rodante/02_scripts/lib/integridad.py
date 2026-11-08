"""Hashes SHA-256 del codigo oficial, los datos y Chronos; manifest del entorno.

Metodo de hash (DESVIACIONES.md, DESV-01): en archivos de texto (por extension) se normaliza CRLF -> LF antes
del SHA-256, para que el hash no dependa de core.autocrlf al clonar; los binarios se hashean byte a byte.
El metodo queda escrito en hashes_congelados.json bajo la clave "_metodo".
"""
from __future__ import annotations

import hashlib
import json
import os
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from lib.entorno import BR, CONFIG, RAIZ_REPO, V2, VARIABLES_ENTORNO

HASHES_CONGELADOS = CONFIG / "hashes_congelados.json"
MANIFEST = CONFIG / "manifest.json"
LIBRERIAS = ("numpy", "pandas", "scipy", "sklearn", "statsmodels", "xgboost", "tensorflow", "keras",
             "torch", "transformers", "matplotlib", "joblib", "safetensors")


EXTENSIONES_TEXTO = (".py", ".csv", ".json", ".md", ".txt", ".mjs", ".cfg", ".toml", ".yaml", ".yml", ".ini")
METODO_NORMALIZADO = {
    "version": 2,
    "texto": "extension en extensiones_texto: se reemplaza CRLF (bytes 0D 0A) por LF (byte 0A) y luego SHA-256",
    "extensiones_texto": list(EXTENSIONES_TEXTO),
    "binarios": "cualquier otra extension: SHA-256 de los bytes tal cual",
    "motivo": "core.autocrlf convierte los fines de linea al clonar; el hash de bytes no seria reproducible en otro clon",
    "registro": "09_reportes/DESVIACIONES.md (DESV-01): cambio de implementacion, no de protocolo",
}


def sha256(ruta: Path) -> str:
    """SHA-256 de los bytes tal cual (metodo version 1)."""
    h = hashlib.sha256()
    with open(ruta, "rb") as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def sha256_normalizado(ruta: Path) -> str:
    """Metodo version 2: texto con CRLF -> LF; binarios byte a byte."""
    ruta = Path(ruta)
    if ruta.suffix.lower() not in EXTENSIONES_TEXTO:
        return sha256(ruta)
    return hashlib.sha256(ruta.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


class Integridad:
    """Calcula y verifica los hashes de todo lo que el experimento lee de fuera de su carpeta."""

    def __init__(self) -> None:
        self.rutas = json.loads((CONFIG / "rutas_datos.json").read_text(encoding="utf-8"))

    def archivos_codigo(self) -> list[Path]:
        src = RAIZ_REPO / self.rutas["codigo_oficial"]
        return sorted(p for p in src.rglob("*.py") if "__pycache__" not in p.parts)

    def archivos_datos(self) -> list[Path]:
        claves = ["produccion_nacional", "produccion_provincial", "nasa_provincial", "indeci_provincial", "sentimiento_mensual"]
        plantillas = [self.rutas[k] for k in claves] + list(self.rutas["referencias_oficiales"].values())
        vistos: list[Path] = []
        for p in plantillas:
            for c in ("sutil", "dulce"):
                ruta = RAIZ_REPO / p.format(c=c)
                if ruta not in vistos:
                    vistos.append(ruta)
        return vistos

    def archivos_chronos(self) -> list[Path]:
        vendor = RAIZ_REPO / self.rutas["chronos_vendor"]
        cache = Path(os.path.expanduser(self.rutas["chronos_cache"]))
        snap = cache / "snapshots" / "a0e552de83495b5c28c14c71c374f3e33280b340"
        codigo = sorted(p for p in vendor.rglob("*.py") if "__pycache__" not in p.parts)
        return codigo + [snap / "config.json", snap / "model.safetensors"]

    def calcular(self, funcion=sha256_normalizado) -> dict[str, dict[str, str]]:
        def rel(p: Path) -> str:
            try:
                return p.relative_to(RAIZ_REPO).as_posix()
            except ValueError:
                return "~/" + p.relative_to(Path.home()).as_posix()
        return {
            "codigo_oficial": {rel(p): funcion(p) for p in self.archivos_codigo()},
            "datos": {rel(p): funcion(p) for p in self.archivos_datos()},
            "chronos": {rel(p): funcion(p) for p in self.archivos_chronos()},
        }

    def congelar(self) -> dict:
        hashes = {"_metodo": METODO_NORMALIZADO, **self.calcular()}
        HASHES_CONGELADOS.write_text(json.dumps(hashes, indent=2, ensure_ascii=False), encoding="utf-8")
        return hashes

    @staticmethod
    def _diferencias(congelado: dict, actual: dict) -> list[str]:
        difs = []
        for grupo, tabla in congelado.items():
            if grupo.startswith("_"):
                continue
            for ruta, h in tabla.items():
                if actual.get(grupo, {}).get(ruta) != h:
                    difs.append(f"{grupo}: {ruta}")
            for ruta in set(actual.get(grupo, {})) - set(tabla):
                difs.append(f"{grupo}: archivo nuevo {ruta}")
        return difs

    def verificar(self) -> dict:
        """Aborta si cualquier hash difiere del congelado (con el metodo declarado en el archivo)."""
        if not HASHES_CONGELADOS.exists():
            raise RuntimeError("No existe hashes_congelados.json: ejecute 00_verificar_entorno.py --congelar.")
        congelado = json.loads(HASHES_CONGELADOS.read_text(encoding="utf-8"))
        version = congelado.get("_metodo", {}).get("version", 1)
        difs = self._diferencias(congelado, self.calcular(sha256_normalizado if version == 2 else sha256))
        if difs:
            raise RuntimeError("ABORTO: cambiaron archivos congelados:\n  " + "\n  ".join(difs))
        return {"metodo_version": version, "diferencias": 0,
                "verificados": sum(len(t) for g, t in congelado.items() if not g.startswith("_"))}

    def normalizar_una_vez(self) -> dict:
        """Regenera hashes_congelados.json con el metodo version 2 (DESV-01). Solo una vez.

        Antes verifica byte a byte contra la version 1: si algo cambio, aborta sin escribir.
        La version 1 se conserva como hashes_congelados_v1_bytes.json para auditoria.
        """
        congelado = json.loads(HASHES_CONGELADOS.read_text(encoding="utf-8"))
        if "_metodo" in congelado:
            raise RuntimeError("hashes_congelados.json ya usa el metodo normalizado; no se regenera otra vez.")
        difs = self._diferencias(congelado, self.calcular(sha256))
        if difs:
            raise RuntimeError("ABORTO: la verificacion byte a byte fallo antes de normalizar:\n  " + "\n  ".join(difs))
        respaldo = CONFIG / "hashes_congelados_v1_bytes.json"
        if respaldo.exists():
            raise RuntimeError(f"Ya existe {respaldo.name}; no se sobrescribe.")
        respaldo.write_bytes(HASHES_CONGELADOS.read_bytes())
        nuevo = self.congelar()
        cambiados = {g: sorted(r for r in t if congelado[g][r] != t[r]) for g, t in nuevo.items() if not g.startswith("_")}
        return {"archivos": sum(len(t) for g, t in nuevo.items() if not g.startswith("_")),
                "hash_distinto_por_CRLF": {g: len(v) for g, v in cambiados.items()}, "respaldo_v1": respaldo.name}


def _version(nombre: str) -> str:
    try:
        mod = __import__(nombre)
        return str(getattr(mod, "__version__", "?"))
    except Exception as exc:  # pragma: no cover - solo informativo
        return f"no disponible ({type(exc).__name__})"


def _hardware() -> dict:
    info = {"plataforma": platform.platform(), "procesador": platform.processor(), "nucleos_logicos": os.cpu_count()}
    try:
        salida = subprocess.run(["wmic", "computersystem", "get", "TotalPhysicalMemory"], capture_output=True, text=True, timeout=20)
        numeros = [s for s in salida.stdout.split() if s.isdigit()]
        if numeros:
            info["ram_gb"] = round(int(numeros[0]) / 1024 ** 3, 1)
        salida = subprocess.run(["wmic", "cpu", "get", "Name"], capture_output=True, text=True, timeout=20)
        lineas = [s.strip() for s in salida.stdout.splitlines() if s.strip() and s.strip() != "Name"]
        if lineas:
            info["cpu"] = lineas[0]
    except Exception as exc:  # pragma: no cover
        info["wmic"] = f"no disponible ({type(exc).__name__})"
    return info


def escribir_manifest(extra: dict | None = None) -> dict:
    try:
        commit = subprocess.run(["git", "rev-parse", "HEAD"], cwd=RAIZ_REPO, capture_output=True, text=True).stdout.strip()
        # Solo lectura: --no-optional-locks evita que git status reescriba el indice (.git/index)
        estado_git = subprocess.run(["git", "--no-optional-locks", "status", "--porcelain"], cwd=RAIZ_REPO,
                                    capture_output=True, text=True, encoding="utf-8").stdout.splitlines()
    except Exception:  # pragma: no cover
        commit, estado_git = None, None
    manifest = {
        "generado_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version,
        "ejecutable": sys.executable,
        "librerias": {n: _version(n) for n in LIBRERIAS},
        "hardware": _hardware(),
        "variables_entorno": {k: os.environ.get(k) for k in VARIABLES_ENTORNO},
        "semilla_global": 42,
        "git_commit": commit,
        "git_status_porcelain": estado_git,
        "carpeta_experimento": BR.relative_to(RAIZ_REPO).as_posix(),
        "hashes_congelados": HASHES_CONGELADOS.relative_to(RAIZ_REPO).as_posix(),
        "hash_de_hashes_congelados": sha256(HASHES_CONGELADOS) if HASHES_CONGELADOS.exists() else None,
    }
    if extra:
        manifest.update(extra)
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return manifest
