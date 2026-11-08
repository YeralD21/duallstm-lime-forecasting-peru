"""Official GC3/GE training runner and dry-run pre-flight checks.

The default public entry point for this module is `dry_run_preflight`, which
does not call `model.fit`. Future official training must call
`run_official_training` explicitly.
"""

from __future__ import annotations

import csv
import json
import platform
import sys
import time
from dataclasses import asdict, replace
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Literal

import numpy as np
import pandas as pd

from v2_reentrenamiento.src.training.artifacts_gc3_ge import build_run_paths, ensure_run_dir
from v2_reentrenamiento.src.training.config_gc3_ge import (
    OFFICIAL_SEEDS,
    OFFICIAL_TRAINING_CONFIG,
    TrainingConfig,
    validate_official_seeds,
)
from v2_reentrenamiento.src.training.history_gc3_ge import history_to_frame, save_history_frame
from v2_reentrenamiento.src.training.metadata_gc3_ge import (
    base_metadata,
    current_git_commit,
    sha256_file,
    write_metadata,
)


Cultivar = Literal["sutil", "dulce"]
ModelName = Literal["GC3", "GE"]

YEAR_COL = "a\u00f1o"
MONTH_COL = "mes"
OFFICIAL_CULTIVARS: tuple[Cultivar, ...] = ("sutil", "dulce")
OFFICIAL_MODELS: tuple[ModelName, ...] = ("GC3", "GE")
EXPECTED_PARAMS = {"GC3": 6273, "GE": 6657}
EXPECTED_BRANCH_B = {"GC3": 33, "GE": 39}
EXPECTED_TOTAL_FEATURES = {"GC3": 37, "GE": 43}
DEFAULT_RESULTS_DIR = Path("v2_reentrenamiento/resultados_v2_final/official_gc3_ge")
SCALER_DIR = Path("v2_reentrenamiento/resultados_v2_final/scalers")
DATA_DIR = Path("v2_reentrenamiento/data/processed")


class LearningRateLogger:
    """Collect learning rates after each epoch for history.csv."""

    def __init__(self) -> None:
        self.values: list[float] = []

    def as_callback(self):
        import tensorflow as tf

        outer = self

        class _LearningRateLogger(tf.keras.callbacks.Callback):
            def on_epoch_end(self, epoch, logs=None):  # noqa: ARG002
                lr = float(tf.keras.backend.get_value(self.model.optimizer.learning_rate))
                outer.values.append(lr)

        return _LearningRateLogger()


def dataset_path(repo_root: Path, cultivar: Cultivar) -> Path:
    return repo_root / DATA_DIR / f"master_dataset_{cultivar}_v2_escalado.csv"


def scaler_path(repo_root: Path, cultivar: Cultivar) -> Path:
    return repo_root / SCALER_DIR / f"scaler_{cultivar}_v2c.joblib"


def _params_path(repo_root: Path, cultivar: Cultivar) -> Path:
    return repo_root / SCALER_DIR / f"scaler_{cultivar}_v2c_parametros.csv"


def read_dataset_calendar(path: Path) -> pd.DataFrame:
    """Read only year/month columns for split and date pre-flight."""

    rows: list[dict[str, int]] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if YEAR_COL not in (reader.fieldnames or []) or MONTH_COL not in (reader.fieldnames or []):
            raise ValueError(f"Dataset missing {YEAR_COL}/{MONTH_COL}: {path}")
        for row in reader:
            rows.append({YEAR_COL: int(row[YEAR_COL]), MONTH_COL: int(row[MONTH_COL])})
    frame = pd.DataFrame(rows)
    frame["fecha"] = pd.to_datetime(
        {
            "year": frame[YEAR_COL].astype(int),
            "month": frame[MONTH_COL].astype(int),
            "day": 1,
        }
    )
    return frame.sort_values("fecha").reset_index(drop=True)


def load_training_validation_frame(path: Path) -> pd.DataFrame:
    """Load only rows allowed for fit: TRAIN effective + VALIDATION 2024."""

    rows: list[dict[str, str]] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            year = int(row[YEAR_COL])
            if year <= 2024:
                rows.append(row)

    frame = pd.DataFrame(rows)
    for column in frame.columns:
        try:
            frame[column] = pd.to_numeric(frame[column])
        except (TypeError, ValueError):
            pass
    frame["fecha"] = pd.to_datetime(
        {
            "year": frame[YEAR_COL].astype(int),
            "month": frame[MONTH_COL].astype(int),
            "day": 1,
        }
    )
    frame = frame.sort_values("fecha").reset_index(drop=True)
    if (frame["fecha"].dt.year >= 2025).any():
        raise ValueError("TEST rows reached the fit dataframe.")
    return frame


def build_train_validation_sequences(
    frame: pd.DataFrame,
    spec: Any,
    *,
    lookback: int = OFFICIAL_TRAINING_CONFIG.lookback,
) -> dict[str, Any]:
    from v2_reentrenamiento.src.models.features_gc3_ge import validate_columns_available

    validate_columns_available(spec, set(frame.columns))
    if lookback != 6:
        raise ValueError(f"Official lookback must be 6, got {lookback}.")
    if frame["fecha"].min() != pd.Timestamp("2016-07-01"):
        raise ValueError(f"Expected first feature row 2016-07, got {frame['fecha'].min()}.")
    if frame["fecha"].max() != pd.Timestamp("2024-12-01"):
        raise ValueError(f"Expected last validation feature row 2024-12, got {frame['fecha'].max()}.")
    if not frame["fecha"].is_monotonic_increasing:
        raise ValueError("Feature rows must be sorted.")
    if frame["fecha"].duplicated().any():
        raise ValueError("Duplicate monthly rows are not allowed.")

    values_a = frame.loc[:, spec.rama_a].to_numpy(dtype=float)
    values_b = frame.loc[:, spec.rama_b].to_numpy(dtype=float)
    values_y = frame.loc[:, spec.target].to_numpy(dtype=float)
    dates = frame["fecha"].reset_index(drop=True)

    x_a: list[np.ndarray] = []
    x_b: list[np.ndarray] = []
    y: list[float] = []
    target_dates: list[pd.Timestamp] = []
    context_end_dates: list[pd.Timestamp] = []
    for target_idx in range(lookback, len(frame)):
        start = target_idx - lookback
        stop = target_idx
        context_dates = dates.iloc[start:stop]
        target_date = dates.iloc[target_idx]
        if not (context_dates < target_date).all():
            raise ValueError("Future leakage detected in context dates.")
        x_a.append(values_a[start:stop])
        x_b.append(values_b[start:stop])
        y.append(float(values_y[target_idx]))
        target_dates.append(target_date)
        context_end_dates.append(dates.iloc[stop - 1])

    x_a_array = np.stack(x_a)
    x_b_array = np.stack(x_b)
    y_array = np.asarray(y, dtype=float)
    target_series = pd.Series(target_dates, name="fecha")
    context_end_series = pd.Series(context_end_dates, name="context_end")

    train_mask = (target_series.dt.year <= 2023).to_numpy()
    val_mask = (target_series.dt.year == 2024).to_numpy()
    if target_series.dt.year.gt(2024).any():
        raise ValueError("TEST target reached training/validation sequences.")

    result = {
        "train": {
            "X_a": x_a_array[train_mask],
            "X_b": x_b_array[train_mask],
            "y": y_array[train_mask],
            "target_dates": target_series[train_mask].reset_index(drop=True),
            "context_end_dates": context_end_series[train_mask].reset_index(drop=True),
        },
        "validation": {
            "X_a": x_a_array[val_mask],
            "X_b": x_b_array[val_mask],
            "y": y_array[val_mask],
            "target_dates": target_series[val_mask].reset_index(drop=True),
            "context_end_dates": context_end_series[val_mask].reset_index(drop=True),
        },
        "feature_rows_loaded_for_fit": int(len(frame)),
        "train_feature_rows": int((frame["fecha"].dt.year <= 2023).sum()),
        "test_loaded_for_fit": False,
    }
    _validate_sequence_shapes(result, spec.model_name)
    return result


def _validate_sequence_shapes(sequences: dict[str, Any], model_name: ModelName) -> None:
    expected_b = EXPECTED_BRANCH_B[model_name]
    expected = {
        "Xa_train": (84, 6, 4),
        "Xb_train": (84, 6, expected_b),
        "y_train": (84,),
        "Xa_val": (12, 6, 4),
        "Xb_val": (12, 6, expected_b),
        "y_val": (12,),
    }
    actual = {
        "Xa_train": tuple(sequences["train"]["X_a"].shape),
        "Xb_train": tuple(sequences["train"]["X_b"].shape),
        "y_train": tuple(sequences["train"]["y"].shape),
        "Xa_val": tuple(sequences["validation"]["X_a"].shape),
        "Xb_val": tuple(sequences["validation"]["X_b"].shape),
        "y_val": tuple(sequences["validation"]["y"].shape),
    }
    if actual != expected:
        raise ValueError(f"{model_name} shape mismatch: expected {expected}, got {actual}")
    if sequences["train_feature_rows"] != 90:
        raise ValueError(f"Expected 90 TRAIN feature rows, got {sequences['train_feature_rows']}.")
    if sequences["train"]["target_dates"].iloc[0] != pd.Timestamp("2017-01-01"):
        raise ValueError("First TRAIN target must be 2017-01.")
    if sequences["train"]["target_dates"].iloc[-1] != pd.Timestamp("2023-12-01"):
        raise ValueError("Last TRAIN target must be 2023-12.")
    if sequences["validation"]["target_dates"].iloc[0] != pd.Timestamp("2024-01-01"):
        raise ValueError("First VAL target must be 2024-01.")
    if sequences["validation"]["target_dates"].iloc[-1] != pd.Timestamp("2024-12-01"):
        raise ValueError("Last VAL target must be 2024-12.")


def _validate_calendar(calendar: pd.DataFrame) -> dict[str, Any]:
    if calendar["fecha"].min() != pd.Timestamp("2016-07-01"):
        raise ValueError(f"Dataset must start at 2016-07, got {calendar['fecha'].min()}.")
    if calendar["fecha"].max() != pd.Timestamp("2025-12-01"):
        raise ValueError(f"Dataset must end at 2025-12, got {calendar['fecha'].max()}.")
    if (calendar["fecha"].dt.year == 2026).any():
        raise ValueError("2026 rows are not allowed.")
    if calendar["fecha"].duplicated().any():
        raise ValueError("Duplicate monthly rows are not allowed.")
    counts = {
        "train_effective_rows": int((calendar["fecha"].dt.year <= 2023).sum()),
        "validation_rows": int((calendar["fecha"].dt.year == 2024).sum()),
        "test_rows": int((calendar["fecha"].dt.year == 2025).sum()),
        "total_rows": int(len(calendar)),
    }
    expected = {
        "train_effective_rows": 90,
        "validation_rows": 12,
        "test_rows": 12,
        "total_rows": 114,
    }
    if counts != expected:
        raise ValueError(f"Unexpected split row counts: expected {expected}, got {counts}")
    return counts


def _validate_no_contemporary_exogenous(spec: FeatureSpec) -> None:
    from v2_reentrenamiento.src.models.features_gc3_ge import (
        FORBIDDEN_CONTEMPORARY_EXOGENOUS,
        TEMPORAL_FEATURES,
    )

    allowed_unlagged = set(TEMPORAL_FEATURES) | set(spec.rama_a)
    violations = [
        feature
        for feature in spec.all_inputs
        if feature not in allowed_unlagged
        and "_lag" not in feature
        and feature in FORBIDDEN_CONTEMPORARY_EXOGENOUS
    ]
    if violations:
        raise ValueError(f"Contemporary exogenous features are not allowed: {violations}")


def _validate_scaler(repo_root: Path, cultivar: Cultivar) -> dict[str, Any]:
    import joblib
    from sklearn.preprocessing import StandardScaler

    path = scaler_path(repo_root, cultivar)
    if path.name != f"scaler_{cultivar}_v2c.joblib":
        raise ValueError(f"Scaler must be v2c, got {path.name}.")
    scaler = joblib.load(path)
    if not isinstance(scaler, StandardScaler):
        raise TypeError(f"Scaler must be StandardScaler, got {type(scaler)!r}.")
    n_features = int(getattr(scaler, "n_features_in_", -1))
    n_samples = int(getattr(scaler, "n_samples_seen_", -1))
    if n_features != 44 or n_samples != 90:
        raise ValueError(f"Scaler expected n_features=44 and n_samples=90, got {n_features}/{n_samples}.")
    params = _params_path(repo_root, cultivar)
    if not params.exists():
        raise FileNotFoundError(f"Missing scaler params CSV: {params}")
    return {
        "path": str(path),
        "params_path": str(params),
        "class": scaler.__class__.__name__,
        "n_features_in": n_features,
        "n_samples_seen": n_samples,
        "hash": sha256_file(path),
        "params_hash": sha256_file(params),
    }


def _official_run_manifest(base_dir: Path) -> list[dict[str, Any]]:
    manifest: list[dict[str, Any]] = []
    for cultivar in OFFICIAL_CULTIVARS:
        for model_name in OFFICIAL_MODELS:
            for seed in OFFICIAL_SEEDS:
                paths = build_run_paths(base_dir, cultivar, model_name, seed)
                existing_files = [str(path) for path in paths.root.rglob("*") if path.is_file()] if paths.root.exists() else []
                manifest.append(
                    {
                        "cultivar": cultivar,
                        "model_name": model_name,
                        "seed": seed,
                        "root": str(paths.root),
                        "exists": paths.root.exists(),
                        "existing_file_count": len(existing_files),
                    }
                )
    return manifest


def _validate_destination(base_dir: Path) -> dict[str, Any]:
    if "technical_pilot" in base_dir.as_posix():
        raise ValueError(f"Official destination must not be technical_pilot*: {base_dir}")
    manifest = _official_run_manifest(base_dir)
    occupied = [item for item in manifest if item["existing_file_count"] > 0]
    if occupied:
        raise FileExistsError(f"Official run directories already contain files: {occupied}")
    return {
        "base_dir": str(base_dir),
        "differentiated_from_technical_pilot": True,
        "silent_overwrite_prevented": True,
        "planned_runs": len(manifest),
        "existing_official_run_files": 0,
        "manifest": manifest,
    }


def _model_config_dict(spec: FeatureSpec) -> dict[str, Any]:
    return {
        "model_name": spec.model_name,
        "lookback": OFFICIAL_TRAINING_CONFIG.lookback,
        "rama_a_features": spec.rama_a,
        "rama_b_features": spec.rama_b,
        "n_features_a": len(spec.rama_a),
        "n_features_b": len(spec.rama_b),
        "total_features": len(spec.all_inputs),
        "architecture": "DualLSTM16_BahdanauAttention16_Dense16_Dropout020_Dense8_Dense1",
        "l2": 0,
        "optimizer": "Adam",
        "learning_rate": OFFICIAL_TRAINING_CONFIG.learning_rate,
        "loss": OFFICIAL_TRAINING_CONFIG.loss,
        "metric": OFFICIAL_TRAINING_CONFIG.metric,
        "batch_size": OFFICIAL_TRAINING_CONFIG.batch_size,
        "max_epochs": OFFICIAL_TRAINING_CONFIG.max_epochs,
        "shuffle": OFFICIAL_TRAINING_CONFIG.shuffle,
    }


def _callback_summary(callbacks: list[Any]) -> list[dict[str, Any]]:
    return [
        {
            "class": callback.__class__.__name__,
            "monitor": getattr(callback, "monitor", None),
            "patience": getattr(callback, "patience", None),
            "restore_best_weights": getattr(callback, "restore_best_weights", None),
            "factor": getattr(callback, "factor", None),
            "min_lr": getattr(callback, "min_lr", None),
            "filepath": str(getattr(callback, "filepath", "")),
            "save_best_only": getattr(callback, "save_best_only", None),
        }
        for callback in callbacks
    ]


def dry_run_preflight(repo_root: Path, *, results_dir: Path | None = None) -> dict[str, Any]:
    """Run all official checks without fitting a model."""

    start = time.perf_counter()
    validate_official_seeds()
    base_dir = repo_root / (results_dir or DEFAULT_RESULTS_DIR)
    destination = _validate_destination(base_dir)

    from v2_reentrenamiento.src.training.determinism import configure_determinism

    determinism = configure_determinism(0)

    import tensorflow as tf
    from tensorflow import keras
    import joblib
    import sklearn

    from v2_reentrenamiento.src.models.dual_lstm_attention import build_gc3_ge_model
    from v2_reentrenamiento.src.models.features_gc3_ge import build_feature_spec
    from v2_reentrenamiento.src.training.callbacks_gc3_ge import build_callbacks

    callback_probe_dir = repo_root / "v2_reentrenamiento/auditorias/.tmp_callbacks_probe"
    callbacks = build_callbacks(callback_probe_dir)
    callback_info = _callback_summary(callbacks)
    for path in sorted(callback_probe_dir.rglob("*"), reverse=True):
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            path.rmdir()
    if callback_probe_dir.exists():
        callback_probe_dir.rmdir()
    if callback_info[0]["class"] != "EarlyStopping" or callback_info[0]["monitor"] != "val_loss":
        raise ValueError("EarlyStopping callback is not official.")
    if callback_info[1]["class"] != "ReduceLROnPlateau" or callback_info[1]["monitor"] != "val_loss":
        raise ValueError("ReduceLROnPlateau callback is not official.")
    if callback_info[2]["class"] != "ModelCheckpoint" or callback_info[2]["save_best_only"] is not True:
        raise ValueError("ModelCheckpoint callback is not official.")

    model_checks: dict[str, Any] = {}
    data_checks: dict[str, Any] = {}
    for model_name in OFFICIAL_MODELS:
        model = build_gc3_ge_model(model_name, 4, EXPECTED_BRANCH_B[model_name])
        params = int(model.count_params())
        if params != EXPECTED_PARAMS[model_name]:
            raise ValueError(f"{model_name} params mismatch: {params}")
        lr = float(tf.keras.backend.get_value(model.optimizer.learning_rate))
        if not np.isclose(lr, OFFICIAL_TRAINING_CONFIG.learning_rate):
            raise ValueError(f"{model_name} learning rate mismatch: {lr}")
        model_checks[model_name] = {
            "params": params,
            "loss": model.loss,
            "optimizer": model.optimizer.__class__.__name__,
            "learning_rate": lr,
            "input_shapes": [str(shape) for shape in model.input_shape],
        }

    for cultivar in OFFICIAL_CULTIVARS:
        cultivar_dataset = dataset_path(repo_root, cultivar)
        if cultivar_dataset.name != f"master_dataset_{cultivar}_v2_escalado.csv":
            raise ValueError(f"Dataset must be *_v2_escalado.csv, got {cultivar_dataset.name}")
        calendar = read_dataset_calendar(cultivar_dataset)
        split_counts = _validate_calendar(calendar)
        fit_frame = load_training_validation_frame(cultivar_dataset)
        scaler = _validate_scaler(repo_root, cultivar)

        data_checks[cultivar] = {
            "dataset_path": str(cultivar_dataset),
            "dataset_hash": sha256_file(cultivar_dataset),
            "split_counts": split_counts,
            "scaler": scaler,
            "models": {},
            "test_rows_loaded_for_fit": False,
            "test_arrays_materialized": False,
        }
        for model_name in OFFICIAL_MODELS:
            spec = build_feature_spec(cultivar, model_name)
            _validate_no_contemporary_exogenous(spec)
            sequences = build_train_validation_sequences(fit_frame, spec)
            train_dates = sequences["train"]["target_dates"]
            val_dates = sequences["validation"]["target_dates"]
            context_end = sequences["train"]["context_end_dates"].iloc[0]
            first_target = train_dates.iloc[0]
            if context_end != pd.Timestamp("2016-12-01") or first_target != pd.Timestamp("2017-01-01"):
                raise ValueError("Alignment t -> t+1 failed for first TRAIN sequence.")
            data_checks[cultivar]["models"][model_name] = {
                "rama_a_features": spec.rama_a,
                "rama_b_features": spec.rama_b,
                "n_features_a": len(spec.rama_a),
                "n_features_b": len(spec.rama_b),
                "total_predictive_inputs": len(spec.all_inputs),
                "contemporary_exogenous_absent": True,
                "fit_feature_rows_loaded": sequences["feature_rows_loaded_for_fit"],
                "train_feature_rows": sequences["train_feature_rows"],
                "train_sequences": int(len(sequences["train"]["y"])),
                "validation_targets": int(len(sequences["validation"]["y"])),
                "shapes": {
                    "Xa_train": list(sequences["train"]["X_a"].shape),
                    "Xb_train": list(sequences["train"]["X_b"].shape),
                    "y_train": list(sequences["train"]["y"].shape),
                    "Xa_val": list(sequences["validation"]["X_a"].shape),
                    "Xb_val": list(sequences["validation"]["X_b"].shape),
                    "y_val": list(sequences["validation"]["y"].shape),
                },
                "first_train_context_end": str(context_end.date()),
                "first_train_target": str(first_target.date()),
                "first_val_target": str(val_dates.iloc[0].date()),
                "last_val_target": str(val_dates.iloc[-1].date()),
            }

    return {
        "status": "READY",
        "decision": "B) reutilizar componentes existentes y crear un orquestador oficial",
        "model_fit_executed": False,
        "test_used_for_training": False,
        "test_loaded_for_fit": False,
        "official_runs_expected": 40,
        "cultivars": OFFICIAL_CULTIVARS,
        "models": OFFICIAL_MODELS,
        "seeds": OFFICIAL_SEEDS,
        "training_config": asdict(OFFICIAL_TRAINING_CONFIG),
        "destination": destination,
        "callbacks": callback_info,
        "model_checks": model_checks,
        "data_checks": data_checks,
        "hashes_registered": True,
        "git_commit": current_git_commit(),
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "tensorflow": tf.__version__,
            "keras": keras.__version__,
            "numpy": np.__version__,
            "pandas": pd.__version__,
            "sklearn": sklearn.__version__,
            "joblib": joblib.__version__,
            "cpu": platform.processor() or None,
            "gpu": [str(device) for device in tf.config.list_physical_devices("GPU")],
        },
        "determinism": asdict(determinism),
        "dry_run_seconds": time.perf_counter() - start,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    }


def write_json(payload: dict[str, Any], path: Path) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def run_official_training(
    repo_root: Path,
    cultivar: Cultivar,
    model_name: ModelName,
    seed: int,
    *,
    results_dir: Path | None = None,
    config: TrainingConfig = OFFICIAL_TRAINING_CONFIG,
) -> dict[str, Any]:
    """Execute one future official run.

    This function intentionally has no dry-run behavior. Callers must choose it
    explicitly, and existing run directories with files are rejected.
    """

    if cultivar not in OFFICIAL_CULTIVARS:
        raise ValueError(f"Unsupported cultivar: {cultivar}")
    if model_name not in OFFICIAL_MODELS:
        raise ValueError(f"Unsupported model: {model_name}")
    if seed not in OFFICIAL_SEEDS:
        raise ValueError(f"Seed must be one of 0..9, got {seed}")
    if config != OFFICIAL_TRAINING_CONFIG:
        raise ValueError("Official training config cannot be changed.")

    from v2_reentrenamiento.src.training.determinism import configure_determinism

    determinism = configure_determinism(seed)

    import tensorflow as tf
    from tensorflow import keras

    from v2_reentrenamiento.src.models.dual_lstm_attention import build_gc3_ge_model
    from v2_reentrenamiento.src.models.features_gc3_ge import build_feature_spec
    from v2_reentrenamiento.src.training.callbacks_gc3_ge import build_callbacks

    base_dir = repo_root / (results_dir or DEFAULT_RESULTS_DIR)
    destination = _validate_destination_for_single_run(base_dir, cultivar, model_name, seed)
    paths = build_run_paths(base_dir, cultivar, model_name, seed)
    ensure_run_dir(paths)

    spec = build_feature_spec(cultivar, model_name)
    data_path = dataset_path(repo_root, cultivar)
    fit_frame = load_training_validation_frame(data_path)
    sequences = build_train_validation_sequences(fit_frame, spec, lookback=config.lookback)
    scaler = _validate_scaler(repo_root, cultivar)

    model = build_gc3_ge_model(model_name, len(spec.rama_a), len(spec.rama_b))
    lr_logger = LearningRateLogger()
    callbacks = build_callbacks(paths.root)
    callbacks.append(lr_logger.as_callback())

    config_payload = {
        "cultivar": cultivar,
        "model_name": model_name,
        "seed": seed,
        "official_result": True,
        "dataset_path": str(data_path),
        "scaler_path": scaler["path"],
        "test_used_for_training": False,
        "test_loaded_for_fit": False,
        "features_a": spec.rama_a,
        "features_b": spec.rama_b,
        "target": spec.target,
        "training_config": asdict(config),
        "callbacks": _callback_summary(callbacks),
        "destination": destination,
    }
    write_json(config_payload, paths.config)

    metadata = base_metadata(
        cultivar=cultivar,
        model_name=model_name,
        seed=seed,
        model_config=_model_config_dict(spec),
        determinism_settings=asdict(determinism),
        dataset_path=data_path,
        scaler_path=Path(scaler["path"]),
        lookback=config.lookback,
        batch_size=config.batch_size,
        learning_rate=config.learning_rate,
        max_epochs=config.max_epochs,
    )

    start = time.perf_counter()
    history = model.fit(
        [sequences["train"]["X_a"], sequences["train"]["X_b"]],
        sequences["train"]["y"],
        validation_data=(
            [sequences["validation"]["X_a"], sequences["validation"]["X_b"]],
            sequences["validation"]["y"],
        ),
        epochs=config.max_epochs,
        batch_size=config.batch_size,
        shuffle=config.shuffle,
        callbacks=callbacks,
        verbose=2,
    )
    fit_seconds = time.perf_counter() - start

    history_frame = history_to_frame(history, lr_logger.values)
    save_history_frame(history_frame, paths.history)
    best_epoch = int(history_frame.loc[history_frame["val_loss"].idxmin(), "epoch"])
    stopped_epoch = int(len(history_frame))
    metadata = replace(
        metadata,
        tensorflow_version=tf.__version__,
        keras_version=keras.__version__,
        numpy_version=np.__version__,
        gpu=str(tf.config.list_physical_devices("GPU")),
        best_epoch=best_epoch,
        stopped_epoch=stopped_epoch,
    )
    write_metadata(metadata, paths.metadata)

    final_status = {
        "status": "complete",
        "cultivar": cultivar,
        "model_name": model_name,
        "seed": seed,
        "fit_seconds": fit_seconds,
        "best_epoch": best_epoch,
        "stopped_epoch": stopped_epoch,
        "best_val_loss": float(history_frame["val_loss"].min()),
        "final_loss": float(history_frame["loss"].iloc[-1]),
        "final_val_loss": float(history_frame["val_loss"].iloc[-1]),
        "final_mae": float(history_frame["mae"].iloc[-1]),
        "final_val_mae": float(history_frame["val_mae"].iloc[-1]),
        "final_learning_rate": float(history_frame["learning_rate"].iloc[-1]),
        "history_path": str(paths.history),
        "checkpoint_path": str(paths.checkpoint),
        "metadata_path": str(paths.metadata),
        "config_path": str(paths.config),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    }
    paths.logs.mkdir(parents=True, exist_ok=True)
    write_json(final_status, paths.logs / "final_status.json")
    return final_status


def _validate_destination_for_single_run(
    base_dir: Path,
    cultivar: Cultivar,
    model_name: ModelName,
    seed: int,
) -> dict[str, Any]:
    if "technical_pilot" in base_dir.as_posix():
        raise ValueError(f"Official destination must not be technical_pilot*: {base_dir}")
    paths = build_run_paths(base_dir, cultivar, model_name, seed)
    existing_files = [str(path) for path in paths.root.rglob("*") if path.is_file()] if paths.root.exists() else []
    if existing_files:
        raise FileExistsError(
            "Official run directory already contains files and will not be overwritten: "
            + ", ".join(existing_files)
        )
    return {
        "base_dir": str(base_dir),
        "run_dir": str(paths.root),
        "differentiated_from_technical_pilot": True,
        "silent_overwrite_prevented": True,
    }
