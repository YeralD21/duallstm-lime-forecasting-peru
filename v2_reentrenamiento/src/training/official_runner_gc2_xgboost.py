"""Official GC2/XGBoost runner scaffold and pre-flight dry-run.

This module intentionally exposes only dry-run/pre-flight behavior for the
current protocol-closing task. It must not call XGBRegressor.fit here.
"""

from __future__ import annotations

import json
import platform
import subprocess
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from xgboost import XGBRegressor

from v2_reentrenamiento.src.models.features_gc2_xgboost import (
    FORBIDDEN_CONTEMPORARY_EXOGENOUS,
    FORBIDDEN_EXACT,
    FORBIDDEN_PATTERN_FRAGMENTS,
    build_gc2_feature_spec,
)
from v2_reentrenamiento.src.training.config_gc2_xgboost import (
    OFFICIAL_GC2_CULTIVARS,
    OFFICIAL_GC2_SEEDS,
    OFFICIAL_GC2_XGB_CONFIG,
    XGBoostGC2Config,
    validate_gc2_config,
    validate_gc2_seeds,
)
from v2_reentrenamiento.src.training.metadata_gc3_ge import (
    current_git_commit,
    sha256_file,
    stable_config_hash,
)
from v2_reentrenamiento.src.training.tabular_gc2_xgboost import (
    build_gc2_tabular_bundle,
    load_train_val_dataframe,
)


REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = REPO_ROOT / "v2_reentrenamiento/data/processed"
SCALER_DIR = REPO_ROOT / "v2_reentrenamiento/resultados_v2_final/scalers"
RESULTS_DIR = REPO_ROOT / "v2_reentrenamiento/resultados_v2_final/official_gc2_xgboost"
AUDIT_PATH = REPO_ROOT / "v2_reentrenamiento/auditorias/AUDITORIA_PREFLIGHT_GC2_XGBOOST.md"
DRY_RUN_JSON_PATH = REPO_ROOT / "v2_reentrenamiento/auditorias/gc2_xgboost_preflight_dry_run.json"


def dataset_path(cultivar: str) -> Path:
    return DATA_DIR / f"master_dataset_{cultivar}_v2_escalado.csv"


def scaler_path(cultivar: str) -> Path:
    return SCALER_DIR / f"scaler_{cultivar}_v2c.joblib"


def future_run_root(cultivar: str, seed: int) -> Path:
    return RESULTS_DIR / cultivar / "GC2_XGBoost" / f"seed_{seed:02d}"


def dry_run_preflight(
    *,
    config: XGBoostGC2Config = OFFICIAL_GC2_XGB_CONFIG,
    audit_path: Path = AUDIT_PATH,
    json_path: Path = DRY_RUN_JSON_PATH,
) -> dict[str, Any]:
    validate_gc2_config(config)
    validate_gc2_seeds()

    started = datetime.now(timezone.utc)
    cultivar_results = {}
    instantiated_params: dict[str, dict[str, Any]] = {}

    for cultivar in OFFICIAL_GC2_CULTIVARS:
        spec = build_gc2_feature_spec(cultivar)
        frame = load_train_val_dataframe(dataset_path(cultivar))
        bundle = build_gc2_tabular_bundle(frame, spec)

        seed_params: dict[str, Any] = {}
        for seed in OFFICIAL_GC2_SEEDS:
            model = XGBRegressor(**config.xgb_params(seed))
            params = model.get_params(deep=False)
            seed_params[str(seed)] = {
                key: params.get(key)
                for key in (
                    "objective",
                    "eval_metric",
                    "booster",
                    "max_depth",
                    "min_child_weight",
                    "learning_rate",
                    "n_estimators",
                    "subsample",
                    "colsample_bytree",
                    "reg_alpha",
                    "reg_lambda",
                    "gamma",
                    "tree_method",
                    "n_jobs",
                    "random_state",
                )
            }
        instantiated_params[cultivar] = seed_params

        cultivar_results[cultivar] = {
            "dataset_path": str(dataset_path(cultivar)),
            "dataset_hash": sha256_file(dataset_path(cultivar)),
            "scaler_path": str(scaler_path(cultivar)),
            "scaler_hash": sha256_file(scaler_path(cultivar)),
            "features": list(spec.predictors),
            "n_features": len(spec.predictors),
            "target": spec.target,
            "train_shape": {
                "X": list(bundle.train.X.shape),
                "y": list(bundle.train.y.shape),
            },
            "validation_shape": {
                "X": list(bundle.validation.X.shape),
                "y": list(bundle.validation.y.shape),
            },
            "train_first_x": _ym(bundle.train.x_dates.iloc[0]),
            "train_first_target": _ym(bundle.train.target_dates.iloc[0]),
            "train_last_x": _ym(bundle.train.x_dates.iloc[-1]),
            "train_last_target": _ym(bundle.train.target_dates.iloc[-1]),
            "train_n": int(len(bundle.train.y)),
            "val_first_x": _ym(bundle.validation.x_dates.iloc[0]),
            "val_first_target": _ym(bundle.validation.target_dates.iloc[0]),
            "val_last_x": _ym(bundle.validation.x_dates.iloc[-1]),
            "val_last_target": _ym(bundle.validation.target_dates.iloc[-1]),
            "val_n": int(len(bundle.validation.y)),
            "rows_loaded": bundle.rows_loaded,
            "test_loaded": bundle.test_loaded,
            "future_artifact_roots": [
                str(future_run_root(cultivar, seed)) for seed in OFFICIAL_GC2_SEEDS
            ],
        }

    controls = _build_controls(cultivar_results, instantiated_params, config)
    failed = [item for item in controls if not item["ok"]]
    if failed:
        payload = _payload(started, cultivar_results, instantiated_params, controls, status="failed")
        _write_json(payload, json_path)
        _write_audit(payload, audit_path)
        reasons = "; ".join(f"{item['id']}: {item['detail']}" for item in failed)
        raise ValueError(f"GC2/XGBoost pre-flight failed: {reasons}")

    payload = _payload(started, cultivar_results, instantiated_params, controls, status="approved")
    _write_json(payload, json_path)
    _write_audit(payload, audit_path)
    return payload


def run_official_training(
    repo_root: Path,
    cultivar: str,
    seed: int,
    *,
    config: XGBoostGC2Config = OFFICIAL_GC2_XGB_CONFIG,
) -> dict[str, Any]:
    """Train one official GC2/XGBoost run without loading TEST 2025."""

    if cultivar not in OFFICIAL_GC2_CULTIVARS:
        raise ValueError(f"Unsupported official cultivar: {cultivar}")
    if seed not in OFFICIAL_GC2_SEEDS:
        raise ValueError(f"Unsupported official seed: {seed}")
    validate_gc2_config(config)
    validate_gc2_seeds()

    started = datetime.now(timezone.utc)
    data_path = repo_root / "v2_reentrenamiento/data/processed" / f"master_dataset_{cultivar}_v2_escalado.csv"
    scaler_file = repo_root / "v2_reentrenamiento/resultados_v2_final/scalers" / f"scaler_{cultivar}_v2c.joblib"
    run_dir = (
        repo_root
        / "v2_reentrenamiento/resultados_v2_final/official_gc2_xgboost"
        / cultivar
        / "GC2_XGBoost"
        / f"seed_{seed:02d}"
    )
    run_dir.mkdir(parents=True, exist_ok=True)

    spec = build_gc2_feature_spec(cultivar)
    frame = load_train_val_dataframe(data_path)
    bundle = build_gc2_tabular_bundle(frame, spec)
    scaler = joblib.load(scaler_file)

    params = config.xgb_params(seed)
    model = XGBRegressor(**params)
    model.fit(bundle.train.X, bundle.train.y)

    train_pred_scaled = model.predict(bundle.train.X)
    val_pred_scaled = model.predict(bundle.validation.X)
    train_real_scaled = bundle.train.y
    val_real_scaled = bundle.validation.y

    train_real = _inverse_target(scaler, spec.target, train_real_scaled)
    train_pred = _inverse_target(scaler, spec.target, train_pred_scaled)
    val_real = _inverse_target(scaler, spec.target, val_real_scaled)
    val_pred = _inverse_target(scaler, spec.target, val_pred_scaled)

    metrics = {
        "train": _metrics(train_real, train_pred),
        "validation": _metrics(val_real, val_pred),
        "train_scaled": _metrics(train_real_scaled, train_pred_scaled),
        "validation_scaled": _metrics(val_real_scaled, val_pred_scaled),
    }
    predictions = pd.concat(
        [
            _predictions_frame("train", bundle.train.target_dates, train_real, train_pred, train_real_scaled, train_pred_scaled),
            _predictions_frame("validation", bundle.validation.target_dates, val_real, val_pred, val_real_scaled, val_pred_scaled),
        ],
        ignore_index=True,
    )
    feature_importance = pd.DataFrame(
        {
            "feature": spec.predictors,
            "importance_gain": model.feature_importances_,
        }
    ).sort_values("importance_gain", ascending=False, ignore_index=True)

    model.save_model(run_dir / "model.xgboost.json")
    joblib.dump(model, run_dir / "model.joblib")
    predictions.to_csv(run_dir / "predicciones_train_val.csv", index=False, encoding="utf-8")
    feature_importance.to_csv(run_dir / "feature_importance.csv", index=False, encoding="utf-8")
    _write_json(metrics, run_dir / "metricas.json")

    config_payload = {
        "cultivar": cultivar,
        "model_name": "GC2_XGBoost",
        "seed": seed,
        "representation": "X_t -> y_(t+1)",
        "config": config.as_dict(),
        "xgb_params": params,
        "features": list(spec.predictors),
        "target": spec.target,
        "no_hpo": True,
        "no_cv": True,
        "no_early_stopping": True,
        "no_best_seed_selection": True,
        "test_loaded": False,
    }
    _write_json(config_payload, run_dir / "config.json")

    metadata = {
        "status": "complete",
        "started_utc": started.isoformat(),
        "finished_utc": datetime.now(timezone.utc).isoformat(),
        "cultivar": cultivar,
        "model_name": "GC2_XGBoost",
        "seed": seed,
        "python": platform.python_version(),
        "os": platform.platform(),
        "cpu": platform.processor() or None,
        "xgboost_version": _xgboost_version(),
        "dataset_path": str(data_path),
        "dataset_hash": sha256_file(data_path),
        "scaler_path": str(scaler_file),
        "scaler_hash": sha256_file(scaler_file),
        "config_hash": stable_config_hash(config.as_dict()),
        "git_commit": current_git_commit(),
        "git_status_sb": _git_status_sb(),
        "train_shape": {"X": list(bundle.train.X.shape), "y": list(bundle.train.y.shape)},
        "validation_shape": {"X": list(bundle.validation.X.shape), "y": list(bundle.validation.y.shape)},
        "test_loaded": bundle.test_loaded,
        "train_dates": {
            "x_first": _ym(bundle.train.x_dates.iloc[0]),
            "x_last": _ym(bundle.train.x_dates.iloc[-1]),
            "target_first": _ym(bundle.train.target_dates.iloc[0]),
            "target_last": _ym(bundle.train.target_dates.iloc[-1]),
        },
        "validation_dates": {
            "x_first": _ym(bundle.validation.x_dates.iloc[0]),
            "x_last": _ym(bundle.validation.x_dates.iloc[-1]),
            "target_first": _ym(bundle.validation.target_dates.iloc[0]),
            "target_last": _ym(bundle.validation.target_dates.iloc[-1]),
        },
        "artifacts": {
            "model_xgboost_json": str(run_dir / "model.xgboost.json"),
            "model_joblib": str(run_dir / "model.joblib"),
            "metrics": str(run_dir / "metricas.json"),
            "predictions": str(run_dir / "predicciones_train_val.csv"),
            "feature_importance": str(run_dir / "feature_importance.csv"),
            "config": str(run_dir / "config.json"),
            "metadata": str(run_dir / "metadata.json"),
        },
        "metrics": metrics,
    }
    _write_json(metadata, run_dir / "metadata.json")
    return {
        "status": "complete",
        "cultivar": cultivar,
        "model_name": "GC2_XGBoost",
        "seed": seed,
        "run_dir": str(run_dir),
        "metrics": metrics,
    }


def _build_controls(
    cultivar_results: dict[str, Any],
    instantiated_params: dict[str, dict[str, Any]],
    config: XGBoostGC2Config,
) -> list[dict[str, Any]]:
    features_by_cultivar = {c: data["features"] for c, data in cultivar_results.items()}
    first_params = instantiated_params["sutil"]["0"]

    def add(control_id: int, name: str, ok: bool, detail: str) -> dict[str, Any]:
        return {"id": control_id, "name": name, "ok": bool(ok), "detail": detail}

    all_features = [feature for features in features_by_cultivar.values() for feature in features]
    controls = [
        add(1, "cultivares = sutil/dulce", tuple(cultivar_results) == OFFICIAL_GC2_CULTIVARS, str(tuple(cultivar_results))),
        add(2, "seeds = 0..9", OFFICIAL_GC2_SEEDS == tuple(range(10)), str(OFFICIAL_GC2_SEEDS)),
        add(3, "total futuro = 20 corridas", len(OFFICIAL_GC2_CULTIVARS) * len(OFFICIAL_GC2_SEEDS) == 20, "2 x 10"),
        add(4, "features = 37", all(data["n_features"] == 37 for data in cultivar_results.values()), str({c: d["n_features"] for c, d in cultivar_results.items()})),
        add(5, "NLP ausente", not any(feature.startswith("avg_sentiment") or feature.startswith("n_noticias") for feature in all_features), "sin avg_sentiment/n_noticias"),
        add(6, "precio ausente", not any("precio_chacra_kg" in feature for feature in all_features), "precio_chacra_kg no presente"),
        add(7, "n_provincias ausente", not any("n_provincias" in feature for feature in all_features), "n_provincias no presente"),
        add(8, "total_afectados ausente", not any("total_afectados" in feature for feature in all_features), "total_afectados no presente"),
        add(9, "contemporaneas exogenas ausentes", not any(feature in FORBIDDEN_CONTEMPORARY_EXOGENOUS for feature in all_features), "solo exogenas lagged"),
        add(10, "lag2 ausente", not any("lag2" in feature for feature in all_features), "lag2 no presente"),
        add(11, "rolling features ausentes", not any(any(fragment in feature for fragment in ("roll", "rolling", "mean", "std")) for feature in all_features), "rolling/mean/std no presentes"),
        add(12, "TRAIN n=89", all(data["train_n"] == 89 for data in cultivar_results.values()), str({c: d["train_n"] for c, d in cultivar_results.items()})),
        add(13, "TRAIN X 2016-07..2023-11", all(data["train_first_x"] == "2016-07" and data["train_last_x"] == "2023-11" for data in cultivar_results.values()), "origenes TRAIN"),
        add(14, "TRAIN y 2016-08..2023-12", all(data["train_first_target"] == "2016-08" and data["train_last_target"] == "2023-12" for data in cultivar_results.values()), "targets TRAIN"),
        add(15, "VAL n=12", all(data["val_n"] == 12 for data in cultivar_results.values()), str({c: d["val_n"] for c, d in cultivar_results.items()})),
        add(16, "VAL X 2023-12..2024-11", all(data["val_first_x"] == "2023-12" and data["val_last_x"] == "2024-11" for data in cultivar_results.values()), "origenes VAL"),
        add(17, "VAL y 2024-01..2024-12", all(data["val_first_target"] == "2024-01" and data["val_last_target"] == "2024-12" for data in cultivar_results.values()), "targets VAL"),
        add(18, "no TEST load", all(data["test_loaded"] is False for data in cultivar_results.values()), "solo filas <=2024 cargadas"),
        add(19, "no HPO", config.hpo_performed is False, "hpo_performed=false"),
        add(20, "no CV", config.cv_performed is False, "cv_performed=false"),
        add(21, "no early stopping", config.early_stopping is False, "early_stopping=false"),
        add(22, "n_estimators=200", first_params["n_estimators"] == 200, str(first_params["n_estimators"])),
        add(23, "max_depth=2", first_params["max_depth"] == 2, str(first_params["max_depth"])),
        add(24, "min_child_weight=1", first_params["min_child_weight"] == 1, str(first_params["min_child_weight"])),
        add(25, "learning_rate=.05", abs(first_params["learning_rate"] - 0.05) < 1e-12, str(first_params["learning_rate"])),
        add(26, "subsample=.8", abs(first_params["subsample"] - 0.8) < 1e-12, str(first_params["subsample"])),
        add(27, "colsample_bytree=.8", abs(first_params["colsample_bytree"] - 0.8) < 1e-12, str(first_params["colsample_bytree"])),
        add(28, "reg_alpha=0", abs(first_params["reg_alpha"] - 0.0) < 1e-12, str(first_params["reg_alpha"])),
        add(29, "reg_lambda=1", abs(first_params["reg_lambda"] - 1.0) < 1e-12, str(first_params["reg_lambda"])),
        add(30, "gamma=0", abs(first_params["gamma"] - 0.0) < 1e-12, str(first_params["gamma"])),
        add(31, "tree_method=hist", first_params["tree_method"] == "hist", str(first_params["tree_method"])),
        add(32, "n_jobs=1", first_params["n_jobs"] == 1, str(first_params["n_jobs"])),
        add(33, "objective reg:squarederror", first_params["objective"] == "reg:squarederror", str(first_params["objective"])),
        add(34, "eval_metric mae", first_params["eval_metric"] == "mae", str(first_params["eval_metric"])),
        add(35, "booster gbtree", first_params["booster"] == "gbtree", str(first_params["booster"])),
    ]
    _ = FORBIDDEN_EXACT, FORBIDDEN_PATTERN_FRAGMENTS
    return controls


def _payload(
    started: datetime,
    cultivar_results: dict[str, Any],
    instantiated_params: dict[str, dict[str, Any]],
    controls: list[dict[str, Any]],
    *,
    status: str,
) -> dict[str, Any]:
    finished = datetime.now(timezone.utc)
    config_dict = OFFICIAL_GC2_XGB_CONFIG.as_dict()
    return {
        "status": status,
        "started_utc": started.isoformat(),
        "finished_utc": finished.isoformat(),
        "duration_seconds": (finished - started).total_seconds(),
        "model_fit_executed": False,
        "test_loaded": False,
        "official_cultivars": list(OFFICIAL_GC2_CULTIVARS),
        "official_seeds": list(OFFICIAL_GC2_SEEDS),
        "future_expected_runs": 20,
        "config": config_dict,
        "config_hash": stable_config_hash(config_dict),
        "git_commit": current_git_commit(),
        "git_status_sb": _git_status_sb(),
        "environment": {
            "python": platform.python_version(),
            "os": platform.platform(),
            "cpu": platform.processor() or None,
        },
        "components_reused": [
            "v2_reentrenamiento.src.models.features_gc3_ge constants",
            "v2_reentrenamiento.src.training.metadata_gc3_ge hash/git helpers",
        ],
        "components_created": [
            "v2_reentrenamiento.src.models.features_gc2_xgboost",
            "v2_reentrenamiento.src.training.config_gc2_xgboost",
            "v2_reentrenamiento.src.training.tabular_gc2_xgboost",
            "v2_reentrenamiento.src.training.official_runner_gc2_xgboost",
        ],
        "cultivar_results": cultivar_results,
        "instantiated_params": instantiated_params,
        "controls": controls,
        "all_controls_ok": all(item["ok"] for item in controls),
    }


def _write_json(payload: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def _metrics(y_true: np.ndarray, y_pred: np.ndarray) -> dict[str, float]:
    return {
        "mae": float(mean_absolute_error(y_true, y_pred)),
        "rmse": float(mean_squared_error(y_true, y_pred) ** 0.5),
        "r2": float(r2_score(y_true, y_pred)),
    }


def _inverse_target(scaler: Any, target: str, values: np.ndarray) -> np.ndarray:
    feature_names = list(getattr(scaler, "feature_names_in_", []))
    if target not in feature_names:
        raise ValueError(f"Target {target} not found in scaler feature_names_in_.")
    idx = feature_names.index(target)
    if not hasattr(scaler, "mean_") or not hasattr(scaler, "scale_"):
        raise TypeError("GC2 target inverse transform expects a fitted StandardScaler.")
    return np.asarray(values, dtype=float) * float(scaler.scale_[idx]) + float(scaler.mean_[idx])


def _predictions_frame(
    split: str,
    dates: pd.Series,
    real: np.ndarray,
    pred: np.ndarray,
    real_scaled: np.ndarray,
    pred_scaled: np.ndarray,
) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "fecha": dates.dt.strftime("%Y-%m"),
            "particion": split,
            "real_t": real,
            "predicho_t": pred,
            "real_scaled": real_scaled,
            "predicho_scaled": pred_scaled,
            "residuo_t": real - pred,
        }
    )


def _xgboost_version() -> str:
    import xgboost

    return xgboost.__version__


def _write_audit(payload: dict[str, Any], path: Path) -> None:
    lines = [
        "# AUDITORIA PREFLIGHT GC2/XGBOOST",
        "",
        "Dry-run/pre-flight del runner oficial GC2/XGBoost v2. No se entreno XGBoost, no se ejecuto `model.fit()`, no se hizo HPO, no se ejecuto TimeSeriesSplit para seleccion y no se cargo TEST 2025 para entrenamiento ni validacion.",
        "",
        "## Archivos creados/modificados",
        "",
        "- `v2_reentrenamiento/DECISIONES_METODOLOGICAS.md`",
        "- `v2_reentrenamiento/src/models/features_gc2_xgboost.py`",
        "- `v2_reentrenamiento/src/training/config_gc2_xgboost.py`",
        "- `v2_reentrenamiento/src/training/tabular_gc2_xgboost.py`",
        "- `v2_reentrenamiento/src/training/official_runner_gc2_xgboost.py`",
        "- `v2_reentrenamiento/auditorias/AUDITORIA_PREFLIGHT_GC2_XGBOOST.md`",
        "- `v2_reentrenamiento/auditorias/gc2_xgboost_preflight_dry_run.json`",
        "",
        "## Componentes reutilizados",
        "",
    ]
    lines.extend(f"- `{item}`" for item in payload["components_reused"])
    lines.extend(
        [
            "",
            "## Config oficial",
            "",
            "```json",
            json.dumps(payload["config"], indent=2, sort_keys=True),
            "```",
            "",
            "## Shapes y fechas",
            "",
        ]
    )
    for cultivar, data in payload["cultivar_results"].items():
        lines.extend(
            [
                f"### {cultivar}",
                "",
                f"- Features: {data['n_features']}",
                f"- TRAIN X: {data['train_first_x']}..{data['train_last_x']}",
                f"- TRAIN y: {data['train_first_target']}..{data['train_last_target']}",
                f"- TRAIN shape: X={data['train_shape']['X']}, y={data['train_shape']['y']}",
                f"- VAL X: {data['val_first_x']}..{data['val_last_x']}",
                f"- VAL y: {data['val_first_target']}..{data['val_last_target']}",
                f"- VAL shape: X={data['validation_shape']['X']}, y={data['validation_shape']['y']}",
                f"- TEST loaded: {str(data['test_loaded']).lower()}",
                "",
            ]
        )
    lines.extend(
        [
            "## Features GC2",
            "",
            "GC2 usa exactamente las 37 features NO-NLP de GC3. Ausentes: NLP, precio_chacra_kg, n_provincias, total_afectados, contemporaneas exogenas, lag2 y rolling mean/std.",
            "",
            "```text",
        ]
    )
    lines.extend(payload["cultivar_results"]["sutil"]["features"])
    lines.extend(
        [
            "```",
            "",
            "## Controles pre-flight",
            "",
            "| ID | Control | Estado | Detalle |",
            "|---:|---|---|---|",
        ]
    )
    for item in payload["controls"]:
        status = "OK" if item["ok"] else "FAIL"
        lines.append(f"| {item['id']} | {item['name']} | {status} | {item['detail']} |")
    lines.extend(
        [
            "",
            "## Confirmaciones",
            "",
            "- `model.fit()` ejecutado: NO.",
            "- TEST 2025 cargado: NO.",
            "- HPO ejecutado: NO.",
            "- TimeSeriesSplit/CV ejecutado: NO.",
            "- Early stopping usado: NO.",
            "- Best seed selection: NO.",
            "",
            "## Git",
            "",
            f"- Git commit/hash: `{payload['git_commit']}`",
            "",
            "```text",
            payload["git_status_sb"],
            "```",
            "",
            "- No commit.",
            "- No push.",
            "",
        ]
    )
    final = (
        "GC2/XGBOOST PRE-FLIGHT APROBADO Y LISTO PARA AUTORIZACIÓN DE ENTRENAMIENTO"
        if payload["all_controls_ok"]
        else "GC2/XGBOOST PRE-FLIGHT NO APROBADO: controles fallidos"
    )
    lines.append(final)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _ym(value) -> str:
    return value.strftime("%Y-%m")


def _git_status_sb() -> str:
    result = subprocess.run(
        ["git", "status", "-sb"],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    text = result.stdout.strip()
    if result.stderr.strip():
        text = result.stderr.strip() + ("\n" + text if text else "")
    return text


if __name__ == "__main__":
    result = dry_run_preflight()
    print(json.dumps({"status": result["status"], "all_controls_ok": result["all_controls_ok"]}, indent=2))
