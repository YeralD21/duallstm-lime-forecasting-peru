# BORRADOR — Nota de auditoría sobre v5 y v3

**Estado:** borrador pendiente de aprobación. No escrito en `DECISIONES_METODOLOGICAS.md`.
**Fecha:** 2026-10-25.
**Alcance:** solo lectura de `v5_rolling_origin_shocks/` y `v3_robustez_metodologica/`; ninguno de los dos se modifica.

Abreviaturas:
- **R5** = `v5_rolling_origin_shocks/scripts/run_rolling_origin.py`
- **R3** = `v3_robustez_metodologica/scripts/run_robustez.mjs`

---

## Parte 1 — Fugas en v5

### 1A. Hallazgo principal: fuga de validación en las LSTM (GC3 y GE) de las ventanas 2023 y 2024

| # | Afirmación | Evidencia |
|---|---|---|
| 1.1 | Las ventanas se definen como `(id, year, origin, target_year)`: A = `(2022, '2022-12', '2023')`, B = `(2023, '2023-12', '2024')`, C = `(2024, '2024-12', '2025')`. | R5:17 |
| 1.2 | GC3 y GE se reentrenan solo en las ventanas A y B; el comentario dice "Each window-year uses following year as validation". | R5:134-135 |
| 1.3 | El conjunto de validación de cada ventana son los meses cuyo año es `year + 1`. | R5:160 |
| 1.4 | En A, `year + 1` = 2023, que es el año objetivo (test) de A; en B, `year + 1` = 2024, el año objetivo de B. **La validación es el mismo año que el test.** | R5:17 + R5:160 |
| 1.5 | Esa validación controla EarlyStopping (`restore_best_weights=True`), ReduceLROnPlateau y ModelCheckpoint, todos sobre `val_loss`. | R5:176; `v2_reentrenamiento/src/training/callbacks_gc3_ge.py:22-37` |
| 1.6 | La aserción solo comprueba que haya 12 meses de validación y que el train termine en `year`; no comprueba que validación y test sean distintos. | R5:166 |
| 1.7 | **Consecuencia:** la época restaurada y la tasa de aprendizaje se eligieron con los mismos meses en que después se evaluó. Las métricas de GC3 y GE en A (2023) y B (2024) de `v5_rolling_origin_shocks/resultados/rolling_origin_metrics.csv`, `aggregated_2023_2025.csv` y `sensitivity_percentiles.csv` **no son pronósticos fuera de muestra**. | — |
| 1.8 | La ventana C (2025) no está afectada: reutiliza las predicciones oficiales v2. | R5:42-58 |
| 1.9 | **Sustitución:** el backtesting rodante recalcula 2023 y 2024 con validación = Y−1, verificada por `experimentos_backtesting_rodante/02_scripts/tests/test_fuga.py` (punto c). | — |

### 1B. Fuga leve de variables exógenas (pesos geográficos de NASA/INDECI)

| # | Afirmación | Evidencia |
|---|---|---|
| 1.10 | v5 toma las features exógenas del dataset oficial de v2. | R5:66 |
| 1.11 | Ese dataset agrega NASA e INDECI de provincia a escala nacional con pesos fijos = superficie media (`verde_actual_ha`) de 2016-01..2023-12. | `v2_reentrenamiento/src/features/pesos_geograficos.py:5-9, 87-95`; `v2_reentrenamiento/notebooks/fase2_features/00_pesos_geograficos.ipynb` celda 2; `02_fusion_dataset_maestro.ipynb` celda 6 |
| 1.12 | En la ventana A (test 2023), los pesos incluyen la superficie del propio año de test. En la ventana B (test 2024) no hay fuga por esta vía, porque los pesos terminan en 2023. No afecta a la variable objetivo, que no pasa por estos pesos. | 1.10 + 1.11 |
| 1.13 | **Magnitud medida** (solo lectura, pesos recalculados con fin 2016..2022 frente a los oficiales 2016..2023): en **Sutil**, diferencia relativa de INDECI-personas afectadas ≤ 1.4 % y temperatura (T2M) ≤ 0.03 °C; en **Dulce**, INDECI hasta **15.3 %** y T2M hasta **0.64 °C** (con pesos 2016–2017). Con pesos 2016–2022 (lo relevante para 2023): Sutil 0.4 % / 0.01 °C; Dulce 0.4 % / 0.04 °C. | Cálculo de la Fase A (`09_reportes/reporte_fase_A.md`, plan A2-f); recalculable con `experimentos_backtesting_rodante/03_ventanas/pesos_geograficos_por_ventana.csv` |
| 1.14 | **Sustitución:** el backtesting rodante recalcula los pesos por ventana con `VentanaTrain(2016-01, diciembre de Y−2)` (D-BR3), verificado por `tests/test_fuga.py` (punto f). | — |

## Parte 2 — Diferencias de protocolo sin fuga hacia el test

### v5

| # | Afirmación | Evidencia |
|---|---|---|
| 2.1 | SARIMA se ajusta con toda la historia de producción hasta el origen, desde 2016-01, incluido el año que v2 reserva como validación. El SARIMA oficial se ajusta en 2016-07..fin de train y solo añade la validación como estado. | R5:71-72, 97; `v2_reentrenamiento/auditorias/evaluar_test_sarima_rolling.py:107-125` |
| 2.2 | Ridge y ElasticNet se ajustan con los objetivos hasta el origen (incluye el año de validación) y con α/l1 congelados de v3. | R5:19, 106 |
| 2.3 | XGB-37 se ajusta con los objetivos hasta el origen y con un StandardScaler ajustado hasta el origen. El oficial ajusta scaler y modelo solo con train. | R5:118-129; `v2_reentrenamiento/src/features/escalado.py:26, 55-63` |
| 2.4 | En la ventana C, los modelos deterministas y regularizados se reajustan con todos los datos anteriores a 2025. | R5:67-68 (comentario) |
| 2.5 | Δs se calcula como MAE_normal − MAE_shock, en toneladas y con el signo invertido respecto a la definición oficial v2 ((MAE_shock − MAE_global)/MAE_global × 100). | R5:215; `v2_reentrenamiento/DECISIONES_METODOLOGICAS.md:820-824` |
| 2.6 | (Los pesos geográficos se trasladaron a la Parte 1B.) | — |
| 2.7 | El umbral de shock se calcula con la historia hasta el origen (coincide con el backtesting rodante). | R5:186-187 |

### v3

| # | Afirmación | Evidencia |
|---|---|---|
| 3.1 | Ridge y ElasticNet están implementados en Node.js: Ridge por ecuaciones normales con el intercepto sin penalizar; ElasticNet por descenso coordenado propio (máximo 4000 iteraciones, parada si Σ\|cambio\| < 1e-7). | R3:64-68, 71-76 |
| 3.2 | La estandarización usa media y desviación poblacional del conjunto de ajuste. | R3:59-62 |
| 3.3 | Los hiperparámetros se eligen por MAE en VAL 2024 sobre la rejilla α ∈ {0.001, 0.01, 0.1, 1, 10, 100} × l1 ∈ {0.2, 0.5, 0.8}. | R3:137; `v3_robustez_metodologica/configs/config_robustez.json` |
| 3.4 | **El modelo final se reajusta con train + validación** (objetivos hasta 2024-12) y con un nuevo estandarizador; la fuente queda registrada como `v3_tabular_37_features_trainval`. XGB-37, GC3 y GE oficiales se ajustan solo con train. | R3:100, 137, 143 |
| 3.5 | La columna `Delta_s` de `resultados_baselines_clasicos.csv` es MAE_shock − MAE_normal en toneladas, no la Δs oficial v2 (%). | R3:78-82 |
| 3.6 | **Reproducción:** el MAE registrado de ElasticNet se reproduce a precisión de máquina (Sutil 3117.6377; Dulce 39.6962). Con ajuste final solo en train, igual que los demás modelos oficiales, da 3222.889 (Sutil, +105.25 t) y 49.346 (Dulce, +9.65 t). La comparación de v3 daba a Ridge y ElasticNet un año más de datos de estimación. | `experimentos_backtesting_rodante/06_metricas/reproducibilidad/elasticnet_reproduccion.json` |

## Resumen

v5 contiene una fuga real de validación hacia el test en GC3/GE (ventanas 2023 y 2024), que es el hallazgo principal, y una fuga leve de variables exógenas por los pesos geográficos (despreciable en Sutil; hasta 15 % en INDECI-Dulce para ventanas tempranas). Sus demás diferencias, y todas las de v3, son de protocolo: cambian la cantidad de datos de estimación o la definición de Δs, pero no usan el test para entrenar ni para elegir. Ningún resultado de v5 (A y B) ni de Ridge/ElasticNet de v3 se mezcla con el backtesting rodante.
