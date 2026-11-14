"""R2-T14 (obs. 8): historial fechado de los archivos de protocolo y preregistro en el repositorio antiguo (privado).

SOLO LECTURA sobre el repositorio antiguo: usa unicamente `git log` y `git show` (no checkout, no fetch, no escribe
nada en el). Para cada archivo de protocolo/preregistro:
    git log --follow --format="%H %ad %s" --date=iso -- <ruta>
(ademas: fecha de commit %cd y ruta del archivo en cada commit, por si fue renombrado), y para cada version el
SHA-256 de `git show <commit>:<ruta>` en bytes tal cual y con CRLF -> LF (metodo de hashes_congelados.json). La
ultima columna compara cada version con el archivo de este repositorio publicado (SHA-256 CRLF -> LF).
No es un paso de reproduce.py: el repositorio antiguo es privado y no se distribuye.
Salidas: 13_revision_r2/HISTORIAL_PROTOCOLO.md y resultados/T14_historial_protocolo.csv
Uso: python 13_revision_r2/scripts/t14_historial_protocolo.py --repo <ruta del clon del repositorio antiguo>
"""
from __future__ import annotations

import argparse
import hashlib
import subprocess
import sys
from pathlib import Path

R2 = Path(__file__).resolve().parents[1]
BR = R2.parent
RAIZ = BR.parents[1]
BR_REL = "v2_reentrenamiento/experimentos_backtesting_rodante"
# archivos de protocolo y preregistro (rutas iguales en ambos repositorios)
ARCHIVOS = [
    f"{BR_REL}/00_plan/borrador_preregistro.md",
    f"{BR_REL}/00_plan/plan_fase_A.md",
    f"{BR_REL}/00_plan/mapa_evidencia.md",
    f"{BR_REL}/00_plan/nota_chronos_pesos.md",
    f"{BR_REL}/01_configuracion/ventanas.json",
    f"{BR_REL}/01_configuracion/umbrales.json",
    f"{BR_REL}/01_configuracion/hiperparametros_congelados.json",
    f"{BR_REL}/01_configuracion/manifest.json",
    f"{BR_REL}/01_configuracion/hashes_congelados.json",
    f"{BR_REL}/01_configuracion/rutas_datos.json",
    f"{BR_REL}/01_configuracion/estilo_figuras.json",
    "v2_reentrenamiento/DECISIONES_METODOLOGICAS.md",
    f"{BR_REL}/09_reportes/DESVIACIONES.md",
    f"{BR_REL}/09_reportes/reporte_fase_A.md",
    f"{BR_REL}/09_reportes/reporte_fase_B.md",
    f"{BR_REL}/09_reportes/nota_v5_v3.md",
]
SEP = "\x1f"


def git(repo: Path, *args: str) -> bytes:
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True)
    if r.returncode != 0:
        raise SystemExit(f"git {' '.join(args)}: {r.stderr.decode(errors='replace')}")
    return r.stdout


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def historial(repo: Path, ruta: str) -> list[dict]:
    out = git(repo, "log", "--follow", "--name-only", f"--format=@@{SEP}%H{SEP}%ad{SEP}%cd{SEP}%s", "--date=iso", "--", ruta)
    filas, act = [], None
    for linea in out.decode("utf-8", errors="replace").splitlines():
        if linea.startswith("@@" + SEP):
            _, h, ad, cd, s = linea.split(SEP, 4)
            act = {"commit": h, "fecha_autor": ad, "fecha_commit": cd, "mensaje": s, "ruta_en_commit": None}
            filas.append(act)
        elif linea.strip() and act is not None and act["ruta_en_commit"] is None:
            act["ruta_en_commit"] = linea.strip()
    for f in filas:
        r = subprocess.run(["git", "-C", str(repo), "show", f"{f['commit']}:{f['ruta_en_commit']}"], capture_output=True)
        if r.returncode != 0:  # el commit borra el archivo
            f.update(sha256_bytes="(archivo borrado en este commit)", sha256_lf="", bytes=0)
        else:
            f.update(sha256_bytes=sha(r.stdout), sha256_lf=sha(r.stdout.replace(b"\r\n", b"\n")), bytes=len(r.stdout))
    return filas


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True, help="clon del repositorio antiguo (solo lectura)")
    repo = Path(ap.parse_args().repo).resolve()
    import pandas as pd

    rama = git(repo, "rev-parse", "--abbrev-ref", "HEAD").decode().strip()
    head = git(repo, "rev-parse", "HEAD").decode().strip()
    remotas = git(repo, "branch", "-r", "--contains", head).decode().split()
    filas = []
    for ruta in ARCHIVOS:
        pub = RAIZ / ruta
        sha_pub = sha(pub.read_bytes().replace(b"\r\n", b"\n")) if pub.exists() else None
        for f in historial(repo, ruta):
            f["archivo"] = ruta
            f["igual_al_publicado"] = (f["sha256_lf"] == sha_pub) if sha_pub else None
            filas.append(f)
    T = pd.DataFrame(filas)[["archivo", "commit", "fecha_autor", "fecha_commit", "mensaje", "ruta_en_commit", "bytes",
                             "sha256_bytes", "sha256_lf", "igual_al_publicado"]]
    T.to_csv(R2 / "resultados" / "T14_historial_protocolo.csv", index=False, lineterminator="\n")

    L = ["# Historial del protocolo y del preregistro (revisión R2, T14, obs. 8)", "",
         "<!-- generado por scripts/t14_historial_protocolo.py; no editar a mano -->", "",
         "Extraído del repositorio antiguo (privado) en modo solo lectura (`git log` y `git show`; sin checkout ni "
         "fetch). Está aquí y no en `01_configuracion/`, porque esa carpeta está preregistrada y congelada.", "",
         f"- Rama del clon: `{rama}`; HEAD `{head}`; ramas remotas (refs locales) que contienen HEAD: "
         f"{', '.join('`' + x + '`' for x in remotas) or 'ninguna'}.",
         "- Comando por archivo: `git log --follow --format=\"%H %ad %s\" --date=iso -- <ruta>`. Se añaden la fecha de "
         "commit (`%cd`) y la ruta en cada commit (`--name-only`).",
         "- SHA-256 de cada versión: `git show <commit>:<ruta>`, en bytes tal cual y con CRLF → LF (método de "
         "`hashes_congelados.json`). «Igual al publicado» compara esa versión con el archivo de este repositorio.",
         "- Las fechas son las que registra git en el clon (zona horaria del autor). No son un sello de tiempo de "
         "terceros: git permite fijarlas a mano. La prueba independiente sería la fecha de push en GitHub (registro "
         "de eventos del repositorio privado), que no se puede consultar sin red.", "",
         "## Resumen: primera versión de cada archivo", "",
         "| archivo | primer commit | fecha (autor) | mensaje | n versiones | última versión igual al publicado |",
         "|---|---|---|---|---|---|"]
    for ruta in ARCHIVOS:
        x = T[T.archivo == ruta]
        if x.empty:
            L.append(f"| `{ruta}` | (sin historial) | | | 0 | |")
            continue
        p, u = x.iloc[-1], x.iloc[0]
        L.append(f"| `{ruta.replace(BR_REL + '/', '')}` | `{p.commit[:10]}` | {p.fecha_autor} | {p.mensaje} | {len(x)} | "
                 f"{'sí' if u.igual_al_publicado else 'no'} |")
    import glob
    import json

    fin = sorted(json.loads(Path(f).read_text(encoding="utf-8"))["fin"]
                 for f in glob.glob(str(BR / "04_modelos" / "**" / "completado.json"), recursive=True))
    pre = T[T.fecha_autor.str.startswith("2026-10-25")][["commit", "fecha_autor", "mensaje"]].drop_duplicates()
    L += ["", "## Cronología frente a la ejecución del experimento (Fase C)", "",
          "- Commits del preregistro (25-oct-2026): "
          + "; ".join(f"`{h[:7]}` {fa} «{m}»" for h, fa, m in pre.itertuples(index=False)) + ".",
          f"- Unidades rolling-origin terminadas (`04_modelos/**/completado.json` de este repositorio, campo `fin`): "
          f"{len(fin)}, entre {fin[0]} y {fin[-1]}." if fin else "- No se encontraron `completado.json`.",
          "- Versiones posteriores al 25-oct de los archivos listados: ver la tabla de cada archivo (fecha y mensaje del "
          "commit). Los cambios de protocolo posteriores están registrados en `09_reportes/DESVIACIONES.md`."]
    L += ["", "## Historial completo por archivo", ""]
    for ruta in ARCHIVOS:
        x = T[T.archivo == ruta]
        L += [f"### `{ruta}`", "", "| commit | fecha (autor, %ad) | fecha (commit, %cd) | mensaje | bytes | SHA-256 (bytes) | SHA-256 (CRLF→LF) | igual al publicado |",
              "|---|---|---|---|---|---|---|---|"]
        for r in x.itertuples(index=False):
            ren = "" if r.ruta_en_commit == ruta else f" (ruta: `{r.ruta_en_commit}`)"
            L.append(f"| `{r.commit}` | {r.fecha_autor} | {r.fecha_commit} | {r.mensaje}{ren} | {r.bytes} | `{r.sha256_bytes}` | "
                     f"`{r.sha256_lf}` | {'sí' if r.igual_al_publicado else 'no'} |")
        L.append("")
    (R2 / "HISTORIAL_PROTOCOLO.md").write_text("\n".join(L), encoding="utf-8", newline="\n")
    print(f"{len(T)} versiones de {T.archivo.nunique()} archivos -> {R2 / 'HISTORIAL_PROTOCOLO.md'}")


if __name__ == "__main__":
    sys.exit(main())
