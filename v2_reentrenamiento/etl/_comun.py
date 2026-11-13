"""Utilidades comunes del ETL reproducible (revisión G7, observación 12).

- Rutas del repositorio y carpeta de salida temporal (nunca data/interim).
- SHA-256 con el método 2 de 01_configuracion/hashes_congelados.json (CRLF -> LF en .csv).
- Comparación fila a fila, celda a celda, como texto (tolerancia 0).
- Fuentes de datos: data_sources.json (raíz del repositorio) da el nombre, el link, la ruta esperada y el
  SHA-256 de cada archivo crudo. verificar_crudo() usa esos datos: si falta el archivo, termina con un mensaje
  que indica el link y la ruta; si el SHA-256 no coincide, advierte que no es el archivo usado en el artículo
  (y termina solo con --estricto).
"""
from __future__ import annotations

import hashlib
import json
import sys
import tempfile
from pathlib import Path

import pandas as pd

ETL = Path(__file__).resolve().parent
V2 = ETL.parent
RAIZ = V2.parent
INTERIM = V2 / "data" / "interim"
RAW = V2 / "data" / "raw"
HASHES = V2 / "experimentos_backtesting_rodante" / "01_configuracion" / "hashes_congelados.json"
SALIDA_POR_DEFECTO = Path(tempfile.gettempdir()) / "etl_v2_salida"
FUENTES = RAIZ / "data_sources.json"


def carpeta_salida(ruta: str | None) -> Path:
    """Devuelve la carpeta de salida y se niega a escribir dentro de data/interim."""
    p = Path(ruta).resolve() if ruta else SALIDA_POR_DEFECTO
    if p == INTERIM.resolve() or INTERIM.resolve() in p.parents:
        raise SystemExit(f"Salida dentro de data/interim ({p}): no permitido; las tablas congeladas no se sobrescriben.")
    p.mkdir(parents=True, exist_ok=True)
    return p


def sha256_norm(ruta: Path) -> str:
    """Método 2 de hashes_congelados.json: en archivos de texto, CRLF -> LF y luego SHA-256."""
    b = Path(ruta).read_bytes()
    if Path(ruta).suffix.lower() in {".py", ".csv", ".json", ".md", ".txt"}:
        b = b.replace(b"\r\n", b"\n")
    return hashlib.sha256(b).hexdigest()


def hash_congelado(rel_repo: str) -> str | None:
    """Hash registrado en hashes_congelados.json (clave 'datos'), o None si el archivo no está registrado."""
    d = json.loads(HASHES.read_text(encoding="utf-8"))
    return d.get("datos", {}).get(rel_repo)


def comparar(nuevo: Path, congelado: Path, rel_repo: str) -> dict:
    """Igualdad fila a fila y celda a celda (texto, tolerancia 0) y SHA-256 frente al congelado."""
    a = pd.read_csv(nuevo, dtype=str, keep_default_na=False, encoding="utf-8")
    b = pd.read_csv(congelado, dtype=str, keep_default_na=False, encoding="utf-8")
    r = {
        "archivo": rel_repo,
        "filas_nuevo": len(a), "filas_congelado": len(b),
        "columnas_iguales": list(a.columns) == list(b.columns),
    }
    if r["columnas_iguales"] and len(a) == len(b):
        dif = a.ne(b)
        r["celdas_distintas"] = int(dif.to_numpy().sum())
        r["filas_distintas"] = int(dif.any(axis=1).sum())
        if r["celdas_distintas"]:
            i = dif.any(axis=1).idxmax()
            r["primera_fila_distinta"] = {"fila": int(i), "nuevo": a.loc[i].to_dict(), "congelado": b.loc[i].to_dict()}
    else:
        r["celdas_distintas"] = None
    r["sha256_nuevo"] = sha256_norm(nuevo)
    r["sha256_congelado_disco"] = sha256_norm(congelado)
    r["sha256_registrado"] = hash_congelado(rel_repo)
    r["igual_a_disco"] = r["sha256_nuevo"] == r["sha256_congelado_disco"]
    r["igual_a_registrado"] = (r["sha256_nuevo"] == r["sha256_registrado"]) if r["sha256_registrado"] else None
    return r


def escribir_csv(df: pd.DataFrame, ruta: Path) -> Path:
    """CSV UTF-8 con fin de línea LF (el hash normalizado es independiente de CRLF/LF)."""
    df.to_csv(ruta, index=False, lineterminator="\n", encoding="utf-8")
    return ruta


def informe(resultados: list[dict], ruta: Path) -> None:
    ruta.write_text(json.dumps(resultados, indent=1, ensure_ascii=False), encoding="utf-8")
    for r in resultados:
        estado = "IDENTICO" if r.get("igual_a_disco") else "DISTINTO"
        reg = r.get("igual_a_registrado")
        reg_txt = "sin hash registrado" if reg is None else ("= hashes_congelados.json" if reg else "!= hashes_congelados.json")
        print(f"[{estado}] {r['archivo']}: filas {r['filas_nuevo']}/{r['filas_congelado']}, "
              f"celdas distintas {r.get('celdas_distintas')}, SHA-256 {reg_txt}")


# ---------------------------------------------------------------- fuentes de datos (data_sources.json)
def fuente(clave: str) -> dict:
    """Entrada `clave` de data_sources.json (p. ej. 'midagri_sisagri', 'indeci', 'geoboundaries')."""
    return json.loads(FUENTES.read_text(encoding="utf-8"))["sources"][clave]


def archivo_fuente(clave: str, nombre: str) -> dict:
    """Archivo `nombre` (expected_file) de la fuente `clave` en data_sources.json."""
    for f in fuente(clave)["files"]:
        if f["expected_file"] == nombre:
            return f
    raise KeyError(f"{nombre} no figura en data_sources.json ({clave})")


def ruta_esperada(clave: str, nombre: str) -> Path | None:
    """Ruta absoluta registrada en data_sources.json, o None si el archivo no se guarda en el repositorio."""
    r = archivo_fuente(clave, nombre)["path"]
    return RAIZ / r if r else None


def _sha256_bytes_y_norm(ruta: Path) -> set[str]:
    """SHA-256 de los bytes tal cual y, en archivos de texto, también con CRLF -> LF (método 2)."""
    b = Path(ruta).read_bytes()
    return {hashlib.sha256(b).hexdigest(), sha256_norm(ruta)}


def verificar_crudo(clave: str, nombre: str, ruta: Path, estricto: bool = False) -> None:
    """Comprueba el archivo crudo `ruta` con data_sources.json.

    - Si no existe: termina (SystemExit) con la fuente, el link y la ruta esperada.
    - Si existe y su SHA-256 no coincide con el registrado: advertencia en stderr de que no es el archivo
      usado en el artículo; la ejecución sigue, salvo con estricto=True (--estricto), que termina.
    """
    f, src = archivo_fuente(clave, nombre), fuente(clave)
    ruta = Path(ruta)
    esperada = RAIZ / f["path"] if f["path"] else None
    if not ruta.exists():
        lineas = [f"Falta el archivo crudo: {ruta}",
                  f"  Fuente: {src['name']}",
                  f"  Link: {src['link']}"]
        if f.get("download_url"):
            lineas.append(f"  Descarga directa: {f['download_url']}")
        lineas.append(f"  Archivo esperado: {f['expected_file']}"
                      + (f" ({f['size_bytes']:,} bytes)" if f.get("size_bytes") else ""))
        if esperada:
            lineas.append(f"  Ruta esperada: {esperada}")
        if f.get("sha256"):
            lineas.append(f"  SHA-256 del archivo usado en el artículo: {f['sha256']}")
        lineas.append("  (datos tomados de data_sources.json)")
        raise SystemExit("\n".join(lineas))
    if not f.get("sha256"):
        return
    hashes = _sha256_bytes_y_norm(ruta)
    if f["sha256"] in hashes:
        print(f"SHA-256 de {ruta.name} verificado (= data_sources.json).")
        return
    msg = (f"ADVERTENCIA: el SHA-256 de {ruta} ({sorted(hashes)[0]}) no coincide con el registrado en "
           f"data_sources.json ({f['sha256']}). No es el archivo usado en el artículo; los resultados pueden diferir.")
    if estricto:
        raise SystemExit(msg + " Se detiene por --estricto.")
    print(msg, file=sys.stderr, flush=True)
