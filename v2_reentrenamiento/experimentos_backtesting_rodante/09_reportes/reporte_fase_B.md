# Reporte — Fase B (prueba mínima y verificaciones)

**Fecha:** 2026-10-25. **Estado:** PAUSA, esperando aprobación para la Fase C.
**Reproducción con un solo comando:** `venv\Scripts\python.exe v2_reentrenamiento\experimentos_backtesting_rodante\02_scripts\run_all.py --fase B`. Las 10 etapas dieron OK en 84 s; los logs están en `10_logs/ejecucion/`.
**No se escribió nada en `DECISIONES_METODOLOGICAS.md`** ni fuera de la carpeta del experimento (`git status`: solo `?? v2_reentrenamiento/experimentos_backtesting_rodante/`).

## 0. Confirmación de DA4

Lo que propuse y queda aprobado es esto: **hiperparámetros elegidos con VAL 2024 por v3 y congelados, y ajuste final solo con el TRAIN de cada ventana.**
- Ridge α: Sutil 10, Dulce 100.
- ElasticNet α/l1: Sutil 0.1/0.5, Dulce 1/0.2.

Matiz: los hiperparámetros **no** se vuelven a elegir con la validación de cada ventana; se usan los de v3 en todas. Si preferías re-seleccionarlos por ventana, dímelo y lo trato como desviación.

## 1. Manifest e integridad

`01_configuracion/manifest.json`:
- Python 3.11.9; numpy 2.4.4, pandas 3.0.2, scikit-learn 1.8.0, statsmodels 0.14.6, xgboost 3.2.0, tensorflow 2.21.0, keras 3.14.0, torch 2.11.0+cpu, transformers 5.5.4, matplotlib 3.10.8.
- CPU AMD64 Family 25 (16 núcleos lógicos), Windows 11 (build 26200).
- Variables: PYTHONHASHSEED=42, TF_ENABLE_ONEDNN_OPTS=0, TF_DETERMINISTIC_OPS=1, HF_HUB_OFFLINE=1.

`01_configuracion/hashes_congelados.json`: SHA-256 de 28 archivos de `v2_reentrenamiento/src`, 21 de datos y referencias, y 44 de Chronos (código vendorizado y snapshot `a0e552de…`). Cada script verifica estos hashes al empezar y **aborta** si alguno cambió.

**Semillas:** el proceso usa PYTHONHASHSEED=42, y numpy/random con semilla 42 (bootstrap 42). Cada corrida GC3/GE/XGB usa su semilla oficial 0..9 mediante `configure_determinism(seed)`, como el runner oficial, que también fija `PYTHONHASHSEED=seed` dentro del proceso. Así se reproduce exactamente el protocolo oficial.

## 2. Reproducción exacta de la ventana 2025 (`tests/test_equivalencia_2025.py`) — OK

| Artefacto | Sutil | Dulce |
|---|---|---|
| Pesos geográficos (106 / 28 provincias) | idénticos bit a bit | idénticos bit a bit |
| Maestro (120 × 16) | idéntico | idéntico |
| Features (114 filas) | idénticas | idénticas |
| Scaler v2c (mean_, scale_, n=90, 2016-07..2023-12) | idéntico | idéntico |
| Dataset escalado | idéntico | idéntico |
| Secuencias GC3 y GE (train 84, val 12, test 12; X_a, X_b, y, fechas) | idénticas a `build_sequences` oficial | idénticas |
| Pares XGB-37 (train 89, val 12) | idénticos a `build_gc2_tabular_bundle` oficial | idénticos |

**Problema encontrado y resuelto.** Los pesos calculados en memoria difieren del CSV oficial en ≤1·10⁻¹⁶. La causa es que pandas escribe los floats en CSV con unos 16 dígitos, y la cadena oficial usa los pesos leídos del CSV (`02_fusion` celda 6). La prueba compara la representación que realmente se usa (tras la ida y vuelta CSV), donde la diferencia es 0. La diferencia en memoria queda registrada en el JSON.

## 3. Mini corrida (ventana 2025, semilla 0, GC3 + SARIMA congelado, ambos cultivos) — OK

| Modelo | Diferencia máxima con la predicción oficial (t) | MAE nuevo | MAE oficial |
|---|---:|---:|---:|
| SARIMA Sutil | 7.3e-12 | 3985.016 | 3985.016 |
| SARIMA Dulce | 5.7e-14 | 21.767 | 21.767 |
| GC3 Sutil seed 0 | 4.8e-4 | 7988.5111 | 7988.5111 |
| GC3 Dulce seed 0 | 1.7e-5 | 103.5998 | 103.5998 |

- **GC3:** los **pesos entrenados son idénticos bit a bit** al checkpoint oficial (18/18 tensores) y coinciden la mejor época (Sutil 70 de 85; Dulce 14 de 29). La diferencia ≤0.0005 t aparece solo al predecir, en la salida escalada (~6·10⁻⁸, el redondeo de float32), con parámetros de desescalado idénticos. Causa probable: otra configuración numérica en el proceso de evaluación oficial (**no verificado**).
- **Determinismo entre corridas:** al repetir `run_all`, las 48 predicciones de GC3 y SARIMA fueron idénticas bit a bit.

## 4. Chronos-Bolt-tiny frente a v4 — OK

- **Sin descargas:** carga offline desde `v4_benchmark_moderno/vendor` con `HF_HUB_OFFLINE=1`.
- **MAE 2025** (idéntico a v4 en todos los dígitos): Sutil 3316.2987, Dulce 34.5572.
- **Diferencia máxima por mes:** 2.8·10⁻¹⁴ t, por el formato CSV de v4.
- **Determinismo:** dos pasadas seguidas dieron predicciones idénticas. No necesita semillas.
- ⚠️ `v4_benchmark_moderno/vendor/` **no está versionado en git** (aparece como `??`). Si no se incluye en un commit, el experimento no es reproducible en un clon del repo.

## 5. ElasticNet — OK

| | Sutil | Dulce |
|---|---:|---:|
| Registrado en v3 (MAE test 2025) | 3117.6377 | 39.6962 |
| Port exacto del algoritmo de v3, protocolo v3 | 3117.6377 (dif. −9e-13) | 39.6962 (dif. −2e-14) |
| sklearn, protocolo v3 | 3117.6377 (dif. 8e-7) | 39.6962 (dif. −5e-9) |
| α/l1 elegidos (los mismos que v3) | 0.1 / 0.5 | 1 / 0.2 |
| **Versión nueva DA4 (solo train)** | **3222.889** | **49.346** |
| Diferencia nueva − registrado | **+105.25 t (+3.4 %)** | **+9.65 t (+24.3 %)** |
| Δs nueva (P75 hasta el origen) | 130.3 % | 83.8 % |

- El pipeline queda validado: se reproduce v3 a precisión de máquina.
- La versión nueva es peor porque no reajusta con el año de validación (2024), que es el más reciente y de nivel mayor. Es el costo de usar la misma información de estimación que los demás modelos (DA1).
- La implementación de sklearn equivale a la de v3: el mismo objetivo con 1/(2n) y X estandarizado con desviación poblacional.

## 6. Prueba automática de fuga (`tests/test_fuga.py`) — OK

Las 16 combinaciones ventana×cultivo dieron OK en:
- (a) scaler: `n_samples_seen_` igual al train y media igual a la del train;
- (b) umbral: historia que termina en el origen y valor reproducible;
- (c) particiones: train ≤ Y−2, val = Y−1, test = Y, sin solapes;
- (d) hiperparámetros iguales a los congelados;
- (e) en todas las particiones, la última entrada es t−1, y en test la producción de entrada desescalada es la real de t−1;
- (f) pesos con `periodo_fin` = fin de train.

**Controles negativos:** un scaler ajustado con un año de más y un umbral calculado con datos de test **son detectados**.

**Hallazgo.** En Dulce 2021 el P75 calculado con la historia que incluye el test coincide en valor con el correcto (33.8 % en 2021, 2022 y 2023). Por eso la prueba verifica la fecha final de la historia y no solo el valor.

## 7. Comprobación de P0 (`tests/test_p0.py`) — OK

Δs = 0 exacto y n_shock = 12 en:
- 12 combinaciones reales (GC3/SARIMA de la Fase B; GC3, GE y XGB-37 oficiales con 10 semillas; Chronos);
- 32 sintéticas (8 ventanas × 2 cultivos × mensual e interanual).

## 8. Figuras (`b05_figura_prueba.py`) — OK

Se generan PNG a 300 dpi, PDF vectorial, CSV y TXT, sin título dentro de la imagen; están en `10_logs/verificaciones/fase_b/figura_prueba/`. **Es una figura de prueba, no de resultados.** Pendiente para las finales: la leyenda tapa datos y hay que moverla.

## 9. Tiempos medidos (`10_logs/verificaciones/tiempos_fase_b.json`)

| Componente | Medido | Estimación Fase C |
|---|---|---|
| SARIMA congelado | 0.07–0.19 s por ventana×cultivo | 1.1 s en total |
| SARIMA-sel (rejilla de 576, maxiter 200) | muestra de 24 órdenes: 0.04–0.33 s por ajuste | ≈ 89 s por ventana×cultivo → **≈ 15 min** (extrapolado) |
| Ridge | 0.4–1.3 ms por ajuste | < 1 s |
| ElasticNet | 0.4–0.9 ms por ajuste | < 1 s |
| XGB-37 (solo el ajuste) | 0.03–0.08 s | 200 ajustes (con XGB-43) < 1 min |
| GC3/GE | subproceso de 10–15 s (fit 4.3–9.3 s) | 200 corridas ≈ **42 min** (techo) |
| Chronos | carga 7.3 s; 0.007 s por pronóstico | ≈ 10 s |
| Bootstrap B = 10 000 (11 modelos × 60 meses) | 0.81 s por llamada | 684 llamadas ≈ **9 min** (Fase D) |
| **Total estimado** | | **Fase C ≈ 1 h; Fase D ≈ 10–15 min más figuras (no medido)** |

## 10. Decisión pendiente DA10: regla de SARIMA-sel

| Opción | Pros | Contras |
|---|---|---|
| (a) Igual que GC1: top-5 por AIC en train; se elige el de menor MAE en validación con un pronóstico de 12 pasos desde el fin de train (`02_gc1` celdas 7 y 9) | Es el procedimiento oficial tal cual | Es el que falló en Sutil (el filtro de AIC dejó fuera el orden que generalizaba), y valida con horizonte 1–12 pero se evalúa a 1 paso |
| **(b) Top-5 por AIC en train; se elige el de menor MAE en validación a 1 paso (rolling con `append(refit=False)` sobre Y−1).** **Recomendada** | Valida igual que se evalúa | Mantiene el filtro de AIC que falló en 2025 |
| (c) Sin filtro de AIC: menor MAE de validación a 1 paso entre los 576 | No depende del filtro de AIC | Con 12 meses de validación hay riesgo de sobreajustar la validación; se aleja de "AIC en train" |

Regla común a las tres: si un ajuste falla, se omite. Si el elegido no converge, se marca y no se fuerza otro.

## 11. Borrador de nota sobre v5 y v3 (para tu aprobación; no escrito en ningún archivo del repo fuera de este reporte)

> **Nota de auditoría — fuga de validación en v5 y diferencias de protocolo de v3 (2026-10-XX)**
>
> **v5_rolling_origin_shocks — fuga en GC3/GE.** En `v5_rolling_origin_shocks/scripts/run_rolling_origin.py`, las ventanas se definen como `('A', 2022, '2022-12', '2023')` y `('B', 2023, '2023-12', '2024')` (l. 17). En `train_neural_fold` el conjunto de validación de early stopping y ReduceLROnPlateau es `year + 1` (l. 160), es decir el año objetivo: 2023 para A y 2024 para B. Así, la época restaurada y la tasa de aprendizaje de GC3 y GE se eligieron mirando los mismos meses que luego se evaluaron. Los resultados de GC3/GE en las ventanas A y B de v5 (`resultados/rolling_origin_*.csv`) **no son pronósticos fuera de muestra** y no deben citarse como tales. La ventana C reutiliza las predicciones oficiales y no está afectada. Además: (i) SARIMA, Ridge, ElasticNet y XGB-37 se ajustan con toda la historia hasta el origen, incluido el año que v2 reserva como validación (l. 97, 106, 118); (ii) Δs se define como MAE_normal − MAE_shock (l. 215), con el signo invertido y en toneladas, distinto de la definición oficial v2 (relativa, %); (iii) los pesos geográficos de NASA/INDECI son los oficiales calculados con 2016–2023, lo que es fuga hacia la ventana A (2023). Estos resultados se sustituyen por los del backtesting rodante (`v2_reentrenamiento/experimentos_backtesting_rodante/`), que recalcula 2023 y 2024 con validación Y−1.
>
> **v3_robustez_metodologica — diferencias de protocolo (no fuga).** Ridge y ElasticNet (`scripts/run_robustez.mjs`) se implementaron en Node.js con descenso coordenado propio (l. 71-75). Los hiperparámetros se eligieron por MAE en VAL 2024 y **el modelo final se reajustó con train + val** (l. 137, fuente `v3_tabular_37_features_trainval`), mientras que XGB-37, GC3 y GE oficiales se ajustan solo con train. La columna `Delta_s` de `resultados_baselines_clasicos.csv` es MAE_shock − MAE_normal en toneladas, no la Δs oficial (%). El MAE registrado se reproduce exactamente (Sutil 3117.64, Dulce 39.70; `experimentos_backtesting_rodante/06_metricas/reproducibilidad/`), pero con ajuste solo en train, como los demás modelos, ElasticNet 2025 da 3222.89 (Sutil) y 49.35 (Dulce). La comparación v3 frente a modelos oficiales en la Tabla de v3 da por tanto a Ridge/ElasticNet un año más de datos de estimación.

## 12. Resumen en lenguaje simple

**Qué hice.**
- Construí el código del experimento (configuración congelada, biblioteca, pruebas y un comando único) y ejecuté la Fase B completa dos veces.
- No toqué nada fuera de la carpeta nueva ni `DECISIONES_METODOLOGICAS.md`.

**Qué encontré.**
- Mi código reproduce exactamente el v2 oficial en 2025: datos, pesos, scaler, secuencias y pares. GC3 reentrenado da pesos idénticos a los oficiales, y SARIMA, las mismas predicciones.
- Chronos reproduce v4.
- ElasticNet reproduce v3 a precisión de máquina. Ajustado solo con train (DA4) empeora: +105 t en Sutil y +9.6 t en Dulce.
- La prueba de fuga pasa en las 16 combinaciones y detecta fugas introducidas a propósito.
- P0 da Δs = 0 exacto.
- La Fase C tardaría alrededor de 1 hora.

**Problemas y cómo los resolví.**
- Diferencias de 10⁻¹⁶ en los pesos por cómo pandas escribe los CSV: se compara la versión que usa la cadena oficial.
- Un control negativo no detectaba la fuga porque el umbral coincidía por casualidad: ahora se verifica la fecha.
- `einops` y Chronos no están instalados en el venv: se usan desde la copia de v4, sin instalar nada.

**Por qué cada decisión.** Todas reproducen el protocolo oficial y tienen una prueba que lo demuestra.

**Qué no es confiable o no verificado.**
- La causa exacta de la diferencia de ≤0.0005 t en la predicción de GC3.
- El tiempo de la rejilla de SARIMA-sel, extrapolado de 24 de 576 órdenes.
- El tiempo de las figuras y del Diebold-Mariano.

**Qué necesita tu aprobación.**
1. DA10: la regla de SARIMA-sel (recomiendo b).
2. La nota sobre v5 y v3: si apruebas el texto y dónde guardarlo.
3. Pasar a la Fase C.
4. Si incluyes `v4_benchmark_moderno/vendor/` en tu commit, por reproducibilidad.
5. Confirmar mi lectura de DA4: hiperparámetros congelados de v3, no re-seleccionados por ventana.
