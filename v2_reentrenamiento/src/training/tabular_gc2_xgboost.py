"""Tabular X_t -> y_(t+1) construction for GC2/XGBoost v2."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

from v2_reentrenamiento.src.models.features_gc2_xgboost import (
    GC2FeatureSpec,
    validate_gc2_columns_available,
)


YEAR_COL = "a\u00f1o"
MONTH_COL = "mes"


@dataclass(frozen=True)
class TabularSplit:
    X: np.ndarray
    y: np.ndarray
    x_dates: pd.Series
    target_dates: pd.Series


@dataclass(frozen=True)
class GC2TabularBundle:
    train: TabularSplit
    validation: TabularSplit
    rows_loaded: int
    test_loaded: bool


def load_train_val_dataframe(path: Path) -> pd.DataFrame:
    """Load only rows needed for TRAIN and VAL dry-run, excluding TEST 2025."""

    rows: list[dict[str, str]] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if YEAR_COL not in (reader.fieldnames or []) or MONTH_COL not in (reader.fieldnames or []):
            raise ValueError(f"Dataset missing {YEAR_COL}/{MONTH_COL}: {path}")
        for row in reader:
            year = int(row[YEAR_COL])
            if year <= 2024:
                rows.append(row)

    frame = pd.DataFrame(rows)
    for column in frame.columns:
        frame[column] = pd.to_numeric(frame[column], errors="raise")
    frame["fecha"] = pd.to_datetime(
        {
            "year": frame[YEAR_COL].astype(int),
            "month": frame[MONTH_COL].astype(int),
            "day": 1,
        }
    )
    frame = frame.sort_values("fecha").reset_index(drop=True)
    _validate_train_val_frame(frame)
    return frame


def build_gc2_tabular_bundle(frame: pd.DataFrame, spec: GC2FeatureSpec) -> GC2TabularBundle:
    validate_gc2_columns_available(spec, set(frame.columns))
    _validate_train_val_frame(frame)

    predictors = frame.loc[:, spec.predictors].to_numpy(dtype=float)
    target = frame.loc[:, spec.target].to_numpy(dtype=float)
    dates = frame["fecha"].reset_index(drop=True)

    x_rows: list[np.ndarray] = []
    y_values: list[float] = []
    x_dates: list[pd.Timestamp] = []
    target_dates: list[pd.Timestamp] = []

    for idx in range(len(frame) - 1):
        x_date = dates.iloc[idx]
        y_date = dates.iloc[idx + 1]
        if y_date != x_date + pd.DateOffset(months=1):
            raise ValueError(f"Non-consecutive monthly pair: {x_date} -> {y_date}")
        if y_date.year > 2024:
            raise ValueError("TEST target reached GC2 dry-run bundle.")
        x_rows.append(predictors[idx])
        y_values.append(float(target[idx + 1]))
        x_dates.append(x_date)
        target_dates.append(y_date)

    X = np.stack(x_rows).astype(float)
    y = np.asarray(y_values, dtype=float)
    x_series = pd.Series(x_dates, name="x_fecha")
    y_series = pd.Series(target_dates, name="target_fecha")

    train_mask = (y_series.dt.year <= 2023).to_numpy()
    val_mask = (y_series.dt.year == 2024).to_numpy()

    bundle = GC2TabularBundle(
        train=TabularSplit(
            X=X[train_mask],
            y=y[train_mask],
            x_dates=x_series[train_mask].reset_index(drop=True),
            target_dates=y_series[train_mask].reset_index(drop=True),
        ),
        validation=TabularSplit(
            X=X[val_mask],
            y=y[val_mask],
            x_dates=x_series[val_mask].reset_index(drop=True),
            target_dates=y_series[val_mask].reset_index(drop=True),
        ),
        rows_loaded=int(len(frame)),
        test_loaded=False,
    )
    validate_gc2_tabular_bundle(bundle)
    return bundle


def validate_gc2_tabular_bundle(bundle: GC2TabularBundle) -> None:
    if bundle.test_loaded:
        raise ValueError("TEST must not be loaded for GC2 pre-flight.")
    if bundle.rows_loaded != 102:
        raise ValueError(f"Expected 102 TRAIN+VAL rows loaded, got {bundle.rows_loaded}.")
    expected_shapes = {
        "X_train": (89, 37),
        "y_train": (89,),
        "X_val": (12, 37),
        "y_val": (12,),
    }
    actual_shapes = {
        "X_train": tuple(bundle.train.X.shape),
        "y_train": tuple(bundle.train.y.shape),
        "X_val": tuple(bundle.validation.X.shape),
        "y_val": tuple(bundle.validation.y.shape),
    }
    if actual_shapes != expected_shapes:
        raise ValueError(f"GC2 shape mismatch: expected {expected_shapes}, got {actual_shapes}")
    _assert_date(bundle.train.x_dates.iloc[0], "2016-07-01", "first TRAIN X")
    _assert_date(bundle.train.target_dates.iloc[0], "2016-08-01", "first TRAIN target")
    _assert_date(bundle.train.x_dates.iloc[-1], "2023-11-01", "last TRAIN X")
    _assert_date(bundle.train.target_dates.iloc[-1], "2023-12-01", "last TRAIN target")
    _assert_date(bundle.validation.x_dates.iloc[0], "2023-12-01", "first VAL X")
    _assert_date(bundle.validation.target_dates.iloc[0], "2024-01-01", "first VAL target")
    _assert_date(bundle.validation.x_dates.iloc[-1], "2024-11-01", "last VAL X")
    _assert_date(bundle.validation.target_dates.iloc[-1], "2024-12-01", "last VAL target")


def _validate_train_val_frame(frame: pd.DataFrame) -> None:
    if frame.empty:
        raise ValueError("GC2 train/validation frame is empty.")
    if frame["fecha"].min() != pd.Timestamp("2016-07-01"):
        raise ValueError(f"Expected first loaded row 2016-07, got {frame['fecha'].min()}.")
    if frame["fecha"].max() != pd.Timestamp("2024-12-01"):
        raise ValueError(f"Expected last loaded row 2024-12, got {frame['fecha'].max()}.")
    if (frame["fecha"].dt.year >= 2025).any():
        raise ValueError("TEST rows reached GC2 train/validation dataframe.")
    if not frame["fecha"].is_monotonic_increasing:
        raise ValueError("GC2 rows must be sorted.")
    if frame["fecha"].duplicated().any():
        raise ValueError("Duplicate monthly rows are not allowed.")


def _assert_date(value: pd.Timestamp, expected: str, label: str) -> None:
    expected_ts = pd.Timestamp(expected)
    if value != expected_ts:
        raise ValueError(f"Expected {label} {expected_ts.date()}, got {value.date()}.")
