"""Official callbacks for GC3/GE training."""

from __future__ import annotations

from pathlib import Path

from .config_gc3_ge import OFFICIAL_TRAINING_CONFIG, TrainingConfig


def build_callbacks(run_dir: Path, config: TrainingConfig = OFFICIAL_TRAINING_CONFIG):
    """Build callbacks for one future run.

    The checkpoint path is scoped to the run directory so different seeds cannot
    overwrite each other.
    """

    from tensorflow.keras import callbacks

    run_dir.mkdir(parents=True, exist_ok=True)
    checkpoint_path = run_dir / "checkpoint_best.keras"
    return [
        callbacks.EarlyStopping(
            monitor=config.early_stopping_monitor,
            patience=config.early_stopping_patience,
            restore_best_weights=config.early_stopping_restore_best_weights,
        ),
        callbacks.ReduceLROnPlateau(
            monitor=config.reduce_lr_monitor,
            factor=config.reduce_lr_factor,
            patience=config.reduce_lr_patience,
            min_lr=config.reduce_lr_min_lr,
        ),
        callbacks.ModelCheckpoint(
            filepath=str(checkpoint_path),
            monitor=config.early_stopping_monitor,
            save_best_only=True,
        ),
    ]
