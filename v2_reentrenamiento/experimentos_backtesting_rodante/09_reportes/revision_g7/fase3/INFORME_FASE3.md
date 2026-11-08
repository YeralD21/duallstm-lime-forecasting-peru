# Revisión G7 — Fase 3: experimentos nuevos (E1–E4)

- **Fecha:** 2026-10-31. **Rama:** `revision-experimento-v2` (sin commit).
- **Alcance:** no se modificó ni se sobrescribió nada existente. Todo lo nuevo está en `12_revision_g7/` y este informe.
- **Fuente de cifras:** todas salen de los CSV de `12_revision_g7/resultados/`. Abreviado `R/`.
- **Metodología:** la de `lib/evaluacion.py`, importada sin cambios.
  - Errores de los modelos con semillas: media mensual del error absoluto sobre las 10 semillas.
  - Máscaras de shock: las del pipeline, MoM e YoY con historia hasta el origen.
- **Control:** las cifras de los 10 modelos originales recalculadas aquí son idénticas a T06. Ejemplo, sutil 2021–2025: Chronos MAE 2,648.55, IC iid [2,171; 3,144], IC por bloques [2,243; 3,085].

---

## 1. Qué se implementó

**Archivos** (`v2_reentrenamiento/experimentos_backtesting_rodante/12_revision_g7/`):

| Archivo | Función |
|---|---|
| `scripts/g7lib.py` | Lógica de los experimentos. Importa `lib/datos.py`, `lib/preparacion.py`, `lib/modelos_series.py`, `lib/modelos_lineales.py` y `src/` sin modificarlos. Define `VentanaY1`, con la misma interfaz que `lib/ventanas.Ventana` pero con `fin_train` = dic Y−1 |
| `scripts/correr.py` | Ejecuta y orquesta las corridas. Es reanudable (salta las unidades con `completado.json`) y lanza cada LSTM en un proceso nuevo, con `configure_determinism(semilla)` antes de importar TensorFlow y `Integridad().verificar()` en cada unidad |
| `scripts/test_fuga_g7.py` | Prueba anti-fuga nueva, adaptada de `02_scripts/tests/test_fuga.py` |
| `scripts/evaluar.py` | Evaluación; escribe `R/T1..T10` |
| `resultados/unidades/<modelo>/<cultivo>/<año>/[seed_XX]/` | `predicciones.csv`, `info.json` (fechas usadas por cada paso), `history.csv` (LSTM) y `completado.json`. Los `checkpoint_best.keras` se borran tras predecir |
| `logs/` | `humo_a.json`, `humo_b.json`, `completa_etapa1.json`, `completa_etapa2.json` (tiempo por unidad), `fuga_g7_antes_corrida_completa.json`, `fuga_g7.json` |

**Entorno:** el mismo del pipeline (`lib/entorno.py`: `PYTHONHASHSEED=42`, `TF_DETERMINISTIC_OPS=1`, `TF_ENABLE_ONEDNN_OPTS=0`, `HF_HUB_OFFLINE=1`). Semilla global 42, semillas 0–9, CPU. Ninguna búsqueda de hiperparámetros y ninguna selección de semilla.

**Experimentos:**

| Exp. | Modelo | Qué cambia respecto del original | Ventanas × semillas |
|---|---|---|---|
| E1 | Ridge-Y1, ElasticNet-Y1 | α (y l1) leídos de `04_modelos/{ridge,elasticnet}/<c>/<Y>/info.json`, elegidos con validación Y−1 como antes. Ajuste final con objetivos 2016-08..dic Y−1; X estandarizado y pesos geográficos hasta dic Y−1 | 5 × 1 |
| E1 | XGB-37-Y1 | Mismos parámetros; scaler, pesos y ajuste hasta dic Y−1 | 5 × 10 |
| E1 | SARIMA-Y1, SARIMA-sel-Y1 | Mismo orden (el fijo; y el elegido por ventana en `04_modelos/sarima_sel/.../info.json`). Coeficientes reestimados con 2016-07..dic Y−1, mismas opciones (maxiter 500). Test a 1 paso con `append(refit=False)`, igual que antes | 5 × 1 |
| E1 | GC3-Y1, GE-Y1 | Train + validación (objetivos 2017-01..dic Y−1), scaler y pesos hasta dic Y−1. **Épocas = `mejor_epoca`** del `estado_final.json` original de esa semilla y ventana (mediana 34 en GC3 y 30.5 en GE; mínimo 1). Sin early stopping ni checkpoint | 5 × 10 |
| E2 | LSTM-U | Una rama: LSTM 16 + Bahdanau 16 + densas 16/8 ReLU + dropout 0.20. Entradas: producción y sus lags 1, 3 y 6 (rama A) + mes_sin/mes_cos (6 variables, secuencia de 6 meses). **2,417 parámetros**, verificados con `count_params()`. Entrenamiento idéntico a GC3 (Adam 0.001, MSE, batch 8, ≤ 300 épocas, EarlyStopping 15 y ReduceLR 0.5/8 sobre Y−1, checkpoint de mejor `val_loss`) | 5 × 10 |
| E2 | LSTM-U-Y1 | Protocolo E1 con la mejor época de LSTM-U (mediana 47.5; mínimo 9) | 5 × 10 |
| E3 | GC3-R | Arquitectura de GC3 (6,273 parámetros) y sus 37 entradas. Objetivo r_t = y_t − y_{t−12}, estandarizado con la media y la DE (ddof = 0) de los objetivos de train 2017-01..fin_train. ŷ_t = y_{t−12} + r̂_t; y_{t−12} es el valor observado | 5 × 10 |
| E3 | GC3-R-Y1 | Protocolo E1 con la mejor época de GC3-R (mediana 5; mínimo 1) | 5 × 10 |
| E4 | Chronos-small, Chronos-base | Zero-shot con el mismo código vendorizado (chronos-forecasting 2.3.2); contexto 2016-01..t−1, mediana, horizonte 1, 4 hilos, float32 | 8 (2018–2025) × 1 |

**ReduceLROnPlateau sin validación (E1/E2/E3 −Y1).**
- En Keras 3.14, `ReduceLROnPlateau.on_epoch_end` escribe `logs["learning_rate"]` **antes** de decidir la reducción (`keras/src/callbacks/reduce_lr_on_plateau.py:88`). Por tanto, la columna `learning_rate` de `history.csv` es el LR con el que se entrenó cada época.
- Las corridas −Y1 usan un `LearningRateScheduler` que reproduce, época a época, el LR de la corrida base hasta su mejor época. Así se replica el calendario de reducciones que la validación indujo en la corrida original.
- Las corridas −Y1 no usan ningún callback que mire datos. La fuente del calendario queda registrada en cada `info.json` (`lr_por_epoca_de`).

**Checkpoints de Chronos.** Se descargaron una vez de Hugging Face a la caché estándar (`~/.cache/huggingface/hub`, fuera del repo). Después se usaron offline (`HF_HUB_OFFLINE=1`), fijando la revisión:

| Modelo | Revisión (commit HF) | `model.safetensors` |
|---|---|---|
| amazon/chronos-bolt-small | `772f3d25d38aec6d914c8949dab4462e2d46f5d8` | 190,888,824 bytes |
| amazon/chronos-bolt-base | `5d9f166d69f47aef3401367a7b842e78fe97b121` | 821,203,576 bytes |

No calculé el SHA-256 de los `.safetensors`: está en NO VERIFICABLE. La revisión del commit de HF identifica el contenido de forma inmutable.

**Tiempos de cómputo** (`logs/*.json`; 16 núcleos, CPU):

| Etapa | Unidades | Procesos | Tiempo de pared |
|---|---|---|---|
| Prueba de humo A (sutil, 2024, semilla 0; 11 modelos) | 11 | 4 | 37 s |
| Prueba de humo B (LSTM-U-Y1 y GC3-R-Y1) | 2 | 2 | 10 s |
| Prueba anti-fuga, antes y después | — | 1 | ≈ 1 min cada una |
| Corrida completa, etapa 1 (todo salvo LSTM-U-Y1 y GC3-R-Y1) | 572 (11 reutilizadas del humo) | 8 | 1,020 s |
| Corrida completa, etapa 2 (LSTM-U-Y1 y GC3-R-Y1) | 200 (2 reutilizadas) | 8 | 355 s |

Tiempo de ajuste mediano por corrida LSTM (`R/T10_lstm_epocas_parametros.csv`): LSTM-U 10.1 s, GC3-R 6.8 s, GC3-Y1 5.8 s, GE-Y1 5.5 s; entre 12 y 18 s por unidad con la carga de TensorFlow. **0 errores.** `R/control_unidades.csv` confirma 60 meses de test por modelo, 10 semillas en los modelos con semilla y 96 meses en Chronos small/base.

**Prueba anti-fuga** (`scripts/test_fuga_g7.py`). Resultado: **OK** antes de la corrida completa (con las 13 unidades del humo) y **OK** después (772 unidades). Ver `logs/fuga_g7_antes_corrida_completa.json` y `logs/fuga_g7.json`. Comprueba, para cada ventana 2021–2025, cultivo y experimento:
- **(a)** pesos geográficos y scaler hasta el fin de train del protocolo (dic Y−2 original, dic Y−1 en −Y1), con el número exacto de filas;
- **(b)** objetivos de train ≤ fin de train; test = 12 meses de Y; validación = Y−1 sin solapamiento (protocolo original);
- **(c)** un paso adelante: última entrada = t−1, y la producción de entrada coincide con la serie real en t−1;
- **(d)** GC3-R: estadísticas del residuo solo con meses ≤ fin de train;
- **(e) perturbación:** se multiplica por 10 la serie nacional desde el mes t (t = ene, jun y dic de Y) y se reconstruye todo (pesos, features, scaler, secuencias y pares). Las entradas del mes t son bit a bit idénticas en los 4 caminos (tabular, GC3, LSTM-U y GC3-R; protocolos Y1 y original). El pronóstico de SARIMA-Y1 y SARIMA-sel-Y1 para junio no cambia;
- **(f) controles negativos, los 3 detectados en ambos cultivos:** scaler con un año de más, entrada contemporánea y_t, y train que incluye el test;
- **(g) artefactos de las 772 unidades:** fechas registradas, contexto de Chronos = t−1, `x_fecha` = t−1, y épocas −Y1 = mejor época de la base, comprobada además contra `argmin(val_loss)`.

---

## 2. Tablas

Abreviaturas: SN = Seasonal Naive, SSel = SARIMA-sel, EN = ElasticNet.

### 2.1 Métricas, pool 2021–2025 (`R/T1_metricas_P75_MoM_YoY.csv`)

MAE en t con IC95 iid [y por bloques de 3 meses]; MASE; MAE_shock, MASE_shock y MAE_shock relativo al SN con MoM P75 y con YoY P75. Ordenado por MAE.

**Sutil** (n_shock MoM = 10, YoY = 10)

| Modelo | MAE [iid] [bloques] | RMSE | MASE | MoM: MAE_sh / MASE_sh / rel SN | YoY: MAE_sh / MASE_sh / rel SN |
|---|---|---|---|---|---|
| Chronos-small (sens.) | 2,453 [1,988; 2,935] [2,040; 2,891] | 3,128 | 0.41 | 4,768 / 0.81 / 0.95 | 1,705 / 0.30 / 0.14 |
| Chronos-base (sens.) | 2,579 [2,084; 3,090] [2,173; 3,007] | 3,290 | 0.43 | 5,137 / 0.88 / 1.02 | 1,936 / 0.35 / 0.15 |
| **Chronos** | **2,649** [2,171; 3,144] [2,243; 3,085] | 3,308 | 0.44 | 4,784 / 0.82 / 0.95 | 1,864 / 0.33 / 0.15 |
| SARIMA-sel | 3,206 [2,563; 3,880] [2,669; 3,710] | 4,177 | 0.54 | 4,936 / 0.84 / 0.98 | 4,079 / 0.73 / 0.33 |
| SARIMA-Y1 | 3,325 [2,746; 3,929] [2,825; 3,858] | 4,091 | 0.55 | 5,169 / 0.88 / 1.03 | 3,176 / 0.57 / 0.25 |
| SARIMA | 3,361 [2,780; 3,970] [2,866; 3,885] | 4,123 | 0.56 | 5,131 / 0.88 / 1.02 | 3,233 / 0.58 / 0.26 |
| Naive | 3,624 [2,920; 4,382] [2,969; 4,295] | 4,768 | 0.61 | 8,506 / 1.45 / 1.69 | 3,172 / 0.57 / 0.25 |
| XGB-37-Y1 | 4,127 [3,340; 4,914] [3,199; 5,105] | 5,287 | 0.70 | 5,735 / 0.98 / 1.14 | 4,435 / 0.80 / 0.35 |
| ElasticNet-Y1 | 4,376 [3,298; 5,541] [3,202; 5,625] | 6,756 | 0.75 | 7,610 / 1.31 / 1.51 | 5,431 / 0.98 / 0.43 |
| Ridge-Y1 | 4,691 [3,544; 5,941] [3,436; 6,015] | 7,368 | 0.80 | 8,298 / 1.43 / 1.65 | 4,896 / 0.88 / 0.39 |
| ElasticNet | 4,872 | 7,051 | 0.83 | 8,154 / 1.40 / 1.62 | 5,404 / 0.97 / 0.43 |
| XGB-37 | 4,881 | 5,940 | 0.81 | 5,955 / 1.02 / 1.18 | 4,816 / 0.87 / 0.39 |
| Ridge | 4,925 | 7,301 | 0.83 | 8,557 / 1.47 / 1.70 | 4,946 / 0.88 / 0.40 |
| GC3-R | 6,056 [5,169; 6,930] [4,908; 7,164] | 7,450 | 1.03 | 5,163 / 0.88 / 1.03 | 11,855 / 2.14 / 0.95 |
| Seasonal Naive | 6,075 | 7,451 | 1.03 | 5,034 / 0.86 / 1.00 | 12,508 / 2.26 / 1.00 |
| LSTM-U-Y1 | 6,306 [5,441; 7,154] [5,126; 7,510] | 7,334 | 1.06 | 6,007 / 1.03 / 1.19 | 7,447 / 1.34 / 0.60 |
| GC3 | 6,361 | 8,073 | 1.08 | 6,074 / 1.04 / 1.21 | 9,166 / 1.65 / 0.73 |
| GC3-Y1 | 6,384 [5,374; 7,395] [4,984; 7,856] | 8,041 | 1.09 | 6,147 / 1.05 / 1.22 | 9,251 / 1.67 / 0.74 |
| GC3-R-Y1 | 6,428 [5,508; 7,329] [5,206; 7,601] | 7,846 | 1.09 | 5,307 / 0.91 / 1.05 | 12,557 / 2.26 / 1.00 |
| GE-Y1 | 6,540 [5,487; 7,577] [5,089; 8,032] | 8,320 | 1.12 | 6,199 / 1.06 / 1.23 | 10,403 / 1.88 / 0.83 |
| GE | 6,744 | 8,648 | 1.15 | 6,827 / 1.17 / 1.36 | 9,796 / 1.77 / 0.78 |
| LSTM-U | 6,811 [5,786; 7,876] [5,311; 8,347] | 8,116 | 1.12 | 7,108 / 1.21 / 1.41 | 7,309 / 1.31 / 0.58 |
| **SARIMA-sel-Y1** | **17,463** [12,375; 23,510] | 39,814 | 2.50 | 4,994 / 0.85 / 0.99 | 4,167 / 0.75 / 0.33 |

**SARIMA-sel-Y1 en sutil 2021 diverge.** El orden (2,1,0)(2,1,1,12), reestimado con 2016-07..2020-12, **no converge** (ConvergenceWarning con maxiter 500; `unidades/SARIMA-sel-Y1/sutil/2021/info.json`). Da pronósticos entre −78,451 y +230,985 t, con MAE de 73,706 en 2021. En las otras 9 ventana-cultivo converge, con MAE de 2,612 a 4,027 en sutil (`R/errores_test_promediados_semillas_g7.csv`).
- Lo reporto tal cual: el protocolo E1 no define un respaldo.
- Sensibilidad post-hoc, no preregistrada: si en 2021 se usa el ajuste original de SARIMA-sel (que convergió), el MAE del pool es (2,304 + 2,612 + 4,027 + 3,291 + 3,680)/5 = **3,183**, con las medias por ventana de ese mismo CSV.

**Dulce** (n_shock MoM = 15, YoY = 16)

| Modelo | MAE [iid] [bloques] | RMSE | MASE | MoM: MAE_sh / MASE_sh / rel SN | YoY: MAE_sh / MASE_sh / rel SN |
|---|---|---|---|---|---|
| SARIMA-Y1 | **18.3** [14.4; 22.8] [14.4; 22.6] | 25.3 | 0.70 | 13.4 / 0.52 / 0.54 | 27.9 / 1.10 / 0.66 |
| SARIMA | 18.4 [14.5; 22.8] [14.5; 22.7] | 25.2 | 0.71 | 14.0 / 0.54 / 0.57 | 27.4 / 1.08 / 0.65 |
| SARIMA-sel-Y1 | 20.0 [15.9; 24.5] [16.0; 24.3] | 26.8 | 0.75 | 18.4 / 0.67 / 0.75 | 28.5 / 1.12 / 0.67 |
| SARIMA-sel | 20.6 [16.5; 25.2] [16.5; 25.1] | 27.5 | 0.77 | 19.7 / 0.72 / 0.80 | 28.4 / 1.11 / 0.67 |
| **GC3-R-Y1** | **23.7** [19.8; 28.3] [19.5; 28.1] | 30.7 | 0.91 | 21.0 / 0.80 / 0.86 | 39.7 / 1.56 / 0.94 |
| **GC3-R** | **23.9** [20.0; 28.4] [19.6; 28.5] | 30.7 | 0.92 | 21.5 / 0.82 / 0.88 | 39.2 / 1.54 / 0.93 |
| Chronos-base (sens.) | 24.3 [19.4; 29.4] [20.2; 28.5] | 32.0 | 0.93 | 37.6 / 1.44 / 1.53 | 32.7 / 1.28 / 0.77 |
| Seasonal Naive | 24.5 [20.5; 29.0] [19.9; 29.2] | 31.6 | 0.95 | 24.5 / 0.94 / 1.00 | 42.4 / 1.67 / 1.00 |
| Chronos-small (sens.) | 29.0 [24.0; 34.3] [23.8; 34.4] | 36.1 | 1.11 | 49.7 / 1.91 / 2.03 | 34.3 / 1.35 / 0.81 |
| Chronos | 30.8 [25.6; 36.4] [25.4; 36.2] | 37.9 | 1.18 | 48.2 / 1.87 / 1.97 | 33.2 / 1.32 / 0.78 |
| LSTM-U-Y1 | 36.6 [29.9; 43.8] [27.6; 45.6] | 49.3 | 1.44 | 36.5 / 1.44 / 1.49 | 41.0 / 1.63 / 0.97 |
| XGB-37-Y1 | 38.6 [31.8; 46.0] [30.8; 46.5] | 48.9 | 1.48 | 46.9 / 1.78 / 1.92 | 33.0 / 1.29 / 0.78 |
| LSTM-U | 40.3 [33.5; 47.4] [31.6; 49.1] | 53.2 | 1.59 | 39.7 / 1.57 / 1.62 | 44.8 / 1.80 / 1.06 |
| ElasticNet-Y1 | 42.3 [34.2; 51.2] | 55.4 | 1.62 | 49.5 / 1.93 / 2.02 | 43.5 / 1.73 / 1.03 |
| Ridge-Y1 | 44.2 [36.1; 53.2] | 57.3 | 1.69 | 51.4 / 2.00 / 2.10 | 49.4 / 1.96 / 1.16 |
| XGB-37 | 48.3 | 60.7 | 1.86 | 65.8 / 2.53 / 2.69 | 42.3 / 1.66 / 1.00 |
| GC3-Y1 | 49.4 [41.2; 58.0] [38.1; 61.0] | 65.6 | 1.93 | 49.4 / 1.93 / 2.02 | 58.5 / 2.33 / 1.38 |
| ElasticNet | 50.2 | 65.8 | 1.93 | 67.2 / 2.61 / 2.74 | 57.3 / 2.26 / 1.35 |
| GE-Y1 | 50.3 [42.3; 58.9] [39.4; 61.8] | 65.8 | 1.96 | 52.5 / 2.03 / 2.14 | 53.0 / 2.12 / 1.25 |
| Ridge | 53.1 | 69.5 | 2.04 | 69.7 / 2.71 / 2.84 | 66.4 / 2.62 / 1.57 |
| GC3 | 56.7 | 76.4 | 2.22 | 60.7 / 2.38 / 2.48 | 58.2 / 2.32 / 1.37 |
| GE | 56.7 | 75.0 | 2.21 | 57.9 / 2.25 / 2.36 | 56.1 / 2.25 / 1.32 |
| Naive | 77.5 | 91.3 | 2.95 | 131.6 / 5.00 / 5.37 | 83.2 / 3.29 / 1.96 |

Pool 2023–2025 (mismo CSV, `pool = sensibilidad_2023_2025`):
- **Sutil:** Chronos-small 2,470; Chronos-base 2,627; Chronos 2,832; SARIMA-Y1 3,489; SARIMA 3,512; SARIMA-sel-Y1 3,666 (converge en 2023–2025); SARIMA-sel 3,705; … GC3-R 7,343; GC3 7,596; GC3-R-Y1 7,871; GC3-Y1 7,900; GE 8,197; GE-Y1 8,289.
- **Dulce:** SARIMA-sel-Y1 20.5; SARIMA-sel 20.9; SARIMA-Y1 21.9; SARIMA 22.0; GC3-R-Y1 26.8; GC3-R 27.2; Chronos-base 27.5; SN 28.1; … GE-Y1 61.0; GC3-Y1 61.5; GE 68.4; GC3 69.9.

Tabla con P50/P60/P90 (MoM e YoY): `R/T2_metricas_shock_todos_percentiles.csv`. Extracto de MAE_shock, pool 2021–2025:

| Cultivo | Modelo | MoM P50 / P60 / P75 / P90 | YoY P50 / P60 / P75 / P90 |
|---|---|---|---|
| Sutil | Chronos | 3,539 / 3,774 / 4,784 / 5,436 | 3,192 / 2,710 / 1,864 / 1,116 |
| Sutil | SARIMA-sel | 3,362 / 3,478 / 4,936 / 7,096 | 4,064 / 4,228 / 4,079 / 5,506 |
| Sutil | GC3 | 6,218 / 6,386 / 6,074 / 7,907 | 7,649 / 7,970 / 9,166 / 10,212 |
| Sutil | GC3-Y1 | 6,613 / 6,682 / 6,147 / 7,940 | 8,161 / 8,516 / 9,251 / 10,455 |
| Sutil | GC3-R | 6,369 / 6,555 / 5,163 / 7,771 | 9,855 / 10,655 / 11,855 / 14,139 |
| Sutil | LSTM-U | 6,188 / 6,238 / 7,108 / 9,162 | 7,492 / 7,202 / 7,309 / 7,309 |
| Dulce | SARIMA-sel | 17.6 / 16.2 / 19.7 / 29.1 | 24.9 / 26.4 / 28.4 / 53.6 |
| Dulce | Seasonal Naive | 20.4 / 21.9 / 24.5 / 21.4 | 37.6 / 40.1 / 42.4 / 68.6 |
| Dulce | GC3 | 49.2 / 53.2 / 60.7 / 39.4 | 67.1 / 65.3 / 58.2 / 67.5 |
| Dulce | GC3-Y1 | 41.8 / 45.0 / 49.4 / 35.3 | 60.9 / 61.1 / 58.5 / 63.2 |
| Dulce | GC3-R | 19.8 / 20.5 / 21.5 / 17.6 | 35.0 / 37.4 / 39.2 / 67.6 |
| Dulce | LSTM-U | 33.4 / 34.6 / 39.6 / 27.3 | 46.9 / 45.9 / 44.8 / 49.3 |

### 2.2 Primeros o empatados con los 21 modelos (10 originales + 11 nuevos; Chronos small/base aparte)

Fuente: `R/T3_ranking_primero_empatado.csv` (`grupo = todos`). Criterio del pipeline: el IC95 del bootstrap pareado iid de (MAE − MAE del mejor) contiene 0.

| Cultivo, pool | Global | Shock MoM P75 | Shock YoY P75 |
|---|---|---|---|
| Sutil 2021–25 | Chronos, SARIMA-sel | SN, Chronos, SARIMA, SARIMA-sel, XGB-37, GC3, XGB-37-Y1, SARIMA-Y1, SARIMA-sel-Y1, GC3-Y1, GE-Y1, LSTM-U-Y1, GC3-R, GC3-R-Y1 | Naive, Chronos |
| Sutil 2023–25 | Chronos, SARIMA, SARIMA-sel, SARIMA-Y1, SARIMA-sel-Y1 | SN, Chronos, SARIMA-sel, XGB-37, GC3, XGB-37-Y1, SARIMA-sel-Y1, LSTM-U, LSTM-U-Y1, GC3-R, GC3-R-Y1 | Naive, Chronos |
| Dulce 2021–25 | SARIMA, SARIMA-sel, SARIMA-Y1, SARIMA-sel-Y1 | SARIMA, SARIMA-Y1 | Chronos, SARIMA, SARIMA-sel, ElasticNet-Y1, XGB-37-Y1, SARIMA-Y1, SARIMA-sel-Y1, LSTM-U-Y1 |
| Dulce 2023–25 | SARIMA, SARIMA-sel, SARIMA-sel-Y1 | SARIMA, SARIMA-sel, SARIMA-Y1, SARIMA-sel-Y1 | Chronos, SARIMA, SARIMA-sel, XGB-37, ElasticNet-Y1, XGB-37-Y1, SARIMA-Y1, SARIMA-sel-Y1 |

En sutil MoM P75 empatan 14 de 21 modelos: con n = 10 meses el criterio discrimina poco.

**Criterio robusto: primero o empatado en ≥ 3 de los 4 umbrales** (`R/T4_robustez.csv`, `grupo = todos`):

| Cultivo, pool | MoM | YoY |
|---|---|---|
| Sutil 2021–25 | Chronos 4; SARIMA 3; SARIMA-Y1 3; SARIMA-sel 3 | Chronos 4; Naive 4 |
| Sutil 2023–25 | Chronos 4; SARIMA-sel 4; SARIMA-sel-Y1 3 | Chronos 4; Naive 4 |
| Dulce 2021–25 | SARIMA 4; SARIMA-Y1 4 | Chronos 4; SARIMA 3; SARIMA-Y1 3; SARIMA-sel 3; SARIMA-sel-Y1 3; **XGB-37-Y1 3** |
| Dulce 2023–25 | SARIMA-sel 3; SARIMA-sel-Y1 3 | Chronos 4; **XGB-37-Y1 4**; SARIMA 3; SARIMA-Y1 3; SARIMA-sel 3; SARIMA-sel-Y1 3 |

**Ninguna variante LSTM es robusta en ningún caso** (GC3, GE, GC3-Y1, GE-Y1, LSTM-U, LSTM-U-Y1, GC3-R ni GC3-R-Y1).

**Añadiendo Chronos small/base** (`grupo = todos_mas_chronos_small_base`):
- **Global sutil:** primeros Chronos, Chronos-small y Chronos-base (2021–2025). En 2023–2025 **solo Chronos-small y Chronos-base**: Chronos-tiny deja de estar empatado.
- **Robustez:** Chronos-small es robusto en sutil MoM (4/4) y en YoY de ambos cultivos; Chronos-base, en YoY. En dulce MoM el ranking robusto no cambia (SARIMA, SARIMA-Y1).

### 2.3 DM-HLN contra el mejor univariado

Fuente: `R/T5_DM_HLN_vs_mejor_univariado.csv`. h = 1, pérdida absoluta, errores promediados por semilla. Referencia: Chronos-tiny (sutil) y SARIMA-sel (dulce). d̄ = MAE(modelo) − MAE(referencia), en t. p bilateral sin ajustar, pool 2021–2025.

| Modelo | Sutil global d̄ (p) | Sutil shock MoM | Sutil shock YoY | Dulce global d̄ (p) | Dulce shock MoM | Dulce shock YoY |
|---|---|---|---|---|---|---|
| SARIMA-Y1 | +677 (0.022) | +385 (0.473) | +1,312 (0.027) | −2.3 (0.178) | −6.3 (0.066) | −0.5 (0.864) |
| SARIMA-sel-Y1 | +14,815 (0.002) | +210 (0.791) | +2,303 (0.044) | −0.7 (0.146) | −1.3 (0.404) | +0.1 (0.856) |
| Ridge-Y1 | +2,042 (0.008) | +3,515 (0.197) | +3,032 (0.031) | +23.6 (<0.001) | +31.7 (0.012) | +21.0 (0.105) |
| ElasticNet-Y1 | +1,728 (0.012) | +2,827 (0.196) | +3,567 (0.030) | +21.7 (<0.001) | +29.8 (0.018) | +15.2 (0.229) |
| XGB-37-Y1 | +1,479 (0.001) | +952 (0.342) | +2,571 (0.111) | +18.0 (<0.001) | +27.3 (0.009) | +4.6 (0.598) |
| GC3-Y1 | +3,735 (<0.001) | +1,363 (0.224) | +7,387 (0.010) | +28.7 (<0.001) | +29.7 (0.006) | +30.1 (0.012) |
| GE-Y1 | +3,892 (<0.001) | +1,416 (0.270) | +8,539 (0.003) | +29.7 (<0.001) | +32.8 (0.004) | +24.7 (0.019) |
| LSTM-U | +4,162 (<0.001) | +2,325 (0.116) | +5,445 (0.016) | +19.6 (<0.001) | +20.0 (0.036) | +16.4 (0.067) |
| LSTM-U-Y1 | +3,657 (<0.001) | +1,223 (0.302) | +5,583 (0.011) | +16.0 (0.001) | +16.8 (0.057) | +12.6 (0.164) |
| GC3-R | +3,407 (<0.001) | +379 (0.814) | +9,991 (<0.001) | **+3.3 (0.148)** | **+1.8 (0.648)** | +10.9 (0.017) |
| GC3-R-Y1 | +3,780 (<0.001) | +524 (0.734) | +10,693 (<0.001) | **+3.1 (0.161)** | **+1.3 (0.718)** | +11.3 (0.008) |
| Chronos-small | −196 (0.093) | −16 (0.960) | −159 (0.627) | +8.4 (0.015) | +30.0 (<0.001) | +5.9 (0.434) |
| Chronos-base | −69 (0.573) | +353 (0.199) | +72 (0.791) | +3.6 (0.241) | +17.9 (0.029) | +4.3 (0.560) |

Para 2023–2025, ver el mismo CSV. Ningún modelo nuevo tiene un d̄ negativo significativo contra la referencia en ningún alcance o pool. El único con d̄ < 0 y p < 0.05 es Chronos-small en sutil global 2023–2025 (−362 t, p = 0.019).

### 2.4 Comparaciones clave con IC pareado

Fuente: `R/T6_comparaciones_clave.csv`. Diferencia A − B del MAE promediado por semilla; IC95 bootstrap pareado iid estratificado por ventana; s = semillas (de 10) en que A es mejor, emparejadas por semilla. Pool 2021–2025.

| A − B | Sutil global | Sutil shock MoM | Sutil shock YoY | Dulce global | Dulce shock MoM | Dulce shock YoY |
|---|---|---|---|---|---|---|
| GC3-Y1 − GC3 | +22 [−298; 337] s5 | +72 [−307; 449] s7 | +85 [−102; 266] s4 | **−7.3 [−10.2; −4.5] s10** | **−11.3 [−15.9; −6.0] s10** | +0.3 [−2.7; 3.3] s5 |
| GE-Y1 − GE | −204 [−568; 159] s8 | **−627 [−893; −327] s10** | **+607 [214; 923] s2** | **−6.4 [−8.5; −4.4] s9** | **−5.3 [−9.2; −1.7] s7** | **−3.0 [−4.8; −1.4] s6** |
| LSTM-U − GC3 | +449 [−106; 1,000] s3 | +1,034 [−52; 2,001] s0 | **−1,857 [−2,917; −823] s8** | **−16.4 [−21.2; −11.8] s10** | **−21.1 [−29.5; −12.2] s10** | **−13.4 [−18.2; −8.1] s8** |
| GC3-R − GC3 | −306 [−1,421; 761] s8 | −912 [−2,994; 966] s9 | +2,689 [−215; 5,478] s0 | **−32.7 [−41.8; −24.2] s10** | **−39.2 [−52.6; −26.6] s10** | **−19.0 [−31.1; −7.6] s10** |
| GC3-R − SARIMA-sel | **+2,850 [2,020; 3,663]** | +227 [−1,461; 1,953] | **+7,776 [6,497; 9,096]** | +3.3 [−0.7; 7.2] | +1.8 [−1.2; 4.7] | **+10.9 [3.2; 18.1]** |
| GC3-R − Chronos | **+3,407 [2,463; 4,311]** | +379 [−1,972; 2,836] | **+9,991 [7,618; 12,346]** | **−6.9 [−13.0; −0.7]** | **−26.7 [−33.5; −19.3]** | +6.0 [−5.7; 17.5] |
| GC3-R-Y1 − GC3-Y1 | +44 [−996; 1,046] s6 | −839 [−3,020; 1,239] s8 | **+3,306 [543; 5,939] s0** | **−25.7 [−33.3; −18.4] s10** | **−28.5 [−39.8; −18.1] s10** | **−18.8 [−32.9; −5.8] s10** |
| GC3-R-Y1 − SARIMA-sel | **+3,222 [2,322; 4,102]** | +372 [−1,326; 2,108] | **+8,478 [7,188; 9,817]** | +3.1 [−0.8; 6.9] | +1.3 [−1.8; 4.2] | **+11.3 [4.5; 17.9]** |
| LSTM-U-Y1 − GC3-Y1 | −78 [−491; 339] s6 | −140 [−828; 549] s7 | **−1,805 [−2,814; −857] s8** | **−12.8 [−16.2; −9.4] s10** | **−12.9 [−18.6; −7.4] s7** | **−17.5 [−23.3; −11.8] s10** |
| XGB-37-Y1 − XGB-37 | **−754 [−1,215; −303] s10** | −220 [−636; 216] s7 | **−382 [−720; −29] s9** | **−9.6 [−13.5; −5.9] s10** | **−18.9 [−27.9; −10.4] s10** | **−9.3 [−14.7; −4.1] s10** |
| Ridge-Y1 − Ridge | −234 [−569; 112] | −259 [−1,091; 620] | −50 [−419; 270] | **−8.9 [−12.8; −4.9]** | **−18.3 [−23.6; −13.6]** | **−17.1 [−22.1; −12.3]** |
| ElasticNet-Y1 − ElasticNet | **−496 [−921; −129]** | −543 [−1,274; 203] | +27 [−392; 382] | **−7.9 [−11.8; −3.9]** | **−17.8 [−22.9; −13.1]** | **−13.8 [−18.3; −9.6]** |
| SARIMA-Y1 − SARIMA | −35 [−90; 21] | +38 [−139; 191] | −57 [−159; 41] | −0.1 [−0.6; 0.3] | −0.6 [−1.5; 0.0] | +0.5 [−0.7; 1.4] |
| SARIMA-sel-Y1 − SARIMA-sel | **+14,258 [9,248; 20,317]** (no convergencia 2021) | +58 [−455; 543] | +88 [−614; 733] | −0.7 [−1.5; 0.2] | −1.3 [−3.8; 1.8] | +0.1 [−1.3; 1.5] |
| Chronos-small − Chronos | −196 [−418; 22] | −16 [−575; 527] | −159 [−745; 422] | −1.8 [−4.0; 0.4] | +1.5 [−3.2; 6.4] | +1.1 [−3.5; 6.2] |
| Chronos-base − Chronos | −69 [−305; 167] | +353 [−71; 749] | +72 [−424; 563] | **−6.6 [−10.1; −2.9]** | **−10.6 [−18.2; −2.1]** | −0.5 [−8.1; 7.9] |

En negrita, los IC que excluyen 0. Las filas de 2023–2025 están en el mismo CSV.

### 2.5 Dispersión entre semillas y razón validación/train

**Dispersión** (`R/T7_dispersion_semillas.csv`, pool 2021–2025): MAE por semilla, media ± DE [mín; máx].

| Modelo | Sutil | Dulce |
|---|---|---|
| GC3 / GC3-Y1 | 6,361 ± 489 / 6,384 ± 577 | 56.7 ± 7.8 / 49.4 ± 5.3 |
| GE / GE-Y1 | 6,744 ± 524 / 6,540 ± 499 | 56.7 ± 7.5 / 50.3 ± 5.1 |
| LSTM-U / LSTM-U-Y1 | 6,811 ± 392 / 6,306 ± 282 | 40.3 ± 2.9 / 36.6 ± 3.1 |
| GC3-R / GC3-R-Y1 | 6,056 ± 162 / 6,428 ± 180 | 23.9 ± 1.4 / 23.7 ± 1.4 |
| XGB-37 / XGB-37-Y1 | 4,881 ± 90 / 4,127 ± 63 | 48.3 ± 1.4 / 38.6 ± 0.9 |

**Razón MAE_val/MAE_train > 2.0** (`R/T8_razon_val_train.csv`; solo los modelos nuevos con validación, es decir, el protocolo original; en los −Y1 la validación forma parte del train):

| Modelo | Sutil: n > 2 de 50 (mediana; máx.) | Dulce |
|---|---|---|
| LSTM-U | 25 (2.01; 4.35) | 5 (0.95; 2.47) |
| GC3-R | 14 (0.90; 4.44) | 1 (0.69; 2.67) |

Como referencia (Fase 1, T15): GC3 31/50 y 12/50; GE 28/50 y 19/50. En sutil, la razón se infla porque el nivel del año de validación es mayor que el del train (advertencia de `hiperparametros_congelados.json`).

**GC3-R para pronto:** su mejor época mediana es 5 (`R/T10`), frente a 34 de GC3 en la Fase C (épocas fijas de GC3-Y1, que copian la mejor época original). El residuo estandarizado aporta poca señal aprendible, y GC3-R queda cerca de "y_{t−12} más una corrección pequeña".

**Chronos small/base, ventanas 2018–2025** (`R/T9_chronos_por_ventana.csv`), MAE por ventana:

| Ventana | Sutil: tiny / small / base | Dulce: tiny / small / base |
|---|---|---|
| 2018 | 1,973 / 2,364 / 2,582 | 31.8 / 31.3 / 36.6 |
| 2019 | 2,702 / 3,157 / 3,119 | 33.5 / 32.7 / 30.4 |
| 2020 | 2,931 / 3,141 / 3,094 | 28.8 / 28.2 / 23.7 |

En 2018–2020, Chronos-tiny es el mejor de los tres en sutil, y base en dulce 2019–2020. Las ventanas 2021–2025 están en el mismo CSV.

---

## 3. ¿CAMBIA LA CONCLUSIÓN PRINCIPAL?

**No.**

1. **Los mejores no cambian:** Chronos en sutil y la familia SARIMA en dulce. Siguen siendo los únicos robustos (≥ 3 de 4 umbrales) en MoM, junto a sus propias variantes −Y1 (§2.2).
2. **Igualar la información no rescata a la DualLSTM.**
   - GC3-Y1 frente a GC3: sin cambio en sutil (+22 [−298; 337]); mejora en dulce (−7.3 [−10.2; −4.5], 10/10 semillas).
   - Aun así sigue muy lejos del mejor: sutil 6,384 frente a 2,649 de Chronos; dulce 49.4 frente a 18.4 de SARIMA.
   - DM contra el mejor univariado, global: p < 0.001 en ambos cultivos (§2.3).
   - Lo mismo vale para GE-Y1.
3. **Una LSTM sin exógenas (LSTM-U) es igual o mejor que GC3:** en dulce −16.4 t [−21.2; −11.8] (10/10 semillas) y en sutil YoY −1,857 [−2,917; −823]. La rama exógena de GC3 no aporta y, en dulce, empeora el pronóstico.
4. **GC3-R** (objetivo residual sobre y_{t−12}) es la mejor red:
   - en dulce, empata con SARIMA-sel en global (+3.3 [−0.7; 7.2], DM p = 0.148) y en shock MoM (+1.8 [−1.2; 4.7]), y supera a Chronos-tiny (−6.9 [−13.0; −0.7]);
   - en sutil, no mejora al Seasonal Naive (6,056 frente a 6,075) y es mucho peor que Chronos (+3,407 [2,463; 4,311]);
   - no es robusta en ningún criterio.
5. **El reajuste −Y1 mejora a los modelos tabulares**, sobre todo XGB-37-Y1 (sutil −754 [−1,215; −303]; dulce −9.6 [−13.5; −5.9]; 10/10 semillas), pero no les cambia de grupo en global. XGB-37-Y1 pasa a ser robusto **solo en dulce YoY** (3/4 y 4/4), junto a Chronos y la familia SARIMA.
6. **Chronos small/base no cambian el ranking del texto:**
   - En sutil empatan con tiny (small −196 [−418; 22]).
   - En dulce, base mejora a tiny (−6.6 [−10.1; −2.9]) pero sigue detrás de SARIMA.
   - Matiz: en sutil 2023–2025, small y base dejan a tiny fuera del empate global (−362, p = 0.019).

---

## 4. Borradores de desviaciones (PENDIENTE DE APROBACIÓN)

No se escribieron en `DESVIACIONES.md`. Texto propuesto:

**DESV-10 — Definición de shock YoY con igual peso; STL y 3M como robustez. Estado: pendiente de aprobación.**
- **Motivo (revisión G7, Fases 1 y 2):** con MoM P75, 14 de 15 shocks de dulce caen en enero–marzo y son estacionalidad de composición (provincias de campaña corta). Además, la MoM no detecta las caídas graduales (sutil mar–jul 2023).
- **Cambio:** la YoY P75 (D-BR7, hoy secundaria) se reporta con el mismo peso que la MoM P75 en el texto principal: tablas de MAE_shock, MASE_shock, MAE_shock relativo al Seasonal Naive y robustez ≥ 3 de 4.
- **Robustez:** la desestacionalizada (STL, `period=12, seasonal=13, robust=True`, estacionalidad fijada al origen) y el cambio a 3 meses se reportan en el suplementario. La STL va con la advertencia de que no está calibrada (marca el 33–45 % de los meses con P75).
- **Se decidió después de ver los resultados.** La conclusión principal no cambia con ninguna definición (Fase 2, §1.6; Fase 3, §2.2).

**DESV-11 — Reajuste final con Y−1 (E1). Estado: pendiente de aprobación.**
- **Motivo:** asimetría de información. Los modelos entrenados usaban coeficientes estimados hasta Y−2, mientras que Naive, Seasonal Naive y Chronos usan la historia hasta t−1.
- **Cambio:** variante "-Y1". Los hiperparámetros se eligen como en el preregistro (validación Y−1) y el ajuste final usa los datos hasta dic Y−1 (scaler y pesos geográficos incluidos).
  - SARIMA: mismo orden, coeficientes reestimados.
  - GC3/GE: tantas épocas como la mejor época de la corrida original, sin early stopping, con el calendario de LR de la corrida original vía `LearningRateScheduler`.
- **Incidencia:** SARIMA-sel-Y1 no converge en sutil 2021 (maxiter 500) y diverge. Se reporta sin respaldo. La sensibilidad que usa el ajuste original en ese caso es post-hoc.
- **Uso:** análisis de robustez; el ranking preregistrado se mantiene.

**DESV-12 — LSTM univariada (LSTM-U). Estado: pendiente de aprobación.**
- **Motivo:** separar el efecto de la arquitectura del efecto de las exógenas.
- **Modelo:** una rama con la arquitectura de la rama A de GC3 y 6 entradas (producción y lags 1, 3 y 6, mes sin y cos), 2,417 parámetros, entrenamiento idéntico a GC3, en protocolos original y −Y1.
- **Uso:** post-hoc, fuera del ranking preregistrado, en tabla aparte.

**DESV-13 — DualLSTM residual (GC3-R). Estado: pendiente de aprobación.**
- **Motivo:** probar si la DualLSTM mejora al aprender solo la desviación respecto del año anterior.
- **Modelo:** GC3 con objetivo r_t = y_t − y_{t−12}, estandarizado con estadísticas del train, y ŷ_t = y_{t−12} + r̂_t, en ambos protocolos.
- **Uso:** post-hoc, fuera del ranking preregistrado.

**DESV-14 — Chronos-Bolt small y base. Estado: pendiente de aprobación.**
- **Modelo:** zero-shot con el protocolo de Chronos-Bolt-tiny, ventanas 2018–2025, revisiones HF `772f3d25…` (small) y `5d9f166d…` (base), descargadas una vez y usadas offline.
- **Uso:** sensibilidad al tamaño del modelo fundacional. Chronos-Bolt-tiny sigue siendo el del ranking. El checkpoint no se eligió con ningún resultado.

---

## 5. HALLAZGOS QUE CAMBIAN EL MANUSCRITO

1. **La desventaja de la DualLSTM no se debe a la asimetría de información.** Con el reajuste −Y1, GC3 no mejora en sutil y mejora 7 t en dulce, y sigue entre los últimos (§2.4, §3). El texto puede afirmarlo con estas cifras.
2. **Las exógenas no ayudan a la red:** LSTM-U (sin clima, INDECI ni NLP; 2,417 parámetros frente a 6,273) es mejor que GC3 en dulce (−16.4 t, 10/10 semillas) y en sutil YoY, y no peor en sutil global (+449 [−106; 1,000]). Esto debilita cualquier afirmación de que la integración multimodal aporta capacidad predictiva.
3. **El objetivo residual estacional (GC3-R) es lo que más mejora a la red** (dulce −32.7 t frente a GC3, 10/10 semillas), y la deja empatada con SARIMA-sel en dulce. Pero GC3-R se detiene en la época 5 (mediana) y en sutil no supera al Seasonal Naive. La lectura honesta es que la red mejora cuando se le da la estacionalidad hecha, no que aprenda la dinámica.
4. **El reajuste −Y1 sí ayuda a los modelos tabulares** (XGB-37-Y1: −754 t en sutil y −9.6 t en dulce, 10/10 semillas). XGB-37-Y1 es robusto en dulce YoY. Si se adopta la YoY con igual peso (DESV-10), hay que mencionarlo.
5. **Reestimar un orden SARIMA seleccionado no es inocuo:** SARIMA-sel-Y1 diverge en sutil 2021 por no convergencia. Cualquier protocolo de reajuste necesita una regla de convergencia o de respaldo preregistrada.
6. **Chronos-tiny no es el mejor Chronos:** small y base empatan con él en sutil 2021–2025 y lo superan en 2023–2025; base es mejor en dulce. Si el texto presenta "Chronos" como benchmark, conviene decir que es la variante más pequeña y que las mayores no cambian la conclusión.
7. **En sutil MoM P75, 14 de 21 modelos empatan con el primero** (n = 10 meses de shock). El "desempeño en shock" de sutil con MoM P75 no discrimina entre modelos, y el texto no debe ordenar modelos por esa cifra sin decirlo.

## NO VERIFICABLE

1. **SHA-256 de los pesos de Chronos small/base:** no lo calculé. La identificación es por la revisión inmutable del commit de Hugging Face, registrada en cada `info.json`, y el tamaño en bytes. Tampoco puedo verificar el corpus de preentrenamiento de ninguno de los tres checkpoints.
2. **Determinismo bajo paralelismo:** las corridas se lanzaron 8 a la vez, con op-determinism activado. Comprobé que las unidades del humo, reutilizadas en la corrida completa, pasan la prueba anti-fuga. No volví a correr unidades para confirmar la identidad bit a bit entre la ejecución en serie y en paralelo.
3. **Calendario de LR en −Y1:** reproduce el LR por época de la corrida base. Es una elección de implementación documentada, no la única posible: con un LR constante los resultados serían otros, y no lo probé, para no buscar sobre el test.
4. **SARIMA-sel-Y1 sutil 2021:** no sé si la no convergencia se resolvería con más iteraciones u otra inicialización. Probarlo sería ajustar mirando el test.
5. **Inferencia:** los p de DM (§2.3) no están ajustados por multiplicidad (13 modelos × 3 alcances × 2 pools). Los IC de §2.4 son bootstrap iid sobre meses, y la variación entre semillas va aparte (columna s).
6. **Shocks con n pequeño:** n = 7–16 meses de shock según el pool. Los empates frecuentes (§2.2) reflejan poca potencia, no equivalencia.
