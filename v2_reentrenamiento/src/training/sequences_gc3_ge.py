"""Temporal sequence construction for GC3/GE v2."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

from v2_reentrenamiento.src.models.features_gc3_ge import FeatureSpec, validate_columns_available
from .config_gc3_ge import OFFICIAL_TRAINING_CONFIG


YEAR_COL = "a\u00f1o"
MONTH_COL = "mes"


@dataclass(frozen=True)
class SequenceSplit:
    X_a: np.ndarray
    X_b: np.ndarray
    y: np.ndarray
    target_dates: pd.Series


@dataclass(frozen=True)
class SequenceBundle:
    train: SequenceSplit
    validation: SequenceSplit
    test: SequenceSplit
    feature_rows: int
    train_feature_rows: int
    lookback: int


def load_feature_dataframe(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    if YEAR_COL not in df.columns or MONTH_COL not in df.columns:
        raise ValueError("Feature dataset must contain year/month columns.")
    df = df.copy()
    df["fecha"] = pd.to_datetime(
        {
            "year": df[YEAR_COL].astype(int),
            "month": df[MONTH_COL].astype(int),
            "day": 1,
        }
    )
    return df.sort_values("fecha").reset_index(drop=True)


def build_sequences(
    df: pd.DataFrame,
    spec: FeatureSpec,
    *,
    lookback: int = OFFICIAL_TRAINING_CONFIG.lookback,
) -> SequenceBundle:
    validate_columns_available(spec, set(df.columns))
    _validate_frame_dates(df)

    X_a_list: list[np.ndarray] = []
    X_b_list: list[np.ndarray] = []
    y_list: list[float] = []
    dates: list[pd.Timestamp] = []

    values_a = df.loc[:, spec.rama_a].to_numpy(dtype=float)
    values_b = df.loc[:, spec.rama_b].to_numpy(dtype=float)
    values_y = df.loc[:, spec.target].to_numpy(dtype=float)
    all_dates = df["fecha"].reset_index(drop=True)

    for target_idx in range(lookback, len(df)):
        start = target_idx - lookback
        stop = target_idx
        context_dates = all_dates.iloc[start:stop]
        target_date = all_dates.iloc[target_idx]
        if not (context_dates < target_date).all():
            raise ValueError("Future leakage detected in context dates.")
        X_a_list.append(values_a[start:stop])
        X_b_list.append(values_b[start:stop])
        y_list.append(float(values_y[target_idx]))
        dates.append(target_date)

    X_a = np.stack(X_a_list)
    X_b = np.stack(X_b_list)
    y = np.asarray(y_list, dtype=float)
    target_dates = pd.Series(dates, name="fecha")

    train_mask = target_dates.dt.year <= 2023
    val_mask = target_dates.dt.year == 2024
    test_mask = target_dates.dt.year == 2025

    bundle = SequenceBundle(
        train=_split(X_a, X_b, y, target_dates, train_mask),
        validation=_split(X_a, X_b, y, target_dates, val_mask),
        test=_split(X_a, X_b, y, target_dates, test_mask),
        feature_rows=len(df),
        train_feature_rows=int((df["fecha"].dt.year <= 2023).sum()),
        lookback=lookback,
    )
    validate_sequence_bundle(bundle)
    return bundle


def validate_sequence_bundle(bundle: SequenceBundle) -> None:
    if bundle.feature_rows != 114:
        raise ValueError(f"Expected 114 feature rows, got {bundle.feature_rows}.")
    if bundle.train_feature_rows != 90:
        raise ValueError(f"Expected 90 TRAIN feature rows, got {bundle.train_feature_rows}.")
    if len(bundle.train.y) != 84:
        raise ValueError(f"Expected 84 TRAIN sequences, got {len(bundle.train.y)}.")
    if len(bundle.validation.y) != 12:
        raise ValueError(f"Expected 12 validation targets, got {len(bundle.validation.y)}.")
    if len(bundle.test.y) != 12:
        raise ValueError(f"Expected 12 test targets, got {len(bundle.test.y)}.")

    _assert_date(bundle.train.target_dates.iloc[0], "2017-01-01", "first TRAIN target")
    _assert_date(bundle.train.target_dates.iloc[-1], "2023-12-01", "last TRAIN target")
    _assert_date(bundle.validation.target_dates.iloc[0], "2024-01-01", "first VAL target")
    _assert_date(bundle.test.target_dates.iloc[0], "2025-01-01", "first TEST target")


def _split(X_a, X_b, y, dates, mask) -> SequenceSplit:
    return SequenceSplit(
        X_a=X_a[mask.to_numpy()],
        X_b=X_b[mask.to_numpy()],
        y=y[mask.to_numpy()],
        target_dates=dates[mask].reset_index(drop=True),
    )


def _validate_frame_dates(df: pd.DataFrame) -> None:
    if (df["fecha"].dt.year == 2026).any():
        raise ValueError("2026 rows are not allowed.")
    if df["fecha"].min() != pd.Timestamp("2016-07-01"):
        raise ValueError(f"Feature rows must start at 2016-07, got {df['fecha'].min()}.")
    if df["fecha"].max() != pd.Timestamp("2025-12-01"):
        raise ValueError(f"Feature rows must end at 2025-12, got {df['fecha'].max()}.")
    if not df["fecha"].is_monotonic_increasing:
        raise ValueError("Feature rows must be sorted by month.")
    if df["fecha"].duplicated().any():
        raise ValueError("Duplicate monthly rows are not allowed.")


def _assert_date(value: pd.Timestamp, expected: str, label: str) -> None:
    expected_ts = pd.Timestamp(expected)
    if value != expected_ts:
        raise ValueError(f"Expected {label} {expected_ts.date()}, got {value.date()}.")
