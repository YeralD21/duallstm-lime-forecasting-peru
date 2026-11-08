# PRERREGISTRO APROBADO — copia de la entrada en DECISIONES_METODOLOGICAS.md

> Aprobado por el usuario el 2026-10-25 con correcciones (P0, D-BR7, D-BR8). Copiado literalmente
> (desde "## 2026-10-25 …") al final de `v2_reentrenamiento/DECISIONES_METODOLOGICAS.md`.
> Incorpora DA1–DA10, con DA4 revisada. La Fase C no se ha lanzado.

---

## 2026-10-25 - D-BR1..D-BR12: preregistro del backtesting rodante v2

**Estado:** PRERREGISTRADO antes de cualquier entrenamiento o evaluación del backtesting (Fase C).
**Carpeta:** `v2_reentrenamiento/experimentos_backtesting_rodante/` (plan en `00_plan/`, configuración en `01_configuracion/`).
**Advertencia:** TEST 2025 ya fue inspeccionado en v2–v9. Las ventanas 2018–2024 son de robustez retrospectiva.
- Los hiperparámetros de GC3, GE y XGB-37 se fijaron con datos hasta 2024.
- El orden del SARIMA congelado de Sutil se adoptó después de ver TEST 2025 (`02b_diagnostico_sarima_sutil.ipynb` celdas 0, 14-15, 20).

**Verificación previa (Fase B):**
- Con Y = 2025 el código reproduce bit a bit los artefactos oficiales v2 (pesos, maestro, features, scaler v2c, secuencias, pares) y los pesos entrenados de GC3 semilla 0.
- La prueba automática de fuga pasa en las 16 combinaciones ventana×cultivo.
- Δs(P0) = 0 exacto.

### D-BR1 - Ventanas
- Origen = diciembre de Y−1; test = enero..diciembre de Y; Y = 2018..2025. 2026 queda excluido.
- Particiones para todos los modelos:

| Partición | Meses |
|---|---|
| Train | hasta diciembre de Y−2 |
| Validación | año Y−1 |
| Test | año Y |

- Inicio del train: features y SARIMA desde 2016-07; objetivos tabulares desde 2016-08; objetivos LSTM desde 2017-01 (lookback 6).
- Mínimo de train para modelos entrenados: 36 meses. Por debajo, la combinación es "no aplica" y no se fuerza.
- Resultado: 118 combinaciones viables y 42 "no aplica" (`03_ventanas/ventanas_viabilidad.csv`).
- **Ranking principal:** ventanas comunes 2021–2025.
- **Sensibilidad preregistrada:** se repiten todas las conclusiones (ranking, empates, robustez, DM) usando solo las ventanas 2023–2025.

### D-BR2 - Modelos
Las semillas, donde hay aleatoriedad, son 0..9. No hay selección de semilla ni de modelo con ningún test.

**Sin ajuste**
- Naive: ŷ_t = y_{t−1}.
- Seasonal Naive: ŷ_t = y_{t−12}.
- Chronos-Bolt-tiny zero-shot: `amazon/chronos-bolt-tiny`, revisión `a0e552de…`, mediana, contexto 2016-01..t−1, copia de `v4_benchmark_moderno/vendor`, sin red. Es determinista.

**SARIMA congelado**
- Sutil (1,1,1)(1,1,0,12); Dulce (1,0,0)(0,1,0,12).
- `trend='c'`, `approximate_diffuse`, `maxiter=500`.
- Ajuste único en train; la validación se añade como estado y el test se pronostica a 1 paso con `append(refit=False)`.

**SARIMA-sel:** regla D-BR10.

**Ridge y ElasticNet (DA4 revisada)**
- En **cada ventana** se reelige α (Ridge) o (α, l1_ratio) (ElasticNet) por el **MAE en toneladas sobre la validación de esa ventana (año Y−1)**.
- Rejilla de v3: α ∈ {0.001, 0.01, 0.1, 1, 10, 100}; l1 ∈ {0.2, 0.5, 0.8}.
- Cada candidato se ajusta **solo con el train** de la ventana. X: 37 predictores de XGB-37 estandarizados con media y desviación poblacional del train; y en toneladas.
- El modelo final es el ajuste en train con los valores elegidos: **no se reajusta con la validación**.
- Empate en el MAE de validación: primero en el orden de la rejilla (α creciente; luego l1 creciente).
- Implementación: sklearn `Ridge` y `ElasticNet(max_iter=100000, tol=1e-10)`.
- Los valores de v3 (Ridge α Sutil 10 / Dulce 100; ElasticNet Sutil 0.1/0.5, Dulce 1/0.2) se usan **solo como control en la ventana 2025**: se reporta si coinciden con los elegidos y la diferencia de MAE.

**XGB-37, GC3 y GE**
- Configuración oficial v2 (`config_gc2_xgboost.py`, `config_gc3_ge.py`, `dual_lstm_attention.py`), sin cambios.
- GC3/GE: early stopping y ReduceLROnPlateau sobre la validación Y−1; predicción con el checkpoint de la mejor época; cada corrida en un proceso nuevo con `configure_determinism(semilla)`.

**Exploratorios**
- XGB-43 (37 predictores + 6 NLP rezagados; mismos parámetros): **post-hoc**, en tabla aparte, fuera del ranking.
- Variantes de v9: excluidas (posible Fase E).

### D-BR3 - Prevención de fuga
Se ajustan **solo con el train de cada ventana**:
- el StandardScaler;
- los pesos geográficos de NASA e INDECI (`PesosGeograficos` con `VentanaTrain(2016-01, diciembre de Y−2)`);
- el denominador de MASE;
- los hiperparámetros reelegidos de Ridge, ElasticNet y SARIMA-sel (con train para ajustar y validación Y−1 para elegir).

Además:
- El umbral de shock se calcula con la historia hasta el origen.
- La validación es siempre anterior al test.
- Los lags de test usan valores observados (un paso adelante).

Prueba automática: `02_scripts/tests/test_fuga.py`, con controles negativos.

### D-BR4 - Definición de shock
- **Mensual:** r_t = |y_t − y_{t−1}|/y_{t−1}. **Interanual:** r_t = |y_t − y_{t−12}|/y_{t−12}.
- Para k = 10..95: shock si r_t > P_k (comparación estricta), con P_k el percentil k (numpy, lineal) de r calculado con los cambios fechados entre el inicio de la serie y el origen (diciembre de Y−1).
- **Principal:** P75 mensual. **Reporte:** P50, P60, P90 e interanual.
- **Barrido:** P0, P10..P95 cada 5.
- **P0 (verificación de código, no es un umbral de análisis):** se define explícitamente como umbral = 0 con comparación **r_t ≥ 0**. Como r_t es un valor absoluto, la condición se cumple siempre, así que **todos** los meses de test son shock. Entonces MAE_shock = MAE_global y **Δs(P0) = 0 exactamente**; si no da 0, hay un error de código y la corrida se detiene. P0 **no** se calcula como el percentil 0 de la historia con comparación estricta: con r_t > mín(historia), los meses de test con un cambio menor o igual que el mínimo histórico quedarían fuera y Δs no sería 0 sin que hubiera error. Para P10..P95 se mantiene la comparación estricta r_t > P_k. La razón MAE_shock/MAE_normal no está definida en P0, porque no hay meses normales.
- Una ventana con menos de 2 shocks en un umbral se marca "no informativa" en las métricas por ventana; sus meses de shock cuentan en el agregado.

### D-BR5 - Métricas
Todas en toneladas reales.
- MAE global, RMSE, MAE normal, MAE shock, n_shock, n_normal.
- Δs = (MAE_shock − MAE_global)/MAE_global × 100.
- Razón MAE_shock/MAE_normal.
- Δs quitando un mes de shock a la vez.
- MASE con denominador D_w = media de |y_t − y_{t−12}| para t entre 2017-01 y diciembre de Y−2, común a todos los modelos de la ventana. En el agregado, cada mes se normaliza con el D_w de su ventana.
- MAE por tercios y cuartiles de |Δy/y| en test.

**Intervalos:** bootstrap pareado iid sobre meses (los mismos índices para todos los modelos), estratificado por ventana, B = 10 000, semilla 42, percentiles 2.5–97.5. Sensibilidad con bloques de 3 meses.

**Significancia:**
- Diebold-Mariano con corrección HLN (h = 1, pérdida absoluta), por pares, sobre las ventanas agrupadas y restringido a meses de shock. Se declara la baja potencia.
- Model Confidence Set opcional (α = 0.10).

**Ablación NLP:** GE − GC3 con semillas emparejadas (s con s), por ventana y agregada.

### D-BR6 - Agregación de semillas
- La serie de error de un modelo con 10 semillas es el **promedio mensual del error absoluto entre las 10 semillas**.
- El bootstrap y el Diebold-Mariano usan ese promedio.
- La dispersión entre semillas se reporta aparte (cajas y DE) y no entra en los intervalos.

### D-BR7 - Regla de "mejor"
- **Mejor en shocks** = menor MAE_shock agregado, evaluado por separado en cada umbral. **Mejor en meses normales** = menor MAE normal.
- **Empate:** el IC 95 % bootstrap pareado de la diferencia de MAE entre dos modelos incluye 0. "Primero" = el de menor MAE junto con todos los que empatan con él.
- **Robusto:** un modelo es robusto si queda primero, o empatado con el primero, en al menos 3 de P50, P60, P75 y P90 (variación mensual); el interanual va aparte. Se evalúa por cultivo.
- Un Δs bajo por sí solo no es evidencia de resiliencia: se exige un MAE_shock bajo en toneladas.
- Si el ranking cambia con el umbral, se reporta como resultado; no se elige el umbral que favorezca a un modelo.
- **Barrido:** se reporta el percentil desde el cual el primer lugar ya no cambia y desde el cual todos los modelos empatan.

### D-BR8 - Diagnóstico de ajuste
- **Sobreajuste:** MAE_val/MAE_train > 2.0 (toneladas; LSTM con los pesos de la mejor época; resto con el ajuste final).
- **Señal complementaria:** la razón MAE_val/MAE_train del **Naive en la misma ventana y cultivo**. Se reporta junto a la de cada modelo como referencia del cambio de nivel y dificultad entre el train y el año de validación, que no depende de ningún ajuste.
- **Señal aparte:** "no supera al Naive" (MAE_train ≥ MAE_train del Naive, o MAE_val ≥ MAE_val del Naive).
- **Advertencia en los gráficos:** en Sutil la validación 2024 tiene un nivel medio mayor que el train, lo que infla la razón.
- **Declaración:** el umbral 2.0 **marcará como sobreajustados a casi todos los modelos entrenados**. La razón oficial de XGB-37 en 2025 ya es ≈7.0 en Sutil y ≈7.8 en Dulce. El umbral se fijó conociendo esos valores, y la bandera se interpreta junto a la razón del Naive, no por sí sola.

### D-BR9 - Exclusiones y no comparables
- No se mezclan resultados de v3, v4 ni v5. Ridge, ElasticNet y Chronos se recalculan con este protocolo.
- Las ventanas A y B de v5 tienen fuga de validación en GC3/GE (`09_reportes/nota_v5_v3.md`).

### D-BR10 - SARIMA-sel: selección del orden por ventana (DA10 = opción b)
En cada ventana y cultivo:
1. Se ajustan en train los 576 órdenes (p 0–3, d 0–1, q 0–3, P 0–2, D 0–1, Q 0–2, m = 12) con las opciones de GC1 (`enforce_stationarity=False`, `enforce_invertibility=False`, `approximate_diffuse`, `trend='c'`, `maxiter=200`; `02_gc1_sarima_prophet.ipynb` celda 7).
2. Los órdenes que fallan (excepción) se descartan y se cuentan. No se excluye ningún candidato por la bandera de convergencia, igual que en GC1.
3. Se ordenan por AIC de train ascendente (empate: orden de la rejilla) y se toman los 5 primeros.
4. Cada uno de los 5 se reajusta en train con `maxiter=500`. Con sus parámetros fijos se calcula el MAE de validación **a 1 paso** sobre el año Y−1 (`forecast(steps=1)` y luego `append([y_real], refit=False)`).
5. Se elige el de menor MAE de validación (empate: menor AIC).
6. El modelo final es ese mismo ajuste (`maxiter=500`). Sigue con el test exactamente como el SARIMA congelado: estado actualizado con la validación y pronóstico a 1 paso con `append(refit=False)`.
7. Se registran, por ventana y cultivo: el orden elegido, **su posición en AIC (1–5)** y su AIC, el AIC y el MAE de validación de los 5 candidatos, el número de órdenes fallidos y la convergencia del elegido.

**Limitación declarada:** el AIC de órdenes con distinto d/D no es estrictamente comparable (cambia la serie diferenciada). Se mantiene por fidelidad a GC1.

### D-BR11 - Reproducibilidad
- Un solo comando: `02_scripts/run_all.py`.
- Cada script verifica la integridad (SHA-256) de `v2_reentrenamiento/src`, de los datos y de Chronos frente a `01_configuracion/hashes_congelados.json` y aborta si cambian.
- Variables: PYTHONHASHSEED=42, TF_ENABLE_ONEDNN_OPTS=0, TF_DETERMINISTIC_OPS=1, HF_HUB_OFFLINE=1. Las versiones y el hardware van en `manifest.json`.
- Durante la corrida se reporta el progreso por ventana. Ante cualquier fallo la corrida se detiene y no se cambia el protocolo.

### D-BR12 - Desviaciones
Cualquier cambio posterior a este preregistro se registra en `experimentos_backtesting_rodante/09_reportes/DESVIACIONES.md`; este texto no se reescribe.
