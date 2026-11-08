"""History normalization for future GC3/GE training diagnostics."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


HISTORY_COLUMNS = ("epoch", "loss", "val_loss", "mae", "val_mae", "learning_rate")


def history_to_frame(history, learning_rates: list[float] | None = None) -> pd.DataFrame:
    data = history.history
    n_epochs = len(data.get("loss", []))
    frame = pd.DataFrame(
        {
            "epoch": list(range(1, n_epochs + 1)),
            "loss": data.get("loss", [None] * n_epochs),
            "val_loss": data.get("val_loss", [None] * n_epochs),
            "mae": data.get("mae", [None] * n_epochs),
            "val_mae": data.get("val_mae", [None] * n_epochs),
            "learning_rate": learning_rates if learning_rates is not None else [None] * n_epochs,
        }
    )
    return frame.loc[:, HISTORY_COLUMNS]


def save_history_frame(frame: pd.DataFrame, path: Path) -> None:
    missing = [column for column in HISTORY_COLUMNS if column not in frame.columns]
    if missing:
        raise ValueError(f"History frame missing columns: {missing}")
    frame.loc[:, HISTORY_COLUMNS].to_csv(path, index=False)
