"""D35 metric definitions for future evaluation.

These functions are utilities only; this module does not run evaluation.
"""

from __future__ import annotations

import numpy as np


def mae(y_true, y_pred) -> float:
    return float(np.mean(np.abs(np.asarray(y_true) - np.asarray(y_pred))))


def rmse(y_true, y_pred) -> float:
    err = np.asarray(y_true) - np.asarray(y_pred)
    return float(np.sqrt(np.mean(err**2)))


def relmae_n1(mae_model: float, mae_naive_t1: float) -> float:
    if mae_naive_t1 == 0:
        raise ValueError("Naive MAE denominator cannot be zero.")
    return float(mae_model / mae_naive_t1)


def mase1(mae_oos: float, d_mase_1: float) -> float:
    if d_mase_1 == 0:
        raise ValueError("D_MASE_1 denominator cannot be zero.")
    return float(mae_oos / d_mase_1)


def rmsse1(rmse_oos: float, d_rmsse_1: float) -> float:
    if d_rmsse_1 == 0:
        raise ValueError("D_RMSSE_1 denominator cannot be zero.")
    return float(rmse_oos / np.sqrt(d_rmsse_1))


def r2_score_d35(y_true, y_pred) -> float:
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    ss_res = float(np.sum((y_true - y_pred) ** 2))
    ss_tot = float(np.sum((y_true - np.mean(y_true)) ** 2))
    if ss_tot == 0:
        raise ValueError("R2 is undefined when y_true has zero variance.")
    return 1.0 - (ss_res / ss_tot)


def conditional_shock_metrics(y_true, y_pred, shock_mask) -> dict[str, float | int]:
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    shock_mask = np.asarray(shock_mask, dtype=bool)
    if len(y_true) != len(y_pred) or len(y_true) != len(shock_mask):
        raise ValueError("y_true, y_pred, and shock_mask must have the same length.")
    if len(y_true) == 0:
        raise ValueError("Metric arrays cannot be empty.")

    abs_error = np.abs(y_true - y_pred)
    mae_global = float(np.mean(abs_error))
    n_shock = int(np.sum(shock_mask))
    n_nonshock = int(len(shock_mask) - n_shock)
    mae_shock = float(np.mean(abs_error[shock_mask])) if n_shock else float("nan")
    mae_nonshock = float(np.mean(abs_error[~shock_mask])) if n_nonshock else float("nan")
    delta_s = ((mae_shock - mae_global) / mae_global) * 100 if mae_global != 0 else float("nan")
    return {
        "MAE_global": mae_global,
        "MAE_shock": mae_shock,
        "MAE_nonshock": mae_nonshock,
        "n_shock": n_shock,
        "n_nonshock": n_nonshock,
        "Delta_s": float(delta_s),
    }
