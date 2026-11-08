"""Centralized determinism setup for v2 neural models."""

from __future__ import annotations

import os
import random
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class DeterminismReport:
    seed: int
    pythonhashseed: str | None
    tf_enable_onednn_opts: str | None
    tf_deterministic_ops: str | None
    tensorflow_previously_loaded: bool
    keras_set_random_seed_used: bool
    enable_op_determinism_used: bool


def configure_determinism(
    seed: int,
    *,
    set_onednn_conservative: bool = True,
    set_tf_deterministic_ops: bool = True,
) -> DeterminismReport:
    """Configure deterministic behavior as far as the active environment allows.

    Environment variables are set before TensorFlow is imported by this
    function. If TensorFlow was imported earlier by the caller, the report flags
    that fact because some variables may no longer have full effect.
    """

    tensorflow_previously_loaded = "tensorflow" in sys.modules

    os.environ["PYTHONHASHSEED"] = str(seed)
    if set_onednn_conservative:
        os.environ.setdefault("TF_ENABLE_ONEDNN_OPTS", "0")
    if set_tf_deterministic_ops:
        os.environ.setdefault("TF_DETERMINISTIC_OPS", "1")

    random.seed(seed)

    import numpy as np
    import tensorflow as tf
    from tensorflow import keras

    np.random.seed(seed)
    tf.random.set_seed(seed)

    keras_seed_used = False
    if hasattr(keras.utils, "set_random_seed"):
        keras.utils.set_random_seed(seed)
        keras_seed_used = True

    op_determinism_used = False
    enable_op_determinism = getattr(tf.config.experimental, "enable_op_determinism", None)
    if enable_op_determinism is not None:
        enable_op_determinism()
        op_determinism_used = True

    return DeterminismReport(
        seed=seed,
        pythonhashseed=os.environ.get("PYTHONHASHSEED"),
        tf_enable_onednn_opts=os.environ.get("TF_ENABLE_ONEDNN_OPTS"),
        tf_deterministic_ops=os.environ.get("TF_DETERMINISTIC_OPS"),
        tensorflow_previously_loaded=tensorflow_previously_loaded,
        keras_set_random_seed_used=keras_seed_used,
        enable_op_determinism_used=op_determinism_used,
    )
