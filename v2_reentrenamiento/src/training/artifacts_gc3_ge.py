"""Artifact path helpers for future GC3/GE multi-seed runs."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal


Cultivar = Literal["sutil", "dulce"]
ModelName = Literal["GC3", "GE"]


@dataclass(frozen=True)
class RunPaths:
    root: Path
    config: Path
    metadata: Path
    history: Path
    checkpoint: Path
    predictions: Path
    metrics: Path
    logs: Path


def build_run_paths(base_dir: Path, cultivar: Cultivar, model_name: ModelName, seed: int) -> RunPaths:
    if cultivar not in ("sutil", "dulce"):
        raise ValueError(f"Unsupported cultivar: {cultivar}")
    if model_name not in ("GC3", "GE"):
        raise ValueError(f"Unsupported model: {model_name}")
    if seed not in range(10):
        raise ValueError(f"Seed must be one of 0..9, got {seed}.")

    root = base_dir / cultivar / model_name / f"seed_{seed:02d}"
    return RunPaths(
        root=root,
        config=root / "config.json",
        metadata=root / "metadata.json",
        history=root / "history.csv",
        checkpoint=root / "checkpoint_best.keras",
        predictions=root / "predicciones.csv",
        metrics=root / "metricas.json",
        logs=root / "logs",
    )


def ensure_run_dir(paths: RunPaths) -> None:
    paths.root.mkdir(parents=True, exist_ok=False)
    paths.logs.mkdir(parents=True, exist_ok=False)
