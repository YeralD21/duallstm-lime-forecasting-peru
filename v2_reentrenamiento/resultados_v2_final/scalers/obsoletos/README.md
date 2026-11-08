# Scalers obsoletos — NO USAR

Movidos aquí el 2026-09-07 durante la regeneración de Fase 2 v2
(decisiones D14–D21). Se conservan solo para auditoría; **ningún modelo
debe cargarlos**.

| Archivo | n_features_in_ | Por qué quedó obsoleto |
|---|---:|---|
| `scaler_{sutil,dulce}.joblib` | 28 | Esquema anterior a `t_index`. Nunca correspondió a los CSV publicados. |
| `scaler_{sutil,dulce}_v2b_tindex.joblib` | 29 | Esquema con ponderación contemporánea, `precio_chacra_kg` y `n_provincias`, y exógenas contemporáneas. |

**Scalers vigentes:** `../scaler_{sutil,dulce}_v2c.joblib` — 44 features,
`n_samples_seen_ = 90`, ajustados solo sobre TRAIN 2016-07..2023-12.

Estado previo con hashes: `../../pesos/REGISTRO_PRE_REGENERACION.json`.
