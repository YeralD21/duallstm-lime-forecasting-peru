"""Etapa 07: GC3 y GE. Cada corrida (ventana, cultivar, modelo, semilla) en un subproceso nuevo.

Una corrida:   python 07_lstm.py --anio 2025 --cultivar sutil --modelo GC3 --semilla 0 [--salida DIR | --destino DIR]
               (--salida: raiz con la estructura <modelo>/<cultivo>/<anio>/seed_XX, como en la Fase B;
                --destino: carpeta exacta, la usa el orquestador)
Orquestador:   python 07_lstm.py --todas [--anios ...] [--cultivares ...] [--modelos GC3 GE] [--semillas ...] [--salida RAIZ]
               (Fase C, reanudable: una unidad por modelo, cultivo, ventana y semilla; ver lib/reanudacion.py.
                Aqui --salida es la raiz que contiene 04_modelos/, 05_predicciones/ y 10_logs/)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.entorno import BR, preparar_entorno  # noqa: E402

preparar_entorno()

import argparse  # noqa: E402
import json  # noqa: E402
import subprocess  # noqa: E402

MODELOS = ("GC3", "GE")


def una(args) -> None:
    from lib.integridad import Integridad
    from lib.modelo_lstm import entrenar_y_predecir

    Integridad().verificar()
    if args.destino:
        destino = Path(args.destino)
    else:
        raiz = Path(args.salida) if args.salida else BR / "04_modelos"
        carpeta = {"GC3": "gc3_lstm_sin_nlp", "GE": "ge_lstm_con_nlp"}[args.modelo]
        destino = raiz / carpeta / args.cultivar / str(args.anio) / f"seed_{args.semilla:02d}"
    estado = entrenar_y_predecir(args.anio, args.cultivar, args.modelo, args.semilla, destino)
    print(json.dumps(estado, default=str))


def trabajo(u, v, tmp: Path) -> dict:
    cmd = [sys.executable, __file__, "--anio", str(u.anio), "--cultivar", u.cultivar, "--modelo", u.modelo,
           "--semilla", str(u.semilla), "--destino", str(tmp)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"subproceso con codigo {r.returncode}: {r.stderr.strip()[-1500:]}")
    estado = json.loads(r.stdout.strip().splitlines()[-1])
    p = json.loads((tmp / "estado_final.json").read_text(encoding="utf-8"))
    if p["semilla"] != u.semilla or p["anio_test"] != u.anio:
        raise AssertionError(f"{u.nombre}: estado_final.json no corresponde a la unidad.")
    import pandas as pd

    pred = pd.read_csv(tmp / "predicciones.csv")
    return {"n_test": int((pred.particion == "test").sum()), "mejor_epoca": estado["mejor_epoca"],
            "epocas": estado["epocas_corridas"], "fit_seconds": round(estado["fit_seconds"], 2)}


def todas(args) -> None:
    from lib.reanudacion import correr_etapa

    correr_etapa("07_lstm", __file__, args, MODELOS, MODELOS, trabajo)


if __name__ == "__main__":
    from lib.reanudacion import argumentos_comunes

    ap = argparse.ArgumentParser()
    ap.add_argument("--anio", type=int)
    ap.add_argument("--cultivar", choices=("sutil", "dulce"))
    ap.add_argument("--modelo", choices=MODELOS)
    ap.add_argument("--semilla", type=int)
    ap.add_argument("--destino")
    ap.add_argument("--todas", action="store_true")
    argumentos_comunes(ap)
    a = ap.parse_args()
    todas(a) if a.todas else una(a)
