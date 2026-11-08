"""Metadata schemas and helpers for future GC3/GE runs."""

from __future__ import annotations

import hashlib
import json
import platform
import subprocess
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class RunMetadata:
    cultivar: str
    model_name: str
    seed: int
    python_version: str | None
    tensorflow_version: str | None
    keras_version: str | None
    numpy_version: str | None
    os: str
    cpu: str | None
    gpu: str | None
    determinism_settings: dict[str, Any]
    one_dnn_setting: str | None
    timestamp_utc: str
    git_commit: str | None
    dataset_hash: str | None
    scaler_hash: str | None
    model_config_hash: str
    lookback: int
    batch_size: int
    learning_rate: float
    max_epochs: int
    best_epoch: int | None = None
    stopped_epoch: int | None = None


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def stable_config_hash(config: dict[str, Any]) -> str:
    payload = json.dumps(config, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def current_git_commit() -> str | None:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
    except Exception:
        return None
    return result.stdout.strip()


def base_metadata(
    *,
    cultivar: str,
    model_name: str,
    seed: int,
    model_config: dict[str, Any],
    determinism_settings: dict[str, Any],
    dataset_path: Path | None,
    scaler_path: Path | None,
    lookback: int,
    batch_size: int,
    learning_rate: float,
    max_epochs: int,
) -> RunMetadata:
    return RunMetadata(
        cultivar=cultivar,
        model_name=model_name,
        seed=seed,
        python_version=platform.python_version(),
        tensorflow_version=None,
        keras_version=None,
        numpy_version=None,
        os=platform.platform(),
        cpu=platform.processor() or None,
        gpu=None,
        determinism_settings=determinism_settings,
        one_dnn_setting=determinism_settings.get("tf_enable_onednn_opts"),
        timestamp_utc=datetime.now(timezone.utc).isoformat(),
        git_commit=current_git_commit(),
        dataset_hash=sha256_file(dataset_path) if dataset_path else None,
        scaler_hash=sha256_file(scaler_path) if scaler_path else None,
        model_config_hash=stable_config_hash(model_config),
        lookback=lookback,
        batch_size=batch_size,
        learning_rate=learning_rate,
        max_epochs=max_epochs,
    )


def write_metadata(metadata: RunMetadata, path: Path) -> None:
    path.write_text(
        json.dumps(asdict(metadata), indent=2, sort_keys=True),
        encoding="utf-8",
    )
