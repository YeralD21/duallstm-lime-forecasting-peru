"""Prueba de reanudacion de la Fase C en una ventana pequena (2021): interrumpe cada etapa a proposito y la reanuda.

Para cada etapa:
  1. corrida interrumpida en reanudacion/c<NN>/int/: con --interrumpir-en n (corte simulado con os._exit despues de
     escribir los archivos en .tmp) o matando el arbol de procesos con taskkill /T /F a mitad de una unidad;
  2. misma orden otra vez en la misma carpeta (reanudacion);
  3. una tercera vez: todas las unidades deben saltarse;
  4. corrida limpia sin interrupcion en reanudacion/c<NN>/limpia/.
Verifica: la 1 termina con error y deja una carpeta .tmp; la 2 termina bien, borra la .tmp y no repite unidades
completas; la 3 no hace nada nuevo; no queda ninguna .tmp; todos los CSV de la reanudada son identicos byte a byte
a los de la limpia. Salida: 10_logs/verificaciones/fase_c_prueba/reanudacion/resultado.json (no toca 04_modelos).

Uso:  python tests/test_reanudacion.py [--casos 03 04 05 06 07]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lib.entorno import BR, VARIABLES_ENTORNO, preparar_entorno  # noqa: E402

preparar_entorno()

import argparse  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import re  # noqa: E402
import shutil  # noqa: E402
import subprocess  # noqa: E402
import time  # noqa: E402

SCRIPTS = BR / "02_scripts"
BASE = BR / "10_logs" / "verificaciones" / "fase_c_prueba" / "reanudacion"
ANIO = "2021"

# caso: (script, argumentos, etapa, modo de interrupcion)
#   ("simulada", n): --interrumpir-en n
#   ("taskkill", k, s): mata el arbol cuando el log tiene k unidades [OK] y s segundos despues del siguiente [INICIO]
CASOS = {
    "03": ("03_modelos_sin_ajuste.py", ["--anios", ANIO], "03_modelos_sin_ajuste", ("simulada", 3)),
    "04": ("04_sarima.py", ["--anios", ANIO], "04_sarima", ("taskkill", 1, 15)),
    "05": ("05_lineales.py", ["--anios", ANIO], "05_lineales", ("simulada", 2)),
    "06": ("06_xgb.py", ["--anios", ANIO, "--semillas", "0", "1", "2"], "06_xgb", ("simulada", 5)),
    "07": ("07_lstm.py", ["--todas", "--anios", ANIO, "--semillas", "0", "1"], "07_lstm", ("taskkill", 2, 4)),
}
RE_OK_UNIDAD = re.compile(r"\[OK\] (?!etapa)")


def env() -> dict:
    return {**os.environ, **VARIABLES_ENTORNO}


def correr(script: str, args: list[str], raiz: Path, extra: list[str] | None = None) -> int:
    cmd = [sys.executable, str(SCRIPTS / script), *args, "--salida", str(raiz), *(extra or [])]
    with open(raiz / "consola.txt", "a", encoding="utf-8") as out:
        return subprocess.run(cmd, env=env(), stdout=out, stderr=subprocess.STDOUT).returncode


def correr_y_matar(script: str, args: list[str], raiz: Path, log: Path, k: int, espera: float) -> dict:
    cmd = [sys.executable, str(SCRIPTS / script), *args, "--salida", str(raiz)]
    with open(raiz / "consola.txt", "a", encoding="utf-8") as out:
        p = subprocess.Popen(cmd, env=env(), stdout=out, stderr=subprocess.STDOUT)
        t_inicio_objetivo = None
        while p.poll() is None:
            lineas = log.read_text(encoding="utf-8").splitlines() if log.exists() else []
            n_ok = sum(1 for x in lineas if RE_OK_UNIDAD.search(x))
            if n_ok >= k and t_inicio_objetivo is None and lineas and re.search(r"\[INICIO\] (?!etapa|integridad)", lineas[-1]):
                t_inicio_objetivo = time.monotonic()
            if t_inicio_objetivo is not None and time.monotonic() - t_inicio_objetivo >= espera:
                r = subprocess.run(["taskkill", "/PID", str(p.pid), "/T", "/F"], capture_output=True, text=True)
                p.wait()
                return {"matado": True, "taskkill": r.stdout.strip().splitlines(), "codigo": p.returncode}
            time.sleep(0.2)
    return {"matado": False, "codigo": p.returncode}


def tmps(raiz: Path) -> list[str]:
    return sorted(p.relative_to(raiz).as_posix() for p in (raiz / "04_modelos").rglob("*.tmp") if p.is_dir())


def completas(raiz: Path) -> list[str]:
    return sorted(p.parent.relative_to(raiz).as_posix() for p in (raiz / "04_modelos").rglob("completado.json")
                  if not p.parent.name.endswith(".tmp"))


def csvs(raiz: Path) -> dict[str, bytes]:
    return {p.relative_to(raiz).as_posix(): p.read_bytes() for p in (raiz / "04_modelos").rglob("*.csv")}


def caso(clave: str) -> dict:
    script, args, etapa, modo = CASOS[clave]
    d = BASE / f"c{clave}"  # rutas cortas: git en Windows no indexa rutas de mas de 260 caracteres
    if d.exists():
        shutil.rmtree(d)
    a, b = d / "int", d / "limpia"
    a.mkdir(parents=True)
    b.mkdir(parents=True)
    log = a / "10_logs" / "ejecucion" / f"faseC_{etapa}.log"
    t0 = time.perf_counter()
    if modo[0] == "simulada":
        r1 = {"codigo": correr(script, args, a, ["--interrumpir-en", str(modo[1])]), "modo": f"--interrumpir-en {modo[1]}"}
    else:
        r1 = {**correr_y_matar(script, args, a, log, modo[1], modo[2]), "modo": f"taskkill tras {modo[1]} OK + {modo[2]} s"}
    r1.update(tmp_tras_corte=tmps(a), completas_tras_corte=len(completas(a)))
    r2 = {"codigo": correr(script, args, a), "tmp": tmps(a), "completas": len(completas(a))}
    texto = log.read_text(encoding="utf-8")
    bloques = texto.split("[INICIO] etapa ")
    r2["saltadas_en_reanudacion"] = bloques[2].count("ya completada") if len(bloques) > 2 else None
    r2["nuevas_en_reanudacion"] = len(RE_OK_UNIDAD.findall(bloques[2])) - r2["saltadas_en_reanudacion"] if len(bloques) > 2 else None
    r3 = {"codigo": correr(script, args, a)}
    bloques = log.read_text(encoding="utf-8").split("[INICIO] etapa ")
    r3["nuevas"] = len(re.findall(r"\[INICIO\] (?!etapa|integridad)", bloques[3]))
    r3["saltadas"] = bloques[3].count("ya completada")
    r4 = {"codigo": correr(script, args, b), "completas": len(completas(b))}
    ca, cb = csvs(a), csvs(b)
    distintos = sorted(k for k in set(ca) | set(cb) if ca.get(k) != cb.get(k))
    ok = (r1["codigo"] != 0 and len(r1["tmp_tras_corte"]) == 1 and r2["codigo"] == 0 and not r2["tmp"]
          and r2["saltadas_en_reanudacion"] == r1["completas_tras_corte"] and r3["codigo"] == 0 and r3["nuevas"] == 0
          and r3["saltadas"] == r2["completas"] and r4["codigo"] == 0 and r4["completas"] == r2["completas"]
          and not distintos and len(ca) > 0)
    return {"etapa": etapa, "script": script, "args": args, "OK": ok, "corrida_1_interrumpida": r1, "corrida_2_reanudada": r2,
            "corrida_3_repetida": r3, "corrida_limpia": r4, "csv_comparados": len(ca), "csv_distintos": distintos,
            "segundos": round(time.perf_counter() - t0, 1), "log": log.relative_to(BR).as_posix()}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--casos", nargs="+", default=list(CASOS))
    claves = ap.parse_args().casos
    BASE.mkdir(parents=True, exist_ok=True)
    salida = BASE / "resultado.json"
    res = json.loads(salida.read_text(encoding="utf-8")) if salida.exists() else {}
    for k in claves:
        res[k] = caso(k)
        print(json.dumps({k: {"OK": res[k]["OK"], "segundos": res[k]["segundos"]}}), flush=True)
        salida.write_text(json.dumps(res, indent=2, ensure_ascii=False), encoding="utf-8")
    if not all(res[k]["OK"] for k in claves):
        raise SystemExit("Alguna prueba de reanudacion fallo; ver resultado.json")


if __name__ == "__main__":
    main()
