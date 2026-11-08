"""Official GC2/XGBoost v2 configuration constants."""

from __future__ import annotations

from dataclasses import asdict, dataclass


OFFICIAL_GC2_CULTIVARS = ("sutil", "dulce")
OFFICIAL_GC2_SEEDS = tuple(range(10))


@dataclass(frozen=True)
class XGBoostGC2Config:
    objective: str = "reg:squarederror"
    eval_metric: str = "mae"
    booster: str = "gbtree"
    max_depth: int = 2
    min_child_weight: int = 1
    learning_rate: float = 0.05
    n_estimators: int = 200
    subsample: float = 0.8
    colsample_bytree: float = 0.8
    reg_alpha: float = 0.0
    reg_lambda: float = 1.0
    gamma: float = 0.0
    tree_method: str = "hist"
    n_jobs: int = 1
    early_stopping: bool = False
    hpo_performed: bool = False
    cv_performed: bool = False
    best_seed_selection: bool = False

    def xgb_params(self, seed: int) -> dict[str, object]:
        return {
            "objective": self.objective,
            "eval_metric": self.eval_metric,
            "booster": self.booster,
            "max_depth": self.max_depth,
            "min_child_weight": self.min_child_weight,
            "learning_rate": self.learning_rate,
            "n_estimators": self.n_estimators,
            "subsample": self.subsample,
            "colsample_bytree": self.colsample_bytree,
            "reg_alpha": self.reg_alpha,
            "reg_lambda": self.reg_lambda,
            "gamma": self.gamma,
            "tree_method": self.tree_method,
            "n_jobs": self.n_jobs,
            "random_state": seed,
        }

    def as_dict(self) -> dict[str, object]:
        return asdict(self)


OFFICIAL_GC2_XGB_CONFIG = XGBoostGC2Config()


def validate_gc2_seeds(seeds: tuple[int, ...] = OFFICIAL_GC2_SEEDS) -> None:
    if seeds != tuple(range(10)):
        raise ValueError(f"Official GC2 seeds must be 0..9, got {seeds}.")


def validate_gc2_config(config: XGBoostGC2Config = OFFICIAL_GC2_XGB_CONFIG) -> None:
    expected = XGBoostGC2Config()
    if config != expected:
        raise ValueError(f"GC2 official config mismatch: {config} != {expected}")
