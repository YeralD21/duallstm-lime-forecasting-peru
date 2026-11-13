"""Single driver: reproduce the paper's tables and figure data and compare them with the published files.

    python reproduce.py              # from the frozen predictions (minutes): integrity, leakage tests, all metrics,
                                     # figures, diagnostic experiments (G7) evaluation, comparison
    python reproduce.py --retrain    # from the frozen input tables (about 2 h on a 16-thread CPU): refits every
                                     # model of the rolling-origin backtesting and of the diagnostic experiments,
                                     # then recomputes everything and compares
    python reproduce.py --no-figures # skip the figure scripts

Comparison: every CSV listed in expected_outputs_sha256.json (SHA-256 with CRLF -> LF, the method of
01_configuracion/hashes_congelados.json) is compared with the regenerated file. When the hash differs, the two
CSV are compared numerically (same shape and columns; maximum absolute and relative difference per file).
Wall-clock run-time columns (TIMING_COLUMNS) are excluded from that comparison and reported separately.
The 15 tables of 09_reportes/revision_g7/fase1/ are not in expected_outputs_sha256.json: g7_fase1.py regenerates
them in a temporary folder (the published files are never overwritten) and compares them cell by cell with the
published ones; its result goes to the "g7_fase1_tables" entry of the report.
The second-round review analyses (13_revision_r2/, post-protocol) run after the existing steps; their outputs are
not part of expected_outputs_sha256.json.
The report is written to reproduction_report.json.

--retrain moves the shipped 04_modelos/, 05_predicciones/ and 12_revision_g7/resultados/unidades/ to
_reference_before_retrain/ and refits from scratch. Run it on a fresh clone.
Chronos weights must be in the Hugging Face cache first: python download_chronos_weights.py [--all].
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BR = ROOT / "v2_reentrenamiento" / "experimentos_backtesting_rodante"
S = BR / "02_scripts"
G7 = BR / "12_revision_g7"
FASE1 = BR / "09_reportes" / "revision_g7" / "fase1"
R2 = BR / "13_revision_r2"
EXPECTED = ROOT / "expected_outputs_sha256.json"
REPORT = ROOT / "reproduction_report.json"
ENV = {**os.environ, "PYTHONHASHSEED": "42", "TF_ENABLE_ONEDNN_OPTS": "0", "TF_DETERMINISTIC_OPS": "1",
       "HF_HUB_OFFLINE": "1", "TRANSFORMERS_OFFLINE": "1", "TF_CPP_MIN_LOG_LEVEL": "2", "PYTHONIOENCODING": "utf-8"}
# wall-clock run times stored in some tables (12_revision_g7/resultados/T10_lstm_epocas_parametros.csv)
TIMING_COLUMNS = {"fit_seconds", "segundos_unidad", "segundos", "seconds"}
TEXT = {".py", ".csv", ".json", ".md", ".txt", ".mjs", ".cfg", ".toml", ".yaml", ".yml", ".ini"}


def sha(p: Path) -> str:
    b = p.read_bytes()
    return hashlib.sha256(b.replace(b"\r\n", b"\n") if p.suffix.lower() in TEXT else b).hexdigest()


def run(name: str, args: list[str], log: list) -> None:
    t0 = time.perf_counter()
    r = subprocess.run([sys.executable, *args], env=ENV, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
    dt = time.perf_counter() - t0
    print(f"[{'OK' if r.returncode == 0 else 'FAILED'}] {name} ({dt:.0f} s)", flush=True)
    log.append({"step": name, "returncode": r.returncode, "seconds": round(dt, 1)})
    if r.returncode != 0:
        print(r.stdout[-4000:], r.stderr[-4000:], sep="\n")
        REPORT.write_text(json.dumps({"steps": log, "stopped_at": name}, indent=1), encoding="utf-8")
        raise SystemExit(f"Stopped: {name} failed.")


def compare_csv(new: Path, ref: Path) -> dict:
    import numpy as np
    import pandas as pd

    a, b = pd.read_csv(new, low_memory=False), pd.read_csv(ref, low_memory=False)
    if list(a.columns) != list(b.columns) or a.shape != b.shape:
        return {"status": "DIFFERENT_SHAPE", "new": list(a.shape), "reference": list(b.shape)}
    out = {"status": "NUMERIC_DIFF", "max_abs": 0.0, "max_rel": 0.0, "non_numeric_cells_different": 0}
    for c in a.columns:
        x, y = pd.to_numeric(a[c], errors="coerce"), pd.to_numeric(b[c], errors="coerce")
        num = x.notna() & y.notna()
        if num.any():
            d = (x[num] - y[num]).abs()
            out["max_abs"] = max(out["max_abs"], float(d.max()))
            rel = d / y[num].abs().replace(0, np.nan)
            if rel.notna().any():
                out["max_rel"] = max(out["max_rel"], float(rel.max()))
        rest = ~num
        out["non_numeric_cells_different"] += int((a[c][rest].fillna("").astype(str) != b[c][rest].fillna("").astype(str)).sum())
    if out["max_abs"] == 0 and out["non_numeric_cells_different"] == 0:
        out["status"] = "EQUAL_VALUES_DIFFERENT_BYTES"
    return out


def compare_with_timing(new: Path, ref: Path) -> dict:
    """Compare excluding wall-clock columns (they change on every run); report them separately."""
    import pandas as pd

    a, b = pd.read_csv(new, low_memory=False), pd.read_csv(ref, low_memory=False)
    timing = [c for c in a.columns if c in TIMING_COLUMNS]
    if not timing or list(a.columns) != list(b.columns) or a.shape != b.shape:
        return compare_csv(new, ref)
    tmp = Path(tempfile.mkdtemp(prefix="duallstm_cmp_"))
    a.drop(columns=timing).to_csv(tmp / "a.csv", index=False)
    b.drop(columns=timing).to_csv(tmp / "b.csv", index=False)
    r = compare_csv(tmp / "a.csv", tmp / "b.csv")
    shutil.rmtree(tmp, ignore_errors=True)
    if r["status"] == "EQUAL_VALUES_DIFFERENT_BYTES":
        r = {"status": "IDENTICAL_EXCEPT_WALL_CLOCK_TIMES"}
    r["wall_clock_columns"] = timing
    r["wall_clock_max_abs_seconds"] = float(max((a[c] - b[c]).abs().max() for c in timing))
    return r


def main() -> None:
    retrain = "--retrain" in sys.argv
    figures = "--no-figures" not in sys.argv
    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))["sha256"]
    log: list = []
    for d in ("10_logs/ejecucion", "10_logs/verificaciones"):
        (BR / d).mkdir(parents=True, exist_ok=True)

    # reference copy of every compared file, before anything is overwritten
    ref_root = ROOT / "_reference_before_retrain" if retrain else Path(tempfile.mkdtemp(prefix="duallstm_ref_"))
    if retrain:
        if ref_root.exists():
            raise SystemExit(f"{ref_root} exists: use a fresh clone for --retrain.")
        for rel in ("04_modelos", "05_predicciones", "12_revision_g7/resultados/unidades"):
            dst = ref_root / BR.relative_to(ROOT) / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(BR / rel), str(dst))
    for rel in expected:
        src, dst = ROOT / rel, ref_root / rel
        if src.exists() and not dst.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
    t_start = time.time()

    run("integrity: SHA-256 of official code, frozen data and Chronos (hashes_congelados.json)",
        ["-c", f"import sys; sys.path.insert(0, r'{S}'); from lib.integridad import Integridad; print(Integridad().verificar())"], log)
    if retrain:
        run("phase C: rolling-origin backtesting, all models refit (run_all.py --fase C)", [str(S / "run_all.py"), "--fase", "C"], log)
        run("diagnostic experiments (G7): all units refit", [str(G7 / "scripts" / "correr.py"), "--todas", "--procesos", "8", "--etiqueta", "reproduce"], log)
    run("leakage test, backtesting (test_fuga.py)", [str(S / "tests" / "test_fuga.py")], log)
    run("leakage test, diagnostic experiments (test_fuga_g7.py)", [str(G7 / "scripts" / "test_fuga_g7.py")], log)
    run("phase D1: metrics, bootstrap, Diebold-Mariano, threshold sweep (run_all.py --fase D1)", [str(S / "run_all.py"), "--fase", "D1"], log)
    run("diagnostic experiments (G7): evaluation T1-T10 (evaluar.py)", [str(G7 / "scripts" / "evaluar.py")], log)
    fase1_tmp = Path(tempfile.mkdtemp(prefix="duallstm_fase1_"))
    run("first-round diagnostic tables (09_reportes/revision_g7/fase1, g7_fase1.py): regenerate and compare cell by cell",
        [str(FASE1 / "g7_fase1.py"), "--json", str(fase1_tmp / "fase1.json")], log)
    fase1 = json.loads((fase1_tmp / "fase1.json").read_text(encoding="utf-8"))
    shutil.rmtree(fase1_tmp, ignore_errors=True)
    if figures:
        run("phase D2: figures (run_all.py --fase D2)", [str(S / "run_all.py"), "--fase", "D2"], log)
        for f in ("11_figuras_d3.py", "13_figura_workflow.py", "14_fig20_reducida_2025.py"):
            run(f"figures: {f}", [str(S / f)], log)
    # second-round review (R2): post-protocol robustness and diagnostics; writes only to 13_revision_r2/resultados/
    for f, name in (("t1_ets_theta.py", "ETS and Theta, rolling origin 2021-2025"),
                    ("t1_t2_evaluar.py", "ETS/Theta metrics, 12-model ranking and 2025-only ranking"),
                    ("t3_sarima.py", "SARIMA constant, no-constant sensitivity and SARIMA-sel fallback rule"),
                    ("t4_verificaciones.py", "predictor lags, fig20 content and Seasonal Naive check")):
        run(f"review R2 (13_revision_r2): {name} ({f})", [str(R2 / "scripts" / f)], log)

    results = {}
    for rel, h in expected.items():
        p = ROOT / rel
        if not p.exists():
            results[rel] = {"status": "MISSING"}
        elif sha(p) == h:
            results[rel] = {"status": "IDENTICAL"}
        elif (ref_root / rel).exists():
            results[rel] = compare_with_timing(p, ref_root / rel)
        else:
            results[rel] = {"status": "HASH_DIFFERENT_NO_REFERENCE"}
        if p.exists():
            results[rel]["regenerated"] = p.stat().st_mtime >= t_start
    regenerated = sum(r.get("regenerated", False) for r in results.values())
    count: dict[str, int] = {}
    for r in results.values():
        count[r["status"]] = count.get(r["status"], 0) + 1
    worst = max((r.get("max_abs", 0.0) for r in results.values()), default=0.0)
    REPORT.write_text(json.dumps({"mode": "retrain" if retrain else "frozen_predictions", "steps": log, "summary": count,
                                  "regenerated_by_this_run": regenerated, "max_abs_difference": worst, "files": results,
                                  "g7_fase1_tables": fase1}, indent=1), encoding="utf-8")
    print(f"Compared {len(results)} files ({regenerated} regenerated by this run): {count}; "
          f"max |difference| = {worst:g}. Report: {REPORT.name}")
    print(f"09_reportes/revision_g7/fase1: {fase1['identical_tables']} of {fase1['tables']} tables identical cell by cell.")
    if not retrain:
        shutil.rmtree(ref_root, ignore_errors=True)
    ok = count.get("IDENTICAL", 0) + count.get("IDENTICAL_EXCEPT_WALL_CLOCK_TIMES", 0)
    raise SystemExit(0 if ok == len(results) and fase1["identical_tables"] == fase1["tables"] else 1)


if __name__ == "__main__":
    main()
