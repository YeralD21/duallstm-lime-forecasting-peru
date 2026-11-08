# Revisión G7 — Fase 1 (solo lectura)

- **Fecha:** 2026-10-31. **Rama:** `revision-experimento-v2`. **HEAD:** `5567ba2`.
- **Alcance:** no se reentrenó ningún modelo ni se modificó ningún archivo existente. Solo se crearon los archivos de esta carpeta.
- **Fuentes de las cifras:** CSV ya existentes (`05_predicciones/`, `03_ventanas/`, `06_metricas/`, `v2_reentrenamiento/data/interim/`) y texto de los PDF extraído con `pdftotext`.
- **Errores de los modelos con semillas:** son la media mensual del error absoluto sobre las 10 semillas, en la columna `ae` de `05_predicciones/errores_test_promediados_semillas.csv`.
- **Pool y umbral:** pool principal 2021–2025; umbral primario P75 MoM, con historia hasta el origen. Las máscaras salen de `03_ventanas/umbrales_y_mascaras.csv`.

**Controles de consistencia (pasan):**
- El MAE_shock y el MASE recalculados reproducen `06_metricas/agregadas/T06_agregadas_IC.csv`: diferencia máxima de 2.1×10⁻⁶ t y 4.7×10⁻¹⁰, en 80 celdas (10 modelos × 2 cultivos × 4 percentiles MoM).
- La suma de las provincias de `limon_{c}_provincia.csv` reproduce exactamente la serie nacional, y el recuento de provincias con producción > 0 coincide con `n_provincias_reportando` en los 120 meses.

**Archivos de esta carpeta:**

| Bloque | Archivo |
|---|---|
| B | `B1_calendario_shocks_P75.csv`, `B2_shocks_por_mes_calendario.csv`, `B3_MAE_inicio_vs_continuacion.csv`, `B4_caso_2023.csv` |
| C | `C_metricas_escaladas_shock.csv` (P50/P60/P75/P90, MoM y YoY; pools 2021–2025 y 2023–2025) |
| D | `D_ranking_modelos_limpios.csv` |
| E | `E1_suplementaria_2021_2025.csv`, `E2_razon_val_train_gt2.csv`, `E3_ventanas_2018_2020.csv` |
| F | `F_parametros_por_observacion.csv` |
| G | `G0_provincias_meses_registro_{sutil,dulce}.csv`, `G1_provincias_por_mes_2021_2025.csv`, `G2_shocks_entradas_salidas.csv` |
| I | `I_ensamble_semillas.csv` |

El script original que generó los CSV se perdió. Se reconstruyó como `09_reportes/revision_g7/fase1/g7_fase1.py`, que regenera las 15 tablas byte a byte desde los archivos congelados y las compara celda por celda con las publicadas (`python g7_fase1.py --estricto`; también lo ejecuta `reproduce.py`).

---

## A. Información que usa cada modelo (ventana de prueba Y = 2024)

Definición de la ventana (`02_scripts/lib/ventanas.py:40-58`): origen dic-2023; **train hasta dic-2022 (Y−2)**; validación ene–dic 2023 (Y−1); test ene–dic 2024. Los artefactos de la ventana 2024 se comprobaron en `04_modelos/*/{c}/2024/`.

| Modelo | 1. Estimación de parámetros/pesos | 2. Entrada al pronosticar cada mes t de 2024 | 3. ¿Reestima con Y−1? | Código |
|---|---|---|---|---|
| Naive | Sin parámetros | y_{t−1} observado | — | `lib/modelos_series.py:24-27` |
| Seasonal Naive | Sin parámetros | y_{t−12} observado | — | `lib/modelos_series.py:30-36` |
| Chronos-Bolt-tiny | Preentrenado; zero-shot, sin ajuste | Serie completa 2016-01..t−1; mediana a 1 paso | — | `03_modelos_sin_ajuste.py:49-52`, `lib/modelo_chronos.py:37-41` |
| SARIMA fijo | 2016-07..**2022-12** (n = 78), orden congelado | Estado del filtro actualizado con 2023 y con 2024 hasta t−1 (`append(refit=False)`) | **No** (los coeficientes no cambian) | `lib/modelos_series.py:57-61, 79-107` |
| SARIMA-sel | Rejilla de 576 órdenes en 2016-07..2022-12; top-5 por AIC; elige por MAE de validación 2023 | Igual que SARIMA fijo | **No**: el modelo final es el mismo ajuste en train | `lib/modelos_series.py:116-154` (paso 6, l. 152-154) |
| Ridge / ElasticNet | Objetivos 2016-08..2022-12 (n = 77); X estandarizado con el train; α (y l1) elegidos por MAE de validación 2023 | X_{t−1} observado: producción t−1 y sus lags 1/3/6, mes sin/cos, t_index, clima e INDECI con lags 1/3/6 | **No** (ajuste final solo en train) | `05_lineales.py:44-57`, `lib/modelos_lineales.py:63-82`, `lib/preparacion.py:97-117` |
| XGB-37 | Objetivos 2016-08..2022-12 (n = 77); scaler ajustado con 2016-07..2022-12; parámetros fijos | X_{t−1} observado, 37 predictores (`x_fecha = t−1` en los 120 pronósticos de test) | **No**; la validación no se usa para nada | `06_xgb.py:46-48, 62` |
| GC3 / GE | Objetivos 2017-01..2022-12 (n = 72); scaler ajustado con 2016-07..2022-12 | Secuencia t−6..t−1 observada (rama A: producción y sus lags; rama B: exógenas con lags; GE añade 6 lags NLP) | **No**; 2023 se usa para EarlyStopping, ReduceLR y el checkpoint de mejor `val_loss` | `lib/modelo_lstm.py:36-55`, `src/training/config_gc3_ge.py:20-25`, `lib/preparacion.py:41-42, 72-94` |

En todas las familias, los pesos geográficos y el escalado se ajustan con datos hasta dic Y−2 (`lib/datos.py:63-65`, `lib/preparacion.py:41-42`).

**4. SARIMA fijo:**
- **Estimación:** los coeficientes se estiman una sola vez con 2016-07..dic Y−2 (para 2024: 2016-07..2022-12, n = 78).
- **Actualización del estado:** se recorre la validación con `forecast(steps=1)` seguido de `append([y], refit=False)`. En el test se hace lo mismo: pronóstico a 1 paso y luego append del valor real.
- **Comprobación:** `parametros_invariantes = True` en todos los `04_modelos/sarima_*/*/*/info.json`.
- **Órdenes:** sutil (1,1,1)(1,1,0,12); dulce (1,0,0)(0,1,0,12).

**5. SARIMA-sel:** el modelo final **no** se reestima con Y−1. Es el mismo ajuste en train del candidato con menor MAE de validación (`lib/modelos_series.py:152-154`). Órdenes elegidos en 2024: sutil (1,1,2)(2,1,1,12), posición 1 en AIC; dulce (2,0,0)(0,1,0,12), posición 2.

**6. Chronos:** en los 192 pronósticos (8 ventanas × 12 meses × 2 cultivos), `contexto_fin` = t−1. Ningún contexto incluye el mes t ni meses posteriores de Y. Fuente: `04_modelos/chronos_bolt_tiny/*/*/predicciones.csv`, columnas `contexto_inicio` y `contexto_fin`.

**Asimetría de información (relevante para el manuscrito):**
- Naive, Seasonal Naive y Chronos usan **toda la historia hasta t−1**.
- Los modelos entrenados pronostican Y con coeficientes estimados hasta **Y−2**: el año Y−1 solo sirve como estado (SARIMA), como entrada observada o para seleccionar/detener el entrenamiento. Nunca entra en los pesos.

Esto viene del diseño D-BR1 y no es una fuga, pero penaliza a los modelos entrenados en series con cambio de nivel.

**7. Fechas**

| Hito | Fecha / commit | Fuente |
|---|---|---|
| Test 2025 de GC1 (SARIMA/Prophet) calculado | 2026-09-03, `ee5f9be` | `DECISIONES_METODOLOGICAS.md` l. 343-395; `experimentos/exp_002_sarima_dulce/config.yaml` ("Test tocado una unica vez") |
| **Orden del SARIMA sutil** (1,1,1)(1,1,0,12) adoptado **después de ver el test 2025** de exp_002 | Decisión del 2026-09-03; commit `bfd19a7` (2026-09-04) | DECISIONES l. 343-385; `hiperparametros_congelados.json` ("se adopto despues de ver TEST 2025") |
| **Orden del SARIMA dulce** (1,0,0)(0,1,0,12): **documentado**. Top-5 por AIC en train 2016-07..2023-12, elegido por MAE de validación 2024. Se mantuvo ("no se modifica") el 2026-09-03 con el test 2025 a la vista (R² = 0.885) | Primer commit `ee5f9be` (2026-09-03) | `experimentos/exp_002_sarima_dulce/config.yaml`; DECISIONES l. 381-385 |
| Protocolo SARIMA rolling (D46–D50) | 2026-09-12 | DECISIONES l. 1457-1530 |
| Arquitectura e hiperparámetros de GC3/GE (COMPACTA-16, MSE heredada de v1, val 2024 para early stopping) | 2026-09-10, `6a7c6dd` | DECISIONES l. 865-1110; `src/training/config_gc3_ge.py` |
| Hiperparámetros de XGB-37 ("anclada en antecedentes históricos v1") | DECISIONES 2026-09-11; archivo `config_gc2_xgboost.py` en `2793465` (2026-09-13) | DECISIONES l. 1254-1272 |
| Test 2025 de v2 (GC3/GE/XGB) evaluado | 2026-09-13, `2793465` | `auditorias/evaluar_test_gc3_ge.py` |
| Rejilla de Ridge/ElasticNet (v3) | `config_robustez.json` **no versionado**; mtime 2026-09-18, después del test 2025 | `v3_robustez_metodologica/configs/config_robustez.json` |
| Chronos (v4): un solo checkpoint, sin HPO | Auditoría con mtime 2026-09-19; no versionada | `v4_benchmark_moderno/auditorias/AUDITORIA_CHRONOS_ZERO_SHOT.md` l. 107 |
| **Preregistro del backtesting D-BR1..D-BR12** | 2026-10-25, `344134b` (22:16) y `db32108` (22:22) | DECISIONES l. 1709 y siguientes |
| Enmienda E-BR1 y scripts de la Fase C | 2026-10-28, `ddb8d4a` | DECISIONES l. 1856 |

El propio preregistro lo declara (DECISIONES l. 1711-1715): *"TEST 2025 ya fue inspeccionado en v2–v9. Las ventanas 2018–2024 son de robustez retrospectiva. Los hiperparámetros de GC3, GE y XGB-37 se fijaron con datos hasta 2024. El orden del SARIMA congelado de Sutil se adoptó después de ver TEST 2025."*

---

## B. Calendario de shocks (P75, 2021–2025)

Detalle de los 51 meses (con y_t, y_ref, cambio %, umbral de la ventana, inicio o continuación y el error de los 10 modelos): `B1_calendario_shocks_P75.csv`. "Inicio" significa que el mes anterior no fue shock con la misma definición; para enero se usó la máscara de la ventana Y−1.

**B.1 Meses de shock por mes calendario** (`B2_shocks_por_mes_calendario.csv`)

| Cultivo / definición | Ene | Feb | Mar | Abr | May | Jun | Jul | Ago | Sep | Oct | Nov | Dic | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sutil P75 MoM | 2 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 2 | 2 | 10 |
| Sutil P75 YoY | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 0 | 0 | 10 |
| **Dulce P75 MoM** | **4** | **5** | **5** | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 15 |
| Dulce P75 YoY | 2 | 0 | 1 | 0 | 0 | 1 | 2 | 2 | 3 | 1 | 2 | 2 | 16 |

- **Dulce MoM:** 14 de los 15 "shocks" son enero–marzo. Son la subida estacional de la campaña, entre +36 % y +47 % cada mes, todos los años. Solo 2024-10 (−33 %) no lo es.
- **Sutil MoM:** reparte sus shocks entre el inicio de la campaña (nov–ene: 6) y el bajón de jun–sep (4).
- **YoY:** el umbral P75 de dulce es bajo (8.1–9.2 %), así que sus 16 "shocks" son variaciones interanuales de 8–17 %, salvo 2024-09 (+39 %).
- **Sutil YoY:** 8 de 10 son la recuperación de 2024 (mar–oct, +40 % a +168 % frente a 2023).

**B.2 MAE (t) en meses de inicio frente a continuación** (`B3_MAE_inicio_vs_continuacion.csv`)

| Cultivo, definición, episodio | n | Naive | SNaive | Chronos | SARIMA | SARIMA-sel | Ridge | ElasticNet | XGB-37 | GC3 | GE |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Sutil MoM, inicio | 8 | 9,254 | 4,935 | 5,234 | 5,655 | 5,814 | 9,070 | 8,702 | 6,409 | 5,848 | 6,717 |
| Sutil MoM, continuación | 2 | 5,516 | 5,431 | 2,980 | 3,035 | 1,422 | 6,503 | 5,961 | 4,142 | 6,981 | 7,266 |
| Sutil YoY, inicio | 2 | 3,249 | 13,404 | 2,560 | 3,861 | 7,748 | 10,208 | 11,372 | 7,886 | 15,872 | 15,492 |
| Sutil YoY, continuación | 8 | 3,153 | 12,284 | 1,690 | 3,076 | 3,162 | 3,631 | 3,912 | 4,049 | 7,490 | 8,372 |
| Dulce MoM, inicio | 6 | 106.9 | 22.8 | 43.4 | 17.6 | 22.9 | 50.4 | 44.2 | 57.5 | 37.0 | 33.2 |
| Dulce MoM, continuación | 9 | 148.1 | 25.6 | 51.4 | 11.6 | 17.6 | 82.6 | 82.6 | 71.4 | 76.5 | 74.3 |
| Dulce YoY, inicio | 6 | 98.7 | 37.9 | 39.4 | 25.6 | 21.7 | 75.9 | 72.3 | 53.8 | 68.1 | 67.5 |
| Dulce YoY, continuación | 10 | 73.9 | 45.1 | 29.5 | 28.5 | 32.4 | 60.7 | 48.3 | 35.4 | 52.2 | 49.2 |

Con n = 2 en algunas celdas (sutil MoM continuación, sutil YoY inicio), la comparación es solo descriptiva.

**B.3 Caso 2023 (Niño costero / ciclón Yaku)** (`B4_caso_2023.csv`)

| Cultivo | Def. | Mes | Cambio % (umbral) | Naive | SNaive | Chronos | SARIMA | SARIMA-sel | Ridge | ElasticNet | XGB-37 | GC3 | GE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sutil | MoM | 2023-08 | −40.3 (23.9) | 6,328 | 13,548 | 4,745 | 5,278 | 10,307 | 11,283 | 12,224 | 5,578 | 12,128 | 10,968 |
| Sutil | MoM | 2023-09 | +46.8 (23.9) | 4,390 | 10,114 | 3,474 | 4,925 | 2,737 | 9,182 | 8,540 | 3,088 | 6,602 | 5,881 |
| Sutil | MoM | 2023-11 | +42.1 (23.9) | 7,156 | 131 | 3,112 | 4,771 | 3,482 | 26,568 | 23,080 | 5,099 | 3,126 | 3,436 |
| Sutil | MoM | 2023-12 | +27.5 (23.9) | 6,641 | 748 | 2,486 | 1,145 | 107 | 3,824 | 3,382 | 5,196 | 7,359 | 8,650 |
| Sutil | YoY | 2023-08 | −59.1 (39.3) | (mismos errores que MoM 2023-08) | | | | | | | | | |
| Sutil | YoY | 2023-09 | −42.3 (39.3) | (mismos errores que MoM 2023-09) | | | | | | | | | |
| Dulce | MoM | 2023-02 | +41.8 (33.8) | 124.1 | 11.6 | 36.7 | 12.0 | 10.6 | 7.0 | 0.4 | 50.4 | 42.3 | 43.8 |
| Dulce | MoM | 2023-03 | +37.4 (33.8) | 157.4 | 3.2 | 50.9 | 5.5 | 4.5 | 51.5 | 59.0 | 93.9 | 59.5 | 61.3 |

Dulce YoY no tiene ningún mes de shock en 2023.

**Lo más importante:** en sutil, la caída de mar–jul de 2023 (Yaku) fue gradual: −12 % a −19 % mensual, siempre por debajo del umbral de 23.9 %. Por eso **ningún mes de feb–jul de 2023 es shock con P75 MoM**. Los shocks de 2023 son agosto (el fondo, −40 %) y la recuperación de sep–dic. Con YoY P75 (umbral 39.3 %) solo entran ago–sep, aunque el YoY de abr–jul fue de −26 % a −38 %. Las variaciones vienen de `limon_sutil_nacional_mensual.csv`. En dulce, 2023 no muestra impacto interanual: YoY entre −8.6 % y +4.9 % (misma fuente).

---

## C. Métricas escaladas de shock (pool 2021–2025)

Fuente: `C_metricas_escaladas_shock.csv`.
- MASE_shock = media, en los meses de shock, de AE/D_w, con el D_w de `03_ventanas/denominador_mase_por_ventana.csv` (media de |y_t − y_{t−12}| en el train de la ventana; `01_construir_ventanas.py:25-31`).
- MAE_shock relativo al Seasonal Naive = MAE_shock del modelo / MAE_shock del Seasonal Naive.
- El ranking por MAE_shock relativo es, por construcción, idéntico al ranking por MAE_shock.

**C.1 P75 MoM**

| Modelo | Sutil MAE_normal | Sutil MAE_shock | t de más | Razón | MASE_shock (rango) | Rel. SNaive | Dulce MAE_normal | Dulce MAE_shock | t de más | Razón | MASE_shock (rango) | Rel. SNaive |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 2,648 | 8,506 | +5,859 | 3.21 | 1.451 (9) | 1.69 | 59.5 | 131.6 | +72.1 | 2.21 | 5.001 (10) | 5.37 |
| Seasonal Naive | 6,283 | 5,034 | −1,249 | 0.80 | 0.861 (3) | 1.00 | 24.5 | 24.5 | 0.0 | 1.00 | 0.939 (3) | 1.00 |
| Chronos | 2,222 | 4,784 | +2,562 | 2.15 | **0.816 (1)** | 0.95 | 25.0 | 48.2 | +23.2 | 1.93 | 1.866 (4) | 1.97 |
| SARIMA | 3,007 | 5,131 | +2,124 | 1.71 | 0.878 (4) | 1.02 | 19.9 | 14.0 | −5.9 | 0.70 | **0.545 (1)** | 0.57 |
| SARIMA-sel | 2,860 | 4,936 | +2,076 | 1.73 | 0.844 (2) | 0.98 | 20.9 | 19.7 | −1.3 | 0.94 | 0.721 (2) | 0.80 |
| Ridge | 4,199 | 8,557 | +4,358 | 2.04 | 1.471 (10) | 1.70 | 47.5 | 69.7 | +22.2 | 1.47 | 2.715 (9) | 2.84 |
| ElasticNet | 4,216 | 8,154 | +3,938 | 1.93 | 1.402 (8) | 1.62 | 44.6 | 67.2 | +22.6 | 1.51 | 2.614 (8) | 2.74 |
| XGB-37 | 4,667 | 5,955 | +1,289 | 1.28 | 1.018 (5) | 1.18 | 42.4 | 65.8 | +23.5 | 1.55 | 2.530 (7) | 2.69 |
| GC3 | 6,419 | 6,074 | −344 | 0.95 | 1.040 (6) | 1.21 | 55.3 | 60.7 | +5.4 | 1.10 | 2.377 (6) | 2.48 |
| GE | 6,727 | 6,827 | +100 | 1.01 | 1.169 (7) | 1.36 | 56.4 | 57.9 | +1.5 | 1.03 | 2.252 (5) | 2.36 |

n_shock = 10 (sutil) y 15 (dulce), de 60 meses.

**C.2 Primer lugar y rangos por MASE_shock en los otros umbrales MoM**

| Cultivo | P50 (n) | P60 (n) | P90 (n) |
|---|---|---|---|
| Sutil | SARIMA-sel 0.575, Chronos 0.601, SARIMA 0.620 (29) | SARIMA-sel 0.596, SARIMA 0.603, Chronos 0.643 (25) | Chronos 0.930, SARIMA 1.158, SARIMA-sel 1.214 (6) |
| Dulce | SARIMA 0.565, SARIMA-sel 0.650, SNaive 0.780 (28) | SARIMA 0.532, SARIMA-sel 0.598, SNaive 0.839 (23) | SARIMA 0.391, SNaive 0.746, SARIMA-sel 0.971 (5) |

**C.3 P75 YoY: MASE_shock (rango)**
- **Sutil:** Chronos 0.332 (1), Naive 0.568 (2), SARIMA 0.580 (3), SARIMA-sel 0.732 (4), XGB-37 0.870 (5), Ridge 0.883 (6), ElasticNet 0.966 (7), GC3 1.653 (8), GE 1.769 (9), Seasonal Naive 2.257 (10).
- **Dulce:** SARIMA 1.082 (1), SARIMA-sel 1.115 (2), Chronos 1.318 (3), XGB-37 1.662 (4), Seasonal Naive 1.671 (5), GE 2.245 (6), ElasticNet 2.261 (7), GC3 2.325 (8), Ridge 2.625 (9), Naive 3.294 (10).

**Lectura:**
- En **dulce**, el Seasonal Naive tiene el mismo error en shock que en meses normales (razón 1.00), y GC3/GE quedan con **2.4 veces** el error del Seasonal Naive en shock.
- En **sutil**, ninguna red supera al Seasonal Naive en shock (rel. 1.21 y 1.36). Las razones shock/normal cercanas a 1 de GC3/GE (0.95 y 1.01) se deben a un MAE_normal alto, no a un MAE_shock bajo.

---

## D. Ranking con modelos "limpios"

**¿Qué modelos no dependen de decisiones tomadas viendo 2025?** Lo confirmo con un matiz: los seis esperados no tienen ningún hiperparámetro fijado con 2025, pero dos de ellos usan rejillas o checkpoints definidos después de ver el test.

| Modelo | ¿Limpio? | Motivo |
|---|---|---|
| Naive, Seasonal Naive | Sí | Sin parámetros |
| Chronos | Sí, con matiz | Un único checkpoint (bolt-tiny), sin HPO ni selección con test (auditoría v4, l. 107). Se eligió en v4 (septiembre de 2026), cuando el test 2025 ya se había inspeccionado. El corpus de preentrenamiento no se puede verificar |
| SARIMA-sel | Sí | Selección por ventana con train y validación propios. La rejilla viene de `02_gc1_sarima_prophet.ipynb` (2026-09-03) y es genérica (p, q ≤ 3; P, Q ≤ 2; d, D ≤ 1) |
| Ridge, ElasticNet | Sí, con matiz | α y l1 se eligen por ventana con la validación propia. La rejilla de v3 (α en décadas 10⁻³..10², l1 ∈ {0.2, 0.5, 0.8}) es genérica pero se definió después del test 2025 (archivo no versionado; mtime 2026-09-18) |
| SARIMA fijo | **No** | Sutil: orden adoptado después de ver el test 2025. Dulce: orden elegido con train hasta 2023 y validación 2024, es decir, información futura para las ventanas 2021–2024 |
| XGB-37, GC3, GE | **No** | Hiperparámetros y arquitectura fijados con datos hasta 2024 y heredados de v1 (DECISIONES l. 1714, 1029-1060, 1265-1268) |

**Ranking (MAE, t) solo con los modelos limpios.** Fuente: `D_ranking_modelos_limpios.csv`. Bootstrap pareado iid estratificado por ventana, B = 10,000, semilla 42, la misma definición que `lib/metricas.py:31-42`. "≈" significa que el IC95 de la diferencia con el líder incluye el 0.

| Conjunto | Cultivo | Global | Shock P75 MoM (n) |
|---|---|---|---|
| 2021–2025 | Sutil | **Chronos 2,649**; ≈ SARIMA-sel 3,206 [−67; 1,195]; Naive 3,624; ElasticNet 4,872; Ridge 4,925; SNaive 6,075 | (10) **Chronos 4,784**; ≈ SARIMA-sel 4,936; ≈ SNaive 5,034; ElasticNet 8,154; Naive 8,506; Ridge 8,557 |
| 2021–2025 | Dulce | **SARIMA-sel 20.6**; ≈ SNaive 24.5 [−0.3; 8.0]; Chronos 30.8; ElasticNet 50.2; Ridge 53.1; Naive 77.5 | (15) **SARIMA-sel 19.7**; SNaive 24.5 [1.7; 7.8]; Chronos 48.2; ElasticNet 67.2; Ridge 69.7; Naive 131.6 |
| 2023–2025 | Sutil | **Chronos 2,832**; ≈ SARIMA-sel 3,705 [−49; 1,802]; Naive 4,124; Ridge 6,110; ElasticNet 6,129; SNaive 7,216 | (7) **Chronos 4,754**; ≈ SARIMA-sel 5,248; ≈ SNaive 5,276; Naive 8,499; ElasticNet 9,928; Ridge 10,341 |
| 2023–2025 | Dulce | **SARIMA-sel 20.9**; SNaive 28.1 [2.4; 11.6]; Chronos 35.0; ElasticNet 59.5; Ridge 64.0; Naive 82.2 | (9) **SARIMA-sel 16.9**; SNaive 25.0 [3.4; 12.6]; Chronos 55.3; ElasticNet 79.7; Ridge 84.2; Naive 138.2 |

Al quitar los modelos "no limpios", **el único primer lugar que cambia es dulce 2021–2025 global, que pasa de SARIMA fijo (18.4) a SARIMA-sel (20.6)**. En sutil, Chronos lidera con o sin ellos.

---

## E. Tabla suplementaria (pool 2021–2025, P75 MoM)

Fuentes:
- `E1_suplementaria_2021_2025.csv`, a partir de `06_metricas/agregadas/T06_agregadas_IC.csv` (MAE, RMSE, MASE, IC iid y por bloques circulares de 3 meses).
- `06_metricas/por_semilla/T15_diagnostico_ajuste.csv` (razón validación/train).
- `T17_descriptivo_2018_2020_{c}.csv` (ventanas 2018–2020).

Rangos: R1 = MAE 2021–2025; R2 = MAE 2023–2025; R3 = MAE_shock 2023–2025; RS = MAE_shock MoM P75 2021–2025; RY = MAE_shock YoY P75 2021–2025. La última columna es el n.º de unidades con razón validación/train > 2.0.

**Sutil**

| Modelo | MAE [IC iid] [IC bloques] | RMSE | MASE | R1 | R2 | R3 | RS | RY | > 2.0 |
|---|---|---|---|---|---|---|---|---|---|
| Naive | 3,624 [2,920; 4,382] [2,969; 4,295] | 4,768 | 0.613 | 4 | 4 | 8 | 9 | 2 | — |
| Seasonal Naive | 6,075 [5,156; 6,987] [4,854; 7,239] | 7,451 | 1.030 | 8 | 8 | 3 | 3 | 10 | — |
| Chronos | 2,649 [2,171; 3,144] [2,243; 3,085] | 3,308 | 0.440 | 1 | 1 | 1 | 1 | 1 | — |
| SARIMA | 3,361 [2,780; 3,970] [2,866; 3,885] | 4,123 | 0.559 | 3 | 2 | 4 | 4 | 3 | — |
| SARIMA-sel | 3,206 [2,563; 3,880] [2,669; 3,710] | 4,177 | 0.540 | 2 | 3 | 2 | 2 | 4 | — |
| Ridge | 4,925 [3,838; 6,074] [3,650; 6,236] | 7,301 | 0.834 | 7 | 6 | 10 | 10 | 6 | 1/5 |
| ElasticNet | 4,872 [3,847; 5,950] [3,617; 6,153] | 7,051 | 0.826 | 5 | 7 | 9 | 8 | 7 | 1/5 |
| XGB-37 | 4,881 [4,063; 5,732] [3,848; 5,944] | 5,940 | 0.809 | 6 | 5 | 5 | 5 | 5 | **50/50** |
| GC3 | 6,361 [5,292; 7,446] [4,846; 7,919] | 8,073 | 1.081 | 9 | 9 | 6 | 6 | 8 | 31/50 |
| GE | 6,744 [5,587; 7,894] [5,062; 8,443] | 8,648 | 1.148 | 10 | 10 | 7 | 7 | 9 | 28/50 |

**Dulce**

| Modelo | MAE [IC iid] [IC bloques] | RMSE | MASE | R1 | R2 | R3 | RS | RY | > 2.0 |
|---|---|---|---|---|---|---|---|---|---|
| Naive | 77.5 [65.7; 89.9] [66.3; 89.2] | 91.3 | 2.946 | 10 | 10 | 10 | 10 | 10 | — |
| Seasonal Naive | 24.5 [20.5; 29.0] [19.9; 29.2] | 31.6 | 0.945 | 3 | 3 | 3 | 3 | 5 | — |
| Chronos | 30.8 [25.6; 36.4] [25.4; 36.2] | 37.9 | 1.184 | 4 | 4 | 4 | 4 | 3 | — |
| SARIMA | 18.4 [14.5; 22.8] [14.5; 22.7] | 25.2 | 0.709 | 1 | 2 | 2 | 1 | 1 | — |
| SARIMA-sel | 20.6 [16.5; 25.2] [16.5; 25.1] | 27.5 | 0.773 | 2 | 1 | 1 | 2 | 2 | — |
| Ridge | 53.1 [43.4; 63.4] [42.7; 64.2] | 69.5 | 2.041 | 7 | 7 | 9 | 9 | 9 | 0/5 |
| ElasticNet | 50.2 [40.7; 60.4] [39.6; 61.5] | 65.8 | 1.929 | 6 | 6 | 8 | 8 | 7 | 0/5 |
| XGB-37 | 48.3 [39.8; 57.2] [38.3; 58.6] | 60.7 | 1.860 | 5 | 5 | 6 | 7 | 4 | **50/50** |
| GC3 | 56.7 [46.9; 67.0] [42.8; 70.8] | 76.4 | 2.221 | 8 | 9 | 7 | 6 | 8 | 12/50 |
| GE | 56.7 [47.5; 66.7] [43.6; 70.2] | 75.0 | 2.210 | 9 | 8 | 5 | 5 | 6 | 19/50 |

T15 no tiene unidades para Naive, Seasonal Naive, Chronos ni SARIMA ("—"). Para sutil, `hiperparametros_congelados.json` advierte que la razón se infla porque el nivel del año de validación es mayor que el del train.

**Ventanas 2018–2020** (`E3_ventanas_2018_2020.csv`, de T17; MAE en t; n de meses de shock P75 MoM entre paréntesis)

| Cultivo | Modelo | 2018 | 2019 | 2020 |
|---|---|---|---|---|
| Sutil | Naive | 2,727 (4) | 3,562 (3) | 4,102 (3) |
| Sutil | Seasonal Naive | 8,317 | 3,728 | 2,443 |
| Sutil | Chronos | 1,973 | 2,702 | 2,931 |
| Dulce | Naive | 72.3 (4) | 74.9 (4) | 66.7 (4) |
| Dulce | Seasonal Naive | 28.0 | 29.4 | 17.1 |
| Dulce | Chronos | 31.9 | 33.5 | 28.8 |

El MASE de 2018 no está definido: no hay meses de denominador (`denominador_mase_por_ventana.csv`).

---

## F. DualLSTM: parámetros por observación de entrenamiento

Fuente: `F_parametros_por_observacion.csv`. n = objetivos de train reales de la LSTM, contados en `predicciones_consolidadas.csv`. Es idéntico en las 10 semillas y en los dos cultivos.

| Ventana | n train (val) | GC3 6,273 / n | GE 6,657 / n | GC3 / (n + val) | GE / (n + val) |
|---|---|---|---|---|---|
| 2021 | 36 (12) | 174.2 | 184.9 | 130.7 | 138.7 |
| 2022 | 48 (12) | 130.7 | 138.7 | 104.6 | 111.0 |
| 2023 | 60 (12) | 104.6 | 111.0 | 87.1 | 92.5 |
| 2024 | 72 (12) | 87.1 | 92.5 | 74.7 | 79.2 |
| 2025 | 84 (12) | 74.7 | 79.2 | 65.3 | 69.3 |

---

## G. Provincias intermitentes

Fuentes: `limon_{c}_provincia.csv` y `limon_{c}_nacional_mensual.csv` (versionadas). "Intermitente" = menos de 120 meses con producción > 0 entre 2016 y 2025.

| | Sutil | Dulce |
|---|---|---|
| Provincias / intermitentes | 107 / 71 | 28 / 23 |
| % de las t de 2016–2025 que aportan las intermitentes | 3.1 % | **47.9 %** |
| Provincias que reportan por mes, 2021–2025 (mín–mediana–máx) | 60–77–94 | 9–14–19 |
| % de la producción del mes que aportan las intermitentes, 2021–2025 (mín–mediana–máx) | 0.8–2.9–7.9 % | 6.7–50.2–70.0 % |
| Media de ese %: meses de shock P75 MoM / normales | 3.0 / 3.0 % | **57.8 / 39.9 %** |

**Coincidencia de shocks con entradas y salidas del registro** (`G2_shocks_entradas_salidas.csv`; neto = t de las provincias que entran − t de las que salen, como % de Δy):
- **Sutil:** en los 20 meses de shock (MoM y YoY), las entradas y salidas explican como máximo el 2.4 % de Δy. **No hay artefacto.**
- **Dulce MoM, todos los eneros de shock (2021-01, 2022-01, 2024-01, 2025-01): entran las mismas 5 provincias** y explican **más del 100 %** del aumento:

| Mes | Δy (t) | Neto entradas (t) | % de Δy |
|---|---|---|---|
| 2021-01 | +85.6 | +108.8 | 127 % |
| 2022-01 | +93.6 | +121.4 | 130 % |
| 2024-01 | +98.1 | +139.3 | 142 % |
| 2025-01 | +94.3 | +145.7 | 155 % |

  Las provincias son Junín|Satipo (72–104 t), Loreto|Maynas (22–25 t), Cajamarca|Chota (12–16 t), Cajamarca|Jaén (≈2 t) y Loreto|Alto Amazonas (1 t). En 2023-01 el aumento (+32.5 %) quedó justo bajo el umbral de 33.8 %. En feb y mar, las entradas explican ≤ 4 %: es crecimiento estacional de las provincias que ya reportan.
- **Dulce YoY**, casos con |%| ≥ 10 %:
  - 2025-08: entra Piura|Huancabamba (16 t) = 48 % de Δy;
  - 2024-11: entra Lambayeque|Ferreñafe (8 t) y sale Áncash|Huarmey (2 t) = 26 %;
  - 2024-10: sale Ferreñafe (6 t) = −17.5 % (va contra el signo de Δy);
  - 2024-01: entra San Martín|Mariscal Cáceres (3 t) = 12 %.

---

## H. Texto dentro de las figuras

Búsqueda en tres sitios:
1. Texto extraído de los 56 PDF de `08_graficos/paper_mdpi/overleaf/figures/` (pdftotext; la carpeta tiene 57 archivos);
2. los `.txt` de `08_graficos/`;
3. los scripts generadores.

**H.1 Dentro de la imagen (PDF):**

| Figura | Texto | Script |
|---|---|---|
| `fig02_train_val_gap_sutil.pdf` | "…ratios are inflated by the level shift **(D-BR8)**." | `02_scripts/10_figuras.py:565` (`ax.text`). En dulce no aparece porque la nota solo se escribe si hay años con nivel alto |
| `fig18b_xgb43_vs_xgb37_exploratory_{sutil,dulce}.pdf` | "EXPLORATORY (post-hoc; not part of the **preregistered** ranking)" | `10_figuras.py:798` (`fig.text`). Grafía "preregistered", distinta de "pre-registered" en otros pies |

No hay "pre-registration" ni "0.49" suelto en ningún PDF. No hay palabras en español: la única coincidencia, "sin/cos" en fig25, es la función seno.

**H.2 En los `.txt` (pies sugeridos):**

| Archivo `.txt` | Texto | Script |
|---|---|---|
| fig02 (sutil y dulce) | "As pre-declared (D-BR8)…"; "(D-BR8)" en el pie | `10_figuras.py:574, 581` |
| fig05 (sutil y dulce) | "(D-BR6)" | `10_figuras.py:171` |
| fig12 (sutil y dulce) | "(D-BR7)" | `10_figuras.py:356` |
| fig15 (sutil y dulce) | "(D-BR6)" | `10_figuras.py:456` |
| fig18b | "preregistered" | `10_figuras.py:809, 817` |
| fig19b | "not part of the pre-registration" | `10_figuras.py:868` |
| fig30 | "pre-registered sensitivity analysis"; "as in D-BR1" | `11_figuras_d3.py:207-209` |
| fig_workflow | "pre-registered sensitivity set"; "follows the pre-registration" | `13_figura_workflow.py:169, 179` |

**H.3 Paquete Overleaf (`captions.tex`):**
- 0 apariciones de "D-BR": `12_paquete_overleaf.py:76-81` sustituye "(D-BR8)" y "(D-BR6)" por "(pre-registered)".
- Aun así conviven tres grafías: "pre-registered" (6), "pre-registration" (2) y "preregistered" (2).
- **"0.49":** aparece solo en `12_paquete_overleaf.py:168` (`0.49\linewidth`, maquetación) y en `resultados_v2_completo.tex:90` (un valor de ACF en TM1, legítimo).
- **Palabras en español:** "(limón sutil)" y "(limón dulce)" en los pies, a propósito.

---

## I. Ensamble de semillas (pool 2021–2025)

Fuente: `I_ensamble_semillas.csv`, a partir de `predicciones_consolidadas.csv`. El ensamble es el pronóstico promedio de las 10 semillas.

| Modelo | Cultivo | MAE, media de los errores por semilla | MAE del ensamble | MAE_shock, media por semilla | MAE_shock del ensamble (n) |
|---|---|---|---|---|---|
| XGB-37 | Sutil | 4,881 | 4,864 | 5,955 | 5,909 (10) |
| GC3 | Sutil | 6,361 | 6,212 | 6,074 | 5,787 |
| GE | Sutil | 6,744 | 6,619 | 6,827 | 6,749 |
| XGB-37 | Dulce | 48.3 | 47.8 | 65.8 | 65.5 (15) |
| GC3 | Dulce | 56.7 | **52.1** | 60.7 | 54.8 |
| GE | Dulce | 56.7 | **50.6** | 57.9 | 50.7 |
| XGB-43 (exploratorio) | Sutil / Dulce | 5,012 / 47.6 | 5,006 / 47.0 | 5,997 / 62.2 | 5,985 / 61.8 |

El ensamble mejora las LSTM entre un 2 % y un 11 %, pero **no cambia ninguna posición relativa frente a SARIMA, SARIMA-sel, Seasonal Naive o Chronos**.

---

## HALLAZGOS QUE CAMBIAN EL MANUSCRITO

1. **En dulce, los "shocks" P75 MoM son estacionalidad y altas de registro, no shocks.**
   - 14 de 15 caen en enero–marzo, la subida de campaña de cada año (B.1).
   - Los cuatro eneros los producen 5 provincias que entran al registro y explican el 127–155 % del aumento (G).
   - Por eso el Seasonal Naive y SARIMA "ganan en shock" y Δs sale negativo (C.1).
   - Lo que el texto atribuya a resiliencia ante shocks en dulce hay que reescribirlo, o cambiar la definición de shock en dulce (por ejemplo, desestacionalizada o YoY).
2. **El ciclón Yaku / Niño costero 2023 casi no entra en las máscaras de sutil.**
   - La caída de mar–jul fue gradual (−12 % a −19 % mensual) y no supera el umbral MoM de 23.9 %.
   - Con YoY P75 solo entran ago–sep (B.3).
   - Si el manuscrito usa 2023 como ejemplo de shock climático, las cifras de "MAE en shock" no lo miden.
3. **El diseño genera una asimetría de información** (A): los modelos entrenados usan coeficientes hasta Y−2 y nunca reestiman con Y−1, mientras que Naive, Seasonal Naive y Chronos usan toda la historia hasta t−1. Hay que declararlo en Métodos y Limitaciones.
4. **Varias configuraciones se fijaron mirando datos posteriores a las ventanas 2021–2024:**
   - SARIMA fijo: sutil después del test 2025; dulce con validación 2024.
   - GC3, GE y XGB-37: datos hasta 2024 y herencia de v1.

   El preregistro ya lo dice (DECISIONES l. 1711-1715), pero el texto debe presentarlo como robustez retrospectiva. Con solo los modelos limpios (D), el primer lugar cambia en dulce global, de SARIMA (18.4) a SARIMA-sel (20.6).
5. **La razón shock/normal y Δs engañan para GC3/GE.** Sus razones cercanas a 1 salen de un MAE_normal alto. En unidades escaladas, GC3/GE tienen 2.4 veces el MAE_shock del Seasonal Naive en dulce y 1.2–1.4 veces en sutil (C). Conviene reportar MASE_shock o el MAE_shock relativo al Seasonal Naive junto a Δs.
6. **Sobreparametrización de la DualLSTM:** entre 75 y 185 parámetros por objetivo de entrenamiento según la ventana (F). XGB-37 marca razón validación/train > 2.0 en las 50 de 50 unidades de ambos cultivos (E).
7. **En dulce, casi la mitad de la producción (47.9 %) viene de 23 provincias intermitentes** (G). La serie nacional mezcla nivel productivo con cobertura del registro. Debe ir en Datos y en Limitaciones.
8. **Texto interno en figuras:**
   - `fig02_train_val_gap_sutil.pdf` lleva "(D-BR8)" dentro de la imagen, en `10_figuras.py:565`. El paquete Overleaf solo corrige los pies, no la imagen.
   - fig18b dice "preregistered" y los demás textos "pre-registered"/"pre-registration": hay que unificar.

## DUDAS / NO VERIFICABLE

1. **Fecha de la rejilla v3 de Ridge/ElasticNet:** `config_robustez.json` no está versionado. Solo tengo el mtime (2026-09-18), que no prueba cuándo se definió la rejilla.
2. **Chronos-Bolt:** no puedo verificar si su corpus de preentrenamiento incluye datos de MIDAGRI ni la fecha de corte del preentrenamiento. El checkpoint se eligió en v4 sin comparar variantes (según la auditoría, no versionada).
3. **Arquitectura DualLSTM heredada de v1:** el CLAUDE.md muestra métricas de test de v1 del 2026-06-21. No pude reconstruir qué datos de test vio v1 al definir la arquitectura, porque v1 no está trazado en este experimento.
4. **"Provincia que reporta"** se definió como producción > 0. No hay en las tablas interinas una marca de "reporte con 0 t" distinta de "no reporta". Si SISAGRI distingue ambos casos, las entradas de enero en dulce podrían ser parte de un ciclo productivo real (cosecha estacional en Satipo) y no un artefacto de registro. Las tablas no permiten distinguirlo.
5. **T15** no tiene unidades de diagnóstico para SARIMA (no guarda predicciones de train), ni para Chronos, Naive o Seasonal Naive como unidad propia. La columna "> 2.0" de E solo cubre Ridge, ElasticNet, XGB-37, GC3 y GE.
6. **Δs, RMSE y MASE no tienen IC** en ningún CSV existente (E). Tampoco se calcularon aquí.
7. **Bootstrap de D:** es una cuenta nueva, replicando la definición de `lib/metricas.py:31-42` (iid estratificado por ventana, B = 10,000, semilla 42), restringida a los 6 modelos limpios. No es una cifra de los CSV de `06_metricas/`.
8. **`resultados_v2_completo.tex` del repo** es la versión generada por script, no la corregida a mano fuera del repo. El "0.49" de H.3 se refiere a esa versión.
