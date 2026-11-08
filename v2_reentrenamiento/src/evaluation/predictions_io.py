"""Prediction table helpers for future official runs."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


PREDICTION_COLUMNS = ("fecha", "y_real", "y_pred", "error", "abs_error", "es_shock")


def build_prediction_frame(fecha, y_real, y_pred, es_shock) -> pd.DataFrame:
    frame = pd.DataFrame(
        {
            "fecha": fecha,
            "y_real": y_real,
            "y_pred": y_pred,
            "es_shock": es_shock,
        }
    )
    frame["error"] = frame["y_pred"] - frame["y_real"]
    frame["abs_error"] = frame["error"].abs()
    return frame.loc[:, PREDICTION_COLUMNS]


def save_prediction_frame(frame: pd.DataFrame, path: Path) -> None:
    missing = [column for column in PREDICTION_COLUMNS if column not in frame.columns]
    if missing:
        raise ValueError(f"Prediction frame missing columns: {missing}")
    frame.loc[:, PREDICTION_COLUMNS].to_csv(path, index=False)
