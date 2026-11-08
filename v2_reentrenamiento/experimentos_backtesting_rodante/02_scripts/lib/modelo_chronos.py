"""Chronos-Bolt-tiny zero-shot desde la copia vendorizada de v4, sin red (HF_HUB_OFFLINE=1).

Protocolo de v4 (v4_benchmark_moderno/scripts/run_chronos_zero_shot.py:63-104): torch con 4 hilos,
float32, CPU, prediction_length=1, cuantil 0.5 como pronostico puntual, contexto = toda la historia hasta t-1.
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np

from lib.entorno import CONFIG, RAIZ_REPO

_HP = json.loads((CONFIG / "hiperparametros_congelados.json").read_text(encoding="utf-8"))["chronos"]


class ChronosZeroShot:
    def __init__(self) -> None:
        if os.environ.get("HF_HUB_OFFLINE") != "1":
            raise RuntimeError("HF_HUB_OFFLINE debe ser 1: no se permite descargar nada.")
        vendor = str(RAIZ_REPO / _HP["vendor"])
        if vendor not in sys.path:
            sys.path.insert(0, vendor)
        import torch
        from chronos import BaseChronosPipeline

        self.torch = torch
        torch.set_num_threads(int(_HP["torch_threads"]))
        self.pipeline = BaseChronosPipeline.from_pretrained(_HP["model_id"], device_map="cpu", torch_dtype=torch.float32)
        cuantiles = getattr(self.pipeline, "quantiles", None) or getattr(getattr(self.pipeline, "model", None), "quantiles", None)
        cuantiles = [float(q) for q in cuantiles]
        self.i_mediana = cuantiles.index(float(_HP["cuantil"]))
        self.modulo = sys.modules["chronos"].__file__

    def predecir(self, contexto: np.ndarray) -> float:
        x = self.torch.tensor(np.asarray(contexto, dtype=float), dtype=self.torch.float32)
        with self.torch.inference_mode():
            arr = self.pipeline.predict(x, prediction_length=1).detach().cpu().numpy()
        return float(arr[0, self.i_mediana, 0] if arr.ndim == 3 else arr[self.i_mediana, 0])
