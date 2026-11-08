"""Explicit GC2/XGBoost feature definition for v2."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from v2_reentrenamiento.src.models.features_gc3_ge import (
    FORBIDDEN_FEATURE_FRAGMENTS,
    INDECI_BASE,
    LAGS,
    NASA_BASE,
    NLP_LAGGED,
    TEMPORAL_FEATURES,
    _lagged,
    rama_a_features,
)


Cultivar = Literal["sutil", "dulce"]

FORBIDDEN_EXACT = (
    "precio_chacra_kg",
    "n_provincias",
    "total_afectados",
)
FORBIDDEN_PATTERN_FRAGMENTS = (
    "lag2",
    "roll",
    "rolling",
    "mean",
    "std",
)
FORBIDDEN_CONTEMPORARY_EXOGENOUS = NASA_BASE + INDECI_BASE + ("avg_sentiment", "n_noticias")


@dataclass(frozen=True)
class GC2FeatureSpec:
    cultivar: Cultivar
    predictors: tuple[str, ...]
    target: str


def gc2_predictors(cultivar: Cultivar) -> tuple[str, ...]:
    if cultivar not in ("sutil", "dulce"):
        raise ValueError(f"Unsupported cultivar: {cultivar}")
    return (
        rama_a_features(cultivar)
        + TEMPORAL_FEATURES
        + _lagged(NASA_BASE)
        + _lagged(INDECI_BASE)
    )


def build_gc2_feature_spec(cultivar: Cultivar) -> GC2FeatureSpec:
    spec = GC2FeatureSpec(
        cultivar=cultivar,
        predictors=gc2_predictors(cultivar),
        target=f"produccion_t_{cultivar}",
    )
    validate_gc2_feature_spec(spec)
    return spec


def validate_gc2_feature_spec(spec: GC2FeatureSpec) -> None:
    if spec.cultivar not in ("sutil", "dulce"):
        raise ValueError(f"Unsupported cultivar: {spec.cultivar}")
    if len(spec.predictors) != 37:
        raise ValueError(f"GC2 must have 37 predictors, got {len(spec.predictors)}.")
    duplicates = sorted({name for name in spec.predictors if spec.predictors.count(name) > 1})
    if duplicates:
        raise ValueError(f"Duplicate predictors are not allowed: {duplicates}")

    forbidden_hits: list[str] = []
    for feature in spec.predictors:
        if feature in FORBIDDEN_EXACT:
            forbidden_hits.append(feature)
        for fragment in FORBIDDEN_FEATURE_FRAGMENTS + FORBIDDEN_PATTERN_FRAGMENTS:
            if fragment in feature:
                forbidden_hits.append(feature)
        if feature in FORBIDDEN_CONTEMPORARY_EXOGENOUS:
            forbidden_hits.append(feature)
        if feature in NLP_LAGGED:
            forbidden_hits.append(feature)
    if forbidden_hits:
        raise ValueError(f"Forbidden GC2 predictors present: {sorted(set(forbidden_hits))}")


def validate_gc2_columns_available(spec: GC2FeatureSpec, columns: set[str]) -> None:
    missing = [name for name in spec.predictors + (spec.target,) if name not in columns]
    if missing:
        raise ValueError(f"Missing required GC2 columns: {missing}")
