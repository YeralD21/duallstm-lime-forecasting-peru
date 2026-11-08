"""Ejecuta el experimento desde cero con un solo comando.

  venv\\Scripts\\python.exe v2_reentrenamiento\\experimentos_backtesting_rodante\\02_scripts\\run_all.py --fase B

Cada etapa corre en su propio proceso con PYTHONHASHSEED=42, TF_ENABLE_ONEDNN_OPTS=0, TF_DETERMINISTIC_OPS=1 y
HF_HUB_OFFLINE=1. Si una etapa falla, se detiene todo (no se cambia el protocolo).
Fase C: --fase C (requiere aprobacion). Fase D se agregara tras su aprobacion.
"""
import os
import subprocess
import sys
import time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
from lib.entorno import BR, VARIABLES_ENTORNO  # noqa: E402

ETAPAS = {
    "B": [
        ("00_verificar_entorno.py", []),
        ("01_construir_ventanas.py", []),
        ("tests/test_equivalencia_2025.py", []),
        ("tests/test_fuga.py", []),
        ("verificaciones_fase_b/b01_reproducir_chronos_v4.py", []),
        ("verificaciones_fase_b/b02_reproducir_elasticnet_v3.py", []),
        ("verificaciones_fase_b/b03_mini_corrida_2025.py", []),
        ("tests/test_p0.py", []),
        ("verificaciones_fase_b/b04_medir_tiempos.py", []),
        ("verificaciones_fase_b/b05_figura_prueba.py", []),
    ],
    # Fase C: cada etapa es reanudable (lib/reanudacion.py). Si se corta, volver a lanzar el mismo comando:
    # las unidades con completado.json valido se saltan. Log de progreso: 10_logs/ejecucion/faseC_<etapa>.log
    "C": [
        ("00_verificar_entorno.py", ["--fase", "C"]),  # manifest con HEAD y git status --porcelain
        ("01_construir_ventanas.py", []),
        ("03_modelos_sin_ajuste.py", []),
        ("04_sarima.py", []),
        ("05_lineales.py", []),
        ("06_xgb.py", []),
        ("07_lstm.py", ["--todas"]),
    ],
    # Fase D1: tablas y estadistica sobre las predicciones congeladas de la Fase C (sin figuras)
    "D1": [
        ("tests/test_equivalencia_metricas_2025.py", []),
        ("08_metricas.py", []),
        ("09_barrido_umbral.py", []),
        ("09b_reporte_fase_D1.py", []),
    ],
    # Fase D2: figuras MDPI solo desde CSV guardados (Fases C y D1)
    "D2": [
        ("10_figuras.py", []),
    ],
}


def main() -> None:
    fase = sys.argv[sys.argv.index("--fase") + 1] if "--fase" in sys.argv else "B"
    env = {**os.environ, **VARIABLES_ENTORNO}
    logs = BR / "10_logs" / "ejecucion"
    logs.mkdir(parents=True, exist_ok=True)
    for script, args in ETAPAS[fase]:
        t0 = time.perf_counter()
        nombre = script.replace("/", "__").removesuffix(".py")
        with open(logs / f"fase{fase}_{nombre}.stdout.log", "w", encoding="utf-8") as out, \
             open(logs / f"fase{fase}_{nombre}.stderr.log", "w", encoding="utf-8") as err:
            r = subprocess.run([sys.executable, str(AQUI / script), *args], env=env, stdout=out, stderr=err)
        print(f"[{'OK' if r.returncode == 0 else 'FALLO'}] {script} ({time.perf_counter() - t0:.1f} s)", flush=True)
        if r.returncode != 0:
            raise SystemExit(f"Se detiene: {script} fallo. Ver {logs}.")


if __name__ == "__main__":
    main()
