"""Official GC3/GE training configuration constants."""

from __future__ import annotations

from dataclasses import dataclass


OFFICIAL_SEEDS = tuple(range(10))


@dataclass(frozen=True)
class TrainingConfig:
    lookback: int = 6
    batch_size: int = 8
    max_epochs: int = 300
    learning_rate: float = 0.001
    loss: str = "mse"
    metric: str = "mae"
    shuffle: bool = False
    early_stopping_monitor: str = "val_loss"
    early_stopping_patience: int = 15
    early_stopping_restore_best_weights: bool = True
    reduce_lr_monitor: str = "val_loss"
    reduce_lr_factor: float = 0.5
    reduce_lr_patience: int = 8
    reduce_lr_min_lr: float = 1e-6


OFFICIAL_TRAINING_CONFIG = TrainingConfig()


def validate_official_seeds(seeds: tuple[int, ...] = OFFICIAL_SEEDS) -> None:
    if seeds != tuple(range(10)):
        raise ValueError(f"Official seeds must be 0..9, got {seeds}.")
