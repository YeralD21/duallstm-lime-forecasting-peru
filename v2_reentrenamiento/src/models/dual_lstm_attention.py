"""Official GC3/GE DualLSTM + Bahdanau Attention architecture.

This module only defines and compiles models. It does not train, evaluate, or
choose hyperparameters.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


ModelName = Literal["GC3", "GE"]

LOOKBACK = 6
LSTM_UNITS = 16
ATTENTION_UNITS = 16
DENSE_UNITS = (16, 8)
DROPOUT = 0.20
LEARNING_RATE = 0.001
LOSS = "mse"
METRICS = ("mae",)

EXPECTED_PARAMS = {
    "GC3": 6273,
    "GE": 6657,
}


@dataclass(frozen=True)
class ModelDimensions:
    """Input dimensions for one official GC3/GE model."""

    model_name: ModelName
    n_features_a: int
    n_features_b: int

    @property
    def total_features(self) -> int:
        return self.n_features_a + self.n_features_b


class BahdanauAttention(keras.layers.Layer):
    """Simplified additive temporal Bahdanau attention.

    Parameters match the audited v1 implementation: Dense projections have no
    bias, scores are normalized along the temporal axis, and the context vector
    is the weighted sum of LSTM states.
    """

    def __init__(self, units: int, **kwargs):
        super().__init__(**kwargs)
        self.units = units
        self.W_query = layers.Dense(units, use_bias=False, name="W_query")
        self.W_values = layers.Dense(units, use_bias=False, name="W_values")
        self.V = layers.Dense(1, use_bias=False, name="V")

    def call(self, query, values):
        q_expanded = tf.expand_dims(self.W_query(query), axis=1)
        energy = self.V(tf.nn.tanh(self.W_values(values) + q_expanded))
        alpha = tf.nn.softmax(energy, axis=1)
        context = tf.reduce_sum(alpha * values, axis=1)
        return context

    def get_config(self):
        config = super().get_config()
        config.update({"units": self.units})
        return config


def _validate_dimensions(dimensions: ModelDimensions) -> None:
    if dimensions.n_features_a != 4:
        raise ValueError(f"Rama A must have 4 features, got {dimensions.n_features_a}.")
    if dimensions.model_name == "GC3" and dimensions.n_features_b != 33:
        raise ValueError(f"GC3 Rama B must have 33 features, got {dimensions.n_features_b}.")
    if dimensions.model_name == "GE" and dimensions.n_features_b != 39:
        raise ValueError(f"GE Rama B must have 39 features, got {dimensions.n_features_b}.")


def build_gc3_ge_model(
    model_name: ModelName,
    n_features_a: int,
    n_features_b: int,
    *,
    compile_model: bool = True,
) -> keras.Model:
    """Build the official v2 GC3/GE model.

    The only structural difference between GC3 and GE is `n_features_b`.
    """

    dimensions = ModelDimensions(model_name, n_features_a, n_features_b)
    _validate_dimensions(dimensions)

    input_a = keras.Input(shape=(LOOKBACK, n_features_a), name="rama_a")
    hidden_a = layers.LSTM(
        LSTM_UNITS,
        return_sequences=True,
        name="lstm_a",
    )(input_a)
    query_a = hidden_a[:, -1, :]
    context_a = BahdanauAttention(ATTENTION_UNITS, name="attention_a")(query_a, hidden_a)

    input_b = keras.Input(shape=(LOOKBACK, n_features_b), name="rama_b")
    hidden_b = layers.LSTM(
        LSTM_UNITS,
        return_sequences=True,
        name="lstm_b",
    )(input_b)
    query_b = hidden_b[:, -1, :]
    context_b = BahdanauAttention(ATTENTION_UNITS, name="attention_b")(query_b, hidden_b)

    merged = layers.Concatenate(name="concatenate")([context_a, context_b])
    x = layers.Dense(DENSE_UNITS[0], activation="relu", name="dense_16")(merged)
    x = layers.Dropout(DROPOUT, name="dropout_020")(x)
    x = layers.Dense(DENSE_UNITS[1], activation="relu", name="dense_8")(x)
    output = layers.Dense(1, name="output")(x)

    model = keras.Model(
        inputs=[input_a, input_b],
        outputs=output,
        name=f"{model_name}_DualLSTM_BahdanauAttention_v2",
    )

    if compile_model:
        model.compile(
            optimizer=keras.optimizers.Adam(learning_rate=LEARNING_RATE),
            loss=LOSS,
            metrics=list(METRICS),
        )

    expected = EXPECTED_PARAMS[model_name]
    obtained = model.count_params()
    if obtained != expected:
        raise ValueError(
            f"{model_name} parameter count mismatch: expected {expected}, got {obtained}."
        )

    return model


def expected_parameter_count(n_features_a: int, n_features_b: int) -> int:
    """Mathematical parameter count for the official architecture."""

    def lstm_params(input_dim: int, units: int) -> int:
        return 4 * units * (input_dim + units + 1)

    def attention_params(lstm_units: int, attention_units: int) -> int:
        return (2 * lstm_units * attention_units) + attention_units

    dense_16 = (2 * LSTM_UNITS * DENSE_UNITS[0]) + DENSE_UNITS[0]
    dense_8 = (DENSE_UNITS[0] * DENSE_UNITS[1]) + DENSE_UNITS[1]
    output = DENSE_UNITS[1] + 1
    return (
        lstm_params(n_features_a, LSTM_UNITS)
        + lstm_params(n_features_b, LSTM_UNITS)
        + attention_params(LSTM_UNITS, ATTENTION_UNITS)
        + attention_params(LSTM_UNITS, ATTENTION_UNITS)
        + dense_16
        + dense_8
        + output
    )
