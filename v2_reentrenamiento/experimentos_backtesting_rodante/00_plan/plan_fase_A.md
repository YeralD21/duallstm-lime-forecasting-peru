# Plan — Fase A (sin ejecutar nada)

**Estado:** APROBADO con enmiendas (ver la sección siguiente). Fase B ejecutada; Fase C pendiente de aprobación.

## Enmiendas aprobadas tras la Fase A

| ID | Decisión aprobada |
|---|---|
| DA1, DA3, DA5, DA7 | Aprobadas tal como se propusieron |
| DA2 | Mínimo de 36 meses, más un análisis de sensibilidad preregistrado que repite las conclusiones solo con las ventanas 2023–2025 |
| DA4 (revisada tras la Fase B) | Ridge y ElasticNet **reeligen α (y l1_ratio) en cada ventana** por MAE en la validación de esa ventana (año Y−1), sobre la rejilla de v3, y el ajuste final es **solo con el train**. Los valores de v3 se conservan únicamente como control de la ventana 2025 (D-BR2) |
| DA10 (tras la Fase B) | SARIMA-sel = opción (b): top-5 por AIC en train y elección por MAE de validación a 1 paso; se registra la posición en AIC del orden elegido (D-BR10) |
| DA6 | Sobreajuste si MAE_val/MAE_train > 2.0; "no supera al Naive" como señal aparte; advertencia de nivel en la validación de Sutil |
| DA8 | Promedio mensual del error absoluto entre las 10 semillas; bootstrap y DM sobre ese promedio; dispersión entre semillas aparte |
| DA9 | Se añade SARIMA-sel (rejilla con AIC en train y elección por validación, repetida en cada ventana) además del SARIMA congelado; regla en DA10 |
| P0, robustez | Aprobadas |

**Consecuencia de DA9:** hay 118 combinaciones viables (59 por cultivo) y 42 "no aplica" (`03_ventanas/ventanas_viabilidad.csv`).

---
**Fecha:** 2026-10-25.
**Rutas:** relativas a la raíz del repo salvo indicación. `src/` = `v2_reentrenamiento/src/`.
**Celdas de notebook:** índice base 0, incluidas las celdas markdown.

---

## A0. Viabilidad de la opción (a): envoltorio sobre `src/` sin tocarlo

**Resultado: viable, con reimplementación de tres piezas en `02_scripts/lib/`.**

Hay fechas escritas a mano en estos módulos, que por tanto **no** se pueden reutilizar tal cual para otras ventanas:

| Módulo | Líneas | Qué tiene fijo |
|---|---|---|
| `src/training/sequences_gc3_ge.py` | 88-90, 104-119, 131-137 | máscaras `year<=2023 / ==2024 / ==2025`, 114 filas, 84 secuencias, primera fecha 2016-07 |
| `src/features/escalado.py` | 26, 55-63 | `RANGOS` train 2016-07..2023-12, val 2024, test 2025; `n_samples_seen_ == 90` |
| `src/training/tabular_gc2_xgboost.py` | 38-66, 148-163 | carga solo filas ≤2024 y valida fechas fijas |
| `src/training/official_runner_gc3_ge.py` | 114, 131, 147-150, 185-187, 235-251, 473 | runner completo con fechas fijas |
| `src/training/official_runner_gc2_xgboost.py` | 330-335 | controles con fechas fijas |
| `src/evaluation/shocks_d35.py` | 14-15 | meses de shock 2025 congelados |

Estos módulos **sí** se reutilizan sin cambios, importados en solo lectura con SHA-256 verificado:

| Módulo | Uso |
|---|---|
| `src/models/dual_lstm_attention.py` (`build_gc3_ge_model`, `BahdanauAttention`, `EXPECTED_PARAMS`) | arquitectura GC3/GE |
| `src/training/config_gc3_ge.py` (`TrainingConfig`, `OFFICIAL_SEEDS`) | hiperparámetros congelados de entrenamiento |
| `src/training/callbacks_gc3_ge.py` (`build_callbacks`) | EarlyStopping, ReduceLROnPlateau, ModelCheckpoint |
| `src/training/determinism.py` (`configure_determinism`) | determinismo |
| `src/models/features_gc3_ge.py` (`build_feature_spec`) | columnas de las ramas A y B |
| `src/models/features_gc2_xgboost.py` (`gc2_predictors`) | 37 predictores de XGB |
| `src/training/config_gc2_xgboost.py` (`OFFICIAL_GC2_XGB_CONFIG`) | hiperparámetros de XGB |
| `src/features/pesos_geograficos.py` (`PesosGeograficos`, `VentanaTrain`) | pesos por ventana; `VentanaTrain` es parametrizable (l. 26-47) |
| `src/features/agregacion_espacial.py` (`AgregadorEspacial`) | agregación provincia → nacional |
| `src/features/features_temporales.py` (`FeaturesTemporales`) | lags 1/3/6, `mes_sin`/`mes_cos`, `t_index` calendario |
| `src/evaluation/metrics_d35.py` | MAE, RMSE, R² |

**Lo que se reimplementa en `lib/`:** (1) partición de secuencias por ventana (copiando el bucle de `sequences_gc3_ge.py:71-80`, que incluye la guarda anti-fuga `context_dates < target_date`); (2) escalador ajustado solo en train por ventana; (3) partición tabular X_t → y_{t+1} por ventana.

**Prueba de equivalencia obligatoria (Fase B):** con la ventana Y=2025, el envoltorio debe reproducir exactamente:
- las matrices de secuencias de `build_sequences` oficial (igualdad elemento a elemento);
- los parámetros de `resultados_v2_final/scalers/scaler_{c}_v2c.joblib`;
- los pesos de `resultados_v2_final/pesos/pesos_geograficos_train.csv`.

Si falla, se detiene la corrida y se pasa a la opción (b).

---

## A1. Ventanas

Origen = diciembre de Y−1; test = enero a diciembre de Y; Y = 2018..2025.

**Esquema de partición propuesto (decisión DA1, opción a): copiar el protocolo oficial v2 desplazado.**
- Train: hasta diciembre de Y−2.
- Validación: año Y−1 (12 meses).
- Test: año Y.

Con Y=2025 coincide exactamente con el split oficial (train ≤2023, val 2024, test 2025; `DECISIONES_METODOLOGICAS.md:64-110`).

| Y | Origen | Train LSTM (objetivos) | n sec. LSTM | Train tabular XGB/Ridge/EN (objetivos) | n pares | Train SARIMA | n obs | Val | Test |
|---|---|---|---:|---|---:|---|---:|---|---|
| 2018 | 2017-12 | — | 0 | 2016-08..2016-12 | 5 | 2016-07..2016-12 | 6 | 2017 | 2018 |
| 2019 | 2018-12 | 2017-01..2017-12 | 12 | 2016-08..2017-12 | 17 | 2016-07..2017-12 | 18 | 2018 | 2019 |
| 2020 | 2019-12 | 2017-01..2018-12 | 24 | 2016-08..2018-12 | 29 | 2016-07..2018-12 | 30 | 2019 | 2020 |
| 2021 | 2020-12 | 2017-01..2019-12 | 36 | 2016-08..2019-12 | 41 | 2016-07..2019-12 | 42 | 2020 | 2021 |
| 2022 | 2021-12 | 2017-01..2020-12 | 48 | 2016-08..2020-12 | 53 | 2016-07..2020-12 | 54 | 2021 | 2022 |
| 2023 | 2022-12 | 2017-01..2021-12 | 60 | 2016-08..2021-12 | 65 | 2016-07..2021-12 | 66 | 2022 | 2023 |
| 2024 | 2023-12 | 2017-01..2022-12 | 72 | 2016-08..2022-12 | 77 | 2016-07..2022-12 | 78 | 2023 | 2024 |
| 2025 | 2024-12 | 2017-01..2023-12 | 84 | 2016-08..2023-12 | 89 | 2016-07..2023-12 | 90 | 2024 | 2025 |

**Por qué los trenes empiezan en esas fechas:**
- Las features empiezan en 2016-07 porque se eliminan las filas sin lag de 6 meses (`features_temporales.py:16`; `DECISIONES:96-100`).
- La LSTM necesita lookback 6 sobre esas filas, así que su primer objetivo es 2017-01 (`official_runner_gc3_ge.py:235-236`).
- XGB empareja X_t con y_{t+1}, así que su primer par es 2016-07 → 2016-08 (`DECISIONES:1320-1335`).
- SARIMA usa 2016-07..origen de train, igual que en GC1 (D47, `DECISIONES:1475-1484`).

**Uso de la validación por modelo:**

| Modelo | Uso de la validación |
|---|---|
| GC3/GE | early stopping y ReduceLROnPlateau sobre `val_loss` (`config_gc3_ge.py:20-26`) |
| SARIMA | se ajusta en train; la validación se incorpora como estado con `append(refit=False)` (D48) |
| XGB, Ridge, ElasticNet | se ajustan solo en train; la validación solo se reporta (XGB oficial: `official_runner_gc2_xgboost.py:330-335`) |
| Naive, Seasonal Naive, Chronos | sin ajuste; usan la historia observada hasta t−1 |

**Mínimo de train propuesto (decisión DA2): 36 meses, igual para todos los modelos entrenados.**
- Justificación: 3 ciclos estacionales completos.
- Para SARIMA con D=1 y m=12 se pierden 13 observaciones por diferenciación (`02b` celda 7, `D_TOTAL = 1+1·12`). Con P=1 estacional hace falta otro ciclo de 12 para tener residuos útiles. Con 36 meses queda al menos un ciclo efectivo.
- Para las LSTM (6 273 / 6 657 parámetros) 36 secuencias ya es muy poco, y se declarará como limitación.

**Combinaciones "no aplica" con mínimo 36:** SARIMA, XGB-37, Ridge, ElasticNet, GC3, GE (y XGB-43) en Y=2018, 2019 y 2020, para ambos cultivos. Son **36 combinaciones**: 6 modelos × 3 ventanas × 2 cultivos.

**Combinaciones viables con mínimo 36:**

| Modelo | Ventanas por cultivo | Total (2 cultivos) |
|---|---|---:|
| Naive, Seasonal Naive, Chronos | 8 (2018–2025) | 48 |
| SARIMA, XGB-37, Ridge, ElasticNet, GC3, GE | 5 (2021–2025) | 60 |
| **Total del ranking principal** | | **108** |
| XGB-43 (exploratorio) | 5 | 10 |

El **ranking principal se calcula sobre las ventanas comunes 2021–2025**. Naive, Seasonal Naive y Chronos se reportan además en 2018–2025 como tabla descriptiva aparte.

**Meses de shock con P75, umbral calculado con |Δy/y| desde 2016-01 hasta el origen:**

| Y | P75 Sutil | n Sutil | Meses Sutil | P75 Dulce | n Dulce | Meses Dulce |
|---|---:|---:|---|---:|---:|---|
| 2018 | 24.7 % | 4 | 01, 07, 09, 12 | 27.6 % | 4 | 01, 02, 04, 11 |
| 2019 | 25.9 % | 3 | 01, 07, 08 | 29.2 % | 4 | 01, 02, 03, 11 |
| 2020 | 25.9 % | 3 | 07, 09, 12 | 31.1 % | 4 | 01, 02, 03, 11 |
| 2021 | 25.9 % | **0** (no informativa) | — | 33.8 % | 3 | 01, 02, 03 |
| 2022 | 23.9 % | 3 | 01, 06, 12 | 33.8 % | 3 | 01, 02, 03 |
| 2023 | 23.9 % | 4 | 08, 09, 11, 12 | 33.8 % | 2 | 02, 03 |
| 2024 | 24.1 % | **0** (no informativa) | — | 32.0 % | 4 | 01, 02, 03, 10 |
| 2025 | 23.2 % | 3 | 01, 07, 11 | 32.8 % | 3 | 01, 02, 03 |

**Totales de meses de shock:**

| Conjunto de ventanas | Sutil | Dulce |
|---|---:|---:|
| Ventanas del ranking (2021–2025) | **10** | **15** |
| Todas las ventanas (2018–2025) | 20 | 27 |

Los meses de 2023 y 2024 coinciden con `v5_rolling_origin_shocks/resultados/shock_thresholds_by_origin.csv`.

---

## A2. Fuga de datos: confirmación por punto

| Punto | Cómo se garantiza | Evidencia y prueba automática |
|---|---|---|
| (a) Scaler solo con el train de la ventana | `StandardScaler` reimplementado en `lib/` y ajustado con las filas de train de cada ventana; las columnas excluidas son las oficiales (`año`, `mes`, `mes_sin`, `mes_cos`; `escalado.py:24`) | Test: `n_samples_seen_` igual al n de train; media del scaler igual a la media recalculada solo con train |
| (b) Umbral de shock solo con historia hasta el origen | percentil de \|Δy/y\| con fechas ≤ origen; **no** se usa el P75 oficial 24.08/32.03 (calculado con TRAIN 2016-2023, `DECISIONES:768-781`) | Test: la fecha máxima usada en cada umbral es igual al origen |
| (c) Validación sale del final del train y nunca del test | val = año Y−1, test = año Y | Test: las fechas de val y test no se cruzan; ningún objetivo de val ≥ Y-01. **v5 viola esto** (ver A4) |
| (d) Hiperparámetros congelados, sin afinar con ningún test | GC3/GE de `config_gc3_ge.py:12-26` y `dual_lstm_attention.py:19-26`; XGB de `config_gc2_xgboost.py:13-32`; órdenes SARIMA de D49 (`DECISIONES:1500-1520`); alfas de Ridge/EN congelados de v3 (`v5 .../run_rolling_origin.py:19`) | Test: hash de cada config igual al congelado. **Declaración:** el orden de SARIMA-Sutil y los alfas de Ridge/EN se eligieron con datos que incluyen 2024 (y el de SARIMA-Sutil, después de ver test 2025). En las ventanas ≤2024 eso es información del futuro sobre hiperparámetros; se declara como limitación |
| (e) Lags reales en test (un paso adelante) | las features vienen de la serie observada (`features_temporales.py:54-63`, `shift(k)`); el contexto LSTM exige `context_dates < target_date` (`sequences_gc3_ge.py:75-77`); SARIMA usa `append([y_real])` | Test: para cada predicción, la fecha máxima de entrada es t−1 |
| (f, nuevo) Pesos geográficos de NASA/INDECI | los pesos oficiales usan superficie media 2016-01..2023-12 (`pesos_geograficos.py:5-9`, `00_pesos_geograficos` celda 2). En ventanas Y≤2024 eso **es fuga**. Medida (solo lectura): en Dulce, con pesos 2016-2017, INDECI agregado difiere un 15.3 % y T2M hasta 0.64 °C; en Sutil, ≤1.4 % y ≤0.03 °C | Decisión DA3. Propuesta: recalcular pesos por ventana con `VentanaTrain(2016,1,Y−2,12)` |
| NLP | `avg_sentiment` y `n_noticias` vienen de un modelo preentrenado sin ajuste (`02_fusion` celda 4); no hay parámetros ajustados con datos futuros | **No verificado:** si la limpieza de INDECI/NASA en `data/interim` imputó con estadísticos de todo el periodo |

---

## A3. Modelos

| Modelo | Semillas | Ajuste por ventana | Notas |
|---|---|---|---|
| Naive | — | ninguno | ŷ_t = y_{t−1} |
| Seasonal Naive | — | ninguno | ŷ_t = y_{t−12} |
| SARIMA rolling | — | 1 ajuste en train, `append` de val y test con `refit=False` | Sutil (1,1,1)(1,1,0,12); Dulce (1,0,0)(0,1,0,12); `trend='c'`, `approximate_diffuse`, `maxiter=500` (`auditorias/evaluar_test_sarima_rolling.py:36-57`). **Se declara: el orden de Sutil se adoptó después de ver test 2025** (`02b_diagnostico_sarima_sutil.ipynb` celdas 0, 14-15, 19-20). Si no converge, se marca "no converge" y no se fuerza |
| Ridge | — | rejilla α en train, elección por validación Y−1, ajuste final en train | **DA4 revisada.** Valores de v3 (Sutil 10, Dulce 100) solo como control en 2025; 37 predictores, X escalado en train |
| ElasticNet | — | rejilla (α, l1) en train, elección por validación Y−1, ajuste final en train | **DA4 revisada.** Valores de v3 (Sutil 0.1/0.5, Dulce 1/0.2) solo como control en 2025 |
| SARIMA-sel | — | 576 órdenes en train, top-5 por AIC, elección por validación Y−1 a 1 paso | D-BR10 |
| Chronos-Bolt-tiny | determinista (por verificar en Fase B) | ninguno | zero-shot, mediana, contexto 2016-01..t−1, univariado (`v4 .../config_chronos_zero_shot.json`). Carga desde `v4_benchmark_moderno/vendor` con `HF_HUB_OFFLINE=1` y snapshot `a0e552de…` |
| XGB-37 | 10 (0..9) | 1 ajuste por semilla en train | `OFFICIAL_GC2_XGB_CONFIG`; X e y escalados en train de la ventana |
| GC3 | 10 | 1 ajuste por semilla | Rama A 4 + Rama B 33 |
| GE | 10 | 1 ajuste por semilla | Rama A 4 + Rama B 39 (33 + 6 NLP) |
| XGB-43 (exploratorio) | 10 | 1 ajuste por semilla | tabla aparte, fuera del ranking |
| v9 (posible Fase E) | — | — | variantes T0/T1/T2 (objetivo) y Etapa 2 (`v9_mejora_dualLSTM/PRERREGISTRO.md:35-62`); post-hoc; **no entran en la corrida principal** |

**Ajustes totales con mínimo 36:**

| Modelo | Ajustes |
|---|---:|
| SARIMA | 10 |
| Ridge | 10 |
| ElasticNet | 10 |
| XGB-37 | 100 |
| GC3 | 100 |
| GE | 100 |
| XGB-43 | 100 |
| **Total** | **430** |

Chronos no se ajusta: son 16 corridas de inferencia (8 ventanas × 2 cultivos) de 12 pronósticos cada una.

**Agregación entre semillas:** para MAE y Δs se usa la media entre semillas del error absoluto mensual, que equivale a la media de los MAE por semilla. **No** se usa un ensamble de predicciones. La dispersión entre semillas se reporta aparte (cajas).

---

## A4. Comparación con v3, v4 y v5

| Aspecto | Este experimento | v5 (rolling-origin) | v3 (Ridge/EN) | v4 (Chronos) |
|---|---|---|---|---|
| Ventanas | Y=2018..2025 | 2023, 2024, 2025 | solo 2025 | solo 2025 |
| Train de modelos entrenados | hasta Y−2 | **hasta el origen Y−1** (incluye el año de validación): SARIMA `run_rolling_origin.py:97`, Ridge/EN l. 106, XGB l. 118 | train + val (`run_robustez.mjs:137,143`, fuente `v3_tabular_37_features_trainval`) | sin entrenamiento |
| Validación de early stopping (LSTM) | año Y−1 | **año Y+1 respecto a `year`, es decir el AÑO DE TEST** (`run_rolling_origin.py:17,160`: `('A',2022,'2022-12','2023')` con `val = year+1 = 2023`). **Fuga** | n/a | n/a |
| Umbral de shock | percentil hasta el origen | igual (l. 186-187) | P75 TRAIN-only oficial | meses oficiales congelados |
| Δs | (MAE_shock − MAE_global)/MAE_global ×100 (v2, `DECISIONES:820-824`) | **MAE_nonshock − MAE_shock** (l. 215) | **MAE_shock − MAE_nonshock** (columna `Delta_s` de `resultados_baselines_clasicos.csv`) | — |
| Pesos geográficos | por ventana (si se aprueba DA3) | oficiales 2016-2023 | oficiales | n/a |
| 2025 | se recalcula | reutiliza predicciones oficiales | — | — |
| Implementación | Python (sklearn/statsmodels/TF) | Python | **Node.js con descenso coordenado propio** (`run_robustez.mjs:71-73`) | Python, paquete vendorizado |

**Conclusión: ninguno de los tres es idéntico. Se recalcula todo con el código nuevo y no se mezclan resultados.**
- v4 coincide en protocolo para 2025. Se reproduce en Fase B como control.
- La fuga de validación de v5 afecta a GC3/GE en sus ventanas A y B. Conviene revisarla aparte, pero aquí no se modifica v5.

---

## A5. Métricas (todas en toneladas reales)

Por modelo, cultivo, ventana y umbral:
- MAE global, RMSE, MAE normal, MAE shock, n_shock, n_normal.
- Δs = (MAE_shock − MAE_global)/MAE_global × 100.
- Razón MAE_shock/MAE_normal.
- Δs quitando un mes de shock a la vez.
- MASE.

**Denominador de MASE (declarado antes de calcular).** Para cada ventana y cultivo:

D_w = media de |y_t − y_{t−12}| con t en los meses de train de la ventana para los que existe y_{t−12} (t de 2017-01 a diciembre de Y−2).

El mismo D_w se aplica a todos los modelos de esa ventana. En el agregado, cada mes se normaliza con el D_w de su ventana.

**Intervalos:**
- Bootstrap pareado sobre meses (los mismos meses remuestreados para todos los modelos), estratificado por ventana.
- B = 10 000, semilla 42, percentil 2.5–97.5.
- MAE_shock se remuestrea solo dentro de los meses de shock.

**Significancia:**
- Diebold-Mariano con corrección HLN (h=1, pérdida absoluta) por pares.
- Dos versiones: (i) todos los meses de las ventanas comunes (n = 60 por cultivo), (ii) solo meses de shock P75 (n = 10 Sutil, 15 Dulce).
- Se advierte la baja potencia.
- Model Confidence Set (opcional), con α = 0.10 y bootstrap de bloque 3.

**Ablación NLP:** GE − GC3 emparejados por semilla (seed s con seed s), por ventana y agregado, con su intervalo bootstrap.

**Descripción de las series** (por partición de cada ventana y de la oficial):
- media, desviación, mínimo, máximo, CV;
- ACF en los rezagos 1 y 12 en TRAIN;
- ADF y KPSS sobre el nivel y sobre la diferencia estacional (Δ12);
- n_shock por ventana y umbral.

**Reproducibilidad (Fase B):**
- ElasticNet con el protocolo v3 (α por VAL 2024 en la rejilla de `config_robustez.json`, reajuste en train+val, test 2025) frente a lo registrado: Sutil MAE 3117.64, Dulce 39.70 (`v3 .../resultados_baselines_clasicos.csv`). Se espera alguna diferencia por cambio de implementación (Node → sklearn; parametrización de α); se reportará.
- Chronos 2025 frente a `v4 .../predicciones_chronos_test2025.csv`.

---

## A6. Criterio de "mejor" (fijado antes de ver resultados)

1. **Umbral principal:** P75 de |Δy/y| mensual, calculado con la historia hasta el origen.
2. **Umbrales de reporte:** P50, P60, P75 y P90 (mensual), más la versión interanual (|y_t − y_{t−12}|/y_{t−12}, mismo cálculo de percentil hasta el origen).
3. **Conjunto de evaluación del ranking:** ventanas comunes 2021–2025, meses agrupados.
4. **Mejor en shocks** = menor MAE_shock agregado (t) en cada umbral por separado. **Mejor en meses normales** = menor MAE normal.
5. **Empate:** dos modelos empatan en un umbral si el intervalo bootstrap pareado al 95 % de la diferencia de MAE (A − B, mismos meses remuestreados) incluye 0. El "primero" de un umbral es el de menor MAE junto con todos los que empatan con él.
6. **Robusto:** queda primero, o empatado con el primero, en al menos 3 de los 4 umbrales mensuales (P50, P60, P75, P90). El interanual se reporta aparte y no cuenta para esta regla (**confirmar**).
7. Si el ranking cambia con el umbral, se reporta como resultado; no se elige el umbral que favorezca a un modelo.
8. Un Δs bajo por sí solo no es evidencia de resiliencia: se exige además MAE_shock bajo en toneladas.
9. **Ventanas no informativas:** si una ventana tiene menos de 2 meses de shock en un umbral, sus métricas por ventana se marcan "no informativa". Sus meses de shock **sí** cuentan en el agregado (DA5).

---

## A7. Barrido de umbral

- Percentiles P0, P10, P15, …, P95, calculados por ventana solo con su historia previa. Puntos de reporte: P50, P60, P75 y P90.
- Para cada uno: Δs, MAE_shock (t), razón MAE_shock/MAE_normal, n_shock por ventana y agregado, y la marca "no informativa".
- **P0 (verificación):** se define como "todos los meses de test son shock" (umbral 0 con comparación ≥). Así MAE_shock = MAE_global y Δs debe ser exactamente 0. Con P0 calculado como el mínimo de la historia y comparación estricta (>), algún mes podría quedar fuera y Δs no sería 0 sin que haya un error. Por eso se propone la definición ≥ 0 (**confirmar**). La razón MAE_shock/MAE_normal no está definida en P0 porque no hay meses normales.
- **Estabilización:** se reporta el primer percentil a partir del cual el primer lugar no cambia en los percentiles siguientes, y el percentil a partir del cual todos los modelos empatan (el ranking deja de discriminar).
- Solo recalcula máscaras sobre predicciones guardadas; no reentrena.

---

## A8. Gráficos

Ver `00_plan/mapa_evidencia.md`. Cada figura tendrá PNG a 300 dpi, PDF, `figNN_*.csv` y `figNN_*.txt`, con nombres en inglés y un archivo por cultivo.

Paleta Okabe-Ito con un color fijo por modelo, guardada en `01_configuracion/estilo_figuras.json`.

**Regla propuesta de sobreajuste/subajuste (DA6),** con MAE en toneladas en la mejor época restaurada:
- **Sobreajuste:** MAE_val > 2 × MAE_train **y** MAE_val > MAE_val del Naive.
- **Subajuste:** MAE_train > MAE_train del Naive (no supera al Naive dentro de la muestra).

Se aplica a GC3, GE, XGB-37, Ridge y ElasticNet.

---

## A9. Costo (a partir de mediciones registradas, no supuestas)

| Componente | Medición existente | Fuente | Estimación Fase C |
|---|---|---|---|
| GC3/GE | 40 corridas en 442.1 s de reloj = **11.1 s/corrida** (`fit_seconds` medio 6.3 s) | `auditorias/entrenamiento_oficial_gc3_ge_manifest.json`; `official_gc3_ge/*/*/seed_*/logs/final_status.json` | 200 corridas ≈ **37 min** (cota superior: las ventanas tempranas tienen menos datos) |
| XGB-37 y XGB-43 | 20 corridas en 108.3 s = **5.4 s/corrida** (incluye E/S y controles) | `auditorias/entrenamiento_oficial_gc2_xgboost_manifest.json` | 200 corridas ≈ **18 min** (cota superior) |
| Chronos | carga 0.84 s; 0.0086 s por pronóstico | `v4 .../auditorias/runtime_metadata.json:17-20` | 16 × (0.84 + 12 × 0.0086) ≈ **15 s** |
| SARIMA, Ridge, ElasticNet | **no medido** (v3 es Node.js; SARIMA no registró su duración) | — | se mide en Fase B |
| Barrido, bootstrap (B = 10 000), DM, figuras | **no medido** | — | se mide en Fase B |
| **Total Fase C** | | | **≈ 55 min más los componentes no medidos** |

La Fase B incluye un microbenchmark cronometrado de cada componente no medido antes de la Fase C.

---

## A10. Decisiones pendientes

| ID | Decisión | Opciones | Recomendación |
|---|---|---|---|
| DA1 | Esquema train/val | (a) protocolo oficial desplazado: train ≤Y−2, val Y−1 para todos; (b) val Y−1 solo para LSTM y los demás modelos entrenan hasta el origen (más datos, pero distinta información de estimación); (c) val = últimos 6 meses (más ventanas viables, pero cambia el protocolo de early stopping) | **(a)**: Y=2025 reproduce el oficial y la información es la misma para todos |
| DA2 | Mínimo de train | 24 meses (2020–2025, 6 ventanas; Sutil 13 y Dulce 19 shocks); **36** (2021–2025, 5 ventanas; 10/15); 48 (2022–2025, 4 ventanas; 10/12) | **36** |
| DA3 | Pesos geográficos | (a) recalcular por ventana con train ≤Y−2; (b) pesos oficiales congelados (fuga en Y≤2024, hasta 15 % en INDECI-Dulce) | **(a)** |
| DA4 | Ridge/EN en el backtest | (a) α congelados de v3 y ajuste solo en train; (b) re-seleccionar α con la validación de cada ventana (más honesto en las ventanas tempranas, pero rompe la regla de hiperparámetros congelados) | **(a)**, declarando que α se eligió con VAL 2024 |
| DA5 | Ventanas no informativas en el agregado | (a) sus meses de shock cuentan en el agregado; (b) se excluyen del agregado de shock | **(a)**: excluirlas cambiaría el denominador según el umbral |
| DA6 | Regla de sobreajuste/subajuste | la de A8, o los umbrales que prefieras | A8 |
| DA7 | Bootstrap | (a) iid pareado estratificado por ventana; (b) bloques de 3 meses | **(a)** como principal y (b) como sensibilidad |
| — | P0 con ≥ 0; robustez solo con 4 umbrales mensuales | confirmar | — |
