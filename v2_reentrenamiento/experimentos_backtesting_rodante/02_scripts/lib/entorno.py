"""Preparacion del entorno. Debe importarse ANTES que numpy, TensorFlow o cualquier modulo de src.

Fija TF_ENABLE_ONEDNN_OPTS=0, TF_DETERMINISTIC_OPS=1, HF_HUB_OFFLINE=1 y PYTHONHASHSEED=42.
PYTHONHASHSEED solo surte efecto al arrancar el interprete: si no vale 42, el script se relanza
a si mismo en un subproceso con el entorno correcto y termina con su codigo de salida.
"""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

VARIABLES_ENTORNO = {
    "TF_ENABLE_ONEDNN_OPTS": "0",
    "TF_DETERMINISTIC_OPS": "1",
    "PYTHONHASHSEED": "42",
    "HF_HUB_OFFLINE": "1",
    "TRANSFORMERS_OFFLINE": "1",
    "TF_CPP_MIN_LOG_LEVEL": "2",
}

RAIZ_REPO = Path(__file__).resolve().parents[4]
V2 = RAIZ_REPO / "v2_reentrenamiento"
BR = V2 / "experimentos_backtesting_rodante"
CONFIG = BR / "01_configuracion"


def preparar_entorno() -> None:
    """Fija las variables y relanza el proceso si PYTHONHASHSEED no es el preregistrado."""
    if os.environ.get("PYTHONHASHSEED") != VARIABLES_ENTORNO["PYTHONHASHSEED"]:
        env = {**os.environ, **VARIABLES_ENTORNO}
        resultado = subprocess.run([sys.executable, *sys.argv], env=env)
        sys.exit(resultado.returncode)
    for clave, valor in VARIABLES_ENTORNO.items():
        os.environ[clave] = valor
    if str(RAIZ_REPO) not in sys.path:
        sys.path.insert(0, str(RAIZ_REPO))
    lib_padre = str(BR / "02_scripts")
    if lib_padre not in sys.path:
        sys.path.insert(0, lib_padre)


def semillas_globales(semilla: int = 42) -> None:
    """Semillas de random y numpy (no TensorFlow: cada corrida neural usa configure_determinism)."""
    import random

    import numpy as np

    random.seed(semilla)
    np.random.seed(semilla)
