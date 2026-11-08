"""Official D35-b shock protocol."""

from __future__ import annotations

import numpy as np


P75_TRAIN_ONLY = {
    "sutil": 0.240834900212216,
    "dulce": 0.320281354618397,
}

OFFICIAL_TEST_SHOCKS_2025 = {
    "sutil": ("2025-01", "2025-07", "2025-11"),
    "dulce": ("2025-01", "2025-02", "2025-03"),
}


def relative_change_abs(y_previous, y_current) -> np.ndarray:
    y_previous = np.asarray(y_previous, dtype=float)
    y_current = np.asarray(y_current, dtype=float)
    if np.any(y_previous == 0):
        raise ValueError("Previous target value cannot be zero for relative change.")
    return np.abs((y_current - y_previous) / y_previous)


def shock_mask(cultivar: str, y_previous, y_current) -> np.ndarray:
    if cultivar not in P75_TRAIN_ONLY:
        raise ValueError(f"Unsupported cultivar: {cultivar}")
    return relative_change_abs(y_previous, y_current) > P75_TRAIN_ONLY[cultivar]
