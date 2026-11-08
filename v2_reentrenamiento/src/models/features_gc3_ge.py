"""Explicit GC3/GE feature definitions for v2."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


Cultivar = Literal["sutil", "dulce"]
ModelName = Literal["GC3", "GE"]

LAGS = (1, 3, 6)
NASA_BASE = ("T2M", "T2M_MAX", "WS2M", "PRECTOTCORR", "RH2M")
INDECI_BASE = (
    "num_emergencias",
    "personas_afectadas",
    "personas_damnificadas",
    "hectareas_cultivo_perdidas",
    "hectareas_cultivo_afectadas",
)
NLP_LAGGED = (
    "avg_sentiment_lag1",
    "avg_sentiment_lag3",
    "avg_sentiment_lag6",
    "n_noticias_lag1",
    "n_noticias_lag3",
    "n_noticias_lag6",
)
TEMPORAL_FEATURES = ("mes_sin", "mes_cos", "t_index")

FORBIDDEN_FEATURE_FRAGMENTS = (
    "precio_chacra_kg",
    "n_provincias",
    "total_afectados",
)

FORBIDDEN_CONTEMPORARY_EXOGENOUS = (
    "T2M",
    "T2M_MAX",
    "WS2M",
    "PRECTOTCORR",
    "RH2M",
    "num_emergencias",
    "personas_afectadas",
    "personas_damnificadas",
    "hectareas_cultivo_perdidas",
    "hectareas_cultivo_afectadas",
    "avg_sentiment",
    "n_noticias",
)


@dataclass(frozen=True)
class FeatureSpec:
    cultivar: Cultivar
    model_name: ModelName
    rama_a: tuple[str, ...]
    rama_b: tuple[str, ...]
    target: str

    @property
    def all_inputs(self) -> tuple[str, ...]:
        return self.rama_a + self.rama_b


def _lagged(names: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(f"{name}_lag{lag}" for name in names for lag in LAGS)


def rama_a_features(cultivar: Cultivar) -> tuple[str, ...]:
    return (
        f"produccion_t_{cultivar}",
        f"produccion_t_{cultivar}_lag1",
        f"produccion_t_{cultivar}_lag3",
        f"produccion_t_{cultivar}_lag6",
    )


def rama_b_gc3_features() -> tuple[str, ...]:
    return TEMPORAL_FEATURES + _lagged(NASA_BASE) + _lagged(INDECI_BASE)


def rama_b_ge_features() -> tuple[str, ...]:
    return rama_b_gc3_features() + NLP_LAGGED


def build_feature_spec(cultivar: Cultivar, model_name: ModelName) -> FeatureSpec:
    if cultivar not in ("sutil", "dulce"):
        raise ValueError(f"Unsupported cultivar: {cultivar}")
    if model_name not in ("GC3", "GE"):
        raise ValueError(f"Unsupported model: {model_name}")

    rama_a = rama_a_features(cultivar)
    rama_b = rama_b_gc3_features() if model_name == "GC3" else rama_b_ge_features()
    spec = FeatureSpec(
        cultivar=cultivar,
        model_name=model_name,
        rama_a=rama_a,
        rama_b=rama_b,
        target=f"produccion_t_{cultivar}",
    )
    validate_feature_spec(spec)
    return spec


def validate_feature_spec(spec: FeatureSpec) -> None:
    if len(spec.rama_a) != 4:
        raise ValueError(f"Rama A must have 4 features, got {len(spec.rama_a)}.")
    if spec.model_name == "GC3" and len(spec.rama_b) != 33:
        raise ValueError(f"GC3 Rama B must have 33 features, got {len(spec.rama_b)}.")
    if spec.model_name == "GE" and len(spec.rama_b) != 39:
        raise ValueError(f"GE Rama B must have 39 features, got {len(spec.rama_b)}.")
    expected_total = 37 if spec.model_name == "GC3" else 43
    if len(spec.all_inputs) != expected_total:
        raise ValueError(
            f"{spec.model_name} must have {expected_total} inputs, got {len(spec.all_inputs)}."
        )

    duplicates = sorted({name for name in spec.all_inputs if spec.all_inputs.count(name) > 1})
    if duplicates:
        raise ValueError(f"Duplicate features are not allowed: {duplicates}")

    for feature in spec.all_inputs:
        for forbidden in FORBIDDEN_FEATURE_FRAGMENTS:
            if forbidden in feature:
                raise ValueError(f"Forbidden feature present: {feature}")

    allowed_unlagged = set(TEMPORAL_FEATURES) | set(spec.rama_a)
    for feature in spec.all_inputs:
        if feature in allowed_unlagged or "_lag" in feature:
            continue
        if feature in FORBIDDEN_CONTEMPORARY_EXOGENOUS:
            raise ValueError(f"Contemporary exogenous feature present: {feature}")


def validate_columns_available(spec: FeatureSpec, columns: set[str]) -> None:
    missing = [feature for feature in spec.all_inputs + (spec.target,) if feature not in columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
