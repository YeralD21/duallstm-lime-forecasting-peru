"""Corre unidades de la Fase 3 (G7). Reanudable: salta las unidades con completado.json.

Una unidad:   python correr.py --modelo GC3-Y1 --cultivar sutil --anio 2024 --semilla 0
Varias:       python correr.py --todas [--modelos ...] [--cultivares ...] [--anios ...] [--semillas ...] [--procesos 6]
Cada unidad LSTM corre en un proceso nuevo (configure_determinism antes de importar TensorFlow).
Salida: 12_revision_g7/resultados/unidades/<modelo>/<cultivar>/<anio>/[seed_XX]/{predicciones.csv, info.json, completado.json}
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "02_scripts"))
from lib.entorno import preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import argparse  # noqa: E402
import json  # noqa: E402
import subprocess  # noqa: E402
import time  # noqa: E402
from concurrent.futures import ThreadPoolExecutor, as_completed  # noqa: E402
from datetime import datetime, timezone  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
import g7lib as G  # noqa: E402

LOGS = G.G7 / "logs"


def una(modelo: str, cultivar: str, anio: int, semilla) -> None:
    fam = G.MODELOS[modelo][0]
    carpeta = G.destino(modelo, cultivar, anio, semilla)
    carpeta.mkdir(parents=True, exist_ok=True)
    t0 = time.perf_counter()
    if fam == "lstm":
        from v2_reentrenamiento.src.training.determinism import configure_determinism

        det = configure_determinism(semilla)
        from lib.integridad import Integridad

        Integridad().verificar()
        pred, info = G.correr_lstm(modelo, cultivar, anio, semilla, carpeta)
        info["determinismo"] = det.__dict__
    else:
        from lib.integridad import Integridad

        Integridad().verificar()
        if fam == "lineal":
            pred, info = G.correr_lineal(modelo, cultivar, anio)
        elif fam == "xgb":
            pred, info = G.correr_xgb(cultivar, anio, semilla)
        elif fam == "sarima":
            pred, info = G.correr_sarima(modelo, cultivar, anio)
        else:
            pred, info = G.correr_chronos(modelo, cultivar, anio)
    info.update({"modelo": modelo, "cultivar": cultivar, "anio_test": anio, "semilla": semilla,
                 "segundos_unidad": time.perf_counter() - t0, "utc": datetime.now(timezone.utc).isoformat()})
    pred.to_csv(carpeta / "predicciones.csv", index=False)
    (carpeta / "info.json").write_text(json.dumps(info, indent=2, default=str, ensure_ascii=False), encoding="utf-8")
    (carpeta / "completado.json").write_text(json.dumps({"ok": True, "n_test": int((pred.particion == "test").sum())}), encoding="utf-8")


def unidades(a):
    out = []
    for m in a.modelos:
        fam, con_sem, _, _ = G.MODELOS[m]
        anios = G.VENTANAS_CHRONOS if fam == "chronos" else G.VENTANAS_ENTRENADOS
        for c in a.cultivares:
            for y in anios:
                if a.anios and y not in a.anios:
                    continue
                for s in (a.semillas if con_sem else [None]):
                    out.append((m, c, y, s))
    return out


def lanzar(u) -> tuple:
    m, c, y, s = u
    if (G.destino(m, c, y, s) / "completado.json").exists():
        return u, "saltada", 0.0
    cmd = [sys.executable, __file__, "--modelo", m, "--cultivar", c, "--anio", str(y)] + ([] if s is None else ["--semilla", str(s)])
    t0 = time.perf_counter()
    r = subprocess.run(cmd, capture_output=True, text=True)
    nombre = f"{m}_{c}_{y}" + ("" if s is None else f"_s{s:02d}")
    if r.returncode != 0:
        (LOGS / "errores").mkdir(parents=True, exist_ok=True)
        (LOGS / "errores" / f"{nombre}.log").write_text(r.stdout + "\n" + r.stderr, encoding="utf-8")
        return u, f"ERROR {r.returncode}", time.perf_counter() - t0
    return u, "ok", time.perf_counter() - t0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--modelo")
    ap.add_argument("--cultivar")
    ap.add_argument("--anio", type=int)
    ap.add_argument("--semilla", type=int)
    ap.add_argument("--todas", action="store_true")
    ap.add_argument("--modelos", nargs="+", default=list(G.MODELOS))
    ap.add_argument("--cultivares", nargs="+", default=["sutil", "dulce"])
    ap.add_argument("--anios", nargs="+", type=int)
    ap.add_argument("--semillas", nargs="+", type=int, default=list(G.SEMILLAS))
    ap.add_argument("--procesos", type=int, default=6)
    ap.add_argument("--etiqueta", default="corrida")
    a = ap.parse_args()
    if not a.todas:
        una(a.modelo, a.cultivar, a.anio, a.semilla)
        sys.exit(0)
    LOGS.mkdir(parents=True, exist_ok=True)
    us = unidades(a)
    t0 = time.perf_counter()
    reg = []
    with ThreadPoolExecutor(max_workers=a.procesos) as ex:
        for f in as_completed([ex.submit(lanzar, u) for u in us]):
            u, estado, seg = f.result()
            reg.append({"modelo": u[0], "cultivar": u[1], "anio": u[2], "semilla": u[3], "estado": estado, "segundos": round(seg, 2)})
            print(f"[{len(reg)}/{len(us)}] {u} {estado} {seg:.1f}s", flush=True)
    total = time.perf_counter() - t0
    (LOGS / f"{a.etiqueta}.json").write_text(json.dumps({"segundos_total": total, "procesos": a.procesos, "unidades": reg}, indent=1), encoding="utf-8")
    n_err = sum(r["estado"].startswith("ERROR") for r in reg)
    print(f"TOTAL {total:.0f}s, errores {n_err}")
    sys.exit(1 if n_err else 0)
