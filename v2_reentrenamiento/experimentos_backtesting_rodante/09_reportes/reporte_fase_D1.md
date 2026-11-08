# Reporte — Fase D1 (tablas y estadística, sin figuras)

Generado por `02_scripts/09b_reporte_fase_D1.py` a partir de los CSV de la Fase D1. El texto del reporte está en `09_reportes/reporte_fase_D1_narrativa.md`. Las vistas redondean; los CSV tienen precisión completa.

## Índice de archivos

Rutas relativas a `v2_reentrenamiento/experimentos_backtesting_rodante/`.

### Vistas (texto en este reporte, CSV y LaTeX)

| # | Tabla | CSV | LaTeX |
|---|---|---|---|
| 1 | Ta_consolidado_resumen | `05_predicciones/Ta_consolidado_resumen.csv` | `06_metricas/tablas_latex/Ta_consolidado_resumen.tex` |
| 2 | T05_MAE_P75_por_ventana_sutil | `06_metricas/por_ventana/T05_MAE_P75_por_ventana_sutil.csv` | `06_metricas/tablas_latex/T05_MAE_P75_por_ventana_sutil.tex` |
| 3 | T05_MAE_shock_P75_por_ventana_sutil | `06_metricas/por_ventana/T05_MAE_shock_P75_por_ventana_sutil.csv` | `06_metricas/tablas_latex/T05_MAE_shock_P75_por_ventana_sutil.tex` |
| 4 | T17_descriptivo_2018_2020_sutil | `06_metricas/agregadas/T17_descriptivo_2018_2020_sutil.csv` | `06_metricas/tablas_latex/T17_descriptivo_2018_2020_sutil.tex` |
| 5 | T05_MAE_P75_por_ventana_dulce | `06_metricas/por_ventana/T05_MAE_P75_por_ventana_dulce.csv` | `06_metricas/tablas_latex/T05_MAE_P75_por_ventana_dulce.tex` |
| 6 | T05_MAE_shock_P75_por_ventana_dulce | `06_metricas/por_ventana/T05_MAE_shock_P75_por_ventana_dulce.csv` | `06_metricas/tablas_latex/T05_MAE_shock_P75_por_ventana_dulce.tex` |
| 7 | T17_descriptivo_2018_2020_dulce | `06_metricas/agregadas/T17_descriptivo_2018_2020_dulce.csv` | `06_metricas/tablas_latex/T17_descriptivo_2018_2020_dulce.tex` |
| 8 | T06_agregadas_P75_principal_2021_2025_sutil | `06_metricas/agregadas/T06_agregadas_P75_principal_2021_2025_sutil.csv` | `06_metricas/tablas_latex/T06_agregadas_P75_principal_2021_2025_sutil.tex` |
| 9 | T08_ranking_shock_principal_2021_2025_sutil | `06_metricas/agregadas/T08_ranking_shock_principal_2021_2025_sutil.csv` | `06_metricas/tablas_latex/T08_ranking_shock_principal_2021_2025_sutil.tex` |
| 10 | T08_ranking_normal_principal_2021_2025_sutil | `06_metricas/agregadas/T08_ranking_normal_principal_2021_2025_sutil.csv` | `06_metricas/tablas_latex/T08_ranking_normal_principal_2021_2025_sutil.tex` |
| 11 | T06_agregadas_P75_principal_2021_2025_dulce | `06_metricas/agregadas/T06_agregadas_P75_principal_2021_2025_dulce.csv` | `06_metricas/tablas_latex/T06_agregadas_P75_principal_2021_2025_dulce.tex` |
| 12 | T08_ranking_shock_principal_2021_2025_dulce | `06_metricas/agregadas/T08_ranking_shock_principal_2021_2025_dulce.csv` | `06_metricas/tablas_latex/T08_ranking_shock_principal_2021_2025_dulce.tex` |
| 13 | T08_ranking_normal_principal_2021_2025_dulce | `06_metricas/agregadas/T08_ranking_normal_principal_2021_2025_dulce.csv` | `06_metricas/tablas_latex/T08_ranking_normal_principal_2021_2025_dulce.tex` |
| 14 | T06_agregadas_P75_sensibilidad_2023_2025_sutil | `06_metricas/agregadas/T06_agregadas_P75_sensibilidad_2023_2025_sutil.csv` | `06_metricas/tablas_latex/T06_agregadas_P75_sensibilidad_2023_2025_sutil.tex` |
| 15 | T08_ranking_shock_sensibilidad_2023_2025_sutil | `06_metricas/agregadas/T08_ranking_shock_sensibilidad_2023_2025_sutil.csv` | `06_metricas/tablas_latex/T08_ranking_shock_sensibilidad_2023_2025_sutil.tex` |
| 16 | T08_ranking_normal_sensibilidad_2023_2025_sutil | `06_metricas/agregadas/T08_ranking_normal_sensibilidad_2023_2025_sutil.csv` | `06_metricas/tablas_latex/T08_ranking_normal_sensibilidad_2023_2025_sutil.tex` |
| 17 | T06_agregadas_P75_sensibilidad_2023_2025_dulce | `06_metricas/agregadas/T06_agregadas_P75_sensibilidad_2023_2025_dulce.csv` | `06_metricas/tablas_latex/T06_agregadas_P75_sensibilidad_2023_2025_dulce.tex` |
| 18 | T08_ranking_shock_sensibilidad_2023_2025_dulce | `06_metricas/agregadas/T08_ranking_shock_sensibilidad_2023_2025_dulce.csv` | `06_metricas/tablas_latex/T08_ranking_shock_sensibilidad_2023_2025_dulce.tex` |
| 19 | T08_ranking_normal_sensibilidad_2023_2025_dulce | `06_metricas/agregadas/T08_ranking_normal_sensibilidad_2023_2025_dulce.csv` | `06_metricas/tablas_latex/T08_ranking_normal_sensibilidad_2023_2025_dulce.tex` |
| 20 | T09_DM_matriz_principal_2021_2025_sutil | `06_metricas/significancia/T09_DM_matriz_principal_2021_2025_sutil.csv` | `06_metricas/tablas_latex/T09_DM_matriz_principal_2021_2025_sutil.tex` |
| 21 | T09_DM_matriz_principal_2021_2025_dulce | `06_metricas/significancia/T09_DM_matriz_principal_2021_2025_dulce.csv` | `06_metricas/tablas_latex/T09_DM_matriz_principal_2021_2025_dulce.tex` |
| 22 | T09_DM_matriz_sensibilidad_2023_2025_sutil | `06_metricas/significancia/T09_DM_matriz_sensibilidad_2023_2025_sutil.csv` | `06_metricas/tablas_latex/T09_DM_matriz_sensibilidad_2023_2025_sutil.tex` |
| 23 | T09_DM_matriz_sensibilidad_2023_2025_dulce | `06_metricas/significancia/T09_DM_matriz_sensibilidad_2023_2025_dulce.csv` | `06_metricas/tablas_latex/T09_DM_matriz_sensibilidad_2023_2025_dulce.tex` |
| 24 | T09_DM_holm_matriz_principal_2021_2025_sutil | `06_metricas/significancia/T09_DM_holm_matriz_principal_2021_2025_sutil.csv` | `06_metricas/tablas_latex/T09_DM_holm_matriz_principal_2021_2025_sutil.tex` |
| 25 | T09_DM_holm_matriz_principal_2021_2025_dulce | `06_metricas/significancia/T09_DM_holm_matriz_principal_2021_2025_dulce.csv` | `06_metricas/tablas_latex/T09_DM_holm_matriz_principal_2021_2025_dulce.tex` |
| 26 | T09_DM_holm_matriz_sensibilidad_2023_2025_sutil | `06_metricas/significancia/T09_DM_holm_matriz_sensibilidad_2023_2025_sutil.csv` | `06_metricas/tablas_latex/T09_DM_holm_matriz_sensibilidad_2023_2025_sutil.tex` |
| 27 | T09_DM_holm_matriz_sensibilidad_2023_2025_dulce | `06_metricas/significancia/T09_DM_holm_matriz_sensibilidad_2023_2025_dulce.csv` | `06_metricas/tablas_latex/T09_DM_holm_matriz_sensibilidad_2023_2025_dulce.tex` |
| 28 | T09_holm_resumen | `06_metricas/significancia/T09_holm_resumen.csv` | `06_metricas/tablas_latex/T09_holm_resumen.tex` |
| 29 | T11_ablacion_sutil | `06_metricas/ablacion_nlp/T11_ablacion_sutil.csv` | `06_metricas/tablas_latex/T11_ablacion_sutil.tex` |
| 30 | T11_ablacion_dulce | `06_metricas/ablacion_nlp/T11_ablacion_dulce.csv` | `06_metricas/tablas_latex/T11_ablacion_dulce.tex` |
| 31 | T12_loo_agregado_sutil | `06_metricas/agregadas/T12_loo_agregado_sutil.csv` | `06_metricas/tablas_latex/T12_loo_agregado_sutil.tex` |
| 32 | T12_loo_agregado_dulce | `06_metricas/agregadas/T12_loo_agregado_dulce.csv` | `06_metricas/tablas_latex/T12_loo_agregado_dulce.tex` |
| 33 | T13_cuartiles_sutil | `06_metricas/agregadas/T13_cuartiles_sutil.csv` | `06_metricas/tablas_latex/T13_cuartiles_sutil.tex` |
| 34 | T13_cuartiles_dulce | `06_metricas/agregadas/T13_cuartiles_dulce.csv` | `06_metricas/tablas_latex/T13_cuartiles_dulce.tex` |
| 35 | T07_dispersion_semillas | `06_metricas/por_semilla/T07_dispersion_semillas.csv` | `06_metricas/tablas_latex/T07_dispersion_semillas.tex` |
| 36 | T15_diagnostico_sutil | `06_metricas/por_semilla/T15_diagnostico_sutil.csv` | `06_metricas/tablas_latex/T15_diagnostico_sutil.tex` |
| 37 | T15_diagnostico_dulce | `06_metricas/por_semilla/T15_diagnostico_dulce.csv` | `06_metricas/tablas_latex/T15_diagnostico_dulce.tex` |
| 38 | T15_mejor_epoca_por_ventana | `06_metricas/por_semilla/T15_mejor_epoca_por_ventana.csv` | `06_metricas/tablas_latex/T15_mejor_epoca_por_ventana.tex` |
| 39 | T03_particiones_sutil | `06_metricas/descripcion_series/T03_particiones_sutil.csv` | `06_metricas/tablas_latex/T03_particiones_sutil.tex` |
| 40 | T04_estacionariedad_sutil | `06_metricas/descripcion_series/T04_estacionariedad_sutil.csv` | `06_metricas/tablas_latex/T04_estacionariedad_sutil.tex` |
| 41 | T03_particiones_dulce | `06_metricas/descripcion_series/T03_particiones_dulce.csv` | `06_metricas/tablas_latex/T03_particiones_dulce.tex` |
| 42 | T04_estacionariedad_dulce | `06_metricas/descripcion_series/T04_estacionariedad_dulce.csv` | `06_metricas/tablas_latex/T04_estacionariedad_dulce.tex` |
| 43 | T20_sarima_sel | `06_metricas/por_ventana/T20_sarima_sel.csv` | `06_metricas/tablas_latex/T20_sarima_sel.tex` |
| 44 | T21_lineales_hiperparametros | `06_metricas/por_ventana/T21_lineales_hiperparametros.csv` | `06_metricas/tablas_latex/T21_lineales_hiperparametros.tex` |
| 45 | T16_exploratorio_xgb43 | `06_metricas/agregadas/T16_exploratorio_xgb43.csv` | `06_metricas/tablas_latex/T16_exploratorio_xgb43.tex` |
| 46 | T_barrido_posiciones_mensual_sutil | `07_barrido_umbral/mensual/T_barrido_posiciones_mensual_sutil.csv` | `06_metricas/tablas_latex/T_barrido_posiciones_mensual_sutil.tex` |
| 47 | T_barrido_delta_s_mensual_sutil | `07_barrido_umbral/mensual/T_barrido_delta_s_mensual_sutil.csv` | `06_metricas/tablas_latex/T_barrido_delta_s_mensual_sutil.tex` |
| 48 | T_barrido_n_shock_mensual_sutil | `07_barrido_umbral/mensual/T_barrido_n_shock_mensual_sutil.csv` | `06_metricas/tablas_latex/T_barrido_n_shock_mensual_sutil.tex` |
| 49 | T_barrido_posiciones_interanual_sutil | `07_barrido_umbral/interanual/T_barrido_posiciones_interanual_sutil.csv` | `06_metricas/tablas_latex/T_barrido_posiciones_interanual_sutil.tex` |
| 50 | T_barrido_delta_s_interanual_sutil | `07_barrido_umbral/interanual/T_barrido_delta_s_interanual_sutil.csv` | `06_metricas/tablas_latex/T_barrido_delta_s_interanual_sutil.tex` |
| 51 | T_barrido_n_shock_interanual_sutil | `07_barrido_umbral/interanual/T_barrido_n_shock_interanual_sutil.csv` | `06_metricas/tablas_latex/T_barrido_n_shock_interanual_sutil.tex` |
| 52 | T_barrido_posiciones_mensual_dulce | `07_barrido_umbral/mensual/T_barrido_posiciones_mensual_dulce.csv` | `06_metricas/tablas_latex/T_barrido_posiciones_mensual_dulce.tex` |
| 53 | T_barrido_delta_s_mensual_dulce | `07_barrido_umbral/mensual/T_barrido_delta_s_mensual_dulce.csv` | `06_metricas/tablas_latex/T_barrido_delta_s_mensual_dulce.tex` |
| 54 | T_barrido_n_shock_mensual_dulce | `07_barrido_umbral/mensual/T_barrido_n_shock_mensual_dulce.csv` | `06_metricas/tablas_latex/T_barrido_n_shock_mensual_dulce.tex` |
| 55 | T_barrido_posiciones_interanual_dulce | `07_barrido_umbral/interanual/T_barrido_posiciones_interanual_dulce.csv` | `06_metricas/tablas_latex/T_barrido_posiciones_interanual_dulce.tex` |
| 56 | T_barrido_delta_s_interanual_dulce | `07_barrido_umbral/interanual/T_barrido_delta_s_interanual_dulce.csv` | `06_metricas/tablas_latex/T_barrido_delta_s_interanual_dulce.tex` |
| 57 | T_barrido_n_shock_interanual_dulce | `07_barrido_umbral/interanual/T_barrido_n_shock_interanual_dulce.csv` | `06_metricas/tablas_latex/T_barrido_n_shock_interanual_dulce.tex` |
| 58 | T_barrido_estabilizacion | `07_barrido_umbral/T_barrido_estabilizacion.csv` | `06_metricas/tablas_latex/T_barrido_estabilizacion.tex` |
| 59 | T_comprobacion_P0 | `07_barrido_umbral/T_comprobacion_P0.csv` | `06_metricas/tablas_latex/T_comprobacion_P0.tex` |

### Comprobación de 2025 (CSV; sin .tex)

| Tabla | CSV |
|---|---|
| Resumen por cultivo y modelo | `06_metricas/reproducibilidad/metricas_2025_vs_oficial.csv` |
| Por corrida (62 filas: GC3, GE y XGB-37 × 10 semillas + SARIMA, por cultivo) | `06_metricas/reproducibilidad/metricas_2025_vs_oficial_por_corrida.csv` |

### Tablas completas en formato largo (anexo; CSV, sin .tex)

| Tabla | CSV |
|---|---|
| T05 completa: modelo × cultivo × ventana × tipo × percentil de reporte | `06_metricas/por_ventana/T05_metricas_por_ventana.csv` |
| T06 completa: agregadas con IC iid y por bloques, ambos conjuntos, P50/P60/P75/P90, mensual e interanual | `06_metricas/agregadas/T06_agregadas_IC.csv` |
| T08 completa: ranking, diferencia con el mejor e indicador 'primero' (iid y bloques) | `06_metricas/agregadas/T08_ranking_empates.csv` |
| T09 completa: DM-HLN por pares, con Holm exploratorio | `06_metricas/significancia/T09_diebold_mariano_hln.csv` |
| T07 completa: métricas por semilla, por ventana y agregadas (P75 mensual) | `06_metricas/por_semilla/T07_metricas_por_semilla.csv` |
| T11 completa: ablación GE − GC3 con la diferencia de cada semilla | `06_metricas/ablacion_nlp/T11_ablacion_GE_menos_GC3.csv` |
| T12 completa: Δs quitando un mes de shock, por ventana y agregado | `06_metricas/agregadas/T12_delta_s_quitando_un_shock.csv` |
| T13 completa: MAE por cuartiles y tercios de |Δy/y| | `06_metricas/agregadas/T13_mae_por_cuartil_cambio.csv` |
| T15 completa: diagnóstico D-BR8 por corrida, con mejor época | `06_metricas/por_semilla/T15_diagnostico_ajuste.csv` |
| T20 candidatos: los 5 candidatos por AIC de SARIMA-sel en cada ventana | `06_metricas/por_ventana/T20_sarima_sel_candidatos.csv` |
| T03 completa: descripción por partición, 2018–2025 | `06_metricas/descripcion_series/T03_descripcion_particiones.csv` |
| T04 completa: ACF, ADF y KPSS (estadísticos, p y retardos) | `06_metricas/descripcion_series/T04_acf_adf_kpss_train.csv` |
| Barrido mensual completo: modelo × percentil | `07_barrido_umbral/mensual/barrido_por_modelo.csv` |
| Barrido interanual completo: modelo × percentil | `07_barrido_umbral/interanual/barrido_por_modelo.csv` |
| n_shock por ventana y percentil (mensual) | `07_barrido_umbral/mensual/n_shock_por_ventana.csv` |
| n_shock por ventana y percentil (interanual) | `07_barrido_umbral/interanual/n_shock_por_ventana.csv` |
| Estabilización del ranking | `07_barrido_umbral/estabilizacion.csv` |
| Comprobación de P0: las 240 comprobaciones | `07_barrido_umbral/comprobacion_P0.csv` |

### Datos (indexados, no impresos)

| Contenido | Archivo |
|---|---|
| Predicciones de todas las particiones y semillas (Fase C), consolidadas | `05_predicciones/predicciones_consolidadas.csv` |
| Error absoluto de test promediado entre semillas (D-BR6), base de todas las métricas | `05_predicciones/errores_test_promediados_semillas.csv` |
| Comprobación de 2025: veredictos, máscaras y SHA-256 de los archivos oficiales | `06_metricas/reproducibilidad/metricas_2025_vs_oficial.json` |
| Comprobación de P0: veredicto | `07_barrido_umbral/comprobacion_P0.json` |

## Estado y alcance

- **Fecha:** 2026-10-28. **Estado:** Fase D1 terminada (tablas y estadística). **Sin figuras** (Fase D2 pendiente). PAUSA.
- **Datos:** predicciones congeladas de la Fase C, commit `09b0945` (488 unidades). No se reentrenó nada.
- **Reproducción:** `venv\Scripts\python.exe v2_reentrenamiento\experimentos_backtesting_rodante\02_scripts\run_all.py --fase D1`. Corre, en orden:
  1. `tests/test_equivalencia_metricas_2025.py`
  2. `08_metricas.py`
  3. `09_barrido_umbral.py`
  4. `09b_reporte_fase_D1.py`
- **Conjuntos:**
  - Principal: ventanas 2021–2025.
  - Sensibilidad: 2023–2025 (D-BR1).
  - Naive, Seasonal Naive y Chronos en 2018–2020: solo descriptivo, sin ranking.
- **XGB-43:** exploratorio (post-hoc), en tabla aparte y fuera del ranking.
- **Reglas aplicadas:** D-BR4 a D-BR8, con la enmienda E-BR1 a D-BR7.
- **Desviaciones:** `09_reportes/DESVIACIONES.md`.
  - DESV-05 (criterio de equivalencia de 2025 para Δs): aprobada.
  - DESV-06 (13 decisiones de implementación): **pendiente de aprobación**.
  - DESV-07 (Holm, exploratorio).
- **No se modificó** `DECISIONES_METODOLOGICAS.md`. No hay commit ni cambio de rama.

## Comprobación previa de 2025

- Se recalcularon las métricas oficiales D35 de GC3, GE y XGB-37 (10 semillas cada uno) y SARIMA rolling con las predicciones de la Fase C, usando los meses de shock oficiales de 2025.
- XGB-37 y SARIMA reproducen todo con diferencias de ≤ 1e-11 t.
- GC3 y GE difieren ≤ 5e-4 t en MAE. Es la diferencia de float32 ya conocida desde la Fase B: los pesos entrenados son idénticos bit a bit.
- El criterio que fijé al escribir la prueba (relativa ≤ 1e-6 en todas las métricas) **falló solo en Δs de Dulce GC3 y GE** (1,18e-6 y 1,43e-6), porque Δs está cerca de 0.
- Se cambió a una tolerancia absoluta de 1e-4 puntos porcentuales para Δs. **Esto se decidió después de ver el resultado** (DESV-05, aprobada). El veredicto original queda guardado.
- La máscara P75 del backtesting para 2025 coincide exactamente con los meses de shock oficiales en los dos cultivos.

## Hallazgos (solo descriptivos; no se elige ningún umbral ni modelo)

1. **Sutil, meses de shock (P75 mensual, 2021–2025, 10 meses):**
   - Chronos tiene el menor MAE_shock (4,784 t).
   - Empatan con él (IC 95 % de la diferencia incluye 0): SARIMA-sel, Seasonal Naive, SARIMA, XGB-37 y GC3.
   - **Robustos** según D-BR7 con E-BR1: **Chronos, SARIMA y SARIMA-sel**.
   - En la sensibilidad 2023–2025: Chronos y SARIMA-sel.
   - En las ventanas 2021 y 2024 no hay ningún shock P75: son no informativas, aunque cuentan en el agregado.
2. **Dulce (15 meses de shock):**
   - SARIMA es primero en P50, P60, P75 y P90 y es **robusto**.
   - SARIMA-sel empata en P50 y P60. En la sensibilidad 2023–2025 son robustos SARIMA y SARIMA-sel.
3. **Meses normales:** el primero es Chronos en Sutil y SARIMA o SARIMA-sel en Dulce.
4. **GC3, GE, XGB-37, Ridge y ElasticNet no son robustos en ningún cultivo.**
   - GC3 y GE tienen Δs cercano a 0, pero su MAE_shock no es bajo.
   - Por E-BR1, un Δs bajo por sí solo no es evidencia de resiliencia.
5. **Barrido P0–P95:**
   - El primer lugar mensual es estable desde P75 en Sutil (Chronos) y desde P0 en Dulce (SARIMA).
   - Nunca empatan todos los modelos.
   - En Dulce interanual, el "estable desde P95" (Naive) es degenerado: n_shock = 1.
6. **P0:** Δs = 0 exacto en las 240 comprobaciones.
7. **Ablación GE − GC3 (emparejada por semilla):**
   - Sutil, global 2021–2025: +382 t, IC [45; 711]. GE es peor y solo 1 de 10 semillas mejora.
   - Dulce, global: +0,1 t, IC [−1,9; 1,9].
   - Dulce, shocks: −2,9 t, IC [−6,2; 0,7]. En la sensibilidad 2023–2025 el de shocks es −4,3 t, IC [−7,2; −1,5].
8. **Diebold-Mariano:**
   - Sin ajustar, en Sutil solo 4 de 45 pares difieren con p < 0,05 en shocks; con Holm (exploratorio) queda 1: Naive peor que Chronos.
   - En Dulce, en shocks, quedan 24 de 31 pares.
   - Global: Sutil 17 de 28; Dulce 28 de 33.
9. **Diagnóstico D-BR8:**
   - XGB-37 (y XGB-43) superan la razón 2 en las 50 corridas por cultivo, con razones de 6 a 26 frente a 0,6–1,4 del Naive. Esto ya estaba declarado.
   - En Sutil, GC3 y GE no superan al Naive en 38 y 39 de 50 corridas.
   - Ninguna LSTM llegó al tope de 300 épocas.
   - En Sutil 2024 la mejor época es temprana (mediana 7,5 en GC3 y 9 en GE).
10. **SARIMA-sel:**
    - Convergió en las 10 unidades, sin órdenes fallidos ni con AIC no finito.
    - El orden elegido varía entre ventanas, con posición en AIC de 1 a 4.
    - En Dulce 2022 coincide con el SARIMA congelado.
11. **Exploratorio XGB-43 frente a XGB-37:**
    - Sutil global: +130 t, IC [1,5; 260].
    - Dulce shocks: −3,6 t, IC [−5,9; −1,2].

## Problemas encontrados y cómo se resolvieron

- **Criterio de equivalencia de 2025:** falló en Δs de Dulce GC3 y GE; se resolvió con DESV-05, decidido después de ver el resultado y aprobado.
- **El `print` final de `09_barrido_umbral.py` falló** por el carácter Δ en la consola de Windows (cp1252). Las salidas ya estaban escritas; se cambió el texto y se volvió a correr.
- **Las vistas de Sutil redondeaban MASE, razones, CV y Δs a enteros.** Se fijaron decimales mínimos por tipo de columna y se regeneraron todas las tablas.

## Qué no se verificó o no se calculó

- **Model Confidence Set:** no calculado, por decisión del autor.
- **Diebold-Mariano:** baja potencia (10 o 15 meses de shock por cultivo). Las ventanas se agrupan, así que la serie no es continua; con h = 1 solo entra la autocovarianza de orden 0.
- **Causa exacta de la diferencia de float32 de GC3/GE:** sigue sin verificar desde la Fase B.
- **Figuras:** no generadas (Fase D2).

## Pendiente de aprobación

1. DESV-06 (13 decisiones de implementación de la Fase D1).
2. Pasar a la Fase D2 (figuras).


## Comprobación previa: ventana 2025 frente a `resultados_v2_final`

- Veredicto (criterio DESV-05): **OK**. Criterio original (relativa ≤ 1e-6 en todo): **no se cumple**.
- Meses de shock oficiales 2025: {'dulce': ['2025-01', '2025-02', '2025-03'], 'sutil': ['2025-01', '2025-07', '2025-11']}.
- Máscara P75 del backtesting 2025: {'sutil': ['2025-01', '2025-07', '2025-11'], 'dulce': ['2025-01', '2025-02', '2025-03']} (coincide: {'sutil': True, 'dulce': True}).
- MAE del Naive t−1: {'sutil': {'nuevo': 4704.292916666665, 'oficial': 4704.292916666665}, 'dulce': {'nuevo': 84.70083333333332, 'oficial': 84.70083333333334}}.

### Resumen por cultivo y modelo (diferencias máximas absolutas; métricas oficiales D35)

Valores exactos (sin redondear; las diferencias son de 1e-16 a 1e-4, por eso no se redondean):

```
cultivar modelo  n_corridas   maxdif_MAE  maxdif_RMSE    maxdif_R2  maxdif_MASE_1  maxdif_RMSSE_1  maxdif_RelMAE_N1  maxdif_MAE_shock  maxdif_MAE_nonshock  maxdif_Delta_s  max_dif_relativa  OK_criterio_original_rel_1e-6   OK
   sutil    GC3          10 3.594840e-04 3.797910e-04 6.470300e-08   1.065270e-07    8.770990e-08      7.641610e-08      3.395120e-04         3.727980e-04    4.694430e-06      1.441660e-07                           True True
   sutil     GE          10 3.994260e-04 3.124380e-04 5.960710e-08   1.183640e-07    7.215520e-08      8.490680e-08      4.793120e-04         3.727980e-04    3.685760e-06      2.171030e-07                           True True
   sutil XGB-37          10 2.728480e-12 1.818990e-12 3.885780e-16   8.881780e-16    4.440890e-16      6.661340e-16      5.456970e-12         1.818990e-12    9.237060e-14      2.240890e-15                           True True
   sutil SARIMA           1 9.094950e-13 1.818990e-12 2.220450e-16   2.220450e-16    4.440890e-16      2.220450e-16      0.000000e+00         1.364240e-12    5.684340e-14      5.899950e-16                           True True
   dulce    GC3          10 3.581330e-06 8.278480e-06 4.057660e-08   4.883320e-08    9.620420e-08      4.228210e-08      8.595190e-06         5.371990e-06    6.035800e-06      1.181210e-06                          False True
   dulce     GE          10 3.984230e-06 5.545950e-06 3.971790e-08   5.432690e-08    6.444950e-08      4.703880e-08      7.162660e-06         5.849500e-06    7.102310e-06      1.433220e-06                          False True
   dulce XGB-37          10 2.842170e-14 2.842170e-14 1.110220e-16   4.440890e-16    3.330670e-16      3.330670e-16      5.684340e-14         2.842170e-14    9.947600e-14      1.828430e-15                           True True
   dulce SARIMA           1 0.000000e+00 3.552710e-15 1.110220e-16   0.000000e+00    5.551120e-17      5.551120e-17      2.131630e-14         1.065810e-14    9.237060e-14      1.978350e-15                           True True
```

### Por corrida (nuevo y oficial)

| cultivar | modelo | seed | MAE | RMSE | R2 | MASE_1 | RMSSE_1 | RelMAE_N1 | MAE_shock | MAE_nonshock | Delta_s | MAE_Naive_t1 | MAE_oficial | RMSE_oficial | R2_oficial | MASE_1_oficial | RMSSE_1_oficial | RelMAE_N1_oficial | MAE_shock_oficial | MAE_nonshock_oficial | Delta_s_oficial |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| sutil | GC3 | 0 | 7,988.5111 | 9,396.9330 | -0.1624 | 2.3673 | 2.1702 | 1.6981 | 5,329.0527 | 8,874.9973 | -33.2910 | 4,704.2929 | 7,988.5111 | 9,396.9330 | -0.1624 | 2.3673 | 2.1702 | 1.6981 | 5,329.0527 | 8,874.9973 | -33.2910 |
| sutil | GC3 | 1 | 8,926.8121 | 10,622.8635 | -0.4855 | 2.6453 | 2.4533 | 1.8976 | 6,946.3040 | 9,586.9815 | -22.1861 | 4,704.2929 | 8,926.8123 | 10,622.8637 | -0.4855 | 2.6453 | 2.4533 | 1.8976 | 6,946.3043 | 9,586.9817 | -22.1861 |
| sutil | GC3 | 2 | 6,748.3614 | 7,725.0667 | 0.2144 | 1.9998 | 1.7840 | 1.4345 | 4,548.4741 | 7,481.6571 | -32.5988 | 4,704.2929 | 6,748.3614 | 7,725.0667 | 0.2144 | 1.9998 | 1.7840 | 1.4345 | 4,548.4744 | 7,481.6571 | -32.5988 |
| sutil | GC3 | 3 | 8,358.1882 | 9,142.8117 | -0.1004 | 2.4768 | 2.1115 | 1.7767 | 6,103.8417 | 9,109.6370 | -26.9717 | 4,704.2929 | 8,358.1881 | 9,142.8117 | -0.1004 | 2.4768 | 2.1115 | 1.7767 | 6,103.8417 | 9,109.6369 | -26.9717 |
| sutil | GC3 | 4 | 7,612.6844 | 8,122.4613 | 0.1315 | 2.2559 | 1.8758 | 1.6182 | 3,909.5109 | 8,847.0756 | -48.6448 | 4,704.2929 | 7,612.6844 | 8,122.4613 | 0.1315 | 2.2559 | 1.8758 | 1.6182 | 3,909.5111 | 8,847.0755 | -48.6448 |
| sutil | GC3 | 5 | 6,105.5352 | 6,442.6440 | 0.4536 | 1.8093 | 1.4879 | 1.2979 | 5,303.8371 | 6,372.7679 | -13.1307 | 4,704.2929 | 6,105.5353 | 6,442.6441 | 0.4536 | 1.8093 | 1.4879 | 1.2979 | 5,303.8371 | 6,372.7680 | -13.1307 |
| sutil | GC3 | 6 | 10,247.1446 | 11,523.8213 | -0.7482 | 3.0366 | 2.6613 | 2.1783 | 7,931.6380 | 11,018.9801 | -22.5966 | 4,704.2929 | 10,247.1447 | 11,523.8213 | -0.7482 | 3.0366 | 2.6613 | 2.1783 | 7,931.6382 | 11,018.9802 | -22.5966 |
| sutil | GC3 | 7 | 9,481.8782 | 10,720.3762 | -0.5129 | 2.8098 | 2.4758 | 2.0156 | 7,536.5260 | 10,130.3289 | -20.5165 | 4,704.2929 | 9,481.8782 | 10,720.3762 | -0.5129 | 2.8098 | 2.4758 | 2.0156 | 7,536.5260 | 10,130.3290 | -20.5165 |
| sutil | GC3 | 8 | 6,230.2970 | 6,470.7062 | 0.4488 | 1.8462 | 1.4944 | 1.3244 | 4,392.0875 | 6,843.0335 | -29.5044 | 4,704.2929 | 6,230.2974 | 6,470.7066 | 0.4488 | 1.8462 | 1.4944 | 1.3244 | 4,392.0878 | 6,843.0339 | -29.5044 |
| sutil | GC3 | 9 | 5,760.5891 | 6,672.9258 | 0.4138 | 1.7071 | 1.5411 | 1.2245 | 3,939.8173 | 6,367.5131 | -31.6074 | 4,704.2929 | 5,760.5891 | 6,672.9258 | 0.4138 | 1.7071 | 1.5411 | 1.2245 | 3,939.8171 | 6,367.5132 | -31.6074 |
| sutil | GE | 0 | 11,131.0939 | 12,892.7805 | -1.1882 | 3.2985 | 2.9775 | 2.3662 | 9,072.6859 | 11,817.2299 | -18.4924 | 4,704.2929 | 11,131.0939 | 12,892.7805 | -1.1882 | 3.2985 | 2.9775 | 2.3662 | 9,072.6860 | 11,817.2299 | -18.4924 |
| sutil | GE | 1 | 10,513.0559 | 12,285.2248 | -0.9868 | 3.1154 | 2.8372 | 2.2348 | 9,001.9631 | 11,016.7536 | -14.3735 | 4,704.2929 | 10,513.0559 | 12,285.2247 | -0.9868 | 3.1154 | 2.8372 | 2.2348 | 9,001.9632 | 11,016.7535 | -14.3735 |
| sutil | GE | 2 | 8,216.8524 | 9,426.5403 | -0.1698 | 2.4349 | 2.1770 | 1.7467 | 7,274.5135 | 8,530.9653 | -11.4684 | 4,704.2929 | 8,216.8525 | 9,426.5405 | -0.1698 | 2.4349 | 2.1770 | 1.7467 | 7,274.5135 | 8,530.9655 | -11.4684 |
| sutil | GE | 3 | 9,109.4553 | 10,542.5880 | -0.4632 | 2.6994 | 2.4347 | 1.9364 | 9,044.6665 | 9,131.0516 | -0.7112 | 4,704.2929 | 9,109.4552 | 10,542.5879 | -0.4632 | 2.6994 | 2.4347 | 1.9364 | 9,044.6664 | 9,131.0515 | -0.7112 |
| sutil | GE | 4 | 9,252.5533 | 10,993.4095 | -0.5910 | 2.7418 | 2.5388 | 1.9668 | 8,257.7571 | 9,584.1520 | -10.7516 | 4,704.2929 | 9,252.5535 | 10,993.4096 | -0.5910 | 2.7418 | 2.5388 | 1.9668 | 8,257.7574 | 9,584.1522 | -10.7516 |
| sutil | GE | 5 | 8,847.5402 | 9,839.6663 | -0.2746 | 2.6218 | 2.2724 | 1.8807 | 7,124.4302 | 9,421.9101 | -19.4756 | 4,704.2929 | 8,847.5400 | 9,839.6661 | -0.2746 | 2.6218 | 2.2724 | 1.8807 | 7,124.4299 | 9,421.9101 | -19.4756 |
| sutil | GE | 6 | 10,698.2967 | 12,161.1618 | -0.9469 | 3.1703 | 2.8085 | 2.2742 | 8,400.0265 | 11,464.3868 | -21.4826 | 4,704.2929 | 10,698.2968 | 12,161.1618 | -0.9469 | 3.1703 | 2.8085 | 2.2742 | 8,400.0265 | 11,464.3868 | -21.4826 |
| sutil | GE | 7 | 10,416.7952 | 11,905.1343 | -0.8658 | 3.0868 | 2.7494 | 2.2143 | 8,349.1322 | 11,106.0161 | -19.8493 | 4,704.2929 | 10,416.7952 | 11,905.1343 | -0.8658 | 3.0868 | 2.7494 | 2.2143 | 8,349.1322 | 11,106.0162 | -19.8493 |
| sutil | GE | 8 | 6,129.1855 | 6,656.1795 | 0.4168 | 1.8163 | 1.5372 | 1.3029 | 3,888.4874 | 6,876.0848 | -36.5578 | 4,704.2929 | 6,129.1851 | 6,656.1792 | 0.4168 | 1.8163 | 1.5372 | 1.3029 | 3,888.4869 | 6,876.0845 | -36.5578 |
| sutil | GE | 9 | 9,949.7585 | 11,598.8166 | -0.7710 | 2.9485 | 2.6787 | 2.1150 | 8,671.2171 | 10,375.9390 | -12.8500 | 4,704.2929 | 9,949.7585 | 11,598.8167 | -0.7710 | 2.9485 | 2.6787 | 2.1150 | 8,671.2169 | 10,375.9391 | -12.8500 |
| sutil | XGB-37 | 0 | 6,065.3255 | 7,087.4335 | 0.3387 | 1.7974 | 1.6368 | 1.2893 | 8,314.1148 | 5,315.7290 | 37.0762 | 4,704.2929 | 6,065.3255 | 7,087.4335 | 0.3387 | 1.7974 | 1.6368 | 1.2893 | 8,314.1148 | 5,315.7290 | 37.0762 |
| sutil | XGB-37 | 1 | 5,848.7960 | 6,994.4616 | 0.3560 | 1.7332 | 1.6153 | 1.2433 | 8,250.0252 | 5,048.3862 | 41.0551 | 4,704.2929 | 5,848.7960 | 6,994.4616 | 0.3560 | 1.7332 | 1.6153 | 1.2433 | 8,250.0252 | 5,048.3862 | 41.0551 |
| sutil | XGB-37 | 2 | 5,919.3098 | 7,080.6607 | 0.3400 | 1.7541 | 1.6352 | 1.2583 | 8,112.1419 | 5,188.3658 | 37.0454 | 4,704.2929 | 5,919.3098 | 7,080.6607 | 0.3400 | 1.7541 | 1.6352 | 1.2583 | 8,112.1419 | 5,188.3658 | 37.0454 |
| sutil | XGB-37 | 3 | 5,872.0443 | 7,068.9045 | 0.3422 | 1.7401 | 1.6325 | 1.2482 | 8,543.0337 | 4,981.7145 | 45.4865 | 4,704.2929 | 5,872.0443 | 7,068.9045 | 0.3422 | 1.7401 | 1.6325 | 1.2482 | 8,543.0337 | 4,981.7145 | 45.4865 |
| sutil | XGB-37 | 4 | 5,775.3154 | 6,923.5035 | 0.3690 | 1.7114 | 1.5989 | 1.2277 | 8,407.4006 | 4,897.9537 | 45.5747 | 4,704.2929 | 5,775.3154 | 6,923.5035 | 0.3690 | 1.7114 | 1.5989 | 1.2277 | 8,407.4006 | 4,897.9537 | 45.5747 |
| sutil | XGB-37 | 5 | 5,919.9140 | 6,891.7226 | 0.3747 | 1.7543 | 1.5916 | 1.2584 | 7,830.1568 | 5,283.1664 | 32.2681 | 4,704.2929 | 5,919.9140 | 6,891.7226 | 0.3747 | 1.7543 | 1.5916 | 1.2584 | 7,830.1568 | 5,283.1664 | 32.2681 |
| sutil | XGB-37 | 6 | 5,626.9161 | 6,834.9804 | 0.3850 | 1.6674 | 1.5785 | 1.1961 | 8,214.7905 | 4,764.2913 | 45.9910 | 4,704.2929 | 5,626.9161 | 6,834.9804 | 0.3850 | 1.6674 | 1.5785 | 1.1961 | 8,214.7905 | 4,764.2913 | 45.9910 |
| sutil | XGB-37 | 7 | 5,867.3526 | 7,017.6799 | 0.3517 | 1.7387 | 1.6207 | 1.2472 | 8,147.6500 | 5,107.2534 | 38.8642 | 4,704.2929 | 5,867.3526 | 7,017.6799 | 0.3517 | 1.7387 | 1.6207 | 1.2472 | 8,147.6500 | 5,107.2534 | 38.8642 |
| sutil | XGB-37 | 8 | 6,059.9726 | 7,103.1253 | 0.3358 | 1.7958 | 1.6404 | 1.2882 | 8,557.9177 | 5,227.3242 | 41.2204 | 4,704.2929 | 6,059.9726 | 7,103.1253 | 0.3358 | 1.7958 | 1.6404 | 1.2882 | 8,557.9177 | 5,227.3242 | 41.2204 |
| sutil | XGB-37 | 9 | 6,068.8074 | 7,105.3806 | 0.3354 | 1.7984 | 1.6409 | 1.2901 | 8,591.7340 | 5,227.8319 | 41.5720 | 4,704.2929 | 6,068.8074 | 7,105.3806 | 0.3354 | 1.7984 | 1.6409 | 1.2901 | 8,591.7340 | 5,227.8319 | 41.5720 |
| sutil | SARIMA | -1 | 3,985.0165 | 4,894.8964 | 0.6846 | 1.1809 | 1.1304 | 0.8471 | 7,824.4029 | 2,705.2210 | 96.3456 | 4,704.2929 | 3,985.0165 | 4,894.8964 | 0.6846 | 1.1809 | 1.1304 | 0.8471 | 7,824.4029 | 2,705.2210 | 96.3456 |
| dulce | GC3 | 0 | 103.5998 | 120.5542 | 0.4955 | 1.4126 | 1.4010 | 1.2231 | 124.2334 | 96.7220 | 19.9166 | 84.7008 | 103.5998 | 120.5542 | 0.4955 | 1.4126 | 1.4010 | 1.2231 | 124.2334 | 96.7220 | 19.9166 |
| dulce | GC3 | 1 | 109.3038 | 137.4185 | 0.3444 | 1.4904 | 1.5969 | 1.2905 | 148.6819 | 96.1778 | 36.0263 | 84.7008 | 109.3038 | 137.4185 | 0.3444 | 1.4904 | 1.5969 | 1.2905 | 148.6819 | 96.1778 | 36.0263 |
| dulce | GC3 | 2 | 126.3325 | 153.8544 | 0.1783 | 1.7226 | 1.7879 | 1.4915 | 163.0264 | 114.1012 | 29.0456 | 84.7008 | 126.3325 | 153.8544 | 0.1783 | 1.7226 | 1.7879 | 1.4915 | 163.0264 | 114.1011 | 29.0456 |
| dulce | GC3 | 3 | 92.5546 | 110.9216 | 0.5729 | 1.2620 | 1.2890 | 1.0927 | 88.0510 | 94.0558 | -4.8659 | 84.7008 | 92.5546 | 110.9216 | 0.5729 | 1.2620 | 1.2890 | 1.0927 | 88.0510 | 94.0558 | -4.8659 |
| dulce | GC3 | 4 | 128.9582 | 148.3270 | 0.2362 | 1.7584 | 1.7237 | 1.5225 | 135.5197 | 126.7710 | 5.0881 | 84.7008 | 128.9582 | 148.3270 | 0.2362 | 1.7584 | 1.7237 | 1.5225 | 135.5197 | 126.7710 | 5.0881 |
| dulce | GC3 | 5 | 57.5816 | 70.5957 | 0.8270 | 0.7852 | 0.8204 | 0.6798 | 48.1944 | 60.7107 | -16.3025 | 84.7008 | 57.5816 | 70.5957 | 0.8270 | 0.7852 | 0.8204 | 0.6798 | 48.1944 | 60.7107 | -16.3025 |
| dulce | GC3 | 6 | 119.9509 | 146.6953 | 0.2530 | 1.6356 | 1.7047 | 1.4162 | 128.5996 | 117.0680 | 7.2102 | 84.7008 | 119.9509 | 146.6953 | 0.2530 | 1.6356 | 1.7047 | 1.4162 | 128.5996 | 117.0680 | 7.2102 |
| dulce | GC3 | 7 | 94.3790 | 111.5729 | 0.5679 | 1.2869 | 1.2966 | 1.1143 | 116.4811 | 87.0117 | 23.4184 | 84.7008 | 94.3790 | 111.5730 | 0.5679 | 1.2869 | 1.2966 | 1.1143 | 116.4811 | 87.0117 | 23.4184 |
| dulce | GC3 | 8 | 96.7459 | 127.3682 | 0.4368 | 1.3192 | 1.4801 | 1.1422 | 90.2251 | 98.9195 | -6.7401 | 84.7008 | 96.7459 | 127.3682 | 0.4368 | 1.3192 | 1.4801 | 1.1422 | 90.2251 | 98.9195 | -6.7401 |
| dulce | GC3 | 9 | 104.7239 | 125.8735 | 0.4500 | 1.4280 | 1.4628 | 1.2364 | 146.4293 | 90.8221 | 39.8241 | 84.7008 | 104.7239 | 125.8735 | 0.4500 | 1.4280 | 1.4628 | 1.2364 | 146.4293 | 90.8221 | 39.8241 |
| dulce | GE | 0 | 86.3830 | 103.1487 | 0.6306 | 1.1779 | 1.1987 | 1.0199 | 98.0771 | 82.4850 | 13.5374 | 84.7008 | 86.3830 | 103.1487 | 0.6306 | 1.1779 | 1.1987 | 1.0199 | 98.0771 | 82.4850 | 13.5374 |
| dulce | GE | 1 | 107.5422 | 137.6278 | 0.3425 | 1.4664 | 1.5994 | 1.2697 | 140.0532 | 96.7052 | 30.2309 | 84.7008 | 107.5422 | 137.6278 | 0.3425 | 1.4664 | 1.5994 | 1.2697 | 140.0532 | 96.7052 | 30.2309 |
| dulce | GE | 2 | 117.6832 | 137.0850 | 0.3476 | 1.6047 | 1.5931 | 1.3894 | 142.3668 | 109.4553 | 20.9747 | 84.7008 | 117.6832 | 137.0850 | 0.3476 | 1.6047 | 1.5931 | 1.3894 | 142.3669 | 109.4553 | 20.9747 |
| dulce | GE | 3 | 77.8396 | 98.7657 | 0.6614 | 1.0614 | 1.1478 | 0.9190 | 68.8989 | 80.8199 | -11.4862 | 84.7008 | 77.8396 | 98.7656 | 0.6614 | 1.0614 | 1.1478 | 0.9190 | 68.8989 | 80.8199 | -11.4862 |
| dulce | GE | 4 | 103.5132 | 124.3753 | 0.4630 | 1.4115 | 1.4454 | 1.2221 | 106.7076 | 102.4483 | 3.0861 | 84.7008 | 103.5132 | 124.3753 | 0.4630 | 1.4115 | 1.4454 | 1.2221 | 106.7076 | 102.4483 | 3.0860 |
| dulce | GE | 5 | 53.7216 | 67.1188 | 0.8436 | 0.7325 | 0.7800 | 0.6343 | 38.4281 | 58.8194 | -28.4681 | 84.7008 | 53.7216 | 67.1188 | 0.8436 | 0.7325 | 0.7800 | 0.6343 | 38.4281 | 58.8194 | -28.4681 |
| dulce | GE | 6 | 115.9415 | 144.0221 | 0.2799 | 1.5809 | 1.6737 | 1.3688 | 95.7288 | 122.6790 | -17.4335 | 84.7008 | 115.9415 | 144.0221 | 0.2799 | 1.5809 | 1.6737 | 1.3688 | 95.7288 | 122.6790 | -17.4335 |
| dulce | GE | 7 | 103.6165 | 127.5803 | 0.4350 | 1.4129 | 1.4826 | 1.2233 | 126.5074 | 95.9862 | 22.0919 | 84.7008 | 103.6165 | 127.5803 | 0.4350 | 1.4129 | 1.4826 | 1.2233 | 126.5074 | 95.9862 | 22.0919 |
| dulce | GE | 8 | 83.0995 | 99.4616 | 0.6566 | 1.1331 | 1.1558 | 0.9811 | 57.9765 | 91.4738 | -30.2324 | 84.7008 | 83.0995 | 99.4616 | 0.6566 | 1.1331 | 1.1558 | 0.9811 | 57.9765 | 91.4738 | -30.2324 |
| dulce | GE | 9 | 106.5053 | 129.8119 | 0.4150 | 1.4523 | 1.5085 | 1.2574 | 124.3315 | 100.5632 | 16.7374 | 84.7008 | 106.5053 | 129.8119 | 0.4150 | 1.4523 | 1.5085 | 1.2574 | 124.3315 | 100.5632 | 16.7374 |
| dulce | XGB-37 | 0 | 56.0483 | 72.9210 | 0.8154 | 0.7642 | 0.8474 | 0.6617 | 86.5415 | 45.8839 | 54.4052 | 84.7008 | 56.0483 | 72.9210 | 0.8154 | 0.7642 | 0.8474 | 0.6617 | 86.5415 | 45.8839 | 54.4052 |
| dulce | XGB-37 | 1 | 58.8372 | 74.7441 | 0.8061 | 0.8023 | 0.8686 | 0.6946 | 83.4278 | 50.6403 | 41.7944 | 84.7008 | 58.8372 | 74.7441 | 0.8061 | 0.8023 | 0.8686 | 0.6946 | 83.4278 | 50.6403 | 41.7944 |
| dulce | XGB-37 | 2 | 60.9382 | 79.4503 | 0.7809 | 0.8309 | 0.9233 | 0.7195 | 94.2719 | 49.8270 | 54.7007 | 84.7008 | 60.9382 | 79.4503 | 0.7809 | 0.8309 | 0.9233 | 0.7195 | 94.2719 | 49.8270 | 54.7007 |
| dulce | XGB-37 | 3 | 60.4821 | 77.2041 | 0.7931 | 0.8247 | 0.8972 | 0.7141 | 91.5502 | 50.1260 | 51.3675 | 84.7008 | 60.4821 | 77.2041 | 0.7931 | 0.8247 | 0.8972 | 0.7141 | 91.5502 | 50.1260 | 51.3675 |
| dulce | XGB-37 | 4 | 56.9879 | 75.7354 | 0.8009 | 0.7771 | 0.8801 | 0.6728 | 85.5388 | 47.4709 | 50.1000 | 84.7008 | 56.9879 | 75.7354 | 0.8009 | 0.7771 | 0.8801 | 0.6728 | 85.5388 | 47.4709 | 50.1000 |
| dulce | XGB-37 | 5 | 64.1732 | 84.9332 | 0.7496 | 0.8750 | 0.9870 | 0.7576 | 97.8249 | 52.9559 | 52.4389 | 84.7008 | 64.1732 | 84.9332 | 0.7496 | 0.8750 | 0.9870 | 0.7576 | 97.8249 | 52.9559 | 52.4389 |
| dulce | XGB-37 | 6 | 60.3741 | 78.5279 | 0.7859 | 0.8232 | 0.9126 | 0.7128 | 91.4786 | 50.0059 | 51.5196 | 84.7008 | 60.3741 | 78.5279 | 0.7859 | 0.8232 | 0.9126 | 0.7128 | 91.4786 | 50.0059 | 51.5196 |
| dulce | XGB-37 | 7 | 59.4982 | 77.3700 | 0.7922 | 0.8113 | 0.8991 | 0.7025 | 94.7673 | 47.7418 | 59.2777 | 84.7008 | 59.4982 | 77.3700 | 0.7922 | 0.8113 | 0.8991 | 0.7025 | 94.7673 | 47.7418 | 59.2777 |
| dulce | XGB-37 | 8 | 59.9092 | 77.2170 | 0.7930 | 0.8169 | 0.8973 | 0.7073 | 85.5841 | 51.3509 | 42.8564 | 84.7008 | 59.9092 | 77.2170 | 0.7930 | 0.8169 | 0.8973 | 0.7073 | 85.5841 | 51.3509 | 42.8564 |
| dulce | XGB-37 | 9 | 56.5405 | 73.9538 | 0.8101 | 0.7710 | 0.8594 | 0.6675 | 90.0598 | 45.3674 | 59.2837 | 84.7008 | 56.5405 | 73.9538 | 0.8101 | 0.7710 | 0.8594 | 0.6675 | 90.0598 | 45.3674 | 59.2837 |
| dulce | SARIMA | -1 | 21.7668 | 31.6165 | 0.9653 | 0.2968 | 0.3674 | 0.2570 | 11.6037 | 25.1544 | -46.6907 | 84.7008 | 21.7668 | 31.6165 | 0.9653 | 0.2968 | 0.3674 | 0.2570 | 11.6037 | 25.1544 | -46.6907 |

## Tablas de resultados (vistas)

### Ta_consolidado_resumen — Consolidado de predicciones de test: error absoluto promediado entre semillas (D-BR6)

| modelo | ventanas | meses_test | semillas |
|---|---|---|---|
| Naive | 2018–2025 | 192 | 1 |
| Seasonal Naive | 2018–2025 | 192 | 1 |
| Chronos | 2018–2025 | 192 | 1 |
| SARIMA | 2021–2025 | 120 | 1 |
| SARIMA-sel | 2021–2025 | 120 | 1 |
| Ridge | 2021–2025 | 120 | 1 |
| ElasticNet | 2021–2025 | 120 | 1 |
| XGB-37 | 2021–2025 | 120 | 10 |
| GC3 | 2021–2025 | 120 | 10 |
| GE | 2021–2025 | 120 | 10 |
| XGB-43 | 2021–2025 | 120 | 10 |

### T05_MAE_P75_por_ventana_sutil — MAE por ventana, P75 mensual, Sutil (t)

| modelo | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Naive | 1,986 | 3,762 | 4,590 | 3,078 | 4,704 |
| Seasonal Naive | 4,590 | 4,136 | 7,638 | 9,850 | 4,160 |
| Chronos | 2,541 | 2,205 | 3,157 | 2,023 | 3,316 |
| SARIMA | 3,208 | 3,061 | 3,693 | 2,858 | 3,985 |
| SARIMA-sel | 2,304 | 2,609 | 3,836 | 3,333 | 3,947 |
| Ridge | 3,108 | 3,187 | 10,778 | 4,322 | 3,232 |
| ElasticNet | 3,006 | 2,968 | 10,413 | 4,751 | 3,223 |
| XGB-37 | 5,211 | 4,552 | 3,785 | 4,957 | 5,902 |
| GC3 | 3,856 | 5,162 | 6,074 | 8,969 | 7,746 |
| GE | 3,867 | 5,260 | 5,391 | 9,774 | 9,426 |
| XGB-43 | 5,333 | 4,664 | 3,679 | 5,466 | 5,918 |

### T05_MAE_shock_P75_por_ventana_sutil — MAE_shock por ventana, P75 mensual, Sutil (t)

| modelo | 2021 (n=0) | 2022 (n=3) | 2023 (n=4) | 2024 (n=0) | 2025 (n=3) |
|---|---|---|---|---|---|
| Naive | — | 8,522 | 6,129 | — | 11,660 |
| Seasonal Naive | — | 4,472 | 6,135 | — | 4,130 |
| Chronos | — | 4,852 | 3,454 | — | 6,487 |
| SARIMA | — | 3,905 | 4,030 | — | 7,824 |
| SARIMA-sel | — | 4,207 | 4,158 | — | 6,701 |
| Ridge | — | 4,394 | 12,714 | — | 7,177 |
| ElasticNet | — | 4,015 | 11,806 | — | 7,423 |
| XGB-37 | — | 5,234 | 4,740 | — | 8,297 |
| GC3 | — | 4,916 | 7,304 | — | 5,594 |
| GE | — | 5,202 | 7,234 | — | 7,908 |
| XGB-43 | — | 5,374 | 4,656 | — | 8,408 |

### T17_descriptivo_2018_2020_sutil — Descriptivo 2018-2020 (sin ranking), modelos sin entrenamiento, P75 mensual, Sutil

| modelo | anio_test | MAE | RMSE | MASE | MAE_normal | MAE_shock | n_shock | Delta_s | informativa |
|---|---|---|---|---|---|---|---|---|---|
| Naive | 2018 | 2,727 | 3,748 | — | 971 | 6,237 | 4 | 128.7 | sí |
| Naive | 2019 | 3,562 | 4,404 | 0.37 | 2,335 | 7,245 | 3 | 103.4 | sí |
| Naive | 2020 | 4,102 | 5,222 | 0.45 | 2,866 | 7,809 | 3 | 90.4 | sí |
| Seasonal Naive | 2018 | 8,317 | 8,868 | — | 8,674 | 7,601 | 4 | -8.6 | sí |
| Seasonal Naive | 2019 | 3,728 | 4,381 | 0.38 | 4,221 | 2,250 | 3 | -39.7 | sí |
| Seasonal Naive | 2020 | 2,443 | 3,183 | 0.27 | 1,751 | 4,516 | 3 | 84.9 | sí |
| Chronos | 2018 | 1,973 | 2,890 | — | 567 | 4,787 | 4 | 142.6 | sí |
| Chronos | 2019 | 2,702 | 3,423 | 0.28 | 2,036 | 4,697 | 3 | 73.9 | sí |
| Chronos | 2020 | 2,931 | 3,734 | 0.32 | 1,959 | 5,848 | 3 | 99.5 | sí |

### T05_MAE_P75_por_ventana_dulce — MAE por ventana, P75 mensual, Dulce (t)

| modelo | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Naive | 67.8 | 73.3 | 76.2 | 85.6 | 84.7 |
| Seasonal Naive | 18.4 | 19.9 | 11.8 | 41.8 | 30.5 |
| Chronos | 19.2 | 30.0 | 30.4 | 39.9 | 34.6 |
| SARIMA | 13.7 | 12.4 | 18.8 | 25.5 | 21.8 |
| SARIMA-sel | 27.9 | 12.4 | 17.4 | 25.6 | 19.8 |
| Ridge | 37.9 | 35.5 | 43.6 | 97.7 | 50.6 |
| ElasticNet | 37.6 | 35.2 | 43.4 | 85.7 | 49.3 |
| XGB-37 | 25.7 | 52.3 | 45.8 | 58.0 | 59.4 |
| GC3 | 36.5 | 37.2 | 38.0 | 68.2 | 103.4 |
| GE | 41.1 | 37.5 | 42.2 | 67.3 | 95.6 |
| XGB-43 | 26.2 | 52.2 | 44.3 | 54.1 | 61.4 |

### T05_MAE_shock_P75_por_ventana_dulce — MAE_shock por ventana, P75 mensual, Dulce (t)

| modelo | 2021 (n=3) | 2022 (n=3) | 2023 (n=2) | 2024 (n=4) | 2025 (n=3) |
|---|---|---|---|---|---|
| Naive | 120.6 | 123.0 | 140.7 | 136.8 | 138.3 |
| Seasonal Naive | 16.0 | 31.5 | 7.4 | 33.2 | 25.9 |
| Chronos | 26.1 | 48.9 | 43.8 | 57.5 | 60.1 |
| SARIMA | 4.3 | 12.9 | 8.8 | 26.4 | 11.6 |
| SARIMA-sel | 34.9 | 12.9 | 7.5 | 25.9 | 11.0 |
| Ridge | 41.9 | 54.1 | 29.3 | 106.5 | 90.9 |
| ElasticNet | 43.5 | 53.5 | 29.7 | 96.5 | 90.7 |
| XGB-37 | 42.2 | 79.6 | 72.2 | 51.9 | 90.1 |
| GC3 | 43.7 | 44.3 | 50.9 | 47.1 | 118.9 |
| GE | 43.8 | 42.7 | 52.5 | 51.0 | 99.9 |
| XGB-43 | 40.0 | 78.9 | 73.3 | 45.9 | 82.3 |

### T17_descriptivo_2018_2020_dulce — Descriptivo 2018-2020 (sin ranking), modelos sin entrenamiento, P75 mensual, Dulce

| modelo | anio_test | MAE | RMSE | MASE | MAE_normal | MAE_shock | n_shock | Delta_s | informativa |
|---|---|---|---|---|---|---|---|---|---|
| Naive | 2018 | 72.3 | 85.2 | — | 52.5 | 112.0 | 4 | 54.8 | sí |
| Naive | 2019 | 74.9 | 84.9 | 1.98 | 53.1 | 118.5 | 4 | 58.3 | sí |
| Naive | 2020 | 66.7 | 84.0 | 2.03 | 40.9 | 118.2 | 4 | 77.2 | sí |
| Seasonal Naive | 2018 | 28.0 | 31.4 | — | 25.1 | 33.6 | 4 | 20.3 | sí |
| Seasonal Naive | 2019 | 29.4 | 38.5 | 0.78 | 33.4 | 21.4 | 4 | -27.0 | sí |
| Seasonal Naive | 2020 | 17.1 | 21.9 | 0.52 | 21.3 | 8.8 | 4 | -48.9 | sí |
| Chronos | 2018 | 31.8 | 38.1 | — | 23.4 | 48.7 | 4 | 52.8 | sí |
| Chronos | 2019 | 33.5 | 36.5 | 0.89 | 32.2 | 35.9 | 4 | 7.4 | sí |
| Chronos | 2020 | 28.8 | 34.0 | 0.88 | 29.3 | 27.7 | 4 | -3.5 | sí |

### T06_agregadas_P75_principal_2021_2025_sutil — Métricas agregadas 2021-2025, P75 mensual, Sutil (t; IC bootstrap pareado 95 %)

| modelo | MAE | IC95 MAE | MAE normal | IC95 normal | MAE shock | IC95 shock | IC95 shock (bloques) | n shock | Δs % | shock/normal | MASE | RMSE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 3,624 | [2,920; 4,382] | 2,648 | [2,102; 3,226] | 8,506 | [7,724; 9,215] | [7,225; 10,123] | 10 | 134.7 | 3.21 | 0.61 | 4,768 |
| Seasonal Naive | 6,075 | [5,156; 6,987] | 6,283 | [5,323; 7,211] | 5,034 | [2,259; 7,928] | [1,922; 8,266] | 10 | -17.1 | 0.80 | 1.03 | 7,451 |
| Chronos | 2,649 | [2,171; 3,144] | 2,222 | [1,786; 2,701] | 4,784 | [3,963; 5,641] | [3,873; 5,845] | 10 | 80.6 | 2.15 | 0.44 | 3,308 |
| SARIMA | 3,361 | [2,780; 3,970] | 3,007 | [2,443; 3,589] | 5,131 | [3,759; 6,624] | [3,657; 6,690] | 10 | 52.7 | 1.71 | 0.56 | 4,123 |
| SARIMA-sel | 3,206 | [2,563; 3,880] | 2,860 | [2,272; 3,469] | 4,936 | [2,866; 7,242] | [2,683; 7,067] | 10 | 54.0 | 1.73 | 0.54 | 4,177 |
| Ridge | 4,925 | [3,838; 6,074] | 4,199 | [3,099; 5,331] | 8,557 | [5,484; 12,360] | [5,298; 11,724] | 10 | 73.7 | 2.04 | 0.83 | 7,301 |
| ElasticNet | 4,872 | [3,847; 5,950] | 4,216 | [3,172; 5,298] | 8,154 | [5,162; 11,484] | [5,106; 10,922] | 10 | 67.4 | 1.93 | 0.83 | 7,051 |
| XGB-37 | 4,881 | [4,063; 5,732] | 4,667 | [3,831; 5,544] | 5,955 | [3,727; 7,965] | [3,330; 8,559] | 10 | 22.0 | 1.28 | 0.81 | 5,940 |
| GC3 | 6,361 | [5,292; 7,446] | 6,419 | [5,215; 7,644] | 6,074 | [4,085; 8,216] | [4,022; 7,942] | 10 | -4.5 | 0.95 | 1.08 | 8,073 |
| GE | 6,744 | [5,587; 7,894] | 6,727 | [5,454; 8,024] | 6,827 | [4,477; 9,213] | [4,284; 9,135] | 10 | 1.2 | 1.01 | 1.15 | 8,648 |

### T08_ranking_shock_principal_2021_2025_sutil — Ranking por MAE_shock (2021-2025, Sutil): posición; * = primero o empatado con el primero (IC95 iid de la diferencia contiene 0)

| modelo | sh-men-P50 | sh-men-P60 | sh-men-P75 | sh-men-P90 | sh-men primero en | sh-int-P50 | sh-int-P60 | sh-int-P75 | sh-int-P90 | sh-int primero en | robusto men | robusto int | robusto men (bloques) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 5 | 8 | 9 | 7 | 0 | 2* | 2* | 2* | 2* | 4 | no | sí | no |
| Seasonal Naive | 6 | 5 | 3* | 4* | 2 | 10 | 10 | 10 | 10 | 0 | no | no | no |
| Chronos | 2* | 3* | 1* | 1* | 4 | 1* | 1* | 1* | 1* | 4 | sí | sí | sí |
| SARIMA | 3* | 2* | 4* | 2 | 3 | 3* | 3* | 3 | 3 | 2 | sí | no | sí |
| SARIMA-sel | 1* | 1* | 2* | 3 | 3 | 4* | 4 | 4 | 6 | 1 | sí | no | sí |
| Ridge | 9 | 10 | 10 | 10 | 0 | 6 | 6 | 6 | 4 | 0 | no | no | no |
| ElasticNet | 10 | 9 | 8 | 9 | 0 | 7 | 7 | 7 | 5 | 0 | no | no | no |
| XGB-37 | 4 | 4 | 5* | 6 | 1 | 5 | 5 | 5 | 7* | 1 | no | no | no |
| GC3 | 8 | 6 | 6* | 5 | 1 | 9 | 8 | 8 | 8 | 0 | no | no | no |
| GE | 7 | 7 | 7 | 8 | 0 | 8 | 9 | 9 | 9 | 0 | no | no | no |

### T08_ranking_normal_principal_2021_2025_sutil — Ranking por MAE normal (2021-2025, Sutil): posición; * = primero o empatado

| modelo | no-men-P50 | no-men-P60 | no-men-P75 | no-men-P90 | no-men primero en | no-int-P50 | no-int-P60 | no-int-P75 | no-int-P90 | no-int primero en |
|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 1* | 1* | 2* | 4 | 3 | 5 | 4 | 4 | 4 | 0 |
| Seasonal Naive | 8 | 8 | 8 | 8 | 0 | 4 | 5 | 6 | 8 | 0 |
| Chronos | 2* | 2* | 1* | 1* | 4 | 1* | 1* | 1* | 1* | 4 |
| SARIMA | 6 | 6 | 4 | 3 | 0 | 3 | 3 | 3* | 3* | 2 |
| SARIMA-sel | 4 | 3 | 3* | 2* | 2 | 2* | 2* | 2* | 2* | 4 |
| Ridge | 5 | 5 | 5 | 5 | 0 | 7 | 7 | 8 | 7 | 0 |
| ElasticNet | 3 | 4 | 6 | 6 | 0 | 6 | 6 | 5 | 6 | 0 |
| XGB-37 | 7 | 7 | 7 | 7 | 0 | 8 | 8 | 7 | 5 | 0 |
| GC3 | 9 | 9 | 9 | 9 | 0 | 9 | 9 | 9 | 9 | 0 |
| GE | 10 | 10 | 10 | 10 | 0 | 10 | 10 | 10 | 10 | 0 |

### T06_agregadas_P75_principal_2021_2025_dulce — Métricas agregadas 2021-2025, P75 mensual, Dulce (t; IC bootstrap pareado 95 %)

| modelo | MAE | IC95 MAE | MAE normal | IC95 normal | MAE shock | IC95 shock | IC95 shock (bloques) | n shock | Δs % | shock/normal | MASE | RMSE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 77.5 | [65.7; 89.9] | 59.5 | [48.6; 71.0] | 131.6 | [116.5; 147.7] | [117.4; 147.1] | 15 | 69.8 | 2.21 | 2.95 | 91.3 |
| Seasonal Naive | 24.5 | [20.5; 29.0] | 24.5 | [19.3; 30.2] | 24.5 | [21.4; 27.8] | [18.8; 30.4] | 15 | -0.0 | 1.00 | 0.95 | 31.6 |
| Chronos | 30.8 | [25.6; 36.4] | 25.0 | [19.8; 30.9] | 48.2 | [40.5; 56.1] | [38.1; 58.3] | 15 | 56.4 | 1.93 | 1.18 | 37.9 |
| SARIMA | 18.4 | [14.5; 22.8] | 19.9 | [15.0; 25.5] | 14.0 | [9.8; 18.0] | [9.7; 20.1] | 15 | -24.1 | 0.70 | 0.71 | 25.2 |
| SARIMA-sel | 20.6 | [16.5; 25.2] | 20.9 | [15.8; 26.9] | 19.7 | [15.6; 23.6] | [13.8; 27.2] | 15 | -4.5 | 0.94 | 0.77 | 27.5 |
| Ridge | 53.1 | [43.4; 63.4] | 47.5 | [37.2; 58.2] | 69.7 | [52.0; 89.3] | [49.0; 94.7] | 15 | 31.3 | 1.47 | 2.04 | 69.5 |
| ElasticNet | 50.2 | [40.7; 60.4] | 44.6 | [34.4; 55.0] | 67.2 | [49.5; 87.1] | [46.8; 91.0] | 15 | 33.8 | 1.51 | 1.93 | 65.8 |
| XGB-37 | 48.3 | [39.8; 57.2] | 42.4 | [33.3; 52.5] | 65.8 | [51.6; 80.6] | [50.4; 80.3] | 15 | 36.4 | 1.55 | 1.86 | 60.7 |
| GC3 | 56.7 | [46.9; 66.9] | 55.3 | [44.1; 67.2] | 60.7 | [46.2; 76.3] | [41.2; 84.4] | 15 | 7.2 | 1.10 | 2.22 | 76.4 |
| GE | 56.7 | [47.5; 66.7] | 56.4 | [45.5; 67.7] | 57.9 | [41.8; 75.2] | [39.8; 78.9] | 15 | 2.0 | 1.03 | 2.21 | 75.0 |

### T08_ranking_shock_principal_2021_2025_dulce — Ranking por MAE_shock (2021-2025, Dulce): posición; * = primero o empatado con el primero (IC95 iid de la diferencia contiene 0)

| modelo | sh-men-P50 | sh-men-P60 | sh-men-P75 | sh-men-P90 | sh-men primero en | sh-int-P50 | sh-int-P60 | sh-int-P75 | sh-int-P90 | sh-int primero en | robusto men | robusto int | robusto men (bloques) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 10 | 10 | 10 | 10 | 0 | 10 | 10 | 10 | 8* | 1 | no | no | no |
| Seasonal Naive | 3 | 3 | 3 | 2 | 0 | 4 | 4 | 5 | 10 | 0 | no | no | no |
| Chronos | 4 | 4 | 4 | 4 | 0 | 3* | 3* | 3* | 1* | 4 | no | sí | no |
| SARIMA | 1* | 1* | 1* | 1* | 4 | 1* | 2* | 1* | 6 | 3 | sí | sí | sí |
| SARIMA-sel | 2* | 2* | 2 | 3 | 2 | 2* | 1* | 2* | 4 | 3 | no | sí | sí |
| Ridge | 9 | 9 | 9 | 8 | 0 | 8 | 9 | 9 | 5 | 0 | no | no | no |
| ElasticNet | 8 | 8 | 8 | 7 | 0 | 6 | 6 | 7 | 3 | 0 | no | no | no |
| XGB-37 | 5 | 6 | 7 | 9 | 0 | 5 | 5 | 4 | 2* | 1 | no | no | no |
| GC3 | 7 | 7 | 6 | 5 | 0 | 9 | 8 | 8 | 9 | 0 | no | no | no |
| GE | 6 | 5 | 5 | 6 | 0 | 7 | 7 | 6 | 7 | 0 | no | no | no |

### T08_ranking_normal_principal_2021_2025_dulce — Ranking por MAE normal (2021-2025, Dulce): posición; * = primero o empatado

| modelo | no-men-P50 | no-men-P60 | no-men-P75 | no-men-P90 | no-men primero en | no-int-P50 | no-int-P60 | no-int-P75 | no-int-P90 | no-int primero en |
|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 5 | 7 | 10 | 10 | 0 | 10 | 10 | 10 | 10 | 0 |
| Seasonal Naive | 4 | 4* | 3 | 3 | 1 | 1* | 2* | 3* | 3 | 3 |
| Chronos | 2* | 3* | 4* | 4 | 3 | 4 | 4 | 4 | 4 | 0 |
| SARIMA | 1* | 1* | 1* | 1* | 4 | 2* | 1* | 1* | 1* | 4 |
| SARIMA-sel | 3* | 2* | 2* | 2* | 4 | 3* | 3 | 2* | 2* | 3 |
| Ridge | 8 | 8 | 7 | 7 | 0 | 6 | 6 | 6 | 7 | 0 |
| ElasticNet | 6 | 6 | 6 | 6 | 0 | 5 | 5 | 5 | 6 | 0 |
| XGB-37 | 7 | 5 | 5 | 5 | 0 | 7 | 7 | 7 | 5 | 0 |
| GC3 | 9 | 9 | 8 | 8 | 0 | 8 | 8 | 8 | 8 | 0 |
| GE | 10 | 10 | 9 | 9 | 0 | 9 | 9 | 9 | 9 | 0 |

### T06_agregadas_P75_sensibilidad_2023_2025_sutil — Métricas agregadas 2023-2025 (sensibilidad), P75 mensual, Sutil (t; IC bootstrap pareado 95 %)

| modelo | MAE | IC95 MAE | MAE normal | IC95 normal | MAE shock | IC95 shock | IC95 shock (bloques) | n shock | Δs % | shock/normal | MASE | RMSE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 4,124 | [3,173; 5,150] | 3,068 | [2,290; 3,885] | 8,499 | [7,827; 9,044] | [6,760; 11,083] | 7 | 106.1 | 2.77 | 0.72 | 5,226 |
| Seasonal Naive | 7,216 | [5,854; 8,598] | 7,684 | [6,275; 9,099] | 5,276 | [1,972; 9,021] | [988; 9,682] | 7 | -26.9 | 0.69 | 1.28 | 8,670 |
| Chronos | 2,832 | [2,218; 3,465] | 2,368 | [1,735; 3,030] | 4,754 | [4,282; 5,305] | [3,660; 6,252] | 7 | 67.9 | 2.01 | 0.50 | 3,484 |
| SARIMA | 3,512 | [2,804; 4,227] | 2,994 | [2,330; 3,674] | 5,656 | [4,548; 6,406] | [4,063; 7,520] | 7 | 61.1 | 1.89 | 0.62 | 4,165 |
| SARIMA-sel | 3,705 | [2,854; 4,605] | 3,333 | [2,487; 4,209] | 5,248 | [3,052; 7,758] | [2,762; 8,044] | 7 | 41.6 | 1.57 | 0.65 | 4,583 |
| Ridge | 6,110 | [4,390; 7,972] | 5,089 | [3,390; 6,928] | 10,341 | [6,327; 15,774] | [6,363; 13,776] | 7 | 69.2 | 2.03 | 1.07 | 8,841 |
| ElasticNet | 6,129 | [4,496; 7,860] | 5,212 | [3,570; 6,966] | 9,928 | [6,189; 14,421] | [6,312; 12,788] | 7 | 62.0 | 1.90 | 1.08 | 8,562 |
| XGB-37 | 4,881 | [3,788; 6,031] | 4,548 | [3,394; 5,739] | 6,264 | [2,991; 8,304] | [2,895; 9,977] | 7 | 28.3 | 1.38 | 0.86 | 6,056 |
| GC3 | 7,596 | [5,974; 9,299] | 7,844 | [5,931; 9,782] | 6,571 | [4,346; 8,712] | [4,106; 8,918] | 7 | -13.5 | 0.84 | 1.34 | 9,405 |
| GE | 8,197 | [6,464; 9,985] | 8,360 | [6,351; 10,372] | 7,523 | [4,888; 10,112] | [4,539; 10,508] | 7 | -8.2 | 0.90 | 1.45 | 10,120 |

### T08_ranking_shock_sensibilidad_2023_2025_sutil — Ranking por MAE_shock (2023-2025 (sensibilidad), Sutil): posición; * = primero o empatado con el primero (IC95 iid de la diferencia contiene 0)

| modelo | sh-men-P50 | sh-men-P60 | sh-men-P75 | sh-men-P90 | sh-men primero en | sh-int-P50 | sh-int-P60 | sh-int-P75 | sh-int-P90 | sh-int primero en | robusto men | robusto int | robusto men (bloques) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 5 | 5 | 8 | 7 | 0 | 3* | 3* | 2* | 2* | 4 | no | sí | no |
| Seasonal Naive | 6 | 6 | 3* | 4* | 2 | 10 | 10 | 10 | 10 | 0 | no | no | no |
| Chronos | 2* | 3* | 1* | 1* | 4 | 1* | 1* | 1* | 1* | 4 | sí | sí | sí |
| SARIMA | 3* | 1* | 4 | 2 | 2 | 2* | 2* | 3 | 3 | 2 | no | no | no |
| SARIMA-sel | 1* | 2* | 2* | 3* | 4 | 4* | 4* | 4 | 6 | 2 | sí | no | sí |
| Ridge | 9 | 10 | 10 | 10 | 0 | 6 | 6 | 6 | 4 | 0 | no | no | no |
| ElasticNet | 10 | 9 | 9 | 9 | 0 | 7 | 7 | 7 | 5 | 0 | no | no | no |
| XGB-37 | 4 | 4* | 5* | 6 | 2 | 5 | 5 | 5 | 7* | 1 | no | no | no |
| GC3 | 8 | 7 | 6* | 5 | 1 | 9 | 8 | 8 | 8 | 0 | no | no | no |
| GE | 7 | 8 | 7 | 8 | 0 | 8 | 9 | 9 | 9 | 0 | no | no | no |

### T08_ranking_normal_sensibilidad_2023_2025_sutil — Ranking por MAE normal (2023-2025 (sensibilidad), Sutil): posición; * = primero o empatado

| modelo | no-men-P50 | no-men-P60 | no-men-P75 | no-men-P90 | no-men primero en | no-int-P50 | no-int-P60 | no-int-P75 | no-int-P90 | no-int primero en |
|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 1* | 1* | 3* | 4 | 3 | 5 | 5 | 4 | 4 | 0 |
| Seasonal Naive | 8 | 8 | 8 | 8 | 0 | 2* | 4* | 6 | 6 | 2 |
| Chronos | 2* | 2* | 1* | 1* | 4 | 1* | 1* | 1* | 1* | 4 |
| SARIMA | 5 | 4 | 2* | 2* | 2 | 4* | 3* | 3* | 3* | 4 |
| SARIMA-sel | 6 | 6 | 4* | 3* | 2 | 3* | 2* | 2* | 2* | 4 |
| Ridge | 3 | 3 | 6 | 6 | 0 | 8 | 8 | 8 | 8 | 0 |
| ElasticNet | 4 | 5 | 7 | 7 | 0 | 7 | 7 | 7 | 7 | 0 |
| XGB-37 | 7 | 7 | 5 | 5 | 0 | 6 | 6 | 5 | 5 | 0 |
| GC3 | 9 | 9 | 9 | 9 | 0 | 9 | 9 | 9 | 9 | 0 |
| GE | 10 | 10 | 10 | 10 | 0 | 10 | 10 | 10 | 10 | 0 |

### T06_agregadas_P75_sensibilidad_2023_2025_dulce — Métricas agregadas 2023-2025 (sensibilidad), P75 mensual, Dulce (t; IC bootstrap pareado 95 %)

| modelo | MAE | IC95 MAE | MAE normal | IC95 normal | MAE shock | IC95 shock | IC95 shock (bloques) | n shock | Δs % | shock/normal | MASE | RMSE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 82.2 | [66.2; 98.9] | 63.5 | [49.4; 79.1] | 138.2 | [119.0; 158.7] | [119.7; 157.3] | 9 | 68.2 | 2.18 | 3.33 | 96.0 |
| Seasonal Naive | 28.1 | [22.3; 34.9] | 29.1 | [21.5; 38.1] | 25.0 | [20.0; 30.4] | [16.6; 33.8] | 9 | -10.8 | 0.86 | 1.14 | 36.5 |
| Chronos | 35.0 | [27.8; 42.6] | 28.2 | [21.1; 36.5] | 55.3 | [44.8; 67.0] | [43.3; 66.0] | 9 | 58.3 | 1.96 | 1.41 | 41.9 |
| SARIMA | 22.0 | [16.1; 28.8] | 23.5 | [16.2; 32.4] | 17.6 | [10.8; 23.9] | [11.8; 28.3] | 9 | -20.2 | 0.75 | 0.89 | 29.6 |
| SARIMA-sel | 20.9 | [15.2; 27.7] | 22.3 | [15.2; 31.3] | 16.9 | [10.7; 22.6] | [11.2; 26.7] | 9 | -19.3 | 0.76 | 0.85 | 28.7 |
| Ridge | 64.0 | [50.1; 78.1] | 57.2 | [42.1; 73.8] | 84.2 | [59.8; 112.3] | [53.6; 118.0] | 9 | 31.6 | 1.47 | 2.58 | 81.0 |
| ElasticNet | 59.5 | [45.6; 73.9] | 52.8 | [37.6; 69.1] | 79.7 | [55.4; 108.8] | [48.8; 111.2] | 9 | 34.0 | 1.51 | 2.40 | 76.2 |
| XGB-37 | 54.4 | [42.1; 67.3] | 49.5 | [35.3; 65.3] | 69.1 | [51.9; 86.3] | [48.6; 85.0] | 9 | 27.1 | 1.40 | 2.21 | 67.6 |
| GC3 | 69.9 | [54.6; 85.1] | 69.2 | [51.6; 87.9] | 71.9 | [49.0; 96.3] | [39.7; 105.5] | 9 | 2.9 | 1.04 | 2.88 | 91.0 |
| GE | 68.4 | [53.9; 83.0] | 68.6 | [52.3; 86.2] | 67.6 | [43.7; 93.7] | [39.4; 97.0] | 9 | -1.1 | 0.99 | 2.81 | 87.4 |

### T08_ranking_shock_sensibilidad_2023_2025_dulce — Ranking por MAE_shock (2023-2025 (sensibilidad), Dulce): posición; * = primero o empatado con el primero (IC95 iid de la diferencia contiene 0)

| modelo | sh-men-P50 | sh-men-P60 | sh-men-P75 | sh-men-P90 | sh-men primero en | sh-int-P50 | sh-int-P60 | sh-int-P75 | sh-int-P90 | sh-int primero en | robusto men | robusto int | robusto men (bloques) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 10 | 10 | 10 | 10 | 0 | 10 | 10 | 10 | 3* | 1 | no | no | no |
| Seasonal Naive | 3* | 3 | 3 | 3 | 1 | 4 | 4 | 4 | 10 | 0 | no | no | no |
| Chronos | 4 | 4 | 4 | 6 | 0 | 3* | 3* | 3* | 1* | 4 | no | sí | no |
| SARIMA | 2* | 2 | 2* | 1* | 3 | 2* | 2* | 1* | 5 | 3 | sí | sí | sí |
| SARIMA-sel | 1* | 1* | 1* | 2 | 3 | 1* | 1* | 2* | 6 | 3 | sí | sí | sí |
| Ridge | 9 | 9 | 9 | 8 | 0 | 8 | 9 | 9 | 7 | 0 | no | no | no |
| ElasticNet | 8 | 7 | 8 | 7 | 0 | 6 | 6 | 7 | 4 | 0 | no | no | no |
| XGB-37 | 5 | 5 | 6 | 9 | 0 | 5 | 5 | 5* | 2* | 2 | no | no | no |
| GC3 | 7 | 8 | 7 | 4 | 0 | 9 | 8 | 8 | 9 | 0 | no | no | no |
| GE | 6 | 6 | 5 | 5 | 0 | 7 | 7 | 6 | 8 | 0 | no | no | no |

### T08_ranking_normal_sensibilidad_2023_2025_dulce — Ranking por MAE normal (2023-2025 (sensibilidad), Dulce): posición; * = primero o empatado

| modelo | no-men-P50 | no-men-P60 | no-men-P75 | no-men-P90 | no-men primero en | no-int-P50 | no-int-P60 | no-int-P75 | no-int-P90 | no-int primero en |
|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 5 | 5 | 8 | 10 | 0 | 10 | 10 | 10 | 10 | 0 |
| Seasonal Naive | 4 | 4 | 4 | 3 | 0 | 1* | 2* | 3* | 3 | 3 |
| Chronos | 3* | 3* | 3* | 4 | 3 | 4 | 4 | 4 | 4 | 0 |
| SARIMA | 2 | 2* | 2 | 2 | 1 | 3* | 3 | 2 | 2 | 1 |
| SARIMA-sel | 1* | 1* | 1* | 1* | 4 | 2* | 1* | 1* | 1* | 4 |
| Ridge | 8 | 8 | 7 | 7 | 0 | 6 | 6 | 6 | 7 | 0 |
| ElasticNet | 6 | 7 | 6 | 6 | 0 | 5 | 5 | 5 | 6 | 0 |
| XGB-37 | 7 | 6 | 5 | 5 | 0 | 7 | 7 | 7 | 5 | 0 |
| GC3 | 10 | 10 | 10 | 9 | 0 | 8 | 8 | 9 | 9 | 0 |
| GE | 9 | 9 | 9 | 8 | 0 | 9 | 9 | 8 | 8 | 0 |

### T09_DM_matriz_principal_2021_2025_sutil — DM-HLN, p-valor sin ajustar (principal_2021_2025, Sutil). Bajo la diagonal: global (n=60); sobre la diagonal: solo shocks P75 mensual (n=10). Signo: + = el modelo de la fila tiene más error que el de la columna

| modelo | Nv | SN | Chr | SAR | SSel | Rdg | EN | X37 | GC3 | GE |
|---|---|---|---|---|---|---|---|---|---|---|
| Naive | — | 0.094+ | 0.000+ | 0.001+ | 0.013+ | 0.984− | 0.881+ | 0.045+ | 0.123+ | 0.259+ |
| Seasonal Naive | 0.001+ | — | 0.867+ | 0.949− | 0.932+ | 0.235− | 0.247− | 0.614− | 0.331− | 0.245− |
| Chronos | 0.003− | 0.000− | — | 0.509− | 0.867− | 0.145− | 0.146− | 0.292− | 0.255− | 0.109− |
| SARIMA | 0.548− | 0.000− | 0.017+ | — | 0.807+ | 0.152− | 0.151− | 0.460− | 0.427− | 0.176− |
| SARIMA-sel | 0.385− | 0.000− | 0.102+ | 0.587− | — | 0.156− | 0.157− | 0.358− | 0.243− | 0.090− |
| Ridge | 0.071+ | 0.180− | 0.002+ | 0.030+ | 0.022+ | — | 0.406+ | 0.333+ | 0.344+ | 0.525+ |
| ElasticNet | 0.066+ | 0.129− | 0.002+ | 0.028+ | 0.018+ | 0.696− | — | 0.389+ | 0.382+ | 0.598+ |
| XGB-37 | 0.018+ | 0.063− | 0.000+ | 0.004+ | 0.001+ | 0.955− | 0.990+ | — | 0.919− | 0.301− |
| GC3 | 0.000+ | 0.641+ | 0.000+ | 0.000+ | 0.000+ | 0.080+ | 0.050+ | 0.001+ | — | 0.225− |
| GE | 0.000+ | 0.341+ | 0.000+ | 0.000+ | 0.000+ | 0.045+ | 0.030+ | 0.000+ | 0.061+ | — |

### T09_DM_matriz_principal_2021_2025_dulce — DM-HLN, p-valor sin ajustar (principal_2021_2025, Dulce). Bajo la diagonal: global (n=60); sobre la diagonal: solo shocks P75 mensual (n=15). Signo: + = el modelo de la fila tiene más error que el de la columna

| modelo | Nv | SN | Chr | SAR | SSel | Rdg | EN | X37 | GC3 | GE |
|---|---|---|---|---|---|---|---|---|---|---|
| Naive | — | 0.000+ | 0.000+ | 0.000+ | 0.000+ | 0.000+ | 0.000+ | 0.000+ | 0.000+ | 0.000+ |
| Seasonal Naive | 0.000− | — | 0.000− | 0.001+ | 0.237+ | 0.001− | 0.001− | 0.001− | 0.004− | 0.005− |
| Chronos | 0.000− | 0.054+ | — | 0.000+ | 0.001+ | 0.031− | 0.038− | 0.024− | 0.183− | 0.234− |
| SARIMA | 0.000− | 0.004− | 0.000− | — | 0.115− | 0.000− | 0.000− | 0.000− | 0.001− | 0.001− |
| SARIMA-sel | 0.000− | 0.121− | 0.005− | 0.203+ | — | 0.001− | 0.001− | 0.001− | 0.005− | 0.005− |
| Ridge | 0.001− | 0.000+ | 0.000+ | 0.000+ | 0.000+ | — | 0.270+ | 0.767+ | 0.387+ | 0.204+ |
| ElasticNet | 0.000− | 0.000+ | 0.000+ | 0.000+ | 0.000+ | 0.009− | — | 0.907+ | 0.496+ | 0.272+ |
| XGB-37 | 0.000− | 0.000+ | 0.000+ | 0.000+ | 0.000+ | 0.377− | 0.693− | — | 0.644+ | 0.449+ |
| GC3 | 0.013− | 0.000+ | 0.000+ | 0.000+ | 0.000+ | 0.533+ | 0.242+ | 0.075+ | — | 0.340+ |
| GE | 0.012− | 0.000+ | 0.000+ | 0.000+ | 0.000+ | 0.508+ | 0.216+ | 0.061+ | 0.954+ | — |

### T09_DM_matriz_sensibilidad_2023_2025_sutil — DM-HLN, p-valor sin ajustar (sensibilidad_2023_2025, Sutil). Bajo la diagonal: global (n=36); sobre la diagonal: solo shocks P75 mensual (n=7). Signo: + = el modelo de la fila tiene más error que el de la columna

| modelo | Nv | SN | Chr | SAR | SSel | Rdg | EN | X37 | GC3 | GE |
|---|---|---|---|---|---|---|---|---|---|---|
| Naive | — | 0.271+ | 0.001+ | 0.010+ | 0.061+ | 0.604− | 0.651− | 0.169+ | 0.356+ | 0.597+ |
| Seasonal Naive | 0.005+ | — | 0.811+ | 0.864− | 0.987+ | 0.239− | 0.231− | 0.711− | 0.409− | 0.313− |
| Chronos | 0.003− | 0.000− | — | 0.064− | 0.655− | 0.126− | 0.108− | 0.327− | 0.247− | 0.098− |
| SARIMA | 0.256− | 0.000− | 0.098+ | — | 0.709+ | 0.175− | 0.158− | 0.697− | 0.601− | 0.300− |
| SARIMA-sel | 0.525− | 0.000− | 0.077+ | 0.637+ | — | 0.167− | 0.151− | 0.528− | 0.340− | 0.162− |
| Ridge | 0.074+ | 0.431− | 0.005+ | 0.020+ | 0.043+ | — | 0.563+ | 0.295+ | 0.323+ | 0.479+ |
| ElasticNet | 0.055+ | 0.399− | 0.003+ | 0.014+ | 0.029+ | 0.932+ | — | 0.320+ | 0.330+ | 0.512+ |
| XGB-37 | 0.264+ | 0.019− | 0.002+ | 0.052+ | 0.046+ | 0.318− | 0.281− | — | 0.854− | 0.283− |
| GC3 | 0.002+ | 0.694+ | 0.000+ | 0.000+ | 0.000+ | 0.267+ | 0.236+ | 0.000+ | — | 0.263− |
| GE | 0.001+ | 0.378+ | 0.000+ | 0.000+ | 0.000+ | 0.158+ | 0.141+ | 0.000+ | 0.061+ | — |

### T09_DM_matriz_sensibilidad_2023_2025_dulce — DM-HLN, p-valor sin ajustar (sensibilidad_2023_2025, Dulce). Bajo la diagonal: global (n=36); sobre la diagonal: solo shocks P75 mensual (n=9). Signo: + = el modelo de la fila tiene más error que el de la columna

| modelo | Nv | SN | Chr | SAR | SSel | Rdg | EN | X37 | GC3 | GE |
|---|---|---|---|---|---|---|---|---|---|---|
| Naive | — | 0.000+ | 0.000+ | 0.000+ | 0.000+ | 0.002+ | 0.001+ | 0.002+ | 0.001+ | 0.000+ |
| Seasonal Naive | 0.000− | — | 0.001− | 0.067+ | 0.033+ | 0.003− | 0.004− | 0.008− | 0.022− | 0.020− |
| Chronos | 0.000− | 0.128+ | — | 0.001+ | 0.001+ | 0.062− | 0.083− | 0.181− | 0.287− | 0.343− |
| SARIMA | 0.000− | 0.050− | 0.009− | — | 0.236+ | 0.003− | 0.005− | 0.004− | 0.019− | 0.017− |
| SARIMA-sel | 0.000− | 0.015− | 0.004− | 0.040− | — | 0.003− | 0.004− | 0.004− | 0.017− | 0.015− |
| Ridge | 0.094− | 0.000+ | 0.000+ | 0.000+ | 0.000+ | — | 0.223+ | 0.472+ | 0.462+ | 0.255+ |
| ElasticNet | 0.036− | 0.000+ | 0.001+ | 0.000+ | 0.000+ | 0.008− | — | 0.578+ | 0.610+ | 0.359+ |
| XGB-37 | 0.011− | 0.000+ | 0.002+ | 0.000+ | 0.000+ | 0.246− | 0.503− | — | 0.868− | 0.925+ |
| GC3 | 0.302− | 0.000+ | 0.000+ | 0.000+ | 0.000+ | 0.508+ | 0.222+ | 0.027+ | — | 0.319+ |
| GE | 0.235− | 0.000+ | 0.000+ | 0.000+ | 0.000+ | 0.603+ | 0.266+ | 0.033+ | 0.335− | — |

### T09_DM_holm_matriz_principal_2021_2025_sutil — DM-HLN, p-valor ajustado por Holm (EXPLORATORIO, DESV-07; familia = 45 pares) (principal_2021_2025, Sutil). Bajo la diagonal: global (n=60); sobre la diagonal: solo shocks P75 mensual (n=10). Signo: + = el modelo de la fila tiene más error que el de la columna

| modelo | Nv | SN | Chr | SAR | SSel | Rdg | EN | X37 | GC3 | GE |
|---|---|---|---|---|---|---|---|---|---|---|
| Naive | — | 1.000+ | 0.001+ | 0.062+ | 0.545+ | 1.000− | 1.000+ | 1.000+ | 1.000+ | 1.000+ |
| Seasonal Naive | 0.029+ | — | 1.000+ | 1.000− | 1.000+ | 1.000− | 1.000− | 1.000− | 1.000− | 1.000− |
| Chronos | 0.075− | 0.000− | — | 1.000− | 1.000− | 1.000− | 1.000− | 1.000− | 1.000− | 1.000− |
| SARIMA | 1.000− | 0.001− | 0.429+ | — | 1.000+ | 1.000− | 1.000− | 1.000− | 1.000− | 1.000− |
| SARIMA-sel | 1.000− | 0.000− | 1.000+ | 1.000− | — | 1.000− | 1.000− | 1.000− | 1.000− | 1.000− |
| Ridge | 0.978+ | 1.000− | 0.061+ | 0.598+ | 0.478+ | — | 1.000+ | 1.000+ | 1.000+ | 1.000+ |
| ElasticNet | 0.978+ | 1.000− | 0.045+ | 0.598+ | 0.429+ | 1.000− | — | 1.000+ | 1.000+ | 1.000+ |
| XGB-37 | 0.429+ | 0.978− | 0.000+ | 0.091+ | 0.019+ | 1.000− | 1.000+ | — | 1.000− | 1.000− |
| GC3 | 0.008+ | 1.000+ | 0.000+ | 0.002+ | 0.000+ | 0.978+ | 0.858+ | 0.029+ | — | 1.000− |
| GE | 0.004+ | 1.000+ | 0.000+ | 0.001+ | 0.000+ | 0.803+ | 0.598+ | 0.005+ | 0.978+ | — |

### T09_DM_holm_matriz_principal_2021_2025_dulce — DM-HLN, p-valor ajustado por Holm (EXPLORATORIO, DESV-07; familia = 45 pares) (principal_2021_2025, Dulce). Bajo la diagonal: global (n=60); sobre la diagonal: solo shocks P75 mensual (n=15). Signo: + = el modelo de la fila tiene más error que el de la columna

| modelo | Nv | SN | Chr | SAR | SSel | Rdg | EN | X37 | GC3 | GE |
|---|---|---|---|---|---|---|---|---|---|---|
| Naive | — | 0.000+ | 0.000+ | 0.000+ | 0.000+ | 0.000+ | 0.000+ | 0.000+ | 0.000+ | 0.000+ |
| Seasonal Naive | 0.000− | — | 0.005− | 0.018+ | 1.000+ | 0.025− | 0.029− | 0.018− | 0.090− | 0.093− |
| Chronos | 0.000− | 0.648+ | — | 0.001+ | 0.029+ | 0.493− | 0.570− | 0.404− | 1.000− | 1.000− |
| SARIMA | 0.000− | 0.070− | 0.008− | — | 1.000− | 0.007− | 0.009− | 0.003− | 0.029− | 0.029− |
| SARIMA-sel | 0.000− | 1.000− | 0.079− | 1.000+ | — | 0.029− | 0.033− | 0.025− | 0.091− | 0.093− |
| Ridge | 0.025− | 0.000+ | 0.001+ | 0.000+ | 0.000+ | — | 1.000+ | 1.000+ | 1.000+ | 1.000+ |
| ElasticNet | 0.006− | 0.000+ | 0.003+ | 0.000+ | 0.000+ | 0.130− | — | 1.000+ | 1.000+ | 1.000+ |
| XGB-37 | 0.002− | 0.000+ | 0.001+ | 0.000+ | 0.000+ | 1.000− | 1.000− | — | 1.000+ | 1.000+ |
| GC3 | 0.166− | 0.000+ | 0.001+ | 0.000+ | 0.000+ | 1.000+ | 1.000+ | 0.750+ | — | 1.000+ |
| GE | 0.165− | 0.000+ | 0.000+ | 0.000+ | 0.000+ | 1.000+ | 1.000+ | 0.676+ | 1.000+ | — |

### T09_DM_holm_matriz_sensibilidad_2023_2025_sutil — DM-HLN, p-valor ajustado por Holm (EXPLORATORIO, DESV-07; familia = 45 pares) (sensibilidad_2023_2025, Sutil). Bajo la diagonal: global (n=36); sobre la diagonal: solo shocks P75 mensual (n=7). Signo: + = el modelo de la fila tiene más error que el de la columna

| modelo | Nv | SN | Chr | SAR | SSel | Rdg | EN | X37 | GC3 | GE |
|---|---|---|---|---|---|---|---|---|---|---|
| Naive | — | 1.000+ | 0.066+ | 0.456+ | 1.000+ | 1.000− | 1.000− | 1.000+ | 1.000+ | 1.000+ |
| Seasonal Naive | 0.153+ | — | 1.000+ | 1.000− | 1.000+ | 1.000− | 1.000− | 1.000− | 1.000− | 1.000− |
| Chronos | 0.097− | 0.001− | — | 1.000− | 1.000− | 1.000− | 1.000− | 1.000− | 1.000− | 1.000− |
| SARIMA | 1.000− | 0.009− | 1.000+ | — | 1.000+ | 1.000− | 1.000− | 1.000− | 1.000− | 1.000− |
| SARIMA-sel | 1.000− | 0.003− | 1.000+ | 1.000+ | — | 1.000− | 1.000− | 1.000− | 1.000− | 1.000− |
| Ridge | 1.000+ | 1.000− | 0.153+ | 0.511+ | 0.987+ | — | 1.000+ | 1.000+ | 1.000+ | 1.000+ |
| ElasticNet | 1.000+ | 1.000− | 0.090+ | 0.370+ | 0.698+ | 1.000+ | — | 1.000+ | 1.000+ | 1.000+ |
| XGB-37 | 1.000+ | 0.489− | 0.078+ | 1.000+ | 1.000+ | 1.000− | 1.000− | — | 1.000− | 1.000− |
| GC3 | 0.064+ | 1.000+ | 0.001+ | 0.010+ | 0.003+ | 1.000+ | 1.000+ | 0.002+ | — | 1.000− |
| GE | 0.024+ | 1.000+ | 0.000+ | 0.003+ | 0.001+ | 1.000+ | 1.000+ | 0.000+ | 1.000+ | — |

### T09_DM_holm_matriz_sensibilidad_2023_2025_dulce — DM-HLN, p-valor ajustado por Holm (EXPLORATORIO, DESV-07; familia = 45 pares) (sensibilidad_2023_2025, Dulce). Bajo la diagonal: global (n=36); sobre la diagonal: solo shocks P75 mensual (n=9). Signo: + = el modelo de la fila tiene más error que el de la columna

| modelo | Nv | SN | Chr | SAR | SSel | Rdg | EN | X37 | GC3 | GE |
|---|---|---|---|---|---|---|---|---|---|---|
| Naive | — | 0.000+ | 0.001+ | 0.000+ | 0.000+ | 0.079+ | 0.043+ | 0.065+ | 0.036+ | 0.006+ |
| Seasonal Naive | 0.000− | — | 0.021− | 1.000+ | 0.594+ | 0.095− | 0.121− | 0.191− | 0.416− | 0.404− |
| Chronos | 0.000− | 1.000+ | — | 0.042+ | 0.030+ | 1.000− | 1.000− | 1.000− | 1.000− | 1.000− |
| SARIMA | 0.000− | 0.597− | 0.169− | — | 1.000+ | 0.095− | 0.124− | 0.121− | 0.392− | 0.387− |
| SARIMA-sel | 0.000− | 0.263− | 0.086− | 0.526− | — | 0.088− | 0.121− | 0.113− | 0.387− | 0.361− |
| Ridge | 1.000− | 0.001+ | 0.011+ | 0.001+ | 0.000+ | — | 1.000+ | 1.000+ | 1.000+ | 1.000+ |
| ElasticNet | 0.503− | 0.004+ | 0.029+ | 0.002+ | 0.001+ | 0.169− | — | 1.000+ | 1.000+ | 1.000+ |
| XGB-37 | 0.194− | 0.008+ | 0.041+ | 0.003+ | 0.002+ | 1.000− | 1.000− | — | 1.000− | 1.000+ |
| GC3 | 1.000− | 0.000+ | 0.006+ | 0.000+ | 0.000+ | 1.000+ | 1.000+ | 0.428+ | — | 1.000+ |
| GE | 1.000− | 0.000+ | 0.004+ | 0.000+ | 0.000+ | 1.000+ | 1.000+ | 0.497+ | 1.000− | — |

### T09_holm_resumen — EXPLORATORIO (DESV-07): pares con p < 0,05 antes y después de Holm, por familia

| conjunto | cultivar | alcance | pares | p_menor_005 | holm_menor_005 |
|---|---|---|---|---|---|
| principal_2021_2025 | dulce | global | 45 | 33 | 28 |
| principal_2021_2025 | dulce | shock_P75_mensual | 45 | 31 | 24 |
| principal_2021_2025 | sutil | global | 45 | 28 | 17 |
| principal_2021_2025 | sutil | shock_P75_mensual | 45 | 4 | 1 |
| sensibilidad_2023_2025 | dulce | global | 45 | 34 | 24 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | 45 | 28 | 10 |
| sensibilidad_2023_2025 | sutil | global | 45 | 24 | 12 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | 45 | 2 | 0 |

### T11_ablacion_sutil — Ablación NLP: MAE(GE) − MAE(GC3) emparejado por semilla, Sutil (t; negativo = GE mejor)

| conjunto | alcance | n meses | GE−GC3 (t) | IC95 | DE semillas | semillas GE mejor (de 10) |
|---|---|---|---|---|---|---|
| 2021 | global | 12 | 11 | [-164; 173] | 756 | 6 |
| 2021 | shock_P75 | 0 | — | — | — | — |
| 2021 | normal_P75 | 12 | 11 | [-164; 173] | 756 | 6 |
| 2022 | global | 12 | 98 | [-542; 730] | 444 | 3 |
| 2022 | shock_P75 | 3 | 286 | [-1,354; 1,261] | 413 | 2 |
| 2022 | normal_P75 | 9 | 35 | [-675; 741] | 545 | 4 |
| 2023 | global | 12 | -683 | [-1,263; -88] | 592 | 9 |
| 2023 | shock_P75 | 4 | -70 | [-940; 801] | 859 | 5 |
| 2023 | normal_P75 | 8 | -990 | [-1,608; -324] | 630 | 9 |
| 2024 | global | 12 | 805 | [529; 1,104] | 734 | 1 |
| 2024 | shock_P75 | 0 | — | — | — | — |
| 2024 | normal_P75 | 12 | 805 | [529; 1,104] | 734 | 1 |
| 2025 | global | 12 | 1,680 | [300; 3,045] | 1,322 | 1 |
| 2025 | shock_P75 | 3 | 2,314 | [112; 4,889] | 1,716 | 1 |
| 2025 | normal_P75 | 9 | 1,469 | [-165; 3,118] | 1,386 | 0 |
| principal_2021_2025 | global | 60 | 382 | [45; 711] | 363 | 1 |
| principal_2021_2025 | shock_P75 | 10 | 752 | [-88; 1,607] | 655 | 1 |
| principal_2021_2025 | normal_P75 | 50 | 308 | [-33; 648] | 314 | 1 |
| sensibilidad_2023_2025 | global | 36 | 601 | [89; 1,096] | 710 | 1 |
| sensibilidad_2023_2025 | shock_P75 | 7 | 952 | [-81; 2,062] | 918 | 2 |
| sensibilidad_2023_2025 | normal_P75 | 29 | 516 | [-39; 1,072] | 693 | 1 |

### T11_ablacion_dulce — Ablación NLP: MAE(GE) − MAE(GC3) emparejado por semilla, Dulce (t; negativo = GE mejor)

| conjunto | alcance | n meses | GE−GC3 (t) | IC95 | DE semillas | semillas GE mejor (de 10) |
|---|---|---|---|---|---|---|
| 2021 | global | 12 | 4.6 | [-0.6; 9.5] | 8.3 | 3 |
| 2021 | shock_P75 | 3 | 0.1 | [-11.8; 18.4] | 9.6 | 3 |
| 2021 | normal_P75 | 9 | 6.0 | [1.6; 10.1] | 9.6 | 2 |
| 2022 | global | 12 | 0.4 | [-1.5; 2.1] | 4.2 | 3 |
| 2022 | shock_P75 | 3 | -1.6 | [-6.1; 2.0] | 7.5 | 5 |
| 2022 | normal_P75 | 9 | 1.0 | [-0.9; 2.8] | 4.0 | 3 |
| 2023 | global | 12 | 4.2 | [1.9; 6.3] | 5.6 | 2 |
| 2023 | shock_P75 | 2 | 1.6 | [1.5; 1.7] | 16.4 | 6 |
| 2023 | normal_P75 | 10 | 4.7 | [2.0; 7.1] | 7.4 | 3 |
| 2024 | global | 12 | -1.0 | [-6.4; 4.4] | 5.0 | 5 |
| 2024 | shock_P75 | 4 | 3.9 | [-0.0; 7.7] | 9.8 | 3 |
| 2024 | normal_P75 | 8 | -3.4 | [-10.4; 4.3] | 6.9 | 7 |
| 2025 | global | 12 | -7.8 | [-13.0; -3.2] | 10.2 | 8 |
| 2025 | shock_P75 | 3 | -19.0 | [-27.3; -13.1] | 13.2 | 9 |
| 2025 | normal_P75 | 9 | -4.1 | [-7.8; -0.4] | 11.0 | 6 |
| principal_2021_2025 | global | 60 | 0.1 | [-1.9; 1.9] | 3.2 | 7 |
| principal_2021_2025 | shock_P75 | 15 | -2.9 | [-6.2; 0.7] | 5.2 | 7 |
| principal_2021_2025 | normal_P75 | 45 | 1.0 | [-0.7; 2.9] | 3.3 | 5 |
| sensibilidad_2023_2025 | global | 36 | -1.5 | [-4.2; 0.9] | 3.7 | 8 |
| sensibilidad_2023_2025 | shock_P75 | 9 | -4.3 | [-7.2; -1.5] | 8.1 | 7 |
| sensibilidad_2023_2025 | normal_P75 | 27 | -0.6 | [-3.2; 2.1] | 3.8 | 6 |

### T12_loo_agregado_sutil — Δs (%) agregado 2021-2025 quitando un mes de shock P75 a la vez, Sutil

| modelo | n_shock | Delta_s | Delta_s_loo_min | Delta_s_loo_max | mes_que_mas_cambia |
|---|---|---|---|---|---|
| Naive | 10 | 134.7 | 132.9 | 148.2 | 2023-09 |
| Seasonal Naive | 10 | -17.1 | -31.3 | -9.7 | 2023-08 |
| Chronos | 10 | 80.6 | 73.9 | 91.2 | 2022-12 |
| SARIMA | 10 | 52.7 | 43.3 | 66.7 | 2022-12 |
| SARIMA-sel | 10 | 54.0 | 40.6 | 67.9 | 2023-12 |
| Ridge | 10 | 73.7 | 43.8 | 87.1 | 2023-11 |
| ElasticNet | 10 | 67.4 | 42.3 | 80.6 | 2023-11 |
| XGB-37 | 10 | 22.0 | 10.2 | 32.4 | 2025-01 |
| GC3 | 10 | -4.5 | -13.8 | 2.6 | 2023-08 |
| GE | 10 | 1.2 | -6.6 | 8.2 | 2025-01 |

### T12_loo_agregado_dulce — Δs (%) agregado 2021-2025 quitando un mes de shock P75 a la vez, Dulce

| modelo | n_shock | Delta_s | Delta_s_loo_min | Delta_s_loo_max | mes_que_mas_cambia |
|---|---|---|---|---|---|
| Naive | 15 | 69.8 | 68.9 | 74.3 | 2021-01 |
| Seasonal Naive | 15 | -0.0 | -5.4 | 4.7 | 2024-03 |
| Chronos | 15 | 56.4 | 51.7 | 63.2 | 2021-02 |
| SARIMA | 15 | -24.1 | -34.5 | -20.4 | 2024-10 |
| SARIMA-sel | 15 | -4.5 | -11.1 | 0.3 | 2021-01 |
| Ridge | 15 | 31.3 | 21.7 | 37.7 | 2024-03 |
| ElasticNet | 15 | 33.8 | 23.5 | 40.9 | 2024-03 |
| XGB-37 | 15 | 36.4 | 30.4 | 42.9 | 2024-02 |
| GC3 | 15 | 7.2 | -5.1 | 10.4 | 2025-03 |
| GE | 15 | 2.0 | -9.5 | 5.5 | 2025-03 |

### T13_cuartiles_sutil — MAE por cuartil de |Δy/y| mensual en test 2021-2025 (15 meses por cuartil), Sutil (t)

| modelo | Q1 (0.003-0.037) | Q2 (0.037-0.097) | Q3 (0.097-0.192) | Q4 (0.192-0.571) |
|---|---|---|---|---|
| Naive | 412 | 2,240 | 4,096 | 7,749 |
| Seasonal Naive | 6,941 | 5,309 | 6,475 | 5,575 |
| Chronos | 1,799 | 1,854 | 2,642 | 4,299 |
| SARIMA | 3,073 | 3,334 | 2,904 | 4,132 |
| SARIMA-sel | 3,517 | 2,730 | 3,024 | 3,552 |
| Ridge | 3,338 | 2,757 | 4,985 | 8,621 |
| ElasticNet | 3,296 | 2,598 | 5,252 | 8,341 |
| XGB-37 | 5,015 | 4,749 | 4,314 | 5,448 |
| GC3 | 6,628 | 6,527 | 5,598 | 6,693 |
| GE | 6,998 | 7,823 | 4,976 | 7,177 |

### T13_cuartiles_dulce — MAE por cuartil de |Δy/y| mensual en test 2021-2025 (15 meses por cuartil), Dulce (t)

| modelo | Q1 (0.007-0.090) | Q2 (0.090-0.165) | Q3 (0.165-0.327) | Q4 (0.327-0.474) |
|---|---|---|---|---|
| Naive | 23.3 | 59.9 | 95.3 | 131.6 |
| Seasonal Naive | 22.1 | 36.1 | 15.4 | 24.5 |
| Chronos | 17.9 | 28.8 | 28.4 | 48.2 |
| SARIMA | 13.3 | 30.1 | 16.2 | 14.0 |
| SARIMA-sel | 18.4 | 28.7 | 15.8 | 19.7 |
| Ridge | 43.5 | 55.7 | 43.3 | 69.7 |
| ElasticNet | 42.6 | 52.4 | 38.7 | 67.2 |
| XGB-37 | 49.4 | 49.7 | 28.2 | 65.8 |
| GC3 | 66.4 | 65.6 | 33.9 | 60.7 |
| GE | 68.7 | 66.1 | 34.3 | 57.9 |

### T07_dispersion_semillas — Dispersión entre las 10 semillas, agregado 2021-2025, P75 mensual (t; fuera de los IC, D-BR6)

| cultivar | modelo | MAE_media | MAE_DE | MAE_min | MAE_max | MAE_shock_media | MAE_shock_DE | Delta_s_media | Delta_s_DE |
|---|---|---|---|---|---|---|---|---|---|
| dulce | GC3 | 56.7 | 7.8 | 45.1 | 68.4 | 60.7 | 14.2 | 7.0 | 17.8 |
| dulce | GE | 56.7 | 7.5 | 43.4 | 68.2 | 57.9 | 15.5 | 1.3 | 18.5 |
| dulce | XGB-37 | 48.3 | 1.4 | 45.6 | 50.2 | 65.8 | 2.0 | 36.5 | 3.1 |
| dulce | XGB-43 | 47.6 | 1.1 | 46.4 | 50.3 | 62.2 | 1.7 | 30.7 | 4.4 |
| sutil | GC3 | 6,361.3 | 488.8 | 5,353.1 | 7,033.1 | 6,074.5 | 626.9 | -4.6 | 5.7 |
| sutil | GE | 6,743.5 | 523.5 | 5,955.9 | 7,417.8 | 6,826.6 | 601.1 | 1.3 | 5.5 |
| sutil | XGB-37 | 4,881.4 | 89.5 | 4,742.1 | 5,040.8 | 5,955.2 | 221.3 | 22.0 | 3.7 |
| sutil | XGB-43 | 5,011.9 | 123.0 | 4,805.5 | 5,164.8 | 5,997.2 | 183.1 | 19.7 | 2.5 |

### T15_diagnostico_sutil — Diagnóstico de ajuste D-BR8, Sutil: MAE (t) medio entre semillas, razón val/train (mediana), corridas con razón > 2, corridas que no superan al Naive, y razón del Naive (XGB-43 exploratorio)

| modelo | anio_test | MAE_train | MAE_val | razon_mediana | sobreajuste | no_supera_naive | Naive_razon |
|---|---|---|---|---|---|---|---|
| Ridge | 2021 | 1,302 | 3,504 | 2.69 | 1/1 | 0/1 | 1.31 |
| Ridge | 2022 | 2,195 | 2,123 | 0.97 | 0/1 | 1/1 | 0.59 |
| Ridge | 2023 | 1,586 | 2,332 | 1.47 | 0/1 | 0/1 | 1.21 |
| Ridge | 2024 | 2,819 | 4,050 | 1.44 | 0/1 | 0/1 | 1.43 |
| Ridge | 2025 | 2,145 | 2,047 | 0.95 | 0/1 | 0/1 | 0.91 |
| ElasticNet | 2021 | 1,528 | 3,438 | 2.25 | 1/1 | 0/1 | 1.31 |
| ElasticNet | 2022 | 1,917 | 2,032 | 1.06 | 0/1 | 1/1 | 0.59 |
| ElasticNet | 2023 | 1,628 | 2,337 | 1.44 | 0/1 | 0/1 | 1.21 |
| ElasticNet | 2024 | 3,097 | 4,032 | 1.30 | 0/1 | 0/1 | 1.43 |
| ElasticNet | 2025 | 1,956 | 1,619 | 0.83 | 0/1 | 0/1 | 0.91 |
| XGB-37 | 2021 | 183 | 4,173 | 23.04 | 10/10 | 6/10 | 1.31 |
| XGB-37 | 2022 | 271 | 2,490 | 9.15 | 10/10 | 10/10 | 0.59 |
| XGB-37 | 2023 | 358 | 4,400 | 12.22 | 10/10 | 10/10 | 1.21 |
| XGB-37 | 2024 | 511 | 4,172 | 8.12 | 10/10 | 0/10 | 1.43 |
| XGB-37 | 2025 | 636 | 4,481 | 7.07 | 10/10 | 10/10 | 0.91 |
| GC3 | 2021 | 1,019 | 2,951 | 3.07 | 10/10 | 0/10 | 1.28 |
| GC3 | 2022 | 1,451 | 2,621 | 1.99 | 5/10 | 8/10 | 0.58 |
| GC3 | 2023 | 1,881 | 5,280 | 3.42 | 8/10 | 10/10 | 1.20 |
| GC3 | 2024 | 4,281 | 5,756 | 1.32 | 0/10 | 10/10 | 1.42 |
| GC3 | 2025 | 2,356 | 7,039 | 4.01 | 8/10 | 10/10 | 0.90 |
| GE | 2021 | 1,007 | 3,288 | 4.04 | 9/10 | 1/10 | 1.28 |
| GE | 2022 | 1,715 | 2,691 | 1.55 | 4/10 | 8/10 | 0.58 |
| GE | 2023 | 1,587 | 5,114 | 3.72 | 9/10 | 10/10 | 1.20 |
| GE | 2024 | 3,664 | 5,465 | 1.54 | 1/10 | 10/10 | 1.42 |
| GE | 2025 | 3,926 | 9,079 | 2.56 | 5/10 | 10/10 | 0.90 |
| XGB-43 | 2021 | 169 | 4,270 | 25.60 | 10/10 | 9/10 | 1.31 |
| XGB-43 | 2022 | 253 | 2,554 | 10.19 | 10/10 | 10/10 | 0.59 |
| XGB-43 | 2023 | 338 | 4,501 | 13.58 | 10/10 | 10/10 | 1.21 |
| XGB-43 | 2024 | 474 | 3,956 | 8.33 | 10/10 | 0/10 | 1.43 |
| XGB-43 | 2025 | 624 | 4,911 | 8.01 | 10/10 | 10/10 | 0.91 |

### T15_diagnostico_dulce — Diagnóstico de ajuste D-BR8, Dulce: MAE (t) medio entre semillas, razón val/train (mediana), corridas con razón > 2, corridas que no superan al Naive, y razón del Naive (XGB-43 exploratorio)

| modelo | anio_test | MAE_train | MAE_val | razon_mediana | sobreajuste | no_supera_naive | Naive_razon |
|---|---|---|---|---|---|---|---|
| Ridge | 2021 | 23.8 | 36.2 | 1.52 | 0/1 | 0/1 | 0.90 |
| Ridge | 2022 | 15.2 | 25.9 | 1.71 | 0/1 | 0/1 | 0.93 |
| Ridge | 2023 | 15.8 | 26.2 | 1.66 | 0/1 | 0/1 | 1.02 |
| Ridge | 2024 | 22.8 | 40.9 | 1.80 | 0/1 | 0/1 | 1.06 |
| Ridge | 2025 | 38.4 | 63.5 | 1.65 | 0/1 | 0/1 | 1.18 |
| ElasticNet | 2021 | 25.0 | 33.3 | 1.33 | 0/1 | 0/1 | 0.90 |
| ElasticNet | 2022 | 15.3 | 25.9 | 1.70 | 0/1 | 0/1 | 0.93 |
| ElasticNet | 2023 | 16.5 | 26.2 | 1.59 | 0/1 | 0/1 | 1.02 |
| ElasticNet | 2024 | 26.6 | 38.2 | 1.43 | 0/1 | 0/1 | 1.06 |
| ElasticNet | 2025 | 35.9 | 62.2 | 1.73 | 0/1 | 0/1 | 1.18 |
| XGB-37 | 2021 | 2.7 | 48.2 | 18.40 | 10/10 | 0/10 | 0.90 |
| XGB-37 | 2022 | 3.5 | 23.7 | 6.69 | 10/10 | 0/10 | 0.93 |
| XGB-37 | 2023 | 4.3 | 43.3 | 9.99 | 10/10 | 0/10 | 1.02 |
| XGB-37 | 2024 | 5.6 | 33.2 | 5.80 | 10/10 | 0/10 | 1.06 |
| XGB-37 | 2025 | 6.2 | 48.5 | 7.73 | 10/10 | 0/10 | 1.18 |
| GC3 | 2021 | 19.7 | 29.7 | 1.57 | 0/10 | 0/10 | 0.88 |
| GC3 | 2022 | 21.6 | 28.8 | 1.38 | 1/10 | 0/10 | 0.92 |
| GC3 | 2023 | 19.6 | 27.9 | 1.43 | 1/10 | 0/10 | 1.01 |
| GC3 | 2024 | 18.4 | 26.4 | 1.49 | 0/10 | 0/10 | 1.05 |
| GC3 | 2025 | 19.6 | 69.5 | 3.44 | 10/10 | 1/10 | 1.17 |
| GE | 2021 | 19.0 | 33.1 | 1.58 | 3/10 | 1/10 | 0.88 |
| GE | 2022 | 23.5 | 32.4 | 1.17 | 2/10 | 0/10 | 0.92 |
| GE | 2023 | 19.5 | 29.0 | 1.57 | 1/10 | 0/10 | 1.01 |
| GE | 2024 | 17.3 | 30.5 | 1.94 | 3/10 | 0/10 | 1.05 |
| GE | 2025 | 16.8 | 60.8 | 3.56 | 10/10 | 0/10 | 1.17 |
| XGB-43 | 2021 | 2.3 | 55.0 | 24.07 | 10/10 | 0/10 | 0.90 |
| XGB-43 | 2022 | 3.1 | 24.1 | 8.29 | 10/10 | 0/10 | 0.93 |
| XGB-43 | 2023 | 3.8 | 43.2 | 11.43 | 10/10 | 0/10 | 1.02 |
| XGB-43 | 2024 | 5.0 | 32.9 | 6.51 | 10/10 | 0/10 | 1.06 |
| XGB-43 | 2025 | 5.9 | 46.5 | 7.99 | 10/10 | 0/10 | 1.18 |

### T15_mejor_epoca_por_ventana — Mejor época (early stopping, paciencia 15) por ventana: distribución entre las 10 semillas

| modelo | cultivar | anio_test | mediana | q1 | q3 | minimo | maximo | epocas_corridas_mediana | epocas_corridas_max |
|---|---|---|---|---|---|---|---|---|---|
| GC3 | dulce | 2021 | 50.5 | 35.5 | 58.8 | 30 | 64 | 65.5 | 79 |
| GC3 | dulce | 2022 | 32.0 | 25.2 | 47.8 | 14 | 66 | 47.0 | 81 |
| GC3 | dulce | 2023 | 29.5 | 22.5 | 33.8 | 18 | 52 | 44.5 | 67 |
| GC3 | dulce | 2024 | 28.5 | 19.2 | 44.8 | 14 | 80 | 43.5 | 95 |
| GC3 | dulce | 2025 | 26.5 | 14.0 | 38.5 | 13 | 50 | 41.5 | 65 |
| GC3 | sutil | 2021 | 67.5 | 52.5 | 71.8 | 33 | 91 | 82.5 | 106 |
| GC3 | sutil | 2022 | 48.0 | 36.5 | 58.0 | 13 | 65 | 63.0 | 80 |
| GC3 | sutil | 2023 | 20.5 | 16.2 | 39.8 | 13 | 56 | 35.5 | 71 |
| GC3 | sutil | 2024 | 7.5 | 6.0 | 10.2 | 4 | 20 | 22.5 | 35 |
| GC3 | sutil | 2025 | 43.5 | 24.5 | 53.8 | 1 | 101 | 58.5 | 116 |
| GE | dulce | 2021 | 46.0 | 30.2 | 72.2 | 17 | 98 | 61.0 | 113 |
| GE | dulce | 2022 | 33.0 | 18.0 | 46.8 | 12 | 63 | 48.0 | 78 |
| GE | dulce | 2023 | 31.0 | 21.5 | 32.8 | 18 | 53 | 46.0 | 68 |
| GE | dulce | 2024 | 34.5 | 22.2 | 47.5 | 14 | 50 | 49.5 | 65 |
| GE | dulce | 2025 | 35.0 | 28.2 | 44.8 | 14 | 78 | 50.0 | 93 |
| GE | sutil | 2021 | 57.5 | 46.0 | 62.2 | 27 | 117 | 72.5 | 132 |
| GE | sutil | 2022 | 34.5 | 19.0 | 72.5 | 13 | 86 | 49.5 | 101 |
| GE | sutil | 2023 | 24.0 | 18.0 | 29.5 | 16 | 54 | 39.0 | 69 |
| GE | sutil | 2024 | 9.0 | 8.0 | 12.8 | 6 | 20 | 24.0 | 35 |
| GE | sutil | 2025 | 10.5 | 1.2 | 33.0 | 1 | 67 | 25.5 | 82 |

### T03_particiones_sutil — Descripción de la serie por partición (train desde 2016-07), Sutil (t)

| anio_test | particion | inicio | fin | n | media | DE | min | max | CV |
|---|---|---|---|---|---|---|---|---|---|
| 2021 | train | 2016-07 | 2019-12 | 42 | 19,715 | 7,293 | 4,852 | 33,259 | 0.37 |
| 2021 | val | 2020-01 | 2020-12 | 12 | 25,132 | 6,673 | 14,810 | 35,010 | 0.27 |
| 2021 | test | 2021-01 | 2021-12 | 12 | 27,980 | 4,362 | 22,839 | 35,180 | 0.16 |
| 2022 | train | 2016-07 | 2020-12 | 54 | 20,919 | 7,453 | 4,852 | 35,010 | 0.36 |
| 2022 | val | 2021-01 | 2021-12 | 12 | 27,980 | 4,362 | 22,839 | 35,180 | 0.16 |
| 2022 | test | 2022-01 | 2022-12 | 12 | 30,558 | 8,004 | 20,730 | 41,868 | 0.26 |
| 2023 | train | 2016-07 | 2021-12 | 66 | 22,203 | 7,487 | 4,852 | 35,180 | 0.34 |
| 2023 | val | 2022-01 | 2022-12 | 12 | 30,558 | 8,004 | 20,730 | 41,868 | 0.26 |
| 2023 | test | 2023-01 | 2023-12 | 12 | 23,067 | 8,319 | 9,388 | 36,552 | 0.36 |
| 2024 | train | 2016-07 | 2022-12 | 78 | 23,488 | 8,104 | 4,852 | 41,868 | 0.35 |
| 2024 | val | 2023-01 | 2023-12 | 12 | 23,067 | 8,319 | 9,388 | 36,552 | 0.36 |
| 2024 | test | 2024-01 | 2024-12 | 12 | 32,209 | 8,550 | 23,811 | 44,162 | 0.27 |
| 2025 | train | 2016-07 | 2023-12 | 90 | 23,432 | 8,087 | 4,852 | 41,868 | 0.35 |
| 2025 | val | 2024-01 | 2024-12 | 12 | 32,209 | 8,550 | 23,811 | 44,162 | 0.27 |
| 2025 | test | 2025-01 | 2025-12 | 12 | 31,908 | 9,103 | 18,017 | 42,120 | 0.29 |

### T04_estacionariedad_sutil — ACF, ADF y KPSS (p) en TRAIN, nivel y Δ12, Sutil (KPSS p acotado a [0.01, 0.10]; '—' = n < 24)

| anio_test | n_train | ACF1 | ACF12 | ADF_nivel_p | KPSS_nivel_p | n_D12 | ADF_D12_p | KPSS_D12_p |
|---|---|---|---|---|---|---|---|---|
| 2018 | 6 | — | — | — | — | 0 | — | — |
| 2019 | 18 | — | — | — | — | 12 | — | — |
| 2020 | 30 | 0.822 | 0.045 | 0.090 | 0.100 | 24 | 0.025 | 0.059 |
| 2021 | 42 | 0.839 | 0.334 | 0.011 | 0.100 | 36 | 0.000 | 0.075 |
| 2022 | 54 | 0.812 | 0.489 | 0.004 | 0.100 | 48 | 0.001 | 0.100 |
| 2023 | 66 | 0.840 | 0.545 | 0.002 | 0.035 | 60 | 0.018 | 0.100 |
| 2024 | 78 | 0.855 | 0.559 | 0.863 | 0.016 | 72 | 0.067 | 0.100 |
| 2025 | 90 | 0.849 | 0.585 | 0.641 | 0.039 | 84 | 0.456 | 0.100 |

### T03_particiones_dulce — Descripción de la serie por partición (train desde 2016-07), Dulce (t)

| anio_test | particion | inicio | fin | n | media | DE | min | max | CV |
|---|---|---|---|---|---|---|---|---|---|
| 2021 | train | 2016-07 | 2019-12 | 42 | 385.9 | 144.9 | 135.7 | 630.7 | 0.38 |
| 2021 | val | 2020-01 | 2020-12 | 12 | 379.5 | 144.6 | 180.7 | 573.6 | 0.38 |
| 2021 | test | 2021-01 | 2021-12 | 12 | 393.8 | 144.0 | 205.9 | 600.3 | 0.37 |
| 2022 | train | 2016-07 | 2020-12 | 54 | 384.5 | 143.5 | 135.7 | 630.7 | 0.37 |
| 2022 | val | 2021-01 | 2021-12 | 12 | 393.8 | 144.0 | 205.9 | 600.3 | 0.37 |
| 2022 | test | 2022-01 | 2022-12 | 12 | 406.4 | 154.5 | 205.8 | 636.7 | 0.38 |
| 2023 | train | 2016-07 | 2021-12 | 66 | 386.2 | 142.5 | 135.7 | 630.7 | 0.37 |
| 2023 | val | 2022-01 | 2022-12 | 12 | 406.4 | 154.5 | 205.8 | 636.7 | 0.38 |
| 2023 | test | 2023-01 | 2023-12 | 12 | 406.5 | 159.9 | 206.4 | 663.1 | 0.39 |
| 2024 | train | 2016-07 | 2022-12 | 78 | 389.3 | 143.6 | 135.7 | 636.7 | 0.37 |
| 2024 | val | 2023-01 | 2023-12 | 12 | 406.5 | 159.9 | 206.4 | 663.1 | 0.39 |
| 2024 | test | 2024-01 | 2024-12 | 12 | 448.3 | 161.4 | 229.4 | 675.8 | 0.36 |
| 2025 | train | 2016-07 | 2023-12 | 90 | 391.6 | 145.0 | 135.7 | 663.1 | 0.37 |
| 2025 | val | 2024-01 | 2024-12 | 12 | 448.3 | 161.4 | 229.4 | 675.8 | 0.36 |
| 2025 | test | 2025-01 | 2025-12 | 12 | 467.8 | 177.3 | 228.7 | 730.4 | 0.38 |

### T04_estacionariedad_dulce — ACF, ADF y KPSS (p) en TRAIN, nivel y Δ12, Dulce (KPSS p acotado a [0.01, 0.10]; '—' = n < 24)

| anio_test | n_train | ACF1 | ACF12 | ADF_nivel_p | KPSS_nivel_p | n_D12 | ADF_D12_p | KPSS_D12_p |
|---|---|---|---|---|---|---|---|---|
| 2018 | 6 | — | — | — | — | 0 | — | — |
| 2019 | 18 | — | — | — | — | 12 | — | — |
| 2020 | 30 | 0.781 | 0.527 | 0.000 | 0.100 | 24 | 0.985 | 0.100 |
| 2021 | 42 | 0.794 | 0.667 | 0.267 | 0.100 | 36 | 0.045 | 0.027 |
| 2022 | 54 | 0.801 | 0.743 | 0.915 | 0.100 | 48 | 0.006 | 0.034 |
| 2023 | 66 | 0.809 | 0.786 | 0.779 | 0.100 | 60 | 0.001 | 0.100 |
| 2024 | 78 | 0.815 | 0.808 | 0.446 | 0.100 | 72 | 0.000 | 0.100 |
| 2025 | 90 | 0.818 | 0.832 | 0.377 | 0.100 | 84 | 0.000 | 0.100 |

### T20_sarima_sel — SARIMA-sel: orden elegido por ventana (D-BR10) y posición en AIC

| cultivar | anio_test | orden | orden_estacional | posicion_AIC | AIC | MAE_val | convergio | fallidos | AIC_no_finito | no_conv_rejilla |
|---|---|---|---|---|---|---|---|---|---|---|
| sutil | 2021 | (2, 1, 0) | (2, 1, 1, 12) | 3 | 954.4 | 2,256.7 | sí | 0 | 0 | 30 |
| sutil | 2022 | (3, 1, 2) | (2, 1, 2, 12) | 4 | 1,183.6 | 1,942.2 | sí | 0 | 0 | 38 |
| sutil | 2023 | (1, 1, 3) | (2, 1, 1, 12) | 2 | 1,406.3 | 2,514.3 | sí | 0 | 0 | 0 |
| sutil | 2024 | (1, 1, 2) | (2, 1, 1, 12) | 1 | 1,635.0 | 4,175.2 | sí | 0 | 0 | 36 |
| sutil | 2025 | (1, 1, 3) | (2, 1, 0, 12) | 4 | 1,874.9 | 2,880.5 | sí | 0 | 0 | 57 |
| dulce | 2021 | (2, 0, 3) | (0, 0, 0, 12) | 2 | 470.1 | 36.8 | sí | 0 | 0 | 78 |
| dulce | 2022 | (1, 0, 0) | (0, 1, 0, 12) | 2 | 594.3 | 13.6 | sí | 0 | 0 | 82 |
| dulce | 2023 | (2, 0, 0) | (0, 1, 0, 12) | 4 | 702.6 | 12.0 | sí | 0 | 0 | 36 |
| dulce | 2024 | (2, 0, 0) | (0, 1, 0, 12) | 2 | 805.7 | 17.3 | sí | 0 | 0 | 103 |
| dulce | 2025 | (2, 0, 1) | (0, 1, 0, 12) | 4 | 913.5 | 25.9 | sí | 0 | 0 | 158 |

### T21_lineales_hiperparametros — Ridge y ElasticNet: α (y l1) elegidos con la validación Y−1

| modelo | cultivar | anio_test | alpha | l1_ratio | MAE_val | control_v3_coincide |
|---|---|---|---|---|---|---|
| Ridge | sutil | 2021 | 1.00 | — | 3,504.28 | — |
| Ridge | sutil | 2022 | 10.00 | — | 2,122.62 | — |
| Ridge | sutil | 2023 | 1.00 | — | 2,332.16 | — |
| Ridge | sutil | 2024 | 100.00 | — | 4,050.05 | — |
| Ridge | sutil | 2025 | 10.00 | — | 2,047.11 | sí |
| Ridge | dulce | 2021 | 10.00 | — | 36.22 | — |
| Ridge | dulce | 2022 | 0.10 | — | 25.93 | — |
| Ridge | dulce | 2023 | 1.00 | — | 26.21 | — |
| Ridge | dulce | 2024 | 10.00 | — | 40.93 | — |
| Ridge | dulce | 2025 | 100.00 | — | 63.54 | sí |
| ElasticNet | sutil | 2021 | 0.10 | 0.50 | 3,437.71 | — |
| ElasticNet | sutil | 2022 | 0.10 | 0.20 | 2,032.26 | — |
| ElasticNet | sutil | 2023 | 0.10 | 0.80 | 2,336.56 | — |
| ElasticNet | sutil | 2024 | 10.00 | 0.80 | 4,031.62 | — |
| ElasticNet | sutil | 2025 | 0.10 | 0.50 | 1,619.16 | sí |
| ElasticNet | dulce | 2021 | 1.00 | 0.80 | 33.25 | — |
| ElasticNet | dulce | 2022 | 0.01 | 0.80 | 25.93 | — |
| ElasticNet | dulce | 2023 | 0.10 | 0.80 | 26.22 | — |
| ElasticNet | dulce | 2024 | 1.00 | 0.80 | 38.24 | — |
| ElasticNet | dulce | 2025 | 1.00 | 0.20 | 62.17 | sí |

### T16_exploratorio_xgb43 — EXPLORATORIO (post-hoc): XGB-43 frente a XGB-37, 2021-2025, P75 mensual (t)

| cultivar | alcance | n_meses | MAE_XGB37 | MAE_XGB43 | dif_43_menos_37 | IC95_lo | IC95_hi |
|---|---|---|---|---|---|---|---|
| sutil | global | 60 | 4,881.4 | 5,011.9 | 130.5 | 1.5 | 260.4 |
| sutil | shock_P75 | 10 | 5,955.2 | 5,997.2 | 42.0 | -240.1 | 338.3 |
| sutil | normal_P75 | 50 | 4,666.7 | 4,814.9 | 148.2 | 6.5 | 286.3 |
| dulce | global | 60 | 48.3 | 47.6 | -0.6 | -2.4 | 1.2 |
| dulce | shock_P75 | 15 | 65.8 | 62.2 | -3.6 | -5.9 | -1.2 |
| dulce | normal_P75 | 45 | 42.4 | 42.8 | 0.4 | -1.7 | 2.5 |

### T_barrido_posiciones_mensual_sutil — Posición por MAE_shock en cada percentil, mensual, Sutil, 2021-2025 (* = primero o empatado con el primero)

| modelo | P0 | P10 | P15 | P20 | P25 | P30 | P35 | P40 | P45 | P50 | P55 | P60 | P65 | P70 | P75 | P80 | P85 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 4 | 4 | 4 | 4 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 8 | 8 | 8 | 9 | 8 | 8 | 7 | 10 |
| Seasonal Naive | 8 | 8 | 8 | 8 | 8 | 6 | 6 | 8 | 6 | 6 | 7 | 5 | 5 | 4* | 3* | 2* | 2* | 4* | 4* |
| Chronos | 1* | 1* | 1* | 1* | 1* | 2* | 1* | 2* | 2* | 2* | 2* | 3* | 3* | 2* | 1* | 1* | 1* | 1* | 1* |
| SARIMA | 3 | 3* | 3* | 3* | 3* | 3* | 3* | 3* | 3* | 3* | 3* | 2* | 2* | 3* | 4* | 4 | 4 | 2 | 5 |
| SARIMA-sel | 2* | 2* | 2* | 2* | 2* | 1* | 2* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 2* | 3* | 3* | 3 | 2* |
| Ridge | 7 | 7 | 7 | 7 | 7 | 8 | 7 | 9 | 9 | 9 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 7 |
| ElasticNet | 5 | 6 | 6 | 6 | 6 | 7 | 8 | 10 | 10 | 10 | 9 | 9 | 9 | 9 | 8 | 9 | 9 | 9 | 3 |
| XGB-37 | 6 | 5 | 5 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5* | 5* | 5* | 5* | 6 | 8 |
| GC3 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 7 | 8 | 8 | 8 | 6 | 6 | 6 | 6* | 6 | 6* | 5 | 6 |
| GE | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 6 | 7 | 7 | 6 | 7 | 7 | 7 | 7 | 7 | 7 | 8 | 9 |
| n_shock | 60 | 51 | 47 | 45 | 43 | 38 | 36 | 32 | 29 | 29 | 28 | 25 | 21 | 12 | 10 | 8 | 7 | 6 | 3 |

### T_barrido_delta_s_mensual_sutil — Δs (%) por percentil, mensual, Sutil, 2021-2025

| modelo | P0 | P10 | P15 | P20 | P25 | P30 | P35 | P40 | P45 | P50 | P55 | P60 | P65 | P70 | P75 | P80 | P85 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 0 | 17 | 25 | 30 | 34 | 46 | 50 | 59 | 66 | 66 | 69 | 78 | 90 | 115 | 135 | 141 | 149 | 140 | 160 |
| Seasonal Naive | 0 | -6 | -6 | -5 | -5 | -3 | -2 | 4 | 0 | 0 | 3 | 4 | -2 | -16 | -17 | -5 | 7 | 20 | 15 |
| Chronos | 0 | 4 | 8 | 11 | 14 | 19 | 23 | 28 | 34 | 34 | 38 | 42 | 41 | 68 | 81 | 94 | 108 | 105 | 114 |
| SARIMA | 0 | -2 | -0 | 3 | 3 | -0 | 0 | 3 | 8 | 8 | 10 | 5 | 6 | 36 | 53 | 82 | 103 | 101 | 111 |
| SARIMA-sel | 0 | -2 | -3 | -3 | -1 | -2 | 3 | 2 | 5 | 5 | 5 | 8 | 1 | 29 | 54 | 82 | 108 | 121 | 95 |
| Ridge | 0 | 6 | 9 | 11 | 14 | 21 | 22 | 35 | 40 | 40 | 44 | 52 | 62 | 91 | 74 | 108 | 126 | 137 | 55 |
| ElasticNet | 0 | 5 | 8 | 11 | 14 | 22 | 24 | 36 | 42 | 42 | 45 | 52 | 60 | 82 | 67 | 102 | 121 | 123 | 41 |
| XGB-37 | 0 | 0 | 1 | -1 | 3 | 6 | 1 | -1 | 0 | 0 | 3 | 7 | 3 | 7 | 22 | 37 | 41 | 63 | 88 |
| GC3 | 0 | 1 | 0 | -1 | 2 | 2 | -0 | -1 | -2 | -2 | -1 | 0 | 3 | -7 | -5 | 11 | 10 | 24 | 14 |
| GE | 0 | 1 | 1 | -1 | 1 | -3 | -5 | -7 | -9 | -9 | -7 | -5 | 1 | -6 | 1 | 19 | 17 | 33 | 38 |

### T_barrido_n_shock_mensual_sutil — n_shock por ventana y percentil, mensual, Sutil (< 2 = ventana no informativa)

| ventana | P0 | P10 | P15 | P20 | P25 | P30 | P35 | P40 | P45 | P50 | P55 | P60 | P65 | P70 | P75 | P80 | P85 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2021 | 12 | 7 | 7 | 7 | 7 | 6 | 5 | 3 | 2 | 2 | 2 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2022 | 12 | 11 | 10 | 9 | 8 | 8 | 7 | 7 | 7 | 7 | 6 | 4 | 4 | 3 | 3 | 1 | 1 | 1 | 0 |
| 2023 | 12 | 12 | 12 | 12 | 12 | 11 | 11 | 11 | 11 | 11 | 11 | 10 | 8 | 5 | 4 | 4 | 3 | 3 | 1 |
| 2024 | 12 | 9 | 7 | 7 | 6 | 6 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2025 | 12 | 12 | 11 | 10 | 10 | 7 | 7 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 3 | 2 | 2 |

### T_barrido_posiciones_interanual_sutil — Posición por MAE_shock en cada percentil, interanual, Sutil, 2021-2025 (* = primero o empatado con el primero)

| modelo | P0 | P10 | P15 | P20 | P25 | P30 | P35 | P40 | P45 | P50 | P55 | P60 | P65 | P70 | P75 | P80 | P85 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 4 | 4 | 4 | 4 | 4* | 2* | 2* | 2* | 2* | 2* | 2* | 2* | 3* | 2* | 2* | 3 | 3 | 2* | 2* |
| Seasonal Naive | 8 | 9 | 9 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 |
| Chronos | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* |
| SARIMA | 3 | 3 | 3 | 3* | 3* | 4* | 4* | 4 | 3* | 3* | 3* | 3* | 2* | 3 | 3 | 2 | 2 | 3 | 6 |
| SARIMA-sel | 2* | 2* | 2* | 2* | 2* | 3* | 3* | 3* | 4* | 4* | 4* | 4 | 4 | 4 | 4 | 5 | 5 | 6 | 7 |
| Ridge | 7 | 5 | 5 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 4 | 4 | 4 | 3* |
| ElasticNet | 5 | 6 | 6 | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 5 | 4* |
| XGB-37 | 6 | 7 | 7 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 6 | 6 | 7* | 5* |
| GC3 | 9 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 9 | 9 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 |
| GE | 10 | 10 | 10 | 9 | 9 | 9 | 9 | 9 | 8 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| n_shock | 60 | 52 | 51 | 44 | 42 | 38 | 34 | 33 | 27 | 25 | 21 | 18 | 16 | 13 | 10 | 7 | 7 | 4 | 3 |

### T_barrido_delta_s_interanual_sutil — Δs (%) por percentil, interanual, Sutil, 2021-2025

| modelo | P0 | P10 | P15 | P20 | P25 | P30 | P35 | P40 | P45 | P50 | P55 | P60 | P65 | P70 | P75 | P80 | P85 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 0 | 0 | 2 | -3 | -2 | -8 | -9 | -11 | 3 | 2 | 8 | -7 | -2 | -25 | -12 | 5 | 5 | -58 | -52 |
| Seasonal Naive | 0 | 14 | 16 | 28 | 32 | 39 | 46 | 48 | 63 | 66 | 76 | 80 | 87 | 95 | 106 | 123 | 123 | 151 | 138 |
| Chronos | 0 | 4 | 5 | 5 | 9 | 8 | 10 | 10 | 22 | 20 | 21 | 2 | 4 | -14 | -30 | -31 | -31 | -58 | -48 |
| SARIMA | 0 | 5 | 6 | 3 | 4 | 6 | 10 | 13 | 18 | 17 | 19 | 9 | 4 | 1 | -4 | 6 | 6 | 11 | 13 |
| SARIMA-sel | 0 | 6 | 7 | 5 | 6 | 8 | 14 | 14 | 27 | 27 | 39 | 32 | 41 | 38 | 27 | 45 | 45 | 72 | 62 |
| Ridge | 0 | -0 | 0 | 2 | 7 | 15 | 21 | 21 | 21 | 18 | 25 | 20 | 23 | -1 | 0 | -11 | -11 | -15 | -41 |
| ElasticNet | 0 | 2 | 3 | 7 | 11 | 19 | 26 | 26 | 28 | 25 | 32 | 27 | 28 | 7 | 11 | 2 | 2 | -1 | -32 |
| XGB-37 | 0 | 3 | 5 | 1 | 2 | 2 | 6 | 6 | 8 | 6 | 2 | 3 | 8 | -1 | -1 | 1 | 1 | 14 | -31 |
| GC3 | 0 | 7 | 9 | 6 | 8 | 11 | 19 | 17 | 24 | 20 | 22 | 25 | 26 | 27 | 44 | 43 | 43 | 61 | 13 |
| GE | 0 | 7 | 9 | 0 | 4 | 6 | 13 | 11 | 17 | 13 | 16 | 21 | 21 | 25 | 45 | 48 | 48 | 68 | 26 |

### T_barrido_n_shock_interanual_sutil — n_shock por ventana y percentil, interanual, Sutil (< 2 = ventana no informativa)

| ventana | P0 | P10 | P15 | P20 | P25 | P30 | P35 | P40 | P45 | P50 | P55 | P60 | P65 | P70 | P75 | P80 | P85 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2021 | 12 | 10 | 10 | 9 | 9 | 9 | 6 | 6 | 3 | 3 | 2 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
| 2022 | 12 | 9 | 8 | 8 | 7 | 5 | 5 | 5 | 3 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2023 | 12 | 10 | 10 | 10 | 10 | 9 | 9 | 9 | 8 | 7 | 7 | 6 | 5 | 3 | 2 | 1 | 1 | 0 | 0 |
| 2024 | 12 | 11 | 11 | 11 | 11 | 11 | 10 | 9 | 9 | 8 | 8 | 8 | 8 | 8 | 8 | 6 | 6 | 4 | 3 |
| 2025 | 12 | 12 | 12 | 6 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |

### T_barrido_posiciones_mensual_dulce — Posición por MAE_shock en cada percentil, mensual, Dulce, 2021-2025 (* = primero o empatado con el primero)

| modelo | P0 | P10 | P15 | P20 | P25 | P30 | P35 | P40 | P45 | P50 | P55 | P60 | P65 | P70 | P75 | P80 | P85 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 |
| Seasonal Naive | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 |
| Chronos | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 |
| SARIMA | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* |
| SARIMA-sel | 2* | 2* | 2* | 2* | 2* | 2* | 2* | 2* | 2* | 2* | 2* | 2* | 2* | 2 | 2 | 2 | 2 | 3 | 9 |
| Ridge | 7 | 7 | 7 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 8 | 8 |
| ElasticNet | 6 | 6 | 6 | 6 | 7 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 7 | 7 | 7 |
| XGB-37 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 6 | 5 | 7 | 6 | 6 | 7 | 7 | 7 | 9 | 9 | 2 |
| GC3 | 8 | 9 | 8 | 9 | 8 | 7 | 7 | 7 | 7 | 7 | 6 | 7 | 7 | 6 | 6 | 6 | 6 | 5 | 6 |
| GE | 9 | 8 | 9 | 8 | 6 | 6 | 6 | 6 | 5 | 6 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 6 | 4 |
| n_shock | 60 | 59 | 53 | 51 | 44 | 42 | 38 | 34 | 29 | 28 | 25 | 23 | 22 | 17 | 15 | 12 | 9 | 5 | 1 |

### T_barrido_delta_s_mensual_dulce — Δs (%) por percentil, mensual, Dulce, 2021-2025

| modelo | P0 | P10 | P15 | P20 | P25 | P30 | P35 | P40 | P45 | P50 | P55 | P60 | P65 | P70 | P75 | P80 | P85 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 0 | 2 | 10 | 13 | 24 | 27 | 32 | 40 | 48 | 51 | 58 | 61 | 61 | 61 | 70 | 68 | 67 | 43 | 10 |
| Seasonal Naive | 0 | 0 | -4 | -1 | 4 | 2 | -3 | 0 | -16 | -17 | -12 | -11 | -8 | -9 | -0 | 2 | 4 | -13 | -34 |
| Chronos | 0 | 1 | 9 | 11 | 15 | 16 | 20 | 27 | 25 | 28 | 35 | 36 | 35 | 48 | 56 | 64 | 54 | 23 | -25 |
| SARIMA | 0 | 1 | 2 | 4 | 7 | -1 | -2 | -4 | -17 | -21 | -28 | -25 | -22 | -25 | -24 | -32 | -22 | -42 | -71 |
| SARIMA-sel | 0 | 1 | 1 | -2 | 2 | -5 | -2 | -4 | -12 | -15 | -17 | -22 | -19 | -9 | -5 | -2 | 18 | 41 | 110 |
| Ridge | 0 | 2 | -1 | 2 | 7 | 10 | 7 | 10 | 10 | 9 | 10 | 7 | 11 | 27 | 31 | 37 | 27 | -12 | -19 |
| ElasticNet | 0 | 2 | -2 | 1 | 6 | 9 | 6 | 9 | 9 | 8 | 8 | 8 | 11 | 29 | 34 | 42 | 32 | -9 | -18 |
| XGB-37 | 0 | 1 | -2 | -0 | 1 | 4 | -2 | 3 | -2 | -1 | 6 | 10 | 10 | 30 | 36 | 43 | 45 | 18 | -76 |
| GC3 | 0 | 0 | -6 | -3 | -5 | -4 | -14 | -9 | -15 | -13 | -10 | -6 | -3 | -0 | 7 | 16 | 1 | -30 | -50 |
| GE | 0 | -0 | -6 | -4 | -6 | -6 | -16 | -12 | -17 | -16 | -13 | -11 | -8 | -5 | 2 | 9 | -1 | -30 | -62 |

### T_barrido_n_shock_mensual_dulce — n_shock por ventana y percentil, mensual, Dulce (< 2 = ventana no informativa)

| ventana | P0 | P10 | P15 | P20 | P25 | P30 | P35 | P40 | P45 | P50 | P55 | P60 | P65 | P70 | P75 | P80 | P85 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2021 | 12 | 11 | 10 | 9 | 9 | 8 | 7 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 3 | 3 | 3 | 1 |
| 2022 | 12 | 12 | 11 | 10 | 9 | 9 | 7 | 6 | 5 | 5 | 5 | 5 | 4 | 4 | 3 | 2 | 2 | 1 | 0 |
| 2023 | 12 | 12 | 11 | 11 | 8 | 8 | 8 | 8 | 7 | 6 | 4 | 4 | 4 | 3 | 2 | 1 | 1 | 0 | 0 |
| 2024 | 12 | 12 | 10 | 10 | 8 | 8 | 8 | 8 | 6 | 6 | 6 | 5 | 5 | 4 | 4 | 3 | 2 | 1 | 0 |
| 2025 | 12 | 12 | 11 | 11 | 10 | 9 | 8 | 7 | 6 | 6 | 5 | 5 | 5 | 3 | 3 | 3 | 1 | 0 | 0 |

### T_barrido_posiciones_interanual_dulce — Posición por MAE_shock en cada percentil, interanual, Dulce, 2021-2025 (* = primero o empatado con el primero)

| modelo | P0 | P10 | P15 | P20 | P25 | P30 | P35 | P40 | P45 | P50 | P55 | P60 | P65 | P70 | P75 | P80 | P85 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10* | 8* | 1* |
| Seasonal Naive | 3 | 3 | 3 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 6 | 8 | 10 | 7 |
| Chronos | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 3 | 3* | 3* | 3* | 3* | 3* | 3* | 3* | 1* | 1* | 1* | 5 |
| SARIMA | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 1* | 2* | 1* | 1* | 1* | 2* | 3 | 6 | 2 |
| SARIMA-sel | 2* | 2* | 2* | 2* | 2* | 2* | 2* | 2* | 2* | 2* | 2* | 1* | 2* | 2* | 2* | 4* | 6 | 4 | 3 |
| Ridge | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 8 | 7 | 9 | 9 | 9 | 9 | 9 | 9 | 5 | 10 |
| ElasticNet | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 8 | 7 | 7 | 5 | 3 | 9 |
| XGB-37 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 3* | 2* | 2* | 4 |
| GC3 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 | 8 | 7 | 8 | 8 | 7 | 9 | 8 |
| GE | 9 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 7 | 8 | 7 | 7 | 6 | 6 | 5 | 4 | 7 | 6 |
| n_shock | 60 | 52 | 49 | 45 | 42 | 40 | 37 | 35 | 30 | 29 | 28 | 23 | 21 | 19 | 16 | 9 | 6 | 4 | 1 |

### T_barrido_delta_s_interanual_dulce — Δs (%) por percentil, interanual, Dulce, 2021-2025

| modelo | P0 | P10 | P15 | P20 | P25 | P30 | P35 | P40 | P45 | P50 | P55 | P60 | P65 | P70 | P75 | P80 | P85 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 0 | 2 | -3 | -0 | -3 | -1 | 4 | 3 | 3 | 5 | 1 | 1 | -1 | -3 | 7 | 2 | -15 | -22 | -26 |
| Seasonal Naive | 0 | 14 | 19 | 25 | 30 | 34 | 39 | 42 | 50 | 53 | 54 | 63 | 66 | 65 | 73 | 95 | 127 | 180 | 405 |
| Chronos | 0 | 1 | -2 | -0 | -3 | 1 | 7 | 7 | 2 | 3 | -1 | -1 | -0 | -2 | 8 | -10 | -12 | 3 | 234 |
| SARIMA | 0 | 6 | 10 | 8 | 13 | 12 | 19 | 21 | 29 | 32 | 34 | 47 | 49 | 53 | 49 | 87 | 158 | 222 | 379 |
| SARIMA-sel | 0 | 8 | 10 | 8 | 9 | 4 | 10 | 9 | 18 | 20 | 22 | 28 | 35 | 39 | 38 | 77 | 138 | 160 | 328 |
| Ridge | 0 | 4 | 6 | 9 | 12 | 17 | 21 | 23 | 20 | 22 | 19 | 25 | 25 | 23 | 25 | 17 | 9 | 7 | 195 |
| ElasticNet | 0 | 3 | 6 | 8 | 11 | 15 | 19 | 20 | 16 | 18 | 15 | 19 | 17 | 14 | 14 | -2 | -4 | -2 | 189 |
| XGB-37 | 0 | 4 | 2 | 5 | 7 | 11 | 16 | 13 | 9 | 10 | 4 | 5 | 2 | -9 | -12 | -29 | -28 | -10 | 87 |
| GC3 | 0 | 7 | 10 | 12 | 15 | 19 | 22 | 22 | 16 | 18 | 19 | 15 | 10 | -1 | 3 | -10 | -4 | 19 | 139 |
| GE | 0 | 6 | 9 | 9 | 12 | 15 | 17 | 17 | 12 | 14 | 14 | 11 | 6 | -4 | -1 | -19 | -15 | 5 | 118 |

### T_barrido_n_shock_interanual_dulce — n_shock por ventana y percentil, interanual, Dulce (< 2 = ventana no informativa)

| ventana | P0 | P10 | P15 | P20 | P25 | P30 | P35 | P40 | P45 | P50 | P55 | P60 | P65 | P70 | P75 | P80 | P85 | P90 | P95 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2021 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 4 | 4 | 3 | 2 | 2 | 2 | 2 | 2 | 1 | 0 |
| 2022 | 12 | 10 | 9 | 9 | 8 | 8 | 6 | 6 | 6 | 6 | 5 | 4 | 4 | 3 | 2 | 1 | 0 | 0 | 0 |
| 2023 | 12 | 8 | 7 | 5 | 4 | 4 | 4 | 3 | 2 | 2 | 2 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 2024 | 12 | 12 | 12 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 10 | 10 | 10 | 9 | 5 | 3 | 2 | 1 |
| 2025 | 12 | 11 | 11 | 11 | 11 | 10 | 10 | 10 | 7 | 6 | 6 | 5 | 4 | 3 | 3 | 1 | 1 | 1 | 0 |

### T_barrido_estabilizacion — Estabilización del ranking por MAE_shock (percentil desde el cual el primer lugar no cambia / todos empatan)

| cultivar | tipo | primer_lugar_estable_desde | modelo_estable | todos_empatan_desde |
|---|---|---|---|---|
| sutil | mensual | 75 | Chronos | — |
| sutil | interanual | 0 | Chronos | — |
| dulce | mensual | 0 | SARIMA | — |
| dulce | interanual | 95 | Naive | — |

### T_comprobacion_P0 — Comprobación de P0 con datos reales: Δs debe ser exactamente 0

| cultivar | tipo | comprobaciones | max_abs_Delta_s | todos_cero_exacto |
|---|---|---|---|---|
| dulce | interanual | 60 | 0.000 | sí |
| dulce | mensual | 60 | 0.000 | sí |
| sutil | interanual | 60 | 0.000 | sí |
| sutil | mensual | 60 | 0.000 | sí |

## Anexo: tablas completas en formato largo (todas las filas)

### T05_metricas_por_ventana.csv — T05 completa: modelo × cultivo × ventana × tipo × percentil de reporte

`06_metricas/por_ventana/T05_metricas_por_ventana.csv` — 1024 filas × 17 columnas.

| cultivar | modelo | anio_test | tipo | percentil | MAE | RMSE | MASE | MAE_normal | MAE_shock | n_shock | n_normal | Delta_s | razon_shock_normal | informativa | conjunto | exploratorio |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| sutil | Naive | 2018 | mensual | 50 | 2,726.637 | 3,748.277 | — | 971.480 | 6,236.951 | 4 | 8 | 128.742 | 6.420 | sí | descriptivo_2018_2020 | no |
| sutil | Naive | 2018 | mensual | 60 | 2,726.637 | 3,748.277 | — | 971.480 | 6,236.951 | 4 | 8 | 128.742 | 6.420 | sí | descriptivo_2018_2020 | no |
| sutil | Naive | 2018 | mensual | 75 | 2,726.637 | 3,748.277 | — | 971.480 | 6,236.951 | 4 | 8 | 128.742 | 6.420 | sí | descriptivo_2018_2020 | no |
| sutil | Naive | 2018 | mensual | 90 | 2,726.637 | 3,748.277 | — | 2,360.492 | 6,754.231 | 1 | 11 | 147.713 | 2.861 | no | descriptivo_2018_2020 | no |
| sutil | Naive | 2018 | interanual | 50 | 2,726.637 | 3,748.277 | — | 3,063.420 | 2,614.376 | 9 | 3 | -4.117 | 0.853 | sí | descriptivo_2018_2020 | no |
| sutil | Naive | 2018 | interanual | 60 | 2,726.637 | 3,748.277 | — | 2,535.939 | 2,821.985 | 8 | 4 | 3.497 | 1.113 | sí | descriptivo_2018_2020 | no |
| sutil | Naive | 2018 | interanual | 75 | 2,726.637 | 3,748.277 | — | 2,959.239 | 2,494.035 | 6 | 6 | -8.531 | 0.843 | sí | descriptivo_2018_2020 | no |
| sutil | Naive | 2018 | interanual | 90 | 2,726.637 | 3,748.277 | — | 2,520.317 | 3,139.276 | 4 | 8 | 15.134 | 1.246 | sí | descriptivo_2018_2020 | no |
| sutil | Naive | 2019 | mensual | 50 | 3,562.447 | 4,404.468 | 0.366 | 1,231.506 | 5,227.404 | 7 | 5 | 46.736 | 4.245 | sí | descriptivo_2018_2020 | no |
| sutil | Naive | 2019 | mensual | 60 | 3,562.447 | 4,404.468 | 0.366 | 1,947.214 | 5,823.772 | 5 | 7 | 63.477 | 2.991 | sí | descriptivo_2018_2020 | no |
| sutil | Naive | 2019 | mensual | 75 | 3,562.447 | 4,404.468 | 0.366 | 2,334.856 | 7,245.218 | 3 | 9 | 103.378 | 3.103 | sí | descriptivo_2018_2020 | no |
| sutil | Naive | 2019 | mensual | 90 | 3,562.447 | 4,404.468 | 0.366 | 3,562.447 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| sutil | Naive | 2019 | interanual | 50 | 3,562.447 | 4,404.468 | 0.366 | 3,500.672 | 4,241.973 | 1 | 11 | 19.075 | 1.212 | no | descriptivo_2018_2020 | no |
| sutil | Naive | 2019 | interanual | 60 | 3,562.447 | 4,404.468 | 0.366 | 3,500.672 | 4,241.973 | 1 | 11 | 19.075 | 1.212 | no | descriptivo_2018_2020 | no |
| sutil | Naive | 2019 | interanual | 75 | 3,562.447 | 4,404.468 | 0.366 | 3,562.447 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| sutil | Naive | 2019 | interanual | 90 | 3,562.447 | 4,404.468 | 0.366 | 3,562.447 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| sutil | Naive | 2020 | mensual | 50 | 4,101.784 | 5,222.431 | 0.454 | 1,940.838 | 7,127.110 | 5 | 7 | 73.756 | 3.672 | sí | descriptivo_2018_2020 | no |
| sutil | Naive | 2020 | mensual | 60 | 4,101.784 | 5,222.431 | 0.454 | 1,940.838 | 7,127.110 | 5 | 7 | 73.756 | 3.672 | sí | descriptivo_2018_2020 | no |
| sutil | Naive | 2020 | mensual | 75 | 4,101.784 | 5,222.431 | 0.454 | 2,865.884 | 7,809.485 | 3 | 9 | 90.392 | 2.725 | sí | descriptivo_2018_2020 | no |
| sutil | Naive | 2020 | mensual | 90 | 4,101.784 | 5,222.431 | 0.454 | 3,423.686 | 11,560.866 | 1 | 11 | 181.850 | 3.377 | no | descriptivo_2018_2020 | no |
| sutil | Naive | 2020 | interanual | 50 | 4,101.784 | 5,222.431 | 0.454 | 4,101.784 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| sutil | Naive | 2020 | interanual | 60 | 4,101.784 | 5,222.431 | 0.454 | 4,101.784 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| sutil | Naive | 2020 | interanual | 75 | 4,101.784 | 5,222.431 | 0.454 | 4,101.784 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| sutil | Naive | 2020 | interanual | 90 | 4,101.784 | 5,222.431 | 0.454 | 4,101.784 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| sutil | Naive | 2021 | mensual | 50 | 1,986.098 | 2,736.198 | 0.274 | 1,349.568 | 5,168.748 | 2 | 10 | 160.246 | 3.830 | sí | principal | no |
| sutil | Naive | 2021 | mensual | 60 | 1,986.098 | 2,736.198 | 0.274 | 1,349.568 | 5,168.748 | 2 | 10 | 160.246 | 3.830 | sí | principal | no |
| sutil | Naive | 2021 | mensual | 75 | 1,986.098 | 2,736.198 | 0.274 | 1,986.098 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Naive | 2021 | mensual | 90 | 1,986.098 | 2,736.198 | 0.274 | 1,986.098 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Naive | 2021 | interanual | 50 | 1,986.098 | 2,736.198 | 0.274 | 2,176.962 | 1,413.504 | 3 | 9 | -28.830 | 0.649 | sí | principal | no |
| sutil | Naive | 2021 | interanual | 60 | 1,986.098 | 2,736.198 | 0.274 | 2,358.268 | 125.248 | 2 | 10 | -93.694 | 0.053 | sí | principal | no |
| sutil | Naive | 2021 | interanual | 75 | 1,986.098 | 2,736.198 | 0.274 | 1,986.098 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Naive | 2021 | interanual | 90 | 1,986.098 | 2,736.198 | 0.274 | 1,986.098 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Naive | 2022 | mensual | 50 | 3,762.176 | 4,921.918 | 0.621 | 1,040.422 | 5,706.285 | 7 | 5 | 51.675 | 5.485 | sí | principal | no |
| sutil | Naive | 2022 | mensual | 60 | 3,762.176 | 4,921.918 | 0.621 | 2,035.251 | 7,216.025 | 4 | 8 | 91.805 | 3.546 | sí | principal | no |
| sutil | Naive | 2022 | mensual | 75 | 3,762.176 | 4,921.918 | 0.621 | 2,175.496 | 8,522.216 | 3 | 9 | 126.524 | 3.917 | sí | principal | no |
| sutil | Naive | 2022 | mensual | 90 | 3,762.176 | 4,921.918 | 0.621 | 3,158.533 | 10,402.249 | 1 | 11 | 176.496 | 3.293 | no | principal | no |
| sutil | Naive | 2022 | interanual | 50 | 3,762.176 | 4,921.918 | 0.621 | 3,245.496 | 5,312.214 | 3 | 9 | 41.201 | 1.637 | sí | principal | no |
| sutil | Naive | 2022 | interanual | 60 | 3,762.176 | 4,921.918 | 0.621 | 3,762.176 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Naive | 2022 | interanual | 75 | 3,762.176 | 4,921.918 | 0.621 | 3,762.176 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Naive | 2022 | interanual | 90 | 3,762.176 | 4,921.918 | 0.621 | 3,762.176 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Naive | 2023 | mensual | 50 | 4,589.653 | 4,878.825 | 0.796 | 1,512.240 | 4,869.418 | 11 | 1 | 6.096 | 3.220 | sí | principal | no |
| sutil | Naive | 2023 | mensual | 60 | 4,589.653 | 4,878.825 | 0.796 | 2,098.142 | 5,087.955 | 10 | 2 | 10.857 | 2.425 | sí | principal | no |
| sutil | Naive | 2023 | mensual | 75 | 4,589.653 | 4,878.825 | 0.796 | 3,820.126 | 6,128.708 | 4 | 8 | 33.533 | 1.604 | sí | principal | no |
| sutil | Naive | 2023 | mensual | 90 | 4,589.653 | 4,878.825 | 0.796 | 4,133.552 | 5,957.955 | 3 | 9 | 29.813 | 1.441 | sí | principal | no |
| sutil | Naive | 2023 | interanual | 50 | 4,589.653 | 4,878.825 | 0.796 | 4,704.368 | 4,507.714 | 7 | 5 | -1.785 | 0.958 | sí | principal | no |
| sutil | Naive | 2023 | interanual | 60 | 4,589.653 | 4,878.825 | 0.796 | 4,862.203 | 4,317.102 | 6 | 6 | -5.938 | 0.888 | sí | principal | no |
| sutil | Naive | 2023 | interanual | 75 | 4,589.653 | 4,878.825 | 0.796 | 4,435.770 | 5,359.070 | 2 | 10 | 16.764 | 1.208 | sí | principal | no |
| sutil | Naive | 2023 | interanual | 90 | 4,589.653 | 4,878.825 | 0.796 | 4,589.653 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Naive | 2024 | mensual | 50 | 3,078.133 | 4,269.754 | 0.560 | 1,185.007 | 6,864.385 | 4 | 8 | 123.005 | 5.793 | sí | principal | no |
| sutil | Naive | 2024 | mensual | 60 | 3,078.133 | 4,269.754 | 0.560 | 1,185.007 | 6,864.385 | 4 | 8 | 123.005 | 5.793 | sí | principal | no |
| sutil | Naive | 2024 | mensual | 75 | 3,078.133 | 4,269.754 | 0.560 | 3,078.133 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Naive | 2024 | mensual | 90 | 3,078.133 | 4,269.754 | 0.560 | 3,078.133 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Naive | 2024 | interanual | 50 | 3,078.133 | 4,269.754 | 0.560 | 3,984.319 | 2,625.040 | 8 | 4 | -14.720 | 0.659 | sí | principal | no |
| sutil | Naive | 2024 | interanual | 60 | 3,078.133 | 4,269.754 | 0.560 | 3,984.319 | 2,625.040 | 8 | 4 | -14.720 | 0.659 | sí | principal | no |
| sutil | Naive | 2024 | interanual | 75 | 3,078.133 | 4,269.754 | 0.560 | 3,984.319 | 2,625.040 | 8 | 4 | -14.720 | 0.659 | sí | principal | no |
| sutil | Naive | 2024 | interanual | 90 | 3,078.133 | 4,269.754 | 0.560 | 3,847.728 | 1,538.943 | 4 | 8 | -50.004 | 0.400 | sí | principal | no |
| sutil | Naive | 2025 | mensual | 50 | 4,704.293 | 6,317.411 | 0.811 | 1,877.835 | 8,661.334 | 5 | 7 | 84.116 | 4.612 | sí | principal | no |
| sutil | Naive | 2025 | mensual | 60 | 4,704.293 | 6,317.411 | 0.811 | 1,877.835 | 8,661.334 | 5 | 7 | 84.116 | 4.612 | sí | principal | no |
| sutil | Naive | 2025 | mensual | 75 | 4,704.293 | 6,317.411 | 0.811 | 2,385.671 | 11,660.157 | 3 | 9 | 147.862 | 4.888 | sí | principal | no |
| sutil | Naive | 2025 | mensual | 90 | 4,704.293 | 6,317.411 | 0.811 | 3,255.389 | 11,948.812 | 2 | 10 | 153.998 | 3.670 | sí | principal | no |
| sutil | Naive | 2025 | interanual | 50 | 4,704.293 | 6,317.411 | 0.811 | 4,648.983 | 4,814.913 | 4 | 8 | 2.351 | 1.036 | sí | principal | no |
| sutil | Naive | 2025 | interanual | 60 | 4,704.293 | 6,317.411 | 0.811 | 4,288.027 | 6,785.623 | 2 | 10 | 44.243 | 1.582 | sí | principal | no |
| sutil | Naive | 2025 | interanual | 75 | 4,704.293 | 6,317.411 | 0.811 | 4,704.293 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Naive | 2025 | interanual | 90 | 4,704.293 | 6,317.411 | 0.811 | 4,704.293 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Seasonal Naive | 2018 | mensual | 50 | 8,316.511 | 8,867.631 | — | 8,674.492 | 7,600.548 | 4 | 8 | -8.609 | 0.876 | sí | descriptivo_2018_2020 | no |
| sutil | Seasonal Naive | 2018 | mensual | 60 | 8,316.511 | 8,867.631 | — | 8,674.492 | 7,600.548 | 4 | 8 | -8.609 | 0.876 | sí | descriptivo_2018_2020 | no |
| sutil | Seasonal Naive | 2018 | mensual | 75 | 8,316.511 | 8,867.631 | — | 8,674.492 | 7,600.548 | 4 | 8 | -8.609 | 0.876 | sí | descriptivo_2018_2020 | no |
| sutil | Seasonal Naive | 2018 | mensual | 90 | 8,316.511 | 8,867.631 | — | 8,858.747 | 2,351.904 | 1 | 11 | -71.720 | 0.265 | no | descriptivo_2018_2020 | no |
| sutil | Seasonal Naive | 2018 | interanual | 50 | 8,316.511 | 8,867.631 | — | 4,243.924 | 9,674.039 | 9 | 3 | 16.323 | 2.280 | sí | descriptivo_2018_2020 | no |
| sutil | Seasonal Naive | 2018 | interanual | 60 | 8,316.511 | 8,867.631 | — | 5,043.672 | 9,952.930 | 8 | 4 | 19.677 | 1.973 | sí | descriptivo_2018_2020 | no |
| sutil | Seasonal Naive | 2018 | interanual | 75 | 8,316.511 | 8,867.631 | — | 6,867.526 | 9,765.495 | 6 | 6 | 17.423 | 1.422 | sí | descriptivo_2018_2020 | no |
| sutil | Seasonal Naive | 2018 | interanual | 90 | 8,316.511 | 8,867.631 | — | 7,817.538 | 9,314.455 | 4 | 8 | 12.000 | 1.191 | sí | descriptivo_2018_2020 | no |
| sutil | Seasonal Naive | 2019 | mensual | 50 | 3,727.871 | 4,381.476 | 0.383 | 4,560.946 | 3,132.818 | 7 | 5 | -15.962 | 0.687 | sí | descriptivo_2018_2020 | no |
| sutil | Seasonal Naive | 2019 | mensual | 60 | 3,727.871 | 4,381.476 | 0.383 | 3,764.531 | 3,676.548 | 5 | 7 | -1.377 | 0.977 | sí | descriptivo_2018_2020 | no |
| sutil | Seasonal Naive | 2019 | mensual | 75 | 3,727.871 | 4,381.476 | 0.383 | 4,220.644 | 2,249.553 | 3 | 9 | -39.656 | 0.533 | sí | descriptivo_2018_2020 | no |
| sutil | Seasonal Naive | 2019 | mensual | 90 | 3,727.871 | 4,381.476 | 0.383 | 3,727.871 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| sutil | Seasonal Naive | 2019 | interanual | 50 | 3,727.871 | 4,381.476 | 0.383 | 3,271.369 | 8,749.392 | 1 | 11 | 134.702 | 2.675 | no | descriptivo_2018_2020 | no |
| sutil | Seasonal Naive | 2019 | interanual | 60 | 3,727.871 | 4,381.476 | 0.383 | 3,271.369 | 8,749.392 | 1 | 11 | 134.702 | 2.675 | no | descriptivo_2018_2020 | no |
| sutil | Seasonal Naive | 2019 | interanual | 75 | 3,727.871 | 4,381.476 | 0.383 | 3,727.871 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| sutil | Seasonal Naive | 2019 | interanual | 90 | 3,727.871 | 4,381.476 | 0.383 | 3,727.871 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| sutil | Seasonal Naive | 2020 | mensual | 50 | 2,442.620 | 3,182.750 | 0.271 | 1,945.617 | 3,138.424 | 5 | 7 | 28.486 | 1.613 | sí | descriptivo_2018_2020 | no |
| sutil | Seasonal Naive | 2020 | mensual | 60 | 2,442.620 | 3,182.750 | 0.271 | 1,945.617 | 3,138.424 | 5 | 7 | 28.486 | 1.613 | sí | descriptivo_2018_2020 | no |
| sutil | Seasonal Naive | 2020 | mensual | 75 | 2,442.620 | 3,182.750 | 0.271 | 1,751.426 | 4,516.200 | 3 | 9 | 84.892 | 2.579 | sí | descriptivo_2018_2020 | no |
| sutil | Seasonal Naive | 2020 | mensual | 90 | 2,442.620 | 3,182.750 | 0.271 | 2,416.943 | 2,725.067 | 1 | 11 | 11.563 | 1.127 | no | descriptivo_2018_2020 | no |
| sutil | Seasonal Naive | 2020 | interanual | 50 | 2,442.620 | 3,182.750 | 0.271 | 2,442.620 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| sutil | Seasonal Naive | 2020 | interanual | 60 | 2,442.620 | 3,182.750 | 0.271 | 2,442.620 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| sutil | Seasonal Naive | 2020 | interanual | 75 | 2,442.620 | 3,182.750 | 0.271 | 2,442.620 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| sutil | Seasonal Naive | 2020 | interanual | 90 | 2,442.620 | 3,182.750 | 0.271 | 2,442.620 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| sutil | Seasonal Naive | 2021 | mensual | 50 | 4,590.342 | 5,061.150 | 0.632 | 4,507.730 | 5,003.400 | 2 | 10 | 8.998 | 1.110 | sí | principal | no |
| sutil | Seasonal Naive | 2021 | mensual | 60 | 4,590.342 | 5,061.150 | 0.632 | 4,507.730 | 5,003.400 | 2 | 10 | 8.998 | 1.110 | sí | principal | no |
| sutil | Seasonal Naive | 2021 | mensual | 75 | 4,590.342 | 5,061.150 | 0.632 | 4,590.342 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Seasonal Naive | 2021 | mensual | 90 | 4,590.342 | 5,061.150 | 0.632 | 4,590.342 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Seasonal Naive | 2021 | interanual | 50 | 4,590.342 | 5,061.150 | 0.632 | 3,704.778 | 7,247.034 | 3 | 9 | 57.876 | 1.956 | sí | principal | no |
| sutil | Seasonal Naive | 2021 | interanual | 60 | 4,590.342 | 5,061.150 | 0.632 | 3,949.026 | 7,796.924 | 2 | 10 | 69.855 | 1.974 | sí | principal | no |
| sutil | Seasonal Naive | 2021 | interanual | 75 | 4,590.342 | 5,061.150 | 0.632 | 4,590.342 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Seasonal Naive | 2021 | interanual | 90 | 4,590.342 | 5,061.150 | 0.632 | 4,590.342 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Seasonal Naive | 2022 | mensual | 50 | 4,136.381 | 5,143.520 | 0.683 | 4,394.199 | 3,952.224 | 7 | 5 | -4.452 | 0.899 | sí | principal | no |
| sutil | Seasonal Naive | 2022 | mensual | 60 | 4,136.381 | 5,143.520 | 0.683 | 4,154.486 | 4,100.170 | 4 | 8 | -0.875 | 0.987 | sí | principal | no |
| sutil | Seasonal Naive | 2022 | mensual | 75 | 4,136.381 | 5,143.520 | 0.683 | 4,024.620 | 4,471.663 | 3 | 9 | 8.106 | 1.111 | sí | principal | no |
| sutil | Seasonal Naive | 2022 | mensual | 90 | 4,136.381 | 5,143.520 | 0.683 | 3,676.805 | 9,191.709 | 1 | 11 | 122.216 | 2.500 | no | principal | no |
| sutil | Seasonal Naive | 2022 | interanual | 50 | 4,136.381 | 5,143.520 | 0.683 | 2,841.555 | 8,020.858 | 3 | 9 | 93.910 | 2.823 | sí | principal | no |
| sutil | Seasonal Naive | 2022 | interanual | 60 | 4,136.381 | 5,143.520 | 0.683 | 4,136.381 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Seasonal Naive | 2022 | interanual | 75 | 4,136.381 | 5,143.520 | 0.683 | 4,136.381 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Seasonal Naive | 2022 | interanual | 90 | 4,136.381 | 5,143.520 | 0.683 | 4,136.381 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Seasonal Naive | 2023 | mensual | 50 | 7,638.063 | 8,767.712 | 1.325 | 7,932.778 | 7,611.270 | 11 | 1 | -0.351 | 0.959 | sí | principal | no |
| sutil | Seasonal Naive | 2023 | mensual | 60 | 7,638.063 | 8,767.712 | 1.325 | 7,461.181 | 7,673.439 | 10 | 2 | 0.463 | 1.028 | sí | principal | no |
| sutil | Seasonal Naive | 2023 | mensual | 75 | 7,638.063 | 8,767.712 | 1.325 | 8,389.538 | 6,135.113 | 4 | 8 | -19.677 | 0.731 | sí | principal | no |
| sutil | Seasonal Naive | 2023 | mensual | 90 | 7,638.063 | 8,767.712 | 1.325 | 7,540.478 | 7,930.817 | 3 | 9 | 3.833 | 1.052 | sí | principal | no |
| sutil | Seasonal Naive | 2023 | interanual | 50 | 7,638.063 | 8,767.712 | 1.325 | 3,570.890 | 10,543.186 | 7 | 5 | 38.035 | 2.953 | sí | principal | no |
| sutil | Seasonal Naive | 2023 | interanual | 60 | 7,638.063 | 8,767.712 | 1.325 | 4,776.341 | 10,499.784 | 6 | 6 | 37.467 | 2.198 | sí | principal | no |
| sutil | Seasonal Naive | 2023 | interanual | 75 | 7,638.063 | 8,767.712 | 1.325 | 6,799.539 | 11,830.680 | 2 | 10 | 54.891 | 1.740 | sí | principal | no |
| sutil | Seasonal Naive | 2023 | interanual | 90 | 7,638.063 | 8,767.712 | 1.325 | 7,638.063 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Seasonal Naive | 2024 | mensual | 50 | 9,849.536 | 11,152.232 | 1.793 | 10,683.904 | 8,180.801 | 4 | 8 | -16.942 | 0.766 | sí | principal | no |
| sutil | Seasonal Naive | 2024 | mensual | 60 | 9,849.536 | 11,152.232 | 1.793 | 10,683.904 | 8,180.801 | 4 | 8 | -16.942 | 0.766 | sí | principal | no |
| sutil | Seasonal Naive | 2024 | mensual | 75 | 9,849.536 | 11,152.232 | 1.793 | 9,849.536 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Seasonal Naive | 2024 | mensual | 90 | 9,849.536 | 11,152.232 | 1.793 | 9,849.536 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Seasonal Naive | 2024 | interanual | 50 | 9,849.536 | 11,152.232 | 1.793 | 4,193.780 | 12,677.415 | 8 | 4 | 28.711 | 3.023 | sí | principal | no |
| sutil | Seasonal Naive | 2024 | interanual | 60 | 9,849.536 | 11,152.232 | 1.793 | 4,193.780 | 12,677.415 | 8 | 4 | 28.711 | 3.023 | sí | principal | no |
| sutil | Seasonal Naive | 2024 | interanual | 75 | 9,849.536 | 11,152.232 | 1.793 | 4,193.780 | 12,677.415 | 8 | 4 | 28.711 | 3.023 | sí | principal | no |
| sutil | Seasonal Naive | 2024 | interanual | 90 | 9,849.536 | 11,152.232 | 1.793 | 7,144.929 | 15,258.750 | 4 | 8 | 54.918 | 2.136 | sí | principal | no |
| sutil | Seasonal Naive | 2025 | mensual | 50 | 4,160.108 | 4,926.647 | 0.717 | 3,970.264 | 4,425.889 | 5 | 7 | 6.389 | 1.115 | sí | principal | no |
| sutil | Seasonal Naive | 2025 | mensual | 60 | 4,160.108 | 4,926.647 | 0.717 | 3,970.264 | 4,425.889 | 5 | 7 | 6.389 | 1.115 | sí | principal | no |
| sutil | Seasonal Naive | 2025 | mensual | 75 | 4,160.108 | 4,926.647 | 0.717 | 4,170.249 | 4,129.686 | 3 | 9 | -0.731 | 0.990 | sí | principal | no |
| sutil | Seasonal Naive | 2025 | mensual | 90 | 4,160.108 | 4,926.647 | 0.717 | 3,905.068 | 5,435.307 | 2 | 10 | 30.653 | 1.392 | sí | principal | no |
| sutil | Seasonal Naive | 2025 | interanual | 50 | 4,160.108 | 4,926.647 | 0.717 | 2,440.135 | 7,600.055 | 4 | 8 | 82.689 | 3.115 | sí | principal | no |
| sutil | Seasonal Naive | 2025 | interanual | 60 | 4,160.108 | 4,926.647 | 0.717 | 3,259.794 | 8,661.675 | 2 | 10 | 108.208 | 2.657 | sí | principal | no |
| sutil | Seasonal Naive | 2025 | interanual | 75 | 4,160.108 | 4,926.647 | 0.717 | 4,160.108 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Seasonal Naive | 2025 | interanual | 90 | 4,160.108 | 4,926.647 | 0.717 | 4,160.108 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Chronos | 2018 | mensual | 50 | 1,973.398 | 2,889.703 | — | 566.765 | 4,786.665 | 4 | 8 | 142.560 | 8.446 | sí | descriptivo_2018_2020 | no |
| sutil | Chronos | 2018 | mensual | 60 | 1,973.398 | 2,889.703 | — | 566.765 | 4,786.665 | 4 | 8 | 142.560 | 8.446 | sí | descriptivo_2018_2020 | no |
| sutil | Chronos | 2018 | mensual | 75 | 1,973.398 | 2,889.703 | — | 566.765 | 4,786.665 | 4 | 8 | 142.560 | 8.446 | sí | descriptivo_2018_2020 | no |
| sutil | Chronos | 2018 | mensual | 90 | 1,973.398 | 2,889.703 | — | 1,640.362 | 5,636.792 | 1 | 11 | 185.639 | 3.436 | no | descriptivo_2018_2020 | no |
| sutil | Chronos | 2018 | interanual | 50 | 1,973.398 | 2,889.703 | — | 2,253.095 | 1,880.166 | 9 | 3 | -4.724 | 0.834 | sí | descriptivo_2018_2020 | no |
| sutil | Chronos | 2018 | interanual | 60 | 1,973.398 | 2,889.703 | — | 1,728.325 | 2,095.935 | 8 | 4 | 6.209 | 1.213 | sí | descriptivo_2018_2020 | no |
| sutil | Chronos | 2018 | interanual | 75 | 1,973.398 | 2,889.703 | — | 1,746.651 | 2,200.146 | 6 | 6 | 11.490 | 1.260 | sí | descriptivo_2018_2020 | no |
| sutil | Chronos | 2018 | interanual | 90 | 1,973.398 | 2,889.703 | — | 1,504.989 | 2,910.216 | 4 | 8 | 47.472 | 1.934 | sí | descriptivo_2018_2020 | no |
| sutil | Chronos | 2019 | mensual | 50 | 2,701.570 | 3,423.363 | 0.277 | 2,595.359 | 2,777.436 | 7 | 5 | 2.808 | 1.070 | sí | descriptivo_2018_2020 | no |
| sutil | Chronos | 2019 | mensual | 60 | 2,701.570 | 3,423.363 | 0.277 | 2,196.557 | 3,408.589 | 5 | 7 | 26.171 | 1.552 | sí | descriptivo_2018_2020 | no |
| sutil | Chronos | 2019 | mensual | 75 | 2,701.570 | 3,423.363 | 0.277 | 2,036.359 | 4,697.205 | 3 | 9 | 73.869 | 2.307 | sí | descriptivo_2018_2020 | no |
| sutil | Chronos | 2019 | mensual | 90 | 2,701.570 | 3,423.363 | 0.277 | 2,701.570 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| sutil | Chronos | 2019 | interanual | 50 | 2,701.570 | 3,423.363 | 0.277 | 2,946.332 | 9.195 | 1 | 11 | -99.660 | 0.003 | no | descriptivo_2018_2020 | no |
| sutil | Chronos | 2019 | interanual | 60 | 2,701.570 | 3,423.363 | 0.277 | 2,946.332 | 9.195 | 1 | 11 | -99.660 | 0.003 | no | descriptivo_2018_2020 | no |
| sutil | Chronos | 2019 | interanual | 75 | 2,701.570 | 3,423.363 | 0.277 | 2,701.570 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| sutil | Chronos | 2019 | interanual | 90 | 2,701.570 | 3,423.363 | 0.277 | 2,701.570 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| sutil | Chronos | 2020 | mensual | 50 | 2,930.994 | 3,733.962 | 0.325 | 1,939.610 | 4,318.931 | 5 | 7 | 47.354 | 2.227 | sí | descriptivo_2018_2020 | no |
| sutil | Chronos | 2020 | mensual | 60 | 2,930.994 | 3,733.962 | 0.325 | 1,939.610 | 4,318.931 | 5 | 7 | 47.354 | 2.227 | sí | descriptivo_2018_2020 | no |
| sutil | Chronos | 2020 | mensual | 75 | 2,930.994 | 3,733.962 | 0.325 | 1,958.622 | 5,848.109 | 3 | 9 | 99.526 | 2.986 | sí | descriptivo_2018_2020 | no |
| sutil | Chronos | 2020 | mensual | 90 | 2,930.994 | 3,733.962 | 0.325 | 2,510.572 | 7,555.633 | 1 | 11 | 157.784 | 3.010 | no | descriptivo_2018_2020 | no |
| sutil | Chronos | 2020 | interanual | 50 | 2,930.994 | 3,733.962 | 0.325 | 2,930.994 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| sutil | Chronos | 2020 | interanual | 60 | 2,930.994 | 3,733.962 | 0.325 | 2,930.994 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| sutil | Chronos | 2020 | interanual | 75 | 2,930.994 | 3,733.962 | 0.325 | 2,930.994 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| sutil | Chronos | 2020 | interanual | 90 | 2,930.994 | 3,733.962 | 0.325 | 2,930.994 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| sutil | Chronos | 2021 | mensual | 50 | 2,540.839 | 2,839.936 | 0.350 | 2,356.063 | 3,464.719 | 2 | 10 | 36.361 | 1.471 | sí | principal | no |
| sutil | Chronos | 2021 | mensual | 60 | 2,540.839 | 2,839.936 | 0.350 | 2,356.063 | 3,464.719 | 2 | 10 | 36.361 | 1.471 | sí | principal | no |
| sutil | Chronos | 2021 | mensual | 75 | 2,540.839 | 2,839.936 | 0.350 | 2,540.839 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Chronos | 2021 | mensual | 90 | 2,540.839 | 2,839.936 | 0.350 | 2,540.839 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Chronos | 2021 | interanual | 50 | 2,540.839 | 2,839.936 | 0.350 | 2,089.798 | 3,893.962 | 3 | 9 | 53.255 | 1.863 | sí | principal | no |
| sutil | Chronos | 2021 | interanual | 60 | 2,540.839 | 2,839.936 | 0.350 | 2,306.701 | 3,711.533 | 2 | 10 | 46.075 | 1.609 | sí | principal | no |
| sutil | Chronos | 2021 | interanual | 75 | 2,540.839 | 2,839.936 | 0.350 | 2,540.839 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Chronos | 2021 | interanual | 90 | 2,540.839 | 2,839.936 | 0.350 | 2,540.839 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Chronos | 2022 | mensual | 50 | 2,205.053 | 3,198.818 | 0.364 | 689.903 | 3,287.303 | 7 | 5 | 49.080 | 4.765 | sí | principal | no |
| sutil | Chronos | 2022 | mensual | 60 | 2,205.053 | 3,198.818 | 0.364 | 1,443.336 | 3,728.489 | 4 | 8 | 69.088 | 2.583 | sí | principal | no |
| sutil | Chronos | 2022 | mensual | 75 | 2,205.053 | 3,198.818 | 0.364 | 1,322.684 | 4,852.160 | 3 | 9 | 120.047 | 3.668 | sí | principal | no |
| sutil | Chronos | 2022 | mensual | 90 | 2,205.053 | 3,198.818 | 0.364 | 1,703.172 | 7,725.752 | 1 | 11 | 250.366 | 4.536 | no | principal | no |
| sutil | Chronos | 2022 | interanual | 50 | 2,205.053 | 3,198.818 | 0.364 | 1,385.067 | 4,665.013 | 3 | 9 | 111.560 | 3.368 | sí | principal | no |
| sutil | Chronos | 2022 | interanual | 60 | 2,205.053 | 3,198.818 | 0.364 | 2,205.053 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Chronos | 2022 | interanual | 75 | 2,205.053 | 3,198.818 | 0.364 | 2,205.053 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Chronos | 2022 | interanual | 90 | 2,205.053 | 3,198.818 | 0.364 | 2,205.053 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Chronos | 2023 | mensual | 50 | 3,157.138 | 3,802.267 | 0.548 | 1,621.799 | 3,296.714 | 11 | 1 | 4.421 | 2.033 | sí | principal | no |
| sutil | Chronos | 2023 | mensual | 60 | 3,157.138 | 3,802.267 | 0.548 | 901.685 | 3,608.229 | 10 | 2 | 14.288 | 4.002 | sí | principal | no |
| sutil | Chronos | 2023 | mensual | 75 | 3,157.138 | 3,802.267 | 0.548 | 3,008.614 | 3,454.185 | 4 | 8 | 9.409 | 1.148 | sí | principal | no |
| sutil | Chronos | 2023 | mensual | 90 | 3,157.138 | 3,802.267 | 0.548 | 2,950.585 | 3,776.796 | 3 | 9 | 19.627 | 1.280 | sí | principal | no |
| sutil | Chronos | 2023 | interanual | 50 | 3,157.138 | 3,802.267 | 0.548 | 2,192.402 | 3,846.235 | 7 | 5 | 21.827 | 1.754 | sí | principal | no |
| sutil | Chronos | 2023 | interanual | 60 | 3,157.138 | 3,802.267 | 0.548 | 2,989.151 | 3,325.125 | 6 | 6 | 5.321 | 1.112 | sí | principal | no |
| sutil | Chronos | 2023 | interanual | 75 | 3,157.138 | 3,802.267 | 0.548 | 2,966.722 | 4,109.217 | 2 | 10 | 30.156 | 1.385 | sí | principal | no |
| sutil | Chronos | 2023 | interanual | 90 | 3,157.138 | 3,802.267 | 0.548 | 3,157.138 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Chronos | 2024 | mensual | 50 | 2,023.404 | 2,456.962 | 0.368 | 1,547.468 | 2,975.276 | 4 | 8 | 47.043 | 1.923 | sí | principal | no |
| sutil | Chronos | 2024 | mensual | 60 | 2,023.404 | 2,456.962 | 0.368 | 1,547.468 | 2,975.276 | 4 | 8 | 47.043 | 1.923 | sí | principal | no |
| sutil | Chronos | 2024 | mensual | 75 | 2,023.404 | 2,456.962 | 0.368 | 2,023.404 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Chronos | 2024 | mensual | 90 | 2,023.404 | 2,456.962 | 0.368 | 2,023.404 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Chronos | 2024 | interanual | 50 | 2,023.404 | 2,456.962 | 0.368 | 3,464.538 | 1,302.837 | 8 | 4 | -35.612 | 0.376 | sí | principal | no |
| sutil | Chronos | 2024 | interanual | 60 | 2,023.404 | 2,456.962 | 0.368 | 3,464.538 | 1,302.837 | 8 | 4 | -35.612 | 0.376 | sí | principal | no |
| sutil | Chronos | 2024 | interanual | 75 | 2,023.404 | 2,456.962 | 0.368 | 3,464.538 | 1,302.837 | 8 | 4 | -35.612 | 0.376 | sí | principal | no |
| sutil | Chronos | 2024 | interanual | 90 | 2,023.404 | 2,456.962 | 0.368 | 2,477.004 | 1,116.204 | 4 | 8 | -44.835 | 0.451 | sí | principal | no |
| sutil | Chronos | 2025 | mensual | 50 | 3,316.299 | 3,991.088 | 0.572 | 2,182.750 | 4,903.266 | 5 | 7 | 47.854 | 2.246 | sí | principal | no |
| sutil | Chronos | 2025 | mensual | 60 | 3,316.299 | 3,991.088 | 0.572 | 2,182.750 | 4,903.266 | 5 | 7 | 47.854 | 2.246 | sí | principal | no |
| sutil | Chronos | 2025 | mensual | 75 | 3,316.299 | 3,991.088 | 0.572 | 2,259.287 | 6,487.334 | 3 | 9 | 95.620 | 2.871 | sí | principal | no |
| sutil | Chronos | 2025 | mensual | 90 | 3,316.299 | 3,991.088 | 0.572 | 2,623.357 | 6,781.005 | 2 | 10 | 104.475 | 2.585 | sí | principal | no |
| sutil | Chronos | 2025 | interanual | 50 | 3,316.299 | 3,991.088 | 0.572 | 2,878.995 | 4,190.906 | 4 | 8 | 26.373 | 1.456 | sí | principal | no |
| sutil | Chronos | 2025 | interanual | 60 | 3,316.299 | 3,991.088 | 0.572 | 2,880.443 | 5,495.577 | 2 | 10 | 65.714 | 1.908 | sí | principal | no |
| sutil | Chronos | 2025 | interanual | 75 | 3,316.299 | 3,991.088 | 0.572 | 3,316.299 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Chronos | 2025 | interanual | 90 | 3,316.299 | 3,991.088 | 0.572 | 3,316.299 | — | 0 | 12 | — | — | no | principal | no |
| sutil | SARIMA | 2021 | mensual | 50 | 3,207.917 | 4,152.987 | 0.442 | 3,509.915 | 1,697.927 | 2 | 10 | -47.071 | 0.484 | sí | principal | no |
| sutil | SARIMA | 2021 | mensual | 60 | 3,207.917 | 4,152.987 | 0.442 | 3,509.915 | 1,697.927 | 2 | 10 | -47.071 | 0.484 | sí | principal | no |
| sutil | SARIMA | 2021 | mensual | 75 | 3,207.917 | 4,152.987 | 0.442 | 3,207.917 | — | 0 | 12 | — | — | no | principal | no |
| sutil | SARIMA | 2021 | mensual | 90 | 3,207.917 | 4,152.987 | 0.442 | 3,207.917 | — | 0 | 12 | — | — | no | principal | no |
| sutil | SARIMA | 2021 | interanual | 50 | 3,207.917 | 4,152.987 | 0.442 | 2,838.638 | 4,315.755 | 3 | 9 | 34.534 | 1.520 | sí | principal | no |
| sutil | SARIMA | 2021 | interanual | 60 | 3,207.917 | 4,152.987 | 0.442 | 2,818.840 | 5,153.301 | 2 | 10 | 60.643 | 1.828 | sí | principal | no |
| sutil | SARIMA | 2021 | interanual | 75 | 3,207.917 | 4,152.987 | 0.442 | 3,207.917 | — | 0 | 12 | — | — | no | principal | no |
| sutil | SARIMA | 2021 | interanual | 90 | 3,207.917 | 4,152.987 | 0.442 | 3,207.917 | — | 0 | 12 | — | — | no | principal | no |
| sutil | SARIMA | 2022 | mensual | 50 | 3,060.829 | 3,962.005 | 0.505 | 1,871.371 | 3,910.443 | 7 | 5 | 27.758 | 2.090 | sí | principal | no |
| sutil | SARIMA | 2022 | mensual | 60 | 3,060.829 | 3,962.005 | 0.505 | 2,634.945 | 3,912.597 | 4 | 8 | 27.828 | 1.485 | sí | principal | no |
| sutil | SARIMA | 2022 | mensual | 75 | 3,060.829 | 3,962.005 | 0.505 | 2,779.411 | 3,905.085 | 3 | 9 | 27.583 | 1.405 | sí | principal | no |
| sutil | SARIMA | 2022 | mensual | 90 | 3,060.829 | 3,962.005 | 0.505 | 2,499.398 | 9,236.577 | 1 | 11 | 201.767 | 3.696 | no | principal | no |
| sutil | SARIMA | 2022 | interanual | 50 | 3,060.829 | 3,962.005 | 0.505 | 1,865.900 | 6,645.617 | 3 | 9 | 117.118 | 3.562 | sí | principal | no |
| sutil | SARIMA | 2022 | interanual | 60 | 3,060.829 | 3,962.005 | 0.505 | 3,060.829 | — | 0 | 12 | — | — | no | principal | no |
| sutil | SARIMA | 2022 | interanual | 75 | 3,060.829 | 3,962.005 | 0.505 | 3,060.829 | — | 0 | 12 | — | — | no | principal | no |
| sutil | SARIMA | 2022 | interanual | 90 | 3,060.829 | 3,962.005 | 0.505 | 3,060.829 | — | 0 | 12 | — | — | no | principal | no |
| sutil | SARIMA | 2023 | mensual | 50 | 3,692.521 | 4,184.492 | 0.641 | 4,651.587 | 3,605.333 | 11 | 1 | -2.361 | 0.775 | sí | principal | no |
| sutil | SARIMA | 2023 | mensual | 60 | 3,692.521 | 4,184.492 | 0.641 | 5,120.914 | 3,406.843 | 10 | 2 | -7.737 | 0.665 | sí | principal | no |
| sutil | SARIMA | 2023 | mensual | 75 | 3,692.521 | 4,184.492 | 0.641 | 3,523.942 | 4,029.680 | 4 | 8 | 9.131 | 1.144 | sí | principal | no |
| sutil | SARIMA | 2023 | mensual | 90 | 3,692.521 | 4,184.492 | 0.641 | 3,259.642 | 4,991.160 | 3 | 9 | 35.169 | 1.531 | sí | principal | no |
| sutil | SARIMA | 2023 | interanual | 50 | 3,692.521 | 4,184.492 | 0.641 | 3,203.611 | 4,041.743 | 7 | 5 | 9.458 | 1.262 | sí | principal | no |
| sutil | SARIMA | 2023 | interanual | 60 | 3,692.521 | 4,184.492 | 0.641 | 3,866.634 | 3,518.408 | 6 | 6 | -4.715 | 0.910 | sí | principal | no |
| sutil | SARIMA | 2023 | interanual | 75 | 3,692.521 | 4,184.492 | 0.641 | 3,410.818 | 5,101.035 | 2 | 10 | 38.145 | 1.496 | sí | principal | no |
| sutil | SARIMA | 2023 | interanual | 90 | 3,692.521 | 4,184.492 | 0.641 | 3,692.521 | — | 0 | 12 | — | — | no | principal | no |
| sutil | SARIMA | 2024 | mensual | 50 | 2,857.652 | 3,250.892 | 0.520 | 3,235.777 | 2,101.402 | 4 | 8 | -26.464 | 0.649 | sí | principal | no |
| sutil | SARIMA | 2024 | mensual | 60 | 2,857.652 | 3,250.892 | 0.520 | 3,235.777 | 2,101.402 | 4 | 8 | -26.464 | 0.649 | sí | principal | no |
| sutil | SARIMA | 2024 | mensual | 75 | 2,857.652 | 3,250.892 | 0.520 | 2,857.652 | — | 0 | 12 | — | — | no | principal | no |
| sutil | SARIMA | 2024 | mensual | 90 | 2,857.652 | 3,250.892 | 0.520 | 2,857.652 | — | 0 | 12 | — | — | no | principal | no |
| sutil | SARIMA | 2024 | interanual | 50 | 2,857.652 | 3,250.892 | 0.520 | 3,041.672 | 2,765.642 | 8 | 4 | -3.220 | 0.909 | sí | principal | no |
| sutil | SARIMA | 2024 | interanual | 60 | 2,857.652 | 3,250.892 | 0.520 | 3,041.672 | 2,765.642 | 8 | 4 | -3.220 | 0.909 | sí | principal | no |
| sutil | SARIMA | 2024 | interanual | 75 | 2,857.652 | 3,250.892 | 0.520 | 3,041.672 | 2,765.642 | 8 | 4 | -3.220 | 0.909 | sí | principal | no |
| sutil | SARIMA | 2024 | interanual | 90 | 2,857.652 | 3,250.892 | 0.520 | 2,423.760 | 3,725.435 | 4 | 8 | 30.367 | 1.537 | sí | principal | no |
| sutil | SARIMA | 2025 | mensual | 50 | 3,985.016 | 4,894.896 | 0.687 | 3,030.891 | 5,320.792 | 5 | 7 | 33.520 | 1.756 | sí | principal | no |
| sutil | SARIMA | 2025 | mensual | 60 | 3,985.016 | 4,894.896 | 0.687 | 3,030.891 | 5,320.792 | 5 | 7 | 33.520 | 1.756 | sí | principal | no |
| sutil | SARIMA | 2025 | mensual | 75 | 3,985.016 | 4,894.896 | 0.687 | 2,705.221 | 7,824.403 | 3 | 9 | 96.346 | 2.892 | sí | principal | no |
| sutil | SARIMA | 2025 | mensual | 90 | 3,985.016 | 4,894.896 | 0.687 | 3,144.400 | 8,188.099 | 2 | 10 | 105.472 | 2.604 | sí | principal | no |
| sutil | SARIMA | 2025 | interanual | 50 | 3,985.016 | 4,894.896 | 0.687 | 4,072.025 | 3,810.999 | 4 | 8 | -4.367 | 0.936 | sí | principal | no |
| sutil | SARIMA | 2025 | interanual | 60 | 3,985.016 | 4,894.896 | 0.687 | 3,537.480 | 6,222.697 | 2 | 10 | 56.152 | 1.759 | sí | principal | no |
| sutil | SARIMA | 2025 | interanual | 75 | 3,985.016 | 4,894.896 | 0.687 | 3,985.016 | — | 0 | 12 | — | — | no | principal | no |
| sutil | SARIMA | 2025 | interanual | 90 | 3,985.016 | 4,894.896 | 0.687 | 3,985.016 | — | 0 | 12 | — | — | no | principal | no |
| sutil | SARIMA-sel | 2021 | mensual | 50 | 2,304.409 | 3,302.533 | 0.317 | 2,512.484 | 1,264.037 | 2 | 10 | -45.147 | 0.503 | sí | principal | no |
| sutil | SARIMA-sel | 2021 | mensual | 60 | 2,304.409 | 3,302.533 | 0.317 | 2,512.484 | 1,264.037 | 2 | 10 | -45.147 | 0.503 | sí | principal | no |
| sutil | SARIMA-sel | 2021 | mensual | 75 | 2,304.409 | 3,302.533 | 0.317 | 2,304.409 | — | 0 | 12 | — | — | no | principal | no |
| sutil | SARIMA-sel | 2021 | mensual | 90 | 2,304.409 | 3,302.533 | 0.317 | 2,304.409 | — | 0 | 12 | — | — | no | principal | no |
| sutil | SARIMA-sel | 2021 | interanual | 50 | 2,304.409 | 3,302.533 | 0.317 | 1,631.110 | 4,324.306 | 3 | 9 | 87.654 | 2.651 | sí | principal | no |
| sutil | SARIMA-sel | 2021 | interanual | 60 | 2,304.409 | 3,302.533 | 0.317 | 1,701.046 | 5,321.225 | 2 | 10 | 130.915 | 3.128 | sí | principal | no |
| sutil | SARIMA-sel | 2021 | interanual | 75 | 2,304.409 | 3,302.533 | 0.317 | 2,304.409 | — | 0 | 12 | — | — | no | principal | no |
| sutil | SARIMA-sel | 2021 | interanual | 90 | 2,304.409 | 3,302.533 | 0.317 | 2,304.409 | — | 0 | 12 | — | — | no | principal | no |
| sutil | SARIMA-sel | 2022 | mensual | 50 | 2,609.490 | 3,645.130 | 0.431 | 1,616.189 | 3,318.990 | 7 | 5 | 27.189 | 2.054 | sí | principal | no |
| sutil | SARIMA-sel | 2022 | mensual | 60 | 2,609.490 | 3,645.130 | 0.431 | 2,014.626 | 3,799.217 | 4 | 8 | 45.592 | 1.886 | sí | principal | no |
| sutil | SARIMA-sel | 2022 | mensual | 75 | 2,609.490 | 3,645.130 | 0.431 | 2,077.106 | 4,206.642 | 3 | 9 | 61.206 | 2.025 | sí | principal | no |
| sutil | SARIMA-sel | 2022 | mensual | 90 | 2,609.490 | 3,645.130 | 0.431 | 1,934.592 | 10,033.359 | 1 | 11 | 284.495 | 5.186 | no | principal | no |
| sutil | SARIMA-sel | 2022 | interanual | 50 | 2,609.490 | 3,645.130 | 0.431 | 1,841.074 | 4,914.736 | 3 | 9 | 88.341 | 2.669 | sí | principal | no |
| sutil | SARIMA-sel | 2022 | interanual | 60 | 2,609.490 | 3,645.130 | 0.431 | 2,609.490 | — | 0 | 12 | — | — | no | principal | no |
| sutil | SARIMA-sel | 2022 | interanual | 75 | 2,609.490 | 3,645.130 | 0.431 | 2,609.490 | — | 0 | 12 | — | — | no | principal | no |
| sutil | SARIMA-sel | 2022 | interanual | 90 | 2,609.490 | 3,645.130 | 0.431 | 2,609.490 | — | 0 | 12 | — | — | no | principal | no |
| sutil | SARIMA-sel | 2023 | mensual | 50 | 3,835.597 | 4,778.631 | 0.666 | 5,290.998 | 3,703.288 | 11 | 1 | -3.450 | 0.700 | sí | principal | no |
| sutil | SARIMA-sel | 2023 | mensual | 60 | 3,835.597 | 4,778.631 | 0.666 | 3,902.579 | 3,822.201 | 10 | 2 | -0.349 | 0.979 | sí | principal | no |
| sutil | SARIMA-sel | 2023 | mensual | 75 | 3,835.597 | 4,778.631 | 0.666 | 3,674.222 | 4,158.346 | 4 | 8 | 8.415 | 1.132 | sí | principal | no |
| sutil | SARIMA-sel | 2023 | mensual | 90 | 3,835.597 | 4,778.631 | 0.666 | 3,277.912 | 5,508.651 | 3 | 9 | 43.619 | 1.681 | sí | principal | no |
| sutil | SARIMA-sel | 2023 | interanual | 50 | 3,835.597 | 4,778.631 | 0.666 | 2,368.085 | 4,883.820 | 7 | 5 | 27.329 | 2.062 | sí | principal | no |
| sutil | SARIMA-sel | 2023 | interanual | 60 | 3,835.597 | 4,778.631 | 0.666 | 3,188.835 | 4,482.360 | 6 | 6 | 16.862 | 1.406 | sí | principal | no |
| sutil | SARIMA-sel | 2023 | interanual | 75 | 3,835.597 | 4,778.631 | 0.666 | 3,298.366 | 6,521.755 | 2 | 10 | 70.032 | 1.977 | sí | principal | no |
| sutil | SARIMA-sel | 2023 | interanual | 90 | 3,835.597 | 4,778.631 | 0.666 | 3,835.597 | — | 0 | 12 | — | — | no | principal | no |
| sutil | SARIMA-sel | 2024 | mensual | 50 | 3,332.996 | 4,172.430 | 0.607 | 4,113.366 | 1,772.257 | 4 | 8 | -46.827 | 0.431 | sí | principal | no |
| sutil | SARIMA-sel | 2024 | mensual | 60 | 3,332.996 | 4,172.430 | 0.607 | 4,113.366 | 1,772.257 | 4 | 8 | -46.827 | 0.431 | sí | principal | no |
| sutil | SARIMA-sel | 2024 | mensual | 75 | 3,332.996 | 4,172.430 | 0.607 | 3,332.996 | — | 0 | 12 | — | — | no | principal | no |
| sutil | SARIMA-sel | 2024 | mensual | 90 | 3,332.996 | 4,172.430 | 0.607 | 3,332.996 | — | 0 | 12 | — | — | no | principal | no |
| sutil | SARIMA-sel | 2024 | interanual | 50 | 3,332.996 | 4,172.430 | 0.607 | 3,062.790 | 3,468.099 | 8 | 4 | 4.053 | 1.132 | sí | principal | no |
| sutil | SARIMA-sel | 2024 | interanual | 60 | 3,332.996 | 4,172.430 | 0.607 | 3,062.790 | 3,468.099 | 8 | 4 | 4.053 | 1.132 | sí | principal | no |
| sutil | SARIMA-sel | 2024 | interanual | 75 | 3,332.996 | 4,172.430 | 0.607 | 3,062.790 | 3,468.099 | 8 | 4 | 4.053 | 1.132 | sí | principal | no |
| sutil | SARIMA-sel | 2024 | interanual | 90 | 3,332.996 | 4,172.430 | 0.607 | 2,246.301 | 5,506.388 | 4 | 8 | 65.208 | 2.451 | sí | principal | no |
| sutil | SARIMA-sel | 2025 | mensual | 50 | 3,946.889 | 4,772.716 | 0.681 | 3,351.547 | 4,780.368 | 5 | 7 | 21.117 | 1.426 | sí | principal | no |
| sutil | SARIMA-sel | 2025 | mensual | 60 | 3,946.889 | 4,772.716 | 0.681 | 3,351.547 | 4,780.368 | 5 | 7 | 21.117 | 1.426 | sí | principal | no |
| sutil | SARIMA-sel | 2025 | mensual | 75 | 3,946.889 | 4,772.716 | 0.681 | 3,028.738 | 6,701.344 | 3 | 9 | 69.788 | 2.213 | sí | principal | no |
| sutil | SARIMA-sel | 2025 | mensual | 90 | 3,946.889 | 4,772.716 | 0.681 | 3,134.848 | 8,007.097 | 2 | 10 | 102.871 | 2.554 | sí | principal | no |
| sutil | SARIMA-sel | 2025 | interanual | 50 | 3,946.889 | 4,772.716 | 0.681 | 4,428.058 | 2,984.552 | 4 | 8 | -24.382 | 0.674 | sí | principal | no |
| sutil | SARIMA-sel | 2025 | interanual | 60 | 3,946.889 | 4,772.716 | 0.681 | 3,654.163 | 5,410.521 | 2 | 10 | 37.083 | 1.481 | sí | principal | no |
| sutil | SARIMA-sel | 2025 | interanual | 75 | 3,946.889 | 4,772.716 | 0.681 | 3,946.889 | — | 0 | 12 | — | — | no | principal | no |
| sutil | SARIMA-sel | 2025 | interanual | 90 | 3,946.889 | 4,772.716 | 0.681 | 3,946.889 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Ridge | 2021 | mensual | 50 | 3,107.618 | 3,738.151 | 0.428 | 2,717.724 | 5,057.084 | 2 | 10 | 62.732 | 1.861 | sí | principal | no |
| sutil | Ridge | 2021 | mensual | 60 | 3,107.618 | 3,738.151 | 0.428 | 2,717.724 | 5,057.084 | 2 | 10 | 62.732 | 1.861 | sí | principal | no |
| sutil | Ridge | 2021 | mensual | 75 | 3,107.618 | 3,738.151 | 0.428 | 3,107.618 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Ridge | 2021 | mensual | 90 | 3,107.618 | 3,738.151 | 0.428 | 3,107.618 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Ridge | 2021 | interanual | 50 | 3,107.618 | 3,738.151 | 0.428 | 2,318.059 | 5,476.293 | 3 | 9 | 76.222 | 2.362 | sí | principal | no |
| sutil | Ridge | 2021 | interanual | 60 | 3,107.618 | 3,738.151 | 0.428 | 2,689.371 | 5,198.849 | 2 | 10 | 67.294 | 1.933 | sí | principal | no |
| sutil | Ridge | 2021 | interanual | 75 | 3,107.618 | 3,738.151 | 0.428 | 3,107.618 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Ridge | 2021 | interanual | 90 | 3,107.618 | 3,738.151 | 0.428 | 3,107.618 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Ridge | 2022 | mensual | 50 | 3,187.126 | 4,253.271 | 0.526 | 4,279.862 | 2,406.600 | 7 | 5 | -24.490 | 0.562 | sí | principal | no |
| sutil | Ridge | 2022 | mensual | 60 | 3,187.126 | 4,253.271 | 0.526 | 3,080.848 | 3,399.681 | 4 | 8 | 6.669 | 1.103 | sí | principal | no |
| sutil | Ridge | 2022 | mensual | 75 | 3,187.126 | 4,253.271 | 0.526 | 2,784.851 | 4,393.951 | 3 | 9 | 37.866 | 1.578 | sí | principal | no |
| sutil | Ridge | 2022 | mensual | 90 | 3,187.126 | 4,253.271 | 0.526 | 2,623.899 | 9,382.618 | 1 | 11 | 194.391 | 3.576 | no | principal | no |
| sutil | Ridge | 2022 | interanual | 50 | 3,187.126 | 4,253.271 | 0.526 | 2,319.837 | 5,788.991 | 3 | 9 | 81.637 | 2.495 | sí | principal | no |
| sutil | Ridge | 2022 | interanual | 60 | 3,187.126 | 4,253.271 | 0.526 | 3,187.126 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Ridge | 2022 | interanual | 75 | 3,187.126 | 4,253.271 | 0.526 | 3,187.126 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Ridge | 2022 | interanual | 90 | 3,187.126 | 4,253.271 | 0.526 | 3,187.126 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Ridge | 2023 | mensual | 50 | 10,777.673 | 13,607.734 | 1.870 | 3,036.815 | 11,481.387 | 11 | 1 | 6.529 | 3.781 | sí | principal | no |
| sutil | Ridge | 2023 | mensual | 60 | 10,777.673 | 13,607.734 | 1.870 | 6,050.655 | 11,723.076 | 10 | 2 | 8.772 | 1.937 | sí | principal | no |
| sutil | Ridge | 2023 | mensual | 75 | 10,777.673 | 13,607.734 | 1.870 | 9,809.441 | 12,714.137 | 4 | 8 | 17.967 | 1.296 | sí | principal | no |
| sutil | Ridge | 2023 | mensual | 90 | 10,777.673 | 13,607.734 | 1.870 | 9,144.416 | 15,677.444 | 3 | 9 | 45.462 | 1.714 | sí | principal | no |
| sutil | Ridge | 2023 | interanual | 50 | 10,777.673 | 13,607.734 | 1.870 | 11,670.639 | 10,139.840 | 7 | 5 | -5.918 | 0.869 | sí | principal | no |
| sutil | Ridge | 2023 | interanual | 60 | 10,777.673 | 13,607.734 | 1.870 | 11,379.626 | 10,175.720 | 6 | 6 | -5.585 | 0.894 | sí | principal | no |
| sutil | Ridge | 2023 | interanual | 75 | 10,777.673 | 13,607.734 | 1.870 | 10,886.722 | 10,232.427 | 2 | 10 | -5.059 | 0.940 | sí | principal | no |
| sutil | Ridge | 2023 | interanual | 90 | 10,777.673 | 13,607.734 | 1.870 | 10,777.673 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Ridge | 2024 | mensual | 50 | 4,321.686 | 5,588.634 | 0.787 | 3,876.940 | 5,211.179 | 4 | 8 | 20.582 | 1.344 | sí | principal | no |
| sutil | Ridge | 2024 | mensual | 60 | 4,321.686 | 5,588.634 | 0.787 | 3,876.940 | 5,211.179 | 4 | 8 | 20.582 | 1.344 | sí | principal | no |
| sutil | Ridge | 2024 | mensual | 75 | 4,321.686 | 5,588.634 | 0.787 | 4,321.686 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Ridge | 2024 | mensual | 90 | 4,321.686 | 5,588.634 | 0.787 | 4,321.686 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Ridge | 2024 | interanual | 50 | 4,321.686 | 5,588.634 | 0.787 | 5,716.104 | 3,624.478 | 8 | 4 | -16.133 | 0.634 | sí | principal | no |
| sutil | Ridge | 2024 | interanual | 60 | 4,321.686 | 5,588.634 | 0.787 | 5,716.104 | 3,624.478 | 8 | 4 | -16.133 | 0.634 | sí | principal | no |
| sutil | Ridge | 2024 | interanual | 75 | 4,321.686 | 5,588.634 | 0.787 | 5,716.104 | 3,624.478 | 8 | 4 | -16.133 | 0.634 | sí | principal | no |
| sutil | Ridge | 2024 | interanual | 90 | 4,321.686 | 5,588.634 | 0.787 | 4,397.978 | 4,169.104 | 4 | 8 | -3.531 | 0.948 | sí | principal | no |
| sutil | Ridge | 2025 | mensual | 50 | 3,231.577 | 4,251.571 | 0.557 | 1,877.710 | 5,126.989 | 5 | 7 | 58.653 | 2.730 | sí | principal | no |
| sutil | Ridge | 2025 | mensual | 60 | 3,231.577 | 4,251.571 | 0.557 | 1,877.710 | 5,126.989 | 5 | 7 | 58.653 | 2.730 | sí | principal | no |
| sutil | Ridge | 2025 | mensual | 75 | 3,231.577 | 4,251.571 | 0.557 | 1,916.477 | 7,176.875 | 3 | 9 | 122.086 | 3.745 | sí | principal | no |
| sutil | Ridge | 2025 | mensual | 90 | 3,231.577 | 4,251.571 | 0.557 | 2,510.215 | 6,838.384 | 2 | 10 | 111.611 | 2.724 | sí | principal | no |
| sutil | Ridge | 2025 | interanual | 50 | 3,231.577 | 4,251.571 | 0.557 | 3,336.277 | 3,022.176 | 4 | 8 | -6.480 | 0.906 | sí | principal | no |
| sutil | Ridge | 2025 | interanual | 60 | 3,231.577 | 4,251.571 | 0.557 | 3,314.770 | 2,815.608 | 2 | 10 | -12.872 | 0.849 | sí | principal | no |
| sutil | Ridge | 2025 | interanual | 75 | 3,231.577 | 4,251.571 | 0.557 | 3,231.577 | — | 0 | 12 | — | — | no | principal | no |
| sutil | Ridge | 2025 | interanual | 90 | 3,231.577 | 4,251.571 | 0.557 | 3,231.577 | — | 0 | 12 | — | — | no | principal | no |
| sutil | ElasticNet | 2021 | mensual | 50 | 3,005.738 | 3,542.671 | 0.414 | 2,527.210 | 5,398.379 | 2 | 10 | 79.602 | 2.136 | sí | principal | no |
| sutil | ElasticNet | 2021 | mensual | 60 | 3,005.738 | 3,542.671 | 0.414 | 2,527.210 | 5,398.379 | 2 | 10 | 79.602 | 2.136 | sí | principal | no |
| sutil | ElasticNet | 2021 | mensual | 75 | 3,005.738 | 3,542.671 | 0.414 | 3,005.738 | — | 0 | 12 | — | — | no | principal | no |
| sutil | ElasticNet | 2021 | mensual | 90 | 3,005.738 | 3,542.671 | 0.414 | 3,005.738 | — | 0 | 12 | — | — | no | principal | no |
| sutil | ElasticNet | 2021 | interanual | 50 | 3,005.738 | 3,542.671 | 0.414 | 2,341.197 | 4,999.363 | 3 | 9 | 66.327 | 2.135 | sí | principal | no |
| sutil | ElasticNet | 2021 | interanual | 60 | 3,005.738 | 3,542.671 | 0.414 | 2,747.402 | 4,297.419 | 2 | 10 | 42.974 | 1.564 | sí | principal | no |
| sutil | ElasticNet | 2021 | interanual | 75 | 3,005.738 | 3,542.671 | 0.414 | 3,005.738 | — | 0 | 12 | — | — | no | principal | no |
| sutil | ElasticNet | 2021 | interanual | 90 | 3,005.738 | 3,542.671 | 0.414 | 3,005.738 | — | 0 | 12 | — | — | no | principal | no |
| sutil | ElasticNet | 2022 | mensual | 50 | 2,967.849 | 4,015.159 | 0.490 | 3,828.905 | 2,352.808 | 7 | 5 | -20.723 | 0.614 | sí | principal | no |
| sutil | ElasticNet | 2022 | mensual | 60 | 2,967.849 | 4,015.159 | 0.490 | 2,897.172 | 3,109.202 | 4 | 8 | 4.763 | 1.073 | sí | principal | no |
| sutil | ElasticNet | 2022 | mensual | 75 | 2,967.849 | 4,015.159 | 0.490 | 2,618.916 | 4,014.647 | 3 | 9 | 35.271 | 1.533 | sí | principal | no |
| sutil | ElasticNet | 2022 | mensual | 90 | 2,967.849 | 4,015.159 | 0.490 | 2,400.580 | 9,207.804 | 1 | 11 | 210.252 | 3.836 | no | principal | no |
| sutil | ElasticNet | 2022 | interanual | 50 | 2,967.849 | 4,015.159 | 0.490 | 2,111.659 | 5,536.416 | 3 | 9 | 86.546 | 2.622 | sí | principal | no |
| sutil | ElasticNet | 2022 | interanual | 60 | 2,967.849 | 4,015.159 | 0.490 | 2,967.849 | — | 0 | 12 | — | — | no | principal | no |
| sutil | ElasticNet | 2022 | interanual | 75 | 2,967.849 | 4,015.159 | 0.490 | 2,967.849 | — | 0 | 12 | — | — | no | principal | no |
| sutil | ElasticNet | 2022 | interanual | 90 | 2,967.849 | 4,015.159 | 0.490 | 2,967.849 | — | 0 | 12 | — | — | no | principal | no |
| sutil | ElasticNet | 2023 | mensual | 50 | 10,412.551 | 12,704.843 | 1.807 | 3,039.965 | 11,082.786 | 11 | 1 | 6.437 | 3.646 | sí | principal | no |
| sutil | ElasticNet | 2023 | mensual | 60 | 10,412.551 | 12,704.843 | 1.807 | 6,707.971 | 11,153.467 | 10 | 2 | 7.116 | 1.663 | sí | principal | no |
| sutil | ElasticNet | 2023 | mensual | 75 | 10,412.551 | 12,704.843 | 1.807 | 9,715.608 | 11,806.438 | 4 | 8 | 13.387 | 1.215 | sí | principal | no |
| sutil | ElasticNet | 2023 | mensual | 90 | 10,412.551 | 12,704.843 | 1.807 | 9,011.851 | 14,614.653 | 3 | 9 | 40.356 | 1.622 | sí | principal | no |
| sutil | ElasticNet | 2023 | interanual | 50 | 10,412.551 | 12,704.843 | 1.807 | 10,301.643 | 10,491.771 | 7 | 5 | 0.761 | 1.018 | sí | principal | no |
| sutil | ElasticNet | 2023 | interanual | 60 | 10,412.551 | 12,704.843 | 1.807 | 10,175.108 | 10,649.994 | 6 | 6 | 2.280 | 1.047 | sí | principal | no |
| sutil | ElasticNet | 2023 | interanual | 75 | 10,412.551 | 12,704.843 | 1.807 | 10,418.710 | 10,381.758 | 2 | 10 | -0.296 | 0.996 | sí | principal | no |
| sutil | ElasticNet | 2023 | interanual | 90 | 10,412.551 | 12,704.843 | 1.807 | 10,412.551 | — | 0 | 12 | — | — | no | principal | no |
| sutil | ElasticNet | 2024 | mensual | 50 | 4,750.530 | 6,275.028 | 0.865 | 4,210.557 | 5,830.475 | 4 | 8 | 22.733 | 1.385 | sí | principal | no |
| sutil | ElasticNet | 2024 | mensual | 60 | 4,750.530 | 6,275.028 | 0.865 | 4,210.557 | 5,830.475 | 4 | 8 | 22.733 | 1.385 | sí | principal | no |
| sutil | ElasticNet | 2024 | mensual | 75 | 4,750.530 | 6,275.028 | 0.865 | 4,750.530 | — | 0 | 12 | — | — | no | principal | no |
| sutil | ElasticNet | 2024 | mensual | 90 | 4,750.530 | 6,275.028 | 0.865 | 4,750.530 | — | 0 | 12 | — | — | no | principal | no |
| sutil | ElasticNet | 2024 | interanual | 50 | 4,750.530 | 6,275.028 | 0.865 | 5,933.159 | 4,159.215 | 8 | 4 | -12.447 | 0.701 | sí | principal | no |
| sutil | ElasticNet | 2024 | interanual | 60 | 4,750.530 | 6,275.028 | 0.865 | 5,933.159 | 4,159.215 | 8 | 4 | -12.447 | 0.701 | sí | principal | no |
| sutil | ElasticNet | 2024 | interanual | 75 | 4,750.530 | 6,275.028 | 0.865 | 5,933.159 | 4,159.215 | 8 | 4 | -12.447 | 0.701 | sí | principal | no |
| sutil | ElasticNet | 2024 | interanual | 90 | 4,750.530 | 6,275.028 | 0.865 | 4,716.942 | 4,817.704 | 4 | 8 | 1.414 | 1.021 | sí | principal | no |
| sutil | ElasticNet | 2025 | mensual | 50 | 3,222.889 | 4,372.336 | 0.556 | 1,586.982 | 5,513.159 | 5 | 7 | 71.063 | 3.474 | sí | principal | no |
| sutil | ElasticNet | 2025 | mensual | 60 | 3,222.889 | 4,372.336 | 0.556 | 1,586.982 | 5,513.159 | 5 | 7 | 71.063 | 3.474 | sí | principal | no |
| sutil | ElasticNet | 2025 | mensual | 75 | 3,222.889 | 4,372.336 | 0.556 | 1,822.996 | 7,422.569 | 3 | 9 | 130.308 | 4.072 | sí | principal | no |
| sutil | ElasticNet | 2025 | mensual | 90 | 3,222.889 | 4,372.336 | 0.556 | 2,658.902 | 6,042.823 | 2 | 10 | 87.497 | 2.273 | sí | principal | no |
| sutil | ElasticNet | 2025 | interanual | 50 | 3,222.889 | 4,372.336 | 0.556 | 3,146.565 | 3,375.537 | 4 | 8 | 4.736 | 1.073 | sí | principal | no |
| sutil | ElasticNet | 2025 | interanual | 60 | 3,222.889 | 4,372.336 | 0.556 | 3,268.145 | 2,996.610 | 2 | 10 | -7.021 | 0.917 | sí | principal | no |
| sutil | ElasticNet | 2025 | interanual | 75 | 3,222.889 | 4,372.336 | 0.556 | 3,222.889 | — | 0 | 12 | — | — | no | principal | no |
| sutil | ElasticNet | 2025 | interanual | 90 | 3,222.889 | 4,372.336 | 0.556 | 3,222.889 | — | 0 | 12 | — | — | no | principal | no |
| sutil | XGB-37 | 2021 | mensual | 50 | 5,211.250 | 5,670.208 | 0.718 | 4,835.664 | 7,089.178 | 2 | 10 | 36.036 | 1.466 | sí | principal | no |
| sutil | XGB-37 | 2021 | mensual | 60 | 5,211.250 | 5,670.208 | 0.718 | 4,835.664 | 7,089.178 | 2 | 10 | 36.036 | 1.466 | sí | principal | no |
| sutil | XGB-37 | 2021 | mensual | 75 | 5,211.250 | 5,670.208 | 0.718 | 5,211.250 | — | 0 | 12 | — | — | no | principal | no |
| sutil | XGB-37 | 2021 | mensual | 90 | 5,211.250 | 5,670.208 | 0.718 | 5,211.250 | — | 0 | 12 | — | — | no | principal | no |
| sutil | XGB-37 | 2021 | interanual | 50 | 5,211.250 | 5,670.208 | 0.718 | 4,722.243 | 6,678.268 | 3 | 9 | 28.151 | 1.414 | sí | principal | no |
| sutil | XGB-37 | 2021 | interanual | 60 | 5,211.250 | 5,670.208 | 0.718 | 5,314.628 | 4,694.359 | 2 | 10 | -9.919 | 0.883 | sí | principal | no |
| sutil | XGB-37 | 2021 | interanual | 75 | 5,211.250 | 5,670.208 | 0.718 | 5,211.250 | — | 0 | 12 | — | — | no | principal | no |
| sutil | XGB-37 | 2021 | interanual | 90 | 5,211.250 | 5,670.208 | 0.718 | 5,211.250 | — | 0 | 12 | — | — | no | principal | no |
| sutil | XGB-37 | 2022 | mensual | 50 | 4,551.578 | 5,841.017 | 0.752 | 5,766.363 | 3,683.874 | 7 | 5 | -19.064 | 0.639 | sí | principal | no |
| sutil | XGB-37 | 2022 | mensual | 60 | 4,551.578 | 5,841.017 | 0.752 | 4,665.723 | 4,323.288 | 4 | 8 | -5.016 | 0.927 | sí | principal | no |
| sutil | XGB-37 | 2022 | mensual | 75 | 4,551.578 | 5,841.017 | 0.752 | 4,324.163 | 5,233.824 | 3 | 9 | 14.989 | 1.210 | sí | principal | no |
| sutil | XGB-37 | 2022 | mensual | 90 | 4,551.578 | 5,841.017 | 0.752 | 4,089.957 | 9,629.407 | 1 | 11 | 111.562 | 2.354 | no | principal | no |
| sutil | XGB-37 | 2022 | interanual | 50 | 4,551.578 | 5,841.017 | 0.752 | 3,484.323 | 7,753.343 | 3 | 9 | 70.344 | 2.225 | sí | principal | no |
| sutil | XGB-37 | 2022 | interanual | 60 | 4,551.578 | 5,841.017 | 0.752 | 4,551.578 | — | 0 | 12 | — | — | no | principal | no |
| sutil | XGB-37 | 2022 | interanual | 75 | 4,551.578 | 5,841.017 | 0.752 | 4,551.578 | — | 0 | 12 | — | — | no | principal | no |
| sutil | XGB-37 | 2022 | interanual | 90 | 4,551.578 | 5,841.017 | 0.752 | 4,551.578 | — | 0 | 12 | — | — | no | principal | no |
| sutil | XGB-37 | 2023 | mensual | 50 | 3,785.322 | 4,270.759 | 0.657 | 979.793 | 4,040.370 | 11 | 1 | 6.738 | 4.124 | sí | principal | no |
| sutil | XGB-37 | 2023 | mensual | 60 | 3,785.322 | 4,270.759 | 0.657 | 1,997.538 | 4,142.879 | 10 | 2 | 9.446 | 2.074 | sí | principal | no |
| sutil | XGB-37 | 2023 | mensual | 75 | 3,785.322 | 4,270.759 | 0.657 | 3,308.002 | 4,739.962 | 4 | 8 | 25.220 | 1.433 | sí | principal | no |
| sutil | XGB-37 | 2023 | mensual | 90 | 3,785.322 | 4,270.759 | 0.657 | 3,517.726 | 4,588.109 | 3 | 9 | 21.208 | 1.304 | sí | principal | no |
| sutil | XGB-37 | 2023 | interanual | 50 | 3,785.322 | 4,270.759 | 0.657 | 3,346.735 | 4,098.599 | 7 | 5 | 8.276 | 1.225 | sí | principal | no |
| sutil | XGB-37 | 2023 | interanual | 60 | 3,785.322 | 4,270.759 | 0.657 | 3,110.932 | 4,459.713 | 6 | 6 | 17.816 | 1.434 | sí | principal | no |
| sutil | XGB-37 | 2023 | interanual | 75 | 3,785.322 | 4,270.759 | 0.657 | 3,675.825 | 4,332.807 | 2 | 10 | 14.463 | 1.179 | sí | principal | no |
| sutil | XGB-37 | 2023 | interanual | 90 | 3,785.322 | 4,270.759 | 0.657 | 3,785.322 | — | 0 | 12 | — | — | no | principal | no |
| sutil | XGB-37 | 2024 | mensual | 50 | 4,956.724 | 6,524.385 | 0.903 | 4,499.919 | 5,870.333 | 4 | 8 | 18.432 | 1.305 | sí | principal | no |
| sutil | XGB-37 | 2024 | mensual | 60 | 4,956.724 | 6,524.385 | 0.903 | 4,499.919 | 5,870.333 | 4 | 8 | 18.432 | 1.305 | sí | principal | no |
| sutil | XGB-37 | 2024 | mensual | 75 | 4,956.724 | 6,524.385 | 0.903 | 4,956.724 | — | 0 | 12 | — | — | no | principal | no |
| sutil | XGB-37 | 2024 | mensual | 90 | 4,956.724 | 6,524.385 | 0.903 | 4,956.724 | — | 0 | 12 | — | — | no | principal | no |
| sutil | XGB-37 | 2024 | interanual | 50 | 4,956.724 | 6,524.385 | 0.903 | 4,995.361 | 4,937.405 | 8 | 4 | -0.390 | 0.988 | sí | principal | no |
| sutil | XGB-37 | 2024 | interanual | 60 | 4,956.724 | 6,524.385 | 0.903 | 4,995.361 | 4,937.405 | 8 | 4 | -0.390 | 0.988 | sí | principal | no |
| sutil | XGB-37 | 2024 | interanual | 75 | 4,956.724 | 6,524.385 | 0.903 | 4,995.361 | 4,937.405 | 8 | 4 | -0.390 | 0.988 | sí | principal | no |
| sutil | XGB-37 | 2024 | interanual | 90 | 4,956.724 | 6,524.385 | 0.903 | 4,657.240 | 5,555.691 | 4 | 8 | 12.084 | 1.193 | sí | principal | no |
| sutil | XGB-37 | 2025 | mensual | 50 | 5,902.375 | 7,010.785 | 1.018 | 5,253.416 | 6,810.919 | 5 | 7 | 15.393 | 1.296 | sí | principal | no |
| sutil | XGB-37 | 2025 | mensual | 60 | 5,902.375 | 7,010.785 | 1.018 | 5,253.416 | 6,810.919 | 5 | 7 | 15.393 | 1.296 | sí | principal | no |
| sutil | XGB-37 | 2025 | mensual | 75 | 5,902.375 | 7,010.785 | 1.018 | 5,104.202 | 8,296.897 | 3 | 9 | 40.569 | 1.626 | sí | principal | no |
| sutil | XGB-37 | 2025 | mensual | 90 | 5,902.375 | 7,010.785 | 1.018 | 4,643.743 | 12,195.535 | 2 | 10 | 106.621 | 2.626 | sí | principal | no |
| sutil | XGB-37 | 2025 | interanual | 50 | 5,902.375 | 7,010.785 | 1.018 | 6,584.126 | 4,538.874 | 4 | 8 | -23.101 | 0.689 | sí | principal | no |
| sutil | XGB-37 | 2025 | interanual | 60 | 5,902.375 | 7,010.785 | 1.018 | 5,627.062 | 7,278.941 | 2 | 10 | 23.322 | 1.294 | sí | principal | no |
| sutil | XGB-37 | 2025 | interanual | 75 | 5,902.375 | 7,010.785 | 1.018 | 5,902.375 | — | 0 | 12 | — | — | no | principal | no |
| sutil | XGB-37 | 2025 | interanual | 90 | 5,902.375 | 7,010.785 | 1.018 | 5,902.375 | — | 0 | 12 | — | — | no | principal | no |
| sutil | GC3 | 2021 | mensual | 50 | 3,856.029 | 4,325.494 | 0.531 | 3,665.762 | 4,807.363 | 2 | 10 | 24.671 | 1.311 | sí | principal | no |
| sutil | GC3 | 2021 | mensual | 60 | 3,856.029 | 4,325.494 | 0.531 | 3,665.762 | 4,807.363 | 2 | 10 | 24.671 | 1.311 | sí | principal | no |
| sutil | GC3 | 2021 | mensual | 75 | 3,856.029 | 4,325.494 | 0.531 | 3,856.029 | — | 0 | 12 | — | — | no | principal | no |
| sutil | GC3 | 2021 | mensual | 90 | 3,856.029 | 4,325.494 | 0.531 | 3,856.029 | — | 0 | 12 | — | — | no | principal | no |
| sutil | GC3 | 2021 | interanual | 50 | 3,856.029 | 4,325.494 | 0.531 | 3,824.464 | 3,950.722 | 3 | 9 | 2.456 | 1.033 | sí | principal | no |
| sutil | GC3 | 2021 | interanual | 60 | 3,856.029 | 4,325.494 | 0.531 | 4,143.807 | 2,417.135 | 2 | 10 | -37.315 | 0.583 | sí | principal | no |
| sutil | GC3 | 2021 | interanual | 75 | 3,856.029 | 4,325.494 | 0.531 | 3,856.029 | — | 0 | 12 | — | — | no | principal | no |
| sutil | GC3 | 2021 | interanual | 90 | 3,856.029 | 4,325.494 | 0.531 | 3,856.029 | — | 0 | 12 | — | — | no | principal | no |
| sutil | GC3 | 2022 | mensual | 50 | 5,161.891 | 6,398.885 | 0.852 | 6,224.041 | 4,403.212 | 7 | 5 | -14.698 | 0.707 | sí | principal | no |
| sutil | GC3 | 2022 | mensual | 60 | 5,161.891 | 6,398.885 | 0.852 | 5,498.087 | 4,489.499 | 4 | 8 | -13.026 | 0.817 | sí | principal | no |
| sutil | GC3 | 2022 | mensual | 75 | 5,161.891 | 6,398.885 | 0.852 | 5,243.881 | 4,915.920 | 3 | 9 | -4.765 | 0.937 | sí | principal | no |
| sutil | GC3 | 2022 | mensual | 90 | 5,161.891 | 6,398.885 | 0.852 | 4,679.764 | 10,465.287 | 1 | 11 | 102.741 | 2.236 | no | principal | no |
| sutil | GC3 | 2022 | interanual | 50 | 5,161.891 | 6,398.885 | 0.852 | 3,933.855 | 8,846.000 | 3 | 9 | 71.371 | 2.249 | sí | principal | no |
| sutil | GC3 | 2022 | interanual | 60 | 5,161.891 | 6,398.885 | 0.852 | 5,161.891 | — | 0 | 12 | — | — | no | principal | no |
| sutil | GC3 | 2022 | interanual | 75 | 5,161.891 | 6,398.885 | 0.852 | 5,161.891 | — | 0 | 12 | — | — | no | principal | no |
| sutil | GC3 | 2022 | interanual | 90 | 5,161.891 | 6,398.885 | 0.852 | 5,161.891 | — | 0 | 12 | — | — | no | principal | no |
| sutil | GC3 | 2023 | mensual | 50 | 6,073.697 | 7,052.960 | 1.054 | 1,624.042 | 6,478.211 | 11 | 1 | 6.660 | 3.989 | sí | principal | no |
| sutil | GC3 | 2023 | mensual | 60 | 6,073.697 | 7,052.960 | 1.054 | 4,723.031 | 6,343.830 | 10 | 2 | 4.448 | 1.343 | sí | principal | no |
| sutil | GC3 | 2023 | mensual | 75 | 6,073.697 | 7,052.960 | 1.054 | 5,458.732 | 7,303.627 | 4 | 8 | 20.250 | 1.338 | sí | principal | no |
| sutil | GC3 | 2023 | mensual | 90 | 6,073.697 | 7,052.960 | 1.054 | 5,669.884 | 7,285.136 | 3 | 9 | 19.946 | 1.285 | sí | principal | no |
| sutil | GC3 | 2023 | interanual | 50 | 6,073.697 | 7,052.960 | 1.054 | 3,791.359 | 7,703.939 | 7 | 5 | 26.841 | 2.032 | sí | principal | no |
| sutil | GC3 | 2023 | interanual | 60 | 6,073.697 | 7,052.960 | 1.054 | 3,641.571 | 8,505.823 | 6 | 6 | 40.044 | 2.336 | sí | principal | no |
| sutil | GC3 | 2023 | interanual | 75 | 6,073.697 | 7,052.960 | 1.054 | 5,415.449 | 9,364.936 | 2 | 10 | 54.188 | 1.729 | sí | principal | no |
| sutil | GC3 | 2023 | interanual | 90 | 6,073.697 | 7,052.960 | 1.054 | 6,073.697 | — | 0 | 12 | — | — | no | principal | no |
| sutil | GC3 | 2024 | mensual | 50 | 8,968.906 | 11,703.585 | 1.633 | 8,090.629 | 10,725.459 | 4 | 8 | 19.585 | 1.326 | sí | principal | no |
| sutil | GC3 | 2024 | mensual | 60 | 8,968.906 | 11,703.585 | 1.633 | 8,090.629 | 10,725.459 | 4 | 8 | 19.585 | 1.326 | sí | principal | no |
| sutil | GC3 | 2024 | mensual | 75 | 8,968.906 | 11,703.585 | 1.633 | 8,968.906 | — | 0 | 12 | — | — | no | principal | no |
| sutil | GC3 | 2024 | mensual | 90 | 8,968.906 | 11,703.585 | 1.633 | 8,968.906 | — | 0 | 12 | — | — | no | principal | no |
| sutil | GC3 | 2024 | interanual | 50 | 8,968.906 | 11,703.585 | 1.633 | 8,673.894 | 9,116.411 | 8 | 4 | 1.645 | 1.051 | sí | principal | no |
| sutil | GC3 | 2024 | interanual | 60 | 8,968.906 | 11,703.585 | 1.633 | 8,673.894 | 9,116.411 | 8 | 4 | 1.645 | 1.051 | sí | principal | no |
| sutil | GC3 | 2024 | interanual | 75 | 8,968.906 | 11,703.585 | 1.633 | 8,673.894 | 9,116.411 | 8 | 4 | 1.645 | 1.051 | sí | principal | no |
| sutil | GC3 | 2024 | interanual | 90 | 8,968.906 | 11,703.585 | 1.633 | 8,347.551 | 10,211.615 | 4 | 8 | 13.856 | 1.223 | sí | principal | no |
| sutil | GC3 | 2025 | mensual | 50 | 7,746.000 | 8,684.061 | 1.336 | 9,604.058 | 5,144.719 | 5 | 7 | -33.582 | 0.536 | sí | principal | no |
| sutil | GC3 | 2025 | mensual | 60 | 7,746.000 | 8,684.061 | 1.336 | 9,604.058 | 5,144.719 | 5 | 7 | -33.582 | 0.536 | sí | principal | no |
| sutil | GC3 | 2025 | mensual | 75 | 7,746.000 | 8,684.061 | 1.336 | 8,463.297 | 5,594.109 | 3 | 9 | -27.781 | 0.661 | sí | principal | no |
| sutil | GC3 | 2025 | mensual | 90 | 7,746.000 | 8,684.061 | 1.336 | 7,783.124 | 7,560.381 | 2 | 10 | -2.396 | 0.971 | sí | principal | no |
| sutil | GC3 | 2025 | interanual | 50 | 7,746.000 | 8,684.061 | 1.336 | 8,370.698 | 6,496.605 | 4 | 8 | -16.130 | 0.776 | sí | principal | no |
| sutil | GC3 | 2025 | interanual | 60 | 7,746.000 | 8,684.061 | 1.336 | 7,829.304 | 7,329.482 | 2 | 10 | -5.377 | 0.936 | sí | principal | no |
| sutil | GC3 | 2025 | interanual | 75 | 7,746.000 | 8,684.061 | 1.336 | 7,746.000 | — | 0 | 12 | — | — | no | principal | no |
| sutil | GC3 | 2025 | interanual | 90 | 7,746.000 | 8,684.061 | 1.336 | 7,746.000 | — | 0 | 12 | — | — | no | principal | no |
| sutil | GE | 2021 | mensual | 50 | 3,867.170 | 4,321.483 | 0.533 | 3,666.506 | 4,870.493 | 2 | 10 | 25.945 | 1.328 | sí | principal | no |
| sutil | GE | 2021 | mensual | 60 | 3,867.170 | 4,321.483 | 0.533 | 3,666.506 | 4,870.493 | 2 | 10 | 25.945 | 1.328 | sí | principal | no |
| sutil | GE | 2021 | mensual | 75 | 3,867.170 | 4,321.483 | 0.533 | 3,867.170 | — | 0 | 12 | — | — | no | principal | no |
| sutil | GE | 2021 | mensual | 90 | 3,867.170 | 4,321.483 | 0.533 | 3,867.170 | — | 0 | 12 | — | — | no | principal | no |
| sutil | GE | 2021 | interanual | 50 | 3,867.170 | 4,321.483 | 0.533 | 3,921.620 | 3,703.820 | 3 | 9 | -4.224 | 0.944 | sí | principal | no |
| sutil | GE | 2021 | interanual | 60 | 3,867.170 | 4,321.483 | 0.533 | 4,199.101 | 2,207.514 | 2 | 10 | -42.917 | 0.526 | sí | principal | no |
| sutil | GE | 2021 | interanual | 75 | 3,867.170 | 4,321.483 | 0.533 | 3,867.170 | — | 0 | 12 | — | — | no | principal | no |
| sutil | GE | 2021 | interanual | 90 | 3,867.170 | 4,321.483 | 0.533 | 3,867.170 | — | 0 | 12 | — | — | no | principal | no |
| sutil | GE | 2022 | mensual | 50 | 5,259.557 | 6,836.400 | 0.868 | 6,756.758 | 4,190.127 | 7 | 5 | -20.333 | 0.620 | sí | principal | no |
| sutil | GE | 2022 | mensual | 60 | 5,259.557 | 6,836.400 | 0.868 | 5,691.886 | 4,394.899 | 4 | 8 | -16.440 | 0.772 | sí | principal | no |
| sutil | GE | 2022 | mensual | 75 | 5,259.557 | 6,836.400 | 0.868 | 5,278.811 | 5,201.793 | 3 | 9 | -1.098 | 0.985 | sí | principal | no |
| sutil | GE | 2022 | mensual | 90 | 5,259.557 | 6,836.400 | 0.868 | 4,699.892 | 11,415.866 | 1 | 11 | 117.050 | 2.429 | no | principal | no |
| sutil | GE | 2022 | interanual | 50 | 5,259.557 | 6,836.400 | 0.868 | 3,977.921 | 9,104.465 | 3 | 9 | 73.103 | 2.289 | sí | principal | no |
| sutil | GE | 2022 | interanual | 60 | 5,259.557 | 6,836.400 | 0.868 | 5,259.557 | — | 0 | 12 | — | — | no | principal | no |
| sutil | GE | 2022 | interanual | 75 | 5,259.557 | 6,836.400 | 0.868 | 5,259.557 | — | 0 | 12 | — | — | no | principal | no |
| sutil | GE | 2022 | interanual | 90 | 5,259.557 | 6,836.400 | 0.868 | 5,259.557 | — | 0 | 12 | — | — | no | principal | no |
| sutil | GE | 2023 | mensual | 50 | 5,390.539 | 6,249.293 | 0.935 | 1,396.321 | 5,753.650 | 11 | 1 | 6.736 | 4.121 | sí | principal | no |
| sutil | GE | 2023 | mensual | 60 | 5,390.539 | 6,249.293 | 0.935 | 3,769.342 | 5,714.779 | 10 | 2 | 6.015 | 1.516 | sí | principal | no |
| sutil | GE | 2023 | mensual | 75 | 5,390.539 | 6,249.293 | 0.935 | 4,468.857 | 7,233.905 | 4 | 8 | 34.196 | 1.619 | sí | principal | no |
| sutil | GE | 2023 | mensual | 90 | 5,390.539 | 6,249.293 | 0.935 | 4,933.477 | 6,761.726 | 3 | 9 | 25.437 | 1.371 | sí | principal | no |
| sutil | GE | 2023 | interanual | 50 | 5,390.539 | 6,249.293 | 0.935 | 4,108.709 | 6,306.132 | 7 | 5 | 16.985 | 1.535 | sí | principal | no |
| sutil | GE | 2023 | interanual | 60 | 5,390.539 | 6,249.293 | 0.935 | 3,782.724 | 6,998.355 | 6 | 6 | 29.827 | 1.850 | sí | principal | no |
| sutil | GE | 2023 | interanual | 75 | 5,390.539 | 6,249.293 | 0.935 | 4,783.737 | 8,424.549 | 2 | 10 | 56.284 | 1.761 | sí | principal | no |
| sutil | GE | 2023 | interanual | 90 | 5,390.539 | 6,249.293 | 0.935 | 5,390.539 | — | 0 | 12 | — | — | no | principal | no |
| sutil | GE | 2024 | mensual | 50 | 9,773.925 | 12,199.029 | 1.780 | 8,877.839 | 11,566.096 | 4 | 8 | 18.336 | 1.303 | sí | principal | no |
| sutil | GE | 2024 | mensual | 60 | 9,773.925 | 12,199.029 | 1.780 | 8,877.839 | 11,566.096 | 4 | 8 | 18.336 | 1.303 | sí | principal | no |
| sutil | GE | 2024 | mensual | 75 | 9,773.925 | 12,199.029 | 1.780 | 9,773.925 | — | 0 | 12 | — | — | no | principal | no |
| sutil | GE | 2024 | mensual | 90 | 9,773.925 | 12,199.029 | 1.780 | 9,773.925 | — | 0 | 12 | — | — | no | principal | no |
| sutil | GE | 2024 | interanual | 50 | 9,773.925 | 12,199.029 | 1.780 | 9,043.982 | 10,138.896 | 8 | 4 | 3.734 | 1.121 | sí | principal | no |
| sutil | GE | 2024 | interanual | 60 | 9,773.925 | 12,199.029 | 1.780 | 9,043.982 | 10,138.896 | 8 | 4 | 3.734 | 1.121 | sí | principal | no |
| sutil | GE | 2024 | interanual | 75 | 9,773.925 | 12,199.029 | 1.780 | 9,043.982 | 10,138.896 | 8 | 4 | 3.734 | 1.121 | sí | principal | no |
| sutil | GE | 2024 | interanual | 90 | 9,773.925 | 12,199.029 | 1.780 | 9,011.198 | 11,299.378 | 4 | 8 | 15.607 | 1.254 | sí | principal | no |
| sutil | GE | 2025 | mensual | 50 | 9,426.459 | 10,830.150 | 1.626 | 11,972.277 | 5,862.313 | 5 | 7 | -37.810 | 0.490 | sí | principal | no |
| sutil | GE | 2025 | mensual | 60 | 9,426.459 | 10,830.150 | 1.626 | 11,972.277 | 5,862.313 | 5 | 7 | -37.810 | 0.490 | sí | principal | no |
| sutil | GE | 2025 | mensual | 75 | 9,426.459 | 10,830.150 | 1.626 | 9,932.449 | 7,908.488 | 3 | 9 | -16.103 | 0.796 | sí | principal | no |
| sutil | GE | 2025 | mensual | 90 | 9,426.459 | 10,830.150 | 1.626 | 9,116.512 | 10,976.192 | 2 | 10 | 16.440 | 1.204 | sí | principal | no |
| sutil | GE | 2025 | interanual | 50 | 9,426.459 | 10,830.150 | 1.626 | 10,726.429 | 6,826.518 | 4 | 8 | -27.581 | 0.636 | sí | principal | no |
| sutil | GE | 2025 | interanual | 60 | 9,426.459 | 10,830.150 | 1.626 | 9,355.432 | 9,781.593 | 2 | 10 | 3.767 | 1.046 | sí | principal | no |
| sutil | GE | 2025 | interanual | 75 | 9,426.459 | 10,830.150 | 1.626 | 9,426.459 | — | 0 | 12 | — | — | no | principal | no |
| sutil | GE | 2025 | interanual | 90 | 9,426.459 | 10,830.150 | 1.626 | 9,426.459 | — | 0 | 12 | — | — | no | principal | no |
| sutil | XGB-43 | 2021 | mensual | 50 | 5,333.052 | 5,803.354 | 0.735 | 4,948.609 | 7,255.268 | 2 | 10 | 36.043 | 1.466 | sí | principal | sí |
| sutil | XGB-43 | 2021 | mensual | 60 | 5,333.052 | 5,803.354 | 0.735 | 4,948.609 | 7,255.268 | 2 | 10 | 36.043 | 1.466 | sí | principal | sí |
| sutil | XGB-43 | 2021 | mensual | 75 | 5,333.052 | 5,803.354 | 0.735 | 5,333.052 | — | 0 | 12 | — | — | no | principal | sí |
| sutil | XGB-43 | 2021 | mensual | 90 | 5,333.052 | 5,803.354 | 0.735 | 5,333.052 | — | 0 | 12 | — | — | no | principal | sí |
| sutil | XGB-43 | 2021 | interanual | 50 | 5,333.052 | 5,803.354 | 0.735 | 4,774.485 | 7,008.752 | 3 | 9 | 31.421 | 1.468 | sí | principal | sí |
| sutil | XGB-43 | 2021 | interanual | 60 | 5,333.052 | 5,803.354 | 0.735 | 5,390.841 | 5,044.106 | 2 | 10 | -5.418 | 0.936 | sí | principal | sí |
| sutil | XGB-43 | 2021 | interanual | 75 | 5,333.052 | 5,803.354 | 0.735 | 5,333.052 | — | 0 | 12 | — | — | no | principal | sí |
| sutil | XGB-43 | 2021 | interanual | 90 | 5,333.052 | 5,803.354 | 0.735 | 5,333.052 | — | 0 | 12 | — | — | no | principal | sí |
| sutil | XGB-43 | 2022 | mensual | 50 | 4,663.571 | 5,969.092 | 0.770 | 5,967.890 | 3,731.915 | 7 | 5 | -19.977 | 0.625 | sí | principal | sí |
| sutil | XGB-43 | 2022 | mensual | 60 | 4,663.571 | 5,969.092 | 0.770 | 4,773.475 | 4,443.763 | 4 | 8 | -4.713 | 0.931 | sí | principal | sí |
| sutil | XGB-43 | 2022 | mensual | 75 | 4,663.571 | 5,969.092 | 0.770 | 4,426.638 | 5,374.369 | 3 | 9 | 15.242 | 1.214 | sí | principal | sí |
| sutil | XGB-43 | 2022 | mensual | 90 | 4,663.571 | 5,969.092 | 0.770 | 4,225.706 | 9,480.089 | 1 | 11 | 103.280 | 2.243 | no | principal | sí |
| sutil | XGB-43 | 2022 | interanual | 50 | 4,663.571 | 5,969.092 | 0.770 | 3,692.484 | 7,576.830 | 3 | 9 | 62.468 | 2.052 | sí | principal | sí |
| sutil | XGB-43 | 2022 | interanual | 60 | 4,663.571 | 5,969.092 | 0.770 | 4,663.571 | — | 0 | 12 | — | — | no | principal | sí |
| sutil | XGB-43 | 2022 | interanual | 75 | 4,663.571 | 5,969.092 | 0.770 | 4,663.571 | — | 0 | 12 | — | — | no | principal | sí |
| sutil | XGB-43 | 2022 | interanual | 90 | 4,663.571 | 5,969.092 | 0.770 | 4,663.571 | — | 0 | 12 | — | — | no | principal | sí |
| sutil | XGB-43 | 2023 | mensual | 50 | 3,679.053 | 4,199.635 | 0.638 | 1,073.345 | 3,915.935 | 11 | 1 | 6.439 | 3.648 | sí | principal | sí |
| sutil | XGB-43 | 2023 | mensual | 60 | 3,679.053 | 4,199.635 | 0.638 | 1,982.459 | 4,018.372 | 10 | 2 | 9.223 | 2.027 | sí | principal | sí |
| sutil | XGB-43 | 2023 | mensual | 75 | 3,679.053 | 4,199.635 | 0.638 | 3,190.502 | 4,656.154 | 4 | 8 | 26.559 | 1.459 | sí | principal | sí |
| sutil | XGB-43 | 2023 | mensual | 90 | 3,679.053 | 4,199.635 | 0.638 | 3,455.610 | 4,349.382 | 3 | 9 | 18.220 | 1.259 | sí | principal | sí |
| sutil | XGB-43 | 2023 | interanual | 50 | 3,679.053 | 4,199.635 | 0.638 | 3,644.791 | 3,703.526 | 7 | 5 | 0.665 | 1.016 | sí | principal | sí |
| sutil | XGB-43 | 2023 | interanual | 60 | 3,679.053 | 4,199.635 | 0.638 | 3,353.749 | 4,004.356 | 6 | 6 | 8.842 | 1.194 | sí | principal | sí |
| sutil | XGB-43 | 2023 | interanual | 75 | 3,679.053 | 4,199.635 | 0.638 | 3,629.020 | 3,929.216 | 2 | 10 | 6.800 | 1.083 | sí | principal | sí |
| sutil | XGB-43 | 2023 | interanual | 90 | 3,679.053 | 4,199.635 | 0.638 | 3,679.053 | — | 0 | 12 | — | — | no | principal | sí |
| sutil | XGB-43 | 2024 | mensual | 50 | 5,466.153 | 7,289.730 | 0.995 | 5,075.555 | 6,247.350 | 4 | 8 | 14.292 | 1.231 | sí | principal | sí |
| sutil | XGB-43 | 2024 | mensual | 60 | 5,466.153 | 7,289.730 | 0.995 | 5,075.555 | 6,247.350 | 4 | 8 | 14.292 | 1.231 | sí | principal | sí |
| sutil | XGB-43 | 2024 | mensual | 75 | 5,466.153 | 7,289.730 | 0.995 | 5,466.153 | — | 0 | 12 | — | — | no | principal | sí |
| sutil | XGB-43 | 2024 | mensual | 90 | 5,466.153 | 7,289.730 | 0.995 | 5,466.153 | — | 0 | 12 | — | — | no | principal | sí |
| sutil | XGB-43 | 2024 | interanual | 50 | 5,466.153 | 7,289.730 | 0.995 | 5,810.410 | 5,294.025 | 8 | 4 | -3.149 | 0.911 | sí | principal | sí |
| sutil | XGB-43 | 2024 | interanual | 60 | 5,466.153 | 7,289.730 | 0.995 | 5,810.410 | 5,294.025 | 8 | 4 | -3.149 | 0.911 | sí | principal | sí |
| sutil | XGB-43 | 2024 | interanual | 75 | 5,466.153 | 7,289.730 | 0.995 | 5,810.410 | 5,294.025 | 8 | 4 | -3.149 | 0.911 | sí | principal | sí |
| sutil | XGB-43 | 2024 | interanual | 90 | 5,466.153 | 7,289.730 | 0.995 | 5,185.330 | 6,027.801 | 4 | 8 | 10.275 | 1.162 | sí | principal | sí |
| sutil | XGB-43 | 2025 | mensual | 50 | 5,917.849 | 7,128.433 | 1.021 | 5,345.372 | 6,719.316 | 5 | 7 | 13.543 | 1.257 | sí | principal | sí |
| sutil | XGB-43 | 2025 | mensual | 60 | 5,917.849 | 7,128.433 | 1.021 | 5,345.372 | 6,719.316 | 5 | 7 | 13.543 | 1.257 | sí | principal | sí |
| sutil | XGB-43 | 2025 | mensual | 75 | 5,917.849 | 7,128.433 | 1.021 | 5,087.786 | 8,408.037 | 3 | 9 | 42.079 | 1.653 | sí | principal | sí |
| sutil | XGB-43 | 2025 | mensual | 90 | 5,917.849 | 7,128.433 | 1.021 | 4,628.462 | 12,364.785 | 2 | 10 | 108.941 | 2.671 | sí | principal | sí |
| sutil | XGB-43 | 2025 | interanual | 50 | 5,917.849 | 7,128.433 | 1.021 | 6,613.976 | 4,525.594 | 4 | 8 | -23.526 | 0.684 | sí | principal | sí |
| sutil | XGB-43 | 2025 | interanual | 60 | 5,917.849 | 7,128.433 | 1.021 | 5,602.695 | 7,493.617 | 2 | 10 | 26.627 | 1.338 | sí | principal | sí |
| sutil | XGB-43 | 2025 | interanual | 75 | 5,917.849 | 7,128.433 | 1.021 | 5,917.849 | — | 0 | 12 | — | — | no | principal | sí |
| sutil | XGB-43 | 2025 | interanual | 90 | 5,917.849 | 7,128.433 | 1.021 | 5,917.849 | — | 0 | 12 | — | — | no | principal | sí |
| dulce | Naive | 2018 | mensual | 50 | 72.343 | 85.188 | — | 47.391 | 107.276 | 5 | 7 | 48.287 | 2.264 | sí | descriptivo_2018_2020 | no |
| dulce | Naive | 2018 | mensual | 60 | 72.343 | 85.188 | — | 52.532 | 111.965 | 4 | 8 | 54.769 | 2.131 | sí | descriptivo_2018_2020 | no |
| dulce | Naive | 2018 | mensual | 75 | 72.343 | 85.188 | — | 52.532 | 111.965 | 4 | 8 | 54.769 | 2.131 | sí | descriptivo_2018_2020 | no |
| dulce | Naive | 2018 | mensual | 90 | 72.343 | 85.188 | — | 66.880 | 99.660 | 2 | 10 | 37.760 | 1.490 | sí | descriptivo_2018_2020 | no |
| dulce | Naive | 2018 | interanual | 50 | 72.343 | 85.188 | — | 69.085 | 78.860 | 4 | 8 | 9.008 | 1.141 | sí | descriptivo_2018_2020 | no |
| dulce | Naive | 2018 | interanual | 60 | 72.343 | 85.188 | — | 72.110 | 73.510 | 2 | 10 | 1.613 | 1.019 | sí | descriptivo_2018_2020 | no |
| dulce | Naive | 2018 | interanual | 75 | 72.343 | 85.188 | — | 68.063 | 119.420 | 1 | 11 | 65.074 | 1.755 | no | descriptivo_2018_2020 | no |
| dulce | Naive | 2018 | interanual | 90 | 72.343 | 85.188 | — | 72.343 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| dulce | Naive | 2019 | mensual | 50 | 74.877 | 84.920 | 1.983 | 53.056 | 118.517 | 4 | 8 | 58.284 | 2.234 | sí | descriptivo_2018_2020 | no |
| dulce | Naive | 2019 | mensual | 60 | 74.877 | 84.920 | 1.983 | 53.056 | 118.517 | 4 | 8 | 58.284 | 2.234 | sí | descriptivo_2018_2020 | no |
| dulce | Naive | 2019 | mensual | 75 | 74.877 | 84.920 | 1.983 | 53.056 | 118.517 | 4 | 8 | 58.284 | 2.234 | sí | descriptivo_2018_2020 | no |
| dulce | Naive | 2019 | mensual | 90 | 74.877 | 84.920 | 1.983 | 53.056 | 118.517 | 4 | 8 | 58.284 | 2.234 | sí | descriptivo_2018_2020 | no |
| dulce | Naive | 2019 | interanual | 50 | 74.877 | 84.920 | 1.983 | 71.400 | 79.744 | 5 | 7 | 6.501 | 1.117 | sí | descriptivo_2018_2020 | no |
| dulce | Naive | 2019 | interanual | 60 | 74.877 | 84.920 | 1.983 | 71.037 | 82.555 | 4 | 8 | 10.255 | 1.162 | sí | descriptivo_2018_2020 | no |
| dulce | Naive | 2019 | interanual | 75 | 74.877 | 84.920 | 1.983 | 81.087 | 43.825 | 2 | 10 | -41.470 | 0.540 | sí | descriptivo_2018_2020 | no |
| dulce | Naive | 2019 | interanual | 90 | 74.877 | 84.920 | 1.983 | 74.877 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| dulce | Naive | 2020 | mensual | 50 | 66.683 | 83.960 | 2.029 | 20.180 | 113.186 | 6 | 6 | 69.737 | 5.609 | sí | descriptivo_2018_2020 | no |
| dulce | Naive | 2020 | mensual | 60 | 66.683 | 83.960 | 2.029 | 40.929 | 118.192 | 4 | 8 | 77.245 | 2.888 | sí | descriptivo_2018_2020 | no |
| dulce | Naive | 2020 | mensual | 75 | 66.683 | 83.960 | 2.029 | 40.929 | 118.192 | 4 | 8 | 77.245 | 2.888 | sí | descriptivo_2018_2020 | no |
| dulce | Naive | 2020 | mensual | 90 | 66.683 | 83.960 | 2.029 | 48.530 | 121.143 | 3 | 9 | 81.670 | 2.496 | sí | descriptivo_2018_2020 | no |
| dulce | Naive | 2020 | interanual | 50 | 66.683 | 83.960 | 2.029 | 70.181 | 59.687 | 4 | 8 | -10.492 | 0.850 | sí | descriptivo_2018_2020 | no |
| dulce | Naive | 2020 | interanual | 60 | 66.683 | 83.960 | 2.029 | 75.162 | 41.246 | 3 | 9 | -38.146 | 0.549 | sí | descriptivo_2018_2020 | no |
| dulce | Naive | 2020 | interanual | 75 | 66.683 | 83.960 | 2.029 | 66.683 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| dulce | Naive | 2020 | interanual | 90 | 66.683 | 83.960 | 2.029 | 66.683 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| dulce | Naive | 2021 | mensual | 50 | 67.831 | 81.770 | 2.139 | 36.915 | 111.114 | 5 | 7 | 63.810 | 3.010 | sí | principal | no |
| dulce | Naive | 2021 | mensual | 60 | 67.831 | 81.770 | 2.139 | 47.775 | 107.942 | 4 | 8 | 59.134 | 2.259 | sí | principal | no |
| dulce | Naive | 2021 | mensual | 75 | 67.831 | 81.770 | 2.139 | 50.231 | 120.630 | 3 | 9 | 77.839 | 2.401 | sí | principal | no |
| dulce | Naive | 2021 | mensual | 90 | 67.831 | 81.770 | 2.139 | 50.231 | 120.630 | 3 | 9 | 77.839 | 2.401 | sí | principal | no |
| dulce | Naive | 2021 | interanual | 50 | 67.831 | 81.770 | 2.139 | 74.089 | 55.315 | 4 | 8 | -18.452 | 0.747 | sí | principal | no |
| dulce | Naive | 2021 | interanual | 60 | 67.831 | 81.770 | 2.139 | 75.373 | 45.203 | 3 | 9 | -33.359 | 0.600 | sí | principal | no |
| dulce | Naive | 2021 | interanual | 75 | 67.831 | 81.770 | 2.139 | 73.608 | 38.944 | 2 | 10 | -42.586 | 0.529 | sí | principal | no |
| dulce | Naive | 2021 | interanual | 90 | 67.831 | 81.770 | 2.139 | 67.645 | 69.879 | 1 | 11 | 3.020 | 1.033 | no | principal | no |
| dulce | Naive | 2022 | mensual | 50 | 73.307 | 85.868 | 2.613 | 42.826 | 115.980 | 5 | 7 | 58.212 | 2.708 | sí | principal | no |
| dulce | Naive | 2022 | mensual | 60 | 73.307 | 85.868 | 2.613 | 42.826 | 115.980 | 5 | 7 | 58.212 | 2.708 | sí | principal | no |
| dulce | Naive | 2022 | mensual | 75 | 73.307 | 85.868 | 2.613 | 56.758 | 122.953 | 3 | 9 | 67.725 | 2.166 | sí | principal | no |
| dulce | Naive | 2022 | mensual | 90 | 73.307 | 85.868 | 2.613 | 71.458 | 93.640 | 1 | 11 | 27.737 | 1.310 | no | principal | no |
| dulce | Naive | 2022 | interanual | 50 | 73.307 | 85.868 | 2.613 | 63.772 | 82.842 | 6 | 6 | 13.007 | 1.299 | sí | principal | no |
| dulce | Naive | 2022 | interanual | 60 | 73.307 | 85.868 | 2.613 | 76.308 | 67.305 | 4 | 8 | -8.187 | 0.882 | sí | principal | no |
| dulce | Naive | 2022 | interanual | 75 | 73.307 | 85.868 | 2.613 | 73.771 | 70.985 | 2 | 10 | -3.167 | 0.962 | sí | principal | no |
| dulce | Naive | 2022 | interanual | 90 | 73.307 | 85.868 | 2.613 | 73.307 | — | 0 | 12 | — | — | no | principal | no |
| dulce | Naive | 2023 | mensual | 50 | 76.179 | 88.915 | 2.915 | 44.563 | 107.795 | 6 | 6 | 41.502 | 2.419 | sí | principal | no |
| dulce | Naive | 2023 | mensual | 60 | 76.179 | 88.915 | 2.915 | 50.909 | 126.720 | 4 | 8 | 66.345 | 2.489 | sí | principal | no |
| dulce | Naive | 2023 | mensual | 75 | 76.179 | 88.915 | 2.915 | 63.269 | 140.730 | 2 | 10 | 84.736 | 2.224 | sí | principal | no |
| dulce | Naive | 2023 | mensual | 90 | 76.179 | 88.915 | 2.915 | 76.179 | — | 0 | 12 | — | — | no | principal | no |
| dulce | Naive | 2023 | interanual | 50 | 76.179 | 88.915 | 2.915 | 77.154 | 71.304 | 2 | 10 | -6.400 | 0.924 | sí | principal | no |
| dulce | Naive | 2023 | interanual | 60 | 76.179 | 88.915 | 2.915 | 78.004 | 56.109 | 1 | 11 | -26.346 | 0.719 | no | principal | no |
| dulce | Naive | 2023 | interanual | 75 | 76.179 | 88.915 | 2.915 | 76.179 | — | 0 | 12 | — | — | no | principal | no |
| dulce | Naive | 2023 | interanual | 90 | 76.179 | 88.915 | 2.915 | 76.179 | — | 0 | 12 | — | — | no | principal | no |
| dulce | Naive | 2024 | mensual | 50 | 85.594 | 100.850 | 3.411 | 42.231 | 128.957 | 6 | 6 | 50.661 | 3.054 | sí | principal | no |
| dulce | Naive | 2024 | mensual | 60 | 85.594 | 100.850 | 3.411 | 45.447 | 141.800 | 5 | 7 | 65.666 | 3.120 | sí | principal | no |
| dulce | Naive | 2024 | mensual | 75 | 85.594 | 100.850 | 3.411 | 59.972 | 136.838 | 4 | 8 | 59.868 | 2.282 | sí | principal | no |
| dulce | Naive | 2024 | mensual | 90 | 85.594 | 100.850 | 3.411 | 84.456 | 98.110 | 1 | 11 | 14.623 | 1.162 | no | principal | no |
| dulce | Naive | 2024 | interanual | 50 | 85.594 | 100.850 | 3.411 | 49.598 | 88.866 | 11 | 1 | 3.823 | 1.792 | sí | principal | no |
| dulce | Naive | 2024 | interanual | 60 | 85.594 | 100.850 | 3.411 | 85.924 | 85.528 | 10 | 2 | -0.077 | 0.995 | sí | principal | no |
| dulce | Naive | 2024 | interanual | 75 | 85.594 | 100.850 | 3.411 | 65.706 | 92.223 | 9 | 3 | 7.745 | 1.404 | sí | principal | no |
| dulce | Naive | 2024 | interanual | 90 | 85.594 | 100.850 | 3.411 | 89.706 | 65.035 | 2 | 10 | -24.019 | 0.725 | sí | principal | no |
| dulce | Naive | 2025 | mensual | 50 | 84.701 | 97.712 | 3.651 | 49.320 | 120.082 | 6 | 6 | 41.772 | 2.435 | sí | principal | no |
| dulce | Naive | 2025 | mensual | 60 | 84.701 | 97.712 | 3.651 | 52.490 | 129.796 | 5 | 7 | 53.241 | 2.473 | sí | principal | no |
| dulce | Naive | 2025 | mensual | 75 | 84.701 | 97.712 | 3.651 | 66.849 | 138.257 | 3 | 9 | 63.229 | 2.068 | sí | principal | no |
| dulce | Naive | 2025 | mensual | 90 | 84.701 | 97.712 | 3.651 | 84.701 | — | 0 | 12 | — | — | no | principal | no |
| dulce | Naive | 2025 | interanual | 50 | 84.701 | 97.712 | 3.651 | 82.897 | 86.505 | 6 | 6 | 2.130 | 1.044 | sí | principal | no |
| dulce | Naive | 2025 | interanual | 60 | 84.701 | 97.712 | 3.651 | 75.259 | 97.920 | 5 | 7 | 15.607 | 1.301 | sí | principal | no |
| dulce | Naive | 2025 | interanual | 75 | 84.701 | 97.712 | 3.651 | 81.719 | 93.647 | 3 | 9 | 10.562 | 1.146 | sí | principal | no |
| dulce | Naive | 2025 | interanual | 90 | 84.701 | 97.712 | 3.651 | 88.665 | 41.090 | 1 | 11 | -51.488 | 0.463 | no | principal | no |
| dulce | Seasonal Naive | 2018 | mensual | 50 | 27.953 | 31.406 | — | 22.775 | 35.202 | 5 | 7 | 25.933 | 1.546 | sí | descriptivo_2018_2020 | no |
| dulce | Seasonal Naive | 2018 | mensual | 60 | 27.953 | 31.406 | — | 25.122 | 33.615 | 4 | 8 | 20.255 | 1.338 | sí | descriptivo_2018_2020 | no |
| dulce | Seasonal Naive | 2018 | mensual | 75 | 27.953 | 31.406 | — | 25.122 | 33.615 | 4 | 8 | 20.255 | 1.338 | sí | descriptivo_2018_2020 | no |
| dulce | Seasonal Naive | 2018 | mensual | 90 | 27.953 | 31.406 | — | 25.004 | 42.700 | 2 | 10 | 52.756 | 1.708 | sí | descriptivo_2018_2020 | no |
| dulce | Seasonal Naive | 2018 | interanual | 50 | 27.953 | 31.406 | — | 21.786 | 40.288 | 4 | 8 | 44.126 | 1.849 | sí | descriptivo_2018_2020 | no |
| dulce | Seasonal Naive | 2018 | interanual | 60 | 27.953 | 31.406 | — | 23.879 | 48.325 | 2 | 10 | 72.879 | 2.024 | sí | descriptivo_2018_2020 | no |
| dulce | Seasonal Naive | 2018 | interanual | 75 | 27.953 | 31.406 | — | 24.817 | 62.450 | 1 | 11 | 123.410 | 2.516 | no | descriptivo_2018_2020 | no |
| dulce | Seasonal Naive | 2018 | interanual | 90 | 27.953 | 31.406 | — | 27.953 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| dulce | Seasonal Naive | 2019 | mensual | 50 | 29.392 | 38.520 | 0.778 | 33.367 | 21.442 | 4 | 8 | -27.047 | 0.643 | sí | descriptivo_2018_2020 | no |
| dulce | Seasonal Naive | 2019 | mensual | 60 | 29.392 | 38.520 | 0.778 | 33.367 | 21.442 | 4 | 8 | -27.047 | 0.643 | sí | descriptivo_2018_2020 | no |
| dulce | Seasonal Naive | 2019 | mensual | 75 | 29.392 | 38.520 | 0.778 | 33.367 | 21.442 | 4 | 8 | -27.047 | 0.643 | sí | descriptivo_2018_2020 | no |
| dulce | Seasonal Naive | 2019 | mensual | 90 | 29.392 | 38.520 | 0.778 | 33.367 | 21.442 | 4 | 8 | -27.047 | 0.643 | sí | descriptivo_2018_2020 | no |
| dulce | Seasonal Naive | 2019 | interanual | 50 | 29.392 | 38.520 | 0.778 | 10.705 | 55.554 | 5 | 7 | 89.008 | 5.189 | sí | descriptivo_2018_2020 | no |
| dulce | Seasonal Naive | 2019 | interanual | 60 | 29.392 | 38.520 | 0.778 | 13.793 | 60.590 | 4 | 8 | 106.142 | 4.393 | sí | descriptivo_2018_2020 | no |
| dulce | Seasonal Naive | 2019 | interanual | 75 | 29.392 | 38.520 | 0.778 | 21.345 | 69.630 | 2 | 10 | 136.899 | 3.262 | sí | descriptivo_2018_2020 | no |
| dulce | Seasonal Naive | 2019 | interanual | 90 | 29.392 | 38.520 | 0.778 | 29.392 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| dulce | Seasonal Naive | 2020 | mensual | 50 | 17.121 | 21.907 | 0.521 | 18.882 | 15.361 | 6 | 6 | -10.283 | 0.814 | sí | descriptivo_2018_2020 | no |
| dulce | Seasonal Naive | 2020 | mensual | 60 | 17.121 | 21.907 | 0.521 | 21.304 | 8.755 | 4 | 8 | -48.863 | 0.411 | sí | descriptivo_2018_2020 | no |
| dulce | Seasonal Naive | 2020 | mensual | 75 | 17.121 | 21.907 | 0.521 | 21.304 | 8.755 | 4 | 8 | -48.863 | 0.411 | sí | descriptivo_2018_2020 | no |
| dulce | Seasonal Naive | 2020 | mensual | 90 | 17.121 | 21.907 | 0.521 | 19.017 | 11.434 | 3 | 9 | -33.219 | 0.601 | sí | descriptivo_2018_2020 | no |
| dulce | Seasonal Naive | 2020 | interanual | 50 | 17.121 | 21.907 | 0.521 | 9.957 | 31.448 | 4 | 8 | 83.681 | 3.158 | sí | descriptivo_2018_2020 | no |
| dulce | Seasonal Naive | 2020 | interanual | 60 | 17.121 | 21.907 | 0.521 | 12.089 | 32.217 | 3 | 9 | 88.173 | 2.665 | sí | descriptivo_2018_2020 | no |
| dulce | Seasonal Naive | 2020 | interanual | 75 | 17.121 | 21.907 | 0.521 | 17.121 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| dulce | Seasonal Naive | 2020 | interanual | 90 | 17.121 | 21.907 | 0.521 | 17.121 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| dulce | Seasonal Naive | 2021 | mensual | 50 | 18.417 | 20.830 | 0.581 | 18.351 | 18.508 | 5 | 7 | 0.495 | 1.009 | sí | principal | no |
| dulce | Seasonal Naive | 2021 | mensual | 60 | 18.417 | 20.830 | 0.581 | 17.674 | 19.902 | 4 | 8 | 8.068 | 1.126 | sí | principal | no |
| dulce | Seasonal Naive | 2021 | mensual | 75 | 18.417 | 20.830 | 0.581 | 19.234 | 15.963 | 3 | 9 | -13.321 | 0.830 | sí | principal | no |
| dulce | Seasonal Naive | 2021 | mensual | 90 | 18.417 | 20.830 | 0.581 | 19.234 | 15.963 | 3 | 9 | -13.321 | 0.830 | sí | principal | no |
| dulce | Seasonal Naive | 2021 | interanual | 50 | 18.417 | 20.830 | 0.581 | 13.506 | 28.238 | 4 | 8 | 53.328 | 2.091 | sí | principal | no |
| dulce | Seasonal Naive | 2021 | interanual | 60 | 18.417 | 20.830 | 0.581 | 13.814 | 32.224 | 3 | 9 | 74.971 | 2.333 | sí | principal | no |
| dulce | Seasonal Naive | 2021 | interanual | 75 | 18.417 | 20.830 | 0.581 | 16.403 | 28.485 | 2 | 10 | 54.670 | 1.737 | sí | principal | no |
| dulce | Seasonal Naive | 2021 | interanual | 90 | 18.417 | 20.830 | 0.581 | 17.207 | 31.720 | 1 | 11 | 72.236 | 1.843 | no | principal | no |
| dulce | Seasonal Naive | 2022 | mensual | 50 | 19.921 | 23.410 | 0.710 | 18.484 | 21.932 | 5 | 7 | 10.096 | 1.187 | sí | principal | no |
| dulce | Seasonal Naive | 2022 | mensual | 60 | 19.921 | 23.410 | 0.710 | 18.484 | 21.932 | 5 | 7 | 10.096 | 1.187 | sí | principal | no |
| dulce | Seasonal Naive | 2022 | mensual | 75 | 19.921 | 23.410 | 0.710 | 16.060 | 31.504 | 3 | 9 | 58.144 | 1.962 | sí | principal | no |
| dulce | Seasonal Naive | 2022 | mensual | 90 | 19.921 | 23.410 | 0.710 | 18.710 | 33.240 | 1 | 11 | 66.860 | 1.777 | no | principal | no |
| dulce | Seasonal Naive | 2022 | interanual | 50 | 19.921 | 23.410 | 0.710 | 9.730 | 30.112 | 6 | 6 | 51.157 | 3.095 | sí | principal | no |
| dulce | Seasonal Naive | 2022 | interanual | 60 | 19.921 | 23.410 | 0.710 | 15.881 | 28.000 | 4 | 8 | 40.556 | 1.763 | sí | principal | no |
| dulce | Seasonal Naive | 2022 | interanual | 75 | 19.921 | 23.410 | 0.710 | 17.386 | 32.595 | 2 | 10 | 63.622 | 1.875 | sí | principal | no |
| dulce | Seasonal Naive | 2022 | interanual | 90 | 19.921 | 23.410 | 0.710 | 19.921 | — | 0 | 12 | — | — | no | principal | no |
| dulce | Seasonal Naive | 2023 | mensual | 50 | 11.841 | 14.780 | 0.453 | 16.165 | 7.518 | 6 | 6 | -36.509 | 0.465 | sí | principal | no |
| dulce | Seasonal Naive | 2023 | mensual | 60 | 11.841 | 14.780 | 0.453 | 14.852 | 5.820 | 4 | 8 | -50.851 | 0.392 | sí | principal | no |
| dulce | Seasonal Naive | 2023 | mensual | 75 | 11.841 | 14.780 | 0.453 | 12.732 | 7.389 | 2 | 10 | -37.597 | 0.580 | sí | principal | no |
| dulce | Seasonal Naive | 2023 | mensual | 90 | 11.841 | 14.780 | 0.453 | 11.841 | — | 0 | 12 | — | — | no | principal | no |
| dulce | Seasonal Naive | 2023 | interanual | 50 | 11.841 | 14.780 | 0.453 | 9.656 | 22.770 | 2 | 10 | 92.290 | 2.358 | sí | principal | no |
| dulce | Seasonal Naive | 2023 | interanual | 60 | 11.841 | 14.780 | 0.453 | 10.708 | 24.310 | 1 | 11 | 105.295 | 2.270 | no | principal | no |
| dulce | Seasonal Naive | 2023 | interanual | 75 | 11.841 | 14.780 | 0.453 | 11.841 | — | 0 | 12 | — | — | no | principal | no |
| dulce | Seasonal Naive | 2023 | interanual | 90 | 11.841 | 14.780 | 0.453 | 11.841 | — | 0 | 12 | — | — | no | principal | no |
| dulce | Seasonal Naive | 2024 | mensual | 50 | 41.808 | 50.237 | 1.666 | 51.021 | 32.595 | 6 | 6 | -22.036 | 0.639 | sí | principal | no |
| dulce | Seasonal Naive | 2024 | mensual | 60 | 41.808 | 50.237 | 1.666 | 47.021 | 34.510 | 5 | 7 | -17.456 | 0.734 | sí | principal | no |
| dulce | Seasonal Naive | 2024 | mensual | 75 | 41.808 | 50.237 | 1.666 | 46.127 | 33.170 | 4 | 8 | -20.661 | 0.719 | sí | principal | no |
| dulce | Seasonal Naive | 2024 | mensual | 90 | 41.808 | 50.237 | 1.666 | 43.252 | 25.930 | 1 | 11 | -37.979 | 0.600 | no | principal | no |
| dulce | Seasonal Naive | 2024 | interanual | 50 | 41.808 | 50.237 | 1.666 | 12.648 | 44.459 | 11 | 1 | 6.341 | 3.515 | sí | principal | no |
| dulce | Seasonal Naive | 2024 | interanual | 60 | 41.808 | 50.237 | 1.666 | 18.384 | 46.493 | 10 | 2 | 11.205 | 2.529 | sí | principal | no |
| dulce | Seasonal Naive | 2024 | interanual | 75 | 41.808 | 50.237 | 1.666 | 28.169 | 46.354 | 9 | 3 | 10.874 | 1.646 | sí | principal | no |
| dulce | Seasonal Naive | 2024 | interanual | 90 | 41.808 | 50.237 | 1.666 | 32.420 | 88.750 | 2 | 10 | 112.279 | 2.738 | sí | principal | no |
| dulce | Seasonal Naive | 2025 | mensual | 50 | 30.528 | 35.440 | 1.316 | 39.829 | 21.227 | 6 | 6 | -30.468 | 0.533 | sí | principal | no |
| dulce | Seasonal Naive | 2025 | mensual | 60 | 30.528 | 35.440 | 1.316 | 35.365 | 23.756 | 5 | 7 | -22.182 | 0.672 | sí | principal | no |
| dulce | Seasonal Naive | 2025 | mensual | 75 | 30.528 | 35.440 | 1.316 | 32.073 | 25.893 | 3 | 9 | -15.182 | 0.807 | sí | principal | no |
| dulce | Seasonal Naive | 2025 | mensual | 90 | 30.528 | 35.440 | 1.316 | 30.528 | — | 0 | 12 | — | — | no | principal | no |
| dulce | Seasonal Naive | 2025 | interanual | 50 | 30.528 | 35.440 | 1.316 | 17.334 | 43.722 | 6 | 6 | 43.221 | 2.522 | sí | principal | no |
| dulce | Seasonal Naive | 2025 | interanual | 60 | 30.528 | 35.440 | 1.316 | 20.406 | 44.699 | 5 | 7 | 46.419 | 2.190 | sí | principal | no |
| dulce | Seasonal Naive | 2025 | interanual | 75 | 30.528 | 35.440 | 1.316 | 25.267 | 46.311 | 3 | 9 | 51.699 | 1.833 | sí | principal | no |
| dulce | Seasonal Naive | 2025 | interanual | 90 | 30.528 | 35.440 | 1.316 | 27.361 | 65.360 | 1 | 11 | 114.099 | 2.389 | no | principal | no |
| dulce | Chronos | 2018 | mensual | 50 | 31.846 | 38.053 | — | 26.689 | 39.066 | 5 | 7 | 22.671 | 1.464 | sí | descriptivo_2018_2020 | no |
| dulce | Chronos | 2018 | mensual | 60 | 31.846 | 38.053 | — | 23.443 | 48.654 | 4 | 8 | 52.778 | 2.075 | sí | descriptivo_2018_2020 | no |
| dulce | Chronos | 2018 | mensual | 75 | 31.846 | 38.053 | — | 23.443 | 48.654 | 4 | 8 | 52.778 | 2.075 | sí | descriptivo_2018_2020 | no |
| dulce | Chronos | 2018 | mensual | 90 | 31.846 | 38.053 | — | 28.188 | 50.139 | 2 | 10 | 57.440 | 1.779 | sí | descriptivo_2018_2020 | no |
| dulce | Chronos | 2018 | interanual | 50 | 31.846 | 38.053 | — | 29.852 | 35.835 | 4 | 8 | 12.524 | 1.200 | sí | descriptivo_2018_2020 | no |
| dulce | Chronos | 2018 | interanual | 60 | 31.846 | 38.053 | — | 28.791 | 47.126 | 2 | 10 | 47.978 | 1.637 | sí | descriptivo_2018_2020 | no |
| dulce | Chronos | 2018 | interanual | 75 | 31.846 | 38.053 | — | 30.023 | 51.905 | 1 | 11 | 62.986 | 1.729 | no | descriptivo_2018_2020 | no |
| dulce | Chronos | 2018 | interanual | 90 | 31.846 | 38.053 | — | 31.846 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| dulce | Chronos | 2019 | mensual | 50 | 33.468 | 36.537 | 0.886 | 32.228 | 35.949 | 4 | 8 | 7.411 | 1.115 | sí | descriptivo_2018_2020 | no |
| dulce | Chronos | 2019 | mensual | 60 | 33.468 | 36.537 | 0.886 | 32.228 | 35.949 | 4 | 8 | 7.411 | 1.115 | sí | descriptivo_2018_2020 | no |
| dulce | Chronos | 2019 | mensual | 75 | 33.468 | 36.537 | 0.886 | 32.228 | 35.949 | 4 | 8 | 7.411 | 1.115 | sí | descriptivo_2018_2020 | no |
| dulce | Chronos | 2019 | mensual | 90 | 33.468 | 36.537 | 0.886 | 32.228 | 35.949 | 4 | 8 | 7.411 | 1.115 | sí | descriptivo_2018_2020 | no |
| dulce | Chronos | 2019 | interanual | 50 | 33.468 | 36.537 | 0.886 | 31.420 | 36.336 | 5 | 7 | 8.568 | 1.156 | sí | descriptivo_2018_2020 | no |
| dulce | Chronos | 2019 | interanual | 60 | 33.468 | 36.537 | 0.886 | 31.099 | 38.207 | 4 | 8 | 14.159 | 1.229 | sí | descriptivo_2018_2020 | no |
| dulce | Chronos | 2019 | interanual | 75 | 33.468 | 36.537 | 0.886 | 33.958 | 31.019 | 2 | 10 | -7.318 | 0.913 | sí | descriptivo_2018_2020 | no |
| dulce | Chronos | 2019 | interanual | 90 | 33.468 | 36.537 | 0.886 | 33.468 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| dulce | Chronos | 2020 | mensual | 50 | 28.763 | 33.984 | 0.875 | 19.517 | 38.010 | 6 | 6 | 32.148 | 1.948 | sí | descriptivo_2018_2020 | no |
| dulce | Chronos | 2020 | mensual | 60 | 28.763 | 33.984 | 0.875 | 29.271 | 27.749 | 4 | 8 | -3.527 | 0.948 | sí | descriptivo_2018_2020 | no |
| dulce | Chronos | 2020 | mensual | 75 | 28.763 | 33.984 | 0.875 | 29.271 | 27.749 | 4 | 8 | -3.527 | 0.948 | sí | descriptivo_2018_2020 | no |
| dulce | Chronos | 2020 | mensual | 90 | 28.763 | 33.984 | 0.875 | 29.915 | 25.307 | 3 | 9 | -12.016 | 0.846 | sí | descriptivo_2018_2020 | no |
| dulce | Chronos | 2020 | interanual | 50 | 28.763 | 33.984 | 0.875 | 22.999 | 40.292 | 4 | 8 | 40.080 | 1.752 | sí | descriptivo_2018_2020 | no |
| dulce | Chronos | 2020 | interanual | 60 | 28.763 | 33.984 | 0.875 | 27.116 | 33.705 | 3 | 9 | 17.182 | 1.243 | sí | descriptivo_2018_2020 | no |
| dulce | Chronos | 2020 | interanual | 75 | 28.763 | 33.984 | 0.875 | 28.763 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| dulce | Chronos | 2020 | interanual | 90 | 28.763 | 33.984 | 0.875 | 28.763 | — | 0 | 12 | — | — | no | descriptivo_2018_2020 | no |
| dulce | Chronos | 2021 | mensual | 50 | 19.185 | 27.026 | 0.605 | 12.101 | 29.101 | 5 | 7 | 51.690 | 2.405 | sí | principal | no |
| dulce | Chronos | 2021 | mensual | 60 | 19.185 | 27.026 | 0.605 | 18.609 | 20.336 | 4 | 8 | 6.003 | 1.093 | sí | principal | no |
| dulce | Chronos | 2021 | mensual | 75 | 19.185 | 27.026 | 0.605 | 16.891 | 26.066 | 3 | 9 | 35.869 | 1.543 | sí | principal | no |
| dulce | Chronos | 2021 | mensual | 90 | 19.185 | 27.026 | 0.605 | 16.891 | 26.066 | 3 | 9 | 35.869 | 1.543 | sí | principal | no |
| dulce | Chronos | 2021 | interanual | 50 | 19.185 | 27.026 | 0.605 | 24.570 | 8.413 | 4 | 8 | -56.146 | 0.342 | sí | principal | no |
| dulce | Chronos | 2021 | interanual | 60 | 19.185 | 27.026 | 0.605 | 24.411 | 3.507 | 3 | 9 | -81.720 | 0.144 | sí | principal | no |
| dulce | Chronos | 2021 | interanual | 75 | 19.185 | 27.026 | 0.605 | 22.680 | 1.707 | 2 | 10 | -91.104 | 0.075 | sí | principal | no |
| dulce | Chronos | 2021 | interanual | 90 | 19.185 | 27.026 | 0.605 | 20.643 | 3.147 | 1 | 11 | -83.596 | 0.152 | no | principal | no |
| dulce | Chronos | 2022 | mensual | 50 | 30.030 | 34.317 | 1.070 | 22.036 | 41.222 | 5 | 7 | 37.267 | 1.871 | sí | principal | no |
| dulce | Chronos | 2022 | mensual | 60 | 30.030 | 34.317 | 1.070 | 22.036 | 41.222 | 5 | 7 | 37.267 | 1.871 | sí | principal | no |
| dulce | Chronos | 2022 | mensual | 75 | 30.030 | 34.317 | 1.070 | 23.730 | 48.932 | 3 | 9 | 62.944 | 2.062 | sí | principal | no |
| dulce | Chronos | 2022 | mensual | 90 | 30.030 | 34.317 | 1.070 | 28.205 | 50.112 | 1 | 11 | 66.871 | 1.777 | no | principal | no |
| dulce | Chronos | 2022 | interanual | 50 | 30.030 | 34.317 | 1.070 | 23.796 | 36.265 | 6 | 6 | 20.761 | 1.524 | sí | principal | no |
| dulce | Chronos | 2022 | interanual | 60 | 30.030 | 34.317 | 1.070 | 29.409 | 31.273 | 4 | 8 | 4.139 | 1.063 | sí | principal | no |
| dulce | Chronos | 2022 | interanual | 75 | 30.030 | 34.317 | 1.070 | 28.865 | 35.857 | 2 | 10 | 19.402 | 1.242 | sí | principal | no |
| dulce | Chronos | 2022 | interanual | 90 | 30.030 | 34.317 | 1.070 | 30.030 | — | 0 | 12 | — | — | no | principal | no |
| dulce | Chronos | 2023 | mensual | 50 | 30.397 | 35.232 | 1.163 | 21.805 | 38.990 | 6 | 6 | 28.268 | 1.788 | sí | principal | no |
| dulce | Chronos | 2023 | mensual | 60 | 30.397 | 35.232 | 1.163 | 22.710 | 45.772 | 4 | 8 | 50.581 | 2.016 | sí | principal | no |
| dulce | Chronos | 2023 | mensual | 75 | 30.397 | 35.232 | 1.163 | 27.716 | 43.803 | 2 | 10 | 44.103 | 1.580 | sí | principal | no |
| dulce | Chronos | 2023 | mensual | 90 | 30.397 | 35.232 | 1.163 | 30.397 | — | 0 | 12 | — | — | no | principal | no |
| dulce | Chronos | 2023 | interanual | 50 | 30.397 | 35.232 | 1.163 | 30.948 | 27.642 | 2 | 10 | -9.064 | 0.893 | sí | principal | no |
| dulce | Chronos | 2023 | interanual | 60 | 30.397 | 35.232 | 1.163 | 31.989 | 12.891 | 1 | 11 | -57.591 | 0.403 | no | principal | no |
| dulce | Chronos | 2023 | interanual | 75 | 30.397 | 35.232 | 1.163 | 30.397 | — | 0 | 12 | — | — | no | principal | no |
| dulce | Chronos | 2023 | interanual | 90 | 30.397 | 35.232 | 1.163 | 30.397 | — | 0 | 12 | — | — | no | principal | no |
| dulce | Chronos | 2024 | mensual | 50 | 39.925 | 50.089 | 1.591 | 35.032 | 44.818 | 6 | 6 | 12.256 | 1.279 | sí | principal | no |
| dulce | Chronos | 2024 | mensual | 60 | 39.925 | 50.089 | 1.591 | 31.288 | 52.016 | 5 | 7 | 30.286 | 1.663 | sí | principal | no |
| dulce | Chronos | 2024 | mensual | 75 | 39.925 | 50.089 | 1.591 | 31.118 | 57.538 | 4 | 8 | 44.117 | 1.849 | sí | principal | no |
| dulce | Chronos | 2024 | mensual | 90 | 39.925 | 50.089 | 1.591 | 37.936 | 61.804 | 1 | 11 | 54.800 | 1.629 | no | principal | no |
| dulce | Chronos | 2024 | interanual | 50 | 39.925 | 50.089 | 1.591 | 45.882 | 39.383 | 11 | 1 | -1.356 | 0.858 | sí | principal | no |
| dulce | Chronos | 2024 | interanual | 60 | 39.925 | 50.089 | 1.591 | 45.067 | 38.896 | 10 | 2 | -2.576 | 0.863 | sí | principal | no |
| dulce | Chronos | 2024 | interanual | 75 | 39.925 | 50.089 | 1.591 | 32.994 | 42.235 | 9 | 3 | 5.786 | 1.280 | sí | principal | no |
| dulce | Chronos | 2024 | interanual | 90 | 39.925 | 50.089 | 1.591 | 37.609 | 51.502 | 2 | 10 | 28.998 | 1.369 | sí | principal | no |
| dulce | Chronos | 2025 | mensual | 50 | 34.557 | 39.077 | 1.489 | 27.379 | 41.735 | 6 | 6 | 20.772 | 1.524 | sí | principal | no |
| dulce | Chronos | 2025 | mensual | 60 | 34.557 | 39.077 | 1.489 | 25.815 | 46.797 | 5 | 7 | 35.419 | 1.813 | sí | principal | no |
| dulce | Chronos | 2025 | mensual | 75 | 34.557 | 39.077 | 1.489 | 26.051 | 60.076 | 3 | 9 | 73.845 | 2.306 | sí | principal | no |
| dulce | Chronos | 2025 | mensual | 90 | 34.557 | 39.077 | 1.489 | 34.557 | — | 0 | 12 | — | — | no | principal | no |
| dulce | Chronos | 2025 | interanual | 50 | 34.557 | 39.077 | 1.489 | 38.969 | 30.146 | 6 | 6 | -12.766 | 0.774 | sí | principal | no |
| dulce | Chronos | 2025 | interanual | 60 | 34.557 | 39.077 | 1.489 | 36.233 | 32.211 | 5 | 7 | -6.789 | 0.889 | sí | principal | no |
| dulce | Chronos | 2025 | interanual | 75 | 34.557 | 39.077 | 1.489 | 37.645 | 25.295 | 3 | 9 | -26.803 | 0.672 | sí | principal | no |
| dulce | Chronos | 2025 | interanual | 90 | 34.557 | 39.077 | 1.489 | 35.804 | 20.839 | 1 | 11 | -39.696 | 0.582 | no | principal | no |
| dulce | SARIMA | 2021 | mensual | 50 | 13.651 | 17.717 | 0.431 | 14.836 | 11.993 | 5 | 7 | -12.149 | 0.808 | sí | principal | no |
| dulce | SARIMA | 2021 | mensual | 60 | 13.651 | 17.717 | 0.431 | 14.410 | 12.134 | 4 | 8 | -11.115 | 0.842 | sí | principal | no |
| dulce | SARIMA | 2021 | mensual | 75 | 13.651 | 17.717 | 0.431 | 16.770 | 4.293 | 3 | 9 | -68.551 | 0.256 | sí | principal | no |
| dulce | SARIMA | 2021 | mensual | 90 | 13.651 | 17.717 | 0.431 | 16.770 | 4.293 | 3 | 9 | -68.551 | 0.256 | sí | principal | no |
| dulce | SARIMA | 2021 | interanual | 50 | 13.651 | 17.717 | 0.431 | 11.332 | 18.289 | 4 | 8 | 33.978 | 1.614 | sí | principal | no |
| dulce | SARIMA | 2021 | interanual | 60 | 13.651 | 17.717 | 0.431 | 10.658 | 22.631 | 3 | 9 | 65.784 | 2.123 | sí | principal | no |
| dulce | SARIMA | 2021 | interanual | 75 | 13.651 | 17.717 | 0.431 | 12.565 | 19.084 | 2 | 10 | 39.798 | 1.519 | sí | principal | no |
| dulce | SARIMA | 2021 | interanual | 90 | 13.651 | 17.717 | 0.431 | 11.651 | 35.656 | 1 | 11 | 161.193 | 3.060 | no | principal | no |
| dulce | SARIMA | 2022 | mensual | 50 | 12.397 | 15.159 | 0.442 | 14.001 | 10.150 | 5 | 7 | -18.122 | 0.725 | sí | principal | no |
| dulce | SARIMA | 2022 | mensual | 60 | 12.397 | 15.159 | 0.442 | 14.001 | 10.150 | 5 | 7 | -18.122 | 0.725 | sí | principal | no |
| dulce | SARIMA | 2022 | mensual | 75 | 12.397 | 15.159 | 0.442 | 12.218 | 12.932 | 3 | 9 | 4.317 | 1.058 | sí | principal | no |
| dulce | SARIMA | 2022 | mensual | 90 | 12.397 | 15.159 | 0.442 | 11.967 | 17.125 | 1 | 11 | 38.140 | 1.431 | no | principal | no |
| dulce | SARIMA | 2022 | interanual | 50 | 12.397 | 15.159 | 0.442 | 6.923 | 17.870 | 6 | 6 | 44.154 | 2.581 | sí | principal | no |
| dulce | SARIMA | 2022 | interanual | 60 | 12.397 | 15.159 | 0.442 | 8.906 | 19.378 | 4 | 8 | 56.320 | 2.176 | sí | principal | no |
| dulce | SARIMA | 2022 | interanual | 75 | 12.397 | 15.159 | 0.442 | 10.171 | 23.522 | 2 | 10 | 89.750 | 2.313 | sí | principal | no |
| dulce | SARIMA | 2022 | interanual | 90 | 12.397 | 15.159 | 0.442 | 12.397 | — | 0 | 12 | — | — | no | principal | no |
| dulce | SARIMA | 2023 | mensual | 50 | 18.760 | 21.181 | 0.718 | 23.787 | 13.733 | 6 | 6 | -26.797 | 0.577 | sí | principal | no |
| dulce | SARIMA | 2023 | mensual | 60 | 18.760 | 21.181 | 0.718 | 22.023 | 12.233 | 4 | 8 | -34.791 | 0.555 | sí | principal | no |
| dulce | SARIMA | 2023 | mensual | 75 | 18.760 | 21.181 | 0.718 | 20.758 | 8.770 | 2 | 10 | -53.250 | 0.423 | sí | principal | no |
| dulce | SARIMA | 2023 | mensual | 90 | 18.760 | 21.181 | 0.718 | 18.760 | — | 0 | 12 | — | — | no | principal | no |
| dulce | SARIMA | 2023 | interanual | 50 | 18.760 | 21.181 | 0.718 | 17.084 | 27.142 | 2 | 10 | 44.677 | 1.589 | sí | principal | no |
| dulce | SARIMA | 2023 | interanual | 60 | 18.760 | 21.181 | 0.718 | 17.296 | 34.863 | 1 | 11 | 85.834 | 2.016 | no | principal | no |
| dulce | SARIMA | 2023 | interanual | 75 | 18.760 | 21.181 | 0.718 | 18.760 | — | 0 | 12 | — | — | no | principal | no |
| dulce | SARIMA | 2023 | interanual | 90 | 18.760 | 21.181 | 0.718 | 18.760 | — | 0 | 12 | — | — | no | principal | no |
| dulce | SARIMA | 2024 | mensual | 50 | 25.486 | 34.446 | 1.016 | 32.069 | 18.903 | 6 | 6 | -25.830 | 0.589 | sí | principal | no |
| dulce | SARIMA | 2024 | mensual | 60 | 25.486 | 34.446 | 1.016 | 27.550 | 22.595 | 5 | 7 | -11.341 | 0.820 | sí | principal | no |
| dulce | SARIMA | 2024 | mensual | 75 | 25.486 | 34.446 | 1.016 | 25.023 | 26.411 | 4 | 8 | 3.629 | 1.055 | sí | principal | no |
| dulce | SARIMA | 2024 | mensual | 90 | 25.486 | 34.446 | 1.016 | 25.660 | 23.571 | 1 | 11 | -7.515 | 0.919 | no | principal | no |
| dulce | SARIMA | 2024 | interanual | 50 | 25.486 | 34.446 | 1.016 | 19.494 | 26.031 | 11 | 1 | 2.137 | 1.335 | sí | principal | no |
| dulce | SARIMA | 2024 | interanual | 60 | 25.486 | 34.446 | 1.016 | 12.715 | 28.040 | 10 | 2 | 10.022 | 2.205 | sí | principal | no |
| dulce | SARIMA | 2024 | interanual | 75 | 25.486 | 34.446 | 1.016 | 21.095 | 26.949 | 9 | 3 | 5.743 | 1.278 | sí | principal | no |
| dulce | SARIMA | 2024 | interanual | 90 | 25.486 | 34.446 | 1.016 | 19.082 | 57.503 | 2 | 10 | 125.626 | 3.013 | sí | principal | no |
| dulce | SARIMA | 2025 | mensual | 50 | 21.767 | 31.616 | 0.938 | 26.345 | 17.188 | 6 | 6 | -21.035 | 0.652 | sí | principal | no |
| dulce | SARIMA | 2025 | mensual | 60 | 21.767 | 31.616 | 0.938 | 28.980 | 11.668 | 5 | 7 | -46.395 | 0.403 | sí | principal | no |
| dulce | SARIMA | 2025 | mensual | 75 | 21.767 | 31.616 | 0.938 | 25.154 | 11.604 | 3 | 9 | -46.691 | 0.461 | sí | principal | no |
| dulce | SARIMA | 2025 | mensual | 90 | 21.767 | 31.616 | 0.938 | 21.767 | — | 0 | 12 | — | — | no | principal | no |
| dulce | SARIMA | 2025 | interanual | 50 | 21.767 | 31.616 | 0.938 | 13.342 | 30.191 | 6 | 6 | 38.704 | 2.263 | sí | principal | no |
| dulce | SARIMA | 2025 | interanual | 60 | 21.767 | 31.616 | 0.938 | 13.909 | 32.767 | 5 | 7 | 50.539 | 2.356 | sí | principal | no |
| dulce | SARIMA | 2025 | interanual | 75 | 21.767 | 31.616 | 0.938 | 16.745 | 36.831 | 3 | 9 | 69.207 | 2.199 | sí | principal | no |
| dulce | SARIMA | 2025 | interanual | 90 | 21.767 | 31.616 | 0.938 | 15.891 | 86.396 | 1 | 11 | 296.916 | 5.437 | no | principal | no |
| dulce | SARIMA-sel | 2021 | mensual | 50 | 27.938 | 32.913 | 0.881 | 24.867 | 32.237 | 5 | 7 | 15.388 | 1.296 | sí | principal | no |
| dulce | SARIMA-sel | 2021 | mensual | 60 | 27.938 | 32.913 | 0.881 | 27.373 | 29.070 | 4 | 8 | 4.050 | 1.062 | sí | principal | no |
| dulce | SARIMA-sel | 2021 | mensual | 75 | 27.938 | 32.913 | 0.881 | 25.631 | 34.859 | 3 | 9 | 24.773 | 1.360 | sí | principal | no |
| dulce | SARIMA-sel | 2021 | mensual | 90 | 27.938 | 32.913 | 0.881 | 25.631 | 34.859 | 3 | 9 | 24.773 | 1.360 | sí | principal | no |
| dulce | SARIMA-sel | 2021 | interanual | 50 | 27.938 | 32.913 | 0.881 | 29.583 | 24.650 | 4 | 8 | -11.771 | 0.833 | sí | principal | no |
| dulce | SARIMA-sel | 2021 | interanual | 60 | 27.938 | 32.913 | 0.881 | 31.107 | 18.431 | 3 | 9 | -34.031 | 0.592 | sí | principal | no |
| dulce | SARIMA-sel | 2021 | interanual | 75 | 27.938 | 32.913 | 0.881 | 28.462 | 25.322 | 2 | 10 | -9.365 | 0.890 | sí | principal | no |
| dulce | SARIMA-sel | 2021 | interanual | 90 | 27.938 | 32.913 | 0.881 | 29.414 | 11.701 | 1 | 11 | -58.120 | 0.398 | no | principal | no |
| dulce | SARIMA-sel | 2022 | mensual | 50 | 12.397 | 15.159 | 0.442 | 14.001 | 10.150 | 5 | 7 | -18.122 | 0.725 | sí | principal | no |
| dulce | SARIMA-sel | 2022 | mensual | 60 | 12.397 | 15.159 | 0.442 | 14.001 | 10.150 | 5 | 7 | -18.122 | 0.725 | sí | principal | no |
| dulce | SARIMA-sel | 2022 | mensual | 75 | 12.397 | 15.159 | 0.442 | 12.218 | 12.932 | 3 | 9 | 4.317 | 1.058 | sí | principal | no |
| dulce | SARIMA-sel | 2022 | mensual | 90 | 12.397 | 15.159 | 0.442 | 11.967 | 17.125 | 1 | 11 | 38.140 | 1.431 | no | principal | no |
| dulce | SARIMA-sel | 2022 | interanual | 50 | 12.397 | 15.159 | 0.442 | 6.923 | 17.870 | 6 | 6 | 44.154 | 2.581 | sí | principal | no |
| dulce | SARIMA-sel | 2022 | interanual | 60 | 12.397 | 15.159 | 0.442 | 8.906 | 19.378 | 4 | 8 | 56.320 | 2.176 | sí | principal | no |
| dulce | SARIMA-sel | 2022 | interanual | 75 | 12.397 | 15.159 | 0.442 | 10.171 | 23.522 | 2 | 10 | 89.750 | 2.313 | sí | principal | no |
| dulce | SARIMA-sel | 2022 | interanual | 90 | 12.397 | 15.159 | 0.442 | 12.397 | — | 0 | 12 | — | — | no | principal | no |
| dulce | SARIMA-sel | 2023 | mensual | 50 | 17.429 | 19.930 | 0.667 | 22.373 | 12.484 | 6 | 6 | -28.368 | 0.558 | sí | principal | no |
| dulce | SARIMA-sel | 2023 | mensual | 60 | 17.429 | 19.930 | 0.667 | 20.833 | 10.620 | 4 | 8 | -39.063 | 0.510 | sí | principal | no |
| dulce | SARIMA-sel | 2023 | mensual | 75 | 17.429 | 19.930 | 0.667 | 19.407 | 7.537 | 2 | 10 | -56.756 | 0.388 | sí | principal | no |
| dulce | SARIMA-sel | 2023 | mensual | 90 | 17.429 | 19.930 | 0.667 | 17.429 | — | 0 | 12 | — | — | no | principal | no |
| dulce | SARIMA-sel | 2023 | interanual | 50 | 17.429 | 19.930 | 0.667 | 15.616 | 26.490 | 2 | 10 | 51.992 | 1.696 | sí | principal | no |
| dulce | SARIMA-sel | 2023 | interanual | 60 | 17.429 | 19.930 | 0.667 | 16.082 | 32.237 | 1 | 11 | 84.969 | 2.005 | no | principal | no |
| dulce | SARIMA-sel | 2023 | interanual | 75 | 17.429 | 19.930 | 0.667 | 17.429 | — | 0 | 12 | — | — | no | principal | no |
| dulce | SARIMA-sel | 2023 | interanual | 90 | 17.429 | 19.930 | 0.667 | 17.429 | — | 0 | 12 | — | — | no | principal | no |
| dulce | SARIMA-sel | 2024 | mensual | 50 | 25.556 | 33.836 | 1.018 | 31.192 | 19.919 | 6 | 6 | -22.056 | 0.639 | sí | principal | no |
| dulce | SARIMA-sel | 2024 | mensual | 60 | 25.556 | 33.836 | 1.018 | 28.070 | 22.035 | 5 | 7 | -13.777 | 0.785 | sí | principal | no |
| dulce | SARIMA-sel | 2024 | mensual | 75 | 25.556 | 33.836 | 1.018 | 25.362 | 25.942 | 4 | 8 | 1.512 | 1.023 | sí | principal | no |
| dulce | SARIMA-sel | 2024 | mensual | 90 | 25.556 | 33.836 | 1.018 | 25.715 | 23.803 | 1 | 11 | -6.860 | 0.926 | no | principal | no |
| dulce | SARIMA-sel | 2024 | interanual | 50 | 25.556 | 33.836 | 1.018 | 18.283 | 26.217 | 11 | 1 | 2.587 | 1.434 | sí | principal | no |
| dulce | SARIMA-sel | 2024 | interanual | 60 | 25.556 | 33.836 | 1.018 | 13.062 | 28.054 | 10 | 2 | 9.778 | 2.148 | sí | principal | no |
| dulce | SARIMA-sel | 2024 | interanual | 75 | 25.556 | 33.836 | 1.018 | 20.203 | 27.340 | 9 | 3 | 6.982 | 1.353 | sí | principal | no |
| dulce | SARIMA-sel | 2024 | interanual | 90 | 25.556 | 33.836 | 1.018 | 19.317 | 56.748 | 2 | 10 | 122.058 | 2.938 | sí | principal | no |
| dulce | SARIMA-sel | 2025 | mensual | 50 | 19.825 | 30.523 | 0.854 | 25.462 | 14.187 | 6 | 6 | -28.436 | 0.557 | sí | principal | no |
| dulce | SARIMA-sel | 2025 | mensual | 60 | 19.825 | 30.523 | 0.854 | 26.478 | 10.509 | 5 | 7 | -46.989 | 0.397 | sí | principal | no |
| dulce | SARIMA-sel | 2025 | mensual | 75 | 19.825 | 30.523 | 0.854 | 22.750 | 11.049 | 3 | 9 | -44.266 | 0.486 | sí | principal | no |
| dulce | SARIMA-sel | 2025 | mensual | 90 | 19.825 | 30.523 | 0.854 | 19.825 | — | 0 | 12 | — | — | no | principal | no |
| dulce | SARIMA-sel | 2025 | interanual | 50 | 19.825 | 30.523 | 0.854 | 10.734 | 28.915 | 6 | 6 | 45.853 | 2.694 | sí | principal | no |
| dulce | SARIMA-sel | 2025 | interanual | 60 | 19.825 | 30.523 | 0.854 | 10.946 | 32.254 | 5 | 7 | 62.697 | 2.947 | sí | principal | no |
| dulce | SARIMA-sel | 2025 | interanual | 75 | 19.825 | 30.523 | 0.854 | 14.179 | 36.760 | 3 | 9 | 85.427 | 2.592 | sí | principal | no |
| dulce | SARIMA-sel | 2025 | interanual | 90 | 19.825 | 30.523 | 0.854 | 13.515 | 89.232 | 1 | 11 | 350.111 | 6.603 | no | principal | no |
| dulce | Ridge | 2021 | mensual | 50 | 37.924 | 47.561 | 1.196 | 37.113 | 39.059 | 5 | 7 | 2.994 | 1.052 | sí | principal | no |
| dulce | Ridge | 2021 | mensual | 60 | 37.924 | 47.561 | 1.196 | 38.486 | 36.798 | 4 | 8 | -2.968 | 0.956 | sí | principal | no |
| dulce | Ridge | 2021 | mensual | 75 | 37.924 | 47.561 | 1.196 | 36.596 | 41.905 | 3 | 9 | 10.499 | 1.145 | sí | principal | no |
| dulce | Ridge | 2021 | mensual | 90 | 37.924 | 47.561 | 1.196 | 36.596 | 41.905 | 3 | 9 | 10.499 | 1.145 | sí | principal | no |
| dulce | Ridge | 2021 | interanual | 50 | 37.924 | 47.561 | 1.196 | 38.642 | 36.486 | 4 | 8 | -3.790 | 0.944 | sí | principal | no |
| dulce | Ridge | 2021 | interanual | 60 | 37.924 | 47.561 | 1.196 | 39.137 | 34.284 | 3 | 9 | -9.597 | 0.876 | sí | principal | no |
| dulce | Ridge | 2021 | interanual | 75 | 37.924 | 47.561 | 1.196 | 41.602 | 19.529 | 2 | 10 | -48.504 | 0.469 | sí | principal | no |
| dulce | Ridge | 2021 | interanual | 90 | 37.924 | 47.561 | 1.196 | 39.419 | 21.477 | 1 | 11 | -43.369 | 0.545 | no | principal | no |
| dulce | Ridge | 2022 | mensual | 50 | 35.521 | 46.775 | 1.266 | 27.436 | 46.841 | 5 | 7 | 31.866 | 1.707 | sí | principal | no |
| dulce | Ridge | 2022 | mensual | 60 | 35.521 | 46.775 | 1.266 | 27.436 | 46.841 | 5 | 7 | 31.866 | 1.707 | sí | principal | no |
| dulce | Ridge | 2022 | mensual | 75 | 35.521 | 46.775 | 1.266 | 29.329 | 54.099 | 3 | 9 | 52.300 | 1.845 | sí | principal | no |
| dulce | Ridge | 2022 | mensual | 90 | 35.521 | 46.775 | 1.266 | 36.038 | 29.839 | 1 | 11 | -15.997 | 0.828 | no | principal | no |
| dulce | Ridge | 2022 | interanual | 50 | 35.521 | 46.775 | 1.266 | 28.518 | 42.524 | 6 | 6 | 19.715 | 1.491 | sí | principal | no |
| dulce | Ridge | 2022 | interanual | 60 | 35.521 | 46.775 | 1.266 | 42.791 | 20.981 | 4 | 8 | -40.934 | 0.490 | sí | principal | no |
| dulce | Ridge | 2022 | interanual | 75 | 35.521 | 46.775 | 1.266 | 36.800 | 29.128 | 2 | 10 | -17.998 | 0.792 | sí | principal | no |
| dulce | Ridge | 2022 | interanual | 90 | 35.521 | 46.775 | 1.266 | 35.521 | — | 0 | 12 | — | — | no | principal | no |
| dulce | Ridge | 2023 | mensual | 50 | 43.562 | 58.431 | 1.667 | 37.987 | 49.137 | 6 | 6 | 12.797 | 1.294 | sí | principal | no |
| dulce | Ridge | 2023 | mensual | 60 | 43.562 | 58.431 | 1.667 | 48.381 | 33.925 | 4 | 8 | -22.122 | 0.701 | sí | principal | no |
| dulce | Ridge | 2023 | mensual | 75 | 43.562 | 58.431 | 1.667 | 46.421 | 29.268 | 2 | 10 | -32.814 | 0.630 | sí | principal | no |
| dulce | Ridge | 2023 | mensual | 90 | 43.562 | 58.431 | 1.667 | 43.562 | — | 0 | 12 | — | — | no | principal | no |
| dulce | Ridge | 2023 | interanual | 50 | 43.562 | 58.431 | 1.667 | 43.931 | 41.721 | 2 | 10 | -4.227 | 0.950 | sí | principal | no |
| dulce | Ridge | 2023 | interanual | 60 | 43.562 | 58.431 | 1.667 | 40.550 | 76.702 | 1 | 11 | 76.075 | 1.892 | no | principal | no |
| dulce | Ridge | 2023 | interanual | 75 | 43.562 | 58.431 | 1.667 | 43.562 | — | 0 | 12 | — | — | no | principal | no |
| dulce | Ridge | 2023 | interanual | 90 | 43.562 | 58.431 | 1.667 | 43.562 | — | 0 | 12 | — | — | no | principal | no |
| dulce | Ridge | 2024 | mensual | 50 | 97.749 | 107.677 | 3.895 | 94.068 | 101.429 | 6 | 6 | 3.766 | 1.078 | sí | principal | no |
| dulce | Ridge | 2024 | mensual | 60 | 97.749 | 107.677 | 3.895 | 94.476 | 102.330 | 5 | 7 | 4.687 | 1.083 | sí | principal | no |
| dulce | Ridge | 2024 | mensual | 75 | 97.749 | 107.677 | 3.895 | 93.353 | 106.540 | 4 | 8 | 8.994 | 1.141 | sí | principal | no |
| dulce | Ridge | 2024 | mensual | 90 | 97.749 | 107.677 | 3.895 | 99.600 | 77.378 | 1 | 11 | -20.840 | 0.777 | no | principal | no |
| dulce | Ridge | 2024 | interanual | 50 | 97.749 | 107.677 | 3.895 | 109.881 | 96.646 | 11 | 1 | -1.128 | 0.880 | sí | principal | no |
| dulce | Ridge | 2024 | interanual | 60 | 97.749 | 107.677 | 3.895 | 89.479 | 99.402 | 10 | 2 | 1.692 | 1.111 | sí | principal | no |
| dulce | Ridge | 2024 | interanual | 75 | 97.749 | 107.677 | 3.895 | 92.111 | 99.628 | 9 | 3 | 1.922 | 1.082 | sí | principal | no |
| dulce | Ridge | 2024 | interanual | 90 | 97.749 | 107.677 | 3.895 | 98.976 | 91.610 | 2 | 10 | -6.280 | 0.926 | sí | principal | no |
| dulce | Ridge | 2025 | mensual | 50 | 50.593 | 68.334 | 2.181 | 53.856 | 47.330 | 6 | 6 | -6.450 | 0.879 | sí | principal | no |
| dulce | Ridge | 2025 | mensual | 60 | 50.593 | 68.334 | 2.181 | 46.726 | 56.008 | 5 | 7 | 10.703 | 1.199 | sí | principal | no |
| dulce | Ridge | 2025 | mensual | 75 | 50.593 | 68.334 | 2.181 | 37.157 | 90.901 | 3 | 9 | 79.670 | 2.446 | sí | principal | no |
| dulce | Ridge | 2025 | mensual | 90 | 50.593 | 68.334 | 2.181 | 50.593 | — | 0 | 12 | — | — | no | principal | no |
| dulce | Ridge | 2025 | interanual | 50 | 50.593 | 68.334 | 2.181 | 45.397 | 55.790 | 6 | 6 | 10.272 | 1.229 | sí | principal | no |
| dulce | Ridge | 2025 | interanual | 60 | 50.593 | 68.334 | 2.181 | 47.745 | 54.581 | 5 | 7 | 7.882 | 1.143 | sí | principal | no |
| dulce | Ridge | 2025 | interanual | 75 | 50.593 | 68.334 | 2.181 | 59.824 | 22.901 | 3 | 9 | -54.735 | 0.383 | sí | principal | no |
| dulce | Ridge | 2025 | interanual | 90 | 50.593 | 68.334 | 2.181 | 53.239 | 21.489 | 1 | 11 | -57.527 | 0.404 | no | principal | no |
| dulce | ElasticNet | 2021 | mensual | 50 | 37.599 | 45.499 | 1.186 | 34.660 | 41.714 | 5 | 7 | 10.944 | 1.204 | sí | principal | no |
| dulce | ElasticNet | 2021 | mensual | 60 | 37.599 | 45.499 | 1.186 | 37.160 | 38.476 | 4 | 8 | 2.332 | 1.035 | sí | principal | no |
| dulce | ElasticNet | 2021 | mensual | 75 | 37.599 | 45.499 | 1.186 | 35.633 | 43.496 | 3 | 9 | 15.683 | 1.221 | sí | principal | no |
| dulce | ElasticNet | 2021 | mensual | 90 | 37.599 | 45.499 | 1.186 | 35.633 | 43.496 | 3 | 9 | 15.683 | 1.221 | sí | principal | no |
| dulce | ElasticNet | 2021 | interanual | 50 | 37.599 | 45.499 | 1.186 | 38.370 | 36.056 | 4 | 8 | -4.103 | 0.940 | sí | principal | no |
| dulce | ElasticNet | 2021 | interanual | 60 | 37.599 | 45.499 | 1.186 | 38.676 | 34.367 | 3 | 9 | -8.597 | 0.889 | sí | principal | no |
| dulce | ElasticNet | 2021 | interanual | 75 | 37.599 | 45.499 | 1.186 | 41.123 | 19.977 | 2 | 10 | -46.869 | 0.486 | sí | principal | no |
| dulce | ElasticNet | 2021 | interanual | 90 | 37.599 | 45.499 | 1.186 | 38.888 | 23.416 | 1 | 11 | -37.722 | 0.602 | no | principal | no |
| dulce | ElasticNet | 2022 | mensual | 50 | 35.157 | 46.376 | 1.253 | 27.275 | 46.192 | 5 | 7 | 31.388 | 1.694 | sí | principal | no |
| dulce | ElasticNet | 2022 | mensual | 60 | 35.157 | 46.376 | 1.253 | 27.275 | 46.192 | 5 | 7 | 31.388 | 1.694 | sí | principal | no |
| dulce | ElasticNet | 2022 | mensual | 75 | 35.157 | 46.376 | 1.253 | 29.051 | 53.473 | 3 | 9 | 52.099 | 1.841 | sí | principal | no |
| dulce | ElasticNet | 2022 | mensual | 90 | 35.157 | 46.376 | 1.253 | 35.663 | 29.585 | 1 | 11 | -15.849 | 0.830 | no | principal | no |
| dulce | ElasticNet | 2022 | interanual | 50 | 35.157 | 46.376 | 1.253 | 28.212 | 42.102 | 6 | 6 | 19.754 | 1.492 | sí | principal | no |
| dulce | ElasticNet | 2022 | interanual | 60 | 35.157 | 46.376 | 1.253 | 42.414 | 20.643 | 4 | 8 | -41.283 | 0.487 | sí | principal | no |
| dulce | ElasticNet | 2022 | interanual | 75 | 35.157 | 46.376 | 1.253 | 36.384 | 29.022 | 2 | 10 | -17.450 | 0.798 | sí | principal | no |
| dulce | ElasticNet | 2022 | interanual | 90 | 35.157 | 46.376 | 1.253 | 35.157 | — | 0 | 12 | — | — | no | principal | no |
| dulce | ElasticNet | 2023 | mensual | 50 | 43.408 | 58.364 | 1.661 | 39.564 | 47.252 | 6 | 6 | 8.856 | 1.194 | sí | principal | no |
| dulce | ElasticNet | 2023 | mensual | 60 | 43.408 | 58.364 | 1.661 | 49.760 | 30.704 | 4 | 8 | -29.267 | 0.617 | sí | principal | no |
| dulce | ElasticNet | 2023 | mensual | 75 | 43.408 | 58.364 | 1.661 | 46.155 | 29.676 | 2 | 10 | -31.635 | 0.643 | sí | principal | no |
| dulce | ElasticNet | 2023 | mensual | 90 | 43.408 | 58.364 | 1.661 | 43.408 | — | 0 | 12 | — | — | no | principal | no |
| dulce | ElasticNet | 2023 | interanual | 50 | 43.408 | 58.364 | 1.661 | 43.710 | 41.900 | 2 | 10 | -3.475 | 0.959 | sí | principal | no |
| dulce | ElasticNet | 2023 | interanual | 60 | 43.408 | 58.364 | 1.661 | 40.643 | 73.829 | 1 | 11 | 70.080 | 1.817 | no | principal | no |
| dulce | ElasticNet | 2023 | interanual | 75 | 43.408 | 58.364 | 1.661 | 43.408 | — | 0 | 12 | — | — | no | principal | no |
| dulce | ElasticNet | 2023 | interanual | 90 | 43.408 | 58.364 | 1.661 | 43.408 | — | 0 | 12 | — | — | no | principal | no |
| dulce | ElasticNet | 2024 | mensual | 50 | 85.731 | 97.913 | 3.416 | 86.611 | 84.850 | 6 | 6 | -1.027 | 0.980 | sí | principal | no |
| dulce | ElasticNet | 2024 | mensual | 60 | 85.731 | 97.913 | 3.416 | 81.963 | 91.005 | 5 | 7 | 6.152 | 1.110 | sí | principal | no |
| dulce | ElasticNet | 2024 | mensual | 75 | 85.731 | 97.913 | 3.416 | 80.343 | 96.506 | 4 | 8 | 12.570 | 1.201 | sí | principal | no |
| dulce | ElasticNet | 2024 | mensual | 90 | 85.731 | 97.913 | 3.416 | 87.224 | 69.308 | 1 | 11 | -19.156 | 0.795 | no | principal | no |
| dulce | ElasticNet | 2024 | interanual | 50 | 85.731 | 97.913 | 3.416 | 112.073 | 83.336 | 11 | 1 | -2.793 | 0.744 | sí | principal | no |
| dulce | ElasticNet | 2024 | interanual | 60 | 85.731 | 97.913 | 3.416 | 88.105 | 85.256 | 10 | 2 | -0.554 | 0.968 | sí | principal | no |
| dulce | ElasticNet | 2024 | interanual | 75 | 85.731 | 97.913 | 3.416 | 90.685 | 84.079 | 9 | 3 | -1.926 | 0.927 | sí | principal | no |
| dulce | ElasticNet | 2024 | interanual | 90 | 85.731 | 97.913 | 3.416 | 87.098 | 78.892 | 2 | 10 | -7.977 | 0.906 | sí | principal | no |
| dulce | ElasticNet | 2025 | mensual | 50 | 49.346 | 66.474 | 2.127 | 51.753 | 46.939 | 6 | 6 | -4.878 | 0.907 | sí | principal | no |
| dulce | ElasticNet | 2025 | mensual | 60 | 49.346 | 66.474 | 2.127 | 44.517 | 56.106 | 5 | 7 | 13.699 | 1.260 | sí | principal | no |
| dulce | ElasticNet | 2025 | mensual | 75 | 49.346 | 66.474 | 2.127 | 35.554 | 90.720 | 3 | 9 | 83.846 | 2.552 | sí | principal | no |
| dulce | ElasticNet | 2025 | mensual | 90 | 49.346 | 66.474 | 2.127 | 49.346 | — | 0 | 12 | — | — | no | principal | no |
| dulce | ElasticNet | 2025 | interanual | 50 | 49.346 | 66.474 | 2.127 | 44.135 | 54.557 | 6 | 6 | 10.560 | 1.236 | sí | principal | no |
| dulce | ElasticNet | 2025 | interanual | 60 | 49.346 | 66.474 | 2.127 | 46.905 | 52.763 | 5 | 7 | 6.924 | 1.125 | sí | principal | no |
| dulce | ElasticNet | 2025 | interanual | 75 | 49.346 | 66.474 | 2.127 | 58.856 | 20.813 | 3 | 9 | -57.822 | 0.354 | sí | principal | no |
| dulce | ElasticNet | 2025 | interanual | 90 | 49.346 | 66.474 | 2.127 | 52.337 | 16.440 | 1 | 11 | -66.683 | 0.314 | no | principal | no |
| dulce | XGB-37 | 2021 | mensual | 50 | 25.748 | 33.511 | 0.812 | 20.312 | 33.358 | 5 | 7 | 29.558 | 1.642 | sí | principal | no |
| dulce | XGB-37 | 2021 | mensual | 60 | 25.748 | 33.511 | 0.812 | 21.939 | 33.365 | 4 | 8 | 29.586 | 1.521 | sí | principal | no |
| dulce | XGB-37 | 2021 | mensual | 75 | 25.748 | 33.511 | 0.812 | 20.251 | 42.236 | 3 | 9 | 64.040 | 2.086 | sí | principal | no |
| dulce | XGB-37 | 2021 | mensual | 90 | 25.748 | 33.511 | 0.812 | 20.251 | 42.236 | 3 | 9 | 64.040 | 2.086 | sí | principal | no |
| dulce | XGB-37 | 2021 | interanual | 50 | 25.748 | 33.511 | 0.812 | 29.064 | 19.115 | 4 | 8 | -25.759 | 0.658 | sí | principal | no |
| dulce | XGB-37 | 2021 | interanual | 60 | 25.748 | 33.511 | 0.812 | 27.145 | 21.556 | 3 | 9 | -16.282 | 0.794 | sí | principal | no |
| dulce | XGB-37 | 2021 | interanual | 75 | 25.748 | 33.511 | 0.812 | 29.269 | 8.144 | 2 | 10 | -68.372 | 0.278 | sí | principal | no |
| dulce | XGB-37 | 2021 | interanual | 90 | 25.748 | 33.511 | 0.812 | 27.475 | 6.752 | 1 | 11 | -73.777 | 0.246 | no | principal | no |
| dulce | XGB-37 | 2022 | mensual | 50 | 52.339 | 59.936 | 1.865 | 45.914 | 61.334 | 5 | 7 | 17.186 | 1.336 | sí | principal | no |
| dulce | XGB-37 | 2022 | mensual | 60 | 52.339 | 59.936 | 1.865 | 45.914 | 61.334 | 5 | 7 | 17.186 | 1.336 | sí | principal | no |
| dulce | XGB-37 | 2022 | mensual | 75 | 52.339 | 59.936 | 1.865 | 43.239 | 79.638 | 3 | 9 | 52.159 | 1.842 | sí | principal | no |
| dulce | XGB-37 | 2022 | mensual | 90 | 52.339 | 59.936 | 1.865 | 51.276 | 64.031 | 1 | 11 | 22.339 | 1.249 | no | principal | no |
| dulce | XGB-37 | 2022 | interanual | 50 | 52.339 | 59.936 | 1.865 | 40.993 | 63.685 | 6 | 6 | 21.679 | 1.554 | sí | principal | no |
| dulce | XGB-37 | 2022 | interanual | 60 | 52.339 | 59.936 | 1.865 | 56.212 | 44.593 | 4 | 8 | -14.800 | 0.793 | sí | principal | no |
| dulce | XGB-37 | 2022 | interanual | 75 | 52.339 | 59.936 | 1.865 | 53.474 | 46.662 | 2 | 10 | -10.847 | 0.873 | sí | principal | no |
| dulce | XGB-37 | 2022 | interanual | 90 | 52.339 | 59.936 | 1.865 | 52.339 | — | 0 | 12 | — | — | no | principal | no |
| dulce | XGB-37 | 2023 | mensual | 50 | 45.798 | 56.691 | 1.753 | 37.344 | 54.251 | 6 | 6 | 18.459 | 1.453 | sí | principal | no |
| dulce | XGB-37 | 2023 | mensual | 60 | 45.798 | 56.691 | 1.753 | 33.973 | 69.447 | 4 | 8 | 51.638 | 2.044 | sí | principal | no |
| dulce | XGB-37 | 2023 | mensual | 75 | 45.798 | 56.691 | 1.753 | 40.523 | 72.171 | 2 | 10 | 57.586 | 1.781 | sí | principal | no |
| dulce | XGB-37 | 2023 | mensual | 90 | 45.798 | 56.691 | 1.753 | 45.798 | — | 0 | 12 | — | — | no | principal | no |
| dulce | XGB-37 | 2023 | interanual | 50 | 45.798 | 56.691 | 1.753 | 47.336 | 38.105 | 2 | 10 | -16.796 | 0.805 | sí | principal | no |
| dulce | XGB-37 | 2023 | interanual | 60 | 45.798 | 56.691 | 1.753 | 46.786 | 34.929 | 1 | 11 | -23.731 | 0.747 | no | principal | no |
| dulce | XGB-37 | 2023 | interanual | 75 | 45.798 | 56.691 | 1.753 | 45.798 | — | 0 | 12 | — | — | no | principal | no |
| dulce | XGB-37 | 2023 | interanual | 90 | 45.798 | 56.691 | 1.753 | 45.798 | — | 0 | 12 | — | — | no | principal | no |
| dulce | XGB-37 | 2024 | mensual | 50 | 58.039 | 67.196 | 2.313 | 75.127 | 40.951 | 6 | 6 | -29.442 | 0.545 | sí | principal | no |
| dulce | XGB-37 | 2024 | mensual | 60 | 58.039 | 67.196 | 2.313 | 68.195 | 43.821 | 5 | 7 | -24.498 | 0.643 | sí | principal | no |
| dulce | XGB-37 | 2024 | mensual | 75 | 58.039 | 67.196 | 2.313 | 61.126 | 51.865 | 4 | 8 | -10.638 | 0.848 | sí | principal | no |
| dulce | XGB-37 | 2024 | mensual | 90 | 58.039 | 67.196 | 2.313 | 54.769 | 94.008 | 1 | 11 | 61.974 | 1.716 | no | principal | no |
| dulce | XGB-37 | 2024 | interanual | 50 | 58.039 | 67.196 | 2.313 | 83.380 | 55.736 | 11 | 1 | -3.969 | 0.668 | sí | principal | no |
| dulce | XGB-37 | 2024 | interanual | 60 | 58.039 | 67.196 | 2.313 | 46.350 | 60.377 | 10 | 2 | 4.028 | 1.303 | sí | principal | no |
| dulce | XGB-37 | 2024 | interanual | 75 | 58.039 | 67.196 | 2.313 | 57.191 | 58.322 | 9 | 3 | 0.487 | 1.020 | sí | principal | no |
| dulce | XGB-37 | 2024 | interanual | 90 | 58.039 | 67.196 | 2.313 | 54.948 | 73.494 | 2 | 10 | 26.629 | 1.338 | sí | principal | no |
| dulce | XGB-37 | 2025 | mensual | 50 | 59.379 | 77.206 | 2.559 | 70.323 | 48.435 | 6 | 6 | -18.430 | 0.689 | sí | principal | no |
| dulce | XGB-37 | 2025 | mensual | 60 | 59.379 | 77.206 | 2.559 | 61.133 | 56.924 | 5 | 7 | -4.135 | 0.931 | sí | principal | no |
| dulce | XGB-37 | 2025 | mensual | 75 | 59.379 | 77.206 | 2.559 | 49.137 | 90.105 | 3 | 9 | 51.745 | 1.834 | sí | principal | no |
| dulce | XGB-37 | 2025 | mensual | 90 | 59.379 | 77.206 | 2.559 | 59.379 | — | 0 | 12 | — | — | no | principal | no |
| dulce | XGB-37 | 2025 | interanual | 50 | 59.379 | 77.206 | 2.559 | 53.570 | 65.188 | 6 | 6 | 9.784 | 1.217 | sí | principal | no |
| dulce | XGB-37 | 2025 | interanual | 60 | 59.379 | 77.206 | 2.559 | 61.020 | 57.081 | 5 | 7 | -3.869 | 0.935 | sí | principal | no |
| dulce | XGB-37 | 2025 | interanual | 75 | 59.379 | 77.206 | 2.559 | 74.452 | 14.159 | 3 | 9 | -76.155 | 0.190 | sí | principal | no |
| dulce | XGB-37 | 2025 | interanual | 90 | 59.379 | 77.206 | 2.559 | 62.902 | 20.622 | 1 | 11 | -65.270 | 0.328 | no | principal | no |
| dulce | GC3 | 2021 | mensual | 50 | 36.517 | 46.262 | 1.152 | 36.832 | 36.077 | 5 | 7 | -1.205 | 0.980 | sí | principal | no |
| dulce | GC3 | 2021 | mensual | 60 | 36.517 | 46.262 | 1.152 | 34.694 | 40.162 | 4 | 8 | 9.982 | 1.158 | sí | principal | no |
| dulce | GC3 | 2021 | mensual | 75 | 36.517 | 46.262 | 1.152 | 34.133 | 43.670 | 3 | 9 | 19.588 | 1.279 | sí | principal | no |
| dulce | GC3 | 2021 | mensual | 90 | 36.517 | 46.262 | 1.152 | 34.133 | 43.670 | 3 | 9 | 19.588 | 1.279 | sí | principal | no |
| dulce | GC3 | 2021 | interanual | 50 | 36.517 | 46.262 | 1.152 | 35.365 | 38.822 | 4 | 8 | 6.312 | 1.098 | sí | principal | no |
| dulce | GC3 | 2021 | interanual | 60 | 36.517 | 46.262 | 1.152 | 34.561 | 42.386 | 3 | 9 | 16.072 | 1.226 | sí | principal | no |
| dulce | GC3 | 2021 | interanual | 75 | 36.517 | 46.262 | 1.152 | 38.565 | 26.279 | 2 | 10 | -28.038 | 0.681 | sí | principal | no |
| dulce | GC3 | 2021 | interanual | 90 | 36.517 | 46.262 | 1.152 | 37.142 | 29.640 | 1 | 11 | -18.833 | 0.798 | no | principal | no |
| dulce | GC3 | 2022 | mensual | 50 | 37.172 | 46.398 | 1.325 | 39.550 | 33.843 | 5 | 7 | -8.956 | 0.856 | sí | principal | no |
| dulce | GC3 | 2022 | mensual | 60 | 37.172 | 46.398 | 1.325 | 39.550 | 33.843 | 5 | 7 | -8.956 | 0.856 | sí | principal | no |
| dulce | GC3 | 2022 | mensual | 75 | 37.172 | 46.398 | 1.325 | 34.785 | 44.333 | 3 | 9 | 19.264 | 1.274 | sí | principal | no |
| dulce | GC3 | 2022 | mensual | 90 | 37.172 | 46.398 | 1.325 | 37.425 | 34.392 | 1 | 11 | -7.479 | 0.919 | no | principal | no |
| dulce | GC3 | 2022 | interanual | 50 | 37.172 | 46.398 | 1.325 | 32.011 | 42.333 | 6 | 6 | 13.884 | 1.322 | sí | principal | no |
| dulce | GC3 | 2022 | interanual | 60 | 37.172 | 46.398 | 1.325 | 42.793 | 25.931 | 4 | 8 | -30.240 | 0.606 | sí | principal | no |
| dulce | GC3 | 2022 | interanual | 75 | 37.172 | 46.398 | 1.325 | 39.192 | 27.075 | 2 | 10 | -27.163 | 0.691 | sí | principal | no |
| dulce | GC3 | 2022 | interanual | 90 | 37.172 | 46.398 | 1.325 | 37.172 | — | 0 | 12 | — | — | no | principal | no |
| dulce | GC3 | 2023 | mensual | 50 | 38.029 | 45.841 | 1.455 | 37.736 | 38.323 | 6 | 6 | 0.772 | 1.016 | sí | principal | no |
| dulce | GC3 | 2023 | mensual | 60 | 38.029 | 45.841 | 1.455 | 38.084 | 37.921 | 4 | 8 | -0.285 | 0.996 | sí | principal | no |
| dulce | GC3 | 2023 | mensual | 75 | 38.029 | 45.841 | 1.455 | 35.449 | 50.930 | 2 | 10 | 33.923 | 1.437 | sí | principal | no |
| dulce | GC3 | 2023 | mensual | 90 | 38.029 | 45.841 | 1.455 | 38.029 | — | 0 | 12 | — | — | no | principal | no |
| dulce | GC3 | 2023 | interanual | 50 | 38.029 | 45.841 | 1.455 | 38.829 | 34.030 | 2 | 10 | -10.518 | 0.876 | sí | principal | no |
| dulce | GC3 | 2023 | interanual | 60 | 38.029 | 45.841 | 1.455 | 38.987 | 27.494 | 1 | 11 | -27.702 | 0.705 | no | principal | no |
| dulce | GC3 | 2023 | interanual | 75 | 38.029 | 45.841 | 1.455 | 38.029 | — | 0 | 12 | — | — | no | principal | no |
| dulce | GC3 | 2023 | interanual | 90 | 38.029 | 45.841 | 1.455 | 38.029 | — | 0 | 12 | — | — | no | principal | no |
| dulce | GC3 | 2024 | mensual | 50 | 68.215 | 81.601 | 2.718 | 88.504 | 47.926 | 6 | 6 | -29.743 | 0.542 | sí | principal | no |
| dulce | GC3 | 2024 | mensual | 60 | 68.215 | 81.601 | 2.718 | 80.008 | 51.705 | 5 | 7 | -24.203 | 0.646 | sí | principal | no |
| dulce | GC3 | 2024 | mensual | 75 | 68.215 | 81.601 | 2.718 | 78.757 | 47.130 | 4 | 8 | -30.910 | 0.598 | sí | principal | no |
| dulce | GC3 | 2024 | mensual | 90 | 68.215 | 81.601 | 2.718 | 71.533 | 31.716 | 1 | 11 | -53.506 | 0.443 | no | principal | no |
| dulce | GC3 | 2024 | interanual | 50 | 68.215 | 81.601 | 2.718 | 104.231 | 64.941 | 11 | 1 | -4.800 | 0.623 | sí | principal | no |
| dulce | GC3 | 2024 | interanual | 60 | 68.215 | 81.601 | 2.718 | 66.189 | 68.620 | 10 | 2 | 0.594 | 1.037 | sí | principal | no |
| dulce | GC3 | 2024 | interanual | 75 | 68.215 | 81.601 | 2.718 | 75.587 | 65.757 | 9 | 3 | -3.602 | 0.870 | sí | principal | no |
| dulce | GC3 | 2024 | interanual | 90 | 68.215 | 81.601 | 2.718 | 63.516 | 91.710 | 2 | 10 | 34.442 | 1.444 | sí | principal | no |
| dulce | GC3 | 2025 | mensual | 50 | 103.413 | 125.318 | 4.457 | 121.844 | 84.982 | 6 | 6 | -17.823 | 0.697 | sí | principal | no |
| dulce | GC3 | 2025 | mensual | 60 | 103.413 | 125.318 | 4.457 | 108.049 | 96.923 | 5 | 7 | -6.276 | 0.897 | sí | principal | no |
| dulce | GC3 | 2025 | mensual | 75 | 103.413 | 125.318 | 4.457 | 98.236 | 118.944 | 3 | 9 | 15.019 | 1.211 | sí | principal | no |
| dulce | GC3 | 2025 | mensual | 90 | 103.413 | 125.318 | 4.457 | 103.413 | — | 0 | 12 | — | — | no | principal | no |
| dulce | GC3 | 2025 | interanual | 50 | 103.413 | 125.318 | 4.457 | 80.959 | 125.867 | 6 | 6 | 21.713 | 1.555 | sí | principal | no |
| dulce | GC3 | 2025 | interanual | 60 | 103.413 | 125.318 | 4.457 | 97.516 | 111.668 | 5 | 7 | 7.983 | 1.145 | sí | principal | no |
| dulce | GC3 | 2025 | interanual | 75 | 103.413 | 125.318 | 4.457 | 112.046 | 77.513 | 3 | 9 | -25.045 | 0.692 | sí | principal | no |
| dulce | GC3 | 2025 | interanual | 90 | 103.413 | 125.318 | 4.457 | 107.628 | 57.047 | 1 | 11 | -44.836 | 0.530 | no | principal | no |
| dulce | GE | 2021 | mensual | 50 | 41.071 | 52.350 | 1.295 | 44.569 | 36.173 | 5 | 7 | -11.925 | 0.812 | sí | principal | no |
| dulce | GE | 2021 | mensual | 60 | 41.071 | 52.350 | 1.295 | 42.237 | 38.738 | 4 | 8 | -5.679 | 0.917 | sí | principal | no |
| dulce | GE | 2021 | mensual | 75 | 41.071 | 52.350 | 1.295 | 40.168 | 43.779 | 3 | 9 | 6.595 | 1.090 | sí | principal | no |
| dulce | GE | 2021 | mensual | 90 | 41.071 | 52.350 | 1.295 | 40.168 | 43.779 | 3 | 9 | 6.595 | 1.090 | sí | principal | no |
| dulce | GE | 2021 | interanual | 50 | 41.071 | 52.350 | 1.295 | 42.187 | 38.838 | 4 | 8 | -5.436 | 0.921 | sí | principal | no |
| dulce | GE | 2021 | interanual | 60 | 41.071 | 52.350 | 1.295 | 39.924 | 44.511 | 3 | 9 | 8.377 | 1.115 | sí | principal | no |
| dulce | GE | 2021 | interanual | 75 | 41.071 | 52.350 | 1.295 | 44.890 | 21.974 | 2 | 10 | -46.496 | 0.490 | sí | principal | no |
| dulce | GE | 2021 | interanual | 90 | 41.071 | 52.350 | 1.295 | 42.658 | 23.614 | 1 | 11 | -42.504 | 0.554 | no | principal | no |
| dulce | GE | 2022 | mensual | 50 | 37.529 | 47.403 | 1.338 | 40.911 | 32.795 | 5 | 7 | -12.616 | 0.802 | sí | principal | no |
| dulce | GE | 2022 | mensual | 60 | 37.529 | 47.403 | 1.338 | 40.911 | 32.795 | 5 | 7 | -12.616 | 0.802 | sí | principal | no |
| dulce | GE | 2022 | mensual | 75 | 37.529 | 47.403 | 1.338 | 35.799 | 42.719 | 3 | 9 | 13.828 | 1.193 | sí | principal | no |
| dulce | GE | 2022 | mensual | 90 | 37.529 | 47.403 | 1.338 | 38.370 | 28.283 | 1 | 11 | -24.638 | 0.737 | no | principal | no |
| dulce | GE | 2022 | interanual | 50 | 37.529 | 47.403 | 1.338 | 32.888 | 42.170 | 6 | 6 | 12.366 | 1.282 | sí | principal | no |
| dulce | GE | 2022 | interanual | 60 | 37.529 | 47.403 | 1.338 | 44.120 | 24.347 | 4 | 8 | -35.126 | 0.552 | sí | principal | no |
| dulce | GE | 2022 | interanual | 75 | 37.529 | 47.403 | 1.338 | 40.586 | 22.244 | 2 | 10 | -40.729 | 0.548 | sí | principal | no |
| dulce | GE | 2022 | interanual | 90 | 37.529 | 47.403 | 1.338 | 37.529 | — | 0 | 12 | — | — | no | principal | no |
| dulce | GE | 2023 | mensual | 50 | 42.237 | 50.813 | 1.616 | 44.674 | 39.799 | 6 | 6 | -5.770 | 0.891 | sí | principal | no |
| dulce | GE | 2023 | mensual | 60 | 42.237 | 50.813 | 1.616 | 44.229 | 38.251 | 4 | 8 | -9.436 | 0.865 | sí | principal | no |
| dulce | GE | 2023 | mensual | 75 | 42.237 | 50.813 | 1.616 | 40.175 | 52.543 | 2 | 10 | 24.402 | 1.308 | sí | principal | no |
| dulce | GE | 2023 | mensual | 90 | 42.237 | 50.813 | 1.616 | 42.237 | — | 0 | 12 | — | — | no | principal | no |
| dulce | GE | 2023 | interanual | 50 | 42.237 | 50.813 | 1.616 | 43.495 | 35.943 | 2 | 10 | -14.902 | 0.826 | sí | principal | no |
| dulce | GE | 2023 | interanual | 60 | 42.237 | 50.813 | 1.616 | 43.440 | 29.003 | 1 | 11 | -31.333 | 0.668 | no | principal | no |
| dulce | GE | 2023 | interanual | 75 | 42.237 | 50.813 | 1.616 | 42.237 | — | 0 | 12 | — | — | no | principal | no |
| dulce | GE | 2023 | interanual | 90 | 42.237 | 50.813 | 1.616 | 42.237 | — | 0 | 12 | — | — | no | principal | no |
| dulce | GE | 2024 | mensual | 50 | 67.251 | 79.600 | 2.680 | 84.163 | 50.339 | 6 | 6 | -25.147 | 0.598 | sí | principal | no |
| dulce | GE | 2024 | mensual | 60 | 67.251 | 79.600 | 2.680 | 78.458 | 51.563 | 5 | 7 | -23.328 | 0.657 | sí | principal | no |
| dulce | GE | 2024 | mensual | 75 | 67.251 | 79.600 | 2.680 | 75.384 | 50.986 | 4 | 8 | -24.186 | 0.676 | sí | principal | no |
| dulce | GE | 2024 | mensual | 90 | 67.251 | 79.600 | 2.680 | 69.895 | 38.175 | 1 | 11 | -43.235 | 0.546 | no | principal | no |
| dulce | GE | 2024 | interanual | 50 | 67.251 | 79.600 | 2.680 | 106.743 | 63.661 | 11 | 1 | -5.338 | 0.596 | sí | principal | no |
| dulce | GE | 2024 | interanual | 60 | 67.251 | 79.600 | 2.680 | 68.312 | 67.039 | 10 | 2 | -0.315 | 0.981 | sí | principal | no |
| dulce | GE | 2024 | interanual | 75 | 67.251 | 79.600 | 2.680 | 74.880 | 64.709 | 9 | 3 | -3.781 | 0.864 | sí | principal | no |
| dulce | GE | 2024 | interanual | 90 | 67.251 | 79.600 | 2.680 | 64.831 | 79.355 | 2 | 10 | 17.997 | 1.224 | sí | principal | no |
| dulce | GE | 2025 | mensual | 50 | 95.585 | 116.900 | 4.120 | 115.863 | 75.306 | 6 | 6 | -21.215 | 0.650 | sí | principal | no |
| dulce | GE | 2025 | mensual | 60 | 95.585 | 116.900 | 4.120 | 102.310 | 86.169 | 5 | 7 | -9.851 | 0.842 | sí | principal | no |
| dulce | GE | 2025 | mensual | 75 | 95.585 | 116.900 | 4.120 | 94.144 | 99.908 | 3 | 9 | 4.523 | 1.061 | sí | principal | no |
| dulce | GE | 2025 | mensual | 90 | 95.585 | 116.900 | 4.120 | 95.585 | — | 0 | 12 | — | — | no | principal | no |
| dulce | GE | 2025 | interanual | 50 | 95.585 | 116.900 | 4.120 | 74.230 | 116.939 | 6 | 6 | 22.341 | 1.575 | sí | principal | no |
| dulce | GE | 2025 | interanual | 60 | 95.585 | 116.900 | 4.120 | 90.735 | 102.374 | 5 | 7 | 7.103 | 1.128 | sí | principal | no |
| dulce | GE | 2025 | interanual | 75 | 95.585 | 116.900 | 4.120 | 102.315 | 75.392 | 3 | 9 | -21.125 | 0.737 | sí | principal | no |
| dulce | GE | 2025 | interanual | 90 | 95.585 | 116.900 | 4.120 | 99.250 | 55.263 | 1 | 11 | -42.184 | 0.557 | no | principal | no |
| dulce | XGB-43 | 2021 | mensual | 50 | 26.196 | 32.932 | 0.826 | 20.823 | 33.719 | 5 | 7 | 28.715 | 1.619 | sí | principal | sí |
| dulce | XGB-43 | 2021 | mensual | 60 | 26.196 | 32.932 | 0.826 | 23.770 | 31.049 | 4 | 8 | 18.524 | 1.306 | sí | principal | sí |
| dulce | XGB-43 | 2021 | mensual | 75 | 26.196 | 32.932 | 0.826 | 21.609 | 39.958 | 3 | 9 | 52.534 | 1.849 | sí | principal | sí |
| dulce | XGB-43 | 2021 | mensual | 90 | 26.196 | 32.932 | 0.826 | 21.609 | 39.958 | 3 | 9 | 52.534 | 1.849 | sí | principal | sí |
| dulce | XGB-43 | 2021 | interanual | 50 | 26.196 | 32.932 | 0.826 | 30.068 | 18.453 | 4 | 8 | -29.560 | 0.614 | sí | principal | sí |
| dulce | XGB-43 | 2021 | interanual | 60 | 26.196 | 32.932 | 0.826 | 28.513 | 19.246 | 3 | 9 | -26.531 | 0.675 | sí | principal | sí |
| dulce | XGB-43 | 2021 | interanual | 75 | 26.196 | 32.932 | 0.826 | 30.406 | 5.148 | 2 | 10 | -80.348 | 0.169 | sí | principal | sí |
| dulce | XGB-43 | 2021 | interanual | 90 | 26.196 | 32.932 | 0.826 | 28.185 | 4.321 | 1 | 11 | -83.507 | 0.153 | no | principal | sí |
| dulce | XGB-43 | 2022 | mensual | 50 | 52.232 | 59.448 | 1.862 | 45.125 | 62.181 | 5 | 7 | 19.049 | 1.378 | sí | principal | sí |
| dulce | XGB-43 | 2022 | mensual | 60 | 52.232 | 59.448 | 1.862 | 45.125 | 62.181 | 5 | 7 | 19.049 | 1.378 | sí | principal | sí |
| dulce | XGB-43 | 2022 | mensual | 75 | 52.232 | 59.448 | 1.862 | 43.359 | 78.851 | 3 | 9 | 50.964 | 1.819 | sí | principal | sí |
| dulce | XGB-43 | 2022 | mensual | 90 | 52.232 | 59.448 | 1.862 | 51.751 | 57.521 | 1 | 11 | 10.127 | 1.112 | no | principal | sí |
| dulce | XGB-43 | 2022 | interanual | 50 | 52.232 | 59.448 | 1.862 | 42.617 | 61.846 | 6 | 6 | 18.407 | 1.451 | sí | principal | sí |
| dulce | XGB-43 | 2022 | interanual | 60 | 52.232 | 59.448 | 1.862 | 56.960 | 42.776 | 4 | 8 | -18.104 | 0.751 | sí | principal | sí |
| dulce | XGB-43 | 2022 | interanual | 75 | 52.232 | 59.448 | 1.862 | 53.528 | 45.752 | 2 | 10 | -12.405 | 0.855 | sí | principal | sí |
| dulce | XGB-43 | 2022 | interanual | 90 | 52.232 | 59.448 | 1.862 | 52.232 | — | 0 | 12 | — | — | no | principal | sí |
| dulce | XGB-43 | 2023 | mensual | 50 | 44.333 | 55.828 | 1.697 | 31.389 | 57.277 | 6 | 6 | 29.197 | 1.825 | sí | principal | sí |
| dulce | XGB-43 | 2023 | mensual | 60 | 44.333 | 55.828 | 1.697 | 31.519 | 69.963 | 4 | 8 | 57.811 | 2.220 | sí | principal | sí |
| dulce | XGB-43 | 2023 | mensual | 75 | 44.333 | 55.828 | 1.697 | 38.543 | 73.283 | 2 | 10 | 65.301 | 1.901 | sí | principal | sí |
| dulce | XGB-43 | 2023 | mensual | 90 | 44.333 | 55.828 | 1.697 | 44.333 | — | 0 | 12 | — | — | no | principal | sí |
| dulce | XGB-43 | 2023 | interanual | 50 | 44.333 | 55.828 | 1.697 | 45.738 | 37.311 | 2 | 10 | -15.839 | 0.816 | sí | principal | sí |
| dulce | XGB-43 | 2023 | interanual | 60 | 44.333 | 55.828 | 1.697 | 46.066 | 25.280 | 1 | 11 | -42.978 | 0.549 | no | principal | sí |
| dulce | XGB-43 | 2023 | interanual | 75 | 44.333 | 55.828 | 1.697 | 44.333 | — | 0 | 12 | — | — | no | principal | sí |
| dulce | XGB-43 | 2023 | interanual | 90 | 44.333 | 55.828 | 1.697 | 44.333 | — | 0 | 12 | — | — | no | principal | sí |
| dulce | XGB-43 | 2024 | mensual | 50 | 54.068 | 64.325 | 2.155 | 72.697 | 35.440 | 6 | 6 | -34.454 | 0.488 | sí | principal | sí |
| dulce | XGB-43 | 2024 | mensual | 60 | 54.068 | 64.325 | 2.155 | 64.901 | 38.903 | 5 | 7 | -28.049 | 0.599 | sí | principal | sí |
| dulce | XGB-43 | 2024 | mensual | 75 | 54.068 | 64.325 | 2.155 | 58.137 | 45.931 | 4 | 8 | -15.050 | 0.790 | sí | principal | sí |
| dulce | XGB-43 | 2024 | mensual | 90 | 54.068 | 64.325 | 2.155 | 51.389 | 83.543 | 1 | 11 | 54.514 | 1.626 | no | principal | sí |
| dulce | XGB-43 | 2024 | interanual | 50 | 54.068 | 64.325 | 2.155 | 77.420 | 51.945 | 11 | 1 | -3.926 | 0.671 | sí | principal | sí |
| dulce | XGB-43 | 2024 | interanual | 60 | 54.068 | 64.325 | 2.155 | 44.701 | 55.942 | 10 | 2 | 3.465 | 1.251 | sí | principal | sí |
| dulce | XGB-43 | 2024 | interanual | 75 | 54.068 | 64.325 | 2.155 | 54.776 | 53.832 | 9 | 3 | -0.436 | 0.983 | sí | principal | sí |
| dulce | XGB-43 | 2024 | interanual | 90 | 54.068 | 64.325 | 2.155 | 49.311 | 77.856 | 2 | 10 | 43.996 | 1.579 | sí | principal | sí |
| dulce | XGB-43 | 2025 | mensual | 50 | 61.354 | 77.118 | 2.644 | 73.656 | 49.053 | 6 | 6 | -20.049 | 0.666 | sí | principal | sí |
| dulce | XGB-43 | 2025 | mensual | 60 | 61.354 | 77.118 | 2.644 | 64.366 | 57.139 | 5 | 7 | -6.871 | 0.888 | sí | principal | sí |
| dulce | XGB-43 | 2025 | mensual | 75 | 61.354 | 77.118 | 2.644 | 54.385 | 82.264 | 3 | 9 | 34.080 | 1.513 | sí | principal | sí |
| dulce | XGB-43 | 2025 | mensual | 90 | 61.354 | 77.118 | 2.644 | 61.354 | — | 0 | 12 | — | — | no | principal | sí |
| dulce | XGB-43 | 2025 | interanual | 50 | 61.354 | 77.118 | 2.644 | 59.363 | 63.346 | 6 | 6 | 3.246 | 1.067 | sí | principal | sí |
| dulce | XGB-43 | 2025 | interanual | 60 | 61.354 | 77.118 | 2.644 | 65.883 | 55.014 | 5 | 7 | -10.334 | 0.835 | sí | principal | sí |
| dulce | XGB-43 | 2025 | interanual | 75 | 61.354 | 77.118 | 2.644 | 76.812 | 14.981 | 3 | 9 | -75.582 | 0.195 | sí | principal | sí |
| dulce | XGB-43 | 2025 | interanual | 90 | 61.354 | 77.118 | 2.644 | 65.357 | 17.326 | 1 | 11 | -71.761 | 0.265 | no | principal | sí |

### T06_agregadas_IC.csv — T06 completa: agregadas con IC iid y por bloques, ambos conjuntos, P50/P60/P75/P90, mensual e interanual

`06_metricas/agregadas/T06_agregadas_IC.csv` — 352 filas × 28 columnas.

| conjunto | cultivar | tipo | percentil | modelo | MAE | RMSE | MASE | MAE_normal | MAE_shock | n_shock | n_normal | Delta_s | razon_shock_normal | exploratorio | iid_global_lo | iid_global_hi | iid_shock_lo | iid_shock_hi | iid_normal_lo | iid_normal_hi | bloq_global_lo | bloq_global_hi | bloq_shock_lo | bloq_shock_hi | bloq_normal_lo | bloq_normal_hi | bloq_shock_remuestreos_sin_shock |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| principal_2021_2025 | sutil | mensual | 50 | Naive | 3,624.070 | 4,767.714 | 0.613 | 1,381.772 | 6,021.010 | 29 | 31 | 66.139 | 4.357 | no | 2,919.722 | 4,381.878 | 5,162.687 | 6,867.847 | 1,003.012 | 1,793.011 | 2,968.932 | 4,295.011 | 5,204.037 | 6,812.570 | 945.375 | 1,822.926 | 0 |
| principal_2021_2025 | sutil | mensual | 50 | Seasonal Naive | 6,074.886 | 7,451.012 | 1.030 | 6,072.392 | 6,077.552 | 29 | 31 | 0.044 | 1.001 | no | 5,156.123 | 6,986.866 | 4,790.031 | 7,336.466 | 4,744.955 | 7,363.056 | 4,854.083 | 7,239.177 | 4,449.774 | 7,500.031 | 4,380.201 | 7,864.146 | 0 |
| principal_2021_2025 | sutil | mensual | 50 | Chronos | 2,648.547 | 3,308.182 | 0.440 | 1,815.837 | 3,538.684 | 29 | 31 | 33.609 | 1.949 | no | 2,171.227 | 3,143.848 | 2,778.482 | 4,329.806 | 1,435.621 | 2,207.704 | 2,242.974 | 3,085.042 | 2,858.799 | 4,290.520 | 1,504.898 | 2,166.959 | 0 |
| principal_2021_2025 | sutil | mensual | 50 | SARIMA | 3,360.787 | 4,122.695 | 0.559 | 3,103.550 | 3,635.765 | 29 | 31 | 8.182 | 1.171 | no | 2,779.970 | 3,970.060 | 2,791.873 | 4,487.509 | 2,372.343 | 3,868.026 | 2,865.760 | 3,885.354 | 2,978.080 | 4,350.867 | 2,471.453 | 3,803.500 | 0 |
| principal_2021_2025 | sutil | mensual | 50 | SARIMA-sel | 3,205.876 | 4,176.530 | 0.540 | 3,060.146 | 3,361.657 | 29 | 31 | 4.859 | 1.099 | no | 2,563.044 | 3,880.304 | 2,409.735 | 4,390.218 | 2,310.649 | 3,856.197 | 2,669.421 | 3,710.457 | 2,383.560 | 4,331.719 | 2,310.609 | 3,841.574 | 0 |
| principal_2021_2025 | sutil | mensual | 50 | Ridge | 4,925.136 | 7,301.277 | 0.834 | 3,089.447 | 6,887.424 | 29 | 31 | 39.842 | 2.229 | no | 3,838.044 | 6,074.414 | 4,909.460 | 9,016.713 | 2,320.120 | 3,901.620 | 3,650.039 | 6,235.715 | 4,615.915 | 9,322.545 | 2,181.930 | 4,079.282 | 0 |
| principal_2021_2025 | sutil | mensual | 50 | ElasticNet | 4,871.911 | 7,050.934 | 0.826 | 2,975.804 | 6,898.785 | 29 | 31 | 41.603 | 2.318 | no | 3,846.717 | 5,950.017 | 5,074.996 | 8,814.909 | 2,172.539 | 3,823.666 | 3,617.416 | 6,153.101 | 4,803.703 | 9,072.349 | 1,997.796 | 4,106.032 | 0 |
| principal_2021_2025 | sutil | mensual | 50 | XGB-37 | 4,881.450 | 5,940.206 | 0.809 | 4,869.081 | 4,894.672 | 29 | 31 | 0.271 | 1.005 | no | 4,062.861 | 5,731.588 | 3,805.415 | 6,020.349 | 3,744.556 | 6,037.899 | 3,848.344 | 5,944.209 | 3,692.747 | 6,142.472 | 3,302.249 | 6,440.739 | 0 |
| principal_2021_2025 | sutil | mensual | 50 | GC3 | 6,361.305 | 8,072.649 | 1.081 | 6,495.333 | 6,218.033 | 29 | 31 | -2.252 | 0.957 | no | 5,292.163 | 7,445.730 | 5,021.148 | 7,432.617 | 4,951.023 | 8,178.674 | 4,846.149 | 7,918.768 | 4,808.406 | 7,714.432 | 4,217.958 | 8,920.922 | 0 |
| principal_2021_2025 | sutil | mensual | 50 | GE | 6,743.530 | 8,647.879 | 1.148 | 7,312.059 | 6,135.792 | 29 | 31 | -9.012 | 0.839 | no | 5,587.118 | 7,894.232 | 4,888.444 | 7,453.111 | 5,683.827 | 9,035.650 | 5,062.121 | 8,442.844 | 4,678.152 | 7,688.786 | 4,751.359 | 9,871.007 | 0 |
| principal_2021_2025 | sutil | mensual | 50 | XGB-43 | 5,011.936 | 6,182.917 | 0.832 | 5,110.352 | 4,906.731 | 29 | 31 | -2.099 | 0.960 | sí | 4,141.407 | 5,916.451 | 3,724.788 | 6,106.648 | 3,895.531 | 6,370.686 | 3,907.445 | 6,149.954 | 3,602.436 | 6,259.012 | 3,450.978 | 6,784.112 | 0 |
| principal_2021_2025 | sutil | mensual | 60 | Naive | 3,624.070 | 4,767.714 | 0.613 | 1,617.110 | 6,433.814 | 25 | 35 | 77.530 | 3.979 | no | 2,919.722 | 4,381.878 | 5,525.732 | 7,300.434 | 1,205.148 | 2,025.900 | 2,968.932 | 4,295.011 | 5,632.375 | 7,215.196 | 1,218.135 | 2,022.270 | 0 |
| principal_2021_2025 | sutil | mensual | 60 | Seasonal Naive | 6,074.886 | 7,451.012 | 1.030 | 5,899.961 | 6,319.781 | 25 | 35 | 4.031 | 1.071 | no | 5,156.123 | 6,986.866 | 4,871.185 | 7,721.275 | 4,718.384 | 7,064.079 | 4,854.083 | 7,239.177 | 4,540.235 | 7,984.477 | 4,343.947 | 7,552.666 | 0 |
| principal_2021_2025 | sutil | mensual | 60 | Chronos | 2,648.547 | 3,308.182 | 0.440 | 1,844.848 | 3,773.724 | 25 | 35 | 42.483 | 2.046 | no | 2,171.227 | 3,143.848 | 2,963.525 | 4,584.928 | 1,438.179 | 2,278.400 | 2,242.974 | 3,085.042 | 3,016.202 | 4,586.495 | 1,494.691 | 2,234.636 | 0 |
| principal_2021_2025 | sutil | mensual | 60 | SARIMA | 3,360.787 | 4,122.695 | 0.559 | 3,243.514 | 3,524.969 | 25 | 35 | 4.885 | 1.087 | no | 2,779.970 | 3,970.060 | 2,595.969 | 4,460.661 | 2,550.256 | 3,968.810 | 2,865.760 | 3,885.354 | 2,758.694 | 4,327.684 | 2,641.597 | 3,909.558 | 0 |
| principal_2021_2025 | sutil | mensual | 60 | SARIMA-sel | 3,205.876 | 4,176.530 | 0.540 | 3,011.850 | 3,477.513 | 25 | 35 | 8.473 | 1.155 | no | 2,563.044 | 3,880.304 | 2,381.279 | 4,646.857 | 2,325.088 | 3,757.652 | 2,669.421 | 3,710.457 | 2,372.555 | 4,593.475 | 2,313.841 | 3,739.402 | 0 |
| principal_2021_2025 | sutil | mensual | 60 | Ridge | 4,925.136 | 7,301.277 | 0.834 | 3,088.138 | 7,496.933 | 25 | 35 | 52.218 | 2.428 | no | 3,838.044 | 6,074.414 | 5,191.665 | 9,976.607 | 2,321.238 | 3,882.574 | 3,650.039 | 6,235.715 | 4,922.952 | 10,341.410 | 2,211.295 | 4,048.801 | 0 |
| principal_2021_2025 | sutil | mensual | 60 | ElasticNet | 4,871.911 | 7,050.934 | 0.826 | 3,047.393 | 7,426.237 | 25 | 35 | 52.430 | 2.437 | no | 3,846.717 | 5,950.017 | 5,312.655 | 9,648.657 | 2,255.804 | 3,878.402 | 3,617.416 | 6,153.101 | 5,073.479 | 9,976.745 | 2,091.120 | 4,137.008 | 0 |
| principal_2021_2025 | sutil | mensual | 60 | XGB-37 | 4,881.450 | 5,940.206 | 0.809 | 4,641.450 | 5,217.449 | 25 | 35 | 6.883 | 1.124 | no | 4,062.861 | 5,731.588 | 3,965.205 | 6,496.992 | 3,636.578 | 5,709.773 | 3,848.344 | 5,944.209 | 3,847.042 | 6,609.402 | 3,208.913 | 6,121.255 | 0 |
| principal_2021_2025 | sutil | mensual | 60 | GC3 | 6,361.305 | 8,072.649 | 1.081 | 6,344.052 | 6,385.458 | 25 | 35 | 0.380 | 1.007 | no | 5,292.163 | 7,445.730 | 5,021.581 | 7,803.739 | 4,958.118 | 7,858.937 | 4,846.149 | 7,918.768 | 4,841.709 | 8,105.624 | 4,295.460 | 8,542.054 | 0 |
| principal_2021_2025 | sutil | mensual | 60 | GE | 6,743.530 | 8,647.879 | 1.148 | 6,987.642 | 6,401.773 | 25 | 35 | -5.068 | 0.916 | no | 5,587.118 | 7,894.232 | 4,961.309 | 7,900.824 | 5,504.518 | 8,549.915 | 5,062.121 | 8,442.844 | 4,776.407 | 8,167.942 | 4,656.711 | 9,355.087 | 0 |
| principal_2021_2025 | sutil | mensual | 60 | XGB-43 | 5,011.936 | 6,182.917 | 0.832 | 4,847.453 | 5,242.211 | 25 | 35 | 4.595 | 1.081 | sí | 4,141.407 | 5,916.451 | 3,918.281 | 6,605.250 | 3,767.391 | 5,993.099 | 3,907.445 | 6,149.954 | 3,790.402 | 6,732.825 | 3,304.797 | 6,446.868 | 0 |
| principal_2021_2025 | sutil | mensual | 75 | Naive | 3,624.070 | 4,767.714 | 0.613 | 2,647.646 | 8,506.195 | 10 | 50 | 134.714 | 3.213 | no | 2,919.722 | 4,381.878 | 7,724.204 | 9,214.616 | 2,102.200 | 3,226.047 | 2,968.932 | 4,295.011 | 7,224.519 | 10,123.223 | 2,084.952 | 3,205.943 | 0 |
| principal_2021_2025 | sutil | mensual | 75 | Seasonal Naive | 6,074.886 | 7,451.012 | 1.030 | 6,282.973 | 5,034.450 | 10 | 50 | -17.127 | 0.801 | no | 5,156.123 | 6,986.866 | 2,258.682 | 7,927.882 | 5,322.524 | 7,210.509 | 4,854.083 | 7,239.177 | 1,922.459 | 8,266.395 | 4,978.199 | 7,556.079 | 0 |
| principal_2021_2025 | sutil | mensual | 75 | Chronos | 2,648.547 | 3,308.182 | 0.440 | 2,221.552 | 4,783.522 | 10 | 50 | 80.609 | 2.153 | no | 2,171.227 | 3,143.848 | 3,963.015 | 5,640.834 | 1,785.917 | 2,701.404 | 2,242.974 | 3,085.042 | 3,872.532 | 5,844.532 | 1,807.248 | 2,672.979 | 0 |
| principal_2021_2025 | sutil | mensual | 75 | SARIMA | 3,360.787 | 4,122.695 | 0.559 | 3,006.801 | 5,130.719 | 10 | 50 | 52.664 | 1.706 | no | 2,779.970 | 3,970.060 | 3,759.047 | 6,624.060 | 2,443.394 | 3,589.411 | 2,865.760 | 3,885.354 | 3,657.366 | 6,690.155 | 2,559.511 | 3,491.974 | 0 |
| principal_2021_2025 | sutil | mensual | 75 | SARIMA-sel | 3,205.876 | 4,176.530 | 0.540 | 2,859.905 | 4,935.734 | 10 | 50 | 53.959 | 1.726 | no | 2,563.044 | 3,880.304 | 2,865.840 | 7,241.675 | 2,272.051 | 3,469.071 | 2,669.421 | 3,710.457 | 2,683.405 | 7,067.222 | 2,309.427 | 3,366.490 | 0 |
| principal_2021_2025 | sutil | mensual | 75 | Ridge | 4,925.136 | 7,301.277 | 0.834 | 4,198.783 | 8,556.902 | 10 | 50 | 73.739 | 2.038 | no | 3,838.044 | 6,074.414 | 5,483.607 | 12,359.686 | 3,099.084 | 5,330.787 | 3,650.039 | 6,235.715 | 5,298.373 | 11,723.850 | 3,116.154 | 5,375.172 | 0 |
| principal_2021_2025 | sutil | mensual | 75 | ElasticNet | 4,871.911 | 7,050.934 | 0.826 | 4,215.546 | 8,153.740 | 10 | 50 | 67.362 | 1.934 | no | 3,846.717 | 5,950.017 | 5,162.253 | 11,483.777 | 3,171.702 | 5,298.318 | 3,617.416 | 6,153.101 | 5,106.148 | 10,921.977 | 3,103.429 | 5,445.116 | 0 |
| principal_2021_2025 | sutil | mensual | 75 | XGB-37 | 4,881.450 | 5,940.206 | 0.809 | 4,666.700 | 5,955.201 | 10 | 50 | 21.997 | 1.276 | no | 4,062.861 | 5,731.588 | 3,727.308 | 7,964.989 | 3,830.938 | 5,544.032 | 3,848.344 | 5,944.209 | 3,329.505 | 8,559.374 | 3,538.972 | 5,830.265 | 0 |
| principal_2021_2025 | sutil | mensual | 75 | GC3 | 6,361.305 | 8,072.649 | 1.081 | 6,418.674 | 6,074.460 | 10 | 50 | -4.509 | 0.946 | no | 5,292.163 | 7,445.730 | 4,084.502 | 8,216.126 | 5,214.943 | 7,644.425 | 4,846.149 | 7,918.768 | 4,021.677 | 7,941.796 | 4,663.167 | 8,219.104 | 0 |
| principal_2021_2025 | sutil | mensual | 75 | GE | 6,743.530 | 8,647.879 | 1.148 | 6,726.907 | 6,826.646 | 10 | 50 | 1.233 | 1.015 | no | 5,587.118 | 7,894.232 | 4,477.293 | 9,213.462 | 5,454.143 | 8,023.757 | 5,062.121 | 8,442.844 | 4,283.650 | 9,134.532 | 4,812.910 | 8,683.599 | 0 |
| principal_2021_2025 | sutil | mensual | 75 | XGB-43 | 5,011.936 | 6,182.917 | 0.832 | 4,814.886 | 5,997.184 | 10 | 50 | 19.658 | 1.246 | sí | 4,141.407 | 5,916.451 | 3,694.150 | 8,061.511 | 3,901.095 | 5,762.378 | 3,907.445 | 6,149.954 | 3,308.222 | 8,625.450 | 3,575.499 | 6,094.340 | 0 |
| principal_2021_2025 | sutil | mensual | 90 | Naive | 3,624.070 | 4,767.714 | 0.613 | 3,060.565 | 8,695.623 | 6 | 54 | 139.941 | 2.841 | no | 2,919.722 | 4,381.878 | 7,911.685 | 9,294.507 | 2,415.854 | 3,754.245 | 2,968.932 | 4,295.011 | 6,257.397 | 11,552.246 | 2,413.743 | 3,725.345 | 31 |
| principal_2021_2025 | sutil | mensual | 90 | Seasonal Naive | 6,074.886 | 7,451.012 | 1.030 | 5,937.748 | 7,309.129 | 6 | 54 | 20.317 | 1.231 | no | 5,156.123 | 6,986.866 | 3,859.155 | 10,759.103 | 5,020.121 | 6,832.359 | 4,854.083 | 7,239.177 | 2,460.135 | 11,302.885 | 4,706.071 | 7,161.756 | 31 |
| principal_2021_2025 | sutil | mensual | 90 | Chronos | 2,648.547 | 3,308.182 | 0.440 | 2,338.790 | 5,436.358 | 6 | 54 | 105.258 | 2.324 | no | 2,171.227 | 3,143.848 | 5,103.938 | 5,920.272 | 1,895.188 | 2,803.501 | 2,242.974 | 3,085.042 | 3,909.765 | 7,095.921 | 1,926.782 | 2,780.880 | 31 |
| principal_2021_2025 | sutil | mensual | 90 | SARIMA | 3,360.787 | 4,122.695 | 0.559 | 2,982.611 | 6,764.376 | 6 | 54 | 101.274 | 2.268 | no | 2,779.970 | 3,970.060 | 6,620.386 | 6,908.365 | 2,441.112 | 3,557.847 | 2,865.760 | 3,885.354 | 5,062.739 | 8,537.592 | 2,574.059 | 3,404.627 | 31 |
| principal_2021_2025 | sutil | mensual | 90 | SARIMA-sel | 3,205.876 | 4,176.530 | 0.540 | 2,773.687 | 7,095.584 | 6 | 54 | 121.331 | 2.558 | no | 2,563.044 | 3,880.304 | 5,376.504 | 9,494.781 | 2,212.239 | 3,361.217 | 2,669.421 | 3,710.457 | 4,588.068 | 9,688.381 | 2,256.568 | 3,252.306 | 31 |
| principal_2021_2025 | sutil | mensual | 90 | Ridge | 4,925.136 | 7,301.277 | 0.834 | 4,174.378 | 11,681.953 | 6 | 54 | 137.190 | 2.798 | no | 3,838.044 | 6,074.414 | 8,308.570 | 16,651.177 | 3,164.177 | 5,277.668 | 3,650.039 | 6,235.715 | 7,396.811 | 18,399.953 | 3,153.900 | 5,283.063 | 31 |
| principal_2021_2025 | sutil | mensual | 90 | ElasticNet | 4,871.911 | 7,050.934 | 0.826 | 4,206.986 | 10,856.235 | 6 | 54 | 122.833 | 2.581 | no | 3,846.717 | 5,950.017 | 7,818.673 | 14,624.473 | 3,216.794 | 5,280.946 | 3,617.416 | 6,153.101 | 6,928.329 | 16,455.416 | 3,126.173 | 5,393.503 | 31 |
| principal_2021_2025 | sutil | mensual | 90 | XGB-37 | 4,881.450 | 5,940.206 | 0.809 | 4,538.929 | 7,964.134 | 6 | 54 | 63.151 | 1.755 | no | 4,062.861 | 5,731.588 | 7,214.136 | 8,458.830 | 3,737.682 | 5,367.786 | 3,848.344 | 5,944.209 | 4,841.990 | 11,506.706 | 3,480.233 | 5,636.852 | 31 |
| principal_2021_2025 | sutil | mensual | 90 | GC3 | 6,361.305 | 8,072.649 | 1.081 | 6,189.571 | 7,906.910 | 6 | 54 | 24.297 | 1.277 | no | 5,292.163 | 7,445.730 | 5,854.985 | 10,328.172 | 5,066.234 | 7,344.208 | 4,846.149 | 7,918.768 | 5,288.821 | 10,078.984 | 4,554.644 | 7,877.606 | 31 |
| principal_2021_2025 | sutil | mensual | 90 | GE | 6,743.530 | 8,647.879 | 1.148 | 6,499.229 | 8,942.238 | 6 | 54 | 32.605 | 1.376 | no | 5,587.118 | 7,894.232 | 7,223.793 | 11,045.237 | 5,271.770 | 7,725.741 | 5,062.121 | 8,442.844 | 6,042.350 | 11,439.362 | 4,725.152 | 8,356.372 | 31 |
| principal_2021_2025 | sutil | mensual | 90 | XGB-43 | 5,011.936 | 6,182.917 | 0.832 | 4,693.673 | 7,876.301 | 6 | 54 | 57.151 | 1.678 | sí | 4,141.407 | 5,916.451 | 6,879.585 | 8,614.159 | 3,819.828 | 5,595.871 | 3,907.445 | 6,149.954 | 4,637.656 | 11,612.344 | 3,536.176 | 5,911.143 | 31 |
| principal_2021_2025 | sutil | interanual | 50 | Naive | 3,624.070 | 4,767.714 | 0.613 | 3,584.374 | 3,679.645 | 25 | 35 | 1.533 | 1.027 | no | 2,919.722 | 4,381.878 | 2,582.206 | 4,868.071 | 2,674.416 | 4,572.679 | 2,968.932 | 4,295.011 | 2,539.984 | 4,766.864 | 2,680.256 | 4,470.929 | 0 |
| principal_2021_2025 | sutil | interanual | 50 | Seasonal Naive | 6,074.886 | 7,451.012 | 1.030 | 3,230.504 | 10,057.020 | 25 | 35 | 65.551 | 3.113 | no | 5,156.123 | 6,986.866 | 9,067.141 | 11,022.841 | 2,543.342 | 3,911.077 | 4,854.083 | 7,239.177 | 8,827.817 | 11,366.861 | 2,532.891 | 3,937.441 | 0 |
| principal_2021_2025 | sutil | interanual | 50 | Chronos | 2,648.547 | 3,308.182 | 0.440 | 2,260.740 | 3,191.476 | 25 | 35 | 20.499 | 1.412 | no | 2,171.227 | 3,143.848 | 2,490.269 | 3,907.130 | 1,766.994 | 2,798.093 | 2,242.974 | 3,085.042 | 2,412.708 | 4,065.748 | 1,872.583 | 2,644.460 | 0 |
| principal_2021_2025 | sutil | interanual | 50 | SARIMA | 3,360.787 | 4,122.695 | 0.559 | 2,945.765 | 3,941.818 | 25 | 35 | 17.289 | 1.338 | no | 2,779.970 | 3,970.060 | 3,034.939 | 4,853.181 | 2,298.880 | 3,591.270 | 2,865.760 | 3,885.354 | 3,121.556 | 4,752.210 | 2,360.894 | 3,580.186 | 0 |
| principal_2021_2025 | sutil | interanual | 50 | SARIMA-sel | 3,205.876 | 4,176.530 | 0.540 | 2,593.306 | 4,063.475 | 25 | 35 | 26.751 | 1.567 | no | 2,563.044 | 3,880.304 | 2,866.736 | 5,351.720 | 2,077.350 | 3,113.651 | 2,669.421 | 3,710.457 | 3,084.088 | 4,964.310 | 2,179.532 | 2,955.046 | 0 |
| principal_2021_2025 | sutil | interanual | 50 | Ridge | 4,925.136 | 7,301.277 | 0.834 | 4,275.683 | 5,834.370 | 25 | 35 | 18.461 | 1.365 | no | 3,838.044 | 6,074.414 | 4,424.178 | 7,436.860 | 2,761.695 | 5,917.207 | 3,650.039 | 6,235.715 | 3,932.119 | 7,827.388 | 2,539.547 | 6,371.999 | 0 |
| principal_2021_2025 | sutil | interanual | 50 | ElasticNet | 4,871.911 | 7,050.934 | 0.826 | 4,013.974 | 6,073.024 | 25 | 35 | 24.654 | 1.513 | no | 3,846.717 | 5,950.017 | 4,705.236 | 7,627.863 | 2,593.140 | 5,557.787 | 3,617.416 | 6,153.101 | 4,091.731 | 8,128.176 | 2,390.988 | 5,923.078 | 0 |
| principal_2021_2025 | sutil | interanual | 50 | XGB-37 | 4,881.450 | 5,940.206 | 0.809 | 4,664.206 | 5,185.590 | 25 | 35 | 6.231 | 1.112 | no | 4,062.861 | 5,731.588 | 3,824.455 | 6,603.144 | 3,750.811 | 5,595.992 | 3,848.344 | 5,944.209 | 3,443.258 | 6,924.698 | 3,688.538 | 5,671.965 | 0 |
| principal_2021_2025 | sutil | interanual | 50 | GC3 | 6,361.305 | 8,072.649 | 1.081 | 5,441.224 | 7,649.418 | 25 | 35 | 20.249 | 1.406 | no | 5,292.163 | 7,445.730 | 5,899.947 | 9,482.745 | 4,235.675 | 6,653.980 | 4,846.149 | 7,918.768 | 5,203.443 | 10,340.799 | 3,926.518 | 6,941.372 | 0 |
| principal_2021_2025 | sutil | interanual | 50 | GE | 6,743.530 | 8,647.879 | 1.148 | 6,103.622 | 7,639.401 | 25 | 35 | 13.285 | 1.252 | no | 5,587.118 | 7,894.232 | 5,857.452 | 9,461.212 | 4,712.968 | 7,479.366 | 5,062.121 | 8,442.844 | 5,200.101 | 10,409.609 | 4,146.757 | 7,954.500 | 0 |
| principal_2021_2025 | sutil | interanual | 50 | XGB-43 | 5,011.936 | 6,182.917 | 0.832 | 4,873.718 | 5,205.440 | 25 | 35 | 3.861 | 1.068 | sí | 4,141.407 | 5,916.451 | 3,690.877 | 6,798.222 | 3,913.754 | 5,847.961 | 3,907.445 | 6,149.954 | 3,301.349 | 7,176.142 | 3,850.454 | 5,921.475 | 0 |
| principal_2021_2025 | sutil | interanual | 60 | Naive | 3,624.070 | 4,767.714 | 0.613 | 3,731.418 | 3,373.593 | 18 | 42 | -6.911 | 0.904 | no | 2,919.722 | 4,381.878 | 2,165.765 | 4,677.098 | 2,897.654 | 4,646.219 | 2,968.932 | 4,295.011 | 1,842.521 | 4,816.004 | 2,921.130 | 4,562.754 | 0 |
| principal_2021_2025 | sutil | interanual | 60 | Seasonal Naive | 6,074.886 | 7,451.012 | 1.030 | 3,979.951 | 10,963.068 | 18 | 42 | 80.465 | 2.755 | no | 5,156.123 | 6,986.866 | 9,671.698 | 12,264.451 | 3,207.128 | 4,778.543 | 4,854.083 | 7,239.177 | 9,489.867 | 12,666.525 | 3,126.256 | 4,852.535 | 0 |
| principal_2021_2025 | sutil | interanual | 60 | Chronos | 2,648.547 | 3,308.182 | 0.440 | 2,622.027 | 2,710.426 | 18 | 42 | 2.336 | 1.034 | no | 2,171.227 | 3,143.848 | 2,014.148 | 3,429.097 | 2,074.663 | 3,210.355 | 2,242.974 | 3,085.042 | 1,828.584 | 3,607.243 | 2,210.348 | 3,054.399 | 0 |
| principal_2021_2025 | sutil | interanual | 60 | SARIMA | 3,360.787 | 4,122.695 | 0.559 | 3,229.992 | 3,665.977 | 18 | 42 | 9.081 | 1.135 | no | 2,779.970 | 3,970.060 | 2,653.266 | 4,648.561 | 2,563.444 | 3,939.992 | 2,865.760 | 3,885.354 | 2,645.828 | 4,553.776 | 2,611.081 | 3,925.586 | 0 |
| principal_2021_2025 | sutil | interanual | 60 | SARIMA-sel | 3,205.876 | 4,176.530 | 0.540 | 2,767.860 | 4,227.914 | 18 | 42 | 31.880 | 1.528 | no | 2,563.044 | 3,880.304 | 2,835.157 | 5,681.795 | 2,143.471 | 3,437.607 | 2,669.421 | 3,710.457 | 3,081.529 | 5,224.343 | 2,201.313 | 3,318.630 | 0 |
| principal_2021_2025 | sutil | interanual | 60 | Ridge | 4,925.136 | 7,301.277 | 0.834 | 4,510.217 | 5,893.281 | 18 | 42 | 19.657 | 1.307 | no | 3,838.044 | 6,074.414 | 4,087.816 | 8,024.128 | 3,203.480 | 5,906.746 | 3,650.039 | 6,235.715 | 3,186.056 | 8,670.886 | 3,022.304 | 6,250.637 | 0 |
| principal_2021_2025 | sutil | interanual | 60 | ElasticNet | 4,871.911 | 7,050.934 | 0.826 | 4,298.879 | 6,208.986 | 18 | 42 | 27.445 | 1.444 | no | 3,846.717 | 5,950.017 | 4,412.451 | 8,264.171 | 3,084.860 | 5,587.250 | 3,617.416 | 6,153.101 | 3,353.115 | 9,105.463 | 2,890.102 | 5,863.228 | 0 |
| principal_2021_2025 | sutil | interanual | 60 | XGB-37 | 4,881.450 | 5,940.206 | 0.809 | 4,825.783 | 5,011.340 | 18 | 42 | 2.661 | 1.038 | no | 4,062.861 | 5,731.588 | 3,499.011 | 6,590.528 | 3,866.362 | 5,812.051 | 3,848.344 | 5,944.209 | 3,041.558 | 7,203.795 | 3,702.645 | 6,049.498 | 0 |
| principal_2021_2025 | sutil | interanual | 60 | GC3 | 6,361.305 | 8,072.649 | 1.081 | 5,671.876 | 7,969.970 | 18 | 42 | 25.288 | 1.405 | no | 5,292.163 | 7,445.730 | 5,806.919 | 10,317.776 | 4,576.199 | 6,770.614 | 4,846.149 | 7,918.768 | 4,729.952 | 11,655.073 | 4,322.796 | 7,105.887 | 0 |
| principal_2021_2025 | sutil | interanual | 60 | GE | 6,743.530 | 8,647.879 | 1.148 | 6,131.721 | 8,171.084 | 18 | 42 | 21.169 | 1.333 | no | 5,587.118 | 7,894.232 | 6,093.546 | 10,404.821 | 4,812.820 | 7,453.914 | 5,062.121 | 8,442.844 | 5,137.633 | 11,858.859 | 4,323.434 | 7,980.110 | 0 |
| principal_2021_2025 | sutil | interanual | 60 | XGB-43 | 5,011.936 | 6,182.917 | 0.832 | 4,982.437 | 5,080.766 | 18 | 42 | 1.373 | 1.020 | sí | 4,141.407 | 5,916.451 | 3,353.535 | 6,870.759 | 3,986.587 | 6,006.437 | 3,907.445 | 6,149.954 | 2,889.991 | 7,614.629 | 3,798.172 | 6,253.422 | 0 |
| principal_2021_2025 | sutil | interanual | 75 | Naive | 3,624.070 | 4,767.714 | 0.613 | 3,714.515 | 3,171.846 | 10 | 50 | -12.478 | 0.854 | no | 2,919.722 | 4,381.878 | 1,674.215 | 4,943.924 | 2,933.888 | 4,552.344 | 2,968.932 | 4,295.011 | 911.823 | 5,028.360 | 3,005.501 | 4,421.988 | 4 |
| principal_2021_2025 | sutil | interanual | 75 | Seasonal Naive | 6,074.886 | 7,451.012 | 1.030 | 4,788.250 | 12,508.067 | 10 | 50 | 105.898 | 2.612 | no | 5,156.123 | 6,986.866 | 10,423.461 | 14,592.681 | 3,939.244 | 5,598.608 | 4,854.083 | 7,239.177 | 10,128.749 | 14,724.638 | 3,731.796 | 5,822.696 | 4 |
| principal_2021_2025 | sutil | interanual | 75 | Chronos | 2,648.547 | 3,308.182 | 0.440 | 2,805.433 | 1,864.113 | 10 | 50 | -29.618 | 0.664 | no | 2,171.227 | 3,143.848 | 1,419.839 | 2,317.092 | 2,259.893 | 3,363.643 | 2,242.974 | 3,085.042 | 968.800 | 2,699.416 | 2,326.122 | 3,309.712 | 4 |
| principal_2021_2025 | sutil | interanual | 75 | SARIMA | 3,360.787 | 4,122.695 | 0.559 | 3,386.401 | 3,232.720 | 10 | 50 | -3.811 | 0.955 | no | 2,779.970 | 3,970.060 | 2,430.059 | 3,968.468 | 2,705.234 | 4,089.601 | 2,865.760 | 3,885.354 | 2,309.603 | 3,908.984 | 2,803.863 | 4,020.908 | 4 |
| principal_2021_2025 | sutil | interanual | 75 | SARIMA-sel | 3,205.876 | 4,176.530 | 0.540 | 3,031.286 | 4,078.830 | 10 | 50 | 27.230 | 1.346 | no | 2,563.044 | 3,880.304 | 2,145.130 | 6,098.922 | 2,388.735 | 3,711.174 | 2,669.421 | 3,710.457 | 2,267.929 | 5,730.660 | 2,475.700 | 3,554.470 | 4 |
| principal_2021_2025 | sutil | interanual | 75 | Ridge | 4,925.136 | 7,301.277 | 0.834 | 4,920.950 | 4,946.068 | 10 | 50 | 0.425 | 1.005 | no | 3,838.044 | 6,074.414 | 3,290.048 | 6,789.016 | 3,665.151 | 6,281.205 | 3,650.039 | 6,235.715 | 1,700.903 | 8,428.557 | 3,697.073 | 6,302.944 | 4 |
| principal_2021_2025 | sutil | interanual | 75 | ElasticNet | 4,871.911 | 7,050.934 | 0.826 | 4,765.549 | 5,403.723 | 10 | 50 | 10.916 | 1.134 | no | 3,846.717 | 5,950.017 | 3,428.325 | 7,594.067 | 3,620.919 | 6,005.907 | 3,617.416 | 6,153.101 | 1,872.155 | 9,347.228 | 3,620.771 | 5,996.936 | 4 |
| principal_2021_2025 | sutil | interanual | 75 | XGB-37 | 4,881.450 | 5,940.206 | 0.809 | 4,894.443 | 4,816.485 | 10 | 50 | -1.331 | 0.984 | no | 4,062.861 | 5,731.588 | 2,547.727 | 7,253.853 | 4,047.314 | 5,780.562 | 3,848.344 | 5,944.209 | 1,543.294 | 8,603.474 | 3,909.222 | 5,898.652 | 4 |
| principal_2021_2025 | sutil | interanual | 75 | GC3 | 6,361.305 | 8,072.649 | 1.081 | 5,800.342 | 9,166.116 | 10 | 50 | 44.092 | 1.580 | no | 5,292.163 | 7,445.730 | 5,191.821 | 13,365.038 | 4,839.332 | 6,779.257 | 4,846.149 | 7,918.768 | 3,513.443 | 15,772.329 | 4,617.685 | 7,028.602 | 4 |
| principal_2021_2025 | sutil | interanual | 75 | GE | 6,743.530 | 8,647.879 | 1.148 | 6,133.031 | 9,796.027 | 10 | 50 | 45.266 | 1.597 | no | 5,587.118 | 7,894.232 | 6,024.869 | 13,767.112 | 4,988.480 | 7,245.037 | 5,062.121 | 8,442.844 | 4,574.157 | 16,061.393 | 4,630.863 | 7,645.213 | 4 |
| principal_2021_2025 | sutil | interanual | 75 | XGB-43 | 5,011.936 | 6,182.917 | 0.832 | 5,010.110 | 5,021.063 | 10 | 50 | 0.182 | 1.002 | sí | 4,141.407 | 5,916.451 | 2,451.818 | 7,798.984 | 4,115.810 | 5,933.254 | 3,907.445 | 6,149.954 | 1,482.035 | 9,423.545 | 3,976.085 | 6,051.719 | 4 |
| principal_2021_2025 | sutil | interanual | 90 | Naive | 3,624.070 | 4,767.714 | 0.613 | 3,773.008 | 1,538.943 | 4 | 56 | -57.536 | 0.408 | no | 2,919.722 | 4,381.878 | 426.541 | 3,220.365 | 3,022.330 | 4,590.466 | 2,968.932 | 4,295.011 | 478.200 | 2,979.033 | 3,096.044 | 4,468.662 | 136 |
| principal_2021_2025 | sutil | interanual | 90 | Seasonal Naive | 6,074.886 | 7,451.012 | 1.030 | 5,418.896 | 15,258.750 | 4 | 56 | 151.178 | 2.816 | no | 5,156.123 | 6,986.866 | 12,120.610 | 17,401.499 | 4,558.230 | 6,255.334 | 4,854.083 | 7,239.177 | 12,225.283 | 17,485.031 | 4,373.669 | 6,399.475 | 136 |
| principal_2021_2025 | sutil | interanual | 90 | Chronos | 2,648.547 | 3,308.182 | 0.440 | 2,758.000 | 1,116.204 | 4 | 56 | -57.856 | 0.405 | no | 2,171.227 | 3,143.848 | 605.768 | 1,469.441 | 2,268.761 | 3,292.917 | 2,242.974 | 3,085.042 | 617.717 | 1,478.782 | 2,343.410 | 3,203.991 | 136 |
| principal_2021_2025 | sutil | interanual | 90 | SARIMA | 3,360.787 | 4,122.695 | 0.559 | 3,334.741 | 3,725.435 | 4 | 56 | 10.850 | 1.117 | no | 2,779.970 | 3,970.060 | 2,832.216 | 4,533.901 | 2,710.639 | 3,987.484 | 2,865.760 | 3,885.354 | 2,797.232 | 4,597.135 | 2,803.453 | 3,891.636 | 136 |
| principal_2021_2025 | sutil | interanual | 90 | SARIMA-sel | 3,205.876 | 4,176.530 | 0.540 | 3,041.554 | 5,506.388 | 4 | 56 | 71.759 | 1.810 | no | 2,563.044 | 3,880.304 | 3,483.781 | 7,463.792 | 2,404.696 | 3,722.854 | 2,669.421 | 3,710.457 | 3,618.828 | 7,393.948 | 2,480.341 | 3,568.184 | 136 |
| principal_2021_2025 | sutil | interanual | 90 | Ridge | 4,925.136 | 7,301.277 | 0.834 | 4,979.138 | 4,169.104 | 4 | 56 | -15.350 | 0.837 | no | 3,838.044 | 6,074.414 | 1,817.620 | 6,562.733 | 3,833.319 | 6,199.861 | 3,650.039 | 6,235.715 | 1,647.693 | 7,005.229 | 3,664.499 | 6,322.165 | 136 |
| principal_2021_2025 | sutil | interanual | 90 | ElasticNet | 4,871.911 | 7,050.934 | 0.826 | 4,875.783 | 4,817.704 | 4 | 56 | -1.113 | 0.988 | no | 3,846.717 | 5,950.017 | 1,909.354 | 7,726.055 | 3,789.860 | 6,014.026 | 3,617.416 | 6,153.101 | 1,708.183 | 8,246.874 | 3,619.017 | 6,157.200 | 136 |
| principal_2021_2025 | sutil | interanual | 90 | XGB-37 | 4,881.450 | 5,940.206 | 0.809 | 4,833.290 | 5,555.691 | 4 | 56 | 13.812 | 1.149 | no | 4,062.861 | 5,731.588 | 1,146.511 | 9,964.871 | 4,014.904 | 5,666.317 | 3,848.344 | 5,944.209 | 925.288 | 10,676.534 | 3,873.350 | 5,822.135 | 136 |
| principal_2021_2025 | sutil | interanual | 90 | GC3 | 6,361.305 | 8,072.649 | 1.081 | 6,086.282 | 10,211.615 | 4 | 56 | 60.527 | 1.678 | no | 5,292.163 | 7,445.730 | 3,003.241 | 17,419.988 | 5,073.721 | 7,120.135 | 4,846.149 | 7,918.768 | 2,813.075 | 18,024.089 | 4,769.867 | 7,489.894 | 136 |
| principal_2021_2025 | sutil | interanual | 90 | GE | 6,743.530 | 8,647.879 | 1.148 | 6,418.112 | 11,299.378 | 4 | 56 | 67.559 | 1.761 | no | 5,587.118 | 7,894.232 | 4,602.185 | 17,996.571 | 5,285.361 | 7,540.333 | 5,062.121 | 8,442.844 | 4,357.755 | 18,579.076 | 4,867.370 | 7,985.926 | 136 |
| principal_2021_2025 | sutil | interanual | 90 | XGB-43 | 5,011.936 | 6,182.917 | 0.832 | 4,939.374 | 6,027.801 | 4 | 56 | 20.269 | 1.220 | sí | 4,141.407 | 5,916.451 | 1,304.236 | 10,751.366 | 4,067.942 | 5,829.429 | 3,907.445 | 6,149.954 | 1,095.744 | 11,520.714 | 3,918.233 | 6,001.292 | 136 |
| principal_2021_2025 | dulce | mensual | 50 | Naive | 77.522 | 91.306 | 2.946 | 42.965 | 117.017 | 28 | 32 | 50.946 | 2.724 | no | 65.688 | 89.905 | 103.188 | 131.062 | 35.247 | 50.630 | 66.298 | 89.249 | 102.981 | 131.072 | 35.770 | 49.915 | 0 |
| principal_2021_2025 | dulce | mensual | 50 | Seasonal Naive | 24.503 | 31.560 | 0.945 | 28.123 | 20.366 | 28 | 32 | -16.885 | 0.724 | no | 20.537 | 28.979 | 16.607 | 24.185 | 21.779 | 35.036 | 19.899 | 29.211 | 15.940 | 24.745 | 20.881 | 35.945 | 0 |
| principal_2021_2025 | dulce | mensual | 50 | Chronos | 30.819 | 37.908 | 1.184 | 23.258 | 39.460 | 28 | 32 | 28.038 | 1.697 | no | 25.644 | 36.427 | 31.576 | 47.421 | 17.567 | 29.766 | 25.446 | 36.246 | 30.710 | 47.871 | 18.298 | 28.804 | 0 |
| principal_2021_2025 | dulce | mensual | 50 | SARIMA | 18.412 | 25.213 | 0.709 | 21.721 | 14.631 | 28 | 32 | -20.538 | 0.674 | no | 14.516 | 22.828 | 10.604 | 18.868 | 15.489 | 28.611 | 14.513 | 22.705 | 11.283 | 18.377 | 15.739 | 28.357 | 0 |
| principal_2021_2025 | dulce | mensual | 50 | SARIMA-sel | 20.629 | 27.520 | 0.773 | 23.320 | 17.553 | 28 | 32 | -14.910 | 0.753 | no | 16.546 | 25.179 | 13.905 | 21.140 | 16.506 | 30.932 | 16.468 | 25.101 | 13.869 | 21.171 | 16.226 | 31.021 | 0 |
| principal_2021_2025 | dulce | mensual | 50 | Ridge | 53.070 | 69.467 | 2.041 | 48.978 | 57.746 | 28 | 32 | 8.811 | 1.179 | no | 43.414 | 63.396 | 43.413 | 73.928 | 37.150 | 61.409 | 42.720 | 64.230 | 42.011 | 75.437 | 35.751 | 61.613 | 0 |
| principal_2021_2025 | dulce | mensual | 50 | ElasticNet | 50.248 | 65.777 | 1.929 | 46.910 | 54.063 | 28 | 32 | 7.593 | 1.153 | no | 40.681 | 60.405 | 39.460 | 70.303 | 35.399 | 58.766 | 39.594 | 61.546 | 38.301 | 71.830 | 34.119 | 59.248 | 0 |
| principal_2021_2025 | dulce | mensual | 50 | XGB-37 | 48.260 | 60.715 | 1.860 | 48.761 | 47.689 | 28 | 32 | -1.185 | 0.978 | no | 39.821 | 57.204 | 35.482 | 60.465 | 38.644 | 59.806 | 38.270 | 58.630 | 33.760 | 60.256 | 36.276 | 61.920 | 0 |
| principal_2021_2025 | dulce | mensual | 50 | GC3 | 56.669 | 76.445 | 2.221 | 63.224 | 49.178 | 28 | 32 | -13.219 | 0.778 | no | 46.893 | 66.950 | 37.813 | 61.321 | 49.422 | 76.958 | 42.763 | 70.828 | 36.316 | 63.658 | 43.478 | 83.764 | 0 |
| principal_2021_2025 | dulce | mensual | 50 | GE | 56.734 | 75.038 | 2.210 | 64.580 | 47.768 | 28 | 32 | -15.804 | 0.740 | no | 47.499 | 66.693 | 36.858 | 59.735 | 51.333 | 77.904 | 43.640 | 70.235 | 36.325 | 60.470 | 46.067 | 83.666 | 0 |
| principal_2021_2025 | dulce | mensual | 50 | XGB-43 | 47.637 | 59.731 | 1.837 | 47.753 | 47.504 | 28 | 32 | -0.278 | 0.995 | sí | 39.323 | 56.352 | 36.643 | 58.857 | 37.147 | 58.884 | 37.618 | 57.681 | 34.948 | 58.694 | 34.579 | 61.404 | 0 |
| principal_2021_2025 | dulce | mensual | 60 | Naive | 77.522 | 91.306 | 2.946 | 47.968 | 125.066 | 23 | 37 | 61.330 | 2.607 | no | 65.688 | 89.905 | 111.183 | 138.950 | 39.658 | 56.299 | 66.298 | 89.249 | 111.245 | 139.098 | 40.918 | 55.033 | 0 |
| principal_2021_2025 | dulce | mensual | 60 | Seasonal Naive | 24.503 | 31.560 | 0.945 | 26.116 | 21.908 | 23 | 37 | -10.591 | 0.839 | no | 20.537 | 28.979 | 17.738 | 25.954 | 20.343 | 32.669 | 19.899 | 29.211 | 16.855 | 27.100 | 19.656 | 33.245 | 0 |
| principal_2021_2025 | dulce | mensual | 60 | Chronos | 30.819 | 37.908 | 1.184 | 23.906 | 41.940 | 23 | 37 | 36.084 | 1.754 | no | 25.644 | 36.427 | 34.515 | 49.420 | 18.170 | 30.509 | 25.446 | 36.246 | 33.437 | 50.266 | 18.687 | 29.318 | 0 |
| principal_2021_2025 | dulce | mensual | 60 | SARIMA | 18.412 | 25.213 | 0.709 | 21.221 | 13.893 | 23 | 37 | -24.545 | 0.655 | no | 14.516 | 22.828 | 9.939 | 17.954 | 15.628 | 27.554 | 14.513 | 22.705 | 10.235 | 18.167 | 15.440 | 27.482 | 0 |
| principal_2021_2025 | dulce | mensual | 60 | SARIMA-sel | 20.629 | 27.520 | 0.773 | 23.392 | 16.184 | 23 | 37 | -21.546 | 0.692 | no | 16.546 | 25.179 | 12.558 | 19.864 | 17.322 | 30.251 | 16.468 | 25.101 | 11.736 | 20.795 | 16.977 | 30.104 | 0 |
| principal_2021_2025 | dulce | mensual | 60 | Ridge | 53.070 | 69.467 | 2.041 | 50.687 | 56.904 | 23 | 37 | 7.224 | 1.123 | no | 43.414 | 63.396 | 42.418 | 72.662 | 38.774 | 63.302 | 42.720 | 64.230 | 41.504 | 74.029 | 37.725 | 63.849 | 0 |
| principal_2021_2025 | dulce | mensual | 60 | ElasticNet | 50.248 | 65.777 | 1.929 | 47.882 | 54.053 | 23 | 37 | 7.573 | 1.129 | no | 40.681 | 60.405 | 39.533 | 69.948 | 36.163 | 60.169 | 39.594 | 61.546 | 38.126 | 71.226 | 35.060 | 60.785 | 0 |
| principal_2021_2025 | dulce | mensual | 60 | XGB-37 | 48.260 | 60.715 | 1.860 | 45.243 | 53.115 | 23 | 37 | 10.058 | 1.174 | no | 39.821 | 57.204 | 39.600 | 67.273 | 35.740 | 55.788 | 38.270 | 58.630 | 38.269 | 66.284 | 33.469 | 58.423 | 0 |
| principal_2021_2025 | dulce | mensual | 60 | GC3 | 56.669 | 76.445 | 2.221 | 58.797 | 53.247 | 23 | 37 | -6.039 | 0.906 | no | 46.893 | 66.950 | 40.779 | 66.495 | 45.593 | 72.425 | 42.763 | 70.828 | 38.548 | 69.472 | 40.955 | 78.518 | 0 |
| principal_2021_2025 | dulce | mensual | 60 | GE | 56.734 | 75.038 | 2.210 | 60.635 | 50.460 | 23 | 37 | -11.059 | 0.832 | no | 47.499 | 66.693 | 38.130 | 63.939 | 48.039 | 73.520 | 43.640 | 70.235 | 37.269 | 64.914 | 43.827 | 79.021 | 0 |
| principal_2021_2025 | dulce | mensual | 60 | XGB-43 | 47.637 | 59.731 | 1.837 | 44.947 | 51.964 | 23 | 37 | 9.083 | 1.156 | sí | 39.323 | 56.352 | 40.181 | 64.459 | 34.923 | 55.665 | 37.618 | 57.681 | 38.517 | 63.768 | 32.617 | 58.365 | 0 |
| principal_2021_2025 | dulce | mensual | 75 | Naive | 77.522 | 91.306 | 2.946 | 59.489 | 131.622 | 15 | 45 | 69.786 | 2.213 | no | 65.688 | 89.905 | 116.489 | 147.725 | 48.623 | 71.028 | 66.298 | 89.249 | 117.416 | 147.076 | 50.372 | 68.733 | 0 |
| principal_2021_2025 | dulce | mensual | 75 | Seasonal Naive | 24.503 | 31.560 | 0.945 | 24.503 | 24.503 | 15 | 45 | -0.001 | 1.000 | no | 20.537 | 28.979 | 21.438 | 27.759 | 19.332 | 30.183 | 19.899 | 29.211 | 18.781 | 30.415 | 18.241 | 30.910 | 0 |
| principal_2021_2025 | dulce | mensual | 75 | Chronos | 30.819 | 37.908 | 1.184 | 25.025 | 48.199 | 15 | 45 | 56.394 | 1.926 | no | 25.644 | 36.427 | 40.482 | 56.116 | 19.772 | 30.912 | 25.446 | 36.246 | 38.086 | 58.314 | 20.163 | 30.140 | 0 |
| principal_2021_2025 | dulce | mensual | 75 | SARIMA | 18.412 | 25.213 | 0.709 | 19.890 | 13.978 | 15 | 45 | -24.083 | 0.703 | no | 14.516 | 22.828 | 9.758 | 18.018 | 15.022 | 25.476 | 14.513 | 22.705 | 9.724 | 20.095 | 15.130 | 24.961 | 0 |
| principal_2021_2025 | dulce | mensual | 75 | SARIMA-sel | 20.629 | 27.520 | 0.773 | 20.941 | 19.691 | 15 | 45 | -4.547 | 0.940 | no | 16.546 | 25.179 | 15.632 | 23.585 | 15.802 | 26.896 | 16.468 | 25.101 | 13.787 | 27.189 | 15.647 | 26.373 | 0 |
| principal_2021_2025 | dulce | mensual | 75 | Ridge | 53.070 | 69.467 | 2.041 | 47.528 | 69.694 | 15 | 45 | 31.325 | 1.466 | no | 43.414 | 63.396 | 52.015 | 89.292 | 37.203 | 58.225 | 42.720 | 64.230 | 49.013 | 94.689 | 35.859 | 60.060 | 0 |
| principal_2021_2025 | dulce | mensual | 75 | ElasticNet | 50.248 | 65.777 | 1.929 | 44.587 | 67.230 | 15 | 45 | 33.796 | 1.508 | no | 40.681 | 60.405 | 49.536 | 87.146 | 34.428 | 54.977 | 39.594 | 61.546 | 46.773 | 90.956 | 33.367 | 56.812 | 0 |
| principal_2021_2025 | dulce | mensual | 75 | XGB-37 | 48.260 | 60.715 | 1.860 | 42.398 | 65.849 | 15 | 45 | 36.445 | 1.553 | no | 39.821 | 57.204 | 51.553 | 80.606 | 33.278 | 52.504 | 38.270 | 58.630 | 50.425 | 80.300 | 32.358 | 54.277 | 0 |
| principal_2021_2025 | dulce | mensual | 75 | GC3 | 56.669 | 76.445 | 2.221 | 55.310 | 60.748 | 15 | 45 | 7.197 | 1.098 | no | 46.893 | 66.950 | 46.155 | 76.344 | 44.140 | 67.188 | 42.763 | 70.828 | 41.214 | 84.421 | 39.138 | 73.184 | 0 |
| principal_2021_2025 | dulce | mensual | 75 | GE | 56.734 | 75.038 | 2.210 | 56.352 | 57.883 | 15 | 45 | 2.025 | 1.027 | no | 47.499 | 66.693 | 41.773 | 75.240 | 45.520 | 67.739 | 43.640 | 70.235 | 39.812 | 78.907 | 41.267 | 73.118 | 0 |
| principal_2021_2025 | dulce | mensual | 75 | XGB-43 | 47.637 | 59.731 | 1.837 | 42.771 | 62.234 | 15 | 45 | 30.643 | 1.455 | sí | 39.323 | 56.352 | 49.399 | 75.661 | 33.402 | 52.854 | 37.618 | 57.681 | 47.139 | 75.813 | 32.518 | 54.754 | 0 |
| principal_2021_2025 | dulce | mensual | 90 | Naive | 77.522 | 91.306 | 2.946 | 74.504 | 110.728 | 5 | 55 | 42.833 | 1.486 | no | 65.688 | 89.905 | 89.740 | 135.975 | 62.420 | 87.053 | 66.298 | 89.249 | 90.977 | 138.119 | 63.256 | 86.313 | 119 |
| principal_2021_2025 | dulce | mensual | 90 | Seasonal Naive | 24.503 | 31.560 | 0.945 | 24.784 | 21.412 | 5 | 55 | -12.615 | 0.864 | no | 20.537 | 28.979 | 19.537 | 23.097 | 20.570 | 29.562 | 19.899 | 29.211 | 15.517 | 33.240 | 19.749 | 30.067 | 119 |
| principal_2021_2025 | dulce | mensual | 90 | Chronos | 30.819 | 37.908 | 1.184 | 30.164 | 38.023 | 5 | 55 | 23.375 | 1.261 | no | 25.644 | 36.427 | 29.093 | 48.713 | 24.725 | 35.959 | 25.446 | 36.246 | 23.132 | 61.804 | 24.429 | 36.046 | 119 |
| principal_2021_2025 | dulce | mensual | 90 | SARIMA | 18.412 | 25.213 | 0.709 | 19.112 | 10.715 | 5 | 55 | -41.805 | 0.561 | no | 14.516 | 22.828 | 8.826 | 12.021 | 14.920 | 23.864 | 14.513 | 22.705 | 3.808 | 23.571 | 14.822 | 23.771 | 119 |
| principal_2021_2025 | dulce | mensual | 90 | SARIMA-sel | 20.629 | 27.520 | 0.773 | 19.858 | 29.101 | 5 | 55 | 41.071 | 1.465 | no | 16.546 | 25.179 | 23.935 | 34.169 | 15.450 | 24.856 | 16.468 | 25.101 | 17.125 | 36.971 | 15.215 | 24.735 | 119 |
| principal_2021_2025 | dulce | mensual | 90 | Ridge | 53.070 | 69.467 | 2.041 | 53.659 | 46.586 | 5 | 55 | -12.217 | 0.868 | no | 43.414 | 63.396 | 36.435 | 56.026 | 43.341 | 64.570 | 42.720 | 64.230 | 29.839 | 77.378 | 41.948 | 66.231 | 119 |
| principal_2021_2025 | dulce | mensual | 90 | ElasticNet | 50.248 | 65.777 | 1.929 | 50.645 | 45.876 | 5 | 55 | -8.701 | 0.906 | no | 40.681 | 60.405 | 39.565 | 53.610 | 40.484 | 61.457 | 39.594 | 61.546 | 29.585 | 69.308 | 38.822 | 63.265 | 119 |
| principal_2021_2025 | dulce | mensual | 90 | XGB-37 | 48.260 | 60.715 | 1.860 | 47.471 | 56.950 | 5 | 55 | 18.005 | 1.200 | no | 39.821 | 57.204 | 38.684 | 73.866 | 38.519 | 56.894 | 38.270 | 58.630 | 32.464 | 94.008 | 36.332 | 58.886 | 119 |
| principal_2021_2025 | dulce | mensual | 90 | GC3 | 56.669 | 76.445 | 2.221 | 58.237 | 39.424 | 5 | 55 | -30.432 | 0.677 | no | 46.893 | 66.950 | 30.099 | 48.820 | 47.926 | 68.823 | 42.763 | 70.828 | 30.592 | 51.018 | 43.189 | 73.788 | 119 |
| principal_2021_2025 | dulce | mensual | 90 | GE | 56.734 | 75.038 | 2.210 | 58.296 | 39.559 | 5 | 55 | -30.273 | 0.679 | no | 47.499 | 66.693 | 26.383 | 59.959 | 48.302 | 68.515 | 43.640 | 70.235 | 25.915 | 57.977 | 44.153 | 73.070 | 119 |
| principal_2021_2025 | dulce | mensual | 90 | XGB-43 | 47.637 | 59.731 | 1.837 | 47.223 | 52.188 | 5 | 55 | 9.554 | 1.105 | sí | 39.323 | 56.352 | 37.856 | 65.972 | 38.297 | 56.508 | 37.618 | 57.681 | 32.622 | 83.543 | 36.231 | 58.436 | 119 |
| principal_2021_2025 | dulce | interanual | 50 | Naive | 77.522 | 91.306 | 2.946 | 73.995 | 81.292 | 29 | 31 | 4.863 | 1.099 | no | 65.688 | 89.905 | 64.124 | 98.634 | 57.871 | 91.310 | 66.298 | 89.249 | 67.179 | 95.896 | 58.252 | 90.609 | 0 |
| principal_2021_2025 | dulce | interanual | 50 | Seasonal Naive | 24.503 | 31.560 | 0.945 | 12.246 | 37.605 | 29 | 31 | 53.471 | 3.071 | no | 20.537 | 28.979 | 31.825 | 44.911 | 9.375 | 15.295 | 19.899 | 29.211 | 30.887 | 45.723 | 9.135 | 15.674 | 0 |
| principal_2021_2025 | dulce | interanual | 50 | Chronos | 30.819 | 37.908 | 1.184 | 29.952 | 31.745 | 29 | 31 | 3.006 | 1.060 | no | 25.644 | 36.427 | 24.204 | 40.042 | 23.551 | 36.787 | 25.446 | 36.246 | 24.482 | 39.460 | 22.901 | 36.620 | 0 |
| principal_2021_2025 | dulce | interanual | 50 | SARIMA | 18.412 | 25.213 | 0.709 | 12.986 | 24.212 | 29 | 31 | 31.500 | 1.864 | no | 14.516 | 22.828 | 17.551 | 31.939 | 9.668 | 16.647 | 14.513 | 22.705 | 17.878 | 31.978 | 9.438 | 16.826 | 0 |
| principal_2021_2025 | dulce | interanual | 50 | SARIMA-sel | 20.629 | 27.520 | 0.773 | 16.679 | 24.851 | 29 | 31 | 20.467 | 1.490 | no | 16.546 | 25.179 | 17.960 | 32.687 | 12.598 | 20.837 | 16.468 | 25.101 | 18.202 | 32.453 | 12.176 | 21.562 | 0 |
| principal_2021_2025 | dulce | interanual | 50 | Ridge | 53.070 | 69.467 | 2.041 | 41.994 | 64.909 | 29 | 31 | 22.310 | 1.546 | no | 43.414 | 63.396 | 50.724 | 79.228 | 29.855 | 55.781 | 42.720 | 64.230 | 51.694 | 80.854 | 29.183 | 56.403 | 0 |
| principal_2021_2025 | dulce | interanual | 50 | ElasticNet | 50.248 | 65.777 | 1.929 | 41.620 | 59.471 | 29 | 31 | 18.356 | 1.429 | no | 40.681 | 60.405 | 45.289 | 74.169 | 29.823 | 54.940 | 39.594 | 61.546 | 46.194 | 75.454 | 29.026 | 55.592 | 0 |
| principal_2021_2025 | dulce | interanual | 50 | XGB-37 | 48.260 | 60.715 | 1.860 | 43.762 | 53.069 | 29 | 31 | 9.964 | 1.213 | no | 39.821 | 57.204 | 40.053 | 66.744 | 33.643 | 54.117 | 38.270 | 58.630 | 39.259 | 68.319 | 32.476 | 55.407 | 0 |
| principal_2021_2025 | dulce | interanual | 50 | GC3 | 56.669 | 76.445 | 2.221 | 46.880 | 67.134 | 29 | 31 | 18.467 | 1.432 | no | 46.893 | 66.950 | 53.606 | 81.561 | 35.219 | 59.786 | 42.763 | 70.828 | 49.497 | 86.535 | 33.025 | 62.997 | 0 |
| principal_2021_2025 | dulce | interanual | 50 | GE | 56.734 | 75.038 | 2.210 | 49.094 | 64.902 | 29 | 31 | 14.397 | 1.322 | no | 47.499 | 66.693 | 51.864 | 78.897 | 37.807 | 61.663 | 43.640 | 70.235 | 48.912 | 82.753 | 35.759 | 64.422 | 0 |
| principal_2021_2025 | dulce | interanual | 50 | XGB-43 | 47.637 | 59.731 | 1.837 | 44.749 | 50.724 | 29 | 31 | 6.480 | 1.134 | sí | 39.323 | 56.352 | 37.737 | 64.487 | 35.133 | 54.550 | 37.618 | 57.681 | 36.735 | 65.821 | 34.196 | 55.510 | 0 |
| principal_2021_2025 | dulce | interanual | 60 | Naive | 77.522 | 91.306 | 2.946 | 76.906 | 78.514 | 23 | 37 | 1.279 | 1.021 | no | 65.688 | 89.905 | 59.937 | 97.497 | 61.984 | 92.493 | 66.298 | 89.249 | 63.822 | 94.605 | 62.454 | 91.965 | 0 |
| principal_2021_2025 | dulce | interanual | 60 | Seasonal Naive | 24.503 | 31.560 | 0.945 | 14.832 | 40.061 | 23 | 37 | 63.494 | 2.701 | no | 20.537 | 28.979 | 33.184 | 49.271 | 11.691 | 18.077 | 19.899 | 29.211 | 32.022 | 49.326 | 10.959 | 18.948 | 0 |
| principal_2021_2025 | dulce | interanual | 60 | Chronos | 30.819 | 37.908 | 1.184 | 31.097 | 30.371 | 23 | 37 | -1.454 | 0.977 | no | 25.644 | 36.427 | 21.723 | 40.197 | 25.259 | 37.185 | 25.446 | 36.246 | 22.763 | 39.392 | 25.069 | 37.071 | 0 |
| principal_2021_2025 | dulce | interanual | 60 | SARIMA | 18.412 | 25.213 | 0.709 | 12.979 | 27.152 | 23 | 37 | 47.471 | 2.092 | no | 14.516 | 22.828 | 18.970 | 36.784 | 10.090 | 16.093 | 14.513 | 22.705 | 19.557 | 35.668 | 9.933 | 16.269 | 0 |
| principal_2021_2025 | dulce | interanual | 60 | SARIMA-sel | 20.629 | 27.520 | 0.773 | 17.050 | 26.385 | 23 | 37 | 27.905 | 1.547 | no | 16.546 | 25.179 | 18.513 | 36.001 | 13.479 | 20.645 | 16.468 | 25.101 | 18.980 | 34.805 | 13.223 | 21.090 | 0 |
| principal_2021_2025 | dulce | interanual | 60 | Ridge | 53.070 | 69.467 | 2.041 | 44.697 | 66.540 | 23 | 37 | 25.381 | 1.489 | no | 43.414 | 63.396 | 50.727 | 82.585 | 33.337 | 57.735 | 42.720 | 64.230 | 50.907 | 86.335 | 32.242 | 57.981 | 0 |
| principal_2021_2025 | dulce | interanual | 60 | ElasticNet | 50.248 | 65.777 | 1.929 | 44.298 | 59.820 | 23 | 37 | 19.050 | 1.350 | no | 40.681 | 60.405 | 43.701 | 76.500 | 33.186 | 56.918 | 39.594 | 61.546 | 44.248 | 79.954 | 32.043 | 57.397 | 0 |
| principal_2021_2025 | dulce | interanual | 60 | XGB-37 | 48.260 | 60.715 | 1.860 | 46.716 | 50.745 | 23 | 37 | 5.149 | 1.086 | no | 39.821 | 57.204 | 37.060 | 65.920 | 36.248 | 57.493 | 38.270 | 58.630 | 36.728 | 68.163 | 35.484 | 58.288 | 0 |
| principal_2021_2025 | dulce | interanual | 60 | GC3 | 56.669 | 76.445 | 2.221 | 51.277 | 65.344 | 23 | 37 | 15.308 | 1.274 | no | 46.893 | 66.950 | 50.936 | 80.870 | 38.866 | 64.242 | 42.763 | 70.828 | 47.871 | 85.513 | 36.051 | 67.466 | 0 |
| principal_2021_2025 | dulce | interanual | 60 | GE | 56.734 | 75.038 | 2.210 | 53.024 | 62.704 | 23 | 37 | 10.521 | 1.183 | no | 47.499 | 66.693 | 49.365 | 77.374 | 40.850 | 65.545 | 43.640 | 70.235 | 47.739 | 80.761 | 38.416 | 68.812 | 0 |
| principal_2021_2025 | dulce | interanual | 60 | XGB-43 | 47.637 | 59.731 | 1.837 | 47.827 | 47.331 | 23 | 37 | -0.642 | 0.990 | sí | 39.323 | 56.352 | 33.571 | 62.539 | 38.065 | 57.906 | 37.618 | 57.681 | 33.592 | 64.454 | 37.202 | 58.652 | 0 |
| principal_2021_2025 | dulce | interanual | 75 | Naive | 77.522 | 91.306 | 2.946 | 75.467 | 83.176 | 16 | 44 | 7.293 | 1.102 | no | 65.688 | 89.905 | 60.102 | 107.494 | 61.795 | 89.477 | 66.298 | 89.249 | 64.604 | 106.489 | 61.380 | 90.051 | 0 |
| principal_2021_2025 | dulce | interanual | 75 | Seasonal Naive | 24.503 | 31.560 | 0.945 | 17.998 | 42.393 | 16 | 44 | 73.010 | 2.355 | no | 20.537 | 28.979 | 32.978 | 55.016 | 14.479 | 21.533 | 19.899 | 29.211 | 31.265 | 54.741 | 13.381 | 22.446 | 0 |
| principal_2021_2025 | dulce | interanual | 75 | Chronos | 30.819 | 37.908 | 1.184 | 29.955 | 33.195 | 16 | 44 | 7.711 | 1.108 | no | 25.644 | 36.427 | 21.193 | 46.096 | 24.676 | 35.327 | 25.446 | 36.246 | 23.195 | 47.369 | 23.977 | 35.621 | 0 |
| principal_2021_2025 | dulce | interanual | 75 | SARIMA | 18.412 | 25.213 | 0.709 | 15.147 | 27.391 | 16 | 44 | 48.764 | 1.808 | no | 14.516 | 22.828 | 15.951 | 40.466 | 12.105 | 18.350 | 14.513 | 22.705 | 16.444 | 38.896 | 12.166 | 18.149 | 0 |
| principal_2021_2025 | dulce | interanual | 75 | SARIMA-sel | 20.629 | 27.520 | 0.773 | 17.811 | 28.377 | 16 | 44 | 37.560 | 1.593 | no | 16.546 | 25.179 | 17.253 | 41.215 | 14.222 | 21.412 | 16.468 | 25.101 | 17.564 | 39.578 | 14.102 | 21.492 | 0 |
| principal_2021_2025 | dulce | interanual | 75 | Ridge | 53.070 | 69.467 | 2.041 | 48.216 | 66.417 | 16 | 44 | 25.150 | 1.377 | no | 43.414 | 63.396 | 47.686 | 85.109 | 37.875 | 59.276 | 42.720 | 64.230 | 50.400 | 91.829 | 35.048 | 61.450 | 0 |
| principal_2021_2025 | dulce | interanual | 75 | ElasticNet | 50.248 | 65.777 | 1.929 | 47.676 | 57.322 | 16 | 44 | 14.078 | 1.202 | no | 40.681 | 60.405 | 38.236 | 77.129 | 37.592 | 58.417 | 39.594 | 61.546 | 42.479 | 81.825 | 34.754 | 60.616 | 0 |
| principal_2021_2025 | dulce | interanual | 75 | XGB-37 | 48.260 | 60.715 | 1.860 | 50.424 | 42.312 | 16 | 44 | -12.327 | 0.839 | no | 39.821 | 57.204 | 29.579 | 54.635 | 40.636 | 60.521 | 38.270 | 58.630 | 32.035 | 58.085 | 38.127 | 62.174 | 0 |
| principal_2021_2025 | dulce | interanual | 75 | GC3 | 56.669 | 76.445 | 2.221 | 56.116 | 58.191 | 16 | 44 | 2.686 | 1.037 | no | 46.893 | 66.950 | 42.990 | 74.380 | 44.432 | 67.892 | 42.763 | 70.828 | 40.888 | 76.415 | 38.277 | 73.778 | 0 |
| principal_2021_2025 | dulce | interanual | 75 | GE | 56.734 | 75.038 | 2.210 | 56.979 | 56.062 | 16 | 44 | -1.185 | 0.984 | no | 47.499 | 66.693 | 42.537 | 70.729 | 45.450 | 68.584 | 43.640 | 70.235 | 42.606 | 71.828 | 40.270 | 73.704 | 0 |
| principal_2021_2025 | dulce | interanual | 75 | XGB-43 | 47.637 | 59.731 | 1.837 | 50.613 | 39.452 | 16 | 44 | -17.181 | 0.779 | sí | 39.323 | 56.352 | 26.318 | 52.588 | 41.344 | 60.035 | 37.618 | 57.681 | 28.735 | 54.523 | 38.889 | 61.762 | 0 |
| principal_2021_2025 | dulce | interanual | 90 | Naive | 77.522 | 91.306 | 2.946 | 78.755 | 60.260 | 4 | 56 | -22.268 | 0.765 | no | 65.688 | 89.905 | 56.488 | 64.032 | 66.339 | 91.760 | 66.298 | 89.249 | 41.090 | 71.230 | 66.782 | 91.339 | 188 |
| principal_2021_2025 | dulce | interanual | 90 | Seasonal Naive | 24.503 | 31.560 | 0.945 | 21.350 | 68.645 | 4 | 56 | 180.149 | 3.215 | no | 20.537 | 28.979 | 51.164 | 86.126 | 18.305 | 24.481 | 19.899 | 29.211 | 31.720 | 98.056 | 17.509 | 25.074 | 188 |
| principal_2021_2025 | dulce | interanual | 90 | Chronos | 30.819 | 37.908 | 1.184 | 30.752 | 31.748 | 4 | 56 | 3.014 | 1.032 | no | 25.644 | 36.427 | 5.998 | 57.497 | 25.772 | 35.734 | 25.446 | 36.246 | 1.575 | 68.669 | 25.278 | 36.291 | 188 |
| principal_2021_2025 | dulce | interanual | 90 | SARIMA | 18.412 | 25.213 | 0.709 | 15.494 | 59.264 | 4 | 56 | 221.877 | 3.825 | no | 14.516 | 22.828 | 43.959 | 74.570 | 12.676 | 18.503 | 14.513 | 22.705 | 31.274 | 87.255 | 12.837 | 18.100 | 188 |
| principal_2021_2025 | dulce | interanual | 90 | SARIMA-sel | 20.629 | 27.520 | 0.773 | 18.273 | 53.607 | 4 | 56 | 159.868 | 2.934 | no | 16.546 | 25.179 | 37.864 | 69.351 | 15.059 | 21.429 | 16.468 | 25.101 | 11.701 | 89.232 | 15.113 | 21.340 | 188 |
| principal_2021_2025 | dulce | interanual | 90 | Ridge | 53.070 | 69.467 | 2.041 | 52.821 | 56.546 | 4 | 56 | 6.550 | 1.071 | no | 43.414 | 63.396 | 23.960 | 89.133 | 43.169 | 62.899 | 42.720 | 64.230 | 21.477 | 111.680 | 41.753 | 64.540 | 188 |
| principal_2021_2025 | dulce | interanual | 90 | ElasticNet | 50.248 | 65.777 | 1.929 | 50.308 | 49.410 | 4 | 56 | -1.668 | 0.982 | no | 40.681 | 60.405 | 16.373 | 82.447 | 40.679 | 60.337 | 39.594 | 61.546 | 14.629 | 100.917 | 38.993 | 62.162 | 188 |
| principal_2021_2025 | dulce | interanual | 90 | XGB-37 | 48.260 | 60.715 | 1.860 | 48.594 | 43.591 | 4 | 56 | -9.676 | 0.897 | no | 39.821 | 57.204 | 35.263 | 51.918 | 39.760 | 57.738 | 38.270 | 58.630 | 6.752 | 73.494 | 38.069 | 59.008 | 188 |
| principal_2021_2025 | dulce | interanual | 90 | GC3 | 56.669 | 76.445 | 2.221 | 55.894 | 67.527 | 4 | 56 | 19.159 | 1.208 | no | 46.893 | 66.950 | 45.560 | 89.493 | 45.932 | 65.955 | 42.763 | 70.828 | 29.640 | 102.351 | 40.804 | 71.085 | 188 |
| principal_2021_2025 | dulce | interanual | 90 | GE | 56.734 | 75.038 | 2.210 | 56.544 | 59.397 | 4 | 56 | 4.692 | 1.050 | no | 47.499 | 66.693 | 37.343 | 81.450 | 46.818 | 66.249 | 43.640 | 70.235 | 23.614 | 92.179 | 42.112 | 70.940 | 188 |
| principal_2021_2025 | dulce | interanual | 90 | XGB-43 | 47.637 | 59.731 | 1.837 | 47.872 | 44.340 | 4 | 56 | -6.921 | 0.926 | sí | 39.323 | 56.352 | 32.261 | 56.418 | 39.402 | 56.687 | 37.618 | 57.681 | 4.321 | 77.856 | 37.517 | 58.137 | 188 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | Naive | 4,124.026 | 5,226.325 | 0.723 | 1,508.571 | 6,216.390 | 20 | 16 | 50.736 | 4.121 | no | 3,173.010 | 5,150.079 | 5,195.992 | 7,146.574 | 987.757 | 2,090.119 | 3,240.788 | 5,010.052 | 5,264.826 | 7,140.218 | 932.440 | 2,110.309 | 0 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | Seasonal Naive | 7,215.902 | 8,670.196 | 1.279 | 7,574.741 | 6,928.831 | 20 | 16 | -3.978 | 0.915 | no | 5,853.918 | 8,597.984 | 5,227.681 | 8,603.889 | 5,313.197 | 9,699.518 | 5,349.332 | 8,939.529 | 4,746.943 | 8,782.593 | 4,682.129 | 10,929.329 | 0 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | Chronos | 2,832.280 | 3,484.378 | 0.496 | 1,830.050 | 3,634.064 | 20 | 16 | 28.309 | 1.986 | no | 2,218.183 | 3,465.237 | 2,737.926 | 4,559.219 | 1,277.670 | 2,369.204 | 2,247.670 | 3,477.132 | 2,753.542 | 4,592.862 | 1,360.073 | 2,345.252 | 0 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | SARIMA | 3,511.730 | 4,164.864 | 0.616 | 3,234.627 | 3,733.412 | 20 | 16 | 6.313 | 1.154 | no | 2,804.130 | 4,226.658 | 2,750.755 | 4,680.135 | 2,335.609 | 4,110.191 | 2,864.417 | 4,182.733 | 2,938.810 | 4,616.033 | 2,412.153 | 4,123.468 | 0 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | SARIMA-sel | 3,705.161 | 4,583.423 | 0.651 | 3,853.672 | 3,586.352 | 20 | 16 | -3.207 | 0.931 | no | 2,853.631 | 4,605.227 | 2,412.862 | 4,831.370 | 2,751.411 | 5,000.422 | 3,009.849 | 4,361.620 | 2,389.317 | 4,758.235 | 2,765.282 | 4,833.995 | 0 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | Ridge | 6,110.312 | 8,840.798 | 1.071 | 2,949.769 | 8,638.746 | 20 | 16 | 41.380 | 2.929 | no | 4,390.039 | 7,971.761 | 5,854.106 | 11,630.942 | 1,850.175 | 4,153.390 | 4,085.590 | 8,125.202 | 5,429.545 | 12,054.265 | 1,641.658 | 4,636.879 | 0 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | ElasticNet | 6,128.657 | 8,561.665 | 1.076 | 2,989.581 | 8,639.917 | 20 | 16 | 40.976 | 2.890 | no | 4,496.304 | 7,860.248 | 6,086.548 | 11,310.273 | 1,736.685 | 4,375.410 | 4,121.627 | 8,106.129 | 5,648.149 | 11,700.168 | 1,517.341 | 5,171.393 | 0 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | XGB-37 | 4,881.474 | 6,056.091 | 0.859 | 4,609.566 | 5,099.000 | 20 | 16 | 4.456 | 1.106 | no | 3,787.676 | 6,031.236 | 3,721.192 | 6,490.130 | 2,907.287 | 6,416.482 | 3,536.920 | 6,298.802 | 3,613.620 | 6,626.696 | 2,113.598 | 7,212.626 | 0 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | GC3 | 7,596.201 | 9,404.867 | 1.341 | 8,348.593 | 6,994.288 | 20 | 16 | -7.924 | 0.838 | no | 5,973.908 | 9,299.278 | 5,401.592 | 8,615.748 | 5,666.664 | 11,292.091 | 5,326.494 | 10,074.508 | 5,131.384 | 8,970.610 | 4,311.152 | 12,847.637 | 0 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | GE | 8,196.974 | 10,119.826 | 1.447 | 9,764.061 | 6,943.305 | 20 | 16 | -15.294 | 0.711 | no | 6,463.621 | 9,985.211 | 5,309.160 | 8,641.692 | 6,899.380 | 12,778.441 | 5,741.963 | 10,744.477 | 5,081.818 | 8,924.766 | 5,316.549 | 14,339.068 | 0 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | XGB-43 | 5,021.018 | 6,368.908 | 0.885 | 4,943.462 | 5,083.064 | 20 | 16 | 1.236 | 1.028 | sí | 3,815.889 | 6,290.762 | 3,598.664 | 6,593.798 | 3,036.413 | 6,960.423 | 3,529.980 | 6,635.167 | 3,445.913 | 6,768.193 | 2,200.186 | 7,787.315 | 0 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | Naive | 4,124.026 | 5,226.325 | 0.723 | 1,577.717 | 6,402.303 | 19 | 17 | 55.244 | 4.058 | no | 3,173.010 | 5,150.079 | 5,367.645 | 7,354.391 | 1,084.334 | 2,118.805 | 3,240.788 | 5,010.052 | 5,497.864 | 7,273.113 | 1,024.434 | 2,152.015 | 0 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | Seasonal Naive | 7,215.902 | 8,670.196 | 1.279 | 7,540.320 | 6,925.634 | 19 | 17 | -4.023 | 0.918 | no | 5,853.918 | 8,597.984 | 5,166.425 | 8,627.626 | 5,393.683 | 9,568.605 | 5,349.332 | 8,939.529 | 4,697.813 | 8,930.453 | 4,781.502 | 10,661.162 | 0 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | Chronos | 2,832.280 | 3,484.378 | 0.496 | 1,733.080 | 3,815.775 | 19 | 17 | 34.724 | 2.202 | no | 2,218.183 | 3,465.237 | 2,918.615 | 4,717.816 | 1,196.711 | 2,269.026 | 2,247.670 | 3,477.132 | 2,944.860 | 4,764.402 | 1,268.797 | 2,238.754 | 0 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | SARIMA | 3,511.730 | 4,164.864 | 0.616 | 3,373.193 | 3,635.684 | 19 | 17 | 3.530 | 1.078 | no | 2,804.130 | 4,226.658 | 2,640.048 | 4,606.133 | 2,508.582 | 4,201.982 | 2,864.417 | 4,182.733 | 2,758.521 | 4,563.434 | 2,569.798 | 4,216.462 | 0 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | SARIMA-sel | 3,705.161 | 4,583.423 | 0.651 | 3,774.877 | 3,642.783 | 19 | 17 | -1.684 | 0.965 | no | 2,853.631 | 4,605.227 | 2,384.715 | 4,932.584 | 2,710.205 | 4,879.020 | 3,009.849 | 4,361.620 | 2,383.639 | 4,921.354 | 2,745.119 | 4,732.227 | 0 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | Ridge | 6,110.312 | 8,840.798 | 1.071 | 3,309.459 | 8,616.338 | 19 | 17 | 41.013 | 2.604 | no | 4,390.039 | 7,971.761 | 5,741.512 | 11,731.959 | 2,168.456 | 4,580.832 | 4,085.590 | 8,125.202 | 5,239.410 | 12,217.895 | 1,880.767 | 4,973.963 | 0 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | ElasticNet | 6,128.657 | 8,561.665 | 1.076 | 3,424.075 | 8,548.545 | 19 | 17 | 39.485 | 2.497 | no | 4,496.304 | 7,860.248 | 5,901.091 | 11,333.613 | 2,095.103 | 4,852.125 | 4,121.627 | 8,106.129 | 5,455.699 | 11,778.284 | 1,740.215 | 5,610.826 | 0 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | XGB-37 | 4,881.474 | 6,056.091 | 0.859 | 4,515.785 | 5,208.669 | 19 | 17 | 6.703 | 1.153 | no | 3,787.676 | 6,031.236 | 3,768.573 | 6,662.384 | 2,924.057 | 6,210.514 | 3,536.920 | 6,298.802 | 3,646.341 | 6,849.051 | 2,173.402 | 6,981.189 | 0 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | GC3 | 7,596.201 | 9,404.867 | 1.341 | 8,317.618 | 6,950.723 | 19 | 17 | -8.497 | 0.836 | no | 5,973.908 | 9,299.278 | 5,280.467 | 8,636.372 | 5,735.556 | 11,136.253 | 5,326.494 | 10,074.508 | 5,054.962 | 9,072.353 | 4,486.732 | 12,558.425 | 0 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | GE | 8,196.974 | 10,119.826 | 1.447 | 9,551.020 | 6,985.460 | 19 | 17 | -14.780 | 0.731 | no | 6,463.621 | 9,985.211 | 5,286.992 | 8,718.986 | 6,825.986 | 12,402.412 | 5,741.963 | 10,744.477 | 5,048.547 | 9,136.524 | 5,364.827 | 13,892.664 | 0 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | XGB-43 | 5,021.018 | 6,368.908 | 0.885 | 4,822.763 | 5,198.405 | 19 | 17 | 3.533 | 1.078 | sí | 3,815.889 | 6,290.762 | 3,633.125 | 6,815.362 | 3,051.524 | 6,702.975 | 3,529.980 | 6,635.167 | 3,480.020 | 6,979.953 | 2,259.959 | 7,509.717 | 0 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | Naive | 4,124.026 | 5,226.325 | 0.723 | 3,067.919 | 8,499.329 | 7 | 29 | 106.093 | 2.770 | no | 3,173.010 | 5,150.079 | 7,827.382 | 9,043.621 | 2,290.430 | 3,885.005 | 3,240.788 | 5,010.052 | 6,759.574 | 11,082.847 | 2,222.683 | 3,881.706 | 1 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | Seasonal Naive | 7,215.902 | 8,670.196 | 1.279 | 7,684.240 | 5,275.644 | 7 | 29 | -26.889 | 0.687 | no | 5,853.918 | 8,597.984 | 1,972.219 | 9,020.803 | 6,275.185 | 9,099.063 | 5,349.332 | 8,939.529 | 987.639 | 9,681.851 | 5,641.218 | 9,569.108 | 1 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | Chronos | 2,832.280 | 3,484.378 | 0.496 | 2,368.391 | 4,754.106 | 7 | 29 | 67.854 | 2.007 | no | 2,218.183 | 3,465.237 | 4,282.398 | 5,304.739 | 1,735.495 | 3,029.897 | 2,247.670 | 3,477.132 | 3,660.187 | 6,252.398 | 1,725.450 | 3,068.178 | 1 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | SARIMA | 3,511.730 | 4,164.864 | 0.616 | 2,994.150 | 5,655.990 | 7 | 29 | 61.060 | 1.889 | no | 2,804.130 | 4,226.658 | 4,547.647 | 6,405.858 | 2,329.705 | 3,673.746 | 2,864.417 | 4,182.733 | 4,063.227 | 7,520.351 | 2,441.934 | 3,600.646 | 1 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | SARIMA-sel | 3,705.161 | 4,583.423 | 0.651 | 3,332.703 | 5,248.203 | 7 | 29 | 41.646 | 1.575 | no | 2,853.631 | 4,605.227 | 3,051.813 | 7,758.430 | 2,487.432 | 4,209.205 | 3,009.849 | 4,361.620 | 2,762.371 | 8,043.848 | 2,574.422 | 3,994.160 | 1 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | Ridge | 6,110.312 | 8,840.798 | 1.071 | 5,089.106 | 10,341.024 | 7 | 29 | 69.239 | 2.032 | no | 4,390.039 | 7,971.761 | 6,326.597 | 15,773.572 | 3,389.763 | 6,927.677 | 4,085.590 | 8,125.202 | 6,362.590 | 13,776.197 | 3,357.462 | 7,048.358 | 1 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | ElasticNet | 6,128.657 | 8,561.665 | 1.076 | 5,211.661 | 9,927.637 | 7 | 29 | 61.987 | 1.905 | no | 4,496.304 | 7,860.248 | 6,188.917 | 14,420.726 | 3,569.985 | 6,965.838 | 4,121.627 | 8,106.129 | 6,312.244 | 12,787.848 | 3,353.970 | 7,319.084 | 1 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | XGB-37 | 4,881.474 | 6,056.091 | 0.859 | 4,547.673 | 6,264.362 | 7 | 29 | 28.329 | 1.377 | no | 3,787.676 | 6,031.236 | 2,991.070 | 8,304.032 | 3,394.285 | 5,739.082 | 3,536.920 | 6,298.802 | 2,895.099 | 9,976.681 | 2,969.079 | 6,202.918 | 1 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | GC3 | 7,596.201 | 9,404.867 | 1.341 | 7,843.669 | 6,570.976 | 7 | 29 | -13.497 | 0.838 | no | 5,973.908 | 9,299.278 | 4,346.090 | 8,711.629 | 5,931.199 | 9,781.853 | 5,326.494 | 10,074.508 | 4,105.527 | 8,918.036 | 5,065.570 | 10,838.824 | 1 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | GE | 8,196.974 | 10,119.826 | 1.447 | 8,359.655 | 7,523.012 | 7 | 29 | -8.222 | 0.900 | no | 6,463.621 | 9,985.211 | 4,887.577 | 10,112.193 | 6,351.443 | 10,371.564 | 5,741.963 | 10,744.477 | 4,538.737 | 10,508.151 | 5,363.397 | 11,493.701 | 1 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | XGB-43 | 5,021.018 | 6,368.908 | 0.885 | 4,720.963 | 6,264.104 | 7 | 29 | 24.758 | 1.327 | sí | 3,815.889 | 6,290.762 | 2,927.858 | 8,500.830 | 3,442.366 | 6,050.551 | 3,529.980 | 6,635.167 | 2,807.446 | 10,077.350 | 2,931.693 | 6,602.494 | 1 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | Naive | 4,124.026 | 5,226.325 | 0.723 | 3,441.724 | 8,354.298 | 5 | 31 | 102.576 | 2.427 | no | 3,173.010 | 5,150.079 | 7,413.572 | 9,072.959 | 2,556.074 | 4,405.637 | 3,240.788 | 5,010.052 | 5,565.985 | 11,948.812 | 2,490.235 | 4,377.883 | 75 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | Seasonal Naive | 7,215.902 | 8,670.196 | 1.279 | 7,261.594 | 6,932.613 | 5 | 31 | -3.926 | 0.955 | no | 5,853.918 | 8,597.984 | 2,792.645 | 11,072.582 | 5,853.313 | 8,694.878 | 5,349.332 | 8,939.529 | 962.367 | 11,830.680 | 5,310.408 | 9,104.601 | 75 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | Chronos | 2,832.280 | 3,484.378 | 0.496 | 2,486.119 | 4,978.480 | 5 | 31 | 75.776 | 2.003 | no | 2,218.183 | 3,465.237 | 4,579.575 | 5,559.176 | 1,855.251 | 3,124.904 | 2,247.670 | 3,477.132 | 3,292.883 | 6,781.005 | 1,839.606 | 3,181.005 | 75 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | SARIMA | 3,511.730 | 4,164.864 | 0.616 | 3,066.858 | 6,269.936 | 5 | 31 | 78.543 | 2.044 | no | 2,804.130 | 4,226.658 | 6,097.148 | 6,442.723 | 2,378.066 | 3,786.430 | 2,864.417 | 4,182.733 | 4,848.000 | 8,188.099 | 2,522.819 | 3,609.083 | 75 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | SARIMA-sel | 3,705.161 | 4,583.423 | 0.651 | 3,253.085 | 6,508.029 | 5 | 31 | 75.648 | 2.001 | no | 2,853.631 | 4,605.227 | 4,445.133 | 9,387.066 | 2,454.824 | 4,088.465 | 3,009.849 | 4,361.620 | 3,482.444 | 9,379.049 | 2,521.226 | 3,919.073 | 75 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | Ridge | 6,110.312 | 8,840.798 | 1.071 | 5,137.488 | 12,141.820 | 5 | 31 | 98.710 | 2.363 | no | 4,390.039 | 7,971.761 | 8,093.761 | 18,104.888 | 3,502.447 | 6,978.342 | 4,085.590 | 8,125.202 | 6,838.384 | 20,772.300 | 3,490.294 | 6,995.278 | 75 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | ElasticNet | 6,128.657 | 8,561.665 | 1.076 | 5,312.969 | 11,185.921 | 5 | 31 | 82.518 | 2.105 | no | 4,496.304 | 7,860.248 | 7,540.847 | 15,707.806 | 3,687.184 | 7,095.291 | 4,121.627 | 8,106.129 | 6,042.823 | 18,233.471 | 3,509.198 | 7,354.253 | 75 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | XGB-37 | 4,881.474 | 6,056.091 | 0.859 | 4,437.989 | 7,631.080 | 5 | 31 | 56.327 | 1.719 | no | 3,787.676 | 6,031.236 | 6,731.082 | 8,224.714 | 3,309.211 | 5,629.510 | 3,536.920 | 6,298.802 | 4,332.807 | 12,195.535 | 2,953.538 | 6,039.278 | 75 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | GC3 | 7,596.201 | 9,404.867 | 1.341 | 7,628.615 | 7,395.234 | 5 | 31 | -2.646 | 0.969 | no | 5,973.908 | 9,299.278 | 4,932.924 | 10,300.749 | 5,812.625 | 9,572.897 | 5,326.494 | 10,074.508 | 4,430.186 | 9,885.833 | 5,039.868 | 10,455.241 | 75 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | GE | 8,196.974 | 10,119.826 | 1.447 | 8,156.565 | 8,447.512 | 5 | 31 | 3.056 | 1.036 | no | 6,463.621 | 9,985.211 | 6,385.378 | 10,971.111 | 6,227.263 | 10,170.814 | 5,741.963 | 10,744.477 | 4,658.726 | 11,439.362 | 5,359.920 | 11,149.104 | 75 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | XGB-43 | 5,021.018 | 6,368.908 | 0.885 | 4,612.224 | 7,555.543 | 5 | 31 | 50.478 | 1.638 | sí | 3,815.889 | 6,290.762 | 6,359.484 | 8,440.973 | 3,358.590 | 5,929.114 | 3,529.980 | 6,635.167 | 3,929.216 | 12,364.785 | 2,932.915 | 6,424.145 | 75 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | Naive | 4,124.026 | 5,226.325 | 0.723 | 4,508.881 | 3,779.682 | 19 | 17 | -8.350 | 0.838 | no | 3,173.010 | 5,150.079 | 2,535.478 | 5,160.835 | 3,026.883 | 6,114.813 | 3,240.788 | 5,010.052 | 2,568.112 | 4,980.388 | 3,074.689 | 6,127.248 | 0 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | Seasonal Naive | 7,215.902 | 8,670.196 | 1.279 | 3,185.332 | 10,822.202 | 19 | 17 | 49.977 | 3.398 | no | 5,853.918 | 8,597.984 | 9,544.241 | 12,046.089 | 2,185.226 | 4,181.811 | 5,349.332 | 8,939.529 | 9,326.230 | 12,434.250 | 2,207.282 | 4,182.762 | 0 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | Chronos | 2,832.280 | 3,484.378 | 0.496 | 2,814.830 | 2,847.893 | 19 | 17 | 0.551 | 1.012 | no | 2,218.183 | 3,465.237 | 2,050.462 | 3,637.998 | 2,032.198 | 3,658.758 | 2,247.670 | 3,477.132 | 1,939.894 | 3,925.899 | 2,162.808 | 3,602.463 | 0 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | SARIMA | 3,511.730 | 4,164.864 | 0.616 | 3,574.173 | 3,455.860 | 19 | 17 | -1.591 | 0.967 | no | 2,804.130 | 4,226.658 | 2,536.527 | 4,376.180 | 2,481.977 | 4,672.634 | 2,864.417 | 4,182.733 | 2,683.133 | 4,257.031 | 2,483.845 | 4,895.938 | 0 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | SARIMA-sel | 3,705.161 | 4,583.423 | 0.651 | 3,500.944 | 3,887.881 | 19 | 17 | 4.932 | 1.111 | no | 2,853.631 | 4,605.227 | 2,547.974 | 5,317.933 | 2,691.883 | 4,322.621 | 3,009.849 | 4,361.620 | 2,752.481 | 4,909.182 | 2,853.659 | 4,265.340 | 0 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | Ridge | 6,110.312 | 8,840.798 | 1.071 | 6,347.519 | 5,898.074 | 19 | 17 | -3.473 | 0.929 | no | 4,390.039 | 7,971.761 | 4,211.676 | 7,864.155 | 3,368.958 | 9,576.199 | 4,085.590 | 8,125.202 | 3,510.178 | 8,586.342 | 2,833.994 | 10,250.145 | 0 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | ElasticNet | 6,128.657 | 8,561.665 | 1.076 | 5,906.669 | 6,327.277 | 19 | 17 | 3.241 | 1.071 | no | 4,496.304 | 7,860.248 | 4,668.320 | 8,214.382 | 3,190.295 | 8,864.779 | 4,121.627 | 8,106.129 | 3,805.121 | 9,115.885 | 2,620.318 | 9,503.193 | 0 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | XGB-37 | 4,881.474 | 6,056.091 | 0.859 | 5,258.125 | 4,544.470 | 19 | 17 | -6.904 | 0.864 | no | 3,787.676 | 6,031.236 | 3,022.191 | 6,180.041 | 3,762.105 | 6,790.668 | 3,536.920 | 6,298.802 | 2,645.482 | 6,618.743 | 3,877.228 | 6,913.924 | 0 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | GC3 | 7,596.201 | 9,404.867 | 1.341 | 7,095.174 | 8,044.488 | 19 | 17 | 5.901 | 1.134 | no | 5,973.908 | 9,299.278 | 5,906.512 | 10,334.011 | 4,913.847 | 9,337.540 | 5,326.494 | 10,074.508 | 5,047.593 | 11,495.027 | 4,326.170 | 9,834.904 | 0 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | GE | 8,196.974 | 10,119.826 | 1.447 | 8,384.171 | 8,029.482 | 19 | 17 | -2.043 | 0.958 | no | 6,463.621 | 9,985.211 | 5,897.291 | 10,259.963 | 5,828.413 | 10,916.718 | 5,741.963 | 10,744.477 | 5,152.678 | 11,470.865 | 4,836.320 | 11,735.261 | 0 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | XGB-43 | 5,021.018 | 6,368.908 | 0.885 | 5,551.612 | 4,546.277 | 19 | 17 | -9.455 | 0.819 | sí | 3,815.889 | 6,290.762 | 2,846.527 | 6,410.903 | 3,990.552 | 7,147.060 | 3,529.980 | 6,635.167 | 2,462.936 | 6,955.182 | 4,072.691 | 7,264.383 | 0 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | Naive | 4,124.026 | 5,226.325 | 0.723 | 4,399.538 | 3,779.636 | 16 | 20 | -8.351 | 0.859 | no | 3,173.010 | 5,150.079 | 2,398.710 | 5,257.896 | 3,074.270 | 5,867.878 | 3,240.788 | 5,010.052 | 2,270.284 | 5,234.688 | 3,101.061 | 5,743.930 | 0 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | Seasonal Naive | 7,215.902 | 8,670.196 | 1.279 | 3,901.555 | 11,358.836 | 16 | 20 | 57.414 | 2.911 | no | 5,853.918 | 8,597.984 | 9,865.859 | 12,829.464 | 2,732.270 | 5,107.971 | 5,349.332 | 8,939.529 | 9,778.175 | 13,149.147 | 2,658.547 | 5,225.207 | 0 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | Chronos | 2,832.280 | 3,484.378 | 0.496 | 3,029.874 | 2,585.288 | 16 | 20 | -8.721 | 0.853 | no | 2,218.183 | 3,465.237 | 1,816.287 | 3,354.426 | 2,214.609 | 3,921.877 | 2,247.670 | 3,477.132 | 1,644.748 | 3,653.179 | 2,337.002 | 3,796.162 | 0 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | SARIMA | 3,511.730 | 4,164.864 | 0.616 | 3,537.065 | 3,480.061 | 16 | 20 | -0.902 | 0.984 | no | 2,804.130 | 4,226.658 | 2,632.420 | 4,281.621 | 2,498.770 | 4,618.790 | 2,864.417 | 4,182.733 | 2,448.035 | 4,305.890 | 2,493.537 | 4,815.182 | 0 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | SARIMA-sel | 3,705.161 | 4,583.423 | 0.651 | 3,396.290 | 4,091.250 | 16 | 20 | 10.420 | 1.205 | no | 2,853.631 | 4,605.227 | 2,603.560 | 5,642.270 | 2,449.642 | 4,372.067 | 3,009.849 | 4,361.620 | 2,856.380 | 5,172.381 | 2,487.060 | 4,365.929 | 0 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | Ridge | 6,110.312 | 8,840.798 | 1.071 | 6,214.494 | 5,980.085 | 16 | 20 | -2.131 | 0.962 | no | 4,390.039 | 7,971.761 | 3,962.808 | 8,352.197 | 3,724.705 | 8,979.982 | 4,085.590 | 8,125.202 | 2,939.787 | 9,218.745 | 3,409.728 | 9,475.234 | 0 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | ElasticNet | 6,128.657 | 8,561.665 | 1.076 | 5,873.237 | 6,447.932 | 16 | 20 | 5.210 | 1.098 | no | 4,496.304 | 7,860.248 | 4,459.735 | 8,749.654 | 3,548.311 | 8,411.034 | 4,121.627 | 8,106.129 | 3,238.810 | 9,773.632 | 3,222.781 | 8,788.055 | 0 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | XGB-37 | 4,881.474 | 6,056.091 | 0.859 | 4,745.883 | 5,050.962 | 16 | 20 | 3.472 | 1.064 | no | 3,787.676 | 6,031.236 | 3,338.837 | 6,833.656 | 3,323.810 | 6,204.281 | 3,536.920 | 6,298.802 | 2,834.400 | 7,574.118 | 3,347.436 | 6,345.039 | 0 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | GC3 | 7,596.201 | 9,404.867 | 1.341 | 6,741.902 | 8,664.074 | 16 | 20 | 14.058 | 1.285 | no | 5,973.908 | 9,299.278 | 6,220.705 | 11,322.873 | 4,790.300 | 8,726.208 | 5,326.494 | 10,074.508 | 5,189.070 | 12,800.857 | 4,486.825 | 9,283.622 | 0 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | GE | 8,196.974 | 10,119.826 | 1.447 | 7,621.330 | 8,916.530 | 16 | 20 | 8.778 | 1.170 | no | 6,463.621 | 9,985.211 | 6,563.884 | 11,442.833 | 5,253.688 | 9,965.007 | 5,741.963 | 10,744.477 | 5,620.938 | 12,903.041 | 4,466.584 | 10,943.452 | 0 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | XGB-43 | 5,021.018 | 6,368.908 | 0.885 | 4,969.555 | 5,085.348 | 16 | 20 | 1.281 | 1.023 | sí | 3,815.889 | 6,290.762 | 3,148.492 | 7,118.291 | 3,469.743 | 6,506.438 | 3,529.980 | 6,635.167 | 2,625.077 | 8,040.218 | 3,421.073 | 6,670.726 | 0 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | Naive | 4,124.026 | 5,226.325 | 0.723 | 4,490.249 | 3,171.846 | 10 | 26 | -23.089 | 0.706 | no | 3,173.010 | 5,150.079 | 1,674.215 | 4,943.924 | 3,285.634 | 5,769.988 | 3,240.788 | 5,010.052 | 966.370 | 5,059.687 | 3,446.120 | 5,532.105 | 2 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | Seasonal Naive | 7,215.902 | 8,670.196 | 1.279 | 5,180.454 | 12,508.067 | 10 | 26 | 73.340 | 2.414 | no | 5,853.918 | 8,597.984 | 10,423.461 | 14,592.681 | 3,900.174 | 6,458.882 | 5,349.332 | 8,939.529 | 10,108.034 | 14,751.801 | 3,549.874 | 6,782.179 | 2 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | Chronos | 2,832.280 | 3,484.378 | 0.496 | 3,204.652 | 1,864.113 | 10 | 26 | -34.183 | 0.582 | no | 2,218.183 | 3,465.237 | 1,419.839 | 2,317.092 | 2,415.238 | 4,040.722 | 2,247.670 | 3,477.132 | 954.533 | 2,742.274 | 2,422.805 | 4,053.005 | 2 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | SARIMA | 3,511.730 | 4,164.864 | 0.616 | 3,619.041 | 3,232.720 | 10 | 26 | -7.945 | 0.893 | no | 2,804.130 | 4,226.658 | 2,430.059 | 3,968.468 | 2,705.507 | 4,559.447 | 2,864.417 | 4,182.733 | 2,290.872 | 3,918.009 | 2,743.687 | 4,611.754 | 2 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | SARIMA-sel | 3,705.161 | 4,583.423 | 0.651 | 3,561.442 | 4,078.830 | 10 | 26 | 10.085 | 1.145 | no | 2,853.631 | 4,605.227 | 2,145.130 | 6,098.922 | 2,683.817 | 4,463.941 | 3,009.849 | 4,361.620 | 2,199.053 | 5,758.346 | 2,769.253 | 4,306.818 | 2 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | Ridge | 6,110.312 | 8,840.798 | 1.071 | 6,558.098 | 4,946.068 | 10 | 26 | -19.054 | 0.754 | no | 4,390.039 | 7,971.761 | 3,290.048 | 6,789.016 | 4,309.269 | 9,033.500 | 4,085.590 | 8,125.202 | 1,775.199 | 8,397.269 | 4,368.890 | 9,078.588 | 2 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | ElasticNet | 6,128.657 | 8,561.665 | 1.076 | 6,407.477 | 5,403.723 | 10 | 26 | -11.829 | 0.843 | no | 4,496.304 | 7,860.248 | 3,428.325 | 7,594.067 | 4,345.811 | 8,627.004 | 4,121.627 | 8,106.129 | 1,919.977 | 9,347.228 | 4,315.147 | 8,661.349 | 2 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | XGB-37 | 4,881.474 | 6,056.091 | 0.859 | 4,906.469 | 4,816.485 | 10 | 26 | -1.331 | 0.982 | no | 3,787.676 | 6,031.236 | 2,547.727 | 7,253.853 | 3,673.472 | 6,162.372 | 3,536.920 | 6,298.802 | 1,560.986 | 8,726.351 | 3,703.970 | 6,024.830 | 2 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | GC3 | 7,596.201 | 9,404.867 | 1.341 | 6,992.387 | 9,166.116 | 10 | 26 | 20.667 | 1.311 | no | 5,973.908 | 9,299.278 | 5,191.821 | 13,365.038 | 5,420.437 | 8,562.895 | 5,326.494 | 10,074.508 | 3,531.184 | 16,005.173 | 5,209.026 | 8,908.917 | 2 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | GE | 8,196.974 | 10,119.826 | 1.447 | 7,581.954 | 9,796.027 | 10 | 26 | 19.508 | 1.292 | no | 6,463.621 | 9,985.211 | 6,024.869 | 13,767.112 | 5,763.988 | 9,426.192 | 5,741.963 | 10,744.477 | 4,551.397 | 16,261.238 | 5,245.894 | 9,937.072 | 2 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | XGB-43 | 5,021.018 | 6,368.908 | 0.885 | 5,021.001 | 5,021.063 | 10 | 26 | 0.001 | 1.000 | sí | 3,815.889 | 6,290.762 | 2,451.818 | 7,798.984 | 3,696.091 | 6,375.783 | 3,529.980 | 6,635.167 | 1,483.056 | 9,586.563 | 3,724.848 | 6,203.136 | 2 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | Naive | 4,124.026 | 5,226.325 | 0.723 | 4,447.162 | 1,538.943 | 4 | 32 | -62.683 | 0.346 | no | 3,173.010 | 5,150.079 | 426.541 | 3,220.365 | 3,379.279 | 5,594.286 | 3,240.788 | 5,010.052 | 478.200 | 2,979.033 | 3,492.366 | 5,396.228 | 134 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | Seasonal Naive | 7,215.902 | 8,670.196 | 1.279 | 6,210.546 | 15,258.750 | 4 | 32 | 111.460 | 2.457 | no | 5,853.918 | 8,597.984 | 12,120.610 | 17,401.499 | 4,960.626 | 7,479.629 | 5,349.332 | 8,939.529 | 12,225.283 | 17,485.031 | 4,697.219 | 7,696.702 | 134 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | Chronos | 2,832.280 | 3,484.378 | 0.496 | 3,046.790 | 1,116.204 | 4 | 32 | -60.590 | 0.366 | no | 2,218.183 | 3,465.237 | 605.768 | 1,469.441 | 2,363.361 | 3,754.392 | 2,247.670 | 3,477.132 | 617.717 | 1,478.782 | 2,429.730 | 3,721.779 | 134 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | SARIMA | 3,511.730 | 4,164.864 | 0.616 | 3,485.017 | 3,725.435 | 4 | 32 | 6.085 | 1.069 | no | 2,804.130 | 4,226.658 | 2,832.216 | 4,533.901 | 2,713.472 | 4,266.791 | 2,864.417 | 4,182.733 | 2,797.232 | 4,597.135 | 2,763.710 | 4,246.623 | 134 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | SARIMA-sel | 3,705.161 | 4,583.423 | 0.651 | 3,480.008 | 5,506.388 | 4 | 32 | 48.614 | 1.582 | no | 2,853.631 | 4,605.227 | 3,483.781 | 7,463.792 | 2,615.775 | 4,381.554 | 3,009.849 | 4,361.620 | 3,618.828 | 7,393.948 | 2,712.773 | 4,190.954 | 134 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | Ridge | 6,110.312 | 8,840.798 | 1.071 | 6,352.963 | 4,169.104 | 4 | 32 | -31.769 | 0.656 | no | 4,390.039 | 7,971.761 | 1,817.620 | 6,562.733 | 4,454.875 | 8,411.445 | 4,085.590 | 8,125.202 | 1,647.693 | 7,005.229 | 4,155.829 | 8,509.232 | 134 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | ElasticNet | 6,128.657 | 8,561.665 | 1.076 | 6,292.526 | 4,817.704 | 4 | 32 | -21.391 | 0.766 | no | 4,496.304 | 7,860.248 | 1,909.354 | 7,726.055 | 4,516.125 | 8,178.270 | 4,121.627 | 8,106.129 | 1,708.183 | 8,246.874 | 4,160.538 | 8,347.730 | 134 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | XGB-37 | 4,881.474 | 6,056.091 | 0.859 | 4,797.197 | 5,555.691 | 4 | 32 | 13.812 | 1.158 | no | 3,787.676 | 6,031.236 | 1,146.511 | 9,964.871 | 3,677.194 | 5,950.942 | 3,536.920 | 6,298.802 | 925.288 | 10,676.534 | 3,639.991 | 5,977.391 | 134 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | GC3 | 7,596.201 | 9,404.867 | 1.341 | 7,269.274 | 10,211.615 | 4 | 32 | 34.431 | 1.405 | no | 5,973.908 | 9,299.278 | 3,003.241 | 17,419.988 | 5,679.475 | 8,855.392 | 5,326.494 | 10,074.508 | 2,813.075 | 18,024.089 | 5,324.232 | 9,460.126 | 134 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | GE | 8,196.974 | 10,119.826 | 1.447 | 7,809.174 | 11,299.378 | 4 | 32 | 37.848 | 1.447 | no | 6,463.621 | 9,985.211 | 4,602.185 | 17,996.571 | 6,081.263 | 9,557.124 | 5,741.963 | 10,744.477 | 4,357.755 | 18,579.076 | 5,556.517 | 10,178.467 | 134 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | XGB-43 | 5,021.018 | 6,368.908 | 0.885 | 4,895.171 | 6,027.801 | 4 | 32 | 20.051 | 1.231 | sí | 3,815.889 | 6,290.762 | 1,304.236 | 10,751.366 | 3,669.673 | 6,170.001 | 3,529.980 | 6,635.167 | 1,095.744 | 11,520.714 | 3,620.141 | 6,249.829 | 134 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | Naive | 82.158 | 95.959 | 3.326 | 45.372 | 118.944 | 18 | 18 | 44.775 | 2.622 | no | 66.161 | 98.885 | 100.054 | 137.819 | 35.510 | 55.587 | 67.740 | 97.332 | 99.576 | 138.113 | 35.042 | 54.882 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | Seasonal Naive | 28.059 | 36.507 | 1.145 | 35.672 | 20.447 | 18 | 18 | -27.130 | 0.573 | no | 22.262 | 34.853 | 15.608 | 25.361 | 25.684 | 47.244 | 21.101 | 35.349 | 14.902 | 26.050 | 24.353 | 48.045 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | Chronos | 34.960 | 41.941 | 1.415 | 28.072 | 41.848 | 18 | 18 | 19.703 | 1.491 | no | 27.772 | 42.598 | 32.094 | 51.902 | 18.931 | 38.889 | 27.531 | 42.712 | 30.628 | 52.042 | 20.322 | 37.217 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | SARIMA | 22.004 | 29.635 | 0.891 | 27.400 | 16.608 | 18 | 18 | -24.524 | 0.606 | no | 16.052 | 28.799 | 11.342 | 22.377 | 17.314 | 39.046 | 16.070 | 28.853 | 12.582 | 21.337 | 17.782 | 38.189 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | SARIMA-sel | 20.936 | 28.715 | 0.847 | 26.342 | 15.530 | 18 | 18 | -25.821 | 0.590 | no | 15.226 | 27.667 | 11.212 | 20.220 | 16.144 | 38.378 | 15.220 | 27.556 | 11.751 | 19.531 | 16.449 | 37.595 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | Ridge | 63.968 | 80.990 | 2.581 | 61.971 | 65.966 | 18 | 18 | 3.123 | 1.064 | no | 50.093 | 78.119 | 45.759 | 89.376 | 44.121 | 80.042 | 48.590 | 80.399 | 42.772 | 91.036 | 42.862 | 78.929 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | ElasticNet | 59.495 | 76.184 | 2.401 | 59.309 | 59.680 | 18 | 18 | 0.312 | 1.006 | no | 45.630 | 73.931 | 39.119 | 83.227 | 41.307 | 76.954 | 43.439 | 76.451 | 36.332 | 84.846 | 40.581 | 75.957 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | XGB-37 | 54.405 | 67.592 | 2.208 | 60.931 | 47.879 | 18 | 18 | -11.995 | 0.786 | no | 42.083 | 67.348 | 31.884 | 64.090 | 44.096 | 79.367 | 39.918 | 69.971 | 29.181 | 63.669 | 40.367 | 81.191 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | GC3 | 69.886 | 90.950 | 2.877 | 82.695 | 57.077 | 18 | 18 | -18.328 | 0.690 | no | 54.575 | 85.103 | 40.391 | 75.511 | 59.266 | 105.943 | 48.239 | 92.064 | 37.945 | 78.489 | 51.898 | 113.487 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | GE | 68.358 | 87.432 | 2.805 | 81.567 | 55.148 | 18 | 18 | -19.324 | 0.676 | no | 53.874 | 82.996 | 39.806 | 72.600 | 59.611 | 103.329 | 48.642 | 88.941 | 38.557 | 73.193 | 53.658 | 109.838 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | XGB-43 | 53.252 | 66.371 | 2.165 | 59.247 | 47.257 | 18 | 18 | -11.258 | 0.798 | sí | 41.063 | 65.918 | 33.562 | 61.247 | 41.098 | 78.031 | 38.923 | 68.403 | 30.814 | 60.823 | 37.191 | 80.825 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | Naive | 82.158 | 95.959 | 3.326 | 49.674 | 133.204 | 14 | 22 | 62.132 | 2.682 | no | 66.161 | 98.885 | 114.776 | 150.827 | 40.471 | 58.882 | 67.740 | 97.332 | 115.159 | 152.039 | 42.213 | 57.261 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | Seasonal Naive | 28.059 | 36.507 | 1.145 | 31.615 | 22.472 | 14 | 22 | -19.911 | 0.711 | no | 22.262 | 34.853 | 17.029 | 27.499 | 22.863 | 41.812 | 21.101 | 35.349 | 15.937 | 29.822 | 21.792 | 42.598 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | Chronos | 34.960 | 41.941 | 1.415 | 26.427 | 48.368 | 14 | 22 | 38.354 | 1.830 | no | 27.772 | 42.598 | 39.095 | 58.209 | 18.316 | 36.010 | 27.531 | 42.712 | 37.860 | 57.610 | 19.896 | 34.151 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | SARIMA | 22.004 | 29.635 | 0.891 | 25.996 | 15.732 | 14 | 22 | -28.504 | 0.605 | no | 16.052 | 28.799 | 10.784 | 20.815 | 17.139 | 36.060 | 16.070 | 28.853 | 11.374 | 21.373 | 17.017 | 35.635 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | SARIMA-sel | 20.936 | 28.715 | 0.847 | 24.932 | 14.657 | 14 | 22 | -29.991 | 0.588 | no | 15.226 | 27.667 | 9.992 | 19.356 | 16.260 | 34.937 | 15.220 | 27.556 | 10.262 | 20.015 | 16.191 | 34.332 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | Ridge | 63.968 | 80.990 | 2.581 | 62.521 | 66.242 | 14 | 22 | 3.555 | 1.060 | no | 50.093 | 78.119 | 45.900 | 88.820 | 44.728 | 81.490 | 48.590 | 80.399 | 43.266 | 90.722 | 43.405 | 80.908 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | ElasticNet | 59.495 | 76.184 | 2.401 | 58.338 | 61.312 | 14 | 22 | 3.054 | 1.051 | no | 45.630 | 73.931 | 40.743 | 84.101 | 40.549 | 77.284 | 43.439 | 76.451 | 37.228 | 85.472 | 39.212 | 77.047 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | XGB-37 | 54.405 | 67.592 | 2.208 | 53.504 | 55.822 | 14 | 22 | 2.604 | 1.043 | no | 42.083 | 67.348 | 37.948 | 72.760 | 37.937 | 70.490 | 39.918 | 69.971 | 35.754 | 70.979 | 34.584 | 74.880 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | GC3 | 69.886 | 90.950 | 2.877 | 73.685 | 63.916 | 14 | 22 | -8.542 | 0.867 | no | 54.575 | 85.103 | 44.141 | 84.239 | 53.140 | 95.232 | 48.239 | 92.064 | 41.132 | 88.213 | 46.902 | 104.427 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | GE | 68.358 | 87.432 | 2.805 | 73.600 | 60.119 | 14 | 22 | -12.053 | 0.817 | no | 53.874 | 82.996 | 41.532 | 80.192 | 54.527 | 93.700 | 48.642 | 88.941 | 40.185 | 80.338 | 49.069 | 101.711 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | XGB-43 | 53.252 | 66.371 | 2.165 | 52.592 | 54.290 | 14 | 22 | 1.949 | 1.032 | sí | 41.063 | 65.918 | 39.622 | 68.684 | 36.253 | 69.951 | 38.923 | 68.403 | 37.151 | 66.697 | 32.792 | 74.758 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | Naive | 82.158 | 95.959 | 3.326 | 63.485 | 138.176 | 9 | 27 | 68.183 | 2.176 | no | 66.161 | 98.885 | 118.957 | 158.722 | 49.357 | 79.089 | 67.740 | 97.332 | 119.712 | 157.276 | 51.462 | 75.430 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | Seasonal Naive | 28.059 | 36.507 | 1.145 | 29.074 | 25.016 | 9 | 27 | -10.847 | 0.860 | no | 22.262 | 34.853 | 19.998 | 30.408 | 21.511 | 38.100 | 21.101 | 35.349 | 16.637 | 33.794 | 19.322 | 38.726 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | Chronos | 34.960 | 41.941 | 1.415 | 28.169 | 55.332 | 9 | 27 | 58.274 | 1.964 | no | 27.772 | 42.598 | 44.815 | 67.046 | 21.051 | 36.501 | 27.531 | 42.712 | 43.272 | 66.024 | 22.443 | 34.734 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | SARIMA | 22.004 | 29.635 | 0.891 | 23.487 | 17.555 | 9 | 27 | -20.220 | 0.747 | no | 16.052 | 28.799 | 10.811 | 23.940 | 16.189 | 32.387 | 16.070 | 28.853 | 11.781 | 28.267 | 16.195 | 31.136 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | SARIMA-sel | 20.936 | 28.715 | 0.847 | 22.286 | 16.888 | 9 | 27 | -19.338 | 0.758 | no | 15.226 | 27.667 | 10.707 | 22.587 | 15.197 | 31.278 | 15.220 | 27.556 | 11.213 | 26.655 | 15.246 | 29.773 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | Ridge | 63.968 | 80.990 | 2.581 | 57.239 | 84.155 | 9 | 27 | 31.558 | 1.470 | no | 50.093 | 78.119 | 59.849 | 112.267 | 42.096 | 73.809 | 48.590 | 80.399 | 53.585 | 118.003 | 39.594 | 75.167 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | ElasticNet | 59.495 | 76.184 | 2.401 | 52.751 | 79.726 | 9 | 27 | 34.006 | 1.511 | no | 45.630 | 73.931 | 55.375 | 108.789 | 37.589 | 69.104 | 43.439 | 76.451 | 48.788 | 111.199 | 35.755 | 70.483 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | XGB-37 | 54.405 | 67.592 | 2.208 | 49.499 | 69.124 | 9 | 27 | 27.054 | 1.396 | no | 42.083 | 67.348 | 51.888 | 86.271 | 35.259 | 65.268 | 39.918 | 69.971 | 48.632 | 85.025 | 34.003 | 69.054 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | GC3 | 69.886 | 90.950 | 2.877 | 69.210 | 71.912 | 9 | 27 | 2.900 | 1.039 | no | 54.575 | 85.103 | 49.009 | 96.328 | 51.557 | 87.940 | 48.239 | 92.064 | 39.712 | 105.468 | 44.438 | 96.376 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | GE | 68.358 | 87.432 | 2.805 | 68.597 | 67.639 | 9 | 27 | -1.051 | 0.986 | no | 53.874 | 82.996 | 43.655 | 93.714 | 52.280 | 86.175 | 48.642 | 88.941 | 39.389 | 96.972 | 46.117 | 93.801 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | XGB-43 | 53.252 | 66.371 | 2.165 | 49.629 | 64.120 | 9 | 27 | 20.409 | 1.292 | sí | 41.063 | 65.918 | 48.600 | 79.820 | 35.015 | 65.218 | 38.923 | 68.403 | 44.126 | 79.371 | 33.691 | 69.188 | 0 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | Naive | 82.158 | 95.959 | 3.326 | 81.702 | 98.110 | 1 | 35 | 19.416 | 1.201 | no | 66.161 | 98.885 | 98.110 | 98.110 | 65.604 | 98.224 | 67.740 | 97.332 | 98.110 | 98.110 | 66.842 | 97.310 | 3217 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | Seasonal Naive | 28.059 | 36.507 | 1.145 | 28.120 | 25.930 | 1 | 35 | -7.588 | 0.922 | no | 22.262 | 34.853 | 25.930 | 25.930 | 22.104 | 35.081 | 21.101 | 35.349 | 25.930 | 25.930 | 20.903 | 35.437 | 3217 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | Chronos | 34.960 | 41.941 | 1.415 | 34.193 | 61.804 | 1 | 35 | 76.785 | 1.808 | no | 27.772 | 42.598 | 61.804 | 61.804 | 26.908 | 41.865 | 27.531 | 42.712 | 61.804 | 61.804 | 26.638 | 41.950 | 3217 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | SARIMA | 22.004 | 29.635 | 0.891 | 21.959 | 23.571 | 1 | 35 | 7.119 | 1.073 | no | 16.052 | 28.799 | 23.571 | 23.571 | 15.936 | 29.046 | 16.070 | 28.853 | 23.571 | 23.571 | 15.701 | 28.932 | 3217 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | SARIMA-sel | 20.936 | 28.715 | 0.847 | 20.854 | 23.803 | 1 | 35 | 13.691 | 1.141 | no | 15.226 | 27.667 | 23.803 | 23.803 | 15.042 | 27.954 | 15.220 | 27.556 | 23.803 | 23.803 | 14.827 | 27.568 | 3217 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | Ridge | 63.968 | 80.990 | 2.581 | 63.585 | 77.378 | 1 | 35 | 20.963 | 1.217 | no | 50.093 | 78.119 | 77.378 | 77.378 | 49.523 | 78.287 | 48.590 | 80.399 | 77.378 | 77.378 | 47.258 | 80.420 | 3217 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | ElasticNet | 59.495 | 76.184 | 2.401 | 59.214 | 69.308 | 1 | 35 | 16.494 | 1.170 | no | 45.630 | 73.931 | 69.308 | 69.308 | 45.133 | 74.069 | 43.439 | 76.451 | 69.308 | 69.308 | 42.283 | 76.621 | 3217 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | XGB-37 | 54.405 | 67.592 | 2.208 | 53.274 | 94.008 | 1 | 35 | 72.793 | 1.765 | no | 42.083 | 67.348 | 94.008 | 94.008 | 40.678 | 66.267 | 39.918 | 69.971 | 94.008 | 94.008 | 38.051 | 69.357 | 3217 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | GC3 | 69.886 | 90.950 | 2.877 | 70.976 | 31.716 | 1 | 35 | -54.618 | 0.447 | no | 54.575 | 85.103 | 31.716 | 31.716 | 55.554 | 86.535 | 48.239 | 92.064 | 31.716 | 31.716 | 49.043 | 93.377 | 3217 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | GE | 68.358 | 87.432 | 2.805 | 69.220 | 38.175 | 1 | 35 | -44.154 | 0.552 | no | 53.874 | 82.996 | 38.175 | 38.175 | 54.612 | 83.935 | 48.642 | 88.941 | 38.175 | 38.175 | 49.023 | 90.041 | 3217 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | XGB-43 | 53.252 | 66.371 | 2.165 | 52.387 | 83.543 | 1 | 35 | 56.882 | 1.595 | sí | 41.063 | 65.918 | 83.543 | 83.543 | 39.839 | 65.123 | 38.923 | 68.403 | 83.543 | 83.543 | 37.074 | 68.019 | 3217 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | Naive | 82.158 | 95.959 | 3.326 | 77.560 | 86.272 | 19 | 17 | 5.007 | 1.112 | no | 66.161 | 98.885 | 64.576 | 108.582 | 55.683 | 101.433 | 67.740 | 97.332 | 69.218 | 104.957 | 55.675 | 100.690 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | Seasonal Naive | 28.059 | 36.507 | 1.145 | 12.542 | 41.943 | 19 | 17 | 49.482 | 3.344 | no | 22.262 | 34.853 | 33.370 | 53.157 | 8.243 | 17.205 | 21.101 | 35.349 | 31.918 | 53.384 | 7.639 | 17.916 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | Chronos | 34.960 | 41.941 | 1.415 | 34.657 | 35.230 | 19 | 17 | 0.774 | 1.017 | no | 27.772 | 42.598 | 24.632 | 47.245 | 25.677 | 44.239 | 27.531 | 42.712 | 25.975 | 46.053 | 24.492 | 44.289 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | SARIMA | 22.004 | 29.635 | 0.891 | 15.905 | 27.461 | 19 | 17 | 24.801 | 1.727 | no | 16.052 | 28.799 | 17.839 | 39.286 | 10.905 | 21.692 | 16.070 | 28.853 | 18.414 | 38.048 | 10.789 | 21.764 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | SARIMA-sel | 20.936 | 28.715 | 0.847 | 14.050 | 27.097 | 19 | 17 | 29.429 | 1.929 | no | 15.226 | 27.667 | 17.519 | 39.012 | 9.732 | 18.795 | 15.220 | 27.556 | 18.037 | 37.657 | 9.634 | 19.054 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | Ridge | 63.968 | 80.990 | 2.581 | 48.327 | 77.962 | 19 | 17 | 21.877 | 1.613 | no | 50.093 | 78.119 | 58.372 | 98.100 | 30.361 | 70.711 | 48.590 | 80.399 | 60.002 | 99.915 | 28.134 | 71.874 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | ElasticNet | 59.495 | 76.184 | 2.401 | 47.881 | 69.886 | 19 | 17 | 17.466 | 1.460 | no | 45.630 | 73.931 | 50.037 | 90.569 | 29.929 | 69.904 | 43.439 | 76.451 | 51.713 | 92.241 | 27.864 | 70.873 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | XGB-37 | 54.405 | 67.592 | 2.208 | 51.656 | 56.865 | 19 | 17 | 4.521 | 1.101 | no | 42.083 | 67.348 | 38.710 | 75.822 | 34.765 | 69.094 | 39.918 | 69.971 | 40.478 | 76.880 | 33.402 | 69.680 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | GC3 | 69.886 | 90.950 | 2.877 | 57.546 | 80.927 | 19 | 17 | 15.798 | 1.406 | no | 54.575 | 85.103 | 61.383 | 101.863 | 37.242 | 80.415 | 48.239 | 92.064 | 56.339 | 106.228 | 34.175 | 84.137 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | GE | 68.358 | 87.432 | 2.805 | 58.063 | 77.568 | 19 | 17 | 13.474 | 1.336 | no | 53.874 | 82.996 | 59.296 | 97.035 | 38.987 | 79.798 | 48.642 | 88.941 | 56.699 | 100.305 | 35.974 | 82.934 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | XGB-43 | 53.252 | 66.371 | 2.165 | 52.410 | 54.005 | 19 | 17 | 1.414 | 1.030 | sí | 41.063 | 65.918 | 35.729 | 73.073 | 36.106 | 69.046 | 38.923 | 68.403 | 37.480 | 73.512 | 35.237 | 69.448 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | Naive | 82.158 | 95.959 | 3.326 | 77.835 | 87.562 | 16 | 20 | 6.577 | 1.125 | no | 66.161 | 98.885 | 63.653 | 113.148 | 57.558 | 99.578 | 67.740 | 97.332 | 68.160 | 108.863 | 57.562 | 99.170 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | Seasonal Naive | 28.059 | 36.507 | 1.145 | 14.870 | 44.546 | 16 | 20 | 58.756 | 2.996 | no | 22.262 | 34.853 | 34.819 | 57.664 | 10.414 | 19.472 | 21.101 | 35.349 | 33.185 | 56.374 | 9.406 | 20.394 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | Chronos | 34.960 | 41.941 | 1.415 | 34.782 | 35.182 | 16 | 20 | 0.635 | 1.011 | no | 27.772 | 42.598 | 23.166 | 48.897 | 26.685 | 43.029 | 27.531 | 42.712 | 25.263 | 48.146 | 26.150 | 43.384 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | SARIMA | 22.004 | 29.635 | 0.891 | 15.653 | 29.944 | 16 | 20 | 36.082 | 1.913 | no | 16.052 | 28.799 | 18.872 | 43.182 | 11.171 | 20.587 | 16.070 | 28.853 | 19.584 | 41.189 | 11.212 | 20.799 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | SARIMA-sel | 20.936 | 28.715 | 0.847 | 13.983 | 29.628 | 16 | 20 | 41.516 | 2.119 | no | 15.226 | 27.667 | 18.695 | 42.918 | 10.081 | 18.027 | 15.220 | 27.556 | 19.433 | 40.829 | 10.022 | 18.418 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | Ridge | 63.968 | 80.990 | 2.581 | 47.961 | 83.977 | 16 | 20 | 31.280 | 1.751 | no | 50.093 | 78.119 | 62.103 | 106.488 | 31.867 | 67.317 | 48.590 | 80.399 | 63.167 | 109.134 | 29.176 | 69.002 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | ElasticNet | 59.495 | 76.184 | 2.401 | 47.581 | 74.387 | 16 | 20 | 25.032 | 1.563 | no | 45.630 | 73.931 | 52.029 | 98.010 | 31.642 | 66.455 | 43.439 | 76.451 | 52.986 | 101.644 | 29.107 | 68.011 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | XGB-37 | 54.405 | 67.592 | 2.208 | 51.724 | 57.757 | 16 | 20 | 6.160 | 1.117 | no | 42.083 | 67.348 | 38.790 | 78.613 | 35.843 | 67.743 | 39.918 | 69.971 | 39.097 | 82.487 | 34.894 | 68.960 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | GC3 | 69.886 | 90.950 | 2.877 | 62.193 | 79.502 | 16 | 20 | 13.760 | 1.278 | no | 54.575 | 85.103 | 59.185 | 101.499 | 41.411 | 83.781 | 48.239 | 92.064 | 56.489 | 105.015 | 36.177 | 89.869 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | GE | 68.358 | 87.432 | 2.805 | 62.480 | 75.704 | 16 | 20 | 10.747 | 1.212 | no | 53.874 | 82.996 | 57.676 | 95.888 | 42.486 | 83.407 | 48.642 | 88.941 | 57.315 | 98.075 | 37.638 | 89.063 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | XGB-43 | 53.252 | 66.371 | 2.165 | 52.865 | 53.735 | 16 | 20 | 0.908 | 1.016 | sí | 41.063 | 65.918 | 34.458 | 74.856 | 37.613 | 67.990 | 38.923 | 68.403 | 35.311 | 77.686 | 36.927 | 69.401 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | Naive | 82.158 | 95.959 | 3.326 | 76.947 | 92.579 | 12 | 24 | 12.684 | 1.203 | no | 66.161 | 98.885 | 63.091 | 123.608 | 58.901 | 96.193 | 67.740 | 97.332 | 69.133 | 121.943 | 57.211 | 97.794 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | Seasonal Naive | 28.059 | 36.507 | 1.145 | 18.917 | 46.343 | 12 | 24 | 65.163 | 2.450 | no | 22.262 | 34.853 | 33.785 | 63.050 | 13.948 | 24.137 | 21.101 | 35.349 | 31.340 | 61.455 | 12.044 | 25.202 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | Chronos | 34.960 | 41.941 | 1.415 | 33.440 | 38.000 | 12 | 24 | 8.696 | 1.136 | no | 27.772 | 42.598 | 22.508 | 55.401 | 26.288 | 41.047 | 27.531 | 42.712 | 26.047 | 56.589 | 24.665 | 41.754 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | SARIMA | 22.004 | 29.635 | 0.891 | 18.296 | 29.420 | 12 | 24 | 33.700 | 1.608 | no | 16.052 | 28.799 | 14.945 | 46.200 | 13.780 | 23.132 | 16.070 | 28.853 | 14.850 | 43.776 | 13.874 | 22.989 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | SARIMA-sel | 20.936 | 28.715 | 0.847 | 16.557 | 29.695 | 12 | 24 | 41.835 | 1.794 | no | 15.226 | 27.667 | 15.235 | 46.537 | 12.527 | 20.821 | 15.220 | 27.556 | 15.419 | 43.850 | 12.433 | 20.749 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | Ridge | 63.968 | 80.990 | 2.581 | 55.729 | 80.446 | 12 | 24 | 25.760 | 1.444 | no | 50.093 | 78.119 | 54.921 | 106.336 | 40.441 | 73.109 | 48.590 | 80.399 | 59.096 | 117.341 | 34.180 | 75.773 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | ElasticNet | 59.495 | 76.184 | 2.401 | 55.111 | 68.263 | 12 | 24 | 14.737 | 1.239 | no | 45.630 | 73.931 | 42.299 | 95.431 | 39.948 | 71.935 | 43.439 | 76.451 | 47.923 | 106.067 | 33.815 | 74.609 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | XGB-37 | 54.405 | 67.592 | 2.208 | 57.967 | 47.281 | 12 | 24 | -13.094 | 0.816 | no | 42.083 | 67.348 | 31.337 | 63.296 | 42.829 | 73.940 | 39.918 | 69.971 | 35.226 | 67.641 | 38.227 | 76.329 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | GC3 | 69.886 | 90.950 | 2.877 | 70.480 | 68.696 | 12 | 24 | -1.702 | 0.975 | no | 54.575 | 85.103 | 48.867 | 90.216 | 50.545 | 90.756 | 48.239 | 92.064 | 45.452 | 90.220 | 39.925 | 99.688 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | GE | 68.358 | 87.432 | 2.805 | 68.847 | 67.379 | 12 | 24 | -1.431 | 0.979 | no | 53.874 | 82.996 | 49.661 | 86.972 | 49.851 | 88.610 | 48.642 | 88.941 | 50.759 | 86.628 | 40.654 | 96.672 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | XGB-43 | 53.252 | 66.371 | 2.165 | 57.818 | 44.120 | 12 | 24 | -17.149 | 0.763 | sí | 41.063 | 65.918 | 26.854 | 61.322 | 43.622 | 73.079 | 38.923 | 68.403 | 31.243 | 63.708 | 39.418 | 75.424 | 0 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | Naive | 82.158 | 95.959 | 3.326 | 84.440 | 57.054 | 3 | 33 | -30.556 | 0.676 | no | 66.161 | 98.885 | 52.024 | 62.083 | 67.233 | 102.037 | 67.740 | 97.332 | 41.090 | 72.580 | 68.649 | 101.262 | 613 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | Seasonal Naive | 28.059 | 36.507 | 1.145 | 23.251 | 80.953 | 3 | 33 | 188.509 | 3.482 | no | 22.262 | 34.853 | 57.646 | 104.261 | 19.016 | 27.396 | 21.101 | 35.349 | 53.789 | 123.711 | 17.760 | 28.403 | 613 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | Chronos | 34.960 | 41.941 | 1.415 | 34.385 | 41.281 | 3 | 33 | 18.083 | 1.201 | no | 27.772 | 42.598 | 6.948 | 75.614 | 27.756 | 41.300 | 27.531 | 42.712 | 0.003 | 103.001 | 26.463 | 42.444 | 613 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | SARIMA | 22.004 | 29.635 | 0.891 | 17.902 | 67.134 | 3 | 33 | 205.094 | 3.750 | no | 16.052 | 28.799 | 46.726 | 87.541 | 13.822 | 22.234 | 16.070 | 28.853 | 26.891 | 88.114 | 14.386 | 21.581 | 613 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | SARIMA-sel | 20.936 | 28.715 | 0.847 | 16.696 | 67.576 | 3 | 33 | 222.772 | 4.047 | no | 15.226 | 27.667 | 46.585 | 88.568 | 13.012 | 20.424 | 15.220 | 27.556 | 25.261 | 89.232 | 13.406 | 20.004 | 613 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | Ridge | 63.968 | 80.990 | 2.581 | 63.580 | 68.236 | 3 | 33 | 6.672 | 1.073 | no | 50.093 | 78.119 | 24.787 | 111.685 | 49.730 | 77.996 | 48.590 | 80.399 | 21.489 | 156.782 | 46.862 | 80.639 | 613 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | ElasticNet | 59.495 | 76.184 | 2.401 | 59.624 | 58.075 | 3 | 33 | -2.387 | 0.974 | no | 45.630 | 73.931 | 14.026 | 102.124 | 45.760 | 74.384 | 43.439 | 76.451 | 12.818 | 144.966 | 42.110 | 77.164 | 613 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | XGB-37 | 54.405 | 67.592 | 2.208 | 54.272 | 55.870 | 3 | 33 | 2.693 | 1.029 | no | 42.083 | 67.348 | 44.767 | 66.974 | 40.863 | 67.730 | 39.918 | 69.971 | 20.622 | 90.149 | 38.494 | 70.128 | 613 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | GC3 | 69.886 | 90.950 | 2.877 | 68.952 | 80.155 | 3 | 33 | 14.695 | 1.162 | no | 54.575 | 85.103 | 50.866 | 109.444 | 53.376 | 84.617 | 48.239 | 92.064 | 47.776 | 135.643 | 44.875 | 92.735 | 613 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | GE | 68.358 | 87.432 | 2.805 | 68.088 | 71.324 | 3 | 33 | 4.340 | 1.048 | no | 53.874 | 82.996 | 41.920 | 100.729 | 53.278 | 83.256 | 48.642 | 88.941 | 35.248 | 123.461 | 46.035 | 89.934 | 613 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | XGB-43 | 53.252 | 66.371 | 2.165 | 52.850 | 57.679 | 3 | 33 | 8.314 | 1.091 | sí | 41.063 | 65.918 | 41.575 | 73.784 | 39.906 | 65.784 | 38.923 | 68.403 | 17.326 | 102.013 | 37.605 | 68.240 | 613 |

### T08_ranking_empates.csv — T08 completa: ranking, diferencia con el mejor e indicador 'primero' (iid y bloques)

`06_metricas/agregadas/T08_ranking_empates.csv` — 1280 filas × 13 columnas.

| conjunto | cultivar | tipo | percentil | criterio | bootstrap | modelo | MAE | posicion | dif_vs_mejor_lo | dif_vs_mejor_hi | primero | n_meses |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| principal_2021_2025 | sutil | mensual | 50 | shock | iid | Naive | 6,021.010 | 5 | 1,646.621 | 3,696.866 | no | 29 |
| principal_2021_2025 | sutil | mensual | 50 | shock | iid | Seasonal Naive | 6,077.552 | 6 | 1,570.199 | 3,889.571 | no | 29 |
| principal_2021_2025 | sutil | mensual | 50 | shock | iid | Chronos | 3,538.684 | 2 | -663.376 | 1,059.165 | sí | 29 |
| principal_2021_2025 | sutil | mensual | 50 | shock | iid | SARIMA | 3,635.765 | 3 | -532.952 | 1,002.688 | sí | 29 |
| principal_2021_2025 | sutil | mensual | 50 | shock | iid | SARIMA-sel | 3,361.657 | 1 | 0.000 | 0.000 | sí | 29 |
| principal_2021_2025 | sutil | mensual | 50 | shock | iid | Ridge | 6,887.424 | 9 | 1,453.481 | 5,789.983 | no | 29 |
| principal_2021_2025 | sutil | mensual | 50 | shock | iid | ElasticNet | 6,898.785 | 10 | 1,686.063 | 5,548.444 | no | 29 |
| principal_2021_2025 | sutil | mensual | 50 | shock | iid | XGB-37 | 4,894.672 | 4 | 523.576 | 2,529.365 | no | 29 |
| principal_2021_2025 | sutil | mensual | 50 | shock | iid | GC3 | 6,218.033 | 8 | 1,774.834 | 3,945.956 | no | 29 |
| principal_2021_2025 | sutil | mensual | 50 | shock | iid | GE | 6,135.792 | 7 | 1,680.944 | 3,902.749 | no | 29 |
| principal_2021_2025 | sutil | mensual | 50 | shock | bloques | Naive | 6,021.010 | 5 | 1,530.479 | 3,853.046 | no | 29 |
| principal_2021_2025 | sutil | mensual | 50 | shock | bloques | Seasonal Naive | 6,077.552 | 6 | 1,342.856 | 4,088.698 | no | 29 |
| principal_2021_2025 | sutil | mensual | 50 | shock | bloques | Chronos | 3,538.684 | 2 | -727.707 | 1,028.950 | sí | 29 |
| principal_2021_2025 | sutil | mensual | 50 | shock | bloques | SARIMA | 3,635.765 | 3 | -402.134 | 988.303 | sí | 29 |
| principal_2021_2025 | sutil | mensual | 50 | shock | bloques | SARIMA-sel | 3,361.657 | 1 | 0.000 | 0.000 | sí | 29 |
| principal_2021_2025 | sutil | mensual | 50 | shock | bloques | Ridge | 6,887.424 | 9 | 1,240.849 | 6,153.568 | no | 29 |
| principal_2021_2025 | sutil | mensual | 50 | shock | bloques | ElasticNet | 6,898.785 | 10 | 1,409.906 | 5,832.695 | no | 29 |
| principal_2021_2025 | sutil | mensual | 50 | shock | bloques | XGB-37 | 4,894.672 | 4 | 480.078 | 2,584.549 | no | 29 |
| principal_2021_2025 | sutil | mensual | 50 | shock | bloques | GC3 | 6,218.033 | 8 | 1,581.106 | 4,189.153 | no | 29 |
| principal_2021_2025 | sutil | mensual | 50 | shock | bloques | GE | 6,135.792 | 7 | 1,441.135 | 4,166.766 | no | 29 |
| principal_2021_2025 | sutil | mensual | 50 | normal | iid | Naive | 1,381.772 | 1 | 0.000 | 0.000 | sí | 31 |
| principal_2021_2025 | sutil | mensual | 50 | normal | iid | Seasonal Naive | 6,072.392 | 8 | 3,284.006 | 6,051.286 | no | 31 |
| principal_2021_2025 | sutil | mensual | 50 | normal | iid | Chronos | 1,815.837 | 2 | -174.108 | 1,011.700 | sí | 31 |
| principal_2021_2025 | sutil | mensual | 50 | normal | iid | SARIMA | 3,103.550 | 6 | 807.372 | 2,655.191 | no | 31 |
| principal_2021_2025 | sutil | mensual | 50 | normal | iid | SARIMA-sel | 3,060.146 | 4 | 774.526 | 2,615.232 | no | 31 |
| principal_2021_2025 | sutil | mensual | 50 | normal | iid | Ridge | 3,089.447 | 5 | 849.728 | 2,603.226 | no | 31 |
| principal_2021_2025 | sutil | mensual | 50 | normal | iid | ElasticNet | 2,975.804 | 3 | 718.714 | 2,524.210 | no | 31 |
| principal_2021_2025 | sutil | mensual | 50 | normal | iid | XGB-37 | 4,869.081 | 7 | 2,380.559 | 4,641.522 | no | 31 |
| principal_2021_2025 | sutil | mensual | 50 | normal | iid | GC3 | 6,495.333 | 9 | 3,601.318 | 6,775.050 | no | 31 |
| principal_2021_2025 | sutil | mensual | 50 | normal | iid | GE | 7,312.059 | 10 | 4,364.131 | 7,629.242 | no | 31 |
| principal_2021_2025 | sutil | mensual | 50 | normal | bloques | Naive | 1,381.772 | 1 | 0.000 | 0.000 | sí | 31 |
| principal_2021_2025 | sutil | mensual | 50 | normal | bloques | Seasonal Naive | 6,072.392 | 8 | 2,882.970 | 6,600.920 | no | 31 |
| principal_2021_2025 | sutil | mensual | 50 | normal | bloques | Chronos | 1,815.837 | 2 | -121.638 | 1,036.644 | sí | 31 |
| principal_2021_2025 | sutil | mensual | 50 | normal | bloques | SARIMA | 3,103.550 | 6 | 811.285 | 2,635.328 | no | 31 |
| principal_2021_2025 | sutil | mensual | 50 | normal | bloques | SARIMA-sel | 3,060.146 | 4 | 840.930 | 2,561.786 | no | 31 |
| principal_2021_2025 | sutil | mensual | 50 | normal | bloques | Ridge | 3,089.447 | 5 | 730.301 | 2,784.649 | no | 31 |
| principal_2021_2025 | sutil | mensual | 50 | normal | bloques | ElasticNet | 2,975.804 | 3 | 561.762 | 2,802.609 | no | 31 |
| principal_2021_2025 | sutil | mensual | 50 | normal | bloques | XGB-37 | 4,869.081 | 7 | 2,062.659 | 4,952.350 | no | 31 |
| principal_2021_2025 | sutil | mensual | 50 | normal | bloques | GC3 | 6,495.333 | 9 | 2,945.545 | 7,468.950 | no | 31 |
| principal_2021_2025 | sutil | mensual | 50 | normal | bloques | GE | 7,312.059 | 10 | 3,500.766 | 8,399.693 | no | 31 |
| principal_2021_2025 | sutil | mensual | 60 | shock | iid | Naive | 6,433.814 | 8 | 1,840.011 | 4,075.390 | no | 25 |
| principal_2021_2025 | sutil | mensual | 60 | shock | iid | Seasonal Naive | 6,319.781 | 5 | 1,570.146 | 4,144.209 | no | 25 |
| principal_2021_2025 | sutil | mensual | 60 | shock | iid | Chronos | 3,773.724 | 3 | -618.258 | 1,246.077 | sí | 25 |
| principal_2021_2025 | sutil | mensual | 60 | shock | iid | SARIMA | 3,524.969 | 2 | -783.449 | 828.495 | sí | 25 |
| principal_2021_2025 | sutil | mensual | 60 | shock | iid | SARIMA-sel | 3,477.513 | 1 | 0.000 | 0.000 | sí | 25 |
| principal_2021_2025 | sutil | mensual | 60 | shock | iid | Ridge | 7,496.933 | 10 | 1,595.045 | 6,643.578 | no | 25 |
| principal_2021_2025 | sutil | mensual | 60 | shock | iid | ElasticNet | 7,426.237 | 9 | 1,801.490 | 6,290.072 | no | 25 |
| principal_2021_2025 | sutil | mensual | 60 | shock | iid | XGB-37 | 5,217.449 | 4 | 649.767 | 2,814.538 | no | 25 |
| principal_2021_2025 | sutil | mensual | 60 | shock | iid | GC3 | 6,385.458 | 6 | 1,724.458 | 4,091.050 | no | 25 |
| principal_2021_2025 | sutil | mensual | 60 | shock | iid | GE | 6,401.773 | 7 | 1,741.591 | 4,124.713 | no | 25 |
| principal_2021_2025 | sutil | mensual | 60 | shock | bloques | Naive | 6,433.814 | 8 | 1,754.370 | 4,230.493 | no | 25 |
| principal_2021_2025 | sutil | mensual | 60 | shock | bloques | Seasonal Naive | 6,319.781 | 5 | 1,335.036 | 4,459.573 | no | 25 |
| principal_2021_2025 | sutil | mensual | 60 | shock | bloques | Chronos | 3,773.724 | 3 | -694.759 | 1,232.526 | sí | 25 |
| principal_2021_2025 | sutil | mensual | 60 | shock | bloques | SARIMA | 3,524.969 | 2 | -793.157 | 901.214 | sí | 25 |
| principal_2021_2025 | sutil | mensual | 60 | shock | bloques | SARIMA-sel | 3,477.513 | 1 | 0.000 | 0.000 | sí | 25 |
| principal_2021_2025 | sutil | mensual | 60 | shock | bloques | Ridge | 7,496.933 | 10 | 1,381.276 | 7,171.433 | no | 25 |
| principal_2021_2025 | sutil | mensual | 60 | shock | bloques | ElasticNet | 7,426.237 | 9 | 1,517.078 | 6,735.709 | no | 25 |
| principal_2021_2025 | sutil | mensual | 60 | shock | bloques | XGB-37 | 5,217.449 | 4 | 616.069 | 2,886.774 | no | 25 |
| principal_2021_2025 | sutil | mensual | 60 | shock | bloques | GC3 | 6,385.458 | 6 | 1,515.316 | 4,440.016 | no | 25 |
| principal_2021_2025 | sutil | mensual | 60 | shock | bloques | GE | 6,401.773 | 7 | 1,472.511 | 4,487.671 | no | 25 |
| principal_2021_2025 | sutil | mensual | 60 | normal | iid | Naive | 1,617.110 | 1 | 0.000 | 0.000 | sí | 35 |
| principal_2021_2025 | sutil | mensual | 60 | normal | iid | Seasonal Naive | 5,899.961 | 8 | 3,012.177 | 5,534.004 | no | 35 |
| principal_2021_2025 | sutil | mensual | 60 | normal | iid | Chronos | 1,844.848 | 2 | -336.929 | 795.960 | sí | 35 |
| principal_2021_2025 | sutil | mensual | 60 | normal | iid | SARIMA | 3,243.514 | 6 | 797.554 | 2,485.670 | no | 35 |
| principal_2021_2025 | sutil | mensual | 60 | normal | iid | SARIMA-sel | 3,011.850 | 3 | 560.056 | 2,306.402 | no | 35 |
| principal_2021_2025 | sutil | mensual | 60 | normal | iid | Ridge | 3,088.138 | 5 | 599.823 | 2,377.022 | no | 35 |
| principal_2021_2025 | sutil | mensual | 60 | normal | iid | ElasticNet | 3,047.393 | 4 | 524.288 | 2,365.499 | no | 35 |
| principal_2021_2025 | sutil | mensual | 60 | normal | iid | XGB-37 | 4,641.450 | 7 | 1,997.867 | 4,140.940 | no | 35 |
| principal_2021_2025 | sutil | mensual | 60 | normal | iid | GC3 | 6,344.052 | 9 | 3,336.701 | 6,237.076 | no | 35 |
| principal_2021_2025 | sutil | mensual | 60 | normal | iid | GE | 6,987.642 | 10 | 3,916.091 | 6,952.670 | no | 35 |
| principal_2021_2025 | sutil | mensual | 60 | normal | bloques | Naive | 1,617.110 | 1 | 0.000 | 0.000 | sí | 35 |
| principal_2021_2025 | sutil | mensual | 60 | normal | bloques | Seasonal Naive | 5,899.961 | 8 | 2,657.584 | 6,039.261 | no | 35 |
| principal_2021_2025 | sutil | mensual | 60 | normal | bloques | Chronos | 1,844.848 | 2 | -313.837 | 829.567 | sí | 35 |
| principal_2021_2025 | sutil | mensual | 60 | normal | bloques | SARIMA | 3,243.514 | 6 | 796.617 | 2,488.657 | no | 35 |
| principal_2021_2025 | sutil | mensual | 60 | normal | bloques | SARIMA-sel | 3,011.850 | 3 | 580.752 | 2,233.428 | no | 35 |
| principal_2021_2025 | sutil | mensual | 60 | normal | bloques | Ridge | 3,088.138 | 5 | 548.320 | 2,496.671 | no | 35 |
| principal_2021_2025 | sutil | mensual | 60 | normal | bloques | ElasticNet | 3,047.393 | 4 | 462.125 | 2,568.158 | no | 35 |
| principal_2021_2025 | sutil | mensual | 60 | normal | bloques | XGB-37 | 4,641.450 | 7 | 1,720.149 | 4,415.785 | no | 35 |
| principal_2021_2025 | sutil | mensual | 60 | normal | bloques | GC3 | 6,344.052 | 9 | 2,786.094 | 6,834.306 | no | 35 |
| principal_2021_2025 | sutil | mensual | 60 | normal | bloques | GE | 6,987.642 | 10 | 3,135.305 | 7,658.866 | no | 35 |
| principal_2021_2025 | sutil | mensual | 75 | shock | iid | Naive | 8,506.195 | 9 | 3,101.807 | 4,319.284 | no | 10 |
| principal_2021_2025 | sutil | mensual | 75 | shock | iid | Seasonal Naive | 5,034.450 | 3 | -1,966.386 | 2,657.895 | sí | 10 |
| principal_2021_2025 | sutil | mensual | 75 | shock | iid | Chronos | 4,783.522 | 1 | 0.000 | 0.000 | sí | 10 |
| principal_2021_2025 | sutil | mensual | 75 | shock | iid | SARIMA | 5,130.719 | 4 | -354.521 | 1,101.942 | sí | 10 |
| principal_2021_2025 | sutil | mensual | 75 | shock | iid | SARIMA-sel | 4,935.734 | 2 | -1,385.200 | 1,820.692 | sí | 10 |
| principal_2021_2025 | sutil | mensual | 75 | shock | iid | Ridge | 8,556.902 | 10 | 992.553 | 7,654.036 | no | 10 |
| principal_2021_2025 | sutil | mensual | 75 | shock | iid | ElasticNet | 8,153.740 | 8 | 715.515 | 6,570.561 | no | 10 |
| principal_2021_2025 | sutil | mensual | 75 | shock | iid | XGB-37 | 5,955.201 | 5 | -869.236 | 2,809.948 | sí | 10 |
| principal_2021_2025 | sutil | mensual | 75 | shock | iid | GC3 | 6,074.460 | 6 | -174.890 | 2,747.427 | sí | 10 |
| principal_2021_2025 | sutil | mensual | 75 | shock | iid | GE | 6,826.646 | 7 | 78.054 | 3,911.162 | no | 10 |
| principal_2021_2025 | sutil | mensual | 75 | shock | bloques | Naive | 8,506.195 | 9 | 2,809.418 | 4,641.985 | no | 10 |
| principal_2021_2025 | sutil | mensual | 75 | shock | bloques | Seasonal Naive | 5,034.450 | 3 | -2,529.734 | 3,259.969 | sí | 10 |
| principal_2021_2025 | sutil | mensual | 75 | shock | bloques | Chronos | 4,783.522 | 1 | 0.000 | 0.000 | sí | 10 |
| principal_2021_2025 | sutil | mensual | 75 | shock | bloques | SARIMA | 5,130.719 | 4 | -468.008 | 1,080.043 | sí | 10 |
| principal_2021_2025 | sutil | mensual | 75 | shock | bloques | SARIMA-sel | 4,935.734 | 2 | -1,614.031 | 1,663.640 | sí | 10 |
| principal_2021_2025 | sutil | mensual | 75 | shock | bloques | Ridge | 8,556.902 | 10 | 103.040 | 7,408.304 | no | 10 |
| principal_2021_2025 | sutil | mensual | 75 | shock | bloques | ElasticNet | 8,153.740 | 8 | -114.459 | 6,550.440 | sí | 10 |
| principal_2021_2025 | sutil | mensual | 75 | shock | bloques | XGB-37 | 5,955.201 | 5 | -1,307.906 | 3,145.176 | sí | 10 |
| principal_2021_2025 | sutil | mensual | 75 | shock | bloques | GC3 | 6,074.460 | 6 | -698.069 | 2,886.284 | sí | 10 |
| principal_2021_2025 | sutil | mensual | 75 | shock | bloques | GE | 6,826.646 | 7 | -348.400 | 3,818.094 | sí | 10 |
| principal_2021_2025 | sutil | mensual | 75 | normal | iid | Naive | 2,647.646 | 2 | -163.034 | 994.836 | sí | 50 |
| principal_2021_2025 | sutil | mensual | 75 | normal | iid | Seasonal Naive | 6,282.973 | 8 | 3,070.000 | 5,044.738 | no | 50 |
| principal_2021_2025 | sutil | mensual | 75 | normal | iid | Chronos | 2,221.552 | 1 | 0.000 | 0.000 | sí | 50 |
| principal_2021_2025 | sutil | mensual | 75 | normal | iid | SARIMA | 3,006.801 | 4 | 131.602 | 1,428.645 | no | 50 |
| principal_2021_2025 | sutil | mensual | 75 | normal | iid | SARIMA-sel | 2,859.905 | 3 | -61.169 | 1,318.337 | sí | 50 |
| principal_2021_2025 | sutil | mensual | 75 | normal | iid | Ridge | 4,198.783 | 5 | 784.172 | 3,256.636 | no | 50 |
| principal_2021_2025 | sutil | mensual | 75 | normal | iid | ElasticNet | 4,215.546 | 6 | 854.848 | 3,201.279 | no | 50 |
| principal_2021_2025 | sutil | mensual | 75 | normal | iid | XGB-37 | 4,666.700 | 7 | 1,498.242 | 3,409.605 | no | 50 |
| principal_2021_2025 | sutil | mensual | 75 | normal | iid | GC3 | 6,418.674 | 9 | 2,908.929 | 5,522.251 | no | 50 |
| principal_2021_2025 | sutil | mensual | 75 | normal | iid | GE | 6,726.907 | 10 | 3,145.578 | 5,923.863 | no | 50 |
| principal_2021_2025 | sutil | mensual | 75 | normal | bloques | Naive | 2,647.646 | 2 | -126.168 | 983.389 | sí | 50 |
| principal_2021_2025 | sutil | mensual | 75 | normal | bloques | Seasonal Naive | 6,282.973 | 8 | 2,720.059 | 5,375.167 | no | 50 |
| principal_2021_2025 | sutil | mensual | 75 | normal | bloques | Chronos | 2,221.552 | 1 | 0.000 | 0.000 | sí | 50 |
| principal_2021_2025 | sutil | mensual | 75 | normal | bloques | SARIMA | 3,006.801 | 4 | 192.281 | 1,380.221 | no | 50 |
| principal_2021_2025 | sutil | mensual | 75 | normal | bloques | SARIMA-sel | 2,859.905 | 3 | 21.559 | 1,244.424 | no | 50 |
| principal_2021_2025 | sutil | mensual | 75 | normal | bloques | Ridge | 4,198.783 | 5 | 775.727 | 3,330.889 | no | 50 |
| principal_2021_2025 | sutil | mensual | 75 | normal | bloques | ElasticNet | 4,215.546 | 6 | 769.853 | 3,373.825 | no | 50 |
| principal_2021_2025 | sutil | mensual | 75 | normal | bloques | XGB-37 | 4,666.700 | 7 | 1,241.350 | 3,741.270 | no | 50 |
| principal_2021_2025 | sutil | mensual | 75 | normal | bloques | GC3 | 6,418.674 | 9 | 2,373.745 | 6,147.660 | no | 50 |
| principal_2021_2025 | sutil | mensual | 75 | normal | bloques | GE | 6,726.907 | 10 | 2,480.803 | 6,619.191 | no | 50 |
| principal_2021_2025 | sutil | mensual | 90 | shock | iid | Naive | 8,695.623 | 7 | 2,624.312 | 4,190.570 | no | 6 |
| principal_2021_2025 | sutil | mensual | 90 | shock | iid | Seasonal Naive | 7,309.129 | 4 | -1,359.316 | 5,104.858 | sí | 6 |
| principal_2021_2025 | sutil | mensual | 90 | shock | iid | Chronos | 5,436.358 | 1 | 0.000 | 0.000 | sí | 6 |
| principal_2021_2025 | sutil | mensual | 90 | shock | iid | SARIMA | 6,764.376 | 2 | 987.263 | 1,545.143 | no | 6 |
| principal_2021_2025 | sutil | mensual | 90 | shock | iid | SARIMA-sel | 7,095.584 | 3 | 97.723 | 3,574.510 | no | 6 |
| principal_2021_2025 | sutil | mensual | 90 | shock | iid | Ridge | 11,681.953 | 10 | 2,866.127 | 11,601.463 | no | 6 |
| principal_2021_2025 | sutil | mensual | 90 | shock | iid | ElasticNet | 10,856.235 | 9 | 2,525.649 | 9,574.760 | no | 6 |
| principal_2021_2025 | sutil | mensual | 90 | shock | iid | XGB-37 | 7,964.134 | 6 | 1,929.270 | 3,106.661 | no | 6 |
| principal_2021_2025 | sutil | mensual | 90 | shock | iid | GC3 | 7,906.910 | 5 | 805.271 | 4,407.900 | no | 6 |
| principal_2021_2025 | sutil | mensual | 90 | shock | iid | GE | 8,942.238 | 8 | 2,113.770 | 5,124.965 | no | 6 |
| principal_2021_2025 | sutil | mensual | 90 | shock | bloques | Naive | 8,695.623 | 7 | 1,808.636 | 4,811.413 | no | 6 |
| principal_2021_2025 | sutil | mensual | 90 | shock | bloques | Seasonal Naive | 7,309.129 | 4 | -2,944.706 | 6,156.369 | sí | 6 |
| principal_2021_2025 | sutil | mensual | 90 | shock | bloques | Chronos | 5,436.358 | 1 | 0.000 | 0.000 | sí | 6 |
| principal_2021_2025 | sutil | mensual | 90 | shock | bloques | SARIMA | 6,764.376 | 2 | 991.843 | 1,570.247 | no | 6 |
| principal_2021_2025 | sutil | mensual | 90 | shock | bloques | SARIMA-sel | 7,095.584 | 3 | 138.970 | 3,234.589 | no | 6 |
| principal_2021_2025 | sutil | mensual | 90 | shock | bloques | Ridge | 11,681.953 | 10 | 534.745 | 14,581.827 | no | 6 |
| principal_2021_2025 | sutil | mensual | 90 | shock | bloques | ElasticNet | 10,856.235 | 9 | -96.348 | 12,376.125 | sí | 6 |
| principal_2021_2025 | sutil | mensual | 90 | shock | bloques | XGB-37 | 7,964.134 | 6 | 790.650 | 4,574.822 | no | 6 |
| principal_2021_2025 | sutil | mensual | 90 | shock | bloques | GC3 | 7,906.910 | 5 | 519.628 | 4,730.037 | no | 6 |
| principal_2021_2025 | sutil | mensual | 90 | shock | bloques | GE | 8,942.238 | 8 | 1,646.237 | 4,956.608 | no | 6 |
| principal_2021_2025 | sutil | mensual | 90 | normal | iid | Naive | 3,060.565 | 4 | 141.960 | 1,318.703 | no | 54 |
| principal_2021_2025 | sutil | mensual | 90 | normal | iid | Seasonal Naive | 5,937.748 | 8 | 2,602.217 | 4,572.460 | no | 54 |
| principal_2021_2025 | sutil | mensual | 90 | normal | iid | Chronos | 2,338.790 | 1 | 0.000 | 0.000 | sí | 54 |
| principal_2021_2025 | sutil | mensual | 90 | normal | iid | SARIMA | 2,982.611 | 3 | 27.778 | 1,275.603 | no | 54 |
| principal_2021_2025 | sutil | mensual | 90 | normal | iid | SARIMA-sel | 2,773.687 | 2 | -236.975 | 1,116.587 | sí | 54 |
| principal_2021_2025 | sutil | mensual | 90 | normal | iid | Ridge | 4,174.378 | 5 | 733.421 | 3,044.135 | no | 54 |
| principal_2021_2025 | sutil | mensual | 90 | normal | iid | ElasticNet | 4,206.986 | 6 | 787.663 | 3,015.698 | no | 54 |
| principal_2021_2025 | sutil | mensual | 90 | normal | iid | XGB-37 | 4,538.929 | 7 | 1,260.259 | 3,159.323 | no | 54 |
| principal_2021_2025 | sutil | mensual | 90 | normal | iid | GC3 | 6,189.571 | 9 | 2,616.964 | 5,124.456 | no | 54 |
| principal_2021_2025 | sutil | mensual | 90 | normal | iid | GE | 6,499.229 | 10 | 2,825.817 | 5,516.699 | no | 54 |
| principal_2021_2025 | sutil | mensual | 90 | normal | bloques | Naive | 3,060.565 | 4 | 134.603 | 1,320.012 | no | 54 |
| principal_2021_2025 | sutil | mensual | 90 | normal | bloques | Seasonal Naive | 5,937.748 | 8 | 2,301.682 | 4,876.880 | no | 54 |
| principal_2021_2025 | sutil | mensual | 90 | normal | bloques | Chronos | 2,338.790 | 1 | 0.000 | 0.000 | sí | 54 |
| principal_2021_2025 | sutil | mensual | 90 | normal | bloques | SARIMA | 2,982.611 | 3 | 102.208 | 1,197.571 | no | 54 |
| principal_2021_2025 | sutil | mensual | 90 | normal | bloques | SARIMA-sel | 2,773.687 | 2 | -147.566 | 999.012 | sí | 54 |
| principal_2021_2025 | sutil | mensual | 90 | normal | bloques | Ridge | 4,174.378 | 5 | 718.511 | 3,087.625 | no | 54 |
| principal_2021_2025 | sutil | mensual | 90 | normal | bloques | ElasticNet | 4,206.986 | 6 | 720.061 | 3,174.976 | no | 54 |
| principal_2021_2025 | sutil | mensual | 90 | normal | bloques | XGB-37 | 4,538.929 | 7 | 1,034.311 | 3,449.437 | no | 54 |
| principal_2021_2025 | sutil | mensual | 90 | normal | bloques | GC3 | 6,189.571 | 9 | 2,120.202 | 5,702.221 | no | 54 |
| principal_2021_2025 | sutil | mensual | 90 | normal | bloques | GE | 6,499.229 | 10 | 2,248.214 | 6,157.560 | no | 54 |
| principal_2021_2025 | sutil | interanual | 50 | shock | iid | Naive | 3,679.645 | 2 | -422.379 | 1,435.119 | sí | 25 |
| principal_2021_2025 | sutil | interanual | 50 | shock | iid | Seasonal Naive | 10,057.020 | 10 | 5,783.795 | 7,941.902 | no | 25 |
| principal_2021_2025 | sutil | interanual | 50 | shock | iid | Chronos | 3,191.476 | 1 | 0.000 | 0.000 | sí | 25 |
| principal_2021_2025 | sutil | interanual | 50 | shock | iid | SARIMA | 3,941.818 | 3 | -245.818 | 1,670.329 | sí | 25 |
| principal_2021_2025 | sutil | interanual | 50 | shock | iid | SARIMA-sel | 4,063.475 | 4 | -242.861 | 2,008.755 | sí | 25 |
| principal_2021_2025 | sutil | interanual | 50 | shock | iid | Ridge | 5,834.370 | 6 | 951.661 | 4,602.452 | no | 25 |
| principal_2021_2025 | sutil | interanual | 50 | shock | iid | ElasticNet | 6,073.024 | 7 | 1,182.942 | 4,789.494 | no | 25 |
| principal_2021_2025 | sutil | interanual | 50 | shock | iid | XGB-37 | 5,185.590 | 5 | 485.977 | 3,537.278 | no | 25 |
| principal_2021_2025 | sutil | interanual | 50 | shock | iid | GC3 | 7,649.418 | 9 | 2,436.335 | 6,537.508 | no | 25 |
| principal_2021_2025 | sutil | interanual | 50 | shock | iid | GE | 7,639.401 | 8 | 2,446.280 | 6,483.851 | no | 25 |
| principal_2021_2025 | sutil | interanual | 50 | shock | bloques | Naive | 3,679.645 | 2 | -634.179 | 1,564.418 | sí | 25 |
| principal_2021_2025 | sutil | interanual | 50 | shock | bloques | Seasonal Naive | 10,057.020 | 10 | 5,191.122 | 8,568.291 | no | 25 |
| principal_2021_2025 | sutil | interanual | 50 | shock | bloques | Chronos | 3,191.476 | 1 | 0.000 | 0.000 | sí | 25 |
| principal_2021_2025 | sutil | interanual | 50 | shock | bloques | SARIMA | 3,941.818 | 3 | -256.250 | 1,606.028 | sí | 25 |
| principal_2021_2025 | sutil | interanual | 50 | shock | bloques | SARIMA-sel | 4,063.475 | 4 | -246.638 | 1,925.881 | sí | 25 |
| principal_2021_2025 | sutil | interanual | 50 | shock | bloques | Ridge | 5,834.370 | 6 | 433.073 | 5,055.168 | no | 25 |
| principal_2021_2025 | sutil | interanual | 50 | shock | bloques | ElasticNet | 6,073.024 | 7 | 582.692 | 5,378.361 | no | 25 |
| principal_2021_2025 | sutil | interanual | 50 | shock | bloques | XGB-37 | 5,185.590 | 5 | 159.374 | 3,948.637 | no | 25 |
| principal_2021_2025 | sutil | interanual | 50 | shock | bloques | GC3 | 7,649.418 | 9 | 1,699.800 | 7,590.002 | no | 25 |
| principal_2021_2025 | sutil | interanual | 50 | shock | bloques | GE | 7,639.401 | 8 | 1,704.101 | 7,558.003 | no | 25 |
| principal_2021_2025 | sutil | interanual | 50 | normal | iid | Naive | 3,584.374 | 5 | 673.737 | 1,975.879 | no | 35 |
| principal_2021_2025 | sutil | interanual | 50 | normal | iid | Seasonal Naive | 3,230.504 | 4 | 94.017 | 1,831.022 | no | 35 |
| principal_2021_2025 | sutil | interanual | 50 | normal | iid | Chronos | 2,260.740 | 1 | 0.000 | 0.000 | sí | 35 |
| principal_2021_2025 | sutil | interanual | 50 | normal | iid | SARIMA | 2,945.765 | 3 | 63.897 | 1,309.965 | no | 35 |
| principal_2021_2025 | sutil | interanual | 50 | normal | iid | SARIMA-sel | 2,593.306 | 2 | -326.356 | 967.133 | sí | 35 |
| principal_2021_2025 | sutil | interanual | 50 | normal | iid | Ridge | 4,275.683 | 7 | 544.002 | 3,589.235 | no | 35 |
| principal_2021_2025 | sutil | interanual | 50 | normal | iid | ElasticNet | 4,013.974 | 6 | 410.367 | 3,187.908 | no | 35 |
| principal_2021_2025 | sutil | interanual | 50 | normal | iid | XGB-37 | 4,664.206 | 8 | 1,417.847 | 3,354.456 | no | 35 |
| principal_2021_2025 | sutil | interanual | 50 | normal | iid | GC3 | 5,441.224 | 9 | 1,846.182 | 4,475.516 | no | 35 |
| principal_2021_2025 | sutil | interanual | 50 | normal | iid | GE | 6,103.622 | 10 | 2,352.131 | 5,276.884 | no | 35 |
| principal_2021_2025 | sutil | interanual | 50 | normal | bloques | Naive | 3,584.374 | 5 | 698.516 | 1,956.902 | no | 35 |
| principal_2021_2025 | sutil | interanual | 50 | normal | bloques | Seasonal Naive | 3,230.504 | 4 | 289.374 | 1,724.504 | no | 35 |
| principal_2021_2025 | sutil | interanual | 50 | normal | bloques | Chronos | 2,260.740 | 1 | 0.000 | 0.000 | sí | 35 |
| principal_2021_2025 | sutil | interanual | 50 | normal | bloques | SARIMA | 2,945.765 | 3 | 125.599 | 1,305.693 | no | 35 |
| principal_2021_2025 | sutil | interanual | 50 | normal | bloques | SARIMA-sel | 2,593.306 | 2 | -153.735 | 783.940 | sí | 35 |
| principal_2021_2025 | sutil | interanual | 50 | normal | bloques | Ridge | 4,275.683 | 7 | 406.436 | 4,077.861 | no | 35 |
| principal_2021_2025 | sutil | interanual | 50 | normal | bloques | ElasticNet | 4,013.974 | 6 | 262.610 | 3,583.173 | no | 35 |
| principal_2021_2025 | sutil | interanual | 50 | normal | bloques | XGB-37 | 4,664.206 | 8 | 1,417.123 | 3,428.567 | no | 35 |
| principal_2021_2025 | sutil | interanual | 50 | normal | bloques | GC3 | 5,441.224 | 9 | 1,695.329 | 4,658.509 | no | 35 |
| principal_2021_2025 | sutil | interanual | 50 | normal | bloques | GE | 6,103.622 | 10 | 1,930.556 | 5,675.992 | no | 35 |
| principal_2021_2025 | sutil | interanual | 60 | shock | iid | Naive | 3,373.593 | 2 | -433.525 | 1,801.064 | sí | 18 |
| principal_2021_2025 | sutil | interanual | 60 | shock | iid | Seasonal Naive | 10,963.068 | 10 | 6,897.263 | 9,612.485 | no | 18 |
| principal_2021_2025 | sutil | interanual | 60 | shock | iid | Chronos | 2,710.426 | 1 | 0.000 | 0.000 | sí | 18 |
| principal_2021_2025 | sutil | interanual | 60 | shock | iid | SARIMA | 3,665.977 | 3 | -396.136 | 2,203.522 | sí | 18 |
| principal_2021_2025 | sutil | interanual | 60 | shock | iid | SARIMA-sel | 4,227.914 | 4 | 20.906 | 2,969.481 | no | 18 |
| principal_2021_2025 | sutil | interanual | 60 | shock | iid | Ridge | 5,893.281 | 6 | 972.370 | 5,711.894 | no | 18 |
| principal_2021_2025 | sutil | interanual | 60 | shock | iid | ElasticNet | 6,208.986 | 7 | 1,268.109 | 5,976.444 | no | 18 |
| principal_2021_2025 | sutil | interanual | 60 | shock | iid | XGB-37 | 5,011.340 | 5 | 788.490 | 3,958.101 | no | 18 |
| principal_2021_2025 | sutil | interanual | 60 | shock | iid | GC3 | 7,969.970 | 8 | 2,864.621 | 7,828.936 | no | 18 |
| principal_2021_2025 | sutil | interanual | 60 | shock | iid | GE | 8,171.084 | 9 | 3,180.759 | 7,912.190 | no | 18 |
| principal_2021_2025 | sutil | interanual | 60 | shock | bloques | Naive | 3,373.593 | 2 | -817.131 | 2,088.119 | sí | 18 |
| principal_2021_2025 | sutil | interanual | 60 | shock | bloques | Seasonal Naive | 10,963.068 | 10 | 6,197.441 | 10,464.524 | no | 18 |
| principal_2021_2025 | sutil | interanual | 60 | shock | bloques | Chronos | 2,710.426 | 1 | 0.000 | 0.000 | sí | 18 |
| principal_2021_2025 | sutil | interanual | 60 | shock | bloques | SARIMA | 3,665.977 | 3 | -385.734 | 1,926.334 | sí | 18 |
| principal_2021_2025 | sutil | interanual | 60 | shock | bloques | SARIMA-sel | 4,227.914 | 4 | 133.907 | 2,815.712 | no | 18 |
| principal_2021_2025 | sutil | interanual | 60 | shock | bloques | Ridge | 5,893.281 | 6 | 112.268 | 6,389.279 | no | 18 |
| principal_2021_2025 | sutil | interanual | 60 | shock | bloques | ElasticNet | 6,208.986 | 7 | 275.686 | 6,865.833 | no | 18 |
| principal_2021_2025 | sutil | interanual | 60 | shock | bloques | XGB-37 | 5,011.340 | 5 | 309.893 | 4,708.575 | no | 18 |
| principal_2021_2025 | sutil | interanual | 60 | shock | bloques | GC3 | 7,969.970 | 8 | 1,734.173 | 9,449.499 | no | 18 |
| principal_2021_2025 | sutil | interanual | 60 | shock | bloques | GE | 8,171.084 | 9 | 2,147.523 | 9,592.320 | no | 18 |
| principal_2021_2025 | sutil | interanual | 60 | normal | iid | Naive | 3,731.418 | 4 | 491.479 | 1,713.546 | no | 42 |
| principal_2021_2025 | sutil | interanual | 60 | normal | iid | Seasonal Naive | 3,979.951 | 5 | 556.155 | 2,141.862 | no | 42 |
| principal_2021_2025 | sutil | interanual | 60 | normal | iid | Chronos | 2,622.027 | 1 | 0.000 | 0.000 | sí | 42 |
| principal_2021_2025 | sutil | interanual | 60 | normal | iid | SARIMA | 3,229.992 | 3 | 47.871 | 1,182.348 | no | 42 |
| principal_2021_2025 | sutil | interanual | 60 | normal | iid | SARIMA-sel | 2,767.860 | 2 | -463.822 | 750.178 | sí | 42 |
| principal_2021_2025 | sutil | interanual | 60 | normal | iid | Ridge | 4,510.217 | 7 | 642.387 | 3,241.102 | no | 42 |
| principal_2021_2025 | sutil | interanual | 60 | normal | iid | ElasticNet | 4,298.879 | 6 | 537.142 | 2,907.674 | no | 42 |
| principal_2021_2025 | sutil | interanual | 60 | normal | iid | XGB-37 | 4,825.783 | 8 | 1,189.446 | 3,196.798 | no | 42 |
| principal_2021_2025 | sutil | interanual | 60 | normal | iid | GC3 | 5,671.876 | 9 | 1,854.476 | 4,265.181 | no | 42 |
| principal_2021_2025 | sutil | interanual | 60 | normal | iid | GE | 6,131.721 | 10 | 2,101.778 | 4,893.311 | no | 42 |
| principal_2021_2025 | sutil | interanual | 60 | normal | bloques | Naive | 3,731.418 | 4 | 527.368 | 1,699.362 | no | 42 |
| principal_2021_2025 | sutil | interanual | 60 | normal | bloques | Seasonal Naive | 3,979.951 | 5 | 623.530 | 2,136.593 | no | 42 |
| principal_2021_2025 | sutil | interanual | 60 | normal | bloques | Chronos | 2,622.027 | 1 | 0.000 | 0.000 | sí | 42 |
| principal_2021_2025 | sutil | interanual | 60 | normal | bloques | SARIMA | 3,229.992 | 3 | 101.631 | 1,168.564 | no | 42 |
| principal_2021_2025 | sutil | interanual | 60 | normal | bloques | SARIMA-sel | 2,767.860 | 2 | -379.016 | 627.924 | sí | 42 |
| principal_2021_2025 | sutil | interanual | 60 | normal | bloques | Ridge | 4,510.217 | 7 | 468.414 | 3,642.192 | no | 42 |
| principal_2021_2025 | sutil | interanual | 60 | normal | bloques | ElasticNet | 4,298.879 | 6 | 384.713 | 3,234.692 | no | 42 |
| principal_2021_2025 | sutil | interanual | 60 | normal | bloques | XGB-37 | 4,825.783 | 8 | 1,053.326 | 3,410.391 | no | 42 |
| principal_2021_2025 | sutil | interanual | 60 | normal | bloques | GC3 | 5,671.876 | 9 | 1,662.328 | 4,504.211 | no | 42 |
| principal_2021_2025 | sutil | interanual | 60 | normal | bloques | GE | 6,131.721 | 10 | 1,681.462 | 5,385.347 | no | 42 |
| principal_2021_2025 | sutil | interanual | 75 | shock | iid | Naive | 3,171.846 | 2 | -90.077 | 2,851.978 | sí | 10 |
| principal_2021_2025 | sutil | interanual | 75 | shock | iid | Seasonal Naive | 12,508.067 | 10 | 8,351.592 | 12,904.867 | no | 10 |
| principal_2021_2025 | sutil | interanual | 75 | shock | iid | Chronos | 1,864.113 | 1 | 0.000 | 0.000 | sí | 10 |
| principal_2021_2025 | sutil | interanual | 75 | shock | iid | SARIMA | 3,232.720 | 3 | 399.107 | 2,223.819 | no | 10 |
| principal_2021_2025 | sutil | interanual | 75 | shock | iid | SARIMA-sel | 4,078.830 | 4 | 115.027 | 4,343.427 | no | 10 |
| principal_2021_2025 | sutil | interanual | 75 | shock | iid | Ridge | 4,946.068 | 6 | 1,092.543 | 5,265.942 | no | 10 |
| principal_2021_2025 | sutil | interanual | 75 | shock | iid | ElasticNet | 5,403.723 | 7 | 1,279.184 | 6,034.041 | no | 10 |
| principal_2021_2025 | sutil | interanual | 75 | shock | iid | XGB-37 | 4,816.485 | 5 | 446.460 | 5,673.369 | no | 10 |
| principal_2021_2025 | sutil | interanual | 75 | shock | iid | GC3 | 9,166.116 | 8 | 3,189.903 | 11,742.247 | no | 10 |
| principal_2021_2025 | sutil | interanual | 75 | shock | iid | GE | 9,796.027 | 9 | 3,968.769 | 12,152.721 | no | 10 |
| principal_2021_2025 | sutil | interanual | 75 | shock | bloques | Naive | 3,171.846 | 2 | -636.758 | 3,088.766 | sí | 10 |
| principal_2021_2025 | sutil | interanual | 75 | shock | bloques | Seasonal Naive | 12,508.067 | 10 | 7,882.979 | 13,501.157 | no | 10 |
| principal_2021_2025 | sutil | interanual | 75 | shock | bloques | Chronos | 1,864.113 | 1 | 0.000 | 0.000 | sí | 10 |
| principal_2021_2025 | sutil | interanual | 75 | shock | bloques | SARIMA | 3,232.720 | 3 | 456.345 | 2,095.912 | no | 10 |
| principal_2021_2025 | sutil | interanual | 75 | shock | bloques | SARIMA-sel | 4,078.830 | 4 | 424.650 | 4,127.119 | no | 10 |
| principal_2021_2025 | sutil | interanual | 75 | shock | bloques | Ridge | 4,946.068 | 6 | 94.272 | 6,872.000 | no | 10 |
| principal_2021_2025 | sutil | interanual | 75 | shock | bloques | ElasticNet | 5,403.723 | 7 | 198.191 | 7,714.674 | no | 10 |
| principal_2021_2025 | sutil | interanual | 75 | shock | bloques | XGB-37 | 4,816.485 | 5 | -535.557 | 7,391.956 | sí | 10 |
| principal_2021_2025 | sutil | interanual | 75 | shock | bloques | GC3 | 9,166.116 | 8 | 1,629.452 | 14,389.527 | no | 10 |
| principal_2021_2025 | sutil | interanual | 75 | shock | bloques | GE | 9,796.027 | 9 | 2,542.034 | 14,809.464 | no | 10 |
| principal_2021_2025 | sutil | interanual | 75 | normal | iid | Naive | 3,714.515 | 4 | 280.004 | 1,538.024 | no | 50 |
| principal_2021_2025 | sutil | interanual | 75 | normal | iid | Seasonal Naive | 4,788.250 | 6 | 1,187.367 | 2,754.158 | no | 50 |
| principal_2021_2025 | sutil | interanual | 75 | normal | iid | Chronos | 2,805.433 | 1 | 0.000 | 0.000 | sí | 50 |
| principal_2021_2025 | sutil | interanual | 75 | normal | iid | SARIMA | 3,386.401 | 3 | -60.404 | 1,213.916 | sí | 50 |
| principal_2021_2025 | sutil | interanual | 75 | normal | iid | SARIMA-sel | 3,031.286 | 2 | -401.465 | 834.702 | sí | 50 |
| principal_2021_2025 | sutil | interanual | 75 | normal | iid | Ridge | 4,920.950 | 8 | 824.036 | 3,533.722 | no | 50 |
| principal_2021_2025 | sutil | interanual | 75 | normal | iid | ElasticNet | 4,765.549 | 5 | 779.509 | 3,251.005 | no | 50 |
| principal_2021_2025 | sutil | interanual | 75 | normal | iid | XGB-37 | 4,894.443 | 7 | 1,181.635 | 2,984.011 | no | 50 |
| principal_2021_2025 | sutil | interanual | 75 | normal | iid | GC3 | 5,800.342 | 9 | 1,893.089 | 4,073.825 | no | 50 |
| principal_2021_2025 | sutil | interanual | 75 | normal | iid | GE | 6,133.031 | 10 | 2,104.373 | 4,515.324 | no | 50 |
| principal_2021_2025 | sutil | interanual | 75 | normal | bloques | Naive | 3,714.515 | 4 | 384.037 | 1,424.729 | no | 50 |
| principal_2021_2025 | sutil | interanual | 75 | normal | bloques | Seasonal Naive | 4,788.250 | 6 | 1,130.094 | 2,852.562 | no | 50 |
| principal_2021_2025 | sutil | interanual | 75 | normal | bloques | Chronos | 2,805.433 | 1 | 0.000 | 0.000 | sí | 50 |
| principal_2021_2025 | sutil | interanual | 75 | normal | bloques | SARIMA | 3,386.401 | 3 | 3.732 | 1,169.129 | no | 50 |
| principal_2021_2025 | sutil | interanual | 75 | normal | bloques | SARIMA-sel | 3,031.286 | 2 | -280.643 | 710.034 | sí | 50 |
| principal_2021_2025 | sutil | interanual | 75 | normal | bloques | Ridge | 4,920.950 | 8 | 787.849 | 3,597.151 | no | 50 |
| principal_2021_2025 | sutil | interanual | 75 | normal | bloques | ElasticNet | 4,765.549 | 5 | 739.771 | 3,271.630 | no | 50 |
| principal_2021_2025 | sutil | interanual | 75 | normal | bloques | XGB-37 | 4,894.443 | 7 | 1,088.455 | 3,103.456 | no | 50 |
| principal_2021_2025 | sutil | interanual | 75 | normal | bloques | GC3 | 5,800.342 | 9 | 1,722.560 | 4,359.889 | no | 50 |
| principal_2021_2025 | sutil | interanual | 75 | normal | bloques | GE | 6,133.031 | 10 | 1,759.838 | 4,940.696 | no | 50 |
| principal_2021_2025 | sutil | interanual | 90 | shock | iid | Naive | 1,538.943 | 2 | -872.232 | 1,946.963 | sí | 4 |
| principal_2021_2025 | sutil | interanual | 90 | shock | iid | Seasonal Naive | 15,258.750 | 10 | 10,697.834 | 16,638.532 | no | 4 |
| principal_2021_2025 | sutil | interanual | 90 | shock | iid | Chronos | 1,116.204 | 1 | 0.000 | 0.000 | sí | 4 |
| principal_2021_2025 | sutil | interanual | 90 | shock | iid | SARIMA | 3,725.435 | 3 | 1,722.092 | 3,294.135 | no | 4 |
| principal_2021_2025 | sutil | interanual | 90 | shock | iid | SARIMA-sel | 5,506.388 | 6 | 2,270.739 | 6,509.629 | no | 4 |
| principal_2021_2025 | sutil | interanual | 90 | shock | iid | Ridge | 4,169.104 | 4 | 348.179 | 5,942.954 | no | 4 |
| principal_2021_2025 | sutil | interanual | 90 | shock | iid | ElasticNet | 4,817.704 | 5 | 439.913 | 6,974.822 | no | 4 |
| principal_2021_2025 | sutil | interanual | 90 | shock | iid | XGB-37 | 5,555.691 | 7 | -322.930 | 9,201.904 | sí | 4 |
| principal_2021_2025 | sutil | interanual | 90 | shock | iid | GC3 | 10,211.615 | 8 | 1,533.800 | 16,657.022 | no | 4 |
| principal_2021_2025 | sutil | interanual | 90 | shock | iid | GE | 11,299.378 | 9 | 3,132.745 | 17,233.604 | no | 4 |
| principal_2021_2025 | sutil | interanual | 90 | shock | bloques | Naive | 1,538.943 | 2 | -981.900 | 2,070.817 | sí | 4 |
| principal_2021_2025 | sutil | interanual | 90 | shock | bloques | Seasonal Naive | 15,258.750 | 10 | 10,746.501 | 16,867.314 | no | 4 |
| principal_2021_2025 | sutil | interanual | 90 | shock | bloques | Chronos | 1,116.204 | 1 | 0.000 | 0.000 | sí | 4 |
| principal_2021_2025 | sutil | interanual | 90 | shock | bloques | SARIMA | 3,725.435 | 3 | 1,722.092 | 3,294.135 | no | 4 |
| principal_2021_2025 | sutil | interanual | 90 | shock | bloques | SARIMA-sel | 5,506.388 | 6 | 2,270.739 | 6,509.629 | no | 4 |
| principal_2021_2025 | sutil | interanual | 90 | shock | bloques | Ridge | 4,169.104 | 4 | 187.593 | 6,387.512 | no | 4 |
| principal_2021_2025 | sutil | interanual | 90 | shock | bloques | ElasticNet | 4,817.704 | 5 | 248.083 | 7,629.157 | no | 4 |
| principal_2021_2025 | sutil | interanual | 90 | shock | bloques | XGB-37 | 5,555.691 | 7 | -553.494 | 10,058.817 | sí | 4 |
| principal_2021_2025 | sutil | interanual | 90 | shock | bloques | GC3 | 10,211.615 | 8 | 1,334.293 | 17,406.372 | no | 4 |
| principal_2021_2025 | sutil | interanual | 90 | shock | bloques | GE | 11,299.378 | 9 | 2,878.974 | 17,961.359 | no | 4 |
| principal_2021_2025 | sutil | interanual | 90 | normal | iid | Naive | 3,773.008 | 4 | 421.198 | 1,627.169 | no | 56 |
| principal_2021_2025 | sutil | interanual | 90 | normal | iid | Seasonal Naive | 5,418.896 | 8 | 1,790.880 | 3,479.271 | no | 56 |
| principal_2021_2025 | sutil | interanual | 90 | normal | iid | Chronos | 2,758.000 | 1 | 0.000 | 0.000 | sí | 56 |
| principal_2021_2025 | sutil | interanual | 90 | normal | iid | SARIMA | 3,334.741 | 3 | -8.331 | 1,142.716 | sí | 56 |
| principal_2021_2025 | sutil | interanual | 90 | normal | iid | SARIMA-sel | 3,041.554 | 2 | -332.786 | 888.363 | sí | 56 |
| principal_2021_2025 | sutil | interanual | 90 | normal | iid | Ridge | 4,979.138 | 7 | 1,050.864 | 3,508.324 | no | 56 |
| principal_2021_2025 | sutil | interanual | 90 | normal | iid | ElasticNet | 4,875.783 | 6 | 1,006.756 | 3,291.650 | no | 56 |
| principal_2021_2025 | sutil | interanual | 90 | normal | iid | XGB-37 | 4,833.290 | 5 | 1,216.223 | 2,920.737 | no | 56 |
| principal_2021_2025 | sutil | interanual | 90 | normal | iid | GC3 | 6,086.282 | 9 | 2,184.015 | 4,466.533 | no | 56 |
| principal_2021_2025 | sutil | interanual | 90 | normal | iid | GE | 6,418.112 | 10 | 2,425.986 | 4,880.931 | no | 56 |
| principal_2021_2025 | sutil | interanual | 90 | normal | bloques | Naive | 3,773.008 | 4 | 439.545 | 1,588.338 | no | 56 |
| principal_2021_2025 | sutil | interanual | 90 | normal | bloques | Seasonal Naive | 5,418.896 | 8 | 1,756.951 | 3,551.293 | no | 56 |
| principal_2021_2025 | sutil | interanual | 90 | normal | bloques | Chronos | 2,758.000 | 1 | 0.000 | 0.000 | sí | 56 |
| principal_2021_2025 | sutil | interanual | 90 | normal | bloques | SARIMA | 3,334.741 | 3 | 56.311 | 1,086.200 | no | 56 |
| principal_2021_2025 | sutil | interanual | 90 | normal | bloques | SARIMA-sel | 3,041.554 | 2 | -244.989 | 792.051 | sí | 56 |
| principal_2021_2025 | sutil | interanual | 90 | normal | bloques | Ridge | 4,979.138 | 7 | 845.720 | 3,638.051 | no | 56 |
| principal_2021_2025 | sutil | interanual | 90 | normal | bloques | ElasticNet | 4,875.783 | 6 | 810.422 | 3,444.112 | no | 56 |
| principal_2021_2025 | sutil | interanual | 90 | normal | bloques | XGB-37 | 4,833.290 | 5 | 1,107.054 | 3,047.128 | no | 56 |
| principal_2021_2025 | sutil | interanual | 90 | normal | bloques | GC3 | 6,086.282 | 9 | 1,950.669 | 4,809.672 | no | 56 |
| principal_2021_2025 | sutil | interanual | 90 | normal | bloques | GE | 6,418.112 | 10 | 2,052.952 | 5,305.848 | no | 56 |
| principal_2021_2025 | dulce | mensual | 50 | shock | iid | Naive | 117.017 | 10 | 87.556 | 117.346 | no | 28 |
| principal_2021_2025 | dulce | mensual | 50 | shock | iid | Seasonal Naive | 20.366 | 3 | 0.912 | 10.266 | no | 28 |
| principal_2021_2025 | dulce | mensual | 50 | shock | iid | Chronos | 39.460 | 4 | 15.735 | 33.548 | no | 28 |
| principal_2021_2025 | dulce | mensual | 50 | shock | iid | SARIMA | 14.631 | 1 | 0.000 | 0.000 | sí | 28 |
| principal_2021_2025 | dulce | mensual | 50 | shock | iid | SARIMA-sel | 17.553 | 2 | -1.168 | 5.791 | sí | 28 |
| principal_2021_2025 | dulce | mensual | 50 | shock | iid | Ridge | 57.746 | 9 | 27.913 | 59.458 | no | 28 |
| principal_2021_2025 | dulce | mensual | 50 | shock | iid | ElasticNet | 54.063 | 8 | 24.116 | 55.808 | no | 28 |
| principal_2021_2025 | dulce | mensual | 50 | shock | iid | XGB-37 | 47.689 | 5 | 19.724 | 46.818 | no | 28 |
| principal_2021_2025 | dulce | mensual | 50 | shock | iid | GC3 | 49.178 | 7 | 22.252 | 47.593 | no | 28 |
| principal_2021_2025 | dulce | mensual | 50 | shock | iid | GE | 47.768 | 6 | 20.958 | 46.084 | no | 28 |
| principal_2021_2025 | dulce | mensual | 50 | shock | bloques | Naive | 117.017 | 10 | 86.335 | 117.580 | no | 28 |
| principal_2021_2025 | dulce | mensual | 50 | shock | bloques | Seasonal Naive | 20.366 | 3 | 0.089 | 10.640 | no | 28 |
| principal_2021_2025 | dulce | mensual | 50 | shock | bloques | Chronos | 39.460 | 4 | 14.368 | 34.058 | no | 28 |
| principal_2021_2025 | dulce | mensual | 50 | shock | bloques | SARIMA | 14.631 | 1 | 0.000 | 0.000 | sí | 28 |
| principal_2021_2025 | dulce | mensual | 50 | shock | bloques | SARIMA-sel | 17.553 | 2 | -1.777 | 7.409 | sí | 28 |
| principal_2021_2025 | dulce | mensual | 50 | shock | bloques | Ridge | 57.746 | 9 | 26.684 | 60.877 | no | 28 |
| principal_2021_2025 | dulce | mensual | 50 | shock | bloques | ElasticNet | 54.063 | 8 | 22.671 | 57.251 | no | 28 |
| principal_2021_2025 | dulce | mensual | 50 | shock | bloques | XGB-37 | 47.689 | 5 | 17.227 | 47.041 | no | 28 |
| principal_2021_2025 | dulce | mensual | 50 | shock | bloques | GC3 | 49.178 | 7 | 19.697 | 50.173 | no | 28 |
| principal_2021_2025 | dulce | mensual | 50 | shock | bloques | GE | 47.768 | 6 | 19.859 | 46.886 | no | 28 |
| principal_2021_2025 | dulce | mensual | 50 | normal | iid | Naive | 42.965 | 5 | 12.275 | 30.051 | no | 32 |
| principal_2021_2025 | dulce | mensual | 50 | normal | iid | Seasonal Naive | 28.123 | 4 | 1.432 | 11.109 | no | 32 |
| principal_2021_2025 | dulce | mensual | 50 | normal | iid | Chronos | 23.258 | 2 | -5.696 | 8.237 | sí | 32 |
| principal_2021_2025 | dulce | mensual | 50 | normal | iid | SARIMA | 21.721 | 1 | 0.000 | 0.000 | sí | 32 |
| principal_2021_2025 | dulce | mensual | 50 | normal | iid | SARIMA-sel | 23.320 | 3 | -2.636 | 6.121 | sí | 32 |
| principal_2021_2025 | dulce | mensual | 50 | normal | iid | Ridge | 48.978 | 8 | 15.086 | 39.223 | no | 32 |
| principal_2021_2025 | dulce | mensual | 50 | normal | iid | ElasticNet | 46.910 | 6 | 13.012 | 36.859 | no | 32 |
| principal_2021_2025 | dulce | mensual | 50 | normal | iid | XGB-37 | 48.761 | 7 | 14.803 | 38.938 | no | 32 |
| principal_2021_2025 | dulce | mensual | 50 | normal | iid | GC3 | 63.224 | 9 | 26.367 | 56.441 | no | 32 |
| principal_2021_2025 | dulce | mensual | 50 | normal | iid | GE | 64.580 | 10 | 28.144 | 57.594 | no | 32 |
| principal_2021_2025 | dulce | mensual | 50 | normal | bloques | Naive | 42.965 | 5 | 13.509 | 28.337 | no | 32 |
| principal_2021_2025 | dulce | mensual | 50 | normal | bloques | Seasonal Naive | 28.123 | 4 | 0.668 | 12.249 | no | 32 |
| principal_2021_2025 | dulce | mensual | 50 | normal | bloques | Chronos | 23.258 | 2 | -5.046 | 7.646 | sí | 32 |
| principal_2021_2025 | dulce | mensual | 50 | normal | bloques | SARIMA | 21.721 | 1 | 0.000 | 0.000 | sí | 32 |
| principal_2021_2025 | dulce | mensual | 50 | normal | bloques | SARIMA-sel | 23.320 | 3 | -3.080 | 6.428 | sí | 32 |
| principal_2021_2025 | dulce | mensual | 50 | normal | bloques | Ridge | 48.978 | 8 | 13.516 | 40.787 | no | 32 |
| principal_2021_2025 | dulce | mensual | 50 | normal | bloques | ElasticNet | 46.910 | 6 | 11.561 | 38.656 | no | 32 |
| principal_2021_2025 | dulce | mensual | 50 | normal | bloques | XGB-37 | 48.761 | 7 | 12.061 | 41.950 | no | 32 |
| principal_2021_2025 | dulce | mensual | 50 | normal | bloques | GC3 | 63.224 | 9 | 20.282 | 63.646 | no | 32 |
| principal_2021_2025 | dulce | mensual | 50 | normal | bloques | GE | 64.580 | 10 | 22.632 | 63.630 | no | 32 |
| principal_2021_2025 | dulce | mensual | 60 | shock | iid | Naive | 125.066 | 10 | 96.304 | 125.854 | no | 23 |
| principal_2021_2025 | dulce | mensual | 60 | shock | iid | Seasonal Naive | 21.908 | 3 | 3.803 | 11.984 | no | 23 |
| principal_2021_2025 | dulce | mensual | 60 | shock | iid | Chronos | 41.940 | 4 | 19.256 | 36.554 | no | 23 |
| principal_2021_2025 | dulce | mensual | 60 | shock | iid | SARIMA | 13.893 | 1 | 0.000 | 0.000 | sí | 23 |
| principal_2021_2025 | dulce | mensual | 60 | shock | iid | SARIMA-sel | 16.184 | 2 | -2.442 | 5.435 | sí | 23 |
| principal_2021_2025 | dulce | mensual | 60 | shock | iid | Ridge | 56.904 | 9 | 28.704 | 58.506 | no | 23 |
| principal_2021_2025 | dulce | mensual | 60 | shock | iid | ElasticNet | 54.053 | 8 | 25.706 | 56.059 | no | 23 |
| principal_2021_2025 | dulce | mensual | 60 | shock | iid | XGB-37 | 53.115 | 6 | 24.957 | 53.913 | no | 23 |
| principal_2021_2025 | dulce | mensual | 60 | shock | iid | GC3 | 53.247 | 7 | 26.634 | 52.827 | no | 23 |
| principal_2021_2025 | dulce | mensual | 60 | shock | iid | GE | 50.460 | 5 | 23.855 | 50.344 | no | 23 |
| principal_2021_2025 | dulce | mensual | 60 | shock | bloques | Naive | 125.066 | 10 | 96.485 | 125.805 | no | 23 |
| principal_2021_2025 | dulce | mensual | 60 | shock | bloques | Seasonal Naive | 21.908 | 3 | 2.917 | 12.833 | no | 23 |
| principal_2021_2025 | dulce | mensual | 60 | shock | bloques | Chronos | 41.940 | 4 | 18.236 | 36.424 | no | 23 |
| principal_2021_2025 | dulce | mensual | 60 | shock | bloques | SARIMA | 13.893 | 1 | 0.000 | 0.000 | sí | 23 |
| principal_2021_2025 | dulce | mensual | 60 | shock | bloques | SARIMA-sel | 16.184 | 2 | -2.916 | 7.992 | sí | 23 |
| principal_2021_2025 | dulce | mensual | 60 | shock | bloques | Ridge | 56.904 | 9 | 27.641 | 59.694 | no | 23 |
| principal_2021_2025 | dulce | mensual | 60 | shock | bloques | ElasticNet | 54.053 | 8 | 23.960 | 56.695 | no | 23 |
| principal_2021_2025 | dulce | mensual | 60 | shock | bloques | XGB-37 | 53.115 | 6 | 22.845 | 52.891 | no | 23 |
| principal_2021_2025 | dulce | mensual | 60 | shock | bloques | GC3 | 53.247 | 7 | 23.764 | 55.659 | no | 23 |
| principal_2021_2025 | dulce | mensual | 60 | shock | bloques | GE | 50.460 | 5 | 22.166 | 51.049 | no | 23 |
| principal_2021_2025 | dulce | mensual | 60 | normal | iid | Naive | 47.968 | 7 | 17.175 | 36.207 | no | 37 |
| principal_2021_2025 | dulce | mensual | 60 | normal | iid | Seasonal Naive | 26.116 | 4 | -0.130 | 9.698 | sí | 37 |
| principal_2021_2025 | dulce | mensual | 60 | normal | iid | Chronos | 23.906 | 3 | -4.331 | 9.482 | sí | 37 |
| principal_2021_2025 | dulce | mensual | 60 | normal | iid | SARIMA | 21.221 | 1 | 0.000 | 0.000 | sí | 37 |
| principal_2021_2025 | dulce | mensual | 60 | normal | iid | SARIMA-sel | 23.392 | 2 | -1.828 | 6.127 | sí | 37 |
| principal_2021_2025 | dulce | mensual | 60 | normal | iid | Ridge | 50.687 | 8 | 16.890 | 42.462 | no | 37 |
| principal_2021_2025 | dulce | mensual | 60 | normal | iid | ElasticNet | 47.882 | 6 | 14.263 | 39.382 | no | 37 |
| principal_2021_2025 | dulce | mensual | 60 | normal | iid | XGB-37 | 45.243 | 5 | 12.682 | 35.421 | no | 37 |
| principal_2021_2025 | dulce | mensual | 60 | normal | iid | GC3 | 58.797 | 9 | 23.056 | 51.840 | no | 37 |
| principal_2021_2025 | dulce | mensual | 60 | normal | iid | GE | 60.635 | 10 | 25.231 | 53.313 | no | 37 |
| principal_2021_2025 | dulce | mensual | 60 | normal | bloques | Naive | 47.968 | 7 | 19.068 | 34.177 | no | 37 |
| principal_2021_2025 | dulce | mensual | 60 | normal | bloques | Seasonal Naive | 26.116 | 4 | -0.974 | 10.982 | sí | 37 |
| principal_2021_2025 | dulce | mensual | 60 | normal | bloques | Chronos | 23.906 | 3 | -4.348 | 9.307 | sí | 37 |
| principal_2021_2025 | dulce | mensual | 60 | normal | bloques | SARIMA | 21.221 | 1 | 0.000 | 0.000 | sí | 37 |
| principal_2021_2025 | dulce | mensual | 60 | normal | bloques | SARIMA-sel | 23.392 | 2 | -2.045 | 6.178 | sí | 37 |
| principal_2021_2025 | dulce | mensual | 60 | normal | bloques | Ridge | 50.687 | 8 | 14.565 | 44.224 | no | 37 |
| principal_2021_2025 | dulce | mensual | 60 | normal | bloques | ElasticNet | 47.882 | 6 | 11.813 | 41.147 | no | 37 |
| principal_2021_2025 | dulce | mensual | 60 | normal | bloques | XGB-37 | 45.243 | 5 | 9.794 | 38.998 | no | 37 |
| principal_2021_2025 | dulce | mensual | 60 | normal | bloques | GC3 | 58.797 | 9 | 18.506 | 59.165 | no | 37 |
| principal_2021_2025 | dulce | mensual | 60 | normal | bloques | GE | 60.635 | 10 | 20.924 | 59.805 | no | 37 |
| principal_2021_2025 | dulce | mensual | 75 | shock | iid | Naive | 131.622 | 10 | 103.014 | 133.375 | no | 15 |
| principal_2021_2025 | dulce | mensual | 75 | shock | iid | Seasonal Naive | 24.503 | 3 | 7.208 | 13.529 | no | 15 |
| principal_2021_2025 | dulce | mensual | 75 | shock | iid | Chronos | 48.199 | 4 | 24.855 | 42.693 | no | 15 |
| principal_2021_2025 | dulce | mensual | 75 | shock | iid | SARIMA | 13.978 | 1 | 0.000 | 0.000 | sí | 15 |
| principal_2021_2025 | dulce | mensual | 75 | shock | iid | SARIMA-sel | 19.691 | 2 | 4.475 | 7.129 | no | 15 |
| principal_2021_2025 | dulce | mensual | 75 | shock | iid | Ridge | 69.694 | 9 | 38.914 | 74.342 | no | 15 |
| principal_2021_2025 | dulce | mensual | 75 | shock | iid | ElasticNet | 67.230 | 8 | 35.768 | 72.471 | no | 15 |
| principal_2021_2025 | dulce | mensual | 75 | shock | iid | XGB-37 | 65.849 | 7 | 37.127 | 66.769 | no | 15 |
| principal_2021_2025 | dulce | mensual | 75 | shock | iid | GC3 | 60.748 | 6 | 32.452 | 61.866 | no | 15 |
| principal_2021_2025 | dulce | mensual | 75 | shock | iid | GE | 57.883 | 5 | 27.912 | 61.091 | no | 15 |
| principal_2021_2025 | dulce | mensual | 75 | shock | bloques | Naive | 131.622 | 10 | 103.367 | 132.108 | no | 15 |
| principal_2021_2025 | dulce | mensual | 75 | shock | bloques | Seasonal Naive | 24.503 | 3 | 4.753 | 14.778 | no | 15 |
| principal_2021_2025 | dulce | mensual | 75 | shock | bloques | Chronos | 48.199 | 4 | 22.975 | 43.282 | no | 15 |
| principal_2021_2025 | dulce | mensual | 75 | shock | bloques | SARIMA | 13.978 | 1 | 0.000 | 0.000 | sí | 15 |
| principal_2021_2025 | dulce | mensual | 75 | shock | bloques | SARIMA-sel | 19.691 | 2 | -0.851 | 13.776 | sí | 15 |
| principal_2021_2025 | dulce | mensual | 75 | shock | bloques | Ridge | 69.694 | 9 | 36.250 | 77.882 | no | 15 |
| principal_2021_2025 | dulce | mensual | 75 | shock | bloques | ElasticNet | 67.230 | 8 | 33.397 | 74.813 | no | 15 |
| principal_2021_2025 | dulce | mensual | 75 | shock | bloques | XGB-37 | 65.849 | 7 | 34.459 | 66.788 | no | 15 |
| principal_2021_2025 | dulce | mensual | 75 | shock | bloques | GC3 | 60.748 | 6 | 25.287 | 70.073 | no | 15 |
| principal_2021_2025 | dulce | mensual | 75 | shock | bloques | GE | 57.883 | 5 | 24.265 | 64.114 | no | 15 |
| principal_2021_2025 | dulce | mensual | 75 | normal | iid | Naive | 59.489 | 10 | 27.009 | 52.692 | no | 45 |
| principal_2021_2025 | dulce | mensual | 75 | normal | iid | Seasonal Naive | 24.503 | 3 | 0.390 | 8.703 | no | 45 |
| principal_2021_2025 | dulce | mensual | 75 | normal | iid | Chronos | 25.025 | 4 | -1.436 | 11.620 | sí | 45 |
| principal_2021_2025 | dulce | mensual | 75 | normal | iid | SARIMA | 19.890 | 1 | 0.000 | 0.000 | sí | 45 |
| principal_2021_2025 | dulce | mensual | 75 | normal | iid | SARIMA-sel | 20.941 | 2 | -2.590 | 4.735 | sí | 45 |
| principal_2021_2025 | dulce | mensual | 75 | normal | iid | Ridge | 47.528 | 7 | 16.960 | 38.274 | no | 45 |
| principal_2021_2025 | dulce | mensual | 75 | normal | iid | ElasticNet | 44.587 | 6 | 14.268 | 35.199 | no | 45 |
| principal_2021_2025 | dulce | mensual | 75 | normal | iid | XGB-37 | 42.398 | 5 | 12.559 | 33.130 | no | 45 |
| principal_2021_2025 | dulce | mensual | 75 | normal | iid | GC3 | 55.310 | 8 | 23.234 | 47.824 | no | 45 |
| principal_2021_2025 | dulce | mensual | 75 | normal | iid | GE | 56.352 | 9 | 24.656 | 48.370 | no | 45 |
| principal_2021_2025 | dulce | mensual | 75 | normal | bloques | Naive | 59.489 | 10 | 29.924 | 49.525 | no | 45 |
| principal_2021_2025 | dulce | mensual | 75 | normal | bloques | Seasonal Naive | 24.503 | 3 | -0.998 | 10.258 | sí | 45 |
| principal_2021_2025 | dulce | mensual | 75 | normal | bloques | Chronos | 25.025 | 4 | -1.466 | 11.567 | sí | 45 |
| principal_2021_2025 | dulce | mensual | 75 | normal | bloques | SARIMA | 19.890 | 1 | 0.000 | 0.000 | sí | 45 |
| principal_2021_2025 | dulce | mensual | 75 | normal | bloques | SARIMA-sel | 20.941 | 2 | -2.026 | 4.053 | sí | 45 |
| principal_2021_2025 | dulce | mensual | 75 | normal | bloques | Ridge | 47.528 | 7 | 15.064 | 41.164 | no | 45 |
| principal_2021_2025 | dulce | mensual | 75 | normal | bloques | ElasticNet | 44.587 | 6 | 12.362 | 37.959 | no | 45 |
| principal_2021_2025 | dulce | mensual | 75 | normal | bloques | XGB-37 | 42.398 | 5 | 10.479 | 35.801 | no | 45 |
| principal_2021_2025 | dulce | mensual | 75 | normal | bloques | GC3 | 55.310 | 8 | 18.422 | 54.340 | no | 45 |
| principal_2021_2025 | dulce | mensual | 75 | normal | bloques | GE | 56.352 | 9 | 20.289 | 54.575 | no | 45 |
| principal_2021_2025 | dulce | mensual | 90 | shock | iid | Naive | 110.728 | 10 | 78.443 | 127.149 | no | 5 |
| principal_2021_2025 | dulce | mensual | 90 | shock | iid | Seasonal Naive | 21.412 | 2 | 10.305 | 11.075 | no | 5 |
| principal_2021_2025 | dulce | mensual | 90 | shock | iid | Chronos | 38.023 | 4 | 17.072 | 39.886 | no | 5 |
| principal_2021_2025 | dulce | mensual | 90 | shock | iid | SARIMA | 10.715 | 1 | 0.000 | 0.000 | sí | 5 |
| principal_2021_2025 | dulce | mensual | 90 | shock | iid | SARIMA-sel | 29.101 | 3 | 15.109 | 22.872 | no | 5 |
| principal_2021_2025 | dulce | mensual | 90 | shock | iid | Ridge | 46.586 | 8 | 24.414 | 47.199 | no | 5 |
| principal_2021_2025 | dulce | mensual | 90 | shock | iid | ElasticNet | 45.876 | 7 | 27.543 | 44.784 | no | 5 |
| principal_2021_2025 | dulce | mensual | 90 | shock | iid | XGB-37 | 56.950 | 9 | 27.387 | 65.039 | no | 5 |
| principal_2021_2025 | dulce | mensual | 90 | shock | iid | GC3 | 39.424 | 5 | 18.802 | 39.993 | no | 5 |
| principal_2021_2025 | dulce | mensual | 90 | shock | iid | GE | 39.559 | 6 | 15.085 | 51.132 | no | 5 |
| principal_2021_2025 | dulce | mensual | 90 | shock | bloques | Naive | 110.728 | 10 | 74.539 | 133.258 | no | 5 |
| principal_2021_2025 | dulce | mensual | 90 | shock | bloques | Seasonal Naive | 21.412 | 2 | 2.359 | 16.115 | no | 5 |
| principal_2021_2025 | dulce | mensual | 90 | shock | bloques | Chronos | 38.023 | 4 | 17.580 | 39.734 | no | 5 |
| principal_2021_2025 | dulce | mensual | 90 | shock | bloques | SARIMA | 10.715 | 1 | 0.000 | 0.000 | sí | 5 |
| principal_2021_2025 | dulce | mensual | 90 | shock | bloques | SARIMA-sel | 29.101 | 3 | 0.000 | 32.435 | sí | 5 |
| principal_2021_2025 | dulce | mensual | 90 | shock | bloques | Ridge | 46.586 | 8 | 12.714 | 54.702 | no | 5 |
| principal_2021_2025 | dulce | mensual | 90 | shock | bloques | ElasticNet | 45.876 | 7 | 12.460 | 48.905 | no | 5 |
| principal_2021_2025 | dulce | mensual | 90 | shock | bloques | XGB-37 | 56.950 | 9 | 24.496 | 70.438 | no | 5 |
| principal_2021_2025 | dulce | mensual | 90 | shock | bloques | GC3 | 39.424 | 5 | 8.145 | 45.263 | no | 5 |
| principal_2021_2025 | dulce | mensual | 90 | shock | bloques | GE | 39.559 | 6 | 11.158 | 50.952 | no | 5 |
| principal_2021_2025 | dulce | mensual | 90 | normal | iid | Naive | 74.504 | 10 | 42.031 | 69.105 | no | 55 |
| principal_2021_2025 | dulce | mensual | 90 | normal | iid | Seasonal Naive | 24.784 | 3 | 1.891 | 9.226 | no | 55 |
| principal_2021_2025 | dulce | mensual | 90 | normal | iid | Chronos | 30.164 | 4 | 4.155 | 17.571 | no | 55 |
| principal_2021_2025 | dulce | mensual | 90 | normal | iid | SARIMA | 19.112 | 1 | 0.000 | 0.000 | sí | 55 |
| principal_2021_2025 | dulce | mensual | 90 | normal | iid | SARIMA-sel | 19.858 | 2 | -2.241 | 3.772 | sí | 55 |
| principal_2021_2025 | dulce | mensual | 90 | normal | iid | Ridge | 53.659 | 7 | 23.874 | 45.399 | no | 55 |
| principal_2021_2025 | dulce | mensual | 90 | normal | iid | ElasticNet | 50.645 | 6 | 20.864 | 42.382 | no | 55 |
| principal_2021_2025 | dulce | mensual | 90 | normal | iid | XGB-37 | 47.471 | 5 | 18.245 | 38.323 | no | 55 |
| principal_2021_2025 | dulce | mensual | 90 | normal | iid | GC3 | 58.237 | 8 | 27.934 | 50.096 | no | 55 |
| principal_2021_2025 | dulce | mensual | 90 | normal | iid | GE | 58.296 | 9 | 28.304 | 49.968 | no | 55 |
| principal_2021_2025 | dulce | mensual | 90 | normal | bloques | Naive | 74.504 | 10 | 42.965 | 68.310 | no | 55 |
| principal_2021_2025 | dulce | mensual | 90 | normal | bloques | Seasonal Naive | 24.784 | 3 | 1.038 | 10.163 | no | 55 |
| principal_2021_2025 | dulce | mensual | 90 | normal | bloques | Chronos | 30.164 | 4 | 3.193 | 18.652 | no | 55 |
| principal_2021_2025 | dulce | mensual | 90 | normal | bloques | SARIMA | 19.112 | 1 | 0.000 | 0.000 | sí | 55 |
| principal_2021_2025 | dulce | mensual | 90 | normal | bloques | SARIMA-sel | 19.858 | 2 | -1.778 | 3.176 | sí | 55 |
| principal_2021_2025 | dulce | mensual | 90 | normal | bloques | Ridge | 53.659 | 7 | 21.598 | 48.036 | no | 55 |
| principal_2021_2025 | dulce | mensual | 90 | normal | bloques | ElasticNet | 50.645 | 6 | 18.423 | 45.310 | no | 55 |
| principal_2021_2025 | dulce | mensual | 90 | normal | bloques | XGB-37 | 47.471 | 5 | 15.115 | 41.358 | no | 55 |
| principal_2021_2025 | dulce | mensual | 90 | normal | bloques | GC3 | 58.237 | 8 | 22.869 | 55.891 | no | 55 |
| principal_2021_2025 | dulce | mensual | 90 | normal | bloques | GE | 58.296 | 9 | 23.745 | 55.147 | no | 55 |
| principal_2021_2025 | dulce | interanual | 50 | shock | iid | Naive | 81.292 | 10 | 37.517 | 77.027 | no | 29 |
| principal_2021_2025 | dulce | interanual | 50 | shock | iid | Seasonal Naive | 37.605 | 4 | 8.657 | 17.687 | no | 29 |
| principal_2021_2025 | dulce | interanual | 50 | shock | iid | Chronos | 31.745 | 3 | -1.981 | 16.404 | sí | 29 |
| principal_2021_2025 | dulce | interanual | 50 | shock | iid | SARIMA | 24.212 | 1 | 0.000 | 0.000 | sí | 29 |
| principal_2021_2025 | dulce | interanual | 50 | shock | iid | SARIMA-sel | 24.851 | 2 | -3.783 | 4.971 | sí | 29 |
| principal_2021_2025 | dulce | interanual | 50 | shock | iid | Ridge | 64.909 | 8 | 26.439 | 54.977 | no | 29 |
| principal_2021_2025 | dulce | interanual | 50 | shock | iid | ElasticNet | 59.471 | 6 | 21.078 | 49.734 | no | 29 |
| principal_2021_2025 | dulce | interanual | 50 | shock | iid | XGB-37 | 53.069 | 5 | 14.521 | 43.087 | no | 29 |
| principal_2021_2025 | dulce | interanual | 50 | shock | iid | GC3 | 67.134 | 9 | 27.773 | 57.567 | no | 29 |
| principal_2021_2025 | dulce | interanual | 50 | shock | iid | GE | 64.902 | 7 | 25.801 | 55.095 | no | 29 |
| principal_2021_2025 | dulce | interanual | 50 | shock | bloques | Naive | 81.292 | 10 | 40.465 | 73.645 | no | 29 |
| principal_2021_2025 | dulce | interanual | 50 | shock | bloques | Seasonal Naive | 37.605 | 4 | 9.030 | 17.836 | no | 29 |
| principal_2021_2025 | dulce | interanual | 50 | shock | bloques | Chronos | 31.745 | 3 | -2.232 | 17.484 | sí | 29 |
| principal_2021_2025 | dulce | interanual | 50 | shock | bloques | SARIMA | 24.212 | 1 | 0.000 | 0.000 | sí | 29 |
| principal_2021_2025 | dulce | interanual | 50 | shock | bloques | SARIMA-sel | 24.851 | 2 | -3.243 | 5.026 | sí | 29 |
| principal_2021_2025 | dulce | interanual | 50 | shock | bloques | Ridge | 64.909 | 8 | 27.338 | 56.188 | no | 29 |
| principal_2021_2025 | dulce | interanual | 50 | shock | bloques | ElasticNet | 59.471 | 6 | 21.154 | 51.343 | no | 29 |
| principal_2021_2025 | dulce | interanual | 50 | shock | bloques | XGB-37 | 53.069 | 5 | 12.119 | 45.478 | no | 29 |
| principal_2021_2025 | dulce | interanual | 50 | shock | bloques | GC3 | 67.134 | 9 | 24.540 | 62.480 | no | 29 |
| principal_2021_2025 | dulce | interanual | 50 | shock | bloques | GE | 64.902 | 7 | 23.541 | 59.345 | no | 29 |
| principal_2021_2025 | dulce | interanual | 50 | normal | iid | Naive | 73.995 | 10 | 45.229 | 79.191 | no | 31 |
| principal_2021_2025 | dulce | interanual | 50 | normal | iid | Seasonal Naive | 12.246 | 1 | 0.000 | 0.000 | sí | 31 |
| principal_2021_2025 | dulce | interanual | 50 | normal | iid | Chronos | 29.952 | 4 | 11.080 | 24.635 | no | 31 |
| principal_2021_2025 | dulce | interanual | 50 | normal | iid | SARIMA | 12.986 | 2 | -3.746 | 5.475 | sí | 31 |
| principal_2021_2025 | dulce | interanual | 50 | normal | iid | SARIMA-sel | 16.679 | 3 | -0.851 | 9.615 | sí | 31 |
| principal_2021_2025 | dulce | interanual | 50 | normal | iid | Ridge | 41.994 | 6 | 18.174 | 43.208 | no | 31 |
| principal_2021_2025 | dulce | interanual | 50 | normal | iid | ElasticNet | 41.620 | 5 | 18.234 | 42.167 | no | 31 |
| principal_2021_2025 | dulce | interanual | 50 | normal | iid | XGB-37 | 43.762 | 7 | 22.295 | 41.055 | no | 31 |
| principal_2021_2025 | dulce | interanual | 50 | normal | iid | GC3 | 46.880 | 8 | 24.902 | 45.510 | no | 31 |
| principal_2021_2025 | dulce | interanual | 50 | normal | iid | GE | 49.094 | 9 | 27.475 | 47.332 | no | 31 |
| principal_2021_2025 | dulce | interanual | 50 | normal | bloques | Naive | 73.995 | 10 | 46.545 | 77.650 | no | 31 |
| principal_2021_2025 | dulce | interanual | 50 | normal | bloques | Seasonal Naive | 12.246 | 1 | 0.000 | 0.000 | sí | 31 |
| principal_2021_2025 | dulce | interanual | 50 | normal | bloques | Chronos | 29.952 | 4 | 11.050 | 23.651 | no | 31 |
| principal_2021_2025 | dulce | interanual | 50 | normal | bloques | SARIMA | 12.986 | 2 | -4.367 | 5.989 | sí | 31 |
| principal_2021_2025 | dulce | interanual | 50 | normal | bloques | SARIMA-sel | 16.679 | 3 | -1.107 | 10.235 | sí | 31 |
| principal_2021_2025 | dulce | interanual | 50 | normal | bloques | Ridge | 41.994 | 6 | 17.755 | 43.419 | no | 31 |
| principal_2021_2025 | dulce | interanual | 50 | normal | bloques | ElasticNet | 41.620 | 5 | 17.847 | 42.501 | no | 31 |
| principal_2021_2025 | dulce | interanual | 50 | normal | bloques | XGB-37 | 43.762 | 7 | 21.834 | 41.592 | no | 31 |
| principal_2021_2025 | dulce | interanual | 50 | normal | bloques | GC3 | 46.880 | 8 | 23.007 | 48.289 | no | 31 |
| principal_2021_2025 | dulce | interanual | 50 | normal | bloques | GE | 49.094 | 9 | 25.747 | 49.695 | no | 31 |
| principal_2021_2025 | dulce | interanual | 60 | shock | iid | Naive | 78.514 | 10 | 29.132 | 74.452 | no | 23 |
| principal_2021_2025 | dulce | interanual | 60 | shock | iid | Seasonal Naive | 40.061 | 4 | 7.231 | 19.426 | no | 23 |
| principal_2021_2025 | dulce | interanual | 60 | shock | iid | Chronos | 30.371 | 3 | -6.740 | 13.792 | sí | 23 |
| principal_2021_2025 | dulce | interanual | 60 | shock | iid | SARIMA | 27.152 | 2 | -4.238 | 4.061 | sí | 23 |
| principal_2021_2025 | dulce | interanual | 60 | shock | iid | SARIMA-sel | 26.385 | 1 | 0.000 | 0.000 | sí | 23 |
| principal_2021_2025 | dulce | interanual | 60 | shock | iid | Ridge | 66.540 | 9 | 23.483 | 56.630 | no | 23 |
| principal_2021_2025 | dulce | interanual | 60 | shock | iid | ElasticNet | 59.820 | 6 | 16.701 | 50.356 | no | 23 |
| principal_2021_2025 | dulce | interanual | 60 | shock | iid | XGB-37 | 50.745 | 5 | 8.849 | 40.271 | no | 23 |
| principal_2021_2025 | dulce | interanual | 60 | shock | iid | GC3 | 65.344 | 8 | 22.366 | 55.323 | no | 23 |
| principal_2021_2025 | dulce | interanual | 60 | shock | iid | GE | 62.704 | 7 | 20.376 | 52.095 | no | 23 |
| principal_2021_2025 | dulce | interanual | 60 | shock | bloques | Naive | 78.514 | 10 | 34.965 | 69.950 | no | 23 |
| principal_2021_2025 | dulce | interanual | 60 | shock | bloques | Seasonal Naive | 40.061 | 4 | 7.927 | 19.756 | no | 23 |
| principal_2021_2025 | dulce | interanual | 60 | shock | bloques | Chronos | 30.371 | 3 | -5.444 | 14.694 | sí | 23 |
| principal_2021_2025 | dulce | interanual | 60 | shock | bloques | SARIMA | 27.152 | 2 | -2.511 | 3.929 | sí | 23 |
| principal_2021_2025 | dulce | interanual | 60 | shock | bloques | SARIMA-sel | 26.385 | 1 | 0.000 | 0.000 | sí | 23 |
| principal_2021_2025 | dulce | interanual | 60 | shock | bloques | Ridge | 66.540 | 9 | 24.503 | 59.572 | no | 23 |
| principal_2021_2025 | dulce | interanual | 60 | shock | bloques | ElasticNet | 59.820 | 6 | 17.578 | 53.427 | no | 23 |
| principal_2021_2025 | dulce | interanual | 60 | shock | bloques | XGB-37 | 50.745 | 5 | 7.067 | 44.110 | no | 23 |
| principal_2021_2025 | dulce | interanual | 60 | shock | bloques | GC3 | 65.344 | 8 | 21.115 | 60.187 | no | 23 |
| principal_2021_2025 | dulce | interanual | 60 | shock | bloques | GE | 62.704 | 7 | 20.030 | 55.505 | no | 23 |
| principal_2021_2025 | dulce | interanual | 60 | normal | iid | Naive | 76.906 | 10 | 48.266 | 80.496 | no | 37 |
| principal_2021_2025 | dulce | interanual | 60 | normal | iid | Seasonal Naive | 14.832 | 2 | -2.588 | 5.983 | sí | 37 |
| principal_2021_2025 | dulce | interanual | 60 | normal | iid | Chronos | 31.097 | 4 | 11.160 | 25.155 | no | 37 |
| principal_2021_2025 | dulce | interanual | 60 | normal | iid | SARIMA | 12.979 | 1 | 0.000 | 0.000 | sí | 37 |
| principal_2021_2025 | dulce | interanual | 60 | normal | iid | SARIMA-sel | 17.050 | 3 | 0.508 | 7.422 | no | 37 |
| principal_2021_2025 | dulce | interanual | 60 | normal | iid | Ridge | 44.697 | 6 | 19.872 | 44.898 | no | 37 |
| principal_2021_2025 | dulce | interanual | 60 | normal | iid | ElasticNet | 44.298 | 5 | 19.555 | 44.138 | no | 37 |
| principal_2021_2025 | dulce | interanual | 60 | normal | iid | XGB-37 | 46.716 | 7 | 22.443 | 45.393 | no | 37 |
| principal_2021_2025 | dulce | interanual | 60 | normal | iid | GC3 | 51.277 | 8 | 24.987 | 51.708 | no | 37 |
| principal_2021_2025 | dulce | interanual | 60 | normal | iid | GE | 53.024 | 9 | 27.055 | 53.168 | no | 37 |
| principal_2021_2025 | dulce | interanual | 60 | normal | bloques | Naive | 76.906 | 10 | 48.605 | 79.991 | no | 37 |
| principal_2021_2025 | dulce | interanual | 60 | normal | bloques | Seasonal Naive | 14.832 | 2 | -3.470 | 6.858 | sí | 37 |
| principal_2021_2025 | dulce | interanual | 60 | normal | bloques | Chronos | 31.097 | 4 | 10.748 | 24.960 | no | 37 |
| principal_2021_2025 | dulce | interanual | 60 | normal | bloques | SARIMA | 12.979 | 1 | 0.000 | 0.000 | sí | 37 |
| principal_2021_2025 | dulce | interanual | 60 | normal | bloques | SARIMA-sel | 17.050 | 3 | 0.940 | 7.279 | no | 37 |
| principal_2021_2025 | dulce | interanual | 60 | normal | bloques | Ridge | 44.697 | 6 | 17.878 | 46.119 | no | 37 |
| principal_2021_2025 | dulce | interanual | 60 | normal | bloques | ElasticNet | 44.298 | 5 | 17.694 | 45.457 | no | 37 |
| principal_2021_2025 | dulce | interanual | 60 | normal | bloques | XGB-37 | 46.716 | 7 | 21.009 | 46.278 | no | 37 |
| principal_2021_2025 | dulce | interanual | 60 | normal | bloques | GC3 | 51.277 | 8 | 21.857 | 55.571 | no | 37 |
| principal_2021_2025 | dulce | interanual | 60 | normal | bloques | GE | 53.024 | 9 | 24.152 | 56.658 | no | 37 |
| principal_2021_2025 | dulce | interanual | 75 | shock | iid | Naive | 83.176 | 10 | 28.493 | 83.352 | no | 16 |
| principal_2021_2025 | dulce | interanual | 75 | shock | iid | Seasonal Naive | 42.393 | 5 | 7.276 | 21.992 | no | 16 |
| principal_2021_2025 | dulce | interanual | 75 | shock | iid | Chronos | 33.195 | 3 | -6.945 | 18.002 | sí | 16 |
| principal_2021_2025 | dulce | interanual | 75 | shock | iid | SARIMA | 27.391 | 1 | 0.000 | 0.000 | sí | 16 |
| principal_2021_2025 | dulce | interanual | 75 | shock | iid | SARIMA-sel | 28.377 | 2 | -3.614 | 5.678 | sí | 16 |
| principal_2021_2025 | dulce | interanual | 75 | shock | iid | Ridge | 66.417 | 9 | 20.658 | 57.661 | no | 16 |
| principal_2021_2025 | dulce | interanual | 75 | shock | iid | ElasticNet | 57.322 | 7 | 11.355 | 49.479 | no | 16 |
| principal_2021_2025 | dulce | interanual | 75 | shock | iid | XGB-37 | 42.312 | 4 | 0.509 | 29.584 | no | 16 |
| principal_2021_2025 | dulce | interanual | 75 | shock | iid | GC3 | 58.191 | 8 | 14.004 | 47.185 | no | 16 |
| principal_2021_2025 | dulce | interanual | 75 | shock | iid | GE | 56.062 | 6 | 12.084 | 44.763 | no | 16 |
| principal_2021_2025 | dulce | interanual | 75 | shock | bloques | Naive | 83.176 | 10 | 36.143 | 80.736 | no | 16 |
| principal_2021_2025 | dulce | interanual | 75 | shock | bloques | Seasonal Naive | 42.393 | 5 | 8.818 | 22.467 | no | 16 |
| principal_2021_2025 | dulce | interanual | 75 | shock | bloques | Chronos | 33.195 | 3 | -5.212 | 21.355 | sí | 16 |
| principal_2021_2025 | dulce | interanual | 75 | shock | bloques | SARIMA | 27.391 | 1 | 0.000 | 0.000 | sí | 16 |
| principal_2021_2025 | dulce | interanual | 75 | shock | bloques | SARIMA-sel | 28.377 | 2 | -2.363 | 4.566 | sí | 16 |
| principal_2021_2025 | dulce | interanual | 75 | shock | bloques | Ridge | 66.417 | 9 | 23.437 | 64.218 | no | 16 |
| principal_2021_2025 | dulce | interanual | 75 | shock | bloques | ElasticNet | 57.322 | 7 | 15.189 | 55.326 | no | 16 |
| principal_2021_2025 | dulce | interanual | 75 | shock | bloques | XGB-37 | 42.312 | 4 | 1.194 | 35.256 | no | 16 |
| principal_2021_2025 | dulce | interanual | 75 | shock | bloques | GC3 | 58.191 | 8 | 15.388 | 51.176 | no | 16 |
| principal_2021_2025 | dulce | interanual | 75 | shock | bloques | GE | 56.062 | 6 | 14.979 | 47.275 | no | 16 |
| principal_2021_2025 | dulce | interanual | 75 | normal | iid | Naive | 75.467 | 10 | 45.643 | 75.411 | no | 44 |
| principal_2021_2025 | dulce | interanual | 75 | normal | iid | Seasonal Naive | 17.998 | 3 | -1.115 | 6.470 | sí | 44 |
| principal_2021_2025 | dulce | interanual | 75 | normal | iid | Chronos | 29.955 | 4 | 8.123 | 21.551 | no | 44 |
| principal_2021_2025 | dulce | interanual | 75 | normal | iid | SARIMA | 15.147 | 1 | 0.000 | 0.000 | sí | 44 |
| principal_2021_2025 | dulce | interanual | 75 | normal | iid | SARIMA-sel | 17.811 | 2 | -0.908 | 6.084 | sí | 44 |
| principal_2021_2025 | dulce | interanual | 75 | normal | iid | Ridge | 48.216 | 6 | 22.428 | 44.059 | no | 44 |
| principal_2021_2025 | dulce | interanual | 75 | normal | iid | ElasticNet | 47.676 | 5 | 22.139 | 43.262 | no | 44 |
| principal_2021_2025 | dulce | interanual | 75 | normal | iid | XGB-37 | 50.424 | 7 | 25.125 | 45.565 | no | 44 |
| principal_2021_2025 | dulce | interanual | 75 | normal | iid | GC3 | 56.116 | 8 | 28.883 | 52.859 | no | 44 |
| principal_2021_2025 | dulce | interanual | 75 | normal | iid | GE | 56.979 | 9 | 29.883 | 53.780 | no | 44 |
| principal_2021_2025 | dulce | interanual | 75 | normal | bloques | Naive | 75.467 | 10 | 44.916 | 76.250 | no | 44 |
| principal_2021_2025 | dulce | interanual | 75 | normal | bloques | Seasonal Naive | 17.998 | 3 | -2.315 | 7.488 | sí | 44 |
| principal_2021_2025 | dulce | interanual | 75 | normal | bloques | Chronos | 29.955 | 4 | 7.356 | 21.702 | no | 44 |
| principal_2021_2025 | dulce | interanual | 75 | normal | bloques | SARIMA | 15.147 | 1 | 0.000 | 0.000 | sí | 44 |
| principal_2021_2025 | dulce | interanual | 75 | normal | bloques | SARIMA-sel | 17.811 | 2 | -0.587 | 5.820 | sí | 44 |
| principal_2021_2025 | dulce | interanual | 75 | normal | bloques | Ridge | 48.216 | 6 | 19.238 | 46.195 | no | 44 |
| principal_2021_2025 | dulce | interanual | 75 | normal | bloques | ElasticNet | 47.676 | 5 | 19.085 | 45.234 | no | 44 |
| principal_2021_2025 | dulce | interanual | 75 | normal | bloques | XGB-37 | 50.424 | 7 | 21.971 | 47.607 | no | 44 |
| principal_2021_2025 | dulce | interanual | 75 | normal | bloques | GC3 | 56.116 | 8 | 22.556 | 58.880 | no | 44 |
| principal_2021_2025 | dulce | interanual | 75 | normal | bloques | GE | 56.979 | 9 | 24.682 | 58.486 | no | 44 |
| principal_2021_2025 | dulce | interanual | 90 | shock | iid | Naive | 60.260 | 8 | -1.010 | 58.034 | sí | 4 |
| principal_2021_2025 | dulce | interanual | 90 | shock | iid | Seasonal Naive | 68.645 | 10 | 28.628 | 45.166 | no | 4 |
| principal_2021_2025 | dulce | interanual | 90 | shock | iid | Chronos | 31.748 | 1 | 0.000 | 0.000 | sí | 4 |
| principal_2021_2025 | dulce | interanual | 90 | shock | iid | SARIMA | 59.264 | 6 | 17.072 | 37.960 | no | 4 |
| principal_2021_2025 | dulce | interanual | 90 | shock | iid | SARIMA-sel | 53.607 | 4 | 11.854 | 31.865 | no | 4 |
| principal_2021_2025 | dulce | interanual | 90 | shock | iid | Ridge | 56.546 | 5 | 17.962 | 31.635 | no | 4 |
| principal_2021_2025 | dulce | interanual | 90 | shock | iid | ElasticNet | 49.410 | 3 | 10.375 | 24.950 | no | 4 |
| principal_2021_2025 | dulce | interanual | 90 | shock | iid | XGB-37 | 43.591 | 2 | -5.579 | 29.265 | sí | 4 |
| principal_2021_2025 | dulce | interanual | 90 | shock | iid | GC3 | 67.527 | 9 | 31.996 | 39.562 | no | 4 |
| principal_2021_2025 | dulce | interanual | 90 | shock | iid | GE | 59.397 | 7 | 23.953 | 31.345 | no | 4 |
| principal_2021_2025 | dulce | interanual | 90 | shock | bloques | Naive | 60.260 | 8 | -12.630 | 69.654 | sí | 4 |
| principal_2021_2025 | dulce | interanual | 90 | shock | bloques | Seasonal Naive | 68.645 | 10 | 24.641 | 49.153 | no | 4 |
| principal_2021_2025 | dulce | interanual | 90 | shock | bloques | Chronos | 31.748 | 1 | 0.000 | 0.000 | sí | 4 |
| principal_2021_2025 | dulce | interanual | 90 | shock | bloques | SARIMA | 59.264 | 6 | 1.823 | 65.556 | no | 4 |
| principal_2021_2025 | dulce | interanual | 90 | shock | bloques | SARIMA-sel | 53.607 | 4 | -3.106 | 68.393 | sí | 4 |
| principal_2021_2025 | dulce | interanual | 90 | shock | bloques | Ridge | 56.546 | 5 | 0.649 | 41.964 | no | 4 |
| principal_2021_2025 | dulce | interanual | 90 | shock | bloques | ElasticNet | 49.410 | 3 | -4.399 | 31.796 | sí | 4 |
| principal_2021_2025 | dulce | interanual | 90 | shock | bloques | XGB-37 | 43.591 | 2 | -6.535 | 32.252 | sí | 4 |
| principal_2021_2025 | dulce | interanual | 90 | shock | bloques | GC3 | 67.527 | 9 | 26.493 | 41.990 | no | 4 |
| principal_2021_2025 | dulce | interanual | 90 | shock | bloques | GE | 59.397 | 7 | 20.463 | 34.834 | no | 4 |
| principal_2021_2025 | dulce | interanual | 90 | normal | iid | Naive | 78.755 | 10 | 50.492 | 76.627 | no | 56 |
| principal_2021_2025 | dulce | interanual | 90 | normal | iid | Seasonal Naive | 21.350 | 3 | 2.335 | 9.156 | no | 56 |
| principal_2021_2025 | dulce | interanual | 90 | normal | iid | Chronos | 30.752 | 4 | 9.444 | 21.123 | no | 56 |
| principal_2021_2025 | dulce | interanual | 90 | normal | iid | SARIMA | 15.494 | 1 | 0.000 | 0.000 | sí | 56 |
| principal_2021_2025 | dulce | interanual | 90 | normal | iid | SARIMA-sel | 18.273 | 2 | -0.181 | 5.547 | sí | 56 |
| principal_2021_2025 | dulce | interanual | 90 | normal | iid | Ridge | 52.821 | 7 | 27.780 | 47.390 | no | 56 |
| principal_2021_2025 | dulce | interanual | 90 | normal | iid | ElasticNet | 50.308 | 6 | 25.380 | 44.631 | no | 56 |
| principal_2021_2025 | dulce | interanual | 90 | normal | iid | XGB-37 | 48.594 | 5 | 23.961 | 42.404 | no | 56 |
| principal_2021_2025 | dulce | interanual | 90 | normal | iid | GC3 | 55.894 | 8 | 30.225 | 50.530 | no | 56 |
| principal_2021_2025 | dulce | interanual | 90 | normal | iid | GE | 56.544 | 9 | 31.159 | 51.074 | no | 56 |
| principal_2021_2025 | dulce | interanual | 90 | normal | bloques | Naive | 78.755 | 10 | 50.544 | 76.743 | no | 56 |
| principal_2021_2025 | dulce | interanual | 90 | normal | bloques | Seasonal Naive | 21.350 | 3 | 1.548 | 9.934 | no | 56 |
| principal_2021_2025 | dulce | interanual | 90 | normal | bloques | Chronos | 30.752 | 4 | 8.868 | 21.488 | no | 56 |
| principal_2021_2025 | dulce | interanual | 90 | normal | bloques | SARIMA | 15.494 | 1 | 0.000 | 0.000 | sí | 56 |
| principal_2021_2025 | dulce | interanual | 90 | normal | bloques | SARIMA-sel | 18.273 | 2 | -0.140 | 5.376 | sí | 56 |
| principal_2021_2025 | dulce | interanual | 90 | normal | bloques | Ridge | 52.821 | 7 | 26.140 | 48.799 | no | 56 |
| principal_2021_2025 | dulce | interanual | 90 | normal | bloques | ElasticNet | 50.308 | 6 | 23.497 | 46.487 | no | 56 |
| principal_2021_2025 | dulce | interanual | 90 | normal | bloques | XGB-37 | 48.594 | 5 | 21.829 | 43.784 | no | 56 |
| principal_2021_2025 | dulce | interanual | 90 | normal | bloques | GC3 | 55.894 | 8 | 25.003 | 55.688 | no | 56 |
| principal_2021_2025 | dulce | interanual | 90 | normal | bloques | GE | 56.544 | 9 | 26.558 | 55.350 | no | 56 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | shock | iid | Naive | 6,216.390 | 5 | 1,409.393 | 3,819.519 | no | 20 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | shock | iid | Seasonal Naive | 6,928.831 | 6 | 1,789.582 | 4,928.738 | no | 20 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | shock | iid | Chronos | 3,634.064 | 2 | -1,017.190 | 1,147.625 | sí | 20 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | shock | iid | SARIMA | 3,733.412 | 3 | -895.248 | 1,108.676 | sí | 20 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | shock | iid | SARIMA-sel | 3,586.352 | 1 | 0.000 | 0.000 | sí | 20 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | shock | iid | Ridge | 8,638.746 | 9 | 2,051.530 | 8,281.935 | no | 20 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | shock | iid | ElasticNet | 8,639.917 | 10 | 2,314.027 | 7,945.439 | no | 20 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | shock | iid | XGB-37 | 5,099.000 | 4 | 202.416 | 2,774.086 | no | 20 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | shock | iid | GC3 | 6,994.288 | 8 | 1,911.035 | 4,951.729 | no | 20 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | shock | iid | GE | 6,943.305 | 7 | 1,880.022 | 4,896.684 | no | 20 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | shock | bloques | Naive | 6,216.390 | 5 | 1,205.578 | 4,126.371 | no | 20 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | shock | bloques | Seasonal Naive | 6,928.831 | 6 | 1,477.550 | 5,124.719 | no | 20 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | shock | bloques | Chronos | 3,634.064 | 2 | -1,136.787 | 1,117.169 | sí | 20 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | shock | bloques | SARIMA | 3,733.412 | 3 | -773.743 | 1,075.500 | sí | 20 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | shock | bloques | SARIMA-sel | 3,586.352 | 1 | 0.000 | 0.000 | sí | 20 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | shock | bloques | Ridge | 8,638.746 | 9 | 1,752.372 | 8,782.205 | no | 20 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | shock | bloques | ElasticNet | 8,639.917 | 10 | 2,018.937 | 8,371.551 | no | 20 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | shock | bloques | XGB-37 | 5,099.000 | 4 | 173.040 | 2,801.125 | no | 20 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | shock | bloques | GC3 | 6,994.288 | 8 | 1,650.252 | 5,159.593 | no | 20 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | shock | bloques | GE | 6,943.305 | 7 | 1,549.839 | 5,147.379 | no | 20 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | normal | iid | Naive | 1,508.571 | 1 | 0.000 | 0.000 | sí | 16 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | normal | iid | Seasonal Naive | 7,574.741 | 8 | 3,785.777 | 8,205.456 | no | 16 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | normal | iid | Chronos | 1,830.050 | 2 | -524.590 | 1,102.784 | sí | 16 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | normal | iid | SARIMA | 3,234.627 | 5 | 636.194 | 2,783.134 | no | 16 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | normal | iid | SARIMA-sel | 3,853.672 | 6 | 1,148.513 | 3,586.341 | no | 16 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | normal | iid | Ridge | 2,949.769 | 3 | 260.456 | 2,782.655 | no | 16 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | normal | iid | ElasticNet | 2,989.581 | 4 | 199.087 | 2,981.562 | no | 16 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | normal | iid | XGB-37 | 4,609.566 | 7 | 1,503.878 | 4,912.423 | no | 16 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | normal | iid | GC3 | 8,348.593 | 9 | 4,268.099 | 9,721.424 | no | 16 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | normal | iid | GE | 9,764.061 | 10 | 5,545.401 | 11,184.371 | no | 16 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | normal | bloques | Naive | 1,508.571 | 1 | 0.000 | 0.000 | sí | 16 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | normal | bloques | Seasonal Naive | 7,574.741 | 8 | 3,052.259 | 9,516.159 | no | 16 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | normal | bloques | Chronos | 1,830.050 | 2 | -492.294 | 1,117.517 | sí | 16 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | normal | bloques | SARIMA | 3,234.627 | 5 | 533.261 | 2,829.990 | no | 16 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | normal | bloques | SARIMA-sel | 3,853.672 | 6 | 1,342.966 | 3,324.724 | no | 16 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | normal | bloques | Ridge | 2,949.769 | 3 | 83.498 | 3,177.390 | no | 16 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | normal | bloques | ElasticNet | 2,989.581 | 4 | -5.105 | 3,709.922 | sí | 16 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | normal | bloques | XGB-37 | 4,609.566 | 7 | 944.291 | 5,485.584 | no | 16 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | normal | bloques | GC3 | 8,348.593 | 9 | 3,101.580 | 11,136.639 | no | 16 |
| sensibilidad_2023_2025 | sutil | mensual | 50 | normal | bloques | GE | 9,764.061 | 10 | 4,119.608 | 12,601.891 | no | 16 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | shock | iid | Naive | 6,402.303 | 5 | 2,045.490 | 3,520.093 | no | 19 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | shock | iid | Seasonal Naive | 6,925.634 | 6 | 1,379.563 | 5,209.918 | no | 19 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | shock | iid | Chronos | 3,815.775 | 3 | -666.736 | 1,186.066 | sí | 19 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | shock | iid | SARIMA | 3,635.684 | 1 | 0.000 | 0.000 | sí | 19 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | shock | iid | SARIMA-sel | 3,642.783 | 2 | -988.728 | 1,081.837 | sí | 19 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | shock | iid | Ridge | 8,616.338 | 10 | 2,243.329 | 8,019.977 | no | 19 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | shock | iid | ElasticNet | 8,548.545 | 9 | 2,398.072 | 7,655.676 | no | 19 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | shock | iid | XGB-37 | 5,208.669 | 4 | -64.708 | 3,052.671 | sí | 19 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | shock | iid | GC3 | 6,950.723 | 7 | 1,360.377 | 5,181.734 | no | 19 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | shock | iid | GE | 6,985.460 | 8 | 1,511.584 | 5,068.385 | no | 19 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | shock | bloques | Naive | 6,402.303 | 5 | 1,948.940 | 3,558.894 | no | 19 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | shock | bloques | Seasonal Naive | 6,925.634 | 6 | 971.884 | 5,569.175 | no | 19 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | shock | bloques | Chronos | 3,815.775 | 3 | -782.269 | 1,286.969 | sí | 19 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | shock | bloques | SARIMA | 3,635.684 | 1 | 0.000 | 0.000 | sí | 19 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | shock | bloques | SARIMA-sel | 3,642.783 | 2 | -1,030.916 | 1,106.313 | sí | 19 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | shock | bloques | Ridge | 8,616.338 | 10 | 1,758.393 | 8,545.795 | no | 19 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | shock | bloques | ElasticNet | 8,548.545 | 9 | 1,930.361 | 8,087.613 | no | 19 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | shock | bloques | XGB-37 | 5,208.669 | 4 | -103.941 | 3,247.976 | sí | 19 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | shock | bloques | GC3 | 6,950.723 | 7 | 1,218.416 | 5,628.451 | no | 19 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | shock | bloques | GE | 6,985.460 | 8 | 1,334.499 | 5,581.729 | no | 19 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | normal | iid | Naive | 1,577.717 | 1 | 0.000 | 0.000 | sí | 17 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | normal | iid | Seasonal Naive | 7,540.320 | 8 | 3,762.926 | 8,040.187 | no | 17 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | normal | iid | Chronos | 1,733.080 | 2 | -669.465 | 923.263 | sí | 17 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | normal | iid | SARIMA | 3,373.193 | 4 | 753.848 | 2,783.973 | no | 17 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | normal | iid | SARIMA-sel | 3,774.877 | 6 | 1,020.932 | 3,394.197 | no | 17 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | normal | iid | Ridge | 3,309.459 | 3 | 526.007 | 3,089.501 | no | 17 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | normal | iid | ElasticNet | 3,424.075 | 5 | 518.032 | 3,353.887 | no | 17 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | normal | iid | XGB-37 | 4,515.785 | 7 | 1,438.809 | 4,629.652 | no | 17 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | normal | iid | GC3 | 8,317.618 | 9 | 4,276.517 | 9,456.876 | no | 17 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | normal | iid | GE | 9,551.020 | 10 | 5,416.432 | 10,755.696 | no | 17 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | normal | bloques | Naive | 1,577.717 | 1 | 0.000 | 0.000 | sí | 17 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | normal | bloques | Seasonal Naive | 7,540.320 | 8 | 3,140.868 | 9,214.499 | no | 17 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | normal | bloques | Chronos | 1,733.080 | 2 | -650.769 | 950.578 | sí | 17 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | normal | bloques | SARIMA | 3,373.193 | 4 | 654.903 | 2,835.407 | no | 17 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | normal | bloques | SARIMA-sel | 3,774.877 | 6 | 1,216.067 | 3,167.755 | no | 17 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | normal | bloques | Ridge | 3,309.459 | 3 | 323.157 | 3,432.598 | no | 17 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | normal | bloques | ElasticNet | 3,424.075 | 5 | 218.189 | 4,051.933 | no | 17 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | normal | bloques | XGB-37 | 4,515.785 | 7 | 914.636 | 5,197.008 | no | 17 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | normal | bloques | GC3 | 8,317.618 | 9 | 3,198.714 | 10,806.159 | no | 17 |
| sensibilidad_2023_2025 | sutil | mensual | 60 | normal | bloques | GE | 9,551.020 | 10 | 4,093.509 | 12,090.736 | no | 17 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | shock | iid | Naive | 8,499.329 | 8 | 2,886.694 | 4,575.155 | no | 7 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | shock | iid | Seasonal Naive | 5,275.644 | 3 | -2,468.551 | 3,761.003 | sí | 7 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | shock | iid | Chronos | 4,754.106 | 1 | 0.000 | 0.000 | sí | 7 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | shock | iid | SARIMA | 5,655.990 | 4 | 200.877 | 1,466.314 | no | 7 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | shock | iid | SARIMA-sel | 5,248.203 | 2 | -1,247.671 | 2,528.541 | sí | 7 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | shock | iid | Ridge | 10,341.024 | 10 | 1,802.928 | 11,163.332 | no | 7 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | shock | iid | ElasticNet | 9,927.637 | 9 | 1,555.732 | 9,682.412 | no | 7 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | shock | iid | XGB-37 | 6,264.362 | 5 | -1,476.515 | 3,501.154 | sí | 7 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | shock | iid | GC3 | 6,570.976 | 6 | -74.285 | 3,582.615 | sí | 7 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | shock | iid | GE | 7,523.012 | 7 | 272.857 | 5,020.212 | no | 7 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | shock | bloques | Naive | 8,499.329 | 8 | 2,457.289 | 5,054.106 | no | 7 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | shock | bloques | Seasonal Naive | 5,275.644 | 3 | -3,523.198 | 4,774.044 | sí | 7 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | shock | bloques | Chronos | 4,754.106 | 1 | 0.000 | 0.000 | sí | 7 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | shock | bloques | SARIMA | 5,655.990 | 4 | 262.789 | 1,424.133 | no | 7 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | shock | bloques | SARIMA-sel | 5,248.203 | 2 | -1,309.613 | 2,519.741 | sí | 7 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | shock | bloques | Ridge | 10,341.024 | 10 | 689.541 | 9,911.622 | no | 7 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | shock | bloques | ElasticNet | 9,927.637 | 9 | 592.690 | 8,848.805 | no | 7 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | shock | bloques | XGB-37 | 6,264.362 | 5 | -1,786.567 | 4,262.488 | sí | 7 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | shock | bloques | GC3 | 6,570.976 | 6 | -893.225 | 3,967.747 | sí | 7 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | shock | bloques | GE | 7,523.012 | 7 | -78.416 | 4,931.585 | sí | 7 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | normal | iid | Naive | 3,067.919 | 3 | -65.513 | 1,496.605 | sí | 29 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | normal | iid | Seasonal Naive | 7,684.240 | 8 | 3,796.320 | 6,877.786 | no | 29 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | normal | iid | Chronos | 2,368.391 | 1 | 0.000 | 0.000 | sí | 29 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | normal | iid | SARIMA | 2,994.150 | 2 | -310.766 | 1,550.294 | sí | 29 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | normal | iid | SARIMA-sel | 3,332.703 | 4 | -79.540 | 2,015.583 | sí | 29 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | normal | iid | Ridge | 5,089.106 | 6 | 861.058 | 4,775.526 | no | 29 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | normal | iid | ElasticNet | 5,211.661 | 7 | 1,044.404 | 4,790.374 | no | 29 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | normal | iid | XGB-37 | 4,547.673 | 5 | 905.458 | 3,492.891 | no | 29 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | normal | iid | GC3 | 7,843.669 | 9 | 3,475.915 | 7,571.884 | no | 29 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | normal | iid | GE | 8,359.655 | 10 | 3,882.931 | 8,146.594 | no | 29 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | normal | bloques | Naive | 3,067.919 | 3 | -104.816 | 1,538.547 | sí | 29 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | normal | bloques | Seasonal Naive | 7,684.240 | 8 | 3,149.827 | 7,391.987 | no | 29 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | normal | bloques | Chronos | 2,368.391 | 1 | 0.000 | 0.000 | sí | 29 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | normal | bloques | SARIMA | 2,994.150 | 2 | -282.986 | 1,564.943 | sí | 29 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | normal | bloques | SARIMA-sel | 3,332.703 | 4 | 28.689 | 1,877.602 | no | 29 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | normal | bloques | Ridge | 5,089.106 | 6 | 753.297 | 4,954.862 | no | 29 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | normal | bloques | ElasticNet | 5,211.661 | 7 | 805.973 | 5,167.508 | no | 29 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | normal | bloques | XGB-37 | 4,547.673 | 5 | 500.736 | 4,035.189 | no | 29 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | normal | bloques | GC3 | 7,843.669 | 9 | 2,534.330 | 8,694.351 | no | 29 |
| sensibilidad_2023_2025 | sutil | mensual | 75 | normal | bloques | GE | 8,359.655 | 10 | 2,871.089 | 9,372.564 | no | 29 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | shock | iid | Naive | 8,354.298 | 7 | 2,613.875 | 4,493.384 | no | 5 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | shock | iid | Seasonal Naive | 6,932.613 | 4 | -1,924.371 | 5,832.638 | sí | 5 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | shock | iid | Chronos | 4,978.480 | 1 | 0.000 | 0.000 | sí | 5 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | shock | iid | SARIMA | 6,269.936 | 2 | 882.551 | 1,552.007 | no | 5 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | shock | iid | SARIMA-sel | 6,508.029 | 3 | -344.254 | 3,827.890 | sí | 5 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | shock | iid | Ridge | 12,141.820 | 10 | 3,107.979 | 13,590.383 | no | 5 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | shock | iid | ElasticNet | 11,185.921 | 9 | 2,734.369 | 11,193.301 | no | 5 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | shock | iid | XGB-37 | 7,631.080 | 6 | 1,934.393 | 3,347.262 | no | 5 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | shock | iid | GC3 | 7,395.234 | 5 | 418.419 | 4,741.573 | no | 5 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | shock | iid | GE | 8,447.512 | 8 | 1,798.502 | 5,411.936 | no | 5 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | shock | bloques | Naive | 8,354.298 | 7 | 1,583.440 | 5,167.808 | no | 5 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | shock | bloques | Seasonal Naive | 6,932.613 | 4 | -4,065.449 | 7,721.462 | sí | 5 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | shock | bloques | Chronos | 4,978.480 | 1 | 0.000 | 0.000 | sí | 5 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | shock | bloques | SARIMA | 6,269.936 | 2 | 961.845 | 1,585.326 | no | 5 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | shock | bloques | SARIMA-sel | 6,508.029 | 3 | -183.429 | 3,462.499 | sí | 5 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | shock | bloques | Ridge | 12,141.820 | 10 | 57.379 | 17,539.726 | no | 5 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | shock | bloques | ElasticNet | 11,185.921 | 9 | -738.182 | 15,000.897 | sí | 5 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | shock | bloques | XGB-37 | 7,631.080 | 6 | 426.686 | 5,414.530 | no | 5 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | shock | bloques | GC3 | 7,395.234 | 5 | 273.330 | 5,255.719 | no | 5 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | shock | bloques | GE | 8,447.512 | 8 | 1,205.533 | 5,422.025 | no | 5 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | normal | iid | Naive | 3,441.724 | 4 | 161.730 | 1,798.681 | no | 31 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | normal | iid | Seasonal Naive | 7,261.594 | 8 | 3,227.508 | 6,371.234 | no | 31 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | normal | iid | Chronos | 2,486.119 | 1 | 0.000 | 0.000 | sí | 31 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | normal | iid | SARIMA | 3,066.858 | 2 | -290.517 | 1,468.512 | sí | 31 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | normal | iid | SARIMA-sel | 3,253.085 | 3 | -245.429 | 1,782.812 | sí | 31 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | normal | iid | Ridge | 5,137.488 | 6 | 909.271 | 4,668.927 | no | 31 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | normal | iid | ElasticNet | 5,312.969 | 7 | 1,118.872 | 4,749.713 | no | 31 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | normal | iid | XGB-37 | 4,437.989 | 5 | 618.176 | 3,316.118 | no | 31 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | normal | iid | GC3 | 7,628.615 | 9 | 3,132.598 | 7,243.360 | no | 31 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | normal | iid | GE | 8,156.565 | 10 | 3,527.078 | 7,863.427 | no | 31 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | normal | bloques | Naive | 3,441.724 | 4 | 96.973 | 1,823.822 | no | 31 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | normal | bloques | Seasonal Naive | 7,261.594 | 8 | 2,710.715 | 6,827.905 | no | 31 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | normal | bloques | Chronos | 2,486.119 | 1 | 0.000 | 0.000 | sí | 31 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | normal | bloques | SARIMA | 3,066.858 | 2 | -248.446 | 1,449.115 | sí | 31 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | normal | bloques | SARIMA-sel | 3,253.085 | 3 | -128.572 | 1,656.180 | sí | 31 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | normal | bloques | Ridge | 5,137.488 | 6 | 814.974 | 4,764.318 | no | 31 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | normal | bloques | ElasticNet | 5,312.969 | 7 | 889.336 | 5,050.132 | no | 31 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | normal | bloques | XGB-37 | 4,437.989 | 5 | 296.913 | 3,757.883 | no | 31 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | normal | bloques | GC3 | 7,628.615 | 9 | 2,379.591 | 8,212.194 | no | 31 |
| sensibilidad_2023_2025 | sutil | mensual | 90 | normal | bloques | GE | 8,156.565 | 10 | 2,652.396 | 8,917.191 | no | 31 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | shock | iid | Naive | 3,779.682 | 3 | -159.623 | 2,088.925 | sí | 19 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | shock | iid | Seasonal Naive | 10,822.202 | 10 | 6,663.701 | 9,273.671 | no | 19 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | shock | iid | Chronos | 2,847.893 | 1 | 0.000 | 0.000 | sí | 19 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | shock | iid | SARIMA | 3,455.860 | 2 | -544.596 | 1,657.466 | sí | 19 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | shock | iid | SARIMA-sel | 3,887.881 | 4 | -363.496 | 2,439.546 | sí | 19 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | shock | iid | Ridge | 5,898.074 | 6 | 947.058 | 5,460.550 | no | 19 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | shock | iid | ElasticNet | 6,327.277 | 7 | 1,356.134 | 5,848.239 | no | 19 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | shock | iid | XGB-37 | 4,544.470 | 5 | 76.964 | 3,395.659 | no | 19 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | shock | iid | GC3 | 8,044.488 | 9 | 2,752.722 | 7,773.592 | no | 19 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | shock | iid | GE | 8,029.482 | 8 | 2,832.237 | 7,657.307 | no | 19 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | shock | bloques | Naive | 3,779.682 | 3 | -298.641 | 2,079.668 | sí | 19 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | shock | bloques | Seasonal Naive | 10,822.202 | 10 | 5,985.256 | 10,011.573 | no | 19 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | shock | bloques | Chronos | 2,847.893 | 1 | 0.000 | 0.000 | sí | 19 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | shock | bloques | SARIMA | 3,455.860 | 2 | -606.692 | 1,612.154 | sí | 19 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | shock | bloques | SARIMA-sel | 3,887.881 | 4 | -328.917 | 2,361.027 | sí | 19 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | shock | bloques | Ridge | 5,898.074 | 6 | 279.185 | 6,215.406 | no | 19 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | shock | bloques | ElasticNet | 6,327.277 | 7 | 538.628 | 6,748.919 | no | 19 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | shock | bloques | XGB-37 | 4,544.470 | 5 | -419.305 | 4,108.365 | sí | 19 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | shock | bloques | GC3 | 8,044.488 | 9 | 1,783.163 | 9,154.144 | no | 19 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | shock | bloques | GE | 8,029.482 | 8 | 1,850.696 | 9,027.464 | no | 19 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | normal | iid | Naive | 4,508.881 | 5 | 665.120 | 2,683.539 | no | 17 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | normal | iid | Seasonal Naive | 3,185.332 | 2 | -962.191 | 1,705.144 | sí | 17 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | normal | iid | Chronos | 2,814.830 | 1 | 0.000 | 0.000 | sí | 17 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | normal | iid | SARIMA | 3,574.173 | 4 | -120.220 | 1,731.005 | sí | 17 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | normal | iid | SARIMA-sel | 3,500.944 | 3 | -187.732 | 1,586.912 | sí | 17 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | normal | iid | Ridge | 6,347.519 | 8 | 782.145 | 6,518.241 | no | 17 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | normal | iid | ElasticNet | 5,906.669 | 7 | 645.048 | 5,794.530 | no | 17 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | normal | iid | XGB-37 | 5,258.125 | 6 | 919.061 | 3,738.433 | no | 17 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | normal | iid | GC3 | 7,095.174 | 9 | 1,897.316 | 6,565.137 | no | 17 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | normal | iid | GE | 8,384.171 | 10 | 2,877.472 | 8,112.116 | no | 17 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | normal | bloques | Naive | 4,508.881 | 5 | 718.804 | 2,710.611 | no | 17 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | normal | bloques | Seasonal Naive | 3,185.332 | 2 | -776.181 | 1,436.474 | sí | 17 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | normal | bloques | Chronos | 2,814.830 | 1 | 0.000 | 0.000 | sí | 17 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | normal | bloques | SARIMA | 3,574.173 | 4 | -184.048 | 1,839.902 | sí | 17 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | normal | bloques | SARIMA-sel | 3,500.944 | 3 | -93.146 | 1,489.526 | sí | 17 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | normal | bloques | Ridge | 6,347.519 | 8 | 312.361 | 7,317.863 | no | 17 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | normal | bloques | ElasticNet | 5,906.669 | 7 | 110.175 | 6,479.936 | no | 17 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | normal | bloques | XGB-37 | 5,258.125 | 6 | 891.840 | 4,019.728 | no | 17 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | normal | bloques | GC3 | 7,095.174 | 9 | 1,485.566 | 6,966.124 | no | 17 |
| sensibilidad_2023_2025 | sutil | interanual | 50 | normal | bloques | GE | 8,384.171 | 10 | 2,045.551 | 8,884.181 | no | 17 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | shock | iid | Naive | 3,779.636 | 3 | -42.219 | 2,473.755 | sí | 16 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | shock | iid | Seasonal Naive | 11,358.836 | 10 | 7,255.965 | 10,281.950 | no | 16 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | shock | iid | Chronos | 2,585.288 | 1 | 0.000 | 0.000 | sí | 16 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | shock | iid | SARIMA | 3,480.061 | 2 | -483.486 | 2,118.700 | sí | 16 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | shock | iid | SARIMA-sel | 4,091.250 | 4 | -145.049 | 3,130.738 | sí | 16 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | shock | iid | Ridge | 5,980.085 | 6 | 909.251 | 6,227.125 | no | 16 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | shock | iid | ElasticNet | 6,447.932 | 7 | 1,379.211 | 6,684.471 | no | 16 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | shock | iid | XGB-37 | 5,050.962 | 5 | 735.383 | 4,337.273 | no | 16 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | shock | iid | GC3 | 8,664.074 | 8 | 3,401.474 | 8,992.993 | no | 16 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | shock | iid | GE | 8,916.530 | 9 | 3,768.776 | 9,090.001 | no | 16 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | shock | bloques | Naive | 3,779.636 | 3 | -208.618 | 2,471.929 | sí | 16 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | shock | bloques | Seasonal Naive | 11,358.836 | 10 | 6,611.143 | 11,114.874 | no | 16 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | shock | bloques | Chronos | 2,585.288 | 1 | 0.000 | 0.000 | sí | 16 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | shock | bloques | SARIMA | 3,480.061 | 2 | -564.098 | 1,911.606 | sí | 16 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | shock | bloques | SARIMA-sel | 4,091.250 | 4 | -46.923 | 2,928.145 | sí | 16 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | shock | bloques | Ridge | 5,980.085 | 6 | -57.002 | 7,079.352 | sí | 16 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | shock | bloques | ElasticNet | 6,447.932 | 7 | 227.685 | 7,655.502 | no | 16 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | shock | bloques | XGB-37 | 5,050.962 | 5 | 221.968 | 5,274.494 | no | 16 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | shock | bloques | GC3 | 8,664.074 | 8 | 2,291.261 | 10,648.948 | no | 16 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | shock | bloques | GE | 8,916.530 | 9 | 2,808.881 | 10,774.818 | no | 16 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | normal | iid | Naive | 4,399.538 | 5 | 400.303 | 2,351.144 | no | 20 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | normal | iid | Seasonal Naive | 3,901.555 | 4 | -424.482 | 2,109.213 | sí | 20 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | normal | iid | Chronos | 3,029.874 | 1 | 0.000 | 0.000 | sí | 20 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | normal | iid | SARIMA | 3,537.065 | 3 | -330.143 | 1,429.255 | sí | 20 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | normal | iid | SARIMA-sel | 3,396.290 | 2 | -548.918 | 1,289.264 | sí | 20 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | normal | iid | Ridge | 6,214.494 | 8 | 877.463 | 5,817.263 | no | 20 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | normal | iid | ElasticNet | 5,873.237 | 7 | 782.805 | 5,192.877 | no | 20 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | normal | iid | XGB-37 | 4,745.883 | 6 | 174.780 | 3,133.315 | no | 20 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | normal | iid | GC3 | 6,741.902 | 9 | 1,590.358 | 5,820.241 | no | 20 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | normal | iid | GE | 7,621.330 | 10 | 2,051.862 | 7,085.614 | no | 20 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | normal | bloques | Naive | 4,399.538 | 5 | 471.684 | 2,261.210 | no | 20 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | normal | bloques | Seasonal Naive | 3,901.555 | 4 | -245.806 | 2,008.174 | sí | 20 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | normal | bloques | Chronos | 3,029.874 | 1 | 0.000 | 0.000 | sí | 20 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | normal | bloques | SARIMA | 3,537.065 | 3 | -363.354 | 1,566.742 | sí | 20 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | normal | bloques | SARIMA-sel | 3,396.290 | 2 | -555.574 | 1,232.974 | sí | 20 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | normal | bloques | Ridge | 6,214.494 | 8 | 525.156 | 6,468.626 | no | 20 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | normal | bloques | ElasticNet | 5,873.237 | 7 | 371.173 | 5,677.138 | no | 20 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | normal | bloques | XGB-37 | 4,745.883 | 6 | 124.270 | 3,331.570 | no | 20 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | normal | bloques | GC3 | 6,741.902 | 9 | 1,331.286 | 6,325.453 | no | 20 |
| sensibilidad_2023_2025 | sutil | interanual | 60 | normal | bloques | GE | 7,621.330 | 10 | 1,347.108 | 8,008.052 | no | 20 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | shock | iid | Naive | 3,171.846 | 2 | -90.077 | 2,851.978 | sí | 10 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | shock | iid | Seasonal Naive | 12,508.067 | 10 | 8,351.592 | 12,904.867 | no | 10 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | shock | iid | Chronos | 1,864.113 | 1 | 0.000 | 0.000 | sí | 10 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | shock | iid | SARIMA | 3,232.720 | 3 | 399.107 | 2,223.819 | no | 10 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | shock | iid | SARIMA-sel | 4,078.830 | 4 | 115.027 | 4,343.427 | no | 10 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | shock | iid | Ridge | 4,946.068 | 6 | 1,092.543 | 5,265.942 | no | 10 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | shock | iid | ElasticNet | 5,403.723 | 7 | 1,279.184 | 6,034.041 | no | 10 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | shock | iid | XGB-37 | 4,816.485 | 5 | 446.460 | 5,673.369 | no | 10 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | shock | iid | GC3 | 9,166.116 | 8 | 3,189.903 | 11,742.247 | no | 10 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | shock | iid | GE | 9,796.027 | 9 | 3,968.769 | 12,152.721 | no | 10 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | shock | bloques | Naive | 3,171.846 | 2 | -595.290 | 3,081.498 | sí | 10 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | shock | bloques | Seasonal Naive | 12,508.067 | 10 | 7,883.015 | 13,501.157 | no | 10 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | shock | bloques | Chronos | 1,864.113 | 1 | 0.000 | 0.000 | sí | 10 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | shock | bloques | SARIMA | 3,232.720 | 3 | 456.378 | 2,101.621 | no | 10 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | shock | bloques | SARIMA-sel | 4,078.830 | 4 | 368.977 | 4,129.583 | no | 10 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | shock | bloques | Ridge | 4,946.068 | 6 | 152.077 | 6,829.303 | no | 10 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | shock | bloques | ElasticNet | 5,403.723 | 7 | 197.695 | 7,703.621 | no | 10 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | shock | bloques | XGB-37 | 4,816.485 | 5 | -559.587 | 7,435.545 | sí | 10 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | shock | bloques | GC3 | 9,166.116 | 8 | 1,634.967 | 14,627.139 | no | 10 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | shock | bloques | GE | 9,796.027 | 9 | 2,458.696 | 15,084.640 | no | 10 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | normal | iid | Naive | 4,490.249 | 4 | 357.530 | 2,189.591 | no | 26 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | normal | iid | Seasonal Naive | 5,180.454 | 6 | 719.657 | 3,169.634 | no | 26 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | normal | iid | Chronos | 3,204.652 | 1 | 0.000 | 0.000 | sí | 26 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | normal | iid | SARIMA | 3,619.041 | 3 | -601.786 | 1,391.831 | sí | 26 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | normal | iid | SARIMA-sel | 3,561.442 | 2 | -584.363 | 1,256.412 | sí | 26 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | normal | iid | Ridge | 6,558.098 | 8 | 1,050.076 | 5,883.728 | no | 26 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | normal | iid | ElasticNet | 6,407.477 | 7 | 1,131.073 | 5,470.211 | no | 26 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | normal | iid | XGB-37 | 4,906.469 | 5 | 444.493 | 2,866.277 | no | 26 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | normal | iid | GC3 | 6,992.387 | 9 | 2,029.299 | 5,544.132 | no | 26 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | normal | iid | GE | 7,581.954 | 10 | 2,395.181 | 6,319.584 | no | 26 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | normal | bloques | Naive | 4,490.249 | 4 | 526.655 | 2,036.757 | no | 26 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | normal | bloques | Seasonal Naive | 5,180.454 | 6 | 676.146 | 3,328.655 | no | 26 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | normal | bloques | Chronos | 3,204.652 | 1 | 0.000 | 0.000 | sí | 26 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | normal | bloques | SARIMA | 3,619.041 | 3 | -526.228 | 1,437.462 | sí | 26 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | normal | bloques | SARIMA-sel | 3,561.442 | 2 | -455.598 | 1,180.200 | sí | 26 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | normal | bloques | Ridge | 6,558.098 | 8 | 894.198 | 6,096.522 | no | 26 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | normal | bloques | ElasticNet | 6,407.477 | 7 | 926.351 | 5,706.837 | no | 26 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | normal | bloques | XGB-37 | 4,906.469 | 5 | 413.358 | 2,904.437 | no | 26 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | normal | bloques | GC3 | 6,992.387 | 9 | 1,768.913 | 6,028.155 | no | 26 |
| sensibilidad_2023_2025 | sutil | interanual | 75 | normal | bloques | GE | 7,581.954 | 10 | 1,861.182 | 7,027.831 | no | 26 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | shock | iid | Naive | 1,538.943 | 2 | -872.232 | 1,946.963 | sí | 4 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | shock | iid | Seasonal Naive | 15,258.750 | 10 | 10,697.834 | 16,638.532 | no | 4 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | shock | iid | Chronos | 1,116.204 | 1 | 0.000 | 0.000 | sí | 4 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | shock | iid | SARIMA | 3,725.435 | 3 | 1,722.092 | 3,294.135 | no | 4 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | shock | iid | SARIMA-sel | 5,506.388 | 6 | 2,270.739 | 6,509.629 | no | 4 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | shock | iid | Ridge | 4,169.104 | 4 | 348.179 | 5,942.954 | no | 4 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | shock | iid | ElasticNet | 4,817.704 | 5 | 439.913 | 6,974.822 | no | 4 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | shock | iid | XGB-37 | 5,555.691 | 7 | -322.930 | 9,201.904 | sí | 4 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | shock | iid | GC3 | 10,211.615 | 8 | 1,533.800 | 16,657.022 | no | 4 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | shock | iid | GE | 11,299.378 | 9 | 3,132.745 | 17,233.604 | no | 4 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | shock | bloques | Naive | 1,538.943 | 2 | -981.900 | 2,070.817 | sí | 4 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | shock | bloques | Seasonal Naive | 15,258.750 | 10 | 10,746.501 | 16,867.314 | no | 4 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | shock | bloques | Chronos | 1,116.204 | 1 | 0.000 | 0.000 | sí | 4 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | shock | bloques | SARIMA | 3,725.435 | 3 | 1,722.092 | 3,294.135 | no | 4 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | shock | bloques | SARIMA-sel | 5,506.388 | 6 | 2,270.739 | 6,509.629 | no | 4 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | shock | bloques | Ridge | 4,169.104 | 4 | 187.593 | 6,387.512 | no | 4 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | shock | bloques | ElasticNet | 4,817.704 | 5 | 248.083 | 7,629.157 | no | 4 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | shock | bloques | XGB-37 | 5,555.691 | 7 | -553.494 | 10,058.817 | sí | 4 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | shock | bloques | GC3 | 10,211.615 | 8 | 1,334.293 | 17,406.372 | no | 4 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | shock | bloques | GE | 11,299.378 | 9 | 2,878.974 | 17,961.359 | no | 4 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | normal | iid | Naive | 4,447.162 | 4 | 549.423 | 2,261.601 | no | 32 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | normal | iid | Seasonal Naive | 6,210.546 | 6 | 1,863.148 | 4,487.985 | no | 32 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | normal | iid | Chronos | 3,046.790 | 1 | 0.000 | 0.000 | sí | 32 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | normal | iid | SARIMA | 3,485.017 | 3 | -414.453 | 1,245.910 | sí | 32 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | normal | iid | SARIMA-sel | 3,480.008 | 2 | -470.121 | 1,302.400 | sí | 32 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | normal | iid | Ridge | 6,352.963 | 8 | 1,366.054 | 5,448.646 | no | 32 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | normal | iid | ElasticNet | 6,292.526 | 7 | 1,444.571 | 5,200.013 | no | 32 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | normal | iid | XGB-37 | 4,797.197 | 5 | 608.705 | 2,847.851 | no | 32 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | normal | iid | GC3 | 7,269.274 | 9 | 2,518.363 | 5,967.382 | no | 32 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | normal | iid | GE | 7,809.174 | 10 | 2,924.432 | 6,614.561 | no | 32 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | normal | bloques | Naive | 4,447.162 | 4 | 581.427 | 2,234.645 | no | 32 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | normal | bloques | Seasonal Naive | 6,210.546 | 6 | 1,786.436 | 4,550.467 | no | 32 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | normal | bloques | Chronos | 3,046.790 | 1 | 0.000 | 0.000 | sí | 32 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | normal | bloques | SARIMA | 3,485.017 | 3 | -349.192 | 1,219.353 | sí | 32 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | normal | bloques | SARIMA-sel | 3,480.008 | 2 | -351.881 | 1,230.878 | sí | 32 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | normal | bloques | Ridge | 6,352.963 | 8 | 955.665 | 5,627.066 | no | 32 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | normal | bloques | ElasticNet | 6,292.526 | 7 | 1,015.990 | 5,451.377 | no | 32 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | normal | bloques | XGB-37 | 4,797.197 | 5 | 497.318 | 3,012.352 | no | 32 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | normal | bloques | GC3 | 7,269.274 | 9 | 2,082.975 | 6,574.376 | no | 32 |
| sensibilidad_2023_2025 | sutil | interanual | 90 | normal | bloques | GE | 7,809.174 | 10 | 2,341.303 | 7,293.159 | no | 32 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | shock | iid | Naive | 118.944 | 10 | 84.478 | 122.366 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | shock | iid | Seasonal Naive | 20.447 | 3 | -0.984 | 10.374 | sí | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | shock | iid | Chronos | 41.848 | 4 | 15.812 | 36.548 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | shock | iid | SARIMA | 16.608 | 2 | -0.474 | 2.663 | sí | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | shock | iid | SARIMA-sel | 15.530 | 1 | 0.000 | 0.000 | sí | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | shock | iid | Ridge | 65.966 | 9 | 29.946 | 73.649 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | shock | iid | ElasticNet | 59.680 | 8 | 23.111 | 67.549 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | shock | iid | XGB-37 | 47.879 | 5 | 15.697 | 49.034 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | shock | iid | GC3 | 57.077 | 7 | 24.304 | 60.213 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | shock | iid | GE | 55.148 | 6 | 23.433 | 57.333 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | shock | bloques | Naive | 118.944 | 10 | 82.968 | 123.615 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | shock | bloques | Seasonal Naive | 20.447 | 3 | -1.630 | 11.044 | sí | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | shock | bloques | Chronos | 41.848 | 4 | 13.564 | 37.137 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | shock | bloques | SARIMA | 16.608 | 2 | -0.280 | 2.776 | sí | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | shock | bloques | SARIMA-sel | 15.530 | 1 | 0.000 | 0.000 | sí | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | shock | bloques | Ridge | 65.966 | 9 | 27.128 | 75.114 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | shock | bloques | ElasticNet | 59.680 | 8 | 20.384 | 69.457 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | shock | bloques | XGB-37 | 47.879 | 5 | 12.073 | 49.629 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | shock | bloques | GC3 | 57.077 | 7 | 21.031 | 64.175 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | shock | bloques | GE | 55.148 | 6 | 21.606 | 58.624 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | normal | iid | Naive | 45.372 | 5 | 4.882 | 32.156 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | normal | iid | Seasonal Naive | 35.672 | 4 | 2.448 | 15.423 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | normal | iid | Chronos | 28.072 | 3 | -10.672 | 12.830 | sí | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | normal | iid | SARIMA | 27.400 | 2 | 0.239 | 1.913 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | normal | iid | SARIMA-sel | 26.342 | 1 | 0.000 | 0.000 | sí | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | normal | iid | Ridge | 61.971 | 8 | 16.436 | 53.605 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | normal | iid | ElasticNet | 59.309 | 6 | 13.504 | 51.033 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | normal | iid | XGB-37 | 60.931 | 7 | 12.908 | 55.670 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | normal | iid | GC3 | 82.695 | 10 | 30.688 | 81.446 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | normal | iid | GE | 81.567 | 9 | 30.581 | 79.219 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | normal | bloques | Naive | 45.372 | 5 | 7.917 | 28.631 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | normal | bloques | Seasonal Naive | 35.672 | 4 | 1.198 | 17.031 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | normal | bloques | Chronos | 28.072 | 3 | -9.581 | 12.567 | sí | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | normal | bloques | SARIMA | 27.400 | 2 | 0.403 | 1.680 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | normal | bloques | SARIMA-sel | 26.342 | 1 | 0.000 | 0.000 | sí | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | normal | bloques | Ridge | 61.971 | 8 | 14.925 | 54.818 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | normal | bloques | ElasticNet | 59.309 | 6 | 11.801 | 52.459 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | normal | bloques | XGB-37 | 60.931 | 7 | 8.853 | 59.257 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | normal | bloques | GC3 | 82.695 | 10 | 22.501 | 91.114 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 50 | normal | bloques | GE | 81.567 | 9 | 23.131 | 87.594 | no | 18 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | shock | iid | Naive | 133.204 | 10 | 100.672 | 135.843 | no | 14 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | shock | iid | Seasonal Naive | 22.472 | 3 | 2.282 | 13.310 | no | 14 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | shock | iid | Chronos | 48.368 | 4 | 24.204 | 43.228 | no | 14 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | shock | iid | SARIMA | 15.732 | 2 | 0.384 | 1.774 | no | 14 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | shock | iid | SARIMA-sel | 14.657 | 1 | 0.000 | 0.000 | sí | 14 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | shock | iid | Ridge | 66.242 | 9 | 32.094 | 72.972 | no | 14 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | shock | iid | ElasticNet | 61.312 | 7 | 26.402 | 68.808 | no | 14 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | shock | iid | XGB-37 | 55.822 | 5 | 23.821 | 58.193 | no | 14 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | shock | iid | GC3 | 63.916 | 8 | 29.833 | 69.382 | no | 14 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | shock | iid | GE | 60.119 | 6 | 27.549 | 65.114 | no | 14 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | shock | bloques | Naive | 133.204 | 10 | 100.995 | 136.397 | no | 14 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | shock | bloques | Seasonal Naive | 22.472 | 3 | 1.376 | 14.673 | no | 14 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | shock | bloques | Chronos | 48.368 | 4 | 22.475 | 42.013 | no | 14 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | shock | bloques | SARIMA | 15.732 | 2 | 0.353 | 1.954 | no | 14 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | shock | bloques | SARIMA-sel | 14.657 | 1 | 0.000 | 0.000 | sí | 14 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | shock | bloques | Ridge | 66.242 | 9 | 29.734 | 74.442 | no | 14 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | shock | bloques | ElasticNet | 61.312 | 7 | 23.130 | 69.605 | no | 14 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | shock | bloques | XGB-37 | 55.822 | 5 | 20.054 | 56.632 | no | 14 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | shock | bloques | GC3 | 63.916 | 8 | 26.067 | 73.161 | no | 14 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | shock | bloques | GE | 60.119 | 6 | 25.457 | 65.190 | no | 14 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | normal | iid | Naive | 49.674 | 5 | 11.962 | 36.650 | no | 22 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | normal | iid | Seasonal Naive | 31.615 | 4 | 0.181 | 12.677 | no | 22 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | normal | iid | Chronos | 26.427 | 3 | -8.940 | 10.969 | sí | 22 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | normal | iid | SARIMA | 25.996 | 2 | -0.331 | 2.525 | sí | 22 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | normal | iid | SARIMA-sel | 24.932 | 1 | 0.000 | 0.000 | sí | 22 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | normal | iid | Ridge | 62.521 | 8 | 18.746 | 57.234 | no | 22 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | normal | iid | ElasticNet | 58.338 | 7 | 14.684 | 52.836 | no | 22 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | normal | iid | XGB-37 | 53.504 | 6 | 10.013 | 47.028 | no | 22 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | normal | iid | GC3 | 73.685 | 10 | 26.054 | 71.236 | no | 22 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | normal | iid | GE | 73.600 | 9 | 26.949 | 70.138 | no | 22 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | normal | bloques | Naive | 49.674 | 5 | 17.682 | 32.002 | no | 22 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | normal | bloques | Seasonal Naive | 31.615 | 4 | -1.333 | 14.688 | sí | 22 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | normal | bloques | Chronos | 26.427 | 3 | -7.834 | 10.648 | sí | 22 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | normal | bloques | SARIMA | 25.996 | 2 | -0.113 | 2.169 | sí | 22 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | normal | bloques | SARIMA-sel | 24.932 | 1 | 0.000 | 0.000 | sí | 22 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | normal | bloques | Ridge | 62.521 | 8 | 15.191 | 58.960 | no | 22 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | normal | bloques | ElasticNet | 58.338 | 7 | 10.955 | 55.004 | no | 22 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | normal | bloques | XGB-37 | 53.504 | 6 | 5.819 | 53.212 | no | 22 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | normal | bloques | GC3 | 73.685 | 10 | 19.517 | 82.410 | no | 22 |
| sensibilidad_2023_2025 | dulce | mensual | 60 | normal | bloques | GE | 73.600 | 9 | 21.011 | 80.074 | no | 22 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | shock | iid | Naive | 138.176 | 10 | 103.950 | 139.845 | no | 9 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | shock | iid | Seasonal Naive | 25.016 | 3 | 3.397 | 12.593 | no | 9 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | shock | iid | Chronos | 55.332 | 4 | 25.802 | 50.219 | no | 9 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | shock | iid | SARIMA | 17.555 | 2 | -0.221 | 1.636 | sí | 9 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | shock | iid | SARIMA-sel | 16.888 | 1 | 0.000 | 0.000 | sí | 9 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | shock | iid | Ridge | 84.155 | 9 | 44.984 | 93.141 | no | 9 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | shock | iid | ElasticNet | 79.726 | 8 | 39.772 | 90.736 | no | 9 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | shock | iid | XGB-37 | 69.124 | 6 | 34.214 | 70.641 | no | 9 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | shock | iid | GC3 | 71.912 | 7 | 33.202 | 79.186 | no | 9 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | shock | iid | GE | 67.639 | 5 | 27.538 | 76.785 | no | 9 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | shock | bloques | Naive | 138.176 | 10 | 102.257 | 138.305 | no | 9 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | shock | bloques | Seasonal Naive | 25.016 | 3 | -0.207 | 13.726 | sí | 9 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | shock | bloques | Chronos | 55.332 | 4 | 20.707 | 48.838 | no | 9 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | shock | bloques | SARIMA | 17.555 | 2 | -0.325 | 2.018 | sí | 9 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | shock | bloques | SARIMA-sel | 16.888 | 1 | 0.000 | 0.000 | sí | 9 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | shock | bloques | Ridge | 84.155 | 9 | 38.752 | 95.809 | no | 9 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | shock | bloques | ElasticNet | 79.726 | 8 | 32.191 | 91.309 | no | 9 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | shock | bloques | XGB-37 | 69.124 | 6 | 24.169 | 72.051 | no | 9 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | shock | bloques | GC3 | 71.912 | 7 | 17.968 | 88.823 | no | 9 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | shock | bloques | GE | 67.639 | 5 | 17.940 | 79.288 | no | 9 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | normal | iid | Naive | 63.485 | 8 | 24.043 | 59.690 | no | 27 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | normal | iid | Seasonal Naive | 29.074 | 4 | 1.208 | 12.071 | no | 27 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | normal | iid | Chronos | 28.169 | 3 | -3.481 | 14.317 | sí | 27 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | normal | iid | SARIMA | 23.487 | 2 | 0.039 | 2.391 | no | 27 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | normal | iid | SARIMA-sel | 22.286 | 1 | 0.000 | 0.000 | sí | 27 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | normal | iid | Ridge | 57.239 | 7 | 19.302 | 51.736 | no | 27 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | normal | iid | ElasticNet | 52.751 | 6 | 15.014 | 47.210 | no | 27 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | normal | iid | XGB-37 | 49.499 | 5 | 11.244 | 43.490 | no | 27 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | normal | iid | GC3 | 69.210 | 10 | 28.369 | 66.236 | no | 27 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | normal | iid | GE | 68.597 | 9 | 28.694 | 64.726 | no | 27 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | normal | bloques | Naive | 63.485 | 8 | 28.959 | 53.643 | no | 27 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | normal | bloques | Seasonal Naive | 29.074 | 4 | -1.234 | 14.334 | sí | 27 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | normal | bloques | Chronos | 28.169 | 3 | -2.120 | 13.805 | sí | 27 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | normal | bloques | SARIMA | 23.487 | 2 | 0.210 | 2.131 | no | 27 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | normal | bloques | SARIMA-sel | 22.286 | 1 | 0.000 | 0.000 | sí | 27 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | normal | bloques | Ridge | 57.239 | 7 | 15.831 | 54.426 | no | 27 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | normal | bloques | ElasticNet | 52.751 | 6 | 11.942 | 49.748 | no | 27 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | normal | bloques | XGB-37 | 49.499 | 5 | 8.866 | 48.489 | no | 27 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | normal | bloques | GC3 | 69.210 | 10 | 20.904 | 76.142 | no | 27 |
| sensibilidad_2023_2025 | dulce | mensual | 75 | normal | bloques | GE | 68.597 | 9 | 22.129 | 73.807 | no | 27 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | shock | iid | Naive | 98.110 | 10 | 74.539 | 74.539 | no | 1 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | shock | iid | Seasonal Naive | 25.930 | 3 | 2.359 | 2.359 | no | 1 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | shock | iid | Chronos | 61.804 | 6 | 38.233 | 38.233 | no | 1 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | shock | iid | SARIMA | 23.571 | 1 | 0.000 | 0.000 | sí | 1 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | shock | iid | SARIMA-sel | 23.803 | 2 | 0.232 | 0.232 | no | 1 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | shock | iid | Ridge | 77.378 | 8 | 53.807 | 53.807 | no | 1 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | shock | iid | ElasticNet | 69.308 | 7 | 45.737 | 45.737 | no | 1 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | shock | iid | XGB-37 | 94.008 | 9 | 70.438 | 70.438 | no | 1 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | shock | iid | GC3 | 31.716 | 4 | 8.145 | 8.145 | no | 1 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | shock | iid | GE | 38.175 | 5 | 14.605 | 14.605 | no | 1 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | shock | bloques | Naive | 98.110 | 10 | 74.539 | 74.539 | no | 1 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | shock | bloques | Seasonal Naive | 25.930 | 3 | 2.359 | 2.359 | no | 1 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | shock | bloques | Chronos | 61.804 | 6 | 38.233 | 38.233 | no | 1 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | shock | bloques | SARIMA | 23.571 | 1 | 0.000 | 0.000 | sí | 1 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | shock | bloques | SARIMA-sel | 23.803 | 2 | 0.232 | 0.232 | no | 1 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | shock | bloques | Ridge | 77.378 | 8 | 53.807 | 53.807 | no | 1 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | shock | bloques | ElasticNet | 69.308 | 7 | 45.737 | 45.737 | no | 1 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | shock | bloques | XGB-37 | 94.008 | 9 | 70.438 | 70.438 | no | 1 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | shock | bloques | GC3 | 31.716 | 4 | 8.145 | 8.145 | no | 1 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | shock | bloques | GE | 38.175 | 5 | 14.605 | 14.605 | no | 1 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | normal | iid | Naive | 81.702 | 10 | 42.351 | 79.206 | no | 35 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | normal | iid | Seasonal Naive | 28.120 | 3 | 2.446 | 11.586 | no | 35 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | normal | iid | Chronos | 34.193 | 4 | 4.019 | 21.914 | no | 35 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | normal | iid | SARIMA | 21.959 | 2 | 0.156 | 2.078 | no | 35 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | normal | iid | SARIMA-sel | 20.854 | 1 | 0.000 | 0.000 | sí | 35 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | normal | iid | Ridge | 63.585 | 7 | 28.277 | 57.636 | no | 35 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | normal | iid | ElasticNet | 59.214 | 6 | 23.806 | 53.494 | no | 35 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | normal | iid | XGB-37 | 53.274 | 5 | 18.077 | 46.531 | no | 35 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | normal | iid | GC3 | 70.976 | 9 | 34.039 | 66.390 | no | 35 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | normal | iid | GE | 69.220 | 8 | 32.918 | 63.915 | no | 35 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | normal | bloques | Naive | 81.702 | 10 | 44.495 | 78.047 | no | 35 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | normal | bloques | Seasonal Naive | 28.120 | 3 | 1.352 | 12.743 | no | 35 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | normal | bloques | Chronos | 34.193 | 4 | 2.904 | 23.563 | no | 35 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | normal | bloques | SARIMA | 21.959 | 2 | 0.410 | 1.816 | no | 35 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | normal | bloques | SARIMA-sel | 20.854 | 1 | 0.000 | 0.000 | sí | 35 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | normal | bloques | Ridge | 63.585 | 7 | 24.703 | 60.719 | no | 35 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | normal | bloques | ElasticNet | 59.214 | 6 | 19.527 | 57.211 | no | 35 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | normal | bloques | XGB-37 | 53.274 | 5 | 13.765 | 50.612 | no | 35 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | normal | bloques | GC3 | 70.976 | 9 | 26.173 | 74.340 | no | 35 |
| sensibilidad_2023_2025 | dulce | mensual | 90 | normal | bloques | GE | 69.220 | 8 | 26.296 | 71.219 | no | 35 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | shock | iid | Naive | 86.272 | 10 | 32.343 | 85.295 | no | 19 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | shock | iid | Seasonal Naive | 41.943 | 4 | 8.144 | 20.656 | no | 19 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | shock | iid | Chronos | 35.230 | 3 | -4.880 | 19.833 | sí | 19 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | shock | iid | SARIMA | 27.461 | 2 | -0.999 | 1.570 | sí | 19 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | shock | iid | SARIMA-sel | 27.097 | 1 | 0.000 | 0.000 | sí | 19 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | shock | iid | Ridge | 77.962 | 8 | 30.900 | 70.261 | no | 19 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | shock | iid | ElasticNet | 69.886 | 6 | 22.674 | 62.808 | no | 19 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | shock | iid | XGB-37 | 56.865 | 5 | 9.791 | 49.327 | no | 19 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | shock | iid | GC3 | 80.927 | 9 | 31.969 | 74.902 | no | 19 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | shock | iid | GE | 77.568 | 7 | 29.415 | 70.684 | no | 19 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | shock | bloques | Naive | 86.272 | 10 | 39.057 | 80.419 | no | 19 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | shock | bloques | Seasonal Naive | 41.943 | 4 | 8.382 | 21.759 | no | 19 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | shock | bloques | Chronos | 35.230 | 3 | -3.824 | 21.493 | sí | 19 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | shock | bloques | SARIMA | 27.461 | 2 | -0.712 | 1.320 | sí | 19 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | shock | bloques | SARIMA-sel | 27.097 | 1 | 0.000 | 0.000 | sí | 19 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | shock | bloques | Ridge | 77.962 | 8 | 32.418 | 72.747 | no | 19 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | shock | bloques | ElasticNet | 69.886 | 6 | 23.719 | 66.057 | no | 19 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | shock | bloques | XGB-37 | 56.865 | 5 | 8.266 | 51.966 | no | 19 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | shock | bloques | GC3 | 80.927 | 9 | 26.809 | 81.433 | no | 19 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | shock | bloques | GE | 77.568 | 7 | 26.137 | 75.854 | no | 19 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | normal | iid | Naive | 77.560 | 10 | 42.827 | 88.798 | no | 17 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | normal | iid | Seasonal Naive | 12.542 | 1 | 0.000 | 0.000 | sí | 17 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | normal | iid | Chronos | 34.657 | 4 | 13.706 | 30.490 | no | 17 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | normal | iid | SARIMA | 15.905 | 3 | -2.911 | 10.320 | sí | 17 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | normal | iid | SARIMA-sel | 14.050 | 2 | -3.872 | 7.212 | sí | 17 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | normal | iid | Ridge | 48.327 | 6 | 18.563 | 57.380 | no | 17 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | normal | iid | ElasticNet | 47.881 | 5 | 18.129 | 56.496 | no | 17 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | normal | iid | XGB-37 | 51.656 | 7 | 24.064 | 54.496 | no | 17 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | normal | iid | GC3 | 57.546 | 8 | 28.122 | 64.372 | no | 17 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | normal | iid | GE | 58.063 | 9 | 29.515 | 63.679 | no | 17 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | normal | bloques | Naive | 77.560 | 10 | 44.513 | 86.385 | no | 17 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | normal | bloques | Seasonal Naive | 12.542 | 1 | 0.000 | 0.000 | sí | 17 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | normal | bloques | Chronos | 34.657 | 4 | 13.690 | 29.751 | no | 17 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | normal | bloques | SARIMA | 15.905 | 3 | -3.593 | 10.849 | sí | 17 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | normal | bloques | SARIMA-sel | 14.050 | 2 | -4.417 | 7.686 | sí | 17 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | normal | bloques | Ridge | 48.327 | 6 | 16.697 | 58.652 | no | 17 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | normal | bloques | ElasticNet | 47.881 | 5 | 16.560 | 57.305 | no | 17 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | normal | bloques | XGB-37 | 51.656 | 7 | 23.766 | 54.199 | no | 17 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | normal | bloques | GC3 | 57.546 | 8 | 25.325 | 67.009 | no | 17 |
| sensibilidad_2023_2025 | dulce | interanual | 50 | normal | bloques | GE | 58.063 | 9 | 26.871 | 66.292 | no | 17 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | shock | iid | Naive | 87.562 | 10 | 27.759 | 87.785 | no | 16 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | shock | iid | Seasonal Naive | 44.546 | 4 | 7.204 | 21.642 | no | 16 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | shock | iid | Chronos | 35.182 | 3 | -8.881 | 18.722 | sí | 16 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | shock | iid | SARIMA | 29.944 | 2 | -1.224 | 1.509 | sí | 16 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | shock | iid | SARIMA-sel | 29.628 | 1 | 0.000 | 0.000 | sí | 16 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | shock | iid | Ridge | 83.977 | 9 | 31.567 | 76.591 | no | 16 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | shock | iid | ElasticNet | 74.387 | 6 | 21.600 | 67.779 | no | 16 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | shock | iid | XGB-37 | 57.757 | 5 | 6.401 | 49.845 | no | 16 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | shock | iid | GC3 | 79.502 | 8 | 26.628 | 71.913 | no | 16 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | shock | iid | GE | 75.704 | 7 | 24.356 | 66.489 | no | 16 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | shock | bloques | Naive | 87.562 | 10 | 35.983 | 81.287 | no | 16 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | shock | bloques | Seasonal Naive | 44.546 | 4 | 7.831 | 22.431 | no | 16 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | shock | bloques | Chronos | 35.182 | 3 | -6.143 | 19.932 | sí | 16 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | shock | bloques | SARIMA | 29.944 | 2 | -0.778 | 1.228 | sí | 16 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | shock | bloques | SARIMA-sel | 29.628 | 1 | 0.000 | 0.000 | sí | 16 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | shock | bloques | Ridge | 83.977 | 9 | 33.290 | 79.862 | no | 16 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | shock | bloques | ElasticNet | 74.387 | 6 | 23.106 | 72.694 | no | 16 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | shock | bloques | XGB-37 | 57.757 | 5 | 5.401 | 55.200 | no | 16 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | shock | bloques | GC3 | 79.502 | 8 | 25.693 | 76.883 | no | 16 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | shock | bloques | GE | 75.704 | 7 | 24.987 | 70.212 | no | 16 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | normal | iid | Naive | 77.835 | 10 | 42.682 | 86.492 | no | 20 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | normal | iid | Seasonal Naive | 14.870 | 2 | -4.631 | 6.025 | sí | 20 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | normal | iid | Chronos | 34.782 | 4 | 10.863 | 30.395 | no | 20 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | normal | iid | SARIMA | 15.653 | 3 | 0.631 | 2.953 | no | 20 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | normal | iid | SARIMA-sel | 13.983 | 1 | 0.000 | 0.000 | sí | 20 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | normal | iid | Ridge | 47.961 | 6 | 16.953 | 54.009 | no | 20 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | normal | iid | ElasticNet | 47.581 | 5 | 16.533 | 53.263 | no | 20 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | normal | iid | XGB-37 | 51.724 | 7 | 20.240 | 55.111 | no | 20 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | normal | iid | GC3 | 62.193 | 8 | 26.920 | 70.459 | no | 20 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | normal | iid | GE | 62.480 | 9 | 27.889 | 69.718 | no | 20 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | normal | bloques | Naive | 77.835 | 10 | 43.454 | 85.662 | no | 20 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | normal | bloques | Seasonal Naive | 14.870 | 2 | -5.675 | 6.976 | sí | 20 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | normal | bloques | Chronos | 34.782 | 4 | 10.128 | 30.641 | no | 20 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | normal | bloques | SARIMA | 15.653 | 3 | 0.625 | 2.940 | no | 20 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | normal | bloques | SARIMA-sel | 13.983 | 1 | 0.000 | 0.000 | sí | 20 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | normal | bloques | Ridge | 47.961 | 6 | 12.931 | 56.913 | no | 20 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | normal | bloques | ElasticNet | 47.581 | 5 | 13.176 | 55.704 | no | 20 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | normal | bloques | XGB-37 | 51.724 | 7 | 19.024 | 56.271 | no | 20 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | normal | bloques | GC3 | 62.193 | 8 | 21.546 | 77.017 | no | 20 |
| sensibilidad_2023_2025 | dulce | interanual | 60 | normal | bloques | GE | 62.480 | 9 | 23.073 | 76.001 | no | 20 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | shock | iid | Naive | 92.579 | 10 | 26.735 | 99.407 | no | 12 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | shock | iid | Seasonal Naive | 46.343 | 4 | 7.117 | 25.624 | no | 12 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | shock | iid | Chronos | 38.000 | 3 | -7.653 | 23.740 | sí | 12 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | shock | iid | SARIMA | 29.420 | 1 | 0.000 | 0.000 | sí | 12 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | shock | iid | SARIMA-sel | 29.695 | 2 | -1.223 | 2.213 | sí | 12 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | shock | iid | Ridge | 80.446 | 9 | 26.703 | 75.668 | no | 12 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | shock | iid | ElasticNet | 68.263 | 7 | 14.106 | 64.789 | no | 12 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | shock | iid | XGB-37 | 47.281 | 5 | -0.264 | 35.480 | sí | 12 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | shock | iid | GC3 | 68.696 | 8 | 17.394 | 60.996 | no | 12 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | shock | iid | GE | 67.379 | 6 | 16.281 | 59.006 | no | 12 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | shock | bloques | Naive | 92.579 | 10 | 38.102 | 95.875 | no | 12 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | shock | bloques | Seasonal Naive | 46.343 | 4 | 8.857 | 26.318 | no | 12 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | shock | bloques | Chronos | 38.000 | 3 | -4.815 | 28.725 | sí | 12 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | shock | bloques | SARIMA | 29.420 | 1 | 0.000 | 0.000 | sí | 12 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | shock | bloques | SARIMA-sel | 29.695 | 2 | -0.848 | 1.540 | sí | 12 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | shock | bloques | Ridge | 80.446 | 9 | 29.830 | 88.847 | no | 12 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | shock | bloques | ElasticNet | 68.263 | 7 | 19.118 | 78.162 | no | 12 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | shock | bloques | XGB-37 | 47.281 | 5 | 1.152 | 44.513 | no | 12 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | shock | bloques | GC3 | 68.696 | 8 | 18.892 | 65.606 | no | 12 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | shock | bloques | GE | 67.379 | 6 | 20.299 | 62.117 | no | 12 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | normal | iid | Naive | 76.947 | 10 | 41.035 | 80.919 | no | 24 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | normal | iid | Seasonal Naive | 18.917 | 3 | -2.349 | 6.737 | sí | 24 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | normal | iid | Chronos | 33.440 | 4 | 7.427 | 26.358 | no | 24 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | normal | iid | SARIMA | 18.296 | 2 | 0.809 | 2.838 | no | 24 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | normal | iid | SARIMA-sel | 16.557 | 1 | 0.000 | 0.000 | sí | 24 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | normal | iid | Ridge | 55.729 | 6 | 23.986 | 56.424 | no | 24 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | normal | iid | ElasticNet | 55.111 | 5 | 23.504 | 55.384 | no | 24 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | normal | iid | XGB-37 | 57.967 | 7 | 25.803 | 57.673 | no | 24 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | normal | iid | GC3 | 70.480 | 9 | 34.084 | 74.010 | no | 24 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | normal | iid | GE | 68.847 | 8 | 33.299 | 71.788 | no | 24 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | normal | bloques | Naive | 76.947 | 10 | 39.544 | 82.212 | no | 24 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | normal | bloques | Seasonal Naive | 18.917 | 3 | -4.384 | 7.978 | sí | 24 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | normal | bloques | Chronos | 33.440 | 4 | 5.887 | 26.795 | no | 24 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | normal | bloques | SARIMA | 18.296 | 2 | 0.871 | 2.910 | no | 24 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | normal | bloques | SARIMA-sel | 16.557 | 1 | 0.000 | 0.000 | sí | 24 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | normal | bloques | Ridge | 55.729 | 6 | 17.476 | 58.898 | no | 24 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | normal | bloques | ElasticNet | 55.111 | 5 | 17.120 | 57.552 | no | 24 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | normal | bloques | XGB-37 | 57.967 | 7 | 20.610 | 60.102 | no | 24 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | normal | bloques | GC3 | 70.480 | 9 | 23.219 | 82.959 | no | 24 |
| sensibilidad_2023_2025 | dulce | interanual | 75 | normal | bloques | GE | 68.847 | 8 | 24.205 | 79.879 | no | 24 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | shock | iid | Naive | 57.054 | 3 | -23.590 | 55.135 | sí | 3 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | shock | iid | Seasonal Naive | 80.953 | 10 | 28.647 | 50.698 | no | 3 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | shock | iid | Chronos | 41.281 | 1 | 0.000 | 0.000 | sí | 3 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | shock | iid | SARIMA | 67.134 | 5 | 11.927 | 39.778 | no | 3 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | shock | iid | SARIMA-sel | 67.576 | 6 | 12.954 | 39.636 | no | 3 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | shock | iid | Ridge | 68.236 | 7 | 17.839 | 36.070 | no | 3 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | shock | iid | ElasticNet | 58.075 | 4 | 7.077 | 26.510 | no | 3 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | shock | iid | XGB-37 | 55.870 | 2 | -8.640 | 37.819 | sí | 3 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | shock | iid | GC3 | 80.155 | 9 | 33.830 | 43.918 | no | 3 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | shock | iid | GE | 71.324 | 8 | 25.114 | 34.971 | no | 3 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | shock | bloques | Naive | 57.054 | 3 | -45.510 | 72.577 | sí | 3 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | shock | bloques | Seasonal Naive | 80.953 | 10 | 20.710 | 53.786 | no | 3 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | shock | bloques | Chronos | 41.281 | 1 | 0.000 | 0.000 | sí | 3 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | shock | bloques | SARIMA | 67.134 | 5 | -14.888 | 65.556 | sí | 3 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | shock | bloques | SARIMA-sel | 67.576 | 6 | -14.766 | 68.393 | sí | 3 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | shock | bloques | Ridge | 68.236 | 7 | 0.649 | 53.781 | no | 3 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | shock | bloques | ElasticNet | 58.075 | 4 | -4.399 | 41.965 | sí | 3 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | shock | bloques | XGB-37 | 55.870 | 2 | -12.852 | 56.837 | sí | 3 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | shock | bloques | GC3 | 80.155 | 9 | 32.642 | 47.773 | no | 3 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | shock | bloques | GE | 71.324 | 8 | 20.460 | 35.245 | no | 3 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | normal | iid | Naive | 84.440 | 10 | 50.338 | 85.568 | no | 33 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | normal | iid | Seasonal Naive | 23.251 | 3 | 2.274 | 10.536 | no | 33 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | normal | iid | Chronos | 34.385 | 4 | 10.013 | 25.268 | no | 33 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | normal | iid | SARIMA | 17.902 | 2 | 0.245 | 2.200 | no | 33 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | normal | iid | SARIMA-sel | 16.696 | 1 | 0.000 | 0.000 | sí | 33 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | normal | iid | Ridge | 63.580 | 7 | 33.534 | 60.938 | no | 33 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | normal | iid | ElasticNet | 59.624 | 6 | 29.390 | 57.171 | no | 33 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | normal | iid | XGB-37 | 54.272 | 5 | 23.914 | 51.221 | no | 33 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | normal | iid | GC3 | 68.952 | 9 | 36.538 | 67.959 | no | 33 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | normal | iid | GE | 68.088 | 8 | 36.326 | 66.398 | no | 33 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | normal | bloques | Naive | 84.440 | 10 | 51.253 | 84.909 | no | 33 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | normal | bloques | Seasonal Naive | 23.251 | 3 | 1.126 | 11.375 | no | 33 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | normal | bloques | Chronos | 34.385 | 4 | 8.713 | 26.218 | no | 33 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | normal | bloques | SARIMA | 17.902 | 2 | 0.439 | 2.117 | no | 33 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | normal | bloques | SARIMA-sel | 16.696 | 1 | 0.000 | 0.000 | sí | 33 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | normal | bloques | Ridge | 63.580 | 7 | 30.426 | 63.245 | no | 33 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | normal | bloques | ElasticNet | 59.624 | 6 | 26.073 | 59.695 | no | 33 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | normal | bloques | XGB-37 | 54.272 | 5 | 21.298 | 53.211 | no | 33 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | normal | bloques | GC3 | 68.952 | 9 | 28.467 | 75.398 | no | 33 |
| sensibilidad_2023_2025 | dulce | interanual | 90 | normal | bloques | GE | 68.088 | 8 | 29.610 | 73.034 | no | 33 |

### T09_diebold_mariano_hln.csv — T09 completa: DM-HLN por pares, con Holm exploratorio

`06_metricas/significancia/T09_diebold_mariano_hln.csv` — 360 filas × 12 columnas.

| conjunto | cultivar | alcance | modelo_A | modelo_B | n | d_media | DM | HLN | p | p_holm_exploratorio | n_pares_familia_holm |
|---|---|---|---|---|---|---|---|---|---|---|---|
| principal_2021_2025 | sutil | global | Naive | Seasonal Naive | 60 | -2,450.815 | -3.519 | -3.490 | 0.001 | 0.029 | 45 |
| principal_2021_2025 | sutil | global | Naive | Chronos | 60 | 975.524 | 3.150 | 3.123 | 0.003 | 0.075 | 45 |
| principal_2021_2025 | sutil | global | Naive | SARIMA | 60 | 263.283 | 0.609 | 0.604 | 0.548 | 1.000 | 45 |
| principal_2021_2025 | sutil | global | Naive | SARIMA-sel | 60 | 418.194 | 0.882 | 0.875 | 0.385 | 1.000 | 45 |
| principal_2021_2025 | sutil | global | Naive | Ridge | 60 | -1,301.065 | -1.855 | -1.840 | 0.071 | 0.978 | 45 |
| principal_2021_2025 | sutil | global | Naive | ElasticNet | 60 | -1,247.841 | -1.886 | -1.871 | 0.066 | 0.978 | 45 |
| principal_2021_2025 | sutil | global | Naive | XGB-37 | 60 | -1,257.379 | -2.451 | -2.430 | 0.018 | 0.429 | 45 |
| principal_2021_2025 | sutil | global | Naive | GC3 | 60 | -2,737.234 | -3.947 | -3.914 | 0.000 | 0.008 | 45 |
| principal_2021_2025 | sutil | global | Naive | GE | 60 | -3,119.460 | -4.202 | -4.167 | 0.000 | 0.004 | 45 |
| principal_2021_2025 | sutil | global | Seasonal Naive | Chronos | 60 | 3,426.339 | 5.829 | 5.780 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | sutil | global | Seasonal Naive | SARIMA | 60 | 2,714.099 | 4.571 | 4.533 | 0.000 | 0.001 | 45 |
| principal_2021_2025 | sutil | global | Seasonal Naive | SARIMA-sel | 60 | 2,869.010 | 5.489 | 5.443 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | sutil | global | Seasonal Naive | Ridge | 60 | 1,149.750 | 1.367 | 1.355 | 0.180 | 1.000 | 45 |
| principal_2021_2025 | sutil | global | Seasonal Naive | ElasticNet | 60 | 1,202.975 | 1.555 | 1.542 | 0.129 | 1.000 | 45 |
| principal_2021_2025 | sutil | global | Seasonal Naive | XGB-37 | 60 | 1,193.436 | 1.910 | 1.894 | 0.063 | 0.978 | 45 |
| principal_2021_2025 | sutil | global | Seasonal Naive | GC3 | 60 | -286.419 | -0.473 | -0.469 | 0.641 | 1.000 | 45 |
| principal_2021_2025 | sutil | global | Seasonal Naive | GE | 60 | -668.644 | -0.968 | -0.960 | 0.341 | 1.000 | 45 |
| principal_2021_2025 | sutil | global | Chronos | SARIMA | 60 | -712.241 | -2.473 | -2.453 | 0.017 | 0.429 | 45 |
| principal_2021_2025 | sutil | global | Chronos | SARIMA-sel | 60 | -557.330 | -1.673 | -1.659 | 0.102 | 1.000 | 45 |
| principal_2021_2025 | sutil | global | Chronos | Ridge | 60 | -2,276.589 | -3.234 | -3.207 | 0.002 | 0.061 | 45 |
| principal_2021_2025 | sutil | global | Chronos | ElasticNet | 60 | -2,223.365 | -3.349 | -3.321 | 0.002 | 0.045 | 45 |
| principal_2021_2025 | sutil | global | Chronos | XGB-37 | 60 | -2,232.903 | -4.885 | -4.844 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | sutil | global | Chronos | GC3 | 60 | -3,712.758 | -5.692 | -5.644 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | sutil | global | Chronos | GE | 60 | -4,094.983 | -5.750 | -5.702 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | sutil | global | SARIMA | SARIMA-sel | 60 | 154.911 | 0.550 | 0.546 | 0.587 | 1.000 | 45 |
| principal_2021_2025 | sutil | global | SARIMA | Ridge | 60 | -1,564.349 | -2.236 | -2.217 | 0.030 | 0.598 | 45 |
| principal_2021_2025 | sutil | global | SARIMA | ElasticNet | 60 | -1,511.124 | -2.265 | -2.246 | 0.028 | 0.598 | 45 |
| principal_2021_2025 | sutil | global | SARIMA | XGB-37 | 60 | -1,520.663 | -3.066 | -3.041 | 0.004 | 0.091 | 45 |
| principal_2021_2025 | sutil | global | SARIMA | GC3 | 60 | -3,000.517 | -4.408 | -4.372 | 0.000 | 0.002 | 45 |
| principal_2021_2025 | sutil | global | SARIMA | GE | 60 | -3,382.743 | -4.681 | -4.642 | 0.000 | 0.001 | 45 |
| principal_2021_2025 | sutil | global | SARIMA-sel | Ridge | 60 | -1,719.260 | -2.378 | -2.358 | 0.022 | 0.478 | 45 |
| principal_2021_2025 | sutil | global | SARIMA-sel | ElasticNet | 60 | -1,666.035 | -2.457 | -2.437 | 0.018 | 0.429 | 45 |
| principal_2021_2025 | sutil | global | SARIMA-sel | XGB-37 | 60 | -1,675.573 | -3.661 | -3.630 | 0.001 | 0.019 | 45 |
| principal_2021_2025 | sutil | global | SARIMA-sel | GC3 | 60 | -3,155.428 | -5.190 | -5.147 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | sutil | global | SARIMA-sel | GE | 60 | -3,537.654 | -5.346 | -5.301 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | sutil | global | Ridge | ElasticNet | 60 | 53.225 | 0.395 | 0.392 | 0.696 | 1.000 | 45 |
| principal_2021_2025 | sutil | global | Ridge | XGB-37 | 60 | 43.686 | 0.058 | 0.057 | 0.955 | 1.000 | 45 |
| principal_2021_2025 | sutil | global | Ridge | GC3 | 60 | -1,436.169 | -1.794 | -1.779 | 0.080 | 0.978 | 45 |
| principal_2021_2025 | sutil | global | Ridge | GE | 60 | -1,818.394 | -2.069 | -2.052 | 0.045 | 0.803 | 45 |
| principal_2021_2025 | sutil | global | ElasticNet | XGB-37 | 60 | -9.538 | -0.013 | -0.013 | 0.990 | 1.000 | 45 |
| principal_2021_2025 | sutil | global | ElasticNet | GC3 | 60 | -1,489.393 | -2.013 | -1.997 | 0.050 | 0.858 | 45 |
| principal_2021_2025 | sutil | global | ElasticNet | GE | 60 | -1,871.619 | -2.247 | -2.228 | 0.030 | 0.598 | 45 |
| principal_2021_2025 | sutil | global | XGB-37 | GC3 | 60 | -1,479.855 | -3.514 | -3.485 | 0.001 | 0.029 | 45 |
| principal_2021_2025 | sutil | global | XGB-37 | GE | 60 | -1,862.080 | -4.098 | -4.064 | 0.000 | 0.005 | 45 |
| principal_2021_2025 | sutil | global | GC3 | GE | 60 | -382.225 | -1.925 | -1.909 | 0.061 | 0.978 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Naive | Seasonal Naive | 10 | 3,471.745 | 1.971 | 1.869 | 0.094 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Naive | Chronos | 10 | 3,722.673 | 8.145 | 7.727 | 0.000 | 0.001 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Naive | SARIMA | 10 | 3,375.476 | 4.780 | 4.534 | 0.001 | 0.062 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Naive | SARIMA-sel | 10 | 3,570.461 | 3.270 | 3.102 | 0.013 | 0.545 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Naive | Ridge | 10 | -50.707 | -0.021 | -0.020 | 0.984 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Naive | ElasticNet | 10 | 352.455 | 0.162 | 0.154 | 0.881 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Naive | XGB-37 | 10 | 2,550.994 | 2.452 | 2.326 | 0.045 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Naive | GC3 | 10 | 2,431.735 | 1.796 | 1.704 | 0.123 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Naive | GE | 10 | 1,679.549 | 1.269 | 1.204 | 0.259 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Seasonal Naive | Chronos | 10 | 250.927 | 0.182 | 0.173 | 0.867 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Seasonal Naive | SARIMA | 10 | -96.269 | -0.069 | -0.066 | 0.949 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Seasonal Naive | SARIMA-sel | 10 | 98.715 | 0.092 | 0.087 | 0.932 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Seasonal Naive | Ridge | 10 | -3,522.453 | -1.342 | -1.273 | 0.235 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Seasonal Naive | ElasticNet | 10 | -3,119.290 | -1.306 | -1.239 | 0.247 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Seasonal Naive | XGB-37 | 10 | -920.751 | -0.551 | -0.522 | 0.614 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Seasonal Naive | GC3 | 10 | -1,040.010 | -1.083 | -1.027 | 0.331 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Seasonal Naive | GE | 10 | -1,792.196 | -1.310 | -1.242 | 0.245 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Chronos | SARIMA | 10 | -347.196 | -0.725 | -0.688 | 0.509 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Chronos | SARIMA-sel | 10 | -152.212 | -0.182 | -0.172 | 0.867 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Chronos | Ridge | 10 | -3,773.380 | -1.681 | -1.595 | 0.145 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Chronos | ElasticNet | 10 | -3,370.218 | -1.677 | -1.591 | 0.146 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Chronos | XGB-37 | 10 | -1,171.678 | -1.181 | -1.120 | 0.292 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Chronos | GC3 | 10 | -1,290.937 | -1.280 | -1.215 | 0.255 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Chronos | GE | 10 | -2,043.124 | -1.876 | -1.779 | 0.109 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | SARIMA | SARIMA-sel | 10 | 194.984 | 0.266 | 0.252 | 0.807 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | SARIMA | Ridge | 10 | -3,426.184 | -1.651 | -1.566 | 0.152 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | SARIMA | ElasticNet | 10 | -3,023.022 | -1.652 | -1.567 | 0.151 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | SARIMA | XGB-37 | 10 | -824.482 | -0.814 | -0.772 | 0.460 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | SARIMA | GC3 | 10 | -943.741 | -0.877 | -0.832 | 0.427 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | SARIMA | GE | 10 | -1,695.928 | -1.547 | -1.467 | 0.176 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | SARIMA-sel | Ridge | 10 | -3,621.168 | -1.632 | -1.548 | 0.156 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | SARIMA-sel | ElasticNet | 10 | -3,218.006 | -1.629 | -1.545 | 0.157 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | SARIMA-sel | XGB-37 | 10 | -1,019.466 | -1.021 | -0.969 | 0.358 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | SARIMA-sel | GC3 | 10 | -1,138.725 | -1.318 | -1.250 | 0.243 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | SARIMA-sel | GE | 10 | -1,890.912 | -2.002 | -1.899 | 0.090 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Ridge | ElasticNet | 10 | 403.162 | 0.919 | 0.872 | 0.406 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Ridge | XGB-37 | 10 | 2,601.702 | 1.078 | 1.023 | 0.333 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Ridge | GC3 | 10 | 2,482.443 | 1.053 | 0.999 | 0.344 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | Ridge | GE | 10 | 1,730.256 | 0.698 | 0.662 | 0.525 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | ElasticNet | XGB-37 | 10 | 2,198.539 | 0.954 | 0.905 | 0.389 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | ElasticNet | GC3 | 10 | 2,079.281 | 0.969 | 0.919 | 0.382 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | ElasticNet | GE | 10 | 1,327.094 | 0.576 | 0.547 | 0.598 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | XGB-37 | GC3 | 10 | -119.259 | -0.111 | -0.105 | 0.919 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | XGB-37 | GE | 10 | -871.445 | -1.157 | -1.098 | 0.301 | 1.000 | 45 |
| principal_2021_2025 | sutil | shock_P75_mensual | GC3 | GE | 10 | -752.187 | -1.374 | -1.303 | 0.225 | 1.000 | 45 |
| principal_2021_2025 | dulce | global | Naive | Seasonal Naive | 60 | 53.019 | 7.976 | 7.910 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | global | Naive | Chronos | 60 | 46.704 | 9.333 | 9.255 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | global | Naive | SARIMA | 60 | 59.110 | 8.687 | 8.614 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | global | Naive | SARIMA-sel | 60 | 56.894 | 8.300 | 8.231 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | global | Naive | Ridge | 60 | 24.453 | 3.388 | 3.360 | 0.001 | 0.025 | 45 |
| principal_2021_2025 | dulce | global | Naive | ElasticNet | 60 | 27.274 | 3.880 | 3.848 | 0.000 | 0.006 | 45 |
| principal_2021_2025 | dulce | global | Naive | XGB-37 | 60 | 29.262 | 4.285 | 4.249 | 0.000 | 0.002 | 45 |
| principal_2021_2025 | dulce | global | Naive | GC3 | 60 | 20.853 | 2.591 | 2.569 | 0.013 | 0.166 | 45 |
| principal_2021_2025 | dulce | global | Naive | GE | 60 | 20.788 | 2.621 | 2.599 | 0.012 | 0.165 | 45 |
| principal_2021_2025 | dulce | global | Seasonal Naive | Chronos | 60 | -6.316 | -1.983 | -1.966 | 0.054 | 0.648 | 45 |
| principal_2021_2025 | dulce | global | Seasonal Naive | SARIMA | 60 | 6.091 | 3.011 | 2.986 | 0.004 | 0.070 | 45 |
| principal_2021_2025 | dulce | global | Seasonal Naive | SARIMA-sel | 60 | 3.874 | 1.588 | 1.574 | 0.121 | 1.000 | 45 |
| principal_2021_2025 | dulce | global | Seasonal Naive | Ridge | 60 | -28.567 | -5.572 | -5.525 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | global | Seasonal Naive | ElasticNet | 60 | -25.745 | -5.229 | -5.185 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | global | Seasonal Naive | XGB-37 | 60 | -23.757 | -5.307 | -5.262 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | global | Seasonal Naive | GC3 | 60 | -32.166 | -6.360 | -6.307 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | global | Seasonal Naive | GE | 60 | -32.231 | -6.733 | -6.677 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | global | Chronos | SARIMA | 60 | 12.407 | 3.785 | 3.753 | 0.000 | 0.008 | 45 |
| principal_2021_2025 | dulce | global | Chronos | SARIMA-sel | 60 | 10.190 | 2.946 | 2.921 | 0.005 | 0.079 | 45 |
| principal_2021_2025 | dulce | global | Chronos | Ridge | 60 | -22.251 | -4.337 | -4.300 | 0.000 | 0.001 | 45 |
| principal_2021_2025 | dulce | global | Chronos | ElasticNet | 60 | -19.429 | -4.067 | -4.033 | 0.000 | 0.003 | 45 |
| principal_2021_2025 | dulce | global | Chronos | XGB-37 | 60 | -17.442 | -4.545 | -4.507 | 0.000 | 0.001 | 45 |
| principal_2021_2025 | dulce | global | Chronos | GC3 | 60 | -25.851 | -4.532 | -4.494 | 0.000 | 0.001 | 45 |
| principal_2021_2025 | dulce | global | Chronos | GE | 60 | -25.916 | -4.842 | -4.801 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | global | SARIMA | SARIMA-sel | 60 | -2.217 | -1.298 | -1.287 | 0.203 | 1.000 | 45 |
| principal_2021_2025 | dulce | global | SARIMA | Ridge | 60 | -34.658 | -6.113 | -6.062 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | global | SARIMA | ElasticNet | 60 | -31.836 | -5.876 | -5.827 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | global | SARIMA | XGB-37 | 60 | -29.848 | -5.970 | -5.920 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | global | SARIMA | GC3 | 60 | -38.257 | -6.293 | -6.240 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | global | SARIMA | GE | 60 | -38.322 | -6.693 | -6.637 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | global | SARIMA-sel | Ridge | 60 | -32.441 | -5.461 | -5.415 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | global | SARIMA-sel | ElasticNet | 60 | -29.619 | -5.224 | -5.180 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | global | SARIMA-sel | XGB-37 | 60 | -27.632 | -5.200 | -5.156 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | global | SARIMA-sel | GC3 | 60 | -36.041 | -5.631 | -5.584 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | global | SARIMA-sel | GE | 60 | -36.106 | -5.968 | -5.919 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | global | Ridge | ElasticNet | 60 | 2.822 | 2.737 | 2.714 | 0.009 | 0.130 | 45 |
| principal_2021_2025 | dulce | global | Ridge | XGB-37 | 60 | 4.809 | 0.898 | 0.890 | 0.377 | 1.000 | 45 |
| principal_2021_2025 | dulce | global | Ridge | GC3 | 60 | -3.600 | -0.632 | -0.627 | 0.533 | 1.000 | 45 |
| principal_2021_2025 | dulce | global | Ridge | GE | 60 | -3.665 | -0.672 | -0.666 | 0.508 | 1.000 | 45 |
| principal_2021_2025 | dulce | global | ElasticNet | XGB-37 | 60 | 1.988 | 0.400 | 0.397 | 0.693 | 1.000 | 45 |
| principal_2021_2025 | dulce | global | ElasticNet | GC3 | 60 | -6.421 | -1.192 | -1.182 | 0.242 | 1.000 | 45 |
| principal_2021_2025 | dulce | global | ElasticNet | GE | 60 | -6.486 | -1.262 | -1.252 | 0.216 | 1.000 | 45 |
| principal_2021_2025 | dulce | global | XGB-37 | GC3 | 60 | -8.409 | -1.828 | -1.813 | 0.075 | 0.750 | 45 |
| principal_2021_2025 | dulce | global | XGB-37 | GE | 60 | -8.474 | -1.923 | -1.907 | 0.061 | 0.676 | 45 |
| principal_2021_2025 | dulce | global | GC3 | GE | 60 | -0.065 | -0.058 | -0.058 | 0.954 | 1.000 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Naive | Seasonal Naive | 15 | 107.119 | 13.557 | 13.097 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Naive | Chronos | 15 | 83.423 | 12.615 | 12.187 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Naive | SARIMA | 15 | 117.644 | 14.660 | 14.163 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Naive | SARIMA-sel | 15 | 111.931 | 12.526 | 12.101 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Naive | Ridge | 15 | 61.928 | 7.523 | 7.268 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Naive | ElasticNet | 15 | 64.392 | 8.243 | 7.964 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Naive | XGB-37 | 15 | 65.773 | 7.015 | 6.777 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Naive | GC3 | 15 | 70.874 | 8.794 | 8.496 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Naive | GE | 15 | 73.739 | 11.799 | 11.399 | 0.000 | 0.000 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Seasonal Naive | Chronos | 15 | -23.696 | -5.325 | -5.145 | 0.000 | 0.005 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Seasonal Naive | SARIMA | 15 | 10.525 | 4.577 | 4.422 | 0.001 | 0.018 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Seasonal Naive | SARIMA-sel | 15 | 4.812 | 1.278 | 1.235 | 0.237 | 1.000 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Seasonal Naive | Ridge | 15 | -45.191 | -4.340 | -4.192 | 0.001 | 0.025 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Seasonal Naive | ElasticNet | 15 | -42.727 | -4.252 | -4.108 | 0.001 | 0.029 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Seasonal Naive | XGB-37 | 15 | -41.347 | -4.590 | -4.434 | 0.001 | 0.018 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Seasonal Naive | GC3 | 15 | -36.245 | -3.521 | -3.402 | 0.004 | 0.090 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Seasonal Naive | GE | 15 | -33.380 | -3.452 | -3.335 | 0.005 | 0.093 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Chronos | SARIMA | 15 | 34.221 | 6.646 | 6.420 | 0.000 | 0.001 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Chronos | SARIMA-sel | 15 | 28.508 | 4.163 | 4.022 | 0.001 | 0.029 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Chronos | Ridge | 15 | -21.495 | -2.486 | -2.401 | 0.031 | 0.493 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Chronos | ElasticNet | 15 | -19.031 | -2.371 | -2.291 | 0.038 | 0.570 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Chronos | XGB-37 | 15 | -17.650 | -2.624 | -2.535 | 0.024 | 0.404 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Chronos | GC3 | 15 | -12.549 | -1.449 | -1.400 | 0.183 | 1.000 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Chronos | GE | 15 | -9.684 | -1.287 | -1.243 | 0.234 | 1.000 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | SARIMA | SARIMA-sel | 15 | -5.713 | -1.740 | -1.681 | 0.115 | 1.000 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | SARIMA | Ridge | 15 | -55.716 | -5.130 | -4.957 | 0.000 | 0.007 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | SARIMA | ElasticNet | 15 | -53.252 | -4.970 | -4.802 | 0.000 | 0.009 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | SARIMA | XGB-37 | 15 | -51.871 | -5.558 | -5.369 | 0.000 | 0.003 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | SARIMA | GC3 | 15 | -46.770 | -4.247 | -4.103 | 0.001 | 0.029 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | SARIMA | GE | 15 | -43.905 | -4.238 | -4.094 | 0.001 | 0.029 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | SARIMA-sel | Ridge | 15 | -50.003 | -4.187 | -4.045 | 0.001 | 0.029 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | SARIMA-sel | ElasticNet | 15 | -47.539 | -4.077 | -3.938 | 0.001 | 0.033 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | SARIMA-sel | XGB-37 | 15 | -46.158 | -4.360 | -4.213 | 0.001 | 0.025 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | SARIMA-sel | GC3 | 15 | -41.057 | -3.493 | -3.374 | 0.005 | 0.091 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | SARIMA-sel | GE | 15 | -38.192 | -3.449 | -3.332 | 0.005 | 0.093 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Ridge | ElasticNet | 15 | 2.464 | 1.189 | 1.149 | 0.270 | 1.000 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Ridge | XGB-37 | 15 | 3.845 | 0.313 | 0.302 | 0.767 | 1.000 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Ridge | GC3 | 15 | 8.946 | 0.924 | 0.893 | 0.387 | 1.000 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | Ridge | GE | 15 | 11.811 | 1.381 | 1.334 | 0.204 | 1.000 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | ElasticNet | XGB-37 | 15 | 1.380 | 0.123 | 0.119 | 0.907 | 1.000 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | ElasticNet | GC3 | 15 | 6.482 | 0.723 | 0.698 | 0.496 | 1.000 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | ElasticNet | GE | 15 | 9.347 | 1.184 | 1.144 | 0.272 | 1.000 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | XGB-37 | GC3 | 15 | 5.101 | 0.488 | 0.472 | 0.644 | 1.000 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | XGB-37 | GE | 15 | 7.966 | 0.807 | 0.780 | 0.449 | 1.000 | 45 |
| principal_2021_2025 | dulce | shock_P75_mensual | GC3 | GE | 15 | 2.865 | 1.022 | 0.987 | 0.340 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | global | Naive | Seasonal Naive | 36 | -3,091.876 | -3.004 | -2.962 | 0.005 | 0.153 | 45 |
| sensibilidad_2023_2025 | sutil | global | Naive | Chronos | 36 | 1,291.746 | 3.208 | 3.163 | 0.003 | 0.097 | 45 |
| sensibilidad_2023_2025 | sutil | global | Naive | SARIMA | 36 | 612.296 | 1.170 | 1.154 | 0.256 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | global | Naive | SARIMA-sel | 36 | 418.865 | 0.651 | 0.642 | 0.525 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | global | Naive | Ridge | 36 | -1,986.286 | -1.866 | -1.840 | 0.074 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | global | Naive | ElasticNet | 36 | -2,004.630 | -2.015 | -1.987 | 0.055 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | global | Naive | XGB-37 | 36 | -757.447 | -1.150 | -1.134 | 0.264 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | global | Naive | GC3 | 36 | -3,472.175 | -3.398 | -3.350 | 0.002 | 0.064 | 45 |
| sensibilidad_2023_2025 | sutil | global | Naive | GE | 36 | -4,072.948 | -3.761 | -3.708 | 0.001 | 0.024 | 45 |
| sensibilidad_2023_2025 | sutil | global | Seasonal Naive | Chronos | 36 | 4,383.622 | 4.941 | 4.872 | 0.000 | 0.001 | 45 |
| sensibilidad_2023_2025 | sutil | global | Seasonal Naive | SARIMA | 36 | 3,704.172 | 4.150 | 4.092 | 0.000 | 0.009 | 45 |
| sensibilidad_2023_2025 | sutil | global | Seasonal Naive | SARIMA-sel | 36 | 3,510.741 | 4.530 | 4.466 | 0.000 | 0.003 | 45 |
| sensibilidad_2023_2025 | sutil | global | Seasonal Naive | Ridge | 36 | 1,105.590 | 0.808 | 0.797 | 0.431 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | global | Seasonal Naive | ElasticNet | 36 | 1,087.246 | 0.865 | 0.853 | 0.399 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | global | Seasonal Naive | XGB-37 | 36 | 2,334.429 | 2.498 | 2.464 | 0.019 | 0.489 | 45 |
| sensibilidad_2023_2025 | sutil | global | Seasonal Naive | GC3 | 36 | -380.299 | -0.402 | -0.396 | 0.694 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | global | Seasonal Naive | GE | 36 | -981.072 | -0.906 | -0.893 | 0.378 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | global | Chronos | SARIMA | 36 | -679.450 | -1.725 | -1.701 | 0.098 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | global | Chronos | SARIMA-sel | 36 | -872.881 | -1.847 | -1.821 | 0.077 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | global | Chronos | Ridge | 36 | -3,278.032 | -3.019 | -2.976 | 0.005 | 0.153 | 45 |
| sensibilidad_2023_2025 | sutil | global | Chronos | ElasticNet | 36 | -3,296.376 | -3.247 | -3.202 | 0.003 | 0.090 | 45 |
| sensibilidad_2023_2025 | sutil | global | Chronos | XGB-37 | 36 | -2,049.194 | -3.313 | -3.267 | 0.002 | 0.078 | 45 |
| sensibilidad_2023_2025 | sutil | global | Chronos | GC3 | 36 | -4,763.921 | -4.996 | -4.926 | 0.000 | 0.001 | 45 |
| sensibilidad_2023_2025 | sutil | global | Chronos | GE | 36 | -5,364.694 | -5.224 | -5.151 | 0.000 | 0.000 | 45 |
| sensibilidad_2023_2025 | sutil | global | SARIMA | SARIMA-sel | 36 | -193.431 | -0.483 | -0.476 | 0.637 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | global | SARIMA | Ridge | 36 | -2,598.582 | -2.463 | -2.429 | 0.020 | 0.511 | 45 |
| sensibilidad_2023_2025 | sutil | global | SARIMA | ElasticNet | 36 | -2,616.927 | -2.632 | -2.596 | 0.014 | 0.370 | 45 |
| sensibilidad_2023_2025 | sutil | global | SARIMA | XGB-37 | 36 | -1,369.744 | -2.039 | -2.010 | 0.052 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | global | SARIMA | GC3 | 36 | -4,084.471 | -4.097 | -4.040 | 0.000 | 0.010 | 45 |
| sensibilidad_2023_2025 | sutil | global | SARIMA | GE | 36 | -4,685.244 | -4.528 | -4.465 | 0.000 | 0.003 | 45 |
| sensibilidad_2023_2025 | sutil | global | SARIMA-sel | Ridge | 36 | -2,405.151 | -2.131 | -2.101 | 0.043 | 0.987 | 45 |
| sensibilidad_2023_2025 | sutil | global | SARIMA-sel | ElasticNet | 36 | -2,423.496 | -2.308 | -2.276 | 0.029 | 0.698 | 45 |
| sensibilidad_2023_2025 | sutil | global | SARIMA-sel | XGB-37 | 36 | -1,176.313 | -2.101 | -2.071 | 0.046 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | global | SARIMA-sel | GC3 | 36 | -3,891.040 | -4.538 | -4.474 | 0.000 | 0.003 | 45 |
| sensibilidad_2023_2025 | sutil | global | SARIMA-sel | GE | 36 | -4,491.813 | -4.866 | -4.798 | 0.000 | 0.001 | 45 |
| sensibilidad_2023_2025 | sutil | global | Ridge | ElasticNet | 36 | -18.345 | -0.087 | -0.086 | 0.932 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | global | Ridge | XGB-37 | 36 | 1,228.838 | 1.028 | 1.014 | 0.318 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | global | Ridge | GC3 | 36 | -1,485.889 | -1.145 | -1.129 | 0.267 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | global | Ridge | GE | 36 | -2,086.662 | -1.462 | -1.441 | 0.158 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | global | ElasticNet | XGB-37 | 36 | 1,247.183 | 1.110 | 1.094 | 0.281 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | global | ElasticNet | GC3 | 36 | -1,467.544 | -1.224 | -1.207 | 0.236 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | global | ElasticNet | GE | 36 | -2,068.318 | -1.529 | -1.507 | 0.141 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | global | XGB-37 | GC3 | 36 | -2,714.727 | -4.724 | -4.658 | 0.000 | 0.002 | 45 |
| sensibilidad_2023_2025 | sutil | global | XGB-37 | GE | 36 | -3,315.501 | -5.421 | -5.345 | 0.000 | 0.000 | 45 |
| sensibilidad_2023_2025 | sutil | global | GC3 | GE | 36 | -600.773 | -1.963 | -1.936 | 0.061 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Naive | Seasonal Naive | 7 | 3,223.685 | 1.310 | 1.213 | 0.271 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Naive | Chronos | 7 | 3,745.223 | 5.971 | 5.528 | 0.001 | 0.066 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Naive | SARIMA | 7 | 2,843.339 | 3.972 | 3.677 | 0.010 | 0.456 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Naive | SARIMA-sel | 7 | 3,251.126 | 2.489 | 2.305 | 0.061 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Naive | Ridge | 7 | -1,841.695 | -0.591 | -0.547 | 0.604 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Naive | ElasticNet | 7 | -1,428.308 | -0.515 | -0.476 | 0.651 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Naive | XGB-37 | 7 | 2,234.967 | 1.687 | 1.562 | 0.169 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Naive | GC3 | 7 | 1,928.353 | 1.079 | 0.999 | 0.356 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Naive | GE | 7 | 976.317 | 0.603 | 0.558 | 0.597 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Seasonal Naive | Chronos | 7 | 521.538 | 0.270 | 0.250 | 0.811 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Seasonal Naive | SARIMA | 7 | -380.346 | -0.192 | -0.178 | 0.864 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Seasonal Naive | SARIMA-sel | 7 | 27.441 | 0.019 | 0.017 | 0.987 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Seasonal Naive | Ridge | 7 | -5,065.380 | -1.412 | -1.308 | 0.239 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Seasonal Naive | ElasticNet | 7 | -4,651.993 | -1.438 | -1.331 | 0.231 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Seasonal Naive | XGB-37 | 7 | -988.718 | -0.419 | -0.388 | 0.711 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Seasonal Naive | GC3 | 7 | -1,295.332 | -0.958 | -0.887 | 0.409 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Seasonal Naive | GE | 7 | -2,247.368 | -1.190 | -1.102 | 0.313 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Chronos | SARIMA | 7 | -901.884 | -2.450 | -2.268 | 0.064 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Chronos | SARIMA-sel | 7 | -494.097 | -0.507 | -0.469 | 0.655 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Chronos | Ridge | 7 | -5,586.918 | -1.918 | -1.776 | 0.126 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Chronos | ElasticNet | 7 | -5,173.531 | -2.036 | -1.885 | 0.108 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Chronos | XGB-37 | 7 | -1,510.256 | -1.154 | -1.068 | 0.327 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Chronos | GC3 | 7 | -1,816.870 | -1.386 | -1.283 | 0.247 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Chronos | GE | 7 | -2,768.906 | -2.112 | -1.956 | 0.098 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | SARIMA | SARIMA-sel | 7 | 407.787 | 0.423 | 0.391 | 0.709 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | SARIMA | Ridge | 7 | -4,685.034 | -1.660 | -1.537 | 0.175 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | SARIMA | ElasticNet | 7 | -4,271.647 | -1.739 | -1.610 | 0.158 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | SARIMA | XGB-37 | 7 | -608.372 | -0.442 | -0.409 | 0.697 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | SARIMA | GC3 | 7 | -914.986 | -0.596 | -0.551 | 0.601 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | SARIMA | GE | 7 | -1,867.022 | -1.225 | -1.134 | 0.300 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | SARIMA-sel | Ridge | 7 | -5,092.822 | -1.699 | -1.573 | 0.167 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | SARIMA-sel | ElasticNet | 7 | -4,679.434 | -1.779 | -1.647 | 0.151 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | SARIMA-sel | XGB-37 | 7 | -1,016.160 | -0.724 | -0.670 | 0.528 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | SARIMA-sel | GC3 | 7 | -1,322.774 | -1.120 | -1.037 | 0.340 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | SARIMA-sel | GE | 7 | -2,274.809 | -1.724 | -1.596 | 0.162 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Ridge | ElasticNet | 7 | 413.387 | 0.661 | 0.612 | 0.563 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Ridge | XGB-37 | 7 | 4,076.662 | 1.239 | 1.147 | 0.295 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Ridge | GC3 | 7 | 3,770.048 | 1.164 | 1.078 | 0.323 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | Ridge | GE | 7 | 2,818.013 | 0.816 | 0.755 | 0.479 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | ElasticNet | XGB-37 | 7 | 3,663.275 | 1.172 | 1.085 | 0.320 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | ElasticNet | GC3 | 7 | 3,356.661 | 1.146 | 1.061 | 0.330 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | ElasticNet | GE | 7 | 2,404.625 | 0.752 | 0.696 | 0.512 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | XGB-37 | GC3 | 7 | -306.614 | -0.207 | -0.192 | 0.854 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | XGB-37 | GE | 7 | -1,258.649 | -1.272 | -1.178 | 0.283 | 1.000 | 45 |
| sensibilidad_2023_2025 | sutil | shock_P75_mensual | GC3 | GE | 7 | -952.035 | -1.334 | -1.235 | 0.263 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | global | Naive | Seasonal Naive | 36 | 54.099 | 5.929 | 5.846 | 0.000 | 0.000 | 45 |
| sensibilidad_2023_2025 | dulce | global | Naive | Chronos | 36 | 47.198 | 6.804 | 6.709 | 0.000 | 0.000 | 45 |
| sensibilidad_2023_2025 | dulce | global | Naive | SARIMA | 36 | 60.154 | 6.482 | 6.391 | 0.000 | 0.000 | 45 |
| sensibilidad_2023_2025 | dulce | global | Naive | SARIMA-sel | 36 | 61.222 | 6.615 | 6.523 | 0.000 | 0.000 | 45 |
| sensibilidad_2023_2025 | dulce | global | Naive | Ridge | 36 | 18.190 | 1.747 | 1.722 | 0.094 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | global | Naive | ElasticNet | 36 | 22.663 | 2.213 | 2.182 | 0.036 | 0.503 | 45 |
| sensibilidad_2023_2025 | dulce | global | Naive | XGB-37 | 36 | 27.753 | 2.732 | 2.693 | 0.011 | 0.194 | 45 |
| sensibilidad_2023_2025 | dulce | global | Naive | GC3 | 36 | 12.272 | 1.062 | 1.047 | 0.302 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | global | Naive | GE | 36 | 13.800 | 1.225 | 1.208 | 0.235 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | global | Seasonal Naive | Chronos | 36 | -6.900 | -1.580 | -1.558 | 0.128 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | global | Seasonal Naive | SARIMA | 36 | 6.055 | 2.061 | 2.033 | 0.050 | 0.597 | 45 |
| sensibilidad_2023_2025 | dulce | global | Seasonal Naive | SARIMA-sel | 36 | 7.123 | 2.582 | 2.546 | 0.015 | 0.263 | 45 |
| sensibilidad_2023_2025 | dulce | global | Seasonal Naive | Ridge | 36 | -35.909 | -4.849 | -4.781 | 0.000 | 0.001 | 45 |
| sensibilidad_2023_2025 | dulce | global | Seasonal Naive | ElasticNet | 36 | -31.436 | -4.346 | -4.285 | 0.000 | 0.004 | 45 |
| sensibilidad_2023_2025 | dulce | global | Seasonal Naive | XGB-37 | 36 | -26.346 | -4.060 | -4.004 | 0.000 | 0.008 | 45 |
| sensibilidad_2023_2025 | dulce | global | Seasonal Naive | GC3 | 36 | -41.827 | -5.441 | -5.365 | 0.000 | 0.000 | 45 |
| sensibilidad_2023_2025 | dulce | global | Seasonal Naive | GE | 36 | -40.298 | -5.652 | -5.573 | 0.000 | 0.000 | 45 |
| sensibilidad_2023_2025 | dulce | global | Chronos | SARIMA | 36 | 12.955 | 2.822 | 2.782 | 0.009 | 0.169 | 45 |
| sensibilidad_2023_2025 | dulce | global | Chronos | SARIMA-sel | 36 | 14.023 | 3.115 | 3.071 | 0.004 | 0.086 | 45 |
| sensibilidad_2023_2025 | dulce | global | Chronos | Ridge | 36 | -29.008 | -3.937 | -3.882 | 0.000 | 0.011 | 45 |
| sensibilidad_2023_2025 | dulce | global | Chronos | ElasticNet | 36 | -24.535 | -3.561 | -3.511 | 0.001 | 0.029 | 45 |
| sensibilidad_2023_2025 | dulce | global | Chronos | XGB-37 | 36 | -19.446 | -3.415 | -3.367 | 0.002 | 0.041 | 45 |
| sensibilidad_2023_2025 | dulce | global | Chronos | GC3 | 36 | -34.926 | -4.170 | -4.112 | 0.000 | 0.006 | 45 |
| sensibilidad_2023_2025 | dulce | global | Chronos | GE | 36 | -33.398 | -4.339 | -4.278 | 0.000 | 0.004 | 45 |
| sensibilidad_2023_2025 | dulce | global | SARIMA | SARIMA-sel | 36 | 1.068 | 2.158 | 2.128 | 0.040 | 0.526 | 45 |
| sensibilidad_2023_2025 | dulce | global | SARIMA | Ridge | 36 | -41.964 | -5.057 | -4.987 | 0.000 | 0.001 | 45 |
| sensibilidad_2023_2025 | dulce | global | SARIMA | ElasticNet | 36 | -37.491 | -4.686 | -4.621 | 0.000 | 0.002 | 45 |
| sensibilidad_2023_2025 | dulce | global | SARIMA | XGB-37 | 36 | -32.401 | -4.473 | -4.410 | 0.000 | 0.003 | 45 |
| sensibilidad_2023_2025 | dulce | global | SARIMA | GC3 | 36 | -47.882 | -5.174 | -5.101 | 0.000 | 0.000 | 45 |
| sensibilidad_2023_2025 | dulce | global | SARIMA | GE | 36 | -46.353 | -5.404 | -5.328 | 0.000 | 0.000 | 45 |
| sensibilidad_2023_2025 | dulce | global | SARIMA-sel | Ridge | 36 | -43.032 | -5.274 | -5.200 | 0.000 | 0.000 | 45 |
| sensibilidad_2023_2025 | dulce | global | SARIMA-sel | ElasticNet | 36 | -38.559 | -4.882 | -4.813 | 0.000 | 0.001 | 45 |
| sensibilidad_2023_2025 | dulce | global | SARIMA-sel | XGB-37 | 36 | -33.469 | -4.657 | -4.592 | 0.000 | 0.002 | 45 |
| sensibilidad_2023_2025 | dulce | global | SARIMA-sel | GC3 | 36 | -48.950 | -5.311 | -5.237 | 0.000 | 0.000 | 45 |
| sensibilidad_2023_2025 | dulce | global | SARIMA-sel | GE | 36 | -47.421 | -5.565 | -5.487 | 0.000 | 0.000 | 45 |
| sensibilidad_2023_2025 | dulce | global | Ridge | ElasticNet | 36 | 4.473 | 2.830 | 2.790 | 0.008 | 0.169 | 45 |
| sensibilidad_2023_2025 | dulce | global | Ridge | XGB-37 | 36 | 9.563 | 1.197 | 1.180 | 0.246 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | global | Ridge | GC3 | 36 | -5.918 | -0.678 | -0.668 | 0.508 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | global | Ridge | GE | 36 | -4.389 | -0.532 | -0.525 | 0.603 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | global | ElasticNet | XGB-37 | 36 | 5.090 | 0.686 | 0.676 | 0.503 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | global | ElasticNet | GC3 | 36 | -10.391 | -1.262 | -1.245 | 0.222 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | global | ElasticNet | GE | 36 | -8.863 | -1.147 | -1.131 | 0.266 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | global | XGB-37 | GC3 | 36 | -15.481 | -2.345 | -2.312 | 0.027 | 0.428 | 45 |
| sensibilidad_2023_2025 | dulce | global | XGB-37 | GE | 36 | -13.952 | -2.249 | -2.218 | 0.033 | 0.497 | 45 |
| sensibilidad_2023_2025 | dulce | global | GC3 | GE | 36 | 1.528 | 0.992 | 0.979 | 0.335 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Naive | Seasonal Naive | 9 | 113.160 | 12.436 | 11.725 | 0.000 | 0.000 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Naive | Chronos | 9 | 82.844 | 9.721 | 9.165 | 0.000 | 0.001 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Naive | SARIMA | 9 | 120.621 | 12.265 | 11.563 | 0.000 | 0.000 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Naive | SARIMA-sel | 9 | 121.288 | 12.493 | 11.779 | 0.000 | 0.000 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Naive | Ridge | 9 | 54.020 | 4.656 | 4.389 | 0.002 | 0.079 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Naive | ElasticNet | 9 | 58.449 | 5.206 | 4.909 | 0.001 | 0.043 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Naive | XGB-37 | 9 | 69.052 | 4.833 | 4.556 | 0.002 | 0.065 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Naive | GC3 | 9 | 66.263 | 5.403 | 5.094 | 0.001 | 0.036 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Naive | GE | 9 | 70.536 | 7.213 | 6.801 | 0.000 | 0.006 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Seasonal Naive | Chronos | 9 | -30.316 | -5.901 | -5.564 | 0.001 | 0.021 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Seasonal Naive | SARIMA | 9 | 7.461 | 2.246 | 2.118 | 0.067 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Seasonal Naive | SARIMA-sel | 9 | 8.128 | 2.728 | 2.572 | 0.033 | 0.594 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Seasonal Naive | Ridge | 9 | -59.140 | -4.459 | -4.204 | 0.003 | 0.095 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Seasonal Naive | ElasticNet | 9 | -54.711 | -4.166 | -3.927 | 0.004 | 0.121 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Seasonal Naive | XGB-37 | 9 | -44.108 | -3.753 | -3.538 | 0.008 | 0.191 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Seasonal Naive | GC3 | 9 | -46.897 | -3.010 | -2.837 | 0.022 | 0.416 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Seasonal Naive | GE | 9 | -42.624 | -3.065 | -2.890 | 0.020 | 0.404 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Chronos | SARIMA | 9 | 37.777 | 5.241 | 4.941 | 0.001 | 0.042 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Chronos | SARIMA-sel | 9 | 38.444 | 5.581 | 5.262 | 0.001 | 0.030 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Chronos | Ridge | 9 | -28.823 | -2.296 | -2.165 | 0.062 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Chronos | ElasticNet | 9 | -24.395 | -2.104 | -1.983 | 0.083 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Chronos | XGB-37 | 9 | -13.792 | -1.554 | -1.465 | 0.181 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Chronos | GC3 | 9 | -16.580 | -1.210 | -1.141 | 0.287 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Chronos | GE | 9 | -12.307 | -1.069 | -1.008 | 0.343 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | SARIMA | SARIMA-sel | 9 | 0.667 | 1.358 | 1.280 | 0.236 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | SARIMA | Ridge | 9 | -66.600 | -4.449 | -4.195 | 0.003 | 0.095 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | SARIMA | ElasticNet | 9 | -62.172 | -4.101 | -3.867 | 0.005 | 0.124 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | SARIMA | XGB-37 | 9 | -51.569 | -4.199 | -3.959 | 0.004 | 0.121 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | SARIMA | GC3 | 9 | -54.357 | -3.120 | -2.942 | 0.019 | 0.392 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | SARIMA | GE | 9 | -50.084 | -3.183 | -3.001 | 0.017 | 0.387 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | SARIMA-sel | Ridge | 9 | -67.268 | -4.547 | -4.287 | 0.003 | 0.088 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | SARIMA-sel | ElasticNet | 9 | -62.839 | -4.202 | -3.962 | 0.004 | 0.121 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | SARIMA-sel | XGB-37 | 9 | -52.236 | -4.281 | -4.036 | 0.004 | 0.113 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | SARIMA-sel | GC3 | 9 | -55.025 | -3.191 | -3.009 | 0.017 | 0.387 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | SARIMA-sel | GE | 9 | -50.752 | -3.270 | -3.083 | 0.015 | 0.361 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Ridge | ElasticNet | 9 | 4.429 | 1.400 | 1.320 | 0.223 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Ridge | XGB-37 | 9 | 15.031 | 0.801 | 0.755 | 0.472 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Ridge | GC3 | 9 | 12.243 | 0.820 | 0.773 | 0.462 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | Ridge | GE | 9 | 16.516 | 1.299 | 1.225 | 0.255 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | ElasticNet | XGB-37 | 9 | 10.603 | 0.614 | 0.579 | 0.578 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | ElasticNet | GC3 | 9 | 7.814 | 0.563 | 0.531 | 0.610 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | ElasticNet | GE | 9 | 12.087 | 1.033 | 0.974 | 0.359 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | XGB-37 | GC3 | 9 | -2.789 | -0.182 | -0.171 | 0.868 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | XGB-37 | GE | 9 | 1.485 | 0.103 | 0.097 | 0.925 | 1.000 | 45 |
| sensibilidad_2023_2025 | dulce | shock_P75_mensual | GC3 | GE | 9 | 4.273 | 1.127 | 1.062 | 0.319 | 1.000 | 45 |

### T07_metricas_por_semilla.csv — T07 completa: métricas por semilla, por ventana y agregadas (P75 mensual)

`06_metricas/por_semilla/T07_metricas_por_semilla.csv` — 480 filas × 13 columnas.

| cultivar | modelo | ventana | semilla | MAE | RMSE | MASE | MAE_normal | MAE_shock | n_shock | n_normal | Delta_s | razon_shock_normal |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| sutil | XGB-37 | 2021 | 0 | 4,991.314 | 5,370.353 | 0.687 | 4,991.314 | — | 0 | 12 | — | — |
| sutil | XGB-37 | 2021 | 1 | 5,069.268 | 5,418.096 | 0.698 | 5,069.268 | — | 0 | 12 | — | — |
| sutil | XGB-37 | 2021 | 2 | 5,074.921 | 5,612.423 | 0.699 | 5,074.921 | — | 0 | 12 | — | — |
| sutil | XGB-37 | 2021 | 3 | 5,224.454 | 5,731.521 | 0.720 | 5,224.454 | — | 0 | 12 | — | — |
| sutil | XGB-37 | 2021 | 4 | 4,970.023 | 5,513.447 | 0.685 | 4,970.023 | — | 0 | 12 | — | — |
| sutil | XGB-37 | 2021 | 5 | 5,182.792 | 5,633.378 | 0.714 | 5,182.792 | — | 0 | 12 | — | — |
| sutil | XGB-37 | 2021 | 6 | 5,520.846 | 5,872.168 | 0.760 | 5,520.846 | — | 0 | 12 | — | — |
| sutil | XGB-37 | 2021 | 7 | 5,016.721 | 5,503.468 | 0.691 | 5,016.721 | — | 0 | 12 | — | — |
| sutil | XGB-37 | 2021 | 8 | 5,485.751 | 5,946.398 | 0.756 | 5,485.751 | — | 0 | 12 | — | — |
| sutil | XGB-37 | 2021 | 9 | 5,576.406 | 6,100.828 | 0.768 | 5,576.406 | — | 0 | 12 | — | — |
| sutil | XGB-37 | 2022 | 0 | 4,433.876 | 5,755.247 | 0.732 | 4,224.720 | 5,061.344 | 3 | 9 | 14.152 | 1.198 |
| sutil | XGB-37 | 2022 | 1 | 4,324.619 | 5,596.526 | 0.714 | 4,092.078 | 5,022.241 | 3 | 9 | 16.131 | 1.227 |
| sutil | XGB-37 | 2022 | 2 | 4,660.552 | 6,017.437 | 0.770 | 4,623.661 | 4,771.226 | 3 | 9 | 2.375 | 1.032 |
| sutil | XGB-37 | 2022 | 3 | 4,453.131 | 5,659.299 | 0.735 | 4,164.823 | 5,318.055 | 3 | 9 | 19.423 | 1.277 |
| sutil | XGB-37 | 2022 | 4 | 4,721.257 | 5,839.395 | 0.780 | 4,489.690 | 5,415.960 | 3 | 9 | 14.714 | 1.206 |
| sutil | XGB-37 | 2022 | 5 | 4,359.857 | 5,608.219 | 0.720 | 4,080.397 | 5,198.238 | 3 | 9 | 19.230 | 1.274 |
| sutil | XGB-37 | 2022 | 6 | 4,956.022 | 6,447.854 | 0.818 | 4,871.232 | 5,210.392 | 3 | 9 | 5.133 | 1.070 |
| sutil | XGB-37 | 2022 | 7 | 4,431.583 | 5,636.118 | 0.732 | 4,189.137 | 5,158.923 | 3 | 9 | 16.413 | 1.232 |
| sutil | XGB-37 | 2022 | 8 | 4,902.017 | 6,157.425 | 0.809 | 4,440.082 | 6,287.820 | 3 | 9 | 28.270 | 1.416 |
| sutil | XGB-37 | 2022 | 9 | 4,272.863 | 5,692.653 | 0.706 | 4,065.806 | 4,894.035 | 3 | 9 | 14.538 | 1.204 |
| sutil | XGB-37 | 2023 | 0 | 3,506.003 | 4,199.133 | 0.608 | 3,086.347 | 4,345.315 | 4 | 8 | 23.939 | 1.408 |
| sutil | XGB-37 | 2023 | 1 | 4,029.622 | 4,489.842 | 0.699 | 3,522.400 | 5,044.067 | 4 | 8 | 25.175 | 1.432 |
| sutil | XGB-37 | 2023 | 2 | 3,451.192 | 3,999.410 | 0.599 | 2,928.290 | 4,496.997 | 4 | 8 | 30.303 | 1.536 |
| sutil | XGB-37 | 2023 | 3 | 3,829.548 | 4,282.397 | 0.665 | 3,389.893 | 4,708.858 | 4 | 8 | 22.961 | 1.389 |
| sutil | XGB-37 | 2023 | 4 | 3,580.851 | 4,086.723 | 0.621 | 2,987.741 | 4,767.071 | 4 | 8 | 33.127 | 1.596 |
| sutil | XGB-37 | 2023 | 5 | 3,791.352 | 4,277.630 | 0.658 | 3,297.565 | 4,778.928 | 4 | 8 | 26.048 | 1.449 |
| sutil | XGB-37 | 2023 | 6 | 3,762.976 | 4,156.747 | 0.653 | 3,327.927 | 4,633.075 | 4 | 8 | 23.123 | 1.392 |
| sutil | XGB-37 | 2023 | 7 | 4,022.641 | 4,367.833 | 0.698 | 3,689.471 | 4,688.982 | 4 | 8 | 16.565 | 1.271 |
| sutil | XGB-37 | 2023 | 8 | 4,077.245 | 4,515.857 | 0.707 | 3,600.809 | 5,030.116 | 4 | 8 | 23.370 | 1.397 |
| sutil | XGB-37 | 2023 | 9 | 3,801.791 | 4,332.019 | 0.660 | 3,249.581 | 4,906.209 | 4 | 8 | 29.050 | 1.510 |
| sutil | XGB-37 | 2024 | 0 | 4,794.704 | 6,370.707 | 0.873 | 4,794.704 | — | 0 | 12 | — | — |
| sutil | XGB-37 | 2024 | 1 | 5,108.520 | 6,847.812 | 0.930 | 5,108.520 | — | 0 | 12 | — | — |
| sutil | XGB-37 | 2024 | 2 | 5,299.612 | 7,012.125 | 0.965 | 5,299.612 | — | 0 | 12 | — | — |
| sutil | XGB-37 | 2024 | 3 | 5,108.497 | 6,656.845 | 0.930 | 5,108.497 | — | 0 | 12 | — | — |
| sutil | XGB-37 | 2024 | 4 | 4,662.965 | 6,125.285 | 0.849 | 4,662.965 | — | 0 | 12 | — | — |
| sutil | XGB-37 | 2024 | 5 | 4,954.439 | 6,438.609 | 0.902 | 4,954.439 | — | 0 | 12 | — | — |
| sutil | XGB-37 | 2024 | 6 | 4,731.212 | 6,248.059 | 0.861 | 4,731.212 | — | 0 | 12 | — | — |
| sutil | XGB-37 | 2024 | 7 | 5,074.842 | 6,732.511 | 0.924 | 5,074.842 | — | 0 | 12 | — | — |
| sutil | XGB-37 | 2024 | 8 | 4,679.165 | 6,091.195 | 0.852 | 4,679.165 | — | 0 | 12 | — | — |
| sutil | XGB-37 | 2024 | 9 | 5,153.280 | 6,720.708 | 0.938 | 5,153.280 | — | 0 | 12 | — | — |
| sutil | XGB-37 | 2025 | 0 | 6,065.325 | 7,087.434 | 1.046 | 5,315.729 | 8,314.115 | 3 | 9 | 37.076 | 1.564 |
| sutil | XGB-37 | 2025 | 1 | 5,848.796 | 6,994.462 | 1.009 | 5,048.386 | 8,250.025 | 3 | 9 | 41.055 | 1.634 |
| sutil | XGB-37 | 2025 | 2 | 5,919.310 | 7,080.661 | 1.021 | 5,188.366 | 8,112.142 | 3 | 9 | 37.045 | 1.564 |
| sutil | XGB-37 | 2025 | 3 | 5,872.044 | 7,068.904 | 1.013 | 4,981.714 | 8,543.034 | 3 | 9 | 45.487 | 1.715 |
| sutil | XGB-37 | 2025 | 4 | 5,775.315 | 6,923.503 | 0.996 | 4,897.954 | 8,407.401 | 3 | 9 | 45.575 | 1.717 |
| sutil | XGB-37 | 2025 | 5 | 5,919.914 | 6,891.723 | 1.021 | 5,283.166 | 7,830.157 | 3 | 9 | 32.268 | 1.482 |
| sutil | XGB-37 | 2025 | 6 | 5,626.916 | 6,834.980 | 0.970 | 4,764.291 | 8,214.790 | 3 | 9 | 45.991 | 1.724 |
| sutil | XGB-37 | 2025 | 7 | 5,867.353 | 7,017.680 | 1.012 | 5,107.253 | 8,147.650 | 3 | 9 | 38.864 | 1.595 |
| sutil | XGB-37 | 2025 | 8 | 6,059.973 | 7,103.125 | 1.045 | 5,227.324 | 8,557.918 | 3 | 9 | 41.220 | 1.637 |
| sutil | XGB-37 | 2025 | 9 | 6,068.807 | 7,105.381 | 1.047 | 5,227.832 | 8,591.734 | 3 | 9 | 41.572 | 1.643 |
| sutil | XGB-37 | agregado_2021_2025 | 0 | 4,758.245 | 5,838.046 | 0.789 | 4,559.741 | 5,750.764 | 10 | 50 | 20.859 | 1.261 |
| sutil | XGB-37 | agregado_2021_2025 | 1 | 4,876.165 | 5,943.914 | 0.810 | 4,651.537 | 5,999.307 | 10 | 50 | 23.033 | 1.290 |
| sutil | XGB-37 | agregado_2021_2025 | 2 | 4,881.117 | 6,049.955 | 0.811 | 4,724.579 | 5,663.809 | 10 | 50 | 16.035 | 1.199 |
| sutil | XGB-37 | agregado_2021_2025 | 3 | 4,897.535 | 5,958.186 | 0.812 | 4,668.668 | 6,041.870 | 10 | 50 | 23.366 | 1.294 |
| sutil | XGB-37 | agregado_2021_2025 | 4 | 4,742.082 | 5,773.248 | 0.786 | 4,479.732 | 6,053.837 | 10 | 50 | 27.662 | 1.351 |
| sutil | XGB-37 | agregado_2021_2025 | 5 | 4,841.671 | 5,838.437 | 0.803 | 4,645.987 | 5,820.090 | 10 | 50 | 20.208 | 1.253 |
| sutil | XGB-37 | agregado_2021_2025 | 6 | 4,919.595 | 5,984.830 | 0.813 | 4,727.356 | 5,880.785 | 10 | 50 | 19.538 | 1.244 |
| sutil | XGB-37 | agregado_2021_2025 | 7 | 4,882.628 | 5,928.009 | 0.811 | 4,685.641 | 5,867.565 | 10 | 50 | 20.172 | 1.252 |
| sutil | XGB-37 | agregado_2021_2025 | 8 | 5,040.830 | 6,020.358 | 0.834 | 4,755.842 | 6,465.768 | 10 | 50 | 28.268 | 1.360 |
| sutil | XGB-37 | agregado_2021_2025 | 9 | 4,974.629 | 6,067.077 | 0.824 | 4,767.912 | 6,008.214 | 10 | 50 | 20.777 | 1.260 |
| sutil | XGB-43 | 2021 | 0 | 5,020.433 | 5,430.752 | 0.691 | 5,020.433 | — | 0 | 12 | — | — |
| sutil | XGB-43 | 2021 | 1 | 5,273.224 | 5,668.114 | 0.726 | 5,273.224 | — | 0 | 12 | — | — |
| sutil | XGB-43 | 2021 | 2 | 5,211.085 | 5,807.088 | 0.718 | 5,211.085 | — | 0 | 12 | — | — |
| sutil | XGB-43 | 2021 | 3 | 5,579.765 | 6,109.422 | 0.768 | 5,579.765 | — | 0 | 12 | — | — |
| sutil | XGB-43 | 2021 | 4 | 5,237.079 | 5,753.104 | 0.721 | 5,237.079 | — | 0 | 12 | — | — |
| sutil | XGB-43 | 2021 | 5 | 5,938.835 | 6,439.505 | 0.818 | 5,938.835 | — | 0 | 12 | — | — |
| sutil | XGB-43 | 2021 | 6 | 5,262.086 | 5,671.620 | 0.725 | 5,262.086 | — | 0 | 12 | — | — |
| sutil | XGB-43 | 2021 | 7 | 5,219.091 | 5,749.541 | 0.719 | 5,219.091 | — | 0 | 12 | — | — |
| sutil | XGB-43 | 2021 | 8 | 5,540.572 | 5,949.006 | 0.763 | 5,540.572 | — | 0 | 12 | — | — |
| sutil | XGB-43 | 2021 | 9 | 5,048.349 | 5,455.388 | 0.695 | 5,048.349 | — | 0 | 12 | — | — |
| sutil | XGB-43 | 2022 | 0 | 4,571.602 | 5,958.773 | 0.755 | 4,187.219 | 5,724.753 | 3 | 9 | 25.224 | 1.367 |
| sutil | XGB-43 | 2022 | 1 | 4,124.378 | 5,442.205 | 0.681 | 3,909.475 | 4,769.085 | 3 | 9 | 15.632 | 1.220 |
| sutil | XGB-43 | 2022 | 2 | 5,199.319 | 6,635.676 | 0.859 | 5,246.175 | 5,058.749 | 3 | 9 | -2.704 | 0.964 |
| sutil | XGB-43 | 2022 | 3 | 4,652.825 | 6,016.049 | 0.768 | 4,332.344 | 5,614.271 | 3 | 9 | 20.664 | 1.296 |
| sutil | XGB-43 | 2022 | 4 | 4,564.934 | 5,689.309 | 0.754 | 4,315.970 | 5,311.827 | 3 | 9 | 16.362 | 1.231 |
| sutil | XGB-43 | 2022 | 5 | 4,699.450 | 5,903.020 | 0.776 | 4,438.243 | 5,483.072 | 3 | 9 | 16.675 | 1.235 |
| sutil | XGB-43 | 2022 | 6 | 4,760.700 | 6,097.864 | 0.786 | 4,469.696 | 5,633.711 | 3 | 9 | 18.338 | 1.260 |
| sutil | XGB-43 | 2022 | 7 | 4,876.297 | 6,112.337 | 0.805 | 4,671.463 | 5,490.801 | 3 | 9 | 12.602 | 1.175 |
| sutil | XGB-43 | 2022 | 8 | 4,706.089 | 5,986.549 | 0.777 | 4,419.961 | 5,564.474 | 3 | 9 | 18.240 | 1.259 |
| sutil | XGB-43 | 2022 | 9 | 4,480.114 | 5,849.133 | 0.740 | 4,275.835 | 5,092.950 | 3 | 9 | 13.679 | 1.191 |
| sutil | XGB-43 | 2023 | 0 | 3,706.389 | 4,221.124 | 0.643 | 3,181.237 | 4,756.693 | 4 | 8 | 28.338 | 1.495 |
| sutil | XGB-43 | 2023 | 1 | 3,577.531 | 4,175.535 | 0.621 | 3,090.649 | 4,551.293 | 4 | 8 | 27.219 | 1.473 |
| sutil | XGB-43 | 2023 | 2 | 3,670.540 | 4,134.142 | 0.637 | 3,199.872 | 4,611.875 | 4 | 8 | 25.646 | 1.441 |
| sutil | XGB-43 | 2023 | 3 | 3,644.076 | 4,092.136 | 0.632 | 3,234.933 | 4,462.361 | 4 | 8 | 22.455 | 1.379 |
| sutil | XGB-43 | 2023 | 4 | 3,432.484 | 4,035.427 | 0.596 | 2,801.267 | 4,694.917 | 4 | 8 | 36.779 | 1.676 |
| sutil | XGB-43 | 2023 | 5 | 3,706.380 | 4,180.129 | 0.643 | 3,207.973 | 4,703.195 | 4 | 8 | 26.895 | 1.466 |
| sutil | XGB-43 | 2023 | 6 | 3,851.823 | 4,410.514 | 0.668 | 3,310.391 | 4,934.686 | 4 | 8 | 28.113 | 1.491 |
| sutil | XGB-43 | 2023 | 7 | 4,139.121 | 4,577.798 | 0.718 | 3,693.803 | 5,029.756 | 4 | 8 | 21.517 | 1.362 |
| sutil | XGB-43 | 2023 | 8 | 3,647.154 | 4,168.601 | 0.633 | 3,189.376 | 4,562.709 | 4 | 8 | 25.103 | 1.431 |
| sutil | XGB-43 | 2023 | 9 | 3,415.033 | 4,000.949 | 0.593 | 2,995.521 | 4,254.058 | 4 | 8 | 24.569 | 1.420 |
| sutil | XGB-43 | 2024 | 0 | 5,841.742 | 7,898.429 | 1.064 | 5,841.742 | — | 0 | 12 | — | — |
| sutil | XGB-43 | 2024 | 1 | 5,733.277 | 7,563.986 | 1.044 | 5,733.277 | — | 0 | 12 | — | — |
| sutil | XGB-43 | 2024 | 2 | 5,546.760 | 7,444.543 | 1.010 | 5,546.760 | — | 0 | 12 | — | — |
| sutil | XGB-43 | 2024 | 3 | 5,552.814 | 7,437.166 | 1.011 | 5,552.814 | — | 0 | 12 | — | — |
| sutil | XGB-43 | 2024 | 4 | 5,149.897 | 6,837.459 | 0.938 | 5,149.897 | — | 0 | 12 | — | — |
| sutil | XGB-43 | 2024 | 5 | 5,386.358 | 7,136.226 | 0.981 | 5,386.358 | — | 0 | 12 | — | — |
| sutil | XGB-43 | 2024 | 6 | 5,550.085 | 7,491.199 | 1.011 | 5,550.085 | — | 0 | 12 | — | — |
| sutil | XGB-43 | 2024 | 7 | 5,109.703 | 6,754.325 | 0.930 | 5,109.703 | — | 0 | 12 | — | — |
| sutil | XGB-43 | 2024 | 8 | 5,606.418 | 7,410.007 | 1.021 | 5,606.418 | — | 0 | 12 | — | — |
| sutil | XGB-43 | 2024 | 9 | 5,184.481 | 6,923.957 | 0.944 | 5,184.481 | — | 0 | 12 | — | — |
| sutil | XGB-43 | 2025 | 0 | 6,076.724 | 7,226.657 | 1.048 | 5,338.353 | 8,291.838 | 3 | 9 | 36.452 | 1.553 |
| sutil | XGB-43 | 2025 | 1 | 5,685.956 | 6,935.244 | 0.981 | 4,779.037 | 8,406.712 | 3 | 9 | 47.850 | 1.759 |
| sutil | XGB-43 | 2025 | 2 | 5,750.640 | 7,122.375 | 0.992 | 4,828.691 | 8,516.490 | 3 | 9 | 48.096 | 1.764 |
| sutil | XGB-43 | 2025 | 3 | 6,317.469 | 7,455.867 | 1.090 | 5,507.489 | 8,747.409 | 3 | 9 | 38.464 | 1.588 |
| sutil | XGB-43 | 2025 | 4 | 5,901.763 | 7,055.883 | 1.018 | 5,092.874 | 8,328.429 | 3 | 9 | 41.118 | 1.635 |
| sutil | XGB-43 | 2025 | 5 | 6,093.160 | 7,248.192 | 1.051 | 5,269.838 | 8,563.125 | 3 | 9 | 40.537 | 1.625 |
| sutil | XGB-43 | 2025 | 6 | 5,825.995 | 7,002.270 | 1.005 | 4,995.760 | 8,316.698 | 3 | 9 | 42.752 | 1.665 |
| sutil | XGB-43 | 2025 | 7 | 5,804.094 | 7,042.249 | 1.001 | 4,911.160 | 8,482.895 | 3 | 9 | 46.154 | 1.727 |
| sutil | XGB-43 | 2025 | 8 | 5,823.295 | 7,143.374 | 1.004 | 4,943.821 | 8,461.716 | 3 | 9 | 45.308 | 1.712 |
| sutil | XGB-43 | 2025 | 9 | 5,899.393 | 7,052.221 | 1.017 | 5,210.837 | 7,965.062 | 3 | 9 | 35.015 | 1.529 |
| sutil | XGB-43 | agregado_2021_2025 | 0 | 5,043.378 | 6,283.752 | 0.840 | 4,830.523 | 6,107.654 | 10 | 50 | 21.102 | 1.264 |
| sutil | XGB-43 | agregado_2021_2025 | 1 | 4,878.873 | 6,074.400 | 0.811 | 4,699.996 | 5,773.256 | 10 | 50 | 18.332 | 1.228 |
| sutil | XGB-43 | agregado_2021_2025 | 2 | 5,075.669 | 6,340.269 | 0.843 | 4,907.338 | 5,917.322 | 10 | 50 | 16.582 | 1.206 |
| sutil | XGB-43 | agregado_2021_2025 | 3 | 5,149.390 | 6,342.947 | 0.854 | 4,960.578 | 6,093.448 | 10 | 50 | 18.333 | 1.228 |
| sutil | XGB-43 | agregado_2021_2025 | 4 | 4,857.231 | 5,971.389 | 0.805 | 4,634.669 | 5,970.044 | 10 | 50 | 22.910 | 1.288 |
| sutil | XGB-43 | agregado_2021_2025 | 5 | 5,164.837 | 6,280.897 | 0.854 | 4,978.777 | 6,095.137 | 10 | 50 | 18.012 | 1.224 |
| sutil | XGB-43 | agregado_2021_2025 | 6 | 5,050.138 | 6,228.221 | 0.839 | 4,828.366 | 6,158.997 | 10 | 50 | 21.957 | 1.276 |
| sutil | XGB-43 | agregado_2021_2025 | 7 | 5,029.661 | 6,108.818 | 0.835 | 4,794.791 | 6,204.011 | 10 | 50 | 23.348 | 1.294 |
| sutil | XGB-43 | agregado_2021_2025 | 8 | 5,064.706 | 6,237.671 | 0.840 | 4,871.058 | 6,032.941 | 10 | 50 | 19.117 | 1.239 |
| sutil | XGB-43 | agregado_2021_2025 | 9 | 4,805.474 | 5,960.809 | 0.798 | 4,642.764 | 5,619.026 | 10 | 50 | 16.930 | 1.210 |
| sutil | GC3 | 2021 | 0 | 4,710.634 | 5,308.505 | 0.649 | 4,710.634 | — | 0 | 12 | — | — |
| sutil | GC3 | 2021 | 1 | 4,032.250 | 4,689.911 | 0.555 | 4,032.250 | — | 0 | 12 | — | — |
| sutil | GC3 | 2021 | 2 | 4,620.471 | 5,229.325 | 0.636 | 4,620.471 | — | 0 | 12 | — | — |
| sutil | GC3 | 2021 | 3 | 3,182.185 | 3,622.719 | 0.438 | 3,182.185 | — | 0 | 12 | — | — |
| sutil | GC3 | 2021 | 4 | 3,941.797 | 4,214.745 | 0.543 | 3,941.797 | — | 0 | 12 | — | — |
| sutil | GC3 | 2021 | 5 | 2,797.357 | 3,296.930 | 0.385 | 2,797.357 | — | 0 | 12 | — | — |
| sutil | GC3 | 2021 | 6 | 3,586.293 | 3,787.363 | 0.494 | 3,586.293 | — | 0 | 12 | — | — |
| sutil | GC3 | 2021 | 7 | 3,280.923 | 3,744.570 | 0.452 | 3,280.923 | — | 0 | 12 | — | — |
| sutil | GC3 | 2021 | 8 | 4,372.216 | 4,980.896 | 0.602 | 4,372.216 | — | 0 | 12 | — | — |
| sutil | GC3 | 2021 | 9 | 4,036.163 | 4,379.971 | 0.556 | 4,036.163 | — | 0 | 12 | — | — |
| sutil | GC3 | 2022 | 0 | 4,164.300 | 5,374.969 | 0.688 | 4,257.012 | 3,886.164 | 3 | 9 | -6.679 | 0.913 |
| sutil | GC3 | 2022 | 1 | 5,442.717 | 6,823.703 | 0.899 | 5,234.151 | 6,068.413 | 3 | 9 | 11.496 | 1.159 |
| sutil | GC3 | 2022 | 2 | 5,164.315 | 6,665.531 | 0.853 | 5,316.255 | 4,708.494 | 3 | 9 | -8.826 | 0.886 |
| sutil | GC3 | 2022 | 3 | 4,770.178 | 6,164.776 | 0.788 | 4,753.087 | 4,821.450 | 3 | 9 | 1.075 | 1.014 |
| sutil | GC3 | 2022 | 4 | 5,277.361 | 6,731.977 | 0.871 | 5,447.850 | 4,765.894 | 3 | 9 | -9.692 | 0.875 |
| sutil | GC3 | 2022 | 5 | 5,425.093 | 6,520.914 | 0.896 | 5,501.440 | 5,196.051 | 3 | 9 | -4.222 | 0.944 |
| sutil | GC3 | 2022 | 6 | 5,769.414 | 6,816.889 | 0.953 | 5,992.737 | 5,099.447 | 3 | 9 | -11.612 | 0.851 |
| sutil | GC3 | 2022 | 7 | 4,796.604 | 6,492.561 | 0.792 | 4,782.195 | 4,839.830 | 3 | 9 | 0.901 | 1.012 |
| sutil | GC3 | 2022 | 8 | 5,282.820 | 6,006.390 | 0.872 | 5,205.601 | 5,514.474 | 3 | 9 | 4.385 | 1.059 |
| sutil | GC3 | 2022 | 9 | 5,526.109 | 6,391.138 | 0.912 | 5,948.484 | 4,258.986 | 3 | 9 | -22.930 | 0.716 |
| sutil | GC3 | 2023 | 0 | 5,625.588 | 6,370.844 | 0.976 | 4,856.448 | 7,163.867 | 4 | 8 | 27.344 | 1.475 |
| sutil | GC3 | 2023 | 1 | 5,058.460 | 5,895.866 | 0.878 | 4,290.256 | 6,594.869 | 4 | 8 | 30.373 | 1.537 |
| sutil | GC3 | 2023 | 2 | 5,893.125 | 6,795.551 | 1.023 | 4,826.517 | 8,026.340 | 4 | 8 | 36.198 | 1.663 |
| sutil | GC3 | 2023 | 3 | 5,695.624 | 6,653.943 | 0.988 | 5,229.843 | 6,627.185 | 4 | 8 | 16.356 | 1.267 |
| sutil | GC3 | 2023 | 4 | 7,251.058 | 8,653.181 | 1.258 | 6,010.521 | 9,732.132 | 4 | 8 | 34.217 | 1.619 |
| sutil | GC3 | 2023 | 5 | 4,661.950 | 5,394.878 | 0.809 | 4,898.735 | 4,188.379 | 4 | 8 | -10.158 | 0.855 |
| sutil | GC3 | 2023 | 6 | 5,678.948 | 6,627.867 | 0.985 | 4,966.754 | 7,103.337 | 4 | 8 | 25.082 | 1.430 |
| sutil | GC3 | 2023 | 7 | 6,943.992 | 7,801.422 | 1.205 | 6,542.952 | 7,746.073 | 4 | 8 | 11.551 | 1.184 |
| sutil | GC3 | 2023 | 8 | 7,547.417 | 8,748.372 | 1.310 | 7,207.124 | 8,228.002 | 4 | 8 | 9.017 | 1.142 |
| sutil | GC3 | 2023 | 9 | 6,380.808 | 7,587.671 | 1.107 | 5,758.169 | 7,626.085 | 4 | 8 | 19.516 | 1.324 |
| sutil | GC3 | 2024 | 0 | 10,343.809 | 12,952.447 | 1.883 | 10,343.809 | — | 0 | 12 | — | — |
| sutil | GC3 | 2024 | 1 | 10,493.178 | 13,169.820 | 1.911 | 10,493.178 | — | 0 | 12 | — | — |
| sutil | GC3 | 2024 | 2 | 10,051.255 | 12,700.843 | 1.830 | 10,051.255 | — | 0 | 12 | — | — |
| sutil | GC3 | 2024 | 3 | 7,206.279 | 10,023.475 | 1.312 | 7,206.279 | — | 0 | 12 | — | — |
| sutil | GC3 | 2024 | 4 | 8,574.874 | 11,134.293 | 1.561 | 8,574.874 | — | 0 | 12 | — | — |
| sutil | GC3 | 2024 | 5 | 7,775.636 | 10,374.130 | 1.416 | 7,775.636 | — | 0 | 12 | — | — |
| sutil | GC3 | 2024 | 6 | 9,883.525 | 12,449.613 | 1.800 | 9,883.525 | — | 0 | 12 | — | — |
| sutil | GC3 | 2024 | 7 | 8,591.912 | 11,964.477 | 1.564 | 8,591.912 | — | 0 | 12 | — | — |
| sutil | GC3 | 2024 | 8 | 7,954.798 | 11,106.697 | 1.448 | 7,954.798 | — | 0 | 12 | — | — |
| sutil | GC3 | 2024 | 9 | 8,813.792 | 11,160.052 | 1.605 | 8,813.792 | — | 0 | 12 | — | — |
| sutil | GC3 | 2025 | 0 | 7,988.511 | 9,396.933 | 1.378 | 8,874.997 | 5,329.053 | 3 | 9 | -33.291 | 0.600 |
| sutil | GC3 | 2025 | 1 | 8,926.812 | 10,622.863 | 1.540 | 9,586.981 | 6,946.304 | 3 | 9 | -22.186 | 0.725 |
| sutil | GC3 | 2025 | 2 | 6,748.361 | 7,725.067 | 1.164 | 7,481.657 | 4,548.474 | 3 | 9 | -32.599 | 0.608 |
| sutil | GC3 | 2025 | 3 | 8,358.188 | 9,142.812 | 1.441 | 9,109.637 | 6,103.842 | 3 | 9 | -26.972 | 0.670 |
| sutil | GC3 | 2025 | 4 | 7,612.684 | 8,122.461 | 1.313 | 8,847.076 | 3,909.511 | 3 | 9 | -48.645 | 0.442 |
| sutil | GC3 | 2025 | 5 | 6,105.535 | 6,442.644 | 1.053 | 6,372.768 | 5,303.837 | 3 | 9 | -13.131 | 0.832 |
| sutil | GC3 | 2025 | 6 | 10,247.145 | 11,523.821 | 1.767 | 11,018.980 | 7,931.638 | 3 | 9 | -22.597 | 0.720 |
| sutil | GC3 | 2025 | 7 | 9,481.878 | 10,720.376 | 1.635 | 10,130.329 | 7,536.526 | 3 | 9 | -20.517 | 0.744 |
| sutil | GC3 | 2025 | 8 | 6,230.297 | 6,470.706 | 1.074 | 6,843.034 | 4,392.087 | 3 | 9 | -29.504 | 0.642 |
| sutil | GC3 | 2025 | 9 | 5,760.589 | 6,672.926 | 0.993 | 6,367.513 | 3,939.817 | 3 | 9 | -31.607 | 0.619 |
| sutil | GC3 | agregado_2021_2025 | 0 | 6,566.568 | 8,411.021 | 1.115 | 6,753.860 | 5,630.112 | 10 | 50 | -14.261 | 0.834 |
| sutil | GC3 | agregado_2021_2025 | 1 | 6,790.683 | 8,827.330 | 1.156 | 6,840.347 | 6,542.363 | 10 | 50 | -3.657 | 0.956 |
| sutil | GC3 | agregado_2021_2025 | 2 | 6,495.505 | 8,233.380 | 1.101 | 6,597.081 | 5,987.626 | 10 | 50 | -7.819 | 0.908 |
| sutil | GC3 | agregado_2021_2025 | 3 | 5,842.491 | 7,476.156 | 0.994 | 5,825.297 | 5,928.461 | 10 | 50 | 1.471 | 1.018 |
| sutil | GC3 | agregado_2021_2025 | 4 | 6,531.555 | 8,098.246 | 1.109 | 6,538.771 | 6,495.474 | 10 | 50 | -0.552 | 0.993 |
| sutil | GC3 | agregado_2021_2025 | 5 | 5,353.114 | 6,806.277 | 0.912 | 5,458.673 | 4,825.318 | 10 | 50 | -9.860 | 0.884 |
| sutil | GC3 | agregado_2021_2025 | 6 | 7,033.065 | 8,860.407 | 1.200 | 7,089.546 | 6,750.660 | 10 | 50 | -4.015 | 0.952 |
| sutil | GC3 | agregado_2021_2025 | 7 | 6,619.062 | 8,661.553 | 1.130 | 6,580.607 | 6,811.336 | 10 | 50 | 2.905 | 1.035 |
| sutil | GC3 | agregado_2021_2025 | 8 | 6,277.510 | 7,780.088 | 1.061 | 6,280.378 | 6,263.169 | 10 | 50 | -0.228 | 0.997 |
| sutil | GC3 | agregado_2021_2025 | 9 | 6,103.492 | 7,572.031 | 1.035 | 6,222.176 | 5,510.075 | 10 | 50 | -9.723 | 0.886 |
| sutil | GE | 2021 | 0 | 4,395.638 | 5,092.856 | 0.605 | 4,395.638 | — | 0 | 12 | — | — |
| sutil | GE | 2021 | 1 | 4,826.117 | 5,484.275 | 0.665 | 4,826.117 | — | 0 | 12 | — | — |
| sutil | GE | 2021 | 2 | 4,757.672 | 5,256.541 | 0.655 | 4,757.672 | — | 0 | 12 | — | — |
| sutil | GE | 2021 | 3 | 3,027.491 | 3,507.177 | 0.417 | 3,027.491 | — | 0 | 12 | — | — |
| sutil | GE | 2021 | 4 | 5,213.970 | 5,437.006 | 0.718 | 5,213.970 | — | 0 | 12 | — | — |
| sutil | GE | 2021 | 5 | 2,720.236 | 3,199.177 | 0.375 | 2,720.236 | — | 0 | 12 | — | — |
| sutil | GE | 2021 | 6 | 3,473.118 | 3,709.870 | 0.478 | 3,473.118 | — | 0 | 12 | — | — |
| sutil | GE | 2021 | 7 | 3,953.097 | 4,494.913 | 0.544 | 3,953.097 | — | 0 | 12 | — | — |
| sutil | GE | 2021 | 8 | 3,502.321 | 3,988.145 | 0.482 | 3,502.321 | — | 0 | 12 | — | — |
| sutil | GE | 2021 | 9 | 2,802.042 | 3,044.871 | 0.386 | 2,802.042 | — | 0 | 12 | — | — |
| sutil | GE | 2022 | 0 | 4,787.998 | 6,360.384 | 0.791 | 4,775.772 | 4,824.676 | 3 | 9 | 0.766 | 1.010 |
| sutil | GE | 2022 | 1 | 5,094.775 | 6,844.015 | 0.841 | 4,904.603 | 5,665.290 | 3 | 9 | 11.198 | 1.155 |
| sutil | GE | 2022 | 2 | 5,226.727 | 6,918.794 | 0.863 | 5,494.132 | 4,424.511 | 3 | 9 | -15.348 | 0.805 |
| sutil | GE | 2022 | 3 | 5,203.482 | 6,787.389 | 0.859 | 5,138.814 | 5,397.485 | 3 | 9 | 3.728 | 1.050 |
| sutil | GE | 2022 | 4 | 5,468.586 | 7,229.943 | 0.903 | 5,600.797 | 5,071.953 | 3 | 9 | -7.253 | 0.906 |
| sutil | GE | 2022 | 5 | 5,433.419 | 6,957.602 | 0.897 | 5,453.961 | 5,371.792 | 3 | 9 | -1.134 | 0.985 |
| sutil | GE | 2022 | 6 | 5,638.153 | 7,773.591 | 0.931 | 5,575.043 | 5,827.484 | 3 | 9 | 3.358 | 1.045 |
| sutil | GE | 2022 | 7 | 4,969.858 | 6,668.888 | 0.821 | 4,889.869 | 5,209.827 | 3 | 9 | 4.828 | 1.065 |
| sutil | GE | 2022 | 8 | 6,000.572 | 6,748.378 | 0.991 | 6,080.383 | 5,761.137 | 3 | 9 | -3.990 | 0.947 |
| sutil | GE | 2022 | 9 | 4,771.999 | 6,075.015 | 0.788 | 4,874.739 | 4,463.777 | 3 | 9 | -6.459 | 0.916 |
| sutil | GE | 2023 | 0 | 5,315.080 | 6,210.033 | 0.922 | 3,915.486 | 8,114.268 | 4 | 8 | 52.665 | 2.072 |
| sutil | GE | 2023 | 1 | 5,466.399 | 6,283.507 | 0.949 | 4,475.684 | 7,447.831 | 4 | 8 | 36.247 | 1.664 |
| sutil | GE | 2023 | 2 | 5,232.745 | 6,042.772 | 0.908 | 4,229.568 | 7,239.099 | 4 | 8 | 38.342 | 1.712 |
| sutil | GE | 2023 | 3 | 4,980.607 | 5,767.783 | 0.864 | 4,325.016 | 6,291.790 | 4 | 8 | 26.326 | 1.455 |
| sutil | GE | 2023 | 4 | 6,282.345 | 7,686.701 | 1.090 | 5,168.017 | 8,511.003 | 4 | 8 | 35.475 | 1.647 |
| sutil | GE | 2023 | 5 | 4,523.621 | 5,334.704 | 0.785 | 4,105.229 | 5,360.404 | 4 | 8 | 18.498 | 1.306 |
| sutil | GE | 2023 | 6 | 4,510.334 | 5,191.915 | 0.783 | 3,609.920 | 6,311.162 | 4 | 8 | 39.927 | 1.748 |
| sutil | GE | 2023 | 7 | 5,912.899 | 6,562.649 | 1.026 | 4,850.286 | 8,038.124 | 4 | 8 | 35.942 | 1.657 |
| sutil | GE | 2023 | 8 | 5,834.145 | 6,661.080 | 1.012 | 5,071.464 | 7,359.508 | 4 | 8 | 26.145 | 1.451 |
| sutil | GE | 2023 | 9 | 5,847.217 | 6,751.789 | 1.015 | 4,937.897 | 7,665.858 | 4 | 8 | 31.103 | 1.552 |
| sutil | GE | 2024 | 0 | 11,459.007 | 13,851.957 | 2.087 | 11,459.007 | — | 0 | 12 | — | — |
| sutil | GE | 2024 | 1 | 9,905.038 | 12,700.370 | 1.804 | 9,905.038 | — | 0 | 12 | — | — |
| sutil | GE | 2024 | 2 | 10,907.571 | 13,225.172 | 1.986 | 10,907.571 | — | 0 | 12 | — | — |
| sutil | GE | 2024 | 3 | 8,180.791 | 10,689.103 | 1.490 | 8,180.791 | — | 0 | 12 | — | — |
| sutil | GE | 2024 | 4 | 9,307.994 | 11,286.195 | 1.695 | 9,307.994 | — | 0 | 12 | — | — |
| sutil | GE | 2024 | 5 | 8,563.665 | 10,888.840 | 1.559 | 8,563.665 | — | 0 | 12 | — | — |
| sutil | GE | 2024 | 6 | 10,896.047 | 12,944.599 | 1.984 | 10,896.047 | — | 0 | 12 | — | — |
| sutil | GE | 2024 | 7 | 9,036.476 | 12,411.663 | 1.645 | 9,036.476 | — | 0 | 12 | — | — |
| sutil | GE | 2024 | 8 | 8,313.221 | 10,636.401 | 1.514 | 8,313.221 | — | 0 | 12 | — | — |
| sutil | GE | 2024 | 9 | 11,169.440 | 13,355.988 | 2.034 | 11,169.440 | — | 0 | 12 | — | — |
| sutil | GE | 2025 | 0 | 11,131.094 | 12,892.781 | 1.920 | 11,817.230 | 9,072.686 | 3 | 9 | -18.492 | 0.768 |
| sutil | GE | 2025 | 1 | 10,513.056 | 12,285.225 | 1.813 | 11,016.754 | 9,001.963 | 3 | 9 | -14.373 | 0.817 |
| sutil | GE | 2025 | 2 | 8,216.852 | 9,426.540 | 1.417 | 8,530.965 | 7,274.514 | 3 | 9 | -11.468 | 0.853 |
| sutil | GE | 2025 | 3 | 9,109.455 | 10,542.588 | 1.571 | 9,131.052 | 9,044.667 | 3 | 9 | -0.711 | 0.991 |
| sutil | GE | 2025 | 4 | 9,252.553 | 10,993.409 | 1.596 | 9,584.152 | 8,257.757 | 3 | 9 | -10.752 | 0.862 |
| sutil | GE | 2025 | 5 | 8,847.540 | 9,839.666 | 1.526 | 9,421.910 | 7,124.430 | 3 | 9 | -19.476 | 0.756 |
| sutil | GE | 2025 | 6 | 10,698.297 | 12,161.162 | 1.845 | 11,464.387 | 8,400.026 | 3 | 9 | -21.483 | 0.733 |
| sutil | GE | 2025 | 7 | 10,416.795 | 11,905.134 | 1.796 | 11,106.016 | 8,349.132 | 3 | 9 | -19.849 | 0.752 |
| sutil | GE | 2025 | 8 | 6,129.185 | 6,656.180 | 1.057 | 6,876.085 | 3,888.487 | 3 | 9 | -36.558 | 0.566 |
| sutil | GE | 2025 | 9 | 9,949.759 | 11,598.817 | 1.716 | 10,375.939 | 8,671.217 | 3 | 9 | -12.850 | 0.836 |
| sutil | GE | agregado_2021_2025 | 0 | 7,417.763 | 9,623.478 | 1.265 | 7,418.333 | 7,414.916 | 10 | 50 | -0.038 | 1.000 |
| sutil | GE | agregado_2021_2025 | 1 | 7,161.077 | 9,258.795 | 1.214 | 7,117.431 | 7,379.308 | 10 | 50 | 3.047 | 1.037 |
| sutil | GE | agregado_2021_2025 | 2 | 6,868.313 | 8,669.266 | 1.166 | 6,960.907 | 6,405.347 | 10 | 50 | -6.741 | 0.920 |
| sutil | GE | agregado_2021_2025 | 3 | 6,100.365 | 7,962.906 | 1.040 | 5,950.566 | 6,849.361 | 10 | 50 | 12.278 | 1.151 |
| sutil | GE | agregado_2021_2025 | 4 | 7,105.090 | 8,822.151 | 1.200 | 7,045.445 | 7,403.314 | 10 | 50 | 4.197 | 1.051 |
| sutil | GE | agregado_2021_2025 | 5 | 6,017.696 | 7,778.019 | 1.028 | 6,042.630 | 5,893.029 | 10 | 50 | -2.072 | 0.975 |
| sutil | GE | agregado_2021_2025 | 6 | 7,043.190 | 9,128.027 | 1.204 | 7,093.284 | 6,792.718 | 10 | 50 | -3.556 | 0.958 |
| sutil | GE | agregado_2021_2025 | 7 | 6,857.825 | 8,983.633 | 1.167 | 6,772.803 | 7,282.937 | 10 | 50 | 6.199 | 1.075 |
| sutil | GE | agregado_2021_2025 | 8 | 5,955.889 | 7,256.082 | 1.011 | 5,979.328 | 5,838.691 | 10 | 50 | -1.968 | 0.976 |
| sutil | GE | agregado_2021_2025 | 9 | 6,908.091 | 8,996.429 | 1.188 | 6,888.341 | 7,006.841 | 10 | 50 | 1.429 | 1.017 |
| dulce | XGB-37 | 2021 | 0 | 26.416 | 34.036 | 0.833 | 21.529 | 41.079 | 3 | 9 | 55.507 | 1.908 |
| dulce | XGB-37 | 2021 | 1 | 21.146 | 29.853 | 0.667 | 15.112 | 39.248 | 3 | 9 | 85.606 | 2.597 |
| dulce | XGB-37 | 2021 | 2 | 26.179 | 32.621 | 0.826 | 21.307 | 40.796 | 3 | 9 | 55.834 | 1.915 |
| dulce | XGB-37 | 2021 | 3 | 27.353 | 34.559 | 0.863 | 22.842 | 40.889 | 3 | 9 | 49.484 | 1.790 |
| dulce | XGB-37 | 2021 | 4 | 27.401 | 35.268 | 0.864 | 23.357 | 39.533 | 3 | 9 | 44.277 | 1.693 |
| dulce | XGB-37 | 2021 | 5 | 26.101 | 33.911 | 0.823 | 19.994 | 44.424 | 3 | 9 | 70.200 | 2.222 |
| dulce | XGB-37 | 2021 | 6 | 27.052 | 33.673 | 0.853 | 21.214 | 44.566 | 3 | 9 | 64.744 | 2.101 |
| dulce | XGB-37 | 2021 | 7 | 23.255 | 32.351 | 0.733 | 16.770 | 42.708 | 3 | 9 | 83.654 | 2.547 |
| dulce | XGB-37 | 2021 | 8 | 25.138 | 34.320 | 0.793 | 19.852 | 40.996 | 3 | 9 | 63.085 | 2.065 |
| dulce | XGB-37 | 2021 | 9 | 27.436 | 34.514 | 0.865 | 20.540 | 48.124 | 3 | 9 | 75.407 | 2.343 |
| dulce | XGB-37 | 2022 | 0 | 56.172 | 64.576 | 2.002 | 46.216 | 86.042 | 3 | 9 | 53.175 | 1.862 |
| dulce | XGB-37 | 2022 | 1 | 51.281 | 60.691 | 1.828 | 41.899 | 79.428 | 3 | 9 | 54.886 | 1.896 |
| dulce | XGB-37 | 2022 | 2 | 50.534 | 58.430 | 1.801 | 42.339 | 75.121 | 3 | 9 | 48.654 | 1.774 |
| dulce | XGB-37 | 2022 | 3 | 53.728 | 60.107 | 1.915 | 44.988 | 79.947 | 3 | 9 | 48.800 | 1.777 |
| dulce | XGB-37 | 2022 | 4 | 53.500 | 62.280 | 1.907 | 45.433 | 77.701 | 3 | 9 | 45.237 | 1.710 |
| dulce | XGB-37 | 2022 | 5 | 53.103 | 59.899 | 1.893 | 43.301 | 82.508 | 3 | 9 | 55.374 | 1.905 |
| dulce | XGB-37 | 2022 | 6 | 50.184 | 55.732 | 1.789 | 42.013 | 74.695 | 3 | 9 | 48.844 | 1.778 |
| dulce | XGB-37 | 2022 | 7 | 53.331 | 59.827 | 1.901 | 45.121 | 77.963 | 3 | 9 | 46.186 | 1.728 |
| dulce | XGB-37 | 2022 | 8 | 52.691 | 61.323 | 1.878 | 41.971 | 84.851 | 3 | 9 | 61.035 | 2.022 |
| dulce | XGB-37 | 2022 | 9 | 48.864 | 56.499 | 1.742 | 39.111 | 78.126 | 3 | 9 | 59.883 | 1.998 |
| dulce | XGB-37 | 2023 | 0 | 49.947 | 60.985 | 1.911 | 43.822 | 80.570 | 2 | 10 | 61.312 | 1.839 |
| dulce | XGB-37 | 2023 | 1 | 45.703 | 56.628 | 1.749 | 39.476 | 76.839 | 2 | 10 | 68.128 | 1.946 |
| dulce | XGB-37 | 2023 | 2 | 46.254 | 57.703 | 1.770 | 39.792 | 78.564 | 2 | 10 | 69.852 | 1.974 |
| dulce | XGB-37 | 2023 | 3 | 43.464 | 54.254 | 1.663 | 39.127 | 65.150 | 2 | 10 | 49.893 | 1.665 |
| dulce | XGB-37 | 2023 | 4 | 47.273 | 60.325 | 1.809 | 42.626 | 70.506 | 2 | 10 | 49.148 | 1.654 |
| dulce | XGB-37 | 2023 | 5 | 43.156 | 54.914 | 1.652 | 37.323 | 72.320 | 2 | 10 | 67.578 | 1.938 |
| dulce | XGB-37 | 2023 | 6 | 48.125 | 57.471 | 1.842 | 43.972 | 68.888 | 2 | 10 | 43.144 | 1.567 |
| dulce | XGB-37 | 2023 | 7 | 44.264 | 54.573 | 1.694 | 38.085 | 75.158 | 2 | 10 | 69.795 | 1.973 |
| dulce | XGB-37 | 2023 | 8 | 45.991 | 55.700 | 1.760 | 42.684 | 62.526 | 2 | 10 | 35.953 | 1.465 |
| dulce | XGB-37 | 2023 | 9 | 43.800 | 54.360 | 1.676 | 38.323 | 71.185 | 2 | 10 | 62.523 | 1.858 |
| dulce | XGB-37 | 2024 | 0 | 57.431 | 65.325 | 2.288 | 60.071 | 52.150 | 4 | 8 | -9.195 | 0.868 |
| dulce | XGB-37 | 2024 | 1 | 55.906 | 65.683 | 2.228 | 59.294 | 49.132 | 4 | 8 | -12.117 | 0.829 |
| dulce | XGB-37 | 2024 | 2 | 54.820 | 63.060 | 2.184 | 58.044 | 48.373 | 4 | 8 | -11.761 | 0.833 |
| dulce | XGB-37 | 2024 | 3 | 59.980 | 68.875 | 2.390 | 61.793 | 56.356 | 4 | 8 | -6.043 | 0.912 |
| dulce | XGB-37 | 2024 | 4 | 59.744 | 68.357 | 2.381 | 62.450 | 54.333 | 4 | 8 | -9.058 | 0.870 |
| dulce | XGB-37 | 2024 | 5 | 64.538 | 74.873 | 2.572 | 67.180 | 59.254 | 4 | 8 | -8.187 | 0.882 |
| dulce | XGB-37 | 2024 | 6 | 60.316 | 71.123 | 2.403 | 64.273 | 52.400 | 4 | 8 | -13.123 | 0.815 |
| dulce | XGB-37 | 2024 | 7 | 59.923 | 69.402 | 2.388 | 64.302 | 51.166 | 4 | 8 | -14.614 | 0.796 |
| dulce | XGB-37 | 2024 | 8 | 56.551 | 65.279 | 2.253 | 58.549 | 52.554 | 4 | 8 | -7.067 | 0.898 |
| dulce | XGB-37 | 2024 | 9 | 51.183 | 59.977 | 2.040 | 55.309 | 42.931 | 4 | 8 | -16.122 | 0.776 |
| dulce | XGB-37 | 2025 | 0 | 56.048 | 72.921 | 2.416 | 45.884 | 86.542 | 3 | 9 | 54.405 | 1.886 |
| dulce | XGB-37 | 2025 | 1 | 58.837 | 74.744 | 2.536 | 50.640 | 83.428 | 3 | 9 | 41.794 | 1.647 |
| dulce | XGB-37 | 2025 | 2 | 60.938 | 79.450 | 2.626 | 49.827 | 94.272 | 3 | 9 | 54.701 | 1.892 |
| dulce | XGB-37 | 2025 | 3 | 60.482 | 77.204 | 2.607 | 50.126 | 91.550 | 3 | 9 | 51.368 | 1.826 |
| dulce | XGB-37 | 2025 | 4 | 56.988 | 75.735 | 2.456 | 47.471 | 85.539 | 3 | 9 | 50.100 | 1.802 |
| dulce | XGB-37 | 2025 | 5 | 64.173 | 84.933 | 2.766 | 52.956 | 97.825 | 3 | 9 | 52.439 | 1.847 |
| dulce | XGB-37 | 2025 | 6 | 60.374 | 78.528 | 2.602 | 50.006 | 91.479 | 3 | 9 | 51.520 | 1.829 |
| dulce | XGB-37 | 2025 | 7 | 59.498 | 77.370 | 2.564 | 47.742 | 94.767 | 3 | 9 | 59.278 | 1.985 |
| dulce | XGB-37 | 2025 | 8 | 59.909 | 77.217 | 2.582 | 51.351 | 85.584 | 3 | 9 | 42.856 | 1.667 |
| dulce | XGB-37 | 2025 | 9 | 56.540 | 73.954 | 2.437 | 45.367 | 90.060 | 3 | 9 | 59.284 | 1.985 |
| dulce | XGB-37 | agregado_2021_2025 | 0 | 49.203 | 61.045 | 1.890 | 43.143 | 67.382 | 15 | 45 | 36.947 | 1.562 |
| dulce | XGB-37 | agregado_2021_2025 | 1 | 46.575 | 59.468 | 1.801 | 40.844 | 63.768 | 15 | 45 | 36.915 | 1.561 |
| dulce | XGB-37 | agregado_2021_2025 | 2 | 47.745 | 60.161 | 1.842 | 41.856 | 65.412 | 15 | 45 | 37.003 | 1.563 |
| dulce | XGB-37 | agregado_2021_2025 | 3 | 49.002 | 60.753 | 1.888 | 43.272 | 66.192 | 15 | 45 | 35.081 | 1.530 |
| dulce | XGB-37 | agregado_2021_2025 | 4 | 48.981 | 61.920 | 1.883 | 43.827 | 64.444 | 15 | 45 | 31.570 | 1.470 |
| dulce | XGB-37 | agregado_2021_2025 | 5 | 50.214 | 64.145 | 1.941 | 43.487 | 70.395 | 15 | 45 | 40.190 | 1.619 |
| dulce | XGB-37 | agregado_2021_2025 | 6 | 49.210 | 61.267 | 1.898 | 43.844 | 65.307 | 15 | 45 | 32.710 | 1.490 |
| dulce | XGB-37 | agregado_2021_2025 | 7 | 48.054 | 60.674 | 1.856 | 41.821 | 66.753 | 15 | 45 | 38.912 | 1.596 |
| dulce | XGB-37 | agregado_2021_2025 | 8 | 48.056 | 60.440 | 1.853 | 42.529 | 64.638 | 15 | 45 | 34.505 | 1.520 |
| dulce | XGB-37 | agregado_2021_2025 | 9 | 45.565 | 57.280 | 1.752 | 39.352 | 64.202 | 15 | 45 | 40.902 | 1.631 |
| dulce | XGB-43 | 2021 | 0 | 26.526 | 32.620 | 0.837 | 23.334 | 36.102 | 3 | 9 | 36.102 | 1.547 |
| dulce | XGB-43 | 2021 | 1 | 28.258 | 34.389 | 0.891 | 23.363 | 42.943 | 3 | 9 | 51.965 | 1.838 |
| dulce | XGB-43 | 2021 | 2 | 24.851 | 32.419 | 0.784 | 19.571 | 40.689 | 3 | 9 | 63.734 | 2.079 |
| dulce | XGB-43 | 2021 | 3 | 29.732 | 36.302 | 0.938 | 26.714 | 38.788 | 3 | 9 | 30.457 | 1.452 |
| dulce | XGB-43 | 2021 | 4 | 25.970 | 32.861 | 0.819 | 21.881 | 38.238 | 3 | 9 | 47.239 | 1.748 |
| dulce | XGB-43 | 2021 | 5 | 25.941 | 31.774 | 0.818 | 19.677 | 44.733 | 3 | 9 | 72.443 | 2.273 |
| dulce | XGB-43 | 2021 | 6 | 24.905 | 30.342 | 0.786 | 19.284 | 41.768 | 3 | 9 | 67.711 | 2.166 |
| dulce | XGB-43 | 2021 | 7 | 25.622 | 33.068 | 0.808 | 22.589 | 34.722 | 3 | 9 | 35.516 | 1.537 |
| dulce | XGB-43 | 2021 | 8 | 25.583 | 35.180 | 0.807 | 19.735 | 43.126 | 3 | 9 | 68.575 | 2.185 |
| dulce | XGB-43 | 2021 | 9 | 24.576 | 30.370 | 0.775 | 19.944 | 38.475 | 3 | 9 | 56.552 | 1.929 |
| dulce | XGB-43 | 2022 | 0 | 52.751 | 58.022 | 1.880 | 44.930 | 76.212 | 3 | 9 | 44.476 | 1.696 |
| dulce | XGB-43 | 2022 | 1 | 52.958 | 60.901 | 1.887 | 43.835 | 80.328 | 3 | 9 | 51.683 | 1.833 |
| dulce | XGB-43 | 2022 | 2 | 51.782 | 58.638 | 1.845 | 43.921 | 75.366 | 3 | 9 | 45.545 | 1.716 |
| dulce | XGB-43 | 2022 | 3 | 54.916 | 63.093 | 1.957 | 46.179 | 81.129 | 3 | 9 | 47.733 | 1.757 |
| dulce | XGB-43 | 2022 | 4 | 55.578 | 60.883 | 1.981 | 47.197 | 80.721 | 3 | 9 | 45.240 | 1.710 |
| dulce | XGB-43 | 2022 | 5 | 49.735 | 58.626 | 1.773 | 40.352 | 77.885 | 3 | 9 | 56.600 | 1.930 |
| dulce | XGB-43 | 2022 | 6 | 52.424 | 61.340 | 1.868 | 40.842 | 87.172 | 3 | 9 | 66.282 | 2.134 |
| dulce | XGB-43 | 2022 | 7 | 50.619 | 57.414 | 1.804 | 42.632 | 74.581 | 3 | 9 | 47.337 | 1.749 |
| dulce | XGB-43 | 2022 | 8 | 51.580 | 58.350 | 1.838 | 43.656 | 75.354 | 3 | 9 | 46.091 | 1.726 |
| dulce | XGB-43 | 2022 | 9 | 49.975 | 57.208 | 1.781 | 40.045 | 79.766 | 3 | 9 | 59.612 | 1.992 |
| dulce | XGB-43 | 2023 | 0 | 45.205 | 56.743 | 1.730 | 40.975 | 66.353 | 2 | 10 | 46.783 | 1.619 |
| dulce | XGB-43 | 2023 | 1 | 44.778 | 54.261 | 1.714 | 40.597 | 65.685 | 2 | 10 | 46.689 | 1.618 |
| dulce | XGB-43 | 2023 | 2 | 45.919 | 56.973 | 1.757 | 39.576 | 77.636 | 2 | 10 | 69.070 | 1.962 |
| dulce | XGB-43 | 2023 | 3 | 46.281 | 57.057 | 1.771 | 40.256 | 76.404 | 2 | 10 | 65.089 | 1.898 |
| dulce | XGB-43 | 2023 | 4 | 45.691 | 57.880 | 1.749 | 38.412 | 82.087 | 2 | 10 | 79.655 | 2.137 |
| dulce | XGB-43 | 2023 | 5 | 41.072 | 52.919 | 1.572 | 36.223 | 65.316 | 2 | 10 | 59.027 | 1.803 |
| dulce | XGB-43 | 2023 | 6 | 45.251 | 58.743 | 1.732 | 37.710 | 82.959 | 2 | 10 | 83.330 | 2.200 |
| dulce | XGB-43 | 2023 | 7 | 41.555 | 53.896 | 1.590 | 36.873 | 64.964 | 2 | 10 | 56.332 | 1.762 |
| dulce | XGB-43 | 2023 | 8 | 44.648 | 56.095 | 1.709 | 37.734 | 79.218 | 2 | 10 | 77.428 | 2.099 |
| dulce | XGB-43 | 2023 | 9 | 42.932 | 53.714 | 1.643 | 37.076 | 72.211 | 2 | 10 | 68.198 | 1.948 |
| dulce | XGB-43 | 2024 | 0 | 51.193 | 59.750 | 2.040 | 53.581 | 46.418 | 4 | 8 | -9.327 | 0.866 |
| dulce | XGB-43 | 2024 | 1 | 52.093 | 61.113 | 2.076 | 55.264 | 45.749 | 4 | 8 | -12.177 | 0.828 |
| dulce | XGB-43 | 2024 | 2 | 52.955 | 62.984 | 2.110 | 56.618 | 45.630 | 4 | 8 | -13.833 | 0.806 |
| dulce | XGB-43 | 2024 | 3 | 55.601 | 65.820 | 2.216 | 60.659 | 45.486 | 4 | 8 | -18.193 | 0.750 |
| dulce | XGB-43 | 2024 | 4 | 54.259 | 65.288 | 2.162 | 59.331 | 44.115 | 4 | 8 | -18.695 | 0.744 |
| dulce | XGB-43 | 2024 | 5 | 55.675 | 67.311 | 2.219 | 60.617 | 45.791 | 4 | 8 | -17.753 | 0.755 |
| dulce | XGB-43 | 2024 | 6 | 50.815 | 60.834 | 2.025 | 53.650 | 45.144 | 4 | 8 | -11.159 | 0.841 |
| dulce | XGB-43 | 2024 | 7 | 55.273 | 67.806 | 2.203 | 60.759 | 44.302 | 4 | 8 | -19.849 | 0.729 |
| dulce | XGB-43 | 2024 | 8 | 53.716 | 64.036 | 2.140 | 59.356 | 42.434 | 4 | 8 | -21.001 | 0.715 |
| dulce | XGB-43 | 2024 | 9 | 59.102 | 68.311 | 2.355 | 61.535 | 54.236 | 4 | 8 | -8.232 | 0.881 |
| dulce | XGB-43 | 2025 | 0 | 62.054 | 79.239 | 2.675 | 54.569 | 84.509 | 3 | 9 | 36.185 | 1.549 |
| dulce | XGB-43 | 2025 | 1 | 61.070 | 75.041 | 2.632 | 55.085 | 79.027 | 3 | 9 | 29.404 | 1.435 |
| dulce | XGB-43 | 2025 | 2 | 61.158 | 79.148 | 2.636 | 55.642 | 77.706 | 3 | 9 | 27.058 | 1.397 |
| dulce | XGB-43 | 2025 | 3 | 64.911 | 80.983 | 2.798 | 58.627 | 83.766 | 3 | 9 | 29.047 | 1.429 |
| dulce | XGB-43 | 2025 | 4 | 61.149 | 76.041 | 2.636 | 54.628 | 80.713 | 3 | 9 | 31.993 | 1.477 |
| dulce | XGB-43 | 2025 | 5 | 59.405 | 73.828 | 2.560 | 51.585 | 82.866 | 3 | 9 | 39.493 | 1.606 |
| dulce | XGB-43 | 2025 | 6 | 62.704 | 76.140 | 2.703 | 54.366 | 87.716 | 3 | 9 | 39.890 | 1.613 |
| dulce | XGB-43 | 2025 | 7 | 61.075 | 77.256 | 2.632 | 51.398 | 90.106 | 3 | 9 | 47.534 | 1.753 |
| dulce | XGB-43 | 2025 | 8 | 62.005 | 79.805 | 2.672 | 55.833 | 80.524 | 3 | 9 | 29.866 | 1.442 |
| dulce | XGB-43 | 2025 | 9 | 58.012 | 73.694 | 2.500 | 52.114 | 75.704 | 3 | 9 | 30.498 | 1.453 |
| dulce | XGB-43 | agregado_2021_2025 | 0 | 47.546 | 59.160 | 1.832 | 43.198 | 60.590 | 15 | 45 | 27.435 | 1.403 |
| dulce | XGB-43 | agregado_2021_2025 | 1 | 47.832 | 58.655 | 1.840 | 43.303 | 61.417 | 15 | 45 | 28.404 | 1.418 |
| dulce | XGB-43 | agregado_2021_2025 | 2 | 47.333 | 59.945 | 1.827 | 42.687 | 61.272 | 15 | 45 | 29.448 | 1.435 |
| dulce | XGB-43 | agregado_2021_2025 | 3 | 50.288 | 62.361 | 1.936 | 46.033 | 63.053 | 15 | 45 | 25.384 | 1.370 |
| dulce | XGB-43 | agregado_2021_2025 | 4 | 48.530 | 60.302 | 1.869 | 43.825 | 62.643 | 15 | 45 | 29.083 | 1.429 |
| dulce | XGB-43 | agregado_2021_2025 | 5 | 46.366 | 58.700 | 1.788 | 41.149 | 62.017 | 15 | 45 | 33.756 | 1.507 |
| dulce | XGB-43 | agregado_2021_2025 | 6 | 47.220 | 59.383 | 1.823 | 40.816 | 66.431 | 15 | 45 | 40.685 | 1.628 |
| dulce | XGB-43 | agregado_2021_2025 | 7 | 46.829 | 59.767 | 1.807 | 42.319 | 60.358 | 15 | 45 | 28.890 | 1.426 |
| dulce | XGB-43 | agregado_2021_2025 | 8 | 47.506 | 60.429 | 1.833 | 42.782 | 61.679 | 15 | 45 | 29.833 | 1.442 |
| dulce | XGB-43 | agregado_2021_2025 | 9 | 46.919 | 58.613 | 1.811 | 41.599 | 62.880 | 15 | 45 | 34.017 | 1.512 |
| dulce | GC3 | 2021 | 0 | 38.297 | 51.318 | 1.208 | 32.311 | 56.254 | 3 | 9 | 46.890 | 1.741 |
| dulce | GC3 | 2021 | 1 | 45.152 | 57.787 | 1.424 | 38.844 | 64.078 | 3 | 9 | 41.915 | 1.650 |
| dulce | GC3 | 2021 | 2 | 39.129 | 56.016 | 1.234 | 37.889 | 42.849 | 3 | 9 | 9.507 | 1.131 |
| dulce | GC3 | 2021 | 3 | 47.142 | 54.889 | 1.487 | 55.134 | 23.168 | 3 | 9 | -50.856 | 0.420 |
| dulce | GC3 | 2021 | 4 | 41.791 | 47.748 | 1.318 | 37.654 | 54.200 | 3 | 9 | 29.693 | 1.439 |
| dulce | GC3 | 2021 | 5 | 30.001 | 42.790 | 0.946 | 20.542 | 58.379 | 3 | 9 | 94.590 | 2.842 |
| dulce | GC3 | 2021 | 6 | 33.982 | 40.384 | 1.072 | 35.145 | 30.494 | 3 | 9 | -10.265 | 0.868 |
| dulce | GC3 | 2021 | 7 | 26.203 | 31.805 | 0.826 | 19.924 | 45.040 | 3 | 9 | 71.888 | 2.261 |
| dulce | GC3 | 2021 | 8 | 31.541 | 35.347 | 0.995 | 31.649 | 31.219 | 3 | 9 | -1.022 | 0.986 |
| dulce | GC3 | 2021 | 9 | 31.933 | 44.530 | 1.007 | 32.237 | 31.020 | 3 | 9 | -2.858 | 0.962 |
| dulce | GC3 | 2022 | 0 | 48.343 | 62.251 | 1.723 | 35.637 | 86.458 | 3 | 9 | 78.844 | 2.426 |
| dulce | GC3 | 2022 | 1 | 41.573 | 48.763 | 1.482 | 34.726 | 62.113 | 3 | 9 | 49.408 | 1.789 |
| dulce | GC3 | 2022 | 2 | 47.602 | 66.951 | 1.697 | 52.669 | 32.403 | 3 | 9 | -31.930 | 0.615 |
| dulce | GC3 | 2022 | 3 | 41.523 | 46.687 | 1.480 | 43.006 | 37.073 | 3 | 9 | -10.717 | 0.862 |
| dulce | GC3 | 2022 | 4 | 28.556 | 36.231 | 1.018 | 26.947 | 33.384 | 3 | 9 | 16.907 | 1.239 |
| dulce | GC3 | 2022 | 5 | 29.204 | 32.905 | 1.041 | 26.301 | 37.913 | 3 | 9 | 29.820 | 1.441 |
| dulce | GC3 | 2022 | 6 | 38.697 | 47.248 | 1.379 | 33.102 | 55.483 | 3 | 9 | 43.378 | 1.676 |
| dulce | GC3 | 2022 | 7 | 28.028 | 35.136 | 0.999 | 31.228 | 18.425 | 3 | 9 | -34.261 | 0.590 |
| dulce | GC3 | 2022 | 8 | 36.858 | 47.449 | 1.314 | 35.504 | 40.918 | 3 | 9 | 11.016 | 1.152 |
| dulce | GC3 | 2022 | 9 | 31.340 | 40.363 | 1.117 | 28.732 | 39.162 | 3 | 9 | 24.961 | 1.363 |
| dulce | GC3 | 2023 | 0 | 42.190 | 47.441 | 1.615 | 40.305 | 51.617 | 2 | 10 | 22.342 | 1.281 |
| dulce | GC3 | 2023 | 1 | 43.071 | 57.750 | 1.648 | 29.316 | 111.844 | 2 | 10 | 159.674 | 3.815 |
| dulce | GC3 | 2023 | 2 | 33.853 | 41.938 | 1.296 | 33.658 | 34.829 | 2 | 10 | 2.883 | 1.035 |
| dulce | GC3 | 2023 | 3 | 36.848 | 44.794 | 1.410 | 33.877 | 51.707 | 2 | 10 | 40.323 | 1.526 |
| dulce | GC3 | 2023 | 4 | 37.323 | 44.999 | 1.428 | 36.367 | 42.104 | 2 | 10 | 12.809 | 1.158 |
| dulce | GC3 | 2023 | 5 | 52.050 | 55.748 | 1.992 | 49.699 | 63.806 | 2 | 10 | 22.585 | 1.284 |
| dulce | GC3 | 2023 | 6 | 37.973 | 45.446 | 1.453 | 42.222 | 16.729 | 2 | 10 | -55.946 | 0.396 |
| dulce | GC3 | 2023 | 7 | 24.736 | 28.756 | 0.947 | 25.736 | 19.739 | 2 | 10 | -20.201 | 0.767 |
| dulce | GC3 | 2023 | 8 | 33.297 | 47.172 | 1.274 | 25.378 | 72.889 | 2 | 10 | 118.907 | 2.872 |
| dulce | GC3 | 2023 | 9 | 38.952 | 44.367 | 1.491 | 37.935 | 44.038 | 2 | 10 | 13.056 | 1.161 |
| dulce | GC3 | 2024 | 0 | 71.818 | 90.540 | 2.862 | 88.361 | 38.732 | 4 | 8 | -46.069 | 0.438 |
| dulce | GC3 | 2024 | 1 | 78.015 | 90.477 | 3.109 | 75.383 | 83.279 | 4 | 8 | 6.747 | 1.105 |
| dulce | GC3 | 2024 | 2 | 95.227 | 111.939 | 3.795 | 116.039 | 53.602 | 4 | 8 | -43.711 | 0.462 |
| dulce | GC3 | 2024 | 3 | 68.656 | 82.816 | 2.736 | 86.204 | 33.561 | 4 | 8 | -51.117 | 0.389 |
| dulce | GC3 | 2024 | 4 | 67.066 | 79.315 | 2.672 | 76.340 | 48.517 | 4 | 8 | -27.657 | 0.636 |
| dulce | GC3 | 2024 | 5 | 65.040 | 76.213 | 2.592 | 73.370 | 48.380 | 4 | 8 | -25.616 | 0.659 |
| dulce | GC3 | 2024 | 6 | 77.467 | 93.520 | 3.087 | 94.244 | 43.913 | 4 | 8 | -43.314 | 0.466 |
| dulce | GC3 | 2024 | 7 | 51.941 | 66.052 | 2.070 | 64.232 | 27.360 | 4 | 8 | -47.325 | 0.426 |
| dulce | GC3 | 2024 | 8 | 42.116 | 49.798 | 1.678 | 47.508 | 31.331 | 4 | 8 | -25.606 | 0.660 |
| dulce | GC3 | 2024 | 9 | 64.803 | 75.337 | 2.582 | 65.894 | 62.621 | 4 | 8 | -3.367 | 0.950 |
| dulce | GC3 | 2025 | 0 | 103.600 | 120.554 | 4.465 | 96.722 | 124.233 | 3 | 9 | 19.917 | 1.284 |
| dulce | GC3 | 2025 | 1 | 109.304 | 137.418 | 4.711 | 96.178 | 148.682 | 3 | 9 | 36.026 | 1.546 |
| dulce | GC3 | 2025 | 2 | 126.332 | 153.854 | 5.445 | 114.101 | 163.026 | 3 | 9 | 29.046 | 1.429 |
| dulce | GC3 | 2025 | 3 | 92.555 | 110.922 | 3.989 | 94.056 | 88.051 | 3 | 9 | -4.866 | 0.936 |
| dulce | GC3 | 2025 | 4 | 128.958 | 148.327 | 5.558 | 126.771 | 135.520 | 3 | 9 | 5.088 | 1.069 |
| dulce | GC3 | 2025 | 5 | 57.582 | 70.596 | 2.482 | 60.711 | 48.194 | 3 | 9 | -16.302 | 0.794 |
| dulce | GC3 | 2025 | 6 | 119.951 | 146.695 | 5.170 | 117.068 | 128.600 | 3 | 9 | 7.210 | 1.099 |
| dulce | GC3 | 2025 | 7 | 94.379 | 111.573 | 4.068 | 87.012 | 116.481 | 3 | 9 | 23.418 | 1.339 |
| dulce | GC3 | 2025 | 8 | 96.746 | 127.368 | 4.170 | 98.919 | 90.225 | 3 | 9 | -6.740 | 0.912 |
| dulce | GC3 | 2025 | 9 | 104.724 | 125.873 | 4.514 | 90.822 | 146.429 | 3 | 9 | 39.824 | 1.612 |
| dulce | GC3 | agregado_2021_2025 | 0 | 60.849 | 79.360 | 2.374 | 57.599 | 70.600 | 15 | 45 | 16.024 | 1.226 |
| dulce | GC3 | agregado_2021_2025 | 1 | 63.423 | 84.997 | 2.475 | 53.866 | 92.095 | 15 | 45 | 45.207 | 1.710 |
| dulce | GC3 | agregado_2021_2025 | 2 | 68.429 | 95.478 | 2.693 | 69.040 | 66.593 | 15 | 45 | -2.682 | 0.965 |
| dulce | GC3 | agregado_2021_2025 | 3 | 57.345 | 72.610 | 2.220 | 61.292 | 45.502 | 15 | 45 | -20.652 | 0.742 |
| dulce | GC3 | agregado_2021_2025 | 4 | 60.739 | 82.352 | 2.399 | 59.928 | 63.173 | 15 | 45 | 4.007 | 1.054 |
| dulce | GC3 | agregado_2021_2025 | 5 | 46.775 | 57.989 | 1.810 | 45.599 | 50.306 | 15 | 45 | 7.548 | 1.103 |
| dulce | GC3 | agregado_2021_2025 | 6 | 61.614 | 85.081 | 2.432 | 63.200 | 56.856 | 15 | 45 | -7.723 | 0.900 |
| dulce | GC3 | agregado_2021_2025 | 7 | 45.057 | 63.062 | 1.782 | 44.771 | 45.917 | 15 | 45 | 1.908 | 1.026 |
| dulce | GC3 | agregado_2021_2025 | 8 | 48.111 | 69.898 | 1.886 | 47.300 | 50.546 | 15 | 45 | 5.060 | 1.069 |
| dulce | GC3 | agregado_2021_2025 | 9 | 54.350 | 73.621 | 2.142 | 50.503 | 65.893 | 15 | 45 | 21.238 | 1.305 |
| dulce | GE | 2021 | 0 | 36.202 | 50.808 | 1.142 | 28.824 | 58.335 | 3 | 9 | 61.138 | 2.024 |
| dulce | GE | 2021 | 1 | 54.934 | 80.138 | 1.733 | 46.737 | 79.526 | 3 | 9 | 44.765 | 1.702 |
| dulce | GE | 2021 | 2 | 44.635 | 67.046 | 1.408 | 43.940 | 46.718 | 3 | 9 | 4.667 | 1.063 |
| dulce | GE | 2021 | 3 | 52.363 | 56.933 | 1.652 | 60.247 | 28.710 | 3 | 9 | -45.170 | 0.477 |
| dulce | GE | 2021 | 4 | 41.052 | 48.661 | 1.295 | 40.659 | 42.232 | 3 | 9 | 2.874 | 1.039 |
| dulce | GE | 2021 | 5 | 53.602 | 59.001 | 1.691 | 49.854 | 64.846 | 3 | 9 | 20.977 | 1.301 |
| dulce | GE | 2021 | 6 | 35.619 | 40.178 | 1.123 | 36.525 | 32.903 | 3 | 9 | -7.627 | 0.901 |
| dulce | GE | 2021 | 7 | 28.472 | 34.178 | 0.898 | 28.086 | 29.633 | 3 | 9 | 4.075 | 1.055 |
| dulce | GE | 2021 | 8 | 24.529 | 29.618 | 0.774 | 25.682 | 21.069 | 3 | 9 | -14.106 | 0.820 |
| dulce | GE | 2021 | 9 | 39.299 | 56.935 | 1.240 | 41.124 | 33.824 | 3 | 9 | -13.931 | 0.822 |
| dulce | GE | 2022 | 0 | 48.650 | 63.626 | 1.734 | 36.300 | 85.702 | 3 | 9 | 76.159 | 2.361 |
| dulce | GE | 2022 | 1 | 43.726 | 51.730 | 1.558 | 36.096 | 66.615 | 3 | 9 | 52.346 | 1.845 |
| dulce | GE | 2022 | 2 | 45.395 | 66.565 | 1.618 | 52.675 | 23.556 | 3 | 9 | -48.109 | 0.447 |
| dulce | GE | 2022 | 3 | 41.839 | 47.685 | 1.491 | 42.109 | 41.028 | 3 | 9 | -1.937 | 0.974 |
| dulce | GE | 2022 | 4 | 29.513 | 39.069 | 1.052 | 26.834 | 37.548 | 3 | 9 | 27.226 | 1.399 |
| dulce | GE | 2022 | 5 | 33.479 | 39.366 | 1.193 | 33.567 | 33.215 | 3 | 9 | -0.788 | 0.990 |
| dulce | GE | 2022 | 6 | 42.012 | 51.978 | 1.497 | 35.515 | 61.505 | 3 | 9 | 46.398 | 1.732 |
| dulce | GE | 2022 | 7 | 32.951 | 39.532 | 1.174 | 36.903 | 21.095 | 3 | 9 | -35.980 | 0.572 |
| dulce | GE | 2022 | 8 | 26.900 | 35.104 | 0.959 | 27.981 | 23.656 | 3 | 9 | -12.058 | 0.845 |
| dulce | GE | 2022 | 9 | 30.827 | 39.378 | 1.099 | 30.014 | 33.266 | 3 | 9 | 7.911 | 1.108 |
| dulce | GE | 2023 | 0 | 49.354 | 57.071 | 1.889 | 43.168 | 80.282 | 2 | 10 | 62.666 | 1.860 |
| dulce | GE | 2023 | 1 | 46.685 | 58.426 | 1.787 | 36.075 | 99.731 | 2 | 10 | 113.628 | 2.765 |
| dulce | GE | 2023 | 2 | 37.648 | 48.363 | 1.441 | 32.950 | 61.134 | 2 | 10 | 62.385 | 1.855 |
| dulce | GE | 2023 | 3 | 40.683 | 49.171 | 1.557 | 37.179 | 58.202 | 2 | 10 | 43.062 | 1.565 |
| dulce | GE | 2023 | 4 | 40.047 | 48.927 | 1.533 | 44.018 | 20.192 | 2 | 10 | -49.580 | 0.459 |
| dulce | GE | 2023 | 5 | 47.581 | 52.166 | 1.821 | 44.813 | 61.422 | 2 | 10 | 29.088 | 1.371 |
| dulce | GE | 2023 | 6 | 40.162 | 47.173 | 1.537 | 43.154 | 25.199 | 2 | 10 | -37.255 | 0.584 |
| dulce | GE | 2023 | 7 | 36.629 | 48.799 | 1.402 | 42.660 | 6.477 | 2 | 10 | -82.317 | 0.152 |
| dulce | GE | 2023 | 8 | 46.835 | 55.357 | 1.792 | 41.883 | 71.596 | 2 | 10 | 52.868 | 1.709 |
| dulce | GE | 2023 | 9 | 36.742 | 42.677 | 1.406 | 35.851 | 41.197 | 2 | 10 | 12.124 | 1.149 |
| dulce | GE | 2024 | 0 | 74.894 | 88.908 | 2.984 | 85.934 | 52.814 | 4 | 8 | -29.481 | 0.615 |
| dulce | GE | 2024 | 1 | 76.451 | 85.313 | 3.046 | 77.334 | 74.686 | 4 | 8 | -2.309 | 0.966 |
| dulce | GE | 2024 | 2 | 95.537 | 110.514 | 3.807 | 112.018 | 62.575 | 4 | 8 | -34.501 | 0.559 |
| dulce | GE | 2024 | 3 | 69.268 | 83.407 | 2.760 | 87.555 | 32.694 | 4 | 8 | -52.800 | 0.373 |
| dulce | GE | 2024 | 4 | 74.658 | 87.931 | 2.975 | 87.045 | 49.885 | 4 | 8 | -33.182 | 0.573 |
| dulce | GE | 2024 | 5 | 61.091 | 73.377 | 2.434 | 65.117 | 53.040 | 4 | 8 | -13.179 | 0.815 |
| dulce | GE | 2024 | 6 | 72.111 | 84.753 | 2.873 | 90.745 | 34.842 | 4 | 8 | -51.682 | 0.384 |
| dulce | GE | 2024 | 7 | 55.902 | 62.942 | 2.228 | 58.488 | 50.730 | 4 | 8 | -9.252 | 0.867 |
| dulce | GE | 2024 | 8 | 35.545 | 49.962 | 1.416 | 37.286 | 32.064 | 4 | 8 | -9.792 | 0.860 |
| dulce | GE | 2024 | 9 | 57.057 | 68.889 | 2.274 | 52.323 | 66.525 | 4 | 8 | 16.594 | 1.271 |
| dulce | GE | 2025 | 0 | 86.383 | 103.149 | 3.723 | 82.485 | 98.077 | 3 | 9 | 13.537 | 1.189 |
| dulce | GE | 2025 | 1 | 107.542 | 137.628 | 4.635 | 96.705 | 140.053 | 3 | 9 | 30.231 | 1.448 |
| dulce | GE | 2025 | 2 | 117.683 | 137.085 | 5.072 | 109.455 | 142.367 | 3 | 9 | 20.975 | 1.301 |
| dulce | GE | 2025 | 3 | 77.840 | 98.766 | 3.355 | 80.820 | 68.899 | 3 | 9 | -11.486 | 0.852 |
| dulce | GE | 2025 | 4 | 103.513 | 124.375 | 4.461 | 102.448 | 106.708 | 3 | 9 | 3.086 | 1.042 |
| dulce | GE | 2025 | 5 | 53.722 | 67.119 | 2.315 | 58.819 | 38.428 | 3 | 9 | -28.468 | 0.653 |
| dulce | GE | 2025 | 6 | 115.941 | 144.022 | 4.997 | 122.679 | 95.729 | 3 | 9 | -17.434 | 0.780 |
| dulce | GE | 2025 | 7 | 103.617 | 127.580 | 4.466 | 95.986 | 126.507 | 3 | 9 | 22.092 | 1.318 |
| dulce | GE | 2025 | 8 | 83.099 | 99.462 | 3.582 | 91.474 | 57.977 | 3 | 9 | -30.232 | 0.634 |
| dulce | GE | 2025 | 9 | 106.505 | 129.812 | 4.590 | 100.563 | 124.332 | 3 | 9 | 16.737 | 1.236 |
| dulce | GE | agregado_2021_2025 | 0 | 59.097 | 75.407 | 2.294 | 54.392 | 73.211 | 15 | 45 | 23.883 | 1.346 |
| dulce | GE | agregado_2021_2025 | 1 | 65.868 | 88.013 | 2.552 | 57.673 | 90.453 | 15 | 45 | 37.325 | 1.568 |
| dulce | GE | agregado_2021_2025 | 2 | 68.180 | 91.946 | 2.669 | 68.451 | 67.366 | 15 | 45 | -1.193 | 0.984 |
| dulce | GE | agregado_2021_2025 | 3 | 56.398 | 70.206 | 2.163 | 60.462 | 44.206 | 15 | 45 | -21.618 | 0.731 |
| dulce | GE | agregado_2021_2025 | 4 | 57.757 | 76.797 | 2.263 | 59.245 | 53.292 | 15 | 45 | -7.729 | 0.900 |
| dulce | GE | agregado_2021_2025 | 5 | 49.895 | 59.399 | 1.891 | 49.983 | 49.631 | 15 | 45 | -0.528 | 0.993 |
| dulce | GE | agregado_2021_2025 | 6 | 61.169 | 83.026 | 2.406 | 64.666 | 50.678 | 15 | 45 | -17.150 | 0.784 |
| dulce | GE | agregado_2021_2025 | 7 | 51.514 | 71.205 | 2.034 | 52.073 | 49.839 | 15 | 45 | -3.253 | 0.957 |
| dulce | GE | agregado_2021_2025 | 8 | 43.382 | 59.267 | 1.705 | 44.963 | 38.637 | 15 | 45 | -10.937 | 0.859 |
| dulce | GE | agregado_2021_2025 | 9 | 54.086 | 75.114 | 2.122 | 51.609 | 61.517 | 15 | 45 | 13.739 | 1.192 |

### T11_ablacion_GE_menos_GC3.csv — T11 completa: ablación GE − GC3 con la diferencia de cada semilla

`06_metricas/ablacion_nlp/T11_ablacion_GE_menos_GC3.csv` — 42 filas × 21 columnas.

| cultivar | conjunto | alcance | n_meses | dif_media_GE_menos_GC3 | IC95_lo | IC95_hi | sd_entre_semillas | min_semilla | max_semilla | semillas_GE_mejor | seed_00 | seed_01 | seed_02 | seed_03 | seed_04 | seed_05 | seed_06 | seed_07 | seed_08 | seed_09 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| sutil | 2021 | global | 12 | 11.141 | -163.762 | 172.803 | 755.699 | -1,234.121 | 1,272.174 | 6.000 | -314.996 | 793.867 | 137.201 | -154.694 | 1,272.174 | -77.120 | -113.174 | 672.174 | -869.895 | -1,234.121 |
| sutil | 2021 | shock_P75 | 0 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| sutil | 2021 | normal_P75 | 12 | 11.141 | -163.762 | 172.803 | 755.699 | -1,234.121 | 1,272.174 | 6.000 | -314.996 | 793.867 | 137.201 | -154.694 | 1,272.174 | -77.120 | -113.174 | 672.174 | -869.895 | -1,234.121 |
| sutil | 2022 | global | 12 | 97.666 | -541.939 | 730.142 | 443.979 | -754.111 | 717.752 | 3.000 | 623.698 | -347.942 | 62.412 | 433.304 | 191.225 | 8.326 | -131.261 | 173.254 | 717.752 | -754.111 |
| sutil | 2022 | shock_P75 | 3 | 285.873 | -1,354.245 | 1,261.284 | 412.690 | -403.123 | 938.513 | 2.000 | 938.513 | -403.123 | -283.983 | 576.035 | 306.059 | 175.742 | 728.037 | 369.997 | 246.663 | 204.791 |
| sutil | 2022 | normal_P75 | 9 | 34.930 | -674.977 | 741.277 | 545.264 | -1,073.745 | 874.782 | 4.000 | 518.760 | -329.548 | 177.877 | 385.727 | 152.947 | -47.479 | -417.694 | 107.673 | 874.782 | -1,073.745 |
| sutil | 2023 | global | 12 | -683.158 | -1,263.270 | -87.564 | 591.562 | -1,713.272 | 407.939 | 9.000 | -310.508 | 407.939 | -660.380 | -715.017 | -968.712 | -138.329 | -1,168.614 | -1,031.093 | -1,713.272 | -533.591 |
| sutil | 2023 | shock_P75 | 4 | -69.722 | -940.387 | 800.943 | 859.453 | -1,221.129 | 1,172.025 | 5.000 | 950.401 | 852.962 | -787.241 | -335.395 | -1,221.129 | 1,172.025 | -792.175 | 292.050 | -868.493 | 39.773 |
| sutil | 2023 | normal_P75 | 8 | -989.875 | -1,608.349 | -323.826 | 630.326 | -2,135.661 | 185.428 | 9.000 | -940.962 | 185.428 | -596.949 | -904.827 | -842.504 | -793.506 | -1,356.834 | -1,692.665 | -2,135.661 | -820.272 |
| sutil | 2024 | global | 12 | 805.019 | 528.605 | 1,103.857 | 734.151 | -588.140 | 2,355.648 | 1.000 | 1,115.198 | -588.140 | 856.316 | 974.512 | 733.120 | 788.029 | 1,012.522 | 444.564 | 358.423 | 2,355.648 |
| sutil | 2024 | shock_P75 | 0 | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| sutil | 2024 | normal_P75 | 12 | 805.019 | 528.605 | 1,103.857 | 734.151 | -588.140 | 2,355.648 | 1.000 | 1,115.198 | -588.140 | 856.316 | 974.512 | 733.120 | 788.029 | 1,012.522 | 444.564 | 358.423 | 2,355.648 |
| sutil | 2025 | global | 12 | 1,680.459 | 299.811 | 3,044.816 | 1,321.539 | -101.112 | 4,189.169 | 1.000 | 3,142.583 | 1,586.244 | 1,468.491 | 751.267 | 1,639.869 | 2,742.005 | 451.152 | 934.917 | -101.112 | 4,189.169 |
| sutil | 2025 | shock_P75 | 3 | 2,314.379 | 111.517 | 4,888.946 | 1,715.875 | -503.600 | 4,731.400 | 1.000 | 3,743.633 | 2,055.659 | 2,726.039 | 2,940.825 | 4,348.246 | 1,820.593 | 468.388 | 812.606 | -503.600 | 4,731.400 |
| sutil | 2025 | normal_P75 | 9 | 1,469.152 | -165.372 | 3,118.037 | 1,385.556 | 21.415 | 4,008.426 | 0.000 | 2,942.233 | 1,429.772 | 1,049.308 | 21.415 | 737.076 | 3,049.142 | 445.407 | 975.687 | 33.051 | 4,008.426 |
| sutil | principal_2021_2025 | global | 60 | 382.225 | 44.634 | 711.420 | 362.827 | -321.621 | 851.195 | 1.000 | 851.195 | 370.394 | 372.808 | 257.874 | 573.535 | 664.582 | 10.125 | 238.763 | -321.621 | 804.599 |
| sutil | principal_2021_2025 | shock_P75 | 10 | 752.187 | -88.167 | 1,607.460 | 654.858 | -424.479 | 1,784.804 | 1.000 | 1,784.804 | 836.945 | 417.720 | 920.900 | 907.840 | 1,067.711 | 42.058 | 471.601 | -424.479 | 1,496.766 |
| sutil | principal_2021_2025 | normal_P75 | 50 | 308.233 | -32.856 | 647.668 | 313.647 | -301.049 | 666.166 | 1.000 | 664.473 | 277.083 | 363.826 | 125.269 | 506.674 | 583.956 | 3.738 | 192.196 | -301.049 | 666.166 |
| sutil | sensibilidad_2023_2025 | global | 36 | 600.773 | 88.926 | 1,095.938 | 709.765 | -485.320 | 2,003.742 | 1.000 | 1,315.758 | 468.681 | 554.809 | 336.921 | 468.092 | 1,130.568 | 98.353 | 116.129 | -485.320 | 2,003.742 |
| sutil | sensibilidad_2023_2025 | shock_P75 | 7 | 952.035 | -80.637 | 2,062.094 | 917.766 | -712.111 | 2,147.501 | 2.000 | 2,147.501 | 1,368.403 | 718.451 | 1,068.699 | 1,165.746 | 1,449.983 | -251.933 | 515.146 | -712.111 | 2,050.470 |
| sutil | sensibilidad_2023_2025 | normal_P75 | 29 | 515.986 | -38.981 | 1,072.106 | 693.145 | -430.578 | 1,992.463 | 1.000 | 1,114.992 | 251.507 | 515.310 | 160.285 | 299.693 | 1,053.468 | 182.905 | 19.815 | -430.578 | 1,992.463 |
| dulce | 2021 | global | 12 | 4.554 | -0.565 | 9.519 | 8.294 | -7.013 | 23.601 | 3.000 | -2.095 | 9.782 | 5.506 | 5.220 | -0.739 | 23.601 | 1.637 | 2.269 | -7.013 | 7.366 |
| dulce | 2021 | shock_P75 | 3 | 0.110 | -11.808 | 18.448 | 9.590 | -15.407 | 15.448 | 3.000 | 2.081 | 15.448 | 3.869 | 5.543 | -11.968 | 6.467 | 2.408 | -15.407 | -10.150 | 2.804 |
| dulce | 2021 | normal_P75 | 9 | 6.035 | 1.598 | 10.108 | 9.570 | -5.967 | 29.312 | 2.000 | -3.487 | 7.894 | 6.051 | 5.113 | 3.004 | 29.312 | 1.380 | 8.161 | -5.967 | 8.887 |
| dulce | 2022 | global | 12 | 0.357 | -1.529 | 2.129 | 4.246 | -9.958 | 4.923 | 3.000 | 0.308 | 2.153 | -2.207 | 0.316 | 0.956 | 4.275 | 3.315 | 4.923 | -9.958 | -0.512 |
| dulce | 2022 | shock_P75 | 3 | -1.615 | -6.109 | 1.979 | 7.485 | -17.262 | 6.022 | 5.000 | -0.756 | 4.502 | -8.847 | 3.955 | 4.164 | -4.698 | 6.022 | 2.670 | -17.262 | -5.896 |
| dulce | 2022 | normal_P75 | 9 | 1.014 | -0.867 | 2.835 | 3.971 | -7.523 | 7.265 | 3.000 | 0.662 | 1.370 | 0.006 | -0.897 | -0.113 | 7.265 | 2.413 | 5.674 | -7.523 | 1.282 |
| dulce | 2023 | global | 12 | 4.207 | 1.914 | 6.332 | 5.561 | -4.469 | 13.538 | 2.000 | 7.164 | 3.614 | 3.794 | 3.835 | 2.724 | -4.469 | 2.188 | 11.893 | 13.538 | -2.210 |
| dulce | 2023 | shock_P75 | 2 | 1.613 | 1.483 | 1.743 | 16.397 | -21.912 | 28.665 | 6.000 | 28.665 | -12.113 | 26.305 | 6.495 | -21.912 | -2.384 | 8.471 | -13.262 | -1.293 | -2.841 |
| dulce | 2023 | normal_P75 | 10 | 4.726 | 1.997 | 7.061 | 7.367 | -4.886 | 16.924 | 3.000 | 2.863 | 6.759 | -0.708 | 3.303 | 7.651 | -4.886 | 0.932 | 16.924 | 16.504 | -2.084 |
| dulce | 2024 | global | 12 | -0.963 | -6.362 | 4.414 | 4.988 | -7.746 | 7.593 | 5.000 | 3.076 | -1.564 | 0.310 | 0.612 | 7.593 | -3.949 | -5.357 | 3.961 | -6.570 | -7.746 |
| dulce | 2024 | shock_P75 | 4 | 3.856 | -0.014 | 7.727 | 9.846 | -9.071 | 23.370 | 3.000 | 14.082 | -8.593 | 8.974 | -0.867 | 1.368 | 4.660 | -9.071 | 23.370 | 0.733 | 3.904 |
| dulce | 2024 | normal_P75 | 8 | -3.373 | -10.360 | 4.278 | 6.916 | -13.571 | 10.705 | 7.000 | -2.427 | 1.951 | -4.021 | 1.351 | 10.705 | -8.253 | -3.500 | -5.744 | -10.222 | -13.571 |
| dulce | 2025 | global | 12 | -7.828 | -13.029 | -3.193 | 10.172 | -25.445 | 9.238 | 8.000 | -17.217 | -1.762 | -8.649 | -14.715 | -25.445 | -3.860 | -4.009 | 9.238 | -13.646 | 1.781 |
| dulce | 2025 | shock_P75 | 3 | -19.037 | -27.262 | -13.052 | 13.179 | -32.871 | 10.026 | 9.000 | -26.156 | -8.629 | -20.660 | -19.152 | -28.812 | -9.766 | -32.871 | 10.026 | -32.249 | -22.098 |
| dulce | 2025 | normal_P75 | 9 | -4.092 | -7.843 | -0.446 | 11.004 | -24.323 | 9.741 | 6.000 | -14.237 | 0.527 | -4.646 | -13.236 | -24.323 | -1.891 | 5.611 | 8.975 | -7.446 | 9.741 |
| dulce | principal_2021_2025 | global | 60 | 0.065 | -1.851 | 1.896 | 3.213 | -4.730 | 6.457 | 7.000 | -1.753 | 2.445 | -0.249 | -0.947 | -2.982 | 3.119 | -0.445 | 6.457 | -4.730 | -0.264 |
| dulce | principal_2021_2025 | shock_P75 | 15 | -2.865 | -6.151 | 0.702 | 5.189 | -11.909 | 3.922 | 7.000 | 2.611 | -1.642 | 0.773 | -1.296 | -9.880 | -0.675 | -6.177 | 3.922 | -11.909 | -4.376 |
| dulce | principal_2021_2025 | normal_P75 | 45 | 1.042 | -0.746 | 2.917 | 3.280 | -3.208 | 7.302 | 5.000 | -3.208 | 3.807 | -0.590 | -0.830 | -0.683 | 4.384 | 1.466 | 7.302 | -2.337 | 1.106 |
| dulce | sensibilidad_2023_2025 | global | 36 | -1.528 | -4.160 | 0.943 | 3.746 | -5.043 | 8.364 | 8.000 | -2.326 | 0.096 | -1.515 | -3.423 | -5.043 | -4.093 | -2.393 | 8.364 | -2.226 | -2.725 |
| dulce | sensibilidad_2023_2025 | shock_P75 | 9 | -4.273 | -7.181 | -1.499 | 8.131 | -13.865 | 10.782 | 7.000 | 3.910 | -9.387 | 2.947 | -5.326 | -13.865 | -1.714 | -13.106 | 10.782 | -10.711 | -6.262 |
| dulce | sensibilidad_2023_2025 | normal_P75 | 27 | -0.613 | -3.203 | 2.065 | 3.838 | -4.886 | 7.558 | 6.000 | -4.404 | 3.257 | -3.002 | -2.789 | -2.102 | -4.886 | 1.179 | 7.558 | 0.602 | -1.546 |

### T12_delta_s_quitando_un_shock.csv — T12 completa: Δs quitando un mes de shock, por ventana y agregado

`06_metricas/agregadas/T12_delta_s_quitando_un_shock.csv` — 132 filas × 10 columnas.

| cultivar | modelo | ventana | n_shock | Delta_s | Delta_s_loo_min | Delta_s_loo_max | mes_que_mas_cambia | Delta_s_loo | exploratorio |
|---|---|---|---|---|---|---|---|---|---|
| sutil | Naive | 2021 | 0 | — | — | — | — | — | no |
| sutil | Naive | 2022 | 3 | 126.524 | 140.054 | 174.741 | 2022-12 | 2022-01:140.0545;2022-06:150.9173;2022-12:174.7408 | no |
| sutil | Naive | 2023 | 4 | 33.533 | 32.825 | 45.585 | 2023-09 | 2023-08:36.7956;2023-09:45.5848;2023-11:32.8254;2023-12:35.3106 | no |
| sutil | Naive | 2024 | 0 | — | — | — | — | — | no |
| sutil | Naive | 2025 | 3 | 147.862 | 183.575 | 189.709 | 2025-07 | 2025-01:185.7034;2025-07:189.7086;2025-11:183.5755 | no |
| sutil | Naive | agregado_2021_2025 | 10 | 134.714 | 132.873 | 148.223 | 2023-09 | 2022-01:136.3945;2022-06:138.9338;2022-12:145.0747;2023-08:144.4836;2023-09:148.2228;2023-11:142.8657;2023-12:143.8734;2025-01:133.6063;2025-07:135.0121;2025-11:132.8729 | no |
| sutil | Seasonal Naive | 2021 | 0 | — | — | — | — | — | no |
| sutil | Seasonal Naive | 2022 | 3 | 8.106 | -42.569 | 40.753 | 2022-01 | 2022-01:-42.5686;2022-06:20.3764;2022-12:40.7531 | no |
| sutil | Seasonal Naive | 2023 | 4 | -19.677 | -48.396 | -2.212 | 2023-08 | 2023-08:-48.3964;2023-09:-35.1288;2023-11:-2.2121;2023-12:-4.0368 | no |
| sutil | Seasonal Naive | 2024 | 0 | — | — | — | — | — | no |
| sutil | Seasonal Naive | 2025 | 3 | -0.731 | -55.400 | 23.522 | 2025-11 | 2025-01:21.0838;2025-07:23.5224;2025-11:-55.4003 | no |
| sutil | Seasonal Naive | agregado_2021_2025 | 10 | -17.127 | -31.265 | -9.657 | 2023-08 | 2022-01:-24.0703;2022-06:-14.5620;2022-12:-10.9411;2023-08:-31.2645;2023-09:-25.5784;2023-11:-9.6567;2023-12:-10.6153;2025-01:-12.2475;2025-07:-11.8170;2025-11:-23.8832 | no |
| sutil | Chronos | 2021 | 0 | — | — | — | — | — | no |
| sutil | Chronos | 2022 | 3 | 120.047 | 100.530 | 181.253 | 2022-12 | 2022-01:100.5297;2022-06:148.6747;2022-12:181.2527 | no |
| sutil | Chronos | 2023 | 4 | 9.409 | 0.372 | 17.360 | 2023-08 | 2023-08:0.3723;2023-09:10.2065;2023-11:12.8752;2023-12:17.3604 | no |
| sutil | Chronos | 2024 | 0 | — | — | — | — | — | no |
| sutil | Chronos | 2025 | 3 | 95.620 | 109.579 | 120.061 | 2025-07 | 2025-01:109.5793;2025-07:120.0612;2025-11:112.9175 | no |
| sutil | Chronos | agregado_2021_2025 | 10 | 80.609 | 73.917 | 91.201 | 2022-12 | 2022-01:73.9169;2022-06:83.2680;2022-12:91.2008;2023-08:83.2303;2023-09:87.0919;2023-11:88.1799;2023-12:90.0491;2025-01:76.3956;2025-07:79.6639;2025-11:77.4192 | no |
| sutil | SARIMA | 2021 | 0 | — | — | — | — | — | no |
| sutil | SARIMA | 2022 | 3 | 27.583 | -50.414 | 74.830 | 2022-01 | 2022-01:-50.4145;2022-06:49.0017;2022-12:74.8305 | no |
| sutil | SARIMA | 2023 | 4 | 9.131 | 1.841 | 27.193 | 2023-12 | 2023-08:1.8406;2023-09:4.2134;2023-11:5.2302;2023-12:27.1927 | no |
| sutil | SARIMA | 2024 | 0 | — | — | — | — | — | no |
| sutil | SARIMA | 2025 | 3 | 96.346 | 110.589 | 121.174 | 2025-07 | 2025-01:110.5888;2025-07:121.1740;2025-11:113.6399 | no |
| sutil | SARIMA | agregado_2021_2025 | 10 | 52.664 | 43.337 | 66.658 | 2022-12 | 2022-01:43.3373;2022-06:60.8620;2022-12:66.6584;2023-08:53.6643;2023-09:54.5647;2023-11:54.9545;2023-12:64.0081;2025-01:45.6417;2025-07:48.9704;2025-11:46.5841 | no |
| sutil | SARIMA-sel | 2021 | 0 | — | — | — | — | — | no |
| sutil | SARIMA-sel | 2022 | 3 | 61.206 | -33.150 | 114.942 | 2022-01 | 2022-01:-33.1496;2022-06:114.9415;2022-12:99.7469 | no |
| sutil | SARIMA-sel | 2023 | 4 | 8.415 | -35.060 | 31.959 | 2023-08 | 2023-08:-35.0602;2023-09:17.7051;2023-11:13.3398;2023-12:31.9589 | no |
| sutil | SARIMA-sel | 2024 | 0 | — | — | — | — | — | no |
| sutil | SARIMA-sel | 2025 | 3 | 69.788 | 55.297 | 103.541 | 2025-07 | 2025-01:81.8890;2025-07:103.5412;2025-11:55.2970 | no |
| sutil | SARIMA-sel | agregado_2021_2025 | 10 | 53.959 | 40.622 | 67.942 | 2023-12 | 2022-01:41.3952;2022-06:66.6190;2022-12:63.2004;2023-08:40.6222;2023-09:61.1813;2023-11:59.2287;2023-12:67.9421;2025-01:50.8032;2025-07:57.6274;2025-11:43.2338 | no |
| sutil | Ridge | 2021 | 0 | — | — | — | — | — | no |
| sutil | Ridge | 2022 | 3 | 37.866 | -27.603 | 72.439 | 2022-01 | 2022-01:-27.6033;2022-06:72.4391;2022-12:68.9995 | no |
| sutil | Ridge | 2023 | 4 | 17.967 | -13.336 | 37.403 | 2023-11 | 2023-08:22.9177;2023-09:27.1800;2023-11:-13.3360;2023-12:37.4033 | no |
| sutil | Ridge | 2024 | 0 | — | — | — | — | — | no |
| sutil | Ridge | 2025 | 3 | 122.086 | 139.099 | 165.698 | 2025-11 | 2025-01:139.0993;2025-07:143.2403;2025-11:165.6981 | no |
| sutil | Ridge | agregado_2021_2025 | 10 | 73.739 | 43.819 | 87.076 | 2023-11 | 2022-01:74.5542;2022-06:87.0761;2022-12:86.5499;2023-08:71.3383;2023-09:74.8913;2023-11:43.8190;2023-12:83.7203;2025-01:76.4245;2025-07:77.1105;2025-11:81.1394 | no |
| sutil | ElasticNet | 2021 | 0 | — | — | — | — | — | no |
| sutil | ElasticNet | 2022 | 3 | 35.271 | -40.928 | 71.059 | 2022-01 | 2022-01:-40.9281;2022-06:71.0587;2022-12:70.7478 | no |
| sutil | ElasticNet | 2023 | 4 | 13.387 | -13.093 | 32.239 | 2023-11 | 2023-08:13.8505;2023-09:21.8522;2023-11:-13.0925;2023-12:32.2388 | no |
| sutil | ElasticNet | 2024 | 0 | — | — | — | — | — | no |
| sutil | ElasticNet | 2025 | 3 | 130.308 | 133.292 | 184.795 | 2025-11 | 2025-01:161.1254;2025-07:133.2923;2025-11:184.7946 | no |
| sutil | ElasticNet | agregado_2021_2025 | 10 | 67.362 | 42.336 | 80.577 | 2023-11 | 2022-01:67.4847;2022-06:80.5773;2022-12:80.5315;2023-08:62.2289;2023-09:68.6341;2023-11:42.3362;2023-12:77.3261;2025-01:70.5189;2025-07:65.7993;2025-11:75.2197 | no |
| sutil | XGB-37 | 2021 | 0 | — | — | — | — | — | no |
| sutil | XGB-37 | 2022 | 3 | 14.989 | -25.769 | 40.778 | 2022-01 | 2022-01:-25.7686;2022-06:40.7783;2022-12:29.1479 | no |
| sutil | XGB-37 | 2023 | 4 | 25.220 | 23.144 | 37.464 | 2023-09 | 2023-08:23.1445;2023-09:37.4639;2023-11:26.0359;2023-12:25.4568 | no |
| sutil | XGB-37 | 2024 | 0 | — | — | — | — | — | no |
| sutil | XGB-37 | 2025 | 3 | 40.569 | 17.691 | 90.748 | 2025-07 | 2025-01:17.6906;2025-07:90.7479;2025-11:20.4714 | no |
| sutil | XGB-37 | agregado_2021_2025 | 10 | 21.997 | 10.234 | 32.400 | 2025-01 | 2022-01:15.5381;2022-06:29.1347;2022-12:26.5029;2023-08:23.1539;2023-09:27.7273;2023-11:24.0397;2023-12:23.8608;2025-01:10.2336;2025-07:32.4001;2025-11:10.9682 | no |
| sutil | GC3 | 2021 | 0 | — | — | — | — | — | no |
| sutil | GC3 | 2022 | 3 | -4.765 | -54.245 | 22.935 | 2022-01 | 2022-01:-54.2448;2022-06:8.7194;2022-12:22.9348 | no |
| sutil | GC3 | 2023 | 4 | 20.250 | 3.119 | 37.129 | 2023-08 | 2023-08:3.1191;2023-09:25.0891;2023-11:37.1290;2023-12:22.2986 | no |
| sutil | GC3 | 2024 | 0 | — | — | — | — | — | no |
| sutil | GC3 | 2025 | 3 | -27.781 | -41.083 | -8.902 | 2025-07 | 2025-01:-40.1223;2025-07:-8.9015;2025-11:-41.0832 | no |
| sutil | GC3 | agregado_2021_2025 | 10 | -4.509 | -13.757 | 2.649 | 2023-08 | 2022-01:-11.2076;2022-06:-0.2109;2022-12:2.6489;2023-08:-13.7571;2023-09:-5.3703;2023-11:-0.2187;2023-12:-6.5045;2025-01:-6.6812;2025-07:1.9224;2025-11:-6.9326 | no |
| sutil | GE | 2021 | 0 | — | — | — | — | — | no |
| sutil | GE | 2022 | 3 | -1.098 | -55.430 | 24.072 | 2022-01 | 2022-01:-55.4297;2022-06:24.0722;2022-12:19.4576 | no |
| sutil | GE | 2023 | 4 | 34.196 | 22.643 | 52.649 | 2023-11 | 2023-08:22.6430;2023-09:43.7498;2023-11:52.6493;2023-12:32.7342 | no |
| sutil | GE | 2024 | 0 | — | — | — | — | — | no |
| sutil | GE | 2025 | 3 | -16.103 | -37.988 | 8.437 | 2025-07 | 2025-01:-37.9875;2025-07:8.4366;2025-11:-24.8887 | no |
| sutil | GE | agregado_2021_2025 | 10 | 1.233 | -6.574 | 8.217 | 2025-01 | 2022-01:-5.2159;2022-06:8.2170;2022-12:7.3221;2023-08:-4.5775;2023-09:2.5678;2023-11:5.9384;2023-12:-1.2994;2025-01:-6.5738;2025-07:8.2073;2025-11:-2.6192 | no |
| sutil | XGB-43 | 2021 | 0 | — | — | — | — | — | sí |
| sutil | XGB-43 | 2022 | 3 | 15.242 | -21.398 | 41.019 | 2022-01 | 2022-01:-21.3975;2022-06:41.0192;2022-12:26.2216 | sí |
| sutil | XGB-43 | 2023 | 4 | 26.559 | 24.036 | 42.733 | 2023-09 | 2023-08:24.5001;2023-09:42.7326;2023-11:26.4442;2023-12:24.0356 | sí |
| sutil | XGB-43 | 2024 | 0 | — | — | — | — | — | sí |
| sutil | XGB-43 | 2025 | 3 | 42.079 | 15.852 | 92.872 | 2025-07 | 2025-01:25.2292;2025-07:92.8720;2025-11:15.8518 | sí |
| sutil | XGB-43 | agregado_2021_2025 | 10 | 19.658 | 7.015 | 29.873 | 2025-11 | 2022-01:13.6540;2022-06:26.5399;2022-12:23.2015;2023-08:20.9554;2023-09:26.5933;2023-11:21.5212;2023-12:20.8214;2025-01:9.4455;2025-07:29.8730;2025-11:7.0147 | sí |
| dulce | Naive | 2021 | 3 | 77.839 | 68.211 | 108.605 | 2021-01 | 2021-01:108.6054;2021-02:95.0166;2021-03:68.2106 | no |
| dulce | Naive | 2022 | 3 | 67.725 | 56.401 | 92.574 | 2022-01 | 2022-01:92.5742;2022-02:85.2896;2022-03:56.4010 | no |
| dulce | Naive | 2023 | 2 | 84.736 | 80.330 | 119.141 | 2023-02 | 2023-02:119.1407;2023-03:80.3305 | no |
| dulce | Naive | 2024 | 4 | 59.868 | 58.624 | 77.307 | 2024-01 | 2024-01:77.3069;2024-02:72.2553;2024-03:58.6237;2024-10:67.1396 | no |
| dulce | Naive | 2025 | 3 | 63.229 | 52.558 | 91.151 | 2025-01 | 2025-01:91.1508;2025-02:73.8724;2025-03:52.5583 | no |
| dulce | Naive | agregado_2021_2025 | 15 | 69.786 | 68.901 | 74.332 | 2021-01 | 2021-01:74.3315;2021-02:72.8134;2021-03:70.0894;2022-01:73.8983;2022-02:73.0427;2022-03:69.9118;2023-02:72.2352;2023-03:70.3863;2024-01:73.6553;2024-02:72.3347;2024-03:69.0306;2024-10:71.0522;2025-01:73.8630;2025-02:71.5402;2025-03:68.9012 | no |
| dulce | Seasonal Naive | 2021 | 3 | -13.321 | -20.805 | -7.388 | 2021-02 | 2021-01:-15.0763;2021-02:-20.8050;2021-03:-7.3883 | no |
| dulce | Seasonal Naive | 2022 | 3 | 58.144 | 63.738 | 71.445 | 2022-02 | 2022-01:63.7378;2022-02:71.4447;2022-03:65.6409 | no |
| dulce | Seasonal Naive | 2023 | 2 | -37.597 | -73.442 | -7.938 | 2023-02 | 2023-02:-73.4420;2023-03:-7.9375 | no |
| dulce | Seasonal Naive | 2024 | 4 | -20.661 | -31.734 | -16.651 | 2024-03 | 2024-01:-17.7287;2024-02:-16.6515;2024-03:-31.7341;2024-10:-22.8650 | no |
| dulce | Seasonal Naive | 2025 | 3 | -15.182 | -25.167 | -2.560 | 2025-01 | 2025-01:-2.5601;2025-02:-21.9321;2025-03:-25.1667 | no |
| dulce | Seasonal Naive | agregado_2021_2025 | 15 | -0.001 | -5.372 | 4.677 | 2024-03 | 2021-01:1.8166;2021-02:1.2681;2021-03:2.5713;2022-01:-1.9557;2022-02:-1.0155;2022-03:-1.7265;2023-02:2.8358;2023-03:4.6772;2024-01:-0.3189;2024-02:0.0836;2024-03:-5.3716;2024-10:-2.2102;2025-01:1.9814;2025-02:-1.2125;2025-03:-1.7263 | no |
| dulce | Chronos | 2021 | 3 | 35.869 | 1.288 | 68.278 | 2021-03 | 2021-01:46.2508;2021-02:68.2775;2021-03:1.2883 | no |
| dulce | Chronos | 2022 | 3 | 62.944 | 51.570 | 93.225 | 2022-02 | 2022-01:71.3996;2022-02:93.2253;2022-03:51.5698 | no |
| dulce | Chronos | 2023 | 2 | 44.103 | 28.692 | 70.626 | 2023-02 | 2023-02:70.6259;2023-03:28.6922 | no |
| dulce | Chronos | 2024 | 4 | 44.117 | 32.496 | 61.221 | 2024-10 | 2024-01:47.9257;2024-02:56.7547;2024-03:32.4963;2024-10:61.2206 | no |
| dulce | Chronos | 2025 | 3 | 73.845 | 62.869 | 101.351 | 2025-02 | 2025-01:92.6651;2025-02:101.3508;2025-03:62.8688 | no |
| dulce | Chronos | agregado_2021_2025 | 15 | 56.394 | 51.749 | 63.211 | 2021-02 | 2021-01:61.5213;2021-02:63.2110;2021-03:58.5337;2022-01:57.6235;2022-02:60.3775;2022-03:55.3396;2023-02:59.5725;2023-03:57.5102;2024-01:55.8978;2024-02:58.4800;2024-03:51.7492;2024-10:59.8499;2025-01:57.0794;2025-02:58.3966;2025-03:52.9254 | no |
| dulce | SARIMA | 2021 | 3 | -68.551 | -77.597 | -60.327 | 2021-02 | 2021-01:-73.5812;2021-02:-77.5965;2021-03:-60.3269 | no |
| dulce | SARIMA | 2022 | 3 | 4.317 | -9.455 | 20.511 | 2022-02 | 2022-01:-9.4546;2022-02:20.5114;2022-03:2.0949 | no |
| dulce | SARIMA | 2023 | 2 | -53.250 | -71.451 | -39.840 | 2023-02 | 2023-02:-71.4506;2023-03:-39.8397 | no |
| dulce | SARIMA | 2024 | 4 | 3.629 | -14.675 | 21.907 | 2024-10 | 2024-01:6.6151;2024-02:21.9068;2024-03:-0.6149;2024-10:-14.6749 | no |
| dulce | SARIMA | 2025 | 3 | -46.691 | -64.450 | -31.397 | 2025-02 | 2025-01:-31.3973;2025-02:-64.4503;2025-03:-51.8603 | no |
| dulce | SARIMA | agregado_2021_2025 | 15 | -24.083 | -34.491 | -20.370 | 2024-10 | 2021-01:-21.6504;2021-02:-22.0273;2021-03:-20.3702;2022-01:-25.3919;2022-02:-22.4877;2022-03:-24.3129;2023-02:-23.7684;2023-03:-21.7339;2024-01:-27.4597;2024-02:-21.8604;2024-03:-29.9411;2024-10:-34.4913;2025-01:-20.8053;2025-02:-26.0444;2025-03:-24.1117 | no |
| dulce | SARIMA-sel | 2021 | 3 | 24.773 | 15.427 | 39.416 | 2021-03 | 2021-01:15.4274;2021-02:27.4187;2021-03:39.4156 | no |
| dulce | SARIMA-sel | 2022 | 3 | 4.317 | -9.455 | 20.511 | 2022-02 | 2022-01:-9.4546;2022-02:20.5114;2022-03:2.0949 | no |
| dulce | SARIMA-sel | 2023 | 2 | -56.756 | -74.949 | -43.280 | 2023-02 | 2023-02:-74.9492;2023-03:-43.2805 | no |
| dulce | SARIMA-sel | 2024 | 4 | 1.512 | -13.867 | 17.704 | 2024-02 | 2024-01:3.6558;2024-02:17.7045;2024-03:-2.8725;2024-10:-13.8670 | no |
| dulce | SARIMA-sel | 2025 | 3 | -44.266 | -62.027 | -25.582 | 2025-01 | 2025-01:-25.5821;2025-02:-62.0270;2025-03:-53.1364 | no |
| dulce | SARIMA-sel | agregado_2021_2025 | 15 | -4.547 | -11.067 | 0.279 | 2021-01 | 2021-01:-11.0669;2021-02:-8.7765;2021-03:-6.3854;2022-01:-3.9348;2022-02:-1.5049;2022-03:-3.0325;2023-02:-2.1919;2023-03:-0.6099;2024-01:-5.7247;2024-02:-1.4788;2024-03:-7.5815;2024-10:-10.5567;2025-01:0.2792;2025-02:-4.1583;2025-03:-3.1242 | no |
| dulce | Ridge | 2021 | 3 | 10.499 | -5.791 | 28.811 | 2021-02 | 2021-01:10.3008;2021-02:28.8111;2021-03:-5.7908 | no |
| dulce | Ridge | 2022 | 3 | 52.300 | -12.734 | 92.697 | 2022-03 | 2022-01:83.7753;2022-02:92.6969;2022-03:-12.7337 | no |
| dulce | Ridge | 2023 | 2 | -32.814 | -83.606 | 9.873 | 2023-03 | 2023-02:9.8727;2023-03:-83.6061 | no |
| dulce | Ridge | 2024 | 4 | 8.994 | -8.407 | 18.606 | 2024-03 | 2024-01:16.7269;2024-02:18.6063;2024-03:-8.4073;2024-10:10.9286 | no |
| dulce | Ridge | 2025 | 3 | 79.670 | 45.840 | 124.066 | 2025-01 | 2025-01:124.0660;2025-02:102.4725;2025-03:45.8400 | no |
| dulce | Ridge | agregado_2021_2025 | 15 | 31.325 | 21.651 | 37.735 | 2024-03 | 2021-01:34.4771;2021-02:36.1216;2021-03:33.1421;2022-01:35.6827;2022-02:36.5766;2022-03:27.9915;2023-02:37.7347;2023-03:33.7057;2024-01:31.3104;2024-02:32.0834;2024-03:21.6509;2024-10:28.9720;2025-01:34.5033;2025-02:31.2645;2025-03:24.1677 | no |
| dulce | ElasticNet | 2021 | 3 | 15.683 | 3.231 | 28.239 | 2021-02 | 2021-01:19.8584;2021-02:28.2389;2021-03:3.2311 | no |
| dulce | ElasticNet | 2022 | 3 | 52.099 | -13.994 | 93.168 | 2022-03 | 2022-01:83.4306;2022-02:93.1678;2022-03:-13.9936 | no |
| dulce | ElasticNet | 2023 | 2 | -31.635 | -99.118 | 24.643 | 2023-03 | 2023-02:24.6429;2023-03:-99.1175 | no |
| dulce | ElasticNet | 2024 | 4 | 12.570 | -9.873 | 22.354 | 2024-03 | 2024-01:21.0369;2024-02:22.3537;2024-03:-9.8728;2024-10:19.3034 | no |
| dulce | ElasticNet | 2025 | 3 | 83.846 | 57.689 | 126.160 | 2025-01 | 2025-01:126.1603;2025-02:106.4104;2025-03:57.6887 | no |
| dulce | ElasticNet | agregado_2021_2025 | 15 | 33.796 | 23.518 | 40.929 | 2024-03 | 2021-01:37.0848;2021-02:37.8617;2021-03:35.6180;2022-01:38.1839;2022-02:39.1959;2022-03:30.1468;2023-02:40.9289;2023-03:35.3670;2024-01:34.3642;2024-02:34.8672;2024-03:23.5179;2024-10:33.7074;2025-01:36.3595;2025-02:33.3254;2025-03:26.9426 | no |
| dulce | XGB-37 | 2021 | 3 | 64.040 | 29.761 | 112.678 | 2021-01 | 2021-01:112.6781;2021-02:70.9854;2021-03:29.7614 | no |
| dulce | XGB-37 | 2022 | 3 | 52.159 | 17.974 | 84.650 | 2022-03 | 2022-01:70.5319;2022-02:84.6498;2022-03:17.9737 | no |
| dulce | XGB-37 | 2023 | 2 | 57.586 | 21.693 | 107.001 | 2023-02 | 2023-02:107.0013;2023-03:21.6926 | no |
| dulce | XGB-37 | 2024 | 4 | -10.638 | -30.952 | 5.728 | 2024-01 | 2024-01:-30.9519;2024-02:5.7280;2024-03:-24.0751;2024-10:-0.1159 | no |
| dulce | XGB-37 | 2025 | 3 | 51.745 | 52.752 | 64.160 | 2025-02 | 2025-01:52.7523;2025-02:64.1597;2025-03:60.6213 | no |
| dulce | XGB-37 | agregado_2021_2025 | 15 | 36.445 | 30.424 | 42.858 | 2024-02 | 2021-01:42.6194;2021-02:39.4227;2021-03:36.8329;2022-01:37.4761;2022-02:39.6450;2022-03:30.4242;2023-02:38.8357;2023-03:34.4453;2024-01:34.4378;2024-02:42.8584;2024-03:35.8901;2024-10:41.3980;2025-01:33.7956;2025-02:35.6463;2025-03:35.0632 | no |
| dulce | GC3 | 2021 | 3 | 19.588 | 4.055 | 37.984 | 2021-01 | 2021-01:37.9843;2021-02:21.8860;2021-03:4.0547 | no |
| dulce | GC3 | 2022 | 3 | 19.264 | -3.239 | 33.710 | 2022-03 | 2022-01:31.7400;2022-02:33.7103;2022-03:-3.2394 | no |
| dulce | GC3 | 2023 | 2 | 33.923 | 17.316 | 58.185 | 2023-02 | 2023-02:58.1847;2023-03:17.3162 | no |
| dulce | GC3 | 2024 | 4 | -30.910 | -53.006 | -25.607 | 2024-03 | 2024-01:-26.9322;2024-02:-25.6068;2024-03:-53.0060;2024-10:-27.3222 | no |
| dulce | GC3 | 2025 | 3 | 15.019 | -11.702 | 40.678 | 2025-03 | 2025-01:40.6785;2025-02:17.7015;2025-03:-11.7020 | no |
| dulce | GC3 | agregado_2021_2025 | 15 | 7.197 | -5.089 | 10.367 | 2025-03 | 2021-01:10.3666;2021-02:8.9377;2021-03:7.4616;2022-01:9.7879;2022-02:9.9682;2022-03:6.8181;2023-02:9.0520;2023-03:7.4419;2024-01:10.0355;2024-02:10.3650;2024-03:3.9872;2024-10:9.9390;2025-01:8.0581;2025-02:2.0330;2025-03:-5.0895 | no |
| dulce | GE | 2021 | 3 | 6.595 | -29.029 | 27.882 | 2021-03 | 2021-01:27.8817;2021-02:18.7976;2021-03:-29.0291 | no |
| dulce | GE | 2022 | 3 | 13.828 | -13.641 | 30.146 | 2022-03 | 2022-01:30.1456;2022-02:26.6879;2022-03:-13.6409 | no |
| dulce | GE | 2023 | 2 | 24.402 | 8.144 | 45.584 | 2023-02 | 2023-02:45.5842;2023-03:8.1445 | no |
| dulce | GE | 2024 | 4 | -24.186 | -48.272 | -17.874 | 2024-03 | 2024-01:-20.9442;2024-02:-17.8744;2024-03:-48.2720;2024-10:-18.2841 | no |
| dulce | GE | 2025 | 3 | 4.523 | -29.278 | 30.488 | 2025-03 | 2025-01:30.4882;2025-02:9.6043;2025-03:-29.2780 | no |
| dulce | GE | agregado_2021_2025 | 15 | 2.025 | -9.493 | 5.465 | 2025-03 | 2021-01:5.4649;2021-02:4.5352;2021-03:0.1493;2022-01:4.8599;2022-02:4.5363;2022-03:1.0773;2023-02:3.3976;2023-03:1.7348;2024-01:3.9295;2024-02:4.7100;2024-03:-2.4908;2024-10:4.6051;2025-01:4.1181;2025-02:-0.9238;2025-03:-9.4928 | no |
| dulce | XGB-43 | 2021 | 3 | 52.534 | 24.566 | 91.400 | 2021-01 | 2021-01:91.3997;2021-02:58.8830;2021-03:24.5657 | sí |
| dulce | XGB-43 | 2022 | 3 | 50.964 | 17.864 | 78.592 | 2022-03 | 2022-01:72.9757;2022-02:78.5922;2022-03:17.8645 | sí |
| dulce | XGB-43 | 2023 | 2 | 65.301 | 38.873 | 109.870 | 2023-02 | 2023-02:109.8699;2023-03:38.8728 | sí |
| dulce | XGB-43 | 2024 | 4 | -15.050 | -35.018 | -1.118 | 2024-01 | 2024-01:-35.0182;2024-02:-1.1181;2024-03:-29.5970;2024-10:-2.3925 | sí |
| dulce | XGB-43 | 2025 | 3 | 34.080 | 30.157 | 45.162 | 2025-02 | 2025-01:30.1570;2025-02:45.1616;2025-03:39.5027 | sí |
| dulce | XGB-43 | agregado_2021_2025 | 15 | 30.643 | 24.106 | 36.447 | 2022-03 | 2021-01:36.0365;2021-02:33.5244;2021-03:31.2523;2022-01:31.8128;2022-02:32.7003;2022-03:24.1057;2023-02:32.0020;2023-03:28.3221;2024-01:29.0967;2024-02:36.4466;2024-03:30.1825;2024-10:36.1443;2025-01:27.8792;2025-02:30.3824;2025-03:29.4219 | sí |

### T13_mae_por_cuartil_cambio.csv — T13 completa: MAE por cuartiles y tercios de |Δy/y|

`06_metricas/agregadas/T13_mae_por_cuartil_cambio.csv` — 154 filas × 8 columnas.

| cultivar | agrupacion | grupo | rango_cambio | n_meses | modelo | MAE | exploratorio |
|---|---|---|---|---|---|---|---|
| sutil | cuartil | 1 | 0.003-0.037 | 15 | Naive | 411.594 | no |
| sutil | cuartil | 1 | 0.003-0.037 | 15 | Seasonal Naive | 6,940.988 | no |
| sutil | cuartil | 1 | 0.003-0.037 | 15 | Chronos | 1,798.519 | no |
| sutil | cuartil | 1 | 0.003-0.037 | 15 | SARIMA | 3,073.101 | no |
| sutil | cuartil | 1 | 0.003-0.037 | 15 | SARIMA-sel | 3,516.601 | no |
| sutil | cuartil | 1 | 0.003-0.037 | 15 | Ridge | 3,337.612 | no |
| sutil | cuartil | 1 | 0.003-0.037 | 15 | ElasticNet | 3,296.288 | no |
| sutil | cuartil | 1 | 0.003-0.037 | 15 | XGB-37 | 5,014.735 | no |
| sutil | cuartil | 1 | 0.003-0.037 | 15 | GC3 | 6,627.583 | no |
| sutil | cuartil | 1 | 0.003-0.037 | 15 | GE | 6,998.055 | no |
| sutil | cuartil | 1 | 0.003-0.037 | 15 | XGB-43 | 5,356.379 | sí |
| sutil | cuartil | 2 | 0.037-0.097 | 15 | Naive | 2,240.115 | no |
| sutil | cuartil | 2 | 0.037-0.097 | 15 | Seasonal Naive | 5,308.598 | no |
| sutil | cuartil | 2 | 0.037-0.097 | 15 | Chronos | 1,854.370 | no |
| sutil | cuartil | 2 | 0.037-0.097 | 15 | SARIMA | 3,334.109 | no |
| sutil | cuartil | 2 | 0.037-0.097 | 15 | SARIMA-sel | 2,730.108 | no |
| sutil | cuartil | 2 | 0.037-0.097 | 15 | Ridge | 2,757.320 | no |
| sutil | cuartil | 2 | 0.037-0.097 | 15 | ElasticNet | 2,598.304 | no |
| sutil | cuartil | 2 | 0.037-0.097 | 15 | XGB-37 | 4,749.092 | no |
| sutil | cuartil | 2 | 0.037-0.097 | 15 | GC3 | 6,527.030 | no |
| sutil | cuartil | 2 | 0.037-0.097 | 15 | GE | 7,822.767 | no |
| sutil | cuartil | 2 | 0.037-0.097 | 15 | XGB-43 | 4,926.752 | sí |
| sutil | cuartil | 3 | 0.097-0.192 | 15 | Naive | 4,095.572 | no |
| sutil | cuartil | 3 | 0.097-0.192 | 15 | Seasonal Naive | 6,474.940 | no |
| sutil | cuartil | 3 | 0.097-0.192 | 15 | Chronos | 2,642.122 | no |
| sutil | cuartil | 3 | 0.097-0.192 | 15 | SARIMA | 2,903.540 | no |
| sutil | cuartil | 3 | 0.097-0.192 | 15 | SARIMA-sel | 3,024.496 | no |
| sutil | cuartil | 3 | 0.097-0.192 | 15 | Ridge | 4,984.619 | no |
| sutil | cuartil | 3 | 0.097-0.192 | 15 | ElasticNet | 5,252.045 | no |
| sutil | cuartil | 3 | 0.097-0.192 | 15 | XGB-37 | 4,313.819 | no |
| sutil | cuartil | 3 | 0.097-0.192 | 15 | GC3 | 5,598.049 | no |
| sutil | cuartil | 3 | 0.097-0.192 | 15 | GE | 4,975.881 | no |
| sutil | cuartil | 3 | 0.097-0.192 | 15 | XGB-43 | 4,162.886 | sí |
| sutil | cuartil | 4 | 0.192-0.571 | 15 | Naive | 7,749.001 | no |
| sutil | cuartil | 4 | 0.192-0.571 | 15 | Seasonal Naive | 5,575.018 | no |
| sutil | cuartil | 4 | 0.192-0.571 | 15 | Chronos | 4,299.175 | no |
| sutil | cuartil | 4 | 0.192-0.571 | 15 | SARIMA | 4,132.399 | no |
| sutil | cuartil | 4 | 0.192-0.571 | 15 | SARIMA-sel | 3,552.301 | no |
| sutil | cuartil | 4 | 0.192-0.571 | 15 | Ridge | 8,620.992 | no |
| sutil | cuartil | 4 | 0.192-0.571 | 15 | ElasticNet | 8,341.008 | no |
| sutil | cuartil | 4 | 0.192-0.571 | 15 | XGB-37 | 5,448.153 | no |
| sutil | cuartil | 4 | 0.192-0.571 | 15 | GC3 | 6,692.555 | no |
| sutil | cuartil | 4 | 0.192-0.571 | 15 | GE | 7,177.417 | no |
| sutil | cuartil | 4 | 0.192-0.571 | 15 | XGB-43 | 5,601.725 | sí |
| sutil | tercio | 1 | 0.003-0.050 | 20 | Naive | 640.398 | no |
| sutil | tercio | 1 | 0.003-0.050 | 20 | Seasonal Naive | 6,771.167 | no |
| sutil | tercio | 1 | 0.003-0.050 | 20 | Chronos | 1,786.533 | no |
| sutil | tercio | 1 | 0.003-0.050 | 20 | SARIMA | 3,369.462 | no |
| sutil | tercio | 1 | 0.003-0.050 | 20 | SARIMA-sel | 3,329.047 | no |
| sutil | tercio | 1 | 0.003-0.050 | 20 | Ridge | 2,989.701 | no |
| sutil | tercio | 1 | 0.003-0.050 | 20 | ElasticNet | 2,927.648 | no |
| sutil | tercio | 1 | 0.003-0.050 | 20 | XGB-37 | 4,189.053 | no |
| sutil | tercio | 1 | 0.003-0.050 | 20 | GC3 | 6,011.468 | no |
| sutil | tercio | 1 | 0.003-0.050 | 20 | GE | 6,757.589 | no |
| sutil | tercio | 1 | 0.003-0.050 | 20 | XGB-43 | 4,440.504 | sí |
| sutil | tercio | 2 | 0.050-0.164 | 20 | Naive | 3,206.439 | no |
| sutil | tercio | 2 | 0.050-0.164 | 20 | Seasonal Naive | 5,310.343 | no |
| sutil | tercio | 2 | 0.050-0.164 | 20 | Chronos | 2,142.700 | no |
| sutil | tercio | 2 | 0.050-0.164 | 20 | SARIMA | 3,195.895 | no |
| sutil | tercio | 2 | 0.050-0.164 | 20 | SARIMA-sel | 3,060.346 | no |
| sutil | tercio | 2 | 0.050-0.164 | 20 | Ridge | 3,204.875 | no |
| sutil | tercio | 2 | 0.050-0.164 | 20 | ElasticNet | 3,280.599 | no |
| sutil | tercio | 2 | 0.050-0.164 | 20 | XGB-37 | 4,974.009 | no |
| sutil | tercio | 2 | 0.050-0.164 | 20 | GC3 | 6,132.065 | no |
| sutil | tercio | 2 | 0.050-0.164 | 20 | GE | 6,285.723 | no |
| sutil | tercio | 2 | 0.050-0.164 | 20 | XGB-43 | 5,070.535 | sí |
| sutil | tercio | 3 | 0.164-0.571 | 20 | Naive | 7,025.374 | no |
| sutil | tercio | 3 | 0.164-0.571 | 20 | Seasonal Naive | 6,143.147 | no |
| sutil | tercio | 3 | 0.164-0.571 | 20 | Chronos | 4,016.407 | no |
| sutil | tercio | 3 | 0.164-0.571 | 20 | SARIMA | 3,517.004 | no |
| sutil | tercio | 3 | 0.164-0.571 | 20 | SARIMA-sel | 3,228.236 | no |
| sutil | tercio | 3 | 0.164-0.571 | 20 | Ridge | 8,580.831 | no |
| sutil | tercio | 3 | 0.164-0.571 | 20 | ElasticNet | 8,407.487 | no |
| sutil | tercio | 3 | 0.164-0.571 | 20 | XGB-37 | 5,481.288 | no |
| sutil | tercio | 3 | 0.164-0.571 | 20 | GC3 | 6,940.380 | no |
| sutil | tercio | 3 | 0.164-0.571 | 20 | GE | 7,187.277 | no |
| sutil | tercio | 3 | 0.164-0.571 | 20 | XGB-43 | 5,524.768 | sí |
| dulce | cuartil | 1 | 0.007-0.090 | 15 | Naive | 23.279 | no |
| dulce | cuartil | 1 | 0.007-0.090 | 15 | Seasonal Naive | 22.064 | no |
| dulce | cuartil | 1 | 0.007-0.090 | 15 | Chronos | 17.885 | no |
| dulce | cuartil | 1 | 0.007-0.090 | 15 | SARIMA | 13.322 | no |
| dulce | cuartil | 1 | 0.007-0.090 | 15 | SARIMA-sel | 18.382 | no |
| dulce | cuartil | 1 | 0.007-0.090 | 15 | Ridge | 43.548 | no |
| dulce | cuartil | 1 | 0.007-0.090 | 15 | ElasticNet | 42.619 | no |
| dulce | cuartil | 1 | 0.007-0.090 | 15 | XGB-37 | 49.382 | no |
| dulce | cuartil | 1 | 0.007-0.090 | 15 | GC3 | 66.408 | no |
| dulce | cuartil | 1 | 0.007-0.090 | 15 | GE | 68.674 | no |
| dulce | cuartil | 1 | 0.007-0.090 | 15 | XGB-43 | 48.471 | sí |
| dulce | cuartil | 2 | 0.090-0.165 | 15 | Naive | 59.927 | no |
| dulce | cuartil | 2 | 0.090-0.165 | 15 | Seasonal Naive | 36.059 | no |
| dulce | cuartil | 2 | 0.090-0.165 | 15 | Chronos | 28.836 | no |
| dulce | cuartil | 2 | 0.090-0.165 | 15 | SARIMA | 30.126 | no |
| dulce | cuartil | 2 | 0.090-0.165 | 15 | SARIMA-sel | 28.653 | no |
| dulce | cuartil | 2 | 0.090-0.165 | 15 | Ridge | 55.730 | no |
| dulce | cuartil | 2 | 0.090-0.165 | 15 | ElasticNet | 52.397 | no |
| dulce | cuartil | 2 | 0.090-0.165 | 15 | XGB-37 | 49.657 | no |
| dulce | cuartil | 2 | 0.090-0.165 | 15 | GC3 | 65.613 | no |
| dulce | cuartil | 2 | 0.090-0.165 | 15 | GE | 66.102 | no |
| dulce | cuartil | 2 | 0.090-0.165 | 15 | XGB-43 | 49.269 | sí |
| dulce | cuartil | 3 | 0.165-0.327 | 15 | Naive | 95.262 | no |
| dulce | cuartil | 3 | 0.165-0.327 | 15 | Seasonal Naive | 15.386 | no |
| dulce | cuartil | 3 | 0.165-0.327 | 15 | Chronos | 28.355 | no |
| dulce | cuartil | 3 | 0.165-0.327 | 15 | SARIMA | 16.222 | no |
| dulce | cuartil | 3 | 0.165-0.327 | 15 | SARIMA-sel | 15.789 | no |
| dulce | cuartil | 3 | 0.165-0.327 | 15 | Ridge | 43.306 | no |
| dulce | cuartil | 3 | 0.165-0.327 | 15 | ElasticNet | 38.746 | no |
| dulce | cuartil | 3 | 0.165-0.327 | 15 | XGB-37 | 28.153 | no |
| dulce | cuartil | 3 | 0.165-0.327 | 15 | GC3 | 33.908 | no |
| dulce | cuartil | 3 | 0.165-0.327 | 15 | GE | 34.279 | no |
| dulce | cuartil | 3 | 0.165-0.327 | 15 | XGB-43 | 30.573 | sí |
| dulce | cuartil | 4 | 0.327-0.474 | 15 | Naive | 131.622 | no |
| dulce | cuartil | 4 | 0.327-0.474 | 15 | Seasonal Naive | 24.503 | no |
| dulce | cuartil | 4 | 0.327-0.474 | 15 | Chronos | 48.199 | no |
| dulce | cuartil | 4 | 0.327-0.474 | 15 | SARIMA | 13.978 | no |
| dulce | cuartil | 4 | 0.327-0.474 | 15 | SARIMA-sel | 19.691 | no |
| dulce | cuartil | 4 | 0.327-0.474 | 15 | Ridge | 69.694 | no |
| dulce | cuartil | 4 | 0.327-0.474 | 15 | ElasticNet | 67.230 | no |
| dulce | cuartil | 4 | 0.327-0.474 | 15 | XGB-37 | 65.849 | no |
| dulce | cuartil | 4 | 0.327-0.474 | 15 | GC3 | 60.748 | no |
| dulce | cuartil | 4 | 0.327-0.474 | 15 | GE | 57.883 | no |
| dulce | cuartil | 4 | 0.327-0.474 | 15 | XGB-43 | 62.234 | sí |
| dulce | tercio | 1 | 0.007-0.108 | 20 | Naive | 31.685 | no |
| dulce | tercio | 1 | 0.007-0.108 | 20 | Seasonal Naive | 23.630 | no |
| dulce | tercio | 1 | 0.007-0.108 | 20 | Chronos | 18.634 | no |
| dulce | tercio | 1 | 0.007-0.108 | 20 | SARIMA | 18.595 | no |
| dulce | tercio | 1 | 0.007-0.108 | 20 | SARIMA-sel | 20.939 | no |
| dulce | tercio | 1 | 0.007-0.108 | 20 | Ridge | 42.267 | no |
| dulce | tercio | 1 | 0.007-0.108 | 20 | ElasticNet | 41.034 | no |
| dulce | tercio | 1 | 0.007-0.108 | 20 | XGB-37 | 43.147 | no |
| dulce | tercio | 1 | 0.007-0.108 | 20 | GC3 | 62.324 | no |
| dulce | tercio | 1 | 0.007-0.108 | 20 | GE | 65.418 | no |
| dulce | tercio | 1 | 0.007-0.108 | 20 | XGB-43 | 41.830 | sí |
| dulce | tercio | 2 | 0.108-0.245 | 20 | Naive | 75.403 | no |
| dulce | tercio | 2 | 0.108-0.245 | 20 | Seasonal Naive | 27.090 | no |
| dulce | tercio | 2 | 0.108-0.245 | 20 | Chronos | 30.837 | no |
| dulce | tercio | 2 | 0.108-0.245 | 20 | SARIMA | 22.005 | no |
| dulce | tercio | 2 | 0.108-0.245 | 20 | SARIMA-sel | 23.471 | no |
| dulce | tercio | 2 | 0.108-0.245 | 20 | Ridge | 52.500 | no |
| dulce | tercio | 2 | 0.108-0.245 | 20 | ElasticNet | 48.553 | no |
| dulce | tercio | 2 | 0.108-0.245 | 20 | XGB-37 | 43.856 | no |
| dulce | tercio | 2 | 0.108-0.245 | 20 | GC3 | 53.527 | no |
| dulce | tercio | 2 | 0.108-0.245 | 20 | GE | 54.130 | no |
| dulce | tercio | 2 | 0.108-0.245 | 20 | XGB-43 | 46.190 | sí |
| dulce | tercio | 3 | 0.245-0.474 | 20 | Naive | 125.479 | no |
| dulce | tercio | 3 | 0.245-0.474 | 20 | Seasonal Naive | 22.790 | no |
| dulce | tercio | 3 | 0.245-0.474 | 20 | Chronos | 42.985 | no |
| dulce | tercio | 3 | 0.245-0.474 | 20 | SARIMA | 14.635 | no |
| dulce | tercio | 3 | 0.245-0.474 | 20 | SARIMA-sel | 17.477 | no |
| dulce | tercio | 3 | 0.245-0.474 | 20 | Ridge | 64.442 | no |
| dulce | tercio | 3 | 0.245-0.474 | 20 | ElasticNet | 61.158 | no |
| dulce | tercio | 3 | 0.245-0.474 | 20 | XGB-37 | 57.778 | no |
| dulce | tercio | 3 | 0.245-0.474 | 20 | GC3 | 54.158 | no |
| dulce | tercio | 3 | 0.245-0.474 | 20 | GE | 50.656 | no |
| dulce | tercio | 3 | 0.245-0.474 | 20 | XGB-43 | 54.891 | sí |

### T15_diagnostico_ajuste.csv — T15 completa: diagnóstico D-BR8 por corrida, con mejor época

`06_metricas/por_semilla/T15_diagnostico_ajuste.csv` — 420 filas × 20 columnas.

| modelo | cultivar | anio_test | semilla | train_inicio | n_train | n_val | MAE_train | MAE_val | razon_val_train | sobreajuste_razon_gt_2 | Naive_MAE_train | Naive_MAE_val | Naive_razon | no_supera_naive | no_supera_naive_train | no_supera_naive_val | exploratorio | mejor_epoca | epocas_corridas |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ridge | dulce | 2021 | — | 2016-08 | 41 | 12 | 23.832 | 36.218 | 1.520 | no | 74.313 | 66.683 | 0.897 | no | no | no | no | — | — |
| Ridge | dulce | 2022 | — | 2016-08 | 53 | 12 | 15.205 | 25.931 | 1.705 | no | 72.586 | 67.831 | 0.934 | no | no | no | no | — | — |
| Ridge | dulce | 2023 | — | 2016-08 | 65 | 12 | 15.794 | 26.207 | 1.659 | no | 71.708 | 73.307 | 1.022 | no | no | no | no | — | — |
| Ridge | dulce | 2024 | — | 2016-08 | 77 | 12 | 22.753 | 40.926 | 1.799 | no | 71.957 | 76.179 | 1.059 | no | no | no | no | — | — |
| Ridge | dulce | 2025 | — | 2016-08 | 89 | 12 | 38.398 | 63.537 | 1.655 | no | 72.526 | 85.594 | 1.180 | no | no | no | no | — | — |
| Ridge | sutil | 2021 | — | 2016-08 | 41 | 12 | 1,302.499 | 3,504.281 | 2.690 | sí | 3,128.885 | 4,101.784 | 1.311 | no | no | no | no | — | — |
| Ridge | sutil | 2022 | — | 2016-08 | 53 | 12 | 2,194.617 | 2,122.623 | 0.967 | no | 3,349.164 | 1,986.098 | 0.593 | sí | no | sí | no | — | — |
| Ridge | sutil | 2023 | — | 2016-08 | 65 | 12 | 1,585.788 | 2,332.164 | 1.471 | no | 3,097.521 | 3,762.176 | 1.215 | no | no | no | no | — | — |
| Ridge | sutil | 2024 | — | 2016-08 | 77 | 12 | 2,818.862 | 4,050.052 | 1.437 | no | 3,201.103 | 4,589.653 | 1.434 | no | no | no | no | — | — |
| Ridge | sutil | 2025 | — | 2016-08 | 89 | 12 | 2,145.490 | 2,047.112 | 0.954 | no | 3,388.324 | 3,078.133 | 0.908 | no | no | no | no | — | — |
| ElasticNet | dulce | 2021 | — | 2016-08 | 41 | 12 | 24.975 | 33.253 | 1.331 | no | 74.313 | 66.683 | 0.897 | no | no | no | no | — | — |
| ElasticNet | dulce | 2022 | — | 2016-08 | 53 | 12 | 15.258 | 25.930 | 1.699 | no | 72.586 | 67.831 | 0.934 | no | no | no | no | — | — |
| ElasticNet | dulce | 2023 | — | 2016-08 | 65 | 12 | 16.514 | 26.223 | 1.588 | no | 71.708 | 73.307 | 1.022 | no | no | no | no | — | — |
| ElasticNet | dulce | 2024 | — | 2016-08 | 77 | 12 | 26.646 | 38.235 | 1.435 | no | 71.957 | 76.179 | 1.059 | no | no | no | no | — | — |
| ElasticNet | dulce | 2025 | — | 2016-08 | 89 | 12 | 35.877 | 62.171 | 1.733 | no | 72.526 | 85.594 | 1.180 | no | no | no | no | — | — |
| ElasticNet | sutil | 2021 | — | 2016-08 | 41 | 12 | 1,528.403 | 3,437.715 | 2.249 | sí | 3,128.885 | 4,101.784 | 1.311 | no | no | no | no | — | — |
| ElasticNet | sutil | 2022 | — | 2016-08 | 53 | 12 | 1,917.368 | 2,032.261 | 1.060 | no | 3,349.164 | 1,986.098 | 0.593 | sí | no | sí | no | — | — |
| ElasticNet | sutil | 2023 | — | 2016-08 | 65 | 12 | 1,628.137 | 2,336.557 | 1.435 | no | 3,097.521 | 3,762.176 | 1.215 | no | no | no | no | — | — |
| ElasticNet | sutil | 2024 | — | 2016-08 | 77 | 12 | 3,096.800 | 4,031.624 | 1.302 | no | 3,201.103 | 4,589.653 | 1.434 | no | no | no | no | — | — |
| ElasticNet | sutil | 2025 | — | 2016-08 | 89 | 12 | 1,955.709 | 1,619.160 | 0.828 | no | 3,388.324 | 3,078.133 | 0.908 | no | no | no | no | — | — |
| XGB-37 | dulce | 2021 | 0.000 | 2016-08 | 41 | 12 | 2.519 | 50.432 | 20.023 | sí | 74.313 | 66.683 | 0.897 | no | no | no | no | — | — |
| XGB-37 | dulce | 2021 | 1.000 | 2016-08 | 41 | 12 | 3.007 | 42.804 | 14.233 | sí | 74.313 | 66.683 | 0.897 | no | no | no | no | — | — |
| XGB-37 | dulce | 2021 | 2.000 | 2016-08 | 41 | 12 | 2.783 | 51.999 | 18.683 | sí | 74.313 | 66.683 | 0.897 | no | no | no | no | — | — |
| XGB-37 | dulce | 2021 | 3.000 | 2016-08 | 41 | 12 | 2.569 | 47.648 | 18.547 | sí | 74.313 | 66.683 | 0.897 | no | no | no | no | — | — |
| XGB-37 | dulce | 2021 | 4.000 | 2016-08 | 41 | 12 | 2.632 | 49.767 | 18.905 | sí | 74.313 | 66.683 | 0.897 | no | no | no | no | — | — |
| XGB-37 | dulce | 2021 | 5.000 | 2016-08 | 41 | 12 | 2.639 | 50.863 | 19.277 | sí | 74.313 | 66.683 | 0.897 | no | no | no | no | — | — |
| XGB-37 | dulce | 2021 | 6.000 | 2016-08 | 41 | 12 | 3.189 | 52.652 | 16.509 | sí | 74.313 | 66.683 | 0.897 | no | no | no | no | — | — |
| XGB-37 | dulce | 2021 | 7.000 | 2016-08 | 41 | 12 | 2.858 | 47.977 | 16.784 | sí | 74.313 | 66.683 | 0.897 | no | no | no | no | — | — |
| XGB-37 | dulce | 2021 | 8.000 | 2016-08 | 41 | 12 | 2.652 | 48.414 | 18.253 | sí | 74.313 | 66.683 | 0.897 | no | no | no | no | — | — |
| XGB-37 | dulce | 2021 | 9.000 | 2016-08 | 41 | 12 | 2.620 | 39.850 | 15.210 | sí | 74.313 | 66.683 | 0.897 | no | no | no | no | — | — |
| XGB-37 | dulce | 2022 | 0.000 | 2016-08 | 53 | 12 | 3.203 | 28.228 | 8.812 | sí | 72.586 | 67.831 | 0.934 | no | no | no | no | — | — |
| XGB-37 | dulce | 2022 | 1.000 | 2016-08 | 53 | 12 | 3.723 | 20.000 | 5.372 | sí | 72.586 | 67.831 | 0.934 | no | no | no | no | — | — |
| XGB-37 | dulce | 2022 | 2.000 | 2016-08 | 53 | 12 | 3.559 | 24.671 | 6.933 | sí | 72.586 | 67.831 | 0.934 | no | no | no | no | — | — |
| XGB-37 | dulce | 2022 | 3.000 | 2016-08 | 53 | 12 | 3.387 | 26.286 | 7.760 | sí | 72.586 | 67.831 | 0.934 | no | no | no | no | — | — |
| XGB-37 | dulce | 2022 | 4.000 | 2016-08 | 53 | 12 | 3.342 | 23.176 | 6.935 | sí | 72.586 | 67.831 | 0.934 | no | no | no | no | — | — |
| XGB-37 | dulce | 2022 | 5.000 | 2016-08 | 53 | 12 | 3.490 | 22.054 | 6.319 | sí | 72.586 | 67.831 | 0.934 | no | no | no | no | — | — |
| XGB-37 | dulce | 2022 | 6.000 | 2016-08 | 53 | 12 | 3.291 | 24.297 | 7.383 | sí | 72.586 | 67.831 | 0.934 | no | no | no | no | — | — |
| XGB-37 | dulce | 2022 | 7.000 | 2016-08 | 53 | 12 | 3.744 | 23.930 | 6.392 | sí | 72.586 | 67.831 | 0.934 | no | no | no | no | — | — |
| XGB-37 | dulce | 2022 | 8.000 | 2016-08 | 53 | 12 | 3.708 | 22.340 | 6.025 | sí | 72.586 | 67.831 | 0.934 | no | no | no | no | — | — |
| XGB-37 | dulce | 2022 | 9.000 | 2016-08 | 53 | 12 | 3.423 | 22.044 | 6.440 | sí | 72.586 | 67.831 | 0.934 | no | no | no | no | — | — |
| XGB-37 | dulce | 2023 | 0.000 | 2016-08 | 65 | 12 | 4.200 | 46.317 | 11.028 | sí | 71.708 | 73.307 | 1.022 | no | no | no | no | — | — |
| XGB-37 | dulce | 2023 | 1.000 | 2016-08 | 65 | 12 | 4.309 | 43.198 | 10.025 | sí | 71.708 | 73.307 | 1.022 | no | no | no | no | — | — |
| XGB-37 | dulce | 2023 | 2.000 | 2016-08 | 65 | 12 | 4.389 | 44.831 | 10.213 | sí | 71.708 | 73.307 | 1.022 | no | no | no | no | — | — |
| XGB-37 | dulce | 2023 | 3.000 | 2016-08 | 65 | 12 | 4.404 | 42.561 | 9.664 | sí | 71.708 | 73.307 | 1.022 | no | no | no | no | — | — |
| XGB-37 | dulce | 2023 | 4.000 | 2016-08 | 65 | 12 | 3.973 | 40.775 | 10.264 | sí | 71.708 | 73.307 | 1.022 | no | no | no | no | — | — |
| XGB-37 | dulce | 2023 | 5.000 | 2016-08 | 65 | 12 | 4.494 | 43.593 | 9.699 | sí | 71.708 | 73.307 | 1.022 | no | no | no | no | — | — |
| XGB-37 | dulce | 2023 | 6.000 | 2016-08 | 65 | 12 | 4.218 | 42.698 | 10.122 | sí | 71.708 | 73.307 | 1.022 | no | no | no | no | — | — |
| XGB-37 | dulce | 2023 | 7.000 | 2016-08 | 65 | 12 | 4.452 | 42.799 | 9.613 | sí | 71.708 | 73.307 | 1.022 | no | no | no | no | — | — |
| XGB-37 | dulce | 2023 | 8.000 | 2016-08 | 65 | 12 | 4.463 | 43.235 | 9.687 | sí | 71.708 | 73.307 | 1.022 | no | no | no | no | — | — |
| XGB-37 | dulce | 2023 | 9.000 | 2016-08 | 65 | 12 | 4.346 | 43.300 | 9.963 | sí | 71.708 | 73.307 | 1.022 | no | no | no | no | — | — |
| XGB-37 | dulce | 2024 | 0.000 | 2016-08 | 77 | 12 | 5.699 | 36.432 | 6.393 | sí | 71.957 | 76.179 | 1.059 | no | no | no | no | — | — |
| XGB-37 | dulce | 2024 | 1.000 | 2016-08 | 77 | 12 | 5.367 | 33.612 | 6.263 | sí | 71.957 | 76.179 | 1.059 | no | no | no | no | — | — |
| XGB-37 | dulce | 2024 | 2.000 | 2016-08 | 77 | 12 | 5.589 | 30.762 | 5.504 | sí | 71.957 | 76.179 | 1.059 | no | no | no | no | — | — |
| XGB-37 | dulce | 2024 | 3.000 | 2016-08 | 77 | 12 | 5.836 | 33.890 | 5.807 | sí | 71.957 | 76.179 | 1.059 | no | no | no | no | — | — |
| XGB-37 | dulce | 2024 | 4.000 | 2016-08 | 77 | 12 | 5.846 | 34.258 | 5.860 | sí | 71.957 | 76.179 | 1.059 | no | no | no | no | — | — |
| XGB-37 | dulce | 2024 | 5.000 | 2016-08 | 77 | 12 | 5.612 | 31.901 | 5.684 | sí | 71.957 | 76.179 | 1.059 | no | no | no | no | — | — |
| XGB-37 | dulce | 2024 | 6.000 | 2016-08 | 77 | 12 | 5.468 | 37.753 | 6.905 | sí | 71.957 | 76.179 | 1.059 | no | no | no | no | — | — |
| XGB-37 | dulce | 2024 | 7.000 | 2016-08 | 77 | 12 | 5.720 | 32.245 | 5.637 | sí | 71.957 | 76.179 | 1.059 | no | no | no | no | — | — |
| XGB-37 | dulce | 2024 | 8.000 | 2016-08 | 77 | 12 | 5.576 | 32.294 | 5.791 | sí | 71.957 | 76.179 | 1.059 | no | no | no | no | — | — |
| XGB-37 | dulce | 2024 | 9.000 | 2016-08 | 77 | 12 | 5.634 | 28.769 | 5.107 | sí | 71.957 | 76.179 | 1.059 | no | no | no | no | — | — |
| XGB-37 | dulce | 2025 | 0.000 | 2016-08 | 89 | 12 | 6.353 | 46.277 | 7.285 | sí | 72.526 | 85.594 | 1.180 | no | no | no | no | — | — |
| XGB-37 | dulce | 2025 | 1.000 | 2016-08 | 89 | 12 | 5.970 | 45.889 | 7.687 | sí | 72.526 | 85.594 | 1.180 | no | no | no | no | — | — |
| XGB-37 | dulce | 2025 | 2.000 | 2016-08 | 89 | 12 | 6.537 | 47.084 | 7.202 | sí | 72.526 | 85.594 | 1.180 | no | no | no | no | — | — |
| XGB-37 | dulce | 2025 | 3.000 | 2016-08 | 89 | 12 | 6.100 | 49.300 | 8.082 | sí | 72.526 | 85.594 | 1.180 | no | no | no | no | — | — |
| XGB-37 | dulce | 2025 | 4.000 | 2016-08 | 89 | 12 | 6.276 | 48.696 | 7.759 | sí | 72.526 | 85.594 | 1.180 | no | no | no | no | — | — |
| XGB-37 | dulce | 2025 | 5.000 | 2016-08 | 89 | 12 | 6.247 | 49.213 | 7.878 | sí | 72.526 | 85.594 | 1.180 | no | no | no | no | — | — |
| XGB-37 | dulce | 2025 | 6.000 | 2016-08 | 89 | 12 | 5.834 | 48.824 | 8.369 | sí | 72.526 | 85.594 | 1.180 | no | no | no | no | — | — |
| XGB-37 | dulce | 2025 | 7.000 | 2016-08 | 89 | 12 | 6.118 | 47.088 | 7.697 | sí | 72.526 | 85.594 | 1.180 | no | no | no | no | — | — |
| XGB-37 | dulce | 2025 | 8.000 | 2016-08 | 89 | 12 | 6.422 | 55.459 | 8.635 | sí | 72.526 | 85.594 | 1.180 | no | no | no | no | — | — |
| XGB-37 | dulce | 2025 | 9.000 | 2016-08 | 89 | 12 | 6.424 | 46.958 | 7.310 | sí | 72.526 | 85.594 | 1.180 | no | no | no | no | — | — |
| XGB-37 | sutil | 2021 | 0.000 | 2016-08 | 41 | 12 | 162.731 | 3,898.489 | 23.957 | sí | 3,128.885 | 4,101.784 | 1.311 | no | no | no | no | — | — |
| XGB-37 | sutil | 2021 | 1.000 | 2016-08 | 41 | 12 | 200.717 | 4,217.512 | 21.012 | sí | 3,128.885 | 4,101.784 | 1.311 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2021 | 2.000 | 2016-08 | 41 | 12 | 174.628 | 4,429.624 | 25.366 | sí | 3,128.885 | 4,101.784 | 1.311 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2021 | 3.000 | 2016-08 | 41 | 12 | 169.174 | 4,235.340 | 25.035 | sí | 3,128.885 | 4,101.784 | 1.311 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2021 | 4.000 | 2016-08 | 41 | 12 | 196.565 | 4,146.846 | 21.097 | sí | 3,128.885 | 4,101.784 | 1.311 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2021 | 5.000 | 2016-08 | 41 | 12 | 187.633 | 4,273.775 | 22.777 | sí | 3,128.885 | 4,101.784 | 1.311 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2021 | 6.000 | 2016-08 | 41 | 12 | 197.334 | 3,965.004 | 20.093 | sí | 3,128.885 | 4,101.784 | 1.311 | no | no | no | no | — | — |
| XGB-37 | sutil | 2021 | 7.000 | 2016-08 | 41 | 12 | 173.566 | 4,042.997 | 23.294 | sí | 3,128.885 | 4,101.784 | 1.311 | no | no | no | no | — | — |
| XGB-37 | sutil | 2021 | 8.000 | 2016-08 | 41 | 12 | 184.452 | 4,026.061 | 21.827 | sí | 3,128.885 | 4,101.784 | 1.311 | no | no | no | no | — | — |
| XGB-37 | sutil | 2021 | 9.000 | 2016-08 | 41 | 12 | 182.659 | 4,495.584 | 24.612 | sí | 3,128.885 | 4,101.784 | 1.311 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2022 | 0.000 | 2016-08 | 53 | 12 | 286.816 | 2,428.490 | 8.467 | sí | 3,349.164 | 1,986.098 | 0.593 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2022 | 1.000 | 2016-08 | 53 | 12 | 277.533 | 2,266.874 | 8.168 | sí | 3,349.164 | 1,986.098 | 0.593 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2022 | 2.000 | 2016-08 | 53 | 12 | 279.354 | 2,571.730 | 9.206 | sí | 3,349.164 | 1,986.098 | 0.593 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2022 | 3.000 | 2016-08 | 53 | 12 | 250.496 | 2,576.990 | 10.288 | sí | 3,349.164 | 1,986.098 | 0.593 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2022 | 4.000 | 2016-08 | 53 | 12 | 280.770 | 2,529.946 | 9.011 | sí | 3,349.164 | 1,986.098 | 0.593 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2022 | 5.000 | 2016-08 | 53 | 12 | 264.300 | 2,404.917 | 9.099 | sí | 3,349.164 | 1,986.098 | 0.593 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2022 | 6.000 | 2016-08 | 53 | 12 | 260.989 | 2,612.924 | 10.012 | sí | 3,349.164 | 1,986.098 | 0.593 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2022 | 7.000 | 2016-08 | 53 | 12 | 271.496 | 2,496.350 | 9.195 | sí | 3,349.164 | 1,986.098 | 0.593 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2022 | 8.000 | 2016-08 | 53 | 12 | 258.002 | 2,487.601 | 9.642 | sí | 3,349.164 | 1,986.098 | 0.593 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2022 | 9.000 | 2016-08 | 53 | 12 | 279.402 | 2,520.159 | 9.020 | sí | 3,349.164 | 1,986.098 | 0.593 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2023 | 0.000 | 2016-08 | 65 | 12 | 376.130 | 4,362.333 | 11.598 | sí | 3,097.521 | 3,762.176 | 1.215 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2023 | 1.000 | 2016-08 | 65 | 12 | 351.919 | 4,196.172 | 11.924 | sí | 3,097.521 | 3,762.176 | 1.215 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2023 | 2.000 | 2016-08 | 65 | 12 | 364.038 | 4,378.913 | 12.029 | sí | 3,097.521 | 3,762.176 | 1.215 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2023 | 3.000 | 2016-08 | 65 | 12 | 363.800 | 4,368.551 | 12.008 | sí | 3,097.521 | 3,762.176 | 1.215 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2023 | 4.000 | 2016-08 | 65 | 12 | 341.994 | 4,668.892 | 13.652 | sí | 3,097.521 | 3,762.176 | 1.215 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2023 | 5.000 | 2016-08 | 65 | 12 | 359.813 | 4,279.832 | 11.895 | sí | 3,097.521 | 3,762.176 | 1.215 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2023 | 6.000 | 2016-08 | 65 | 12 | 356.445 | 4,465.070 | 12.527 | sí | 3,097.521 | 3,762.176 | 1.215 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2023 | 7.000 | 2016-08 | 65 | 12 | 341.173 | 4,286.318 | 12.563 | sí | 3,097.521 | 3,762.176 | 1.215 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2023 | 8.000 | 2016-08 | 65 | 12 | 353.992 | 4,392.183 | 12.408 | sí | 3,097.521 | 3,762.176 | 1.215 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2023 | 9.000 | 2016-08 | 65 | 12 | 369.235 | 4,602.827 | 12.466 | sí | 3,097.521 | 3,762.176 | 1.215 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2024 | 0.000 | 2016-08 | 77 | 12 | 511.196 | 4,136.041 | 8.091 | sí | 3,201.103 | 4,589.653 | 1.434 | no | no | no | no | — | — |
| XGB-37 | sutil | 2024 | 1.000 | 2016-08 | 77 | 12 | 495.863 | 4,478.000 | 9.031 | sí | 3,201.103 | 4,589.653 | 1.434 | no | no | no | no | — | — |
| XGB-37 | sutil | 2024 | 2.000 | 2016-08 | 77 | 12 | 510.442 | 4,250.339 | 8.327 | sí | 3,201.103 | 4,589.653 | 1.434 | no | no | no | no | — | — |
| XGB-37 | sutil | 2024 | 3.000 | 2016-08 | 77 | 12 | 526.069 | 4,293.155 | 8.161 | sí | 3,201.103 | 4,589.653 | 1.434 | no | no | no | no | — | — |
| XGB-37 | sutil | 2024 | 4.000 | 2016-08 | 77 | 12 | 522.075 | 4,206.894 | 8.058 | sí | 3,201.103 | 4,589.653 | 1.434 | no | no | no | no | — | — |
| XGB-37 | sutil | 2024 | 5.000 | 2016-08 | 77 | 12 | 476.117 | 3,880.179 | 8.150 | sí | 3,201.103 | 4,589.653 | 1.434 | no | no | no | no | — | — |
| XGB-37 | sutil | 2024 | 6.000 | 2016-08 | 77 | 12 | 504.998 | 4,081.096 | 8.081 | sí | 3,201.103 | 4,589.653 | 1.434 | no | no | no | no | — | — |
| XGB-37 | sutil | 2024 | 7.000 | 2016-08 | 77 | 12 | 525.158 | 3,997.693 | 7.612 | sí | 3,201.103 | 4,589.653 | 1.434 | no | no | no | no | — | — |
| XGB-37 | sutil | 2024 | 8.000 | 2016-08 | 77 | 12 | 510.110 | 4,063.309 | 7.966 | sí | 3,201.103 | 4,589.653 | 1.434 | no | no | no | no | — | — |
| XGB-37 | sutil | 2024 | 9.000 | 2016-08 | 77 | 12 | 527.169 | 4,337.132 | 8.227 | sí | 3,201.103 | 4,589.653 | 1.434 | no | no | no | no | — | — |
| XGB-37 | sutil | 2025 | 0.000 | 2016-08 | 89 | 12 | 601.168 | 4,636.179 | 7.712 | sí | 3,388.324 | 3,078.133 | 0.908 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2025 | 1.000 | 2016-08 | 89 | 12 | 631.514 | 4,719.800 | 7.474 | sí | 3,388.324 | 3,078.133 | 0.908 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2025 | 2.000 | 2016-08 | 89 | 12 | 636.881 | 4,404.311 | 6.915 | sí | 3,388.324 | 3,078.133 | 0.908 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2025 | 3.000 | 2016-08 | 89 | 12 | 627.901 | 4,399.868 | 7.007 | sí | 3,388.324 | 3,078.133 | 0.908 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2025 | 4.000 | 2016-08 | 89 | 12 | 671.183 | 4,174.339 | 6.219 | sí | 3,388.324 | 3,078.133 | 0.908 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2025 | 5.000 | 2016-08 | 89 | 12 | 634.039 | 4,519.765 | 7.129 | sí | 3,388.324 | 3,078.133 | 0.908 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2025 | 6.000 | 2016-08 | 89 | 12 | 661.917 | 4,343.036 | 6.561 | sí | 3,388.324 | 3,078.133 | 0.908 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2025 | 7.000 | 2016-08 | 89 | 12 | 633.087 | 4,374.932 | 6.910 | sí | 3,388.324 | 3,078.133 | 0.908 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2025 | 8.000 | 2016-08 | 89 | 12 | 621.839 | 4,534.728 | 7.292 | sí | 3,388.324 | 3,078.133 | 0.908 | sí | no | sí | no | — | — |
| XGB-37 | sutil | 2025 | 9.000 | 2016-08 | 89 | 12 | 644.204 | 4,706.915 | 7.307 | sí | 3,388.324 | 3,078.133 | 0.908 | sí | no | sí | no | — | — |
| GC3 | dulce | 2021 | 0.000 | 2017-01 | 36 | 12 | 19.253 | 28.979 | 1.505 | no | 75.568 | 66.683 | 0.882 | no | no | no | no | 30.000 | 45.000 |
| GC3 | dulce | 2021 | 1.000 | 2017-01 | 36 | 12 | 20.522 | 32.540 | 1.586 | no | 75.568 | 66.683 | 0.882 | no | no | no | no | 35.000 | 50.000 |
| GC3 | dulce | 2021 | 2.000 | 2017-01 | 36 | 12 | 15.536 | 29.018 | 1.868 | no | 75.568 | 66.683 | 0.882 | no | no | no | no | 60.000 | 75.000 |
| GC3 | dulce | 2021 | 3.000 | 2017-01 | 36 | 12 | 21.380 | 21.021 | 0.983 | no | 75.568 | 66.683 | 0.882 | no | no | no | no | 55.000 | 70.000 |
| GC3 | dulce | 2021 | 4.000 | 2017-01 | 36 | 12 | 23.122 | 35.794 | 1.548 | no | 75.568 | 66.683 | 0.882 | no | no | no | no | 32.000 | 47.000 |
| GC3 | dulce | 2021 | 5.000 | 2017-01 | 36 | 12 | 18.887 | 34.913 | 1.848 | no | 75.568 | 66.683 | 0.882 | no | no | no | no | 55.000 | 70.000 |
| GC3 | dulce | 2021 | 6.000 | 2017-01 | 36 | 12 | 17.890 | 22.883 | 1.279 | no | 75.568 | 66.683 | 0.882 | no | no | no | no | 46.000 | 61.000 |
| GC3 | dulce | 2021 | 7.000 | 2017-01 | 36 | 12 | 21.250 | 40.054 | 1.885 | no | 75.568 | 66.683 | 0.882 | no | no | no | no | 61.000 | 76.000 |
| GC3 | dulce | 2021 | 8.000 | 2017-01 | 36 | 12 | 18.039 | 28.713 | 1.592 | no | 75.568 | 66.683 | 0.882 | no | no | no | no | 64.000 | 79.000 |
| GC3 | dulce | 2021 | 9.000 | 2017-01 | 36 | 12 | 21.320 | 23.073 | 1.082 | no | 75.568 | 66.683 | 0.882 | no | no | no | no | 37.000 | 52.000 |
| GC3 | dulce | 2022 | 0.000 | 2017-01 | 48 | 12 | 20.731 | 32.641 | 1.574 | no | 73.347 | 67.831 | 0.925 | no | no | no | no | 26.000 | 41.000 |
| GC3 | dulce | 2022 | 1.000 | 2017-01 | 48 | 12 | 18.162 | 36.357 | 2.002 | sí | 73.347 | 67.831 | 0.925 | no | no | no | no | 35.000 | 50.000 |
| GC3 | dulce | 2022 | 2.000 | 2017-01 | 48 | 12 | 25.112 | 35.944 | 1.431 | no | 73.347 | 67.831 | 0.925 | no | no | no | no | 23.000 | 38.000 |
| GC3 | dulce | 2022 | 3.000 | 2017-01 | 48 | 12 | 20.966 | 33.004 | 1.574 | no | 73.347 | 67.831 | 0.925 | no | no | no | no | 52.000 | 67.000 |
| GC3 | dulce | 2022 | 4.000 | 2017-01 | 48 | 12 | 16.194 | 25.467 | 1.573 | no | 73.347 | 67.831 | 0.925 | no | no | no | no | 61.000 | 76.000 |
| GC3 | dulce | 2022 | 5.000 | 2017-01 | 48 | 12 | 15.892 | 18.625 | 1.172 | no | 73.347 | 67.831 | 0.925 | no | no | no | no | 66.000 | 81.000 |
| GC3 | dulce | 2022 | 6.000 | 2017-01 | 48 | 12 | 28.913 | 28.321 | 0.980 | no | 73.347 | 67.831 | 0.925 | no | no | no | no | 14.000 | 29.000 |
| GC3 | dulce | 2022 | 7.000 | 2017-01 | 48 | 12 | 26.385 | 24.145 | 0.915 | no | 73.347 | 67.831 | 0.925 | no | no | no | no | 34.000 | 49.000 |
| GC3 | dulce | 2022 | 8.000 | 2017-01 | 48 | 12 | 20.898 | 23.851 | 1.141 | no | 73.347 | 67.831 | 0.925 | no | no | no | no | 30.000 | 45.000 |
| GC3 | dulce | 2022 | 9.000 | 2017-01 | 48 | 12 | 22.649 | 30.038 | 1.326 | no | 73.347 | 67.831 | 0.925 | no | no | no | no | 25.000 | 40.000 |
| GC3 | dulce | 2023 | 0.000 | 2017-01 | 60 | 12 | 13.407 | 24.483 | 1.826 | no | 72.243 | 73.307 | 1.015 | no | no | no | no | 52.000 | 67.000 |
| GC3 | dulce | 2023 | 1.000 | 2017-01 | 60 | 12 | 19.857 | 28.324 | 1.426 | no | 72.243 | 73.307 | 1.015 | no | no | no | no | 21.000 | 36.000 |
| GC3 | dulce | 2023 | 2.000 | 2017-01 | 60 | 12 | 20.112 | 28.731 | 1.429 | no | 72.243 | 73.307 | 1.015 | no | no | no | no | 28.000 | 43.000 |
| GC3 | dulce | 2023 | 3.000 | 2017-01 | 60 | 12 | 20.146 | 30.266 | 1.502 | no | 72.243 | 73.307 | 1.015 | no | no | no | no | 48.000 | 63.000 |
| GC3 | dulce | 2023 | 4.000 | 2017-01 | 60 | 12 | 23.560 | 29.345 | 1.246 | no | 72.243 | 73.307 | 1.015 | no | no | no | no | 19.000 | 34.000 |
| GC3 | dulce | 2023 | 5.000 | 2017-01 | 60 | 12 | 21.678 | 31.858 | 1.470 | no | 72.243 | 73.307 | 1.015 | no | no | no | no | 18.000 | 33.000 |
| GC3 | dulce | 2023 | 6.000 | 2017-01 | 60 | 12 | 20.467 | 28.354 | 1.385 | no | 72.243 | 73.307 | 1.015 | no | no | no | no | 33.000 | 48.000 |
| GC3 | dulce | 2023 | 7.000 | 2017-01 | 60 | 12 | 20.647 | 16.803 | 0.814 | no | 72.243 | 73.307 | 1.015 | no | no | no | no | 34.000 | 49.000 |
| GC3 | dulce | 2023 | 8.000 | 2017-01 | 60 | 12 | 15.587 | 36.121 | 2.317 | sí | 72.243 | 73.307 | 1.015 | no | no | no | no | 31.000 | 46.000 |
| GC3 | dulce | 2023 | 9.000 | 2017-01 | 60 | 12 | 20.426 | 24.666 | 1.208 | no | 72.243 | 73.307 | 1.015 | no | no | no | no | 27.000 | 42.000 |
| GC3 | dulce | 2024 | 0.000 | 2017-01 | 72 | 12 | 15.181 | 26.148 | 1.722 | no | 72.421 | 76.179 | 1.052 | no | no | no | no | 34.000 | 49.000 |
| GC3 | dulce | 2024 | 1.000 | 2017-01 | 72 | 12 | 19.074 | 29.150 | 1.528 | no | 72.421 | 76.179 | 1.052 | no | no | no | no | 23.000 | 38.000 |
| GC3 | dulce | 2024 | 2.000 | 2017-01 | 72 | 12 | 14.109 | 16.968 | 1.203 | no | 72.421 | 76.179 | 1.052 | no | no | no | no | 44.000 | 59.000 |
| GC3 | dulce | 2024 | 3.000 | 2017-01 | 72 | 12 | 14.913 | 27.354 | 1.834 | no | 72.421 | 76.179 | 1.052 | no | no | no | no | 80.000 | 95.000 |
| GC3 | dulce | 2024 | 4.000 | 2017-01 | 72 | 12 | 22.019 | 32.124 | 1.459 | no | 72.421 | 76.179 | 1.052 | no | no | no | no | 17.000 | 32.000 |
| GC3 | dulce | 2024 | 5.000 | 2017-01 | 72 | 12 | 21.239 | 37.075 | 1.746 | no | 72.421 | 76.179 | 1.052 | no | no | no | no | 19.000 | 34.000 |
| GC3 | dulce | 2024 | 6.000 | 2017-01 | 72 | 12 | 24.702 | 31.787 | 1.287 | no | 72.421 | 76.179 | 1.052 | no | no | no | no | 14.000 | 29.000 |
| GC3 | dulce | 2024 | 7.000 | 2017-01 | 72 | 12 | 14.708 | 20.713 | 1.408 | no | 72.421 | 76.179 | 1.052 | no | no | no | no | 53.000 | 68.000 |
| GC3 | dulce | 2024 | 8.000 | 2017-01 | 72 | 12 | 22.114 | 16.782 | 0.759 | no | 72.421 | 76.179 | 1.052 | no | no | no | no | 20.000 | 35.000 |
| GC3 | dulce | 2024 | 9.000 | 2017-01 | 72 | 12 | 15.687 | 26.141 | 1.666 | no | 72.421 | 76.179 | 1.052 | no | no | no | no | 45.000 | 60.000 |
| GC3 | dulce | 2025 | 0.000 | 2017-01 | 84 | 12 | 19.996 | 84.247 | 4.213 | sí | 72.958 | 85.594 | 1.173 | no | no | no | no | 14.000 | 29.000 |
| GC3 | dulce | 2025 | 1.000 | 2017-01 | 84 | 12 | 17.876 | 74.354 | 4.159 | sí | 72.958 | 85.594 | 1.173 | no | no | no | no | 26.000 | 41.000 |
| GC3 | dulce | 2025 | 2.000 | 2017-01 | 84 | 12 | 15.258 | 89.563 | 5.870 | sí | 72.958 | 85.594 | 1.173 | sí | no | sí | no | 39.000 | 54.000 |
| GC3 | dulce | 2025 | 3.000 | 2017-01 | 84 | 12 | 17.181 | 67.102 | 3.906 | sí | 72.958 | 85.594 | 1.173 | no | no | no | no | 50.000 | 65.000 |
| GC3 | dulce | 2025 | 4.000 | 2017-01 | 84 | 12 | 17.885 | 61.398 | 3.433 | sí | 72.958 | 85.594 | 1.173 | no | no | no | no | 27.000 | 42.000 |
| GC3 | dulce | 2025 | 5.000 | 2017-01 | 84 | 12 | 22.748 | 58.493 | 2.571 | sí | 72.958 | 85.594 | 1.173 | no | no | no | no | 14.000 | 29.000 |
| GC3 | dulce | 2025 | 6.000 | 2017-01 | 84 | 12 | 23.368 | 80.494 | 3.445 | sí | 72.958 | 85.594 | 1.173 | no | no | no | no | 13.000 | 28.000 |
| GC3 | dulce | 2025 | 7.000 | 2017-01 | 84 | 12 | 17.856 | 58.273 | 3.264 | sí | 72.958 | 85.594 | 1.173 | no | no | no | no | 41.000 | 56.000 |
| GC3 | dulce | 2025 | 8.000 | 2017-01 | 84 | 12 | 16.945 | 57.686 | 3.404 | sí | 72.958 | 85.594 | 1.173 | no | no | no | no | 37.000 | 52.000 |
| GC3 | dulce | 2025 | 9.000 | 2017-01 | 84 | 12 | 26.569 | 63.774 | 2.400 | sí | 72.958 | 85.594 | 1.173 | no | no | no | no | 13.000 | 28.000 |
| GC3 | sutil | 2021 | 0.000 | 2017-01 | 36 | 12 | 1,428.901 | 3,818.432 | 2.672 | sí | 3,200.940 | 4,101.784 | 1.281 | no | no | no | no | 33.000 | 48.000 |
| GC3 | sutil | 2021 | 1.000 | 2017-01 | 36 | 12 | 968.858 | 3,447.231 | 3.558 | sí | 3,200.940 | 4,101.784 | 1.281 | no | no | no | no | 72.000 | 87.000 |
| GC3 | sutil | 2021 | 2.000 | 2017-01 | 36 | 12 | 775.944 | 3,348.876 | 4.316 | sí | 3,200.940 | 4,101.784 | 1.281 | no | no | no | no | 91.000 | 106.000 |
| GC3 | sutil | 2021 | 3.000 | 2017-01 | 36 | 12 | 812.396 | 3,126.444 | 3.848 | sí | 3,200.940 | 4,101.784 | 1.281 | no | no | no | no | 66.000 | 81.000 |
| GC3 | sutil | 2021 | 4.000 | 2017-01 | 36 | 12 | 621.923 | 2,525.066 | 4.060 | sí | 3,200.940 | 4,101.784 | 1.281 | no | no | no | no | 91.000 | 106.000 |
| GC3 | sutil | 2021 | 5.000 | 2017-01 | 36 | 12 | 813.066 | 2,812.977 | 3.460 | sí | 3,200.940 | 4,101.784 | 1.281 | no | no | no | no | 69.000 | 84.000 |
| GC3 | sutil | 2021 | 6.000 | 2017-01 | 36 | 12 | 1,273.182 | 2,669.049 | 2.096 | sí | 3,200.940 | 4,101.784 | 1.281 | no | no | no | no | 44.000 | 59.000 |
| GC3 | sutil | 2021 | 7.000 | 2017-01 | 36 | 12 | 984.004 | 2,371.921 | 2.410 | sí | 3,200.940 | 4,101.784 | 1.281 | no | no | no | no | 71.000 | 86.000 |
| GC3 | sutil | 2021 | 8.000 | 2017-01 | 36 | 12 | 1,161.566 | 2,485.813 | 2.140 | sí | 3,200.940 | 4,101.784 | 1.281 | no | no | no | no | 50.000 | 65.000 |
| GC3 | sutil | 2021 | 9.000 | 2017-01 | 36 | 12 | 1,346.825 | 2,905.877 | 2.158 | sí | 3,200.940 | 4,101.784 | 1.281 | no | no | no | no | 60.000 | 75.000 |
| GC3 | sutil | 2022 | 0.000 | 2017-01 | 48 | 12 | 1,568.635 | 3,150.418 | 2.008 | sí | 3,426.151 | 1,986.098 | 0.580 | sí | no | sí | no | 23.000 | 38.000 |
| GC3 | sutil | 2022 | 1.000 | 2017-01 | 48 | 12 | 1,294.434 | 3,554.116 | 2.746 | sí | 3,426.151 | 1,986.098 | 0.580 | sí | no | sí | no | 51.000 | 66.000 |
| GC3 | sutil | 2022 | 2.000 | 2017-01 | 48 | 12 | 1,037.890 | 3,131.971 | 3.018 | sí | 3,426.151 | 1,986.098 | 0.580 | sí | no | sí | no | 58.000 | 73.000 |
| GC3 | sutil | 2022 | 3.000 | 2017-01 | 48 | 12 | 1,008.066 | 1,843.598 | 1.829 | no | 3,426.151 | 1,986.098 | 0.580 | no | no | no | no | 65.000 | 80.000 |
| GC3 | sutil | 2022 | 4.000 | 2017-01 | 48 | 12 | 876.030 | 2,653.315 | 3.029 | sí | 3,426.151 | 1,986.098 | 0.580 | sí | no | sí | no | 58.000 | 73.000 |
| GC3 | sutil | 2022 | 5.000 | 2017-01 | 48 | 12 | 1,204.335 | 1,683.909 | 1.398 | no | 3,426.151 | 1,986.098 | 0.580 | no | no | no | no | 44.000 | 59.000 |
| GC3 | sutil | 2022 | 6.000 | 2017-01 | 48 | 12 | 1,126.972 | 2,233.576 | 1.982 | no | 3,426.151 | 1,986.098 | 0.580 | sí | no | sí | no | 45.000 | 60.000 |
| GC3 | sutil | 2022 | 7.000 | 2017-01 | 48 | 12 | 3,996.275 | 3,360.921 | 0.841 | no | 3,426.151 | 1,986.098 | 0.580 | sí | sí | sí | no | 13.000 | 28.000 |
| GC3 | sutil | 2022 | 8.000 | 2017-01 | 48 | 12 | 1,376.811 | 2,541.968 | 1.846 | no | 3,426.151 | 1,986.098 | 0.580 | sí | no | sí | no | 34.000 | 49.000 |
| GC3 | sutil | 2022 | 9.000 | 2017-01 | 48 | 12 | 1,024.436 | 2,056.351 | 2.007 | sí | 3,426.151 | 1,986.098 | 0.580 | sí | no | sí | no | 62.000 | 77.000 |
| GC3 | sutil | 2023 | 0.000 | 2017-01 | 60 | 12 | 2,020.725 | 5,158.147 | 2.553 | sí | 3,138.140 | 3,762.176 | 1.199 | sí | no | sí | no | 13.000 | 28.000 |
| GC3 | sutil | 2023 | 1.000 | 2017-01 | 60 | 12 | 2,952.218 | 5,402.246 | 1.830 | no | 3,138.140 | 3,762.176 | 1.199 | sí | no | sí | no | 16.000 | 31.000 |
| GC3 | sutil | 2023 | 2.000 | 2017-01 | 60 | 12 | 1,025.775 | 5,677.950 | 5.535 | sí | 3,138.140 | 3,762.176 | 1.199 | sí | no | sí | no | 56.000 | 71.000 |
| GC3 | sutil | 2023 | 3.000 | 2017-01 | 60 | 12 | 1,026.447 | 4,717.818 | 4.596 | sí | 3,138.140 | 3,762.176 | 1.199 | sí | no | sí | no | 54.000 | 69.000 |
| GC3 | sutil | 2023 | 4.000 | 2017-01 | 60 | 12 | 993.015 | 4,755.715 | 4.789 | sí | 3,138.140 | 3,762.176 | 1.199 | sí | no | sí | no | 43.000 | 58.000 |
| GC3 | sutil | 2023 | 5.000 | 2017-01 | 60 | 12 | 1,407.372 | 5,323.869 | 3.783 | sí | 3,138.140 | 3,762.176 | 1.199 | sí | no | sí | no | 30.000 | 45.000 |
| GC3 | sutil | 2023 | 6.000 | 2017-01 | 60 | 12 | 1,936.756 | 6,273.874 | 3.239 | sí | 3,138.140 | 3,762.176 | 1.199 | sí | no | sí | no | 17.000 | 32.000 |
| GC3 | sutil | 2023 | 7.000 | 2017-01 | 60 | 12 | 3,088.928 | 4,360.794 | 1.412 | no | 3,138.140 | 3,762.176 | 1.199 | sí | no | sí | no | 17.000 | 32.000 |
| GC3 | sutil | 2023 | 8.000 | 2017-01 | 60 | 12 | 1,458.204 | 5,236.692 | 3.591 | sí | 3,138.140 | 3,762.176 | 1.199 | sí | no | sí | no | 24.000 | 39.000 |
| GC3 | sutil | 2023 | 9.000 | 2017-01 | 60 | 12 | 2,900.322 | 5,891.117 | 2.031 | sí | 3,138.140 | 3,762.176 | 1.199 | sí | no | sí | no | 15.000 | 30.000 |
| GC3 | sutil | 2024 | 0.000 | 2017-01 | 72 | 12 | 4,418.464 | 5,624.969 | 1.273 | no | 3,242.146 | 4,589.653 | 1.416 | sí | sí | sí | no | 5.000 | 20.000 |
| GC3 | sutil | 2024 | 1.000 | 2017-01 | 72 | 12 | 4,634.293 | 5,411.990 | 1.168 | no | 3,242.146 | 4,589.653 | 1.416 | sí | sí | sí | no | 8.000 | 23.000 |
| GC3 | sutil | 2024 | 2.000 | 2017-01 | 72 | 12 | 3,809.007 | 5,579.575 | 1.465 | no | 3,242.146 | 4,589.653 | 1.416 | sí | sí | sí | no | 11.000 | 26.000 |
| GC3 | sutil | 2024 | 3.000 | 2017-01 | 72 | 12 | 2,627.363 | 5,086.504 | 1.936 | no | 3,242.146 | 4,589.653 | 1.416 | sí | no | sí | no | 20.000 | 35.000 |
| GC3 | sutil | 2024 | 4.000 | 2017-01 | 72 | 12 | 4,585.426 | 6,914.236 | 1.508 | no | 3,242.146 | 4,589.653 | 1.416 | sí | sí | sí | no | 6.000 | 21.000 |
| GC3 | sutil | 2024 | 5.000 | 2017-01 | 72 | 12 | 3,407.976 | 4,007.366 | 1.176 | no | 3,242.146 | 4,589.653 | 1.416 | sí | sí | no | no | 14.000 | 29.000 |
| GC3 | sutil | 2024 | 6.000 | 2017-01 | 72 | 12 | 3,714.736 | 5,635.044 | 1.517 | no | 3,242.146 | 4,589.653 | 1.416 | sí | sí | sí | no | 8.000 | 23.000 |
| GC3 | sutil | 2024 | 7.000 | 2017-01 | 72 | 12 | 5,516.450 | 6,239.306 | 1.131 | no | 3,242.146 | 4,589.653 | 1.416 | sí | sí | sí | no | 4.000 | 19.000 |
| GC3 | sutil | 2024 | 8.000 | 2017-01 | 72 | 12 | 5,073.596 | 6,893.833 | 1.359 | no | 3,242.146 | 4,589.653 | 1.416 | sí | sí | sí | no | 6.000 | 21.000 |
| GC3 | sutil | 2024 | 9.000 | 2017-01 | 72 | 12 | 5,019.256 | 6,165.820 | 1.228 | no | 3,242.146 | 4,589.653 | 1.416 | sí | sí | sí | no | 7.000 | 22.000 |
| GC3 | sutil | 2025 | 0.000 | 2017-01 | 84 | 12 | 1,207.767 | 4,872.834 | 4.035 | sí | 3,434.647 | 3,078.133 | 0.896 | sí | no | sí | no | 70.000 | 85.000 |
| GC3 | sutil | 2025 | 1.000 | 2017-01 | 84 | 12 | 2,188.271 | 8,708.793 | 3.980 | sí | 3,434.647 | 3,078.133 | 0.896 | sí | no | sí | no | 38.000 | 53.000 |
| GC3 | sutil | 2025 | 2.000 | 2017-01 | 84 | 12 | 1,265.998 | 6,971.126 | 5.506 | sí | 3,434.647 | 3,078.133 | 0.896 | sí | no | sí | no | 55.000 | 70.000 |
| GC3 | sutil | 2025 | 3.000 | 2017-01 | 84 | 12 | 2,245.070 | 7,161.125 | 3.190 | sí | 3,434.647 | 3,078.133 | 0.896 | sí | no | sí | no | 20.000 | 35.000 |
| GC3 | sutil | 2025 | 4.000 | 2017-01 | 84 | 12 | 920.599 | 6,868.151 | 7.461 | sí | 3,434.647 | 3,078.133 | 0.896 | sí | no | sí | no | 101.000 | 116.000 |
| GC3 | sutil | 2025 | 5.000 | 2017-01 | 84 | 12 | 1,252.178 | 6,276.896 | 5.013 | sí | 3,434.647 | 3,078.133 | 0.896 | sí | no | sí | no | 47.000 | 62.000 |
| GC3 | sutil | 2025 | 6.000 | 2017-01 | 84 | 12 | 6,242.607 | 9,470.031 | 1.517 | no | 3,434.647 | 3,078.133 | 0.896 | sí | sí | sí | no | 1.000 | 16.000 |
| GC3 | sutil | 2025 | 7.000 | 2017-01 | 84 | 12 | 5,410.600 | 8,722.858 | 1.612 | no | 3,434.647 | 3,078.133 | 0.896 | sí | sí | sí | no | 4.000 | 19.000 |
| GC3 | sutil | 2025 | 8.000 | 2017-01 | 84 | 12 | 1,270.125 | 4,681.545 | 3.686 | sí | 3,434.647 | 3,078.133 | 0.896 | sí | no | sí | no | 50.000 | 65.000 |
| GC3 | sutil | 2025 | 9.000 | 2017-01 | 84 | 12 | 1,560.386 | 6,653.754 | 4.264 | sí | 3,434.647 | 3,078.133 | 0.896 | sí | no | sí | no | 40.000 | 55.000 |
| GE | dulce | 2021 | 0.000 | 2017-01 | 36 | 12 | 14.536 | 23.674 | 1.629 | no | 75.568 | 66.683 | 0.882 | no | no | no | no | 50.000 | 65.000 |
| GE | dulce | 2021 | 1.000 | 2017-01 | 36 | 12 | 20.362 | 48.720 | 2.393 | sí | 75.568 | 66.683 | 0.882 | no | no | no | no | 37.000 | 52.000 |
| GE | dulce | 2021 | 2.000 | 2017-01 | 36 | 12 | 15.760 | 35.946 | 2.281 | sí | 75.568 | 66.683 | 0.882 | no | no | no | no | 61.000 | 76.000 |
| GE | dulce | 2021 | 3.000 | 2017-01 | 36 | 12 | 16.483 | 21.724 | 1.318 | no | 75.568 | 66.683 | 0.882 | no | no | no | no | 98.000 | 113.000 |
| GE | dulce | 2021 | 4.000 | 2017-01 | 36 | 12 | 26.989 | 35.256 | 1.306 | no | 75.568 | 66.683 | 0.882 | no | no | no | no | 28.000 | 43.000 |
| GE | dulce | 2021 | 5.000 | 2017-01 | 36 | 12 | 27.814 | 70.512 | 2.535 | sí | 75.568 | 66.683 | 0.882 | sí | no | sí | no | 17.000 | 32.000 |
| GE | dulce | 2021 | 6.000 | 2017-01 | 36 | 12 | 26.182 | 27.353 | 1.045 | no | 75.568 | 66.683 | 0.882 | no | no | no | no | 20.000 | 35.000 |
| GE | dulce | 2021 | 7.000 | 2017-01 | 36 | 12 | 11.995 | 23.870 | 1.990 | no | 75.568 | 66.683 | 0.882 | no | no | no | no | 91.000 | 106.000 |
| GE | dulce | 2021 | 8.000 | 2017-01 | 36 | 12 | 17.755 | 25.451 | 1.433 | no | 75.568 | 66.683 | 0.882 | no | no | no | no | 42.000 | 57.000 |
| GE | dulce | 2021 | 9.000 | 2017-01 | 36 | 12 | 12.011 | 18.447 | 1.536 | no | 75.568 | 66.683 | 0.882 | no | no | no | no | 76.000 | 91.000 |
| GE | dulce | 2022 | 0.000 | 2017-01 | 48 | 12 | 31.337 | 35.835 | 1.144 | no | 73.347 | 67.831 | 0.925 | no | no | no | no | 12.000 | 27.000 |
| GE | dulce | 2022 | 1.000 | 2017-01 | 48 | 12 | 15.029 | 43.598 | 2.901 | sí | 73.347 | 67.831 | 0.925 | no | no | no | no | 48.000 | 63.000 |
| GE | dulce | 2022 | 2.000 | 2017-01 | 48 | 12 | 16.799 | 36.511 | 2.173 | sí | 73.347 | 67.831 | 0.925 | no | no | no | no | 63.000 | 78.000 |
| GE | dulce | 2022 | 3.000 | 2017-01 | 48 | 12 | 20.064 | 31.948 | 1.592 | no | 73.347 | 67.831 | 0.925 | no | no | no | no | 52.000 | 67.000 |
| GE | dulce | 2022 | 4.000 | 2017-01 | 48 | 12 | 19.115 | 29.516 | 1.544 | no | 73.347 | 67.831 | 0.925 | no | no | no | no | 43.000 | 58.000 |
| GE | dulce | 2022 | 5.000 | 2017-01 | 48 | 12 | 19.664 | 23.005 | 1.170 | no | 73.347 | 67.831 | 0.925 | no | no | no | no | 33.000 | 48.000 |
| GE | dulce | 2022 | 6.000 | 2017-01 | 48 | 12 | 31.367 | 29.135 | 0.929 | no | 73.347 | 67.831 | 0.925 | no | no | no | no | 13.000 | 28.000 |
| GE | dulce | 2022 | 7.000 | 2017-01 | 48 | 12 | 27.103 | 31.060 | 1.146 | no | 73.347 | 67.831 | 0.925 | no | no | no | no | 33.000 | 48.000 |
| GE | dulce | 2022 | 8.000 | 2017-01 | 48 | 12 | 20.772 | 24.211 | 1.166 | no | 73.347 | 67.831 | 0.925 | no | no | no | no | 30.000 | 45.000 |
| GE | dulce | 2022 | 9.000 | 2017-01 | 48 | 12 | 33.423 | 39.382 | 1.178 | no | 73.347 | 67.831 | 0.925 | no | no | no | no | 14.000 | 29.000 |
| GE | dulce | 2023 | 0.000 | 2017-01 | 60 | 12 | 13.156 | 34.565 | 2.627 | sí | 72.243 | 73.307 | 1.015 | no | no | no | no | 53.000 | 68.000 |
| GE | dulce | 2023 | 1.000 | 2017-01 | 60 | 12 | 15.356 | 27.120 | 1.766 | no | 72.243 | 73.307 | 1.015 | no | no | no | no | 32.000 | 47.000 |
| GE | dulce | 2023 | 2.000 | 2017-01 | 60 | 12 | 23.317 | 31.344 | 1.344 | no | 72.243 | 73.307 | 1.015 | no | no | no | no | 19.000 | 34.000 |
| GE | dulce | 2023 | 3.000 | 2017-01 | 60 | 12 | 17.966 | 30.841 | 1.717 | no | 72.243 | 73.307 | 1.015 | no | no | no | no | 48.000 | 63.000 |
| GE | dulce | 2023 | 4.000 | 2017-01 | 60 | 12 | 22.977 | 26.842 | 1.168 | no | 72.243 | 73.307 | 1.015 | no | no | no | no | 20.000 | 35.000 |
| GE | dulce | 2023 | 5.000 | 2017-01 | 60 | 12 | 20.487 | 29.597 | 1.445 | no | 72.243 | 73.307 | 1.015 | no | no | no | no | 18.000 | 33.000 |
| GE | dulce | 2023 | 6.000 | 2017-01 | 60 | 12 | 18.172 | 30.699 | 1.689 | no | 72.243 | 73.307 | 1.015 | no | no | no | no | 33.000 | 48.000 |
| GE | dulce | 2023 | 7.000 | 2017-01 | 60 | 12 | 29.240 | 22.039 | 0.754 | no | 72.243 | 73.307 | 1.015 | no | no | no | no | 26.000 | 41.000 |
| GE | dulce | 2023 | 8.000 | 2017-01 | 60 | 12 | 16.689 | 33.035 | 1.979 | no | 72.243 | 73.307 | 1.015 | no | no | no | no | 31.000 | 46.000 |
| GE | dulce | 2023 | 9.000 | 2017-01 | 60 | 12 | 17.401 | 23.549 | 1.353 | no | 72.243 | 73.307 | 1.015 | no | no | no | no | 31.000 | 46.000 |
| GE | dulce | 2024 | 0.000 | 2017-01 | 72 | 12 | 15.317 | 32.621 | 2.130 | sí | 72.421 | 76.179 | 1.052 | no | no | no | no | 34.000 | 49.000 |
| GE | dulce | 2024 | 1.000 | 2017-01 | 72 | 12 | 15.427 | 37.203 | 2.412 | sí | 72.421 | 76.179 | 1.052 | no | no | no | no | 29.000 | 44.000 |
| GE | dulce | 2024 | 2.000 | 2017-01 | 72 | 12 | 13.871 | 16.164 | 1.165 | no | 72.421 | 76.179 | 1.052 | no | no | no | no | 43.000 | 58.000 |
| GE | dulce | 2024 | 3.000 | 2017-01 | 72 | 12 | 17.206 | 33.591 | 1.952 | no | 72.421 | 76.179 | 1.052 | no | no | no | no | 50.000 | 65.000 |
| GE | dulce | 2024 | 4.000 | 2017-01 | 72 | 12 | 16.153 | 33.046 | 2.046 | sí | 72.421 | 76.179 | 1.052 | no | no | no | no | 49.000 | 64.000 |
| GE | dulce | 2024 | 5.000 | 2017-01 | 72 | 12 | 19.936 | 37.688 | 1.890 | no | 72.421 | 76.179 | 1.052 | no | no | no | no | 19.000 | 34.000 |
| GE | dulce | 2024 | 6.000 | 2017-01 | 72 | 12 | 24.019 | 32.825 | 1.367 | no | 72.421 | 76.179 | 1.052 | no | no | no | no | 14.000 | 29.000 |
| GE | dulce | 2024 | 7.000 | 2017-01 | 72 | 12 | 15.296 | 30.145 | 1.971 | no | 72.421 | 76.179 | 1.052 | no | no | no | no | 50.000 | 65.000 |
| GE | dulce | 2024 | 8.000 | 2017-01 | 72 | 12 | 20.624 | 22.407 | 1.086 | no | 72.421 | 76.179 | 1.052 | no | no | no | no | 20.000 | 35.000 |
| GE | dulce | 2024 | 9.000 | 2017-01 | 72 | 12 | 15.497 | 29.804 | 1.923 | no | 72.421 | 76.179 | 1.052 | no | no | no | no | 35.000 | 50.000 |
| GE | dulce | 2025 | 0.000 | 2017-01 | 84 | 12 | 15.058 | 64.981 | 4.316 | sí | 72.958 | 85.594 | 1.173 | no | no | no | no | 41.000 | 56.000 |
| GE | dulce | 2025 | 1.000 | 2017-01 | 84 | 12 | 17.074 | 54.720 | 3.205 | sí | 72.958 | 85.594 | 1.173 | no | no | no | no | 27.000 | 42.000 |
| GE | dulce | 2025 | 2.000 | 2017-01 | 84 | 12 | 14.516 | 77.792 | 5.359 | sí | 72.958 | 85.594 | 1.173 | no | no | no | no | 39.000 | 54.000 |
| GE | dulce | 2025 | 3.000 | 2017-01 | 84 | 12 | 13.097 | 64.391 | 4.916 | sí | 72.958 | 85.594 | 1.173 | no | no | no | no | 78.000 | 93.000 |
| GE | dulce | 2025 | 4.000 | 2017-01 | 84 | 12 | 16.111 | 54.296 | 3.370 | sí | 72.958 | 85.594 | 1.173 | no | no | no | no | 46.000 | 61.000 |
| GE | dulce | 2025 | 5.000 | 2017-01 | 84 | 12 | 21.752 | 51.846 | 2.383 | sí | 72.958 | 85.594 | 1.173 | no | no | no | no | 14.000 | 29.000 |
| GE | dulce | 2025 | 6.000 | 2017-01 | 84 | 12 | 18.874 | 70.932 | 3.758 | sí | 72.958 | 85.594 | 1.173 | no | no | no | no | 28.000 | 43.000 |
| GE | dulce | 2025 | 7.000 | 2017-01 | 84 | 12 | 21.176 | 71.051 | 3.355 | sí | 72.958 | 85.594 | 1.173 | no | no | no | no | 31.000 | 46.000 |
| GE | dulce | 2025 | 8.000 | 2017-01 | 84 | 12 | 16.043 | 43.610 | 2.718 | sí | 72.958 | 85.594 | 1.173 | no | no | no | no | 29.000 | 44.000 |
| GE | dulce | 2025 | 9.000 | 2017-01 | 84 | 12 | 14.530 | 54.627 | 3.760 | sí | 72.958 | 85.594 | 1.173 | no | no | no | no | 47.000 | 62.000 |
| GE | sutil | 2021 | 0.000 | 2017-01 | 36 | 12 | 1,147.117 | 3,612.898 | 3.150 | sí | 3,200.940 | 4,101.784 | 1.281 | no | no | no | no | 33.000 | 48.000 |
| GE | sutil | 2021 | 1.000 | 2017-01 | 36 | 12 | 1,139.681 | 4,690.039 | 4.115 | sí | 3,200.940 | 4,101.784 | 1.281 | sí | no | sí | no | 56.000 | 71.000 |
| GE | sutil | 2021 | 2.000 | 2017-01 | 36 | 12 | 869.159 | 3,817.079 | 4.392 | sí | 3,200.940 | 4,101.784 | 1.281 | no | no | no | no | 60.000 | 75.000 |
| GE | sutil | 2021 | 3.000 | 2017-01 | 36 | 12 | 695.933 | 2,855.572 | 4.103 | sí | 3,200.940 | 4,101.784 | 1.281 | no | no | no | no | 66.000 | 81.000 |
| GE | sutil | 2021 | 4.000 | 2017-01 | 36 | 12 | 780.923 | 3,192.735 | 4.088 | sí | 3,200.940 | 4,101.784 | 1.281 | no | no | no | no | 59.000 | 74.000 |
| GE | sutil | 2021 | 5.000 | 2017-01 | 36 | 12 | 801.359 | 3,339.961 | 4.168 | sí | 3,200.940 | 4,101.784 | 1.281 | no | no | no | no | 63.000 | 78.000 |
| GE | sutil | 2021 | 6.000 | 2017-01 | 36 | 12 | 959.720 | 3,054.352 | 3.183 | sí | 3,200.940 | 4,101.784 | 1.281 | no | no | no | no | 45.000 | 60.000 |
| GE | sutil | 2021 | 7.000 | 2017-01 | 36 | 12 | 2,148.371 | 3,204.370 | 1.492 | no | 3,200.940 | 4,101.784 | 1.281 | no | no | no | no | 27.000 | 42.000 |
| GE | sutil | 2021 | 8.000 | 2017-01 | 36 | 12 | 907.651 | 2,638.294 | 2.907 | sí | 3,200.940 | 4,101.784 | 1.281 | no | no | no | no | 49.000 | 64.000 |
| GE | sutil | 2021 | 9.000 | 2017-01 | 36 | 12 | 620.002 | 2,471.549 | 3.986 | sí | 3,200.940 | 4,101.784 | 1.281 | no | no | no | no | 117.000 | 132.000 |
| GE | sutil | 2022 | 0.000 | 2017-01 | 48 | 12 | 1,580.303 | 3,510.603 | 2.221 | sí | 3,426.151 | 1,986.098 | 0.580 | sí | no | sí | no | 22.000 | 37.000 |
| GE | sutil | 2022 | 1.000 | 2017-01 | 48 | 12 | 2,843.274 | 3,880.379 | 1.365 | no | 3,426.151 | 1,986.098 | 0.580 | sí | no | sí | no | 18.000 | 33.000 |
| GE | sutil | 2022 | 2.000 | 2017-01 | 48 | 12 | 790.561 | 2,519.118 | 3.186 | sí | 3,426.151 | 1,986.098 | 0.580 | sí | no | sí | no | 76.000 | 91.000 |
| GE | sutil | 2022 | 3.000 | 2017-01 | 48 | 12 | 868.625 | 2,209.422 | 2.544 | sí | 3,426.151 | 1,986.098 | 0.580 | sí | no | sí | no | 65.000 | 80.000 |
| GE | sutil | 2022 | 4.000 | 2017-01 | 48 | 12 | 765.703 | 2,631.153 | 3.436 | sí | 3,426.151 | 1,986.098 | 0.580 | sí | no | sí | no | 86.000 | 101.000 |
| GE | sutil | 2022 | 5.000 | 2017-01 | 48 | 12 | 932.656 | 1,510.544 | 1.620 | no | 3,426.151 | 1,986.098 | 0.580 | no | no | no | no | 75.000 | 90.000 |
| GE | sutil | 2022 | 6.000 | 2017-01 | 48 | 12 | 2,387.225 | 3,169.252 | 1.328 | no | 3,426.151 | 1,986.098 | 0.580 | sí | no | sí | no | 14.000 | 29.000 |
| GE | sutil | 2022 | 7.000 | 2017-01 | 48 | 12 | 3,983.191 | 3,140.534 | 0.788 | no | 3,426.151 | 1,986.098 | 0.580 | sí | sí | sí | no | 13.000 | 28.000 |
| GE | sutil | 2022 | 8.000 | 2017-01 | 48 | 12 | 1,897.203 | 2,706.068 | 1.426 | no | 3,426.151 | 1,986.098 | 0.580 | sí | no | sí | no | 22.000 | 37.000 |
| GE | sutil | 2022 | 9.000 | 2017-01 | 48 | 12 | 1,100.592 | 1,632.722 | 1.483 | no | 3,426.151 | 1,986.098 | 0.580 | no | no | no | no | 47.000 | 62.000 |
| GE | sutil | 2023 | 0.000 | 2017-01 | 60 | 12 | 1,747.705 | 4,447.675 | 2.545 | sí | 3,138.140 | 3,762.176 | 1.199 | sí | no | sí | no | 16.000 | 31.000 |
| GE | sutil | 2023 | 1.000 | 2017-01 | 60 | 12 | 1,832.170 | 5,187.454 | 2.831 | sí | 3,138.140 | 3,762.176 | 1.199 | sí | no | sí | no | 23.000 | 38.000 |
| GE | sutil | 2023 | 2.000 | 2017-01 | 60 | 12 | 1,243.317 | 5,605.766 | 4.509 | sí | 3,138.140 | 3,762.176 | 1.199 | sí | no | sí | no | 28.000 | 43.000 |
| GE | sutil | 2023 | 3.000 | 2017-01 | 60 | 12 | 1,041.832 | 5,083.652 | 4.880 | sí | 3,138.140 | 3,762.176 | 1.199 | sí | no | sí | no | 54.000 | 69.000 |
| GE | sutil | 2023 | 4.000 | 2017-01 | 60 | 12 | 1,443.338 | 5,396.310 | 3.739 | sí | 3,138.140 | 3,762.176 | 1.199 | sí | no | sí | no | 21.000 | 36.000 |
| GE | sutil | 2023 | 5.000 | 2017-01 | 60 | 12 | 1,391.639 | 5,161.099 | 3.709 | sí | 3,138.140 | 3,762.176 | 1.199 | sí | no | sí | no | 30.000 | 45.000 |
| GE | sutil | 2023 | 6.000 | 2017-01 | 60 | 12 | 1,716.643 | 5,962.543 | 3.473 | sí | 3,138.140 | 3,762.176 | 1.199 | sí | no | sí | no | 17.000 | 32.000 |
| GE | sutil | 2023 | 7.000 | 2017-01 | 60 | 12 | 2,885.279 | 3,920.247 | 1.359 | no | 3,138.140 | 3,762.176 | 1.199 | sí | no | sí | no | 17.000 | 32.000 |
| GE | sutil | 2023 | 8.000 | 2017-01 | 60 | 12 | 1,353.191 | 5,164.121 | 3.816 | sí | 3,138.140 | 3,762.176 | 1.199 | sí | no | sí | no | 25.000 | 40.000 |
| GE | sutil | 2023 | 9.000 | 2017-01 | 60 | 12 | 1,211.515 | 5,212.999 | 4.303 | sí | 3,138.140 | 3,762.176 | 1.199 | sí | no | sí | no | 31.000 | 46.000 |
| GE | sutil | 2024 | 0.000 | 2017-01 | 72 | 12 | 3,855.989 | 5,567.252 | 1.444 | no | 3,242.146 | 4,589.653 | 1.416 | sí | sí | sí | no | 6.000 | 21.000 |
| GE | sutil | 2024 | 1.000 | 2017-01 | 72 | 12 | 4,843.244 | 5,439.454 | 1.123 | no | 3,242.146 | 4,589.653 | 1.416 | sí | sí | sí | no | 8.000 | 23.000 |
| GE | sutil | 2024 | 2.000 | 2017-01 | 72 | 12 | 3,430.771 | 5,241.590 | 1.528 | no | 3,242.146 | 4,589.653 | 1.416 | sí | sí | sí | no | 12.000 | 27.000 |
| GE | sutil | 2024 | 3.000 | 2017-01 | 72 | 12 | 2,558.920 | 4,916.582 | 1.921 | no | 3,242.146 | 4,589.653 | 1.416 | sí | no | sí | no | 20.000 | 35.000 |
| GE | sutil | 2024 | 4.000 | 2017-01 | 72 | 12 | 3,756.041 | 6,224.914 | 1.657 | no | 3,242.146 | 4,589.653 | 1.416 | sí | sí | sí | no | 8.000 | 23.000 |
| GE | sutil | 2024 | 5.000 | 2017-01 | 72 | 12 | 3,266.537 | 4,144.645 | 1.269 | no | 3,242.146 | 4,589.653 | 1.416 | sí | sí | no | no | 13.000 | 28.000 |
| GE | sutil | 2024 | 6.000 | 2017-01 | 72 | 12 | 2,557.039 | 5,362.581 | 2.097 | sí | 3,242.146 | 4,589.653 | 1.416 | sí | no | sí | no | 13.000 | 28.000 |
| GE | sutil | 2024 | 7.000 | 2017-01 | 72 | 12 | 4,839.925 | 5,801.359 | 1.199 | no | 3,242.146 | 4,589.653 | 1.416 | sí | sí | sí | no | 6.000 | 21.000 |
| GE | sutil | 2024 | 8.000 | 2017-01 | 72 | 12 | 3,900.812 | 6,345.631 | 1.627 | no | 3,242.146 | 4,589.653 | 1.416 | sí | sí | sí | no | 9.000 | 24.000 |
| GE | sutil | 2024 | 9.000 | 2017-01 | 72 | 12 | 3,628.069 | 5,609.675 | 1.546 | no | 3,242.146 | 4,589.653 | 1.416 | sí | sí | sí | no | 9.000 | 24.000 |
| GE | sutil | 2025 | 0.000 | 2017-01 | 84 | 12 | 6,126.240 | 10,510.084 | 1.716 | no | 3,434.647 | 3,078.133 | 0.896 | sí | sí | sí | no | 1.000 | 16.000 |
| GE | sutil | 2025 | 1.000 | 2017-01 | 84 | 12 | 5,102.534 | 8,882.308 | 1.741 | no | 3,434.647 | 3,078.133 | 0.896 | sí | sí | sí | no | 6.000 | 21.000 |
| GE | sutil | 2025 | 2.000 | 2017-01 | 84 | 12 | 1,962.353 | 9,930.988 | 5.061 | sí | 3,434.647 | 3,078.133 | 0.896 | sí | no | sí | no | 38.000 | 53.000 |
| GE | sutil | 2025 | 3.000 | 2017-01 | 84 | 12 | 2,917.615 | 9,864.019 | 3.381 | sí | 3,434.647 | 3,078.133 | 0.896 | sí | no | sí | no | 15.000 | 30.000 |
| GE | sutil | 2025 | 4.000 | 2017-01 | 84 | 12 | 2,177.157 | 10,016.639 | 4.601 | sí | 3,434.647 | 3,078.133 | 0.896 | sí | no | sí | no | 18.000 | 33.000 |
| GE | sutil | 2025 | 5.000 | 2017-01 | 84 | 12 | 1,283.505 | 8,001.911 | 6.234 | sí | 3,434.647 | 3,078.133 | 0.896 | sí | no | sí | no | 67.000 | 82.000 |
| GE | sutil | 2025 | 6.000 | 2017-01 | 84 | 12 | 6,162.324 | 9,070.753 | 1.472 | no | 3,434.647 | 3,078.133 | 0.896 | sí | sí | sí | no | 1.000 | 16.000 |
| GE | sutil | 2025 | 7.000 | 2017-01 | 84 | 12 | 6,408.079 | 8,771.270 | 1.369 | no | 3,434.647 | 3,078.133 | 0.896 | sí | sí | sí | no | 1.000 | 16.000 |
| GE | sutil | 2025 | 8.000 | 2017-01 | 84 | 12 | 1,119.540 | 6,775.714 | 6.052 | sí | 3,434.647 | 3,078.133 | 0.896 | sí | no | sí | no | 49.000 | 64.000 |
| GE | sutil | 2025 | 9.000 | 2017-01 | 84 | 12 | 6,003.395 | 8,964.234 | 1.493 | no | 3,434.647 | 3,078.133 | 0.896 | sí | sí | sí | no | 2.000 | 17.000 |
| XGB-43 | dulce | 2021 | 0.000 | 2016-08 | 41 | 12 | 2.262 | 55.994 | 24.753 | sí | 74.313 | 66.683 | 0.897 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2021 | 1.000 | 2016-08 | 41 | 12 | 2.311 | 55.530 | 24.029 | sí | 74.313 | 66.683 | 0.897 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2021 | 2.000 | 2016-08 | 41 | 12 | 2.444 | 54.691 | 22.380 | sí | 74.313 | 66.683 | 0.897 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2021 | 3.000 | 2016-08 | 41 | 12 | 2.195 | 52.919 | 24.113 | sí | 74.313 | 66.683 | 0.897 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2021 | 4.000 | 2016-08 | 41 | 12 | 2.426 | 52.860 | 21.787 | sí | 74.313 | 66.683 | 0.897 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2021 | 5.000 | 2016-08 | 41 | 12 | 2.140 | 54.421 | 25.428 | sí | 74.313 | 66.683 | 0.897 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2021 | 6.000 | 2016-08 | 41 | 12 | 2.248 | 61.548 | 27.382 | sí | 74.313 | 66.683 | 0.897 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2021 | 7.000 | 2016-08 | 41 | 12 | 2.234 | 58.193 | 26.048 | sí | 74.313 | 66.683 | 0.897 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2021 | 8.000 | 2016-08 | 41 | 12 | 2.332 | 54.078 | 23.191 | sí | 74.313 | 66.683 | 0.897 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2021 | 9.000 | 2016-08 | 41 | 12 | 2.570 | 49.502 | 19.264 | sí | 74.313 | 66.683 | 0.897 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2022 | 0.000 | 2016-08 | 53 | 12 | 3.107 | 26.437 | 8.509 | sí | 72.586 | 67.831 | 0.934 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2022 | 1.000 | 2016-08 | 53 | 12 | 3.330 | 19.492 | 5.854 | sí | 72.586 | 67.831 | 0.934 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2022 | 2.000 | 2016-08 | 53 | 12 | 3.211 | 23.431 | 7.297 | sí | 72.586 | 67.831 | 0.934 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2022 | 3.000 | 2016-08 | 53 | 12 | 3.049 | 26.822 | 8.798 | sí | 72.586 | 67.831 | 0.934 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2022 | 4.000 | 2016-08 | 53 | 12 | 2.994 | 25.511 | 8.522 | sí | 72.586 | 67.831 | 0.934 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2022 | 5.000 | 2016-08 | 53 | 12 | 2.782 | 23.487 | 8.442 | sí | 72.586 | 67.831 | 0.934 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2022 | 6.000 | 2016-08 | 53 | 12 | 3.025 | 25.207 | 8.333 | sí | 72.586 | 67.831 | 0.934 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2022 | 7.000 | 2016-08 | 53 | 12 | 2.922 | 24.111 | 8.252 | sí | 72.586 | 67.831 | 0.934 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2022 | 8.000 | 2016-08 | 53 | 12 | 3.156 | 22.084 | 6.997 | sí | 72.586 | 67.831 | 0.934 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2022 | 9.000 | 2016-08 | 53 | 12 | 3.027 | 23.981 | 7.922 | sí | 72.586 | 67.831 | 0.934 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2023 | 0.000 | 2016-08 | 65 | 12 | 3.769 | 44.773 | 11.880 | sí | 71.708 | 73.307 | 1.022 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2023 | 1.000 | 2016-08 | 65 | 12 | 3.854 | 40.542 | 10.520 | sí | 71.708 | 73.307 | 1.022 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2023 | 2.000 | 2016-08 | 65 | 12 | 3.784 | 45.865 | 12.121 | sí | 71.708 | 73.307 | 1.022 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2023 | 3.000 | 2016-08 | 65 | 12 | 3.825 | 43.643 | 11.410 | sí | 71.708 | 73.307 | 1.022 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2023 | 4.000 | 2016-08 | 65 | 12 | 3.764 | 43.090 | 11.449 | sí | 71.708 | 73.307 | 1.022 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2023 | 5.000 | 2016-08 | 65 | 12 | 3.739 | 41.917 | 11.211 | sí | 71.708 | 73.307 | 1.022 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2023 | 6.000 | 2016-08 | 65 | 12 | 3.783 | 42.972 | 11.359 | sí | 71.708 | 73.307 | 1.022 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2023 | 7.000 | 2016-08 | 65 | 12 | 3.746 | 39.863 | 10.642 | sí | 71.708 | 73.307 | 1.022 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2023 | 8.000 | 2016-08 | 65 | 12 | 3.849 | 46.039 | 11.961 | sí | 71.708 | 73.307 | 1.022 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2023 | 9.000 | 2016-08 | 65 | 12 | 3.704 | 43.017 | 11.615 | sí | 71.708 | 73.307 | 1.022 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2024 | 0.000 | 2016-08 | 77 | 12 | 5.207 | 36.560 | 7.022 | sí | 71.957 | 76.179 | 1.059 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2024 | 1.000 | 2016-08 | 77 | 12 | 5.162 | 32.692 | 6.334 | sí | 71.957 | 76.179 | 1.059 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2024 | 2.000 | 2016-08 | 77 | 12 | 4.987 | 31.973 | 6.412 | sí | 71.957 | 76.179 | 1.059 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2024 | 3.000 | 2016-08 | 77 | 12 | 5.167 | 33.296 | 6.444 | sí | 71.957 | 76.179 | 1.059 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2024 | 4.000 | 2016-08 | 77 | 12 | 4.899 | 34.590 | 7.060 | sí | 71.957 | 76.179 | 1.059 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2024 | 5.000 | 2016-08 | 77 | 12 | 4.881 | 29.869 | 6.119 | sí | 71.957 | 76.179 | 1.059 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2024 | 6.000 | 2016-08 | 77 | 12 | 4.894 | 33.184 | 6.781 | sí | 71.957 | 76.179 | 1.059 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2024 | 7.000 | 2016-08 | 77 | 12 | 4.984 | 32.809 | 6.583 | sí | 71.957 | 76.179 | 1.059 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2024 | 8.000 | 2016-08 | 77 | 12 | 4.896 | 31.076 | 6.348 | sí | 71.957 | 76.179 | 1.059 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2024 | 9.000 | 2016-08 | 77 | 12 | 4.900 | 33.235 | 6.783 | sí | 71.957 | 76.179 | 1.059 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2025 | 0.000 | 2016-08 | 89 | 12 | 5.901 | 46.176 | 7.826 | sí | 72.526 | 85.594 | 1.180 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2025 | 1.000 | 2016-08 | 89 | 12 | 5.775 | 48.216 | 8.349 | sí | 72.526 | 85.594 | 1.180 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2025 | 2.000 | 2016-08 | 89 | 12 | 5.699 | 45.637 | 8.008 | sí | 72.526 | 85.594 | 1.180 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2025 | 3.000 | 2016-08 | 89 | 12 | 5.795 | 46.738 | 8.065 | sí | 72.526 | 85.594 | 1.180 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2025 | 4.000 | 2016-08 | 89 | 12 | 6.230 | 49.720 | 7.981 | sí | 72.526 | 85.594 | 1.180 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2025 | 5.000 | 2016-08 | 89 | 12 | 5.599 | 42.329 | 7.560 | sí | 72.526 | 85.594 | 1.180 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2025 | 6.000 | 2016-08 | 89 | 12 | 6.033 | 44.085 | 7.307 | sí | 72.526 | 85.594 | 1.180 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2025 | 7.000 | 2016-08 | 89 | 12 | 5.840 | 44.147 | 7.559 | sí | 72.526 | 85.594 | 1.180 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2025 | 8.000 | 2016-08 | 89 | 12 | 5.848 | 49.224 | 8.417 | sí | 72.526 | 85.594 | 1.180 | no | no | no | sí | — | — |
| XGB-43 | dulce | 2025 | 9.000 | 2016-08 | 89 | 12 | 5.801 | 49.037 | 8.453 | sí | 72.526 | 85.594 | 1.180 | no | no | no | sí | — | — |
| XGB-43 | sutil | 2021 | 0.000 | 2016-08 | 41 | 12 | 153.243 | 4,125.074 | 26.919 | sí | 3,128.885 | 4,101.784 | 1.311 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2021 | 1.000 | 2016-08 | 41 | 12 | 164.309 | 4,496.190 | 27.364 | sí | 3,128.885 | 4,101.784 | 1.311 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2021 | 2.000 | 2016-08 | 41 | 12 | 175.543 | 4,390.098 | 25.009 | sí | 3,128.885 | 4,101.784 | 1.311 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2021 | 3.000 | 2016-08 | 41 | 12 | 163.798 | 4,336.366 | 26.474 | sí | 3,128.885 | 4,101.784 | 1.311 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2021 | 4.000 | 2016-08 | 41 | 12 | 179.302 | 3,939.986 | 21.974 | sí | 3,128.885 | 4,101.784 | 1.311 | no | no | no | sí | — | — |
| XGB-43 | sutil | 2021 | 5.000 | 2016-08 | 41 | 12 | 162.365 | 4,387.759 | 27.024 | sí | 3,128.885 | 4,101.784 | 1.311 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2021 | 6.000 | 2016-08 | 41 | 12 | 173.461 | 4,160.960 | 23.988 | sí | 3,128.885 | 4,101.784 | 1.311 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2021 | 7.000 | 2016-08 | 41 | 12 | 171.320 | 4,122.144 | 24.061 | sí | 3,128.885 | 4,101.784 | 1.311 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2021 | 8.000 | 2016-08 | 41 | 12 | 161.626 | 4,231.683 | 26.182 | sí | 3,128.885 | 4,101.784 | 1.311 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2021 | 9.000 | 2016-08 | 41 | 12 | 184.041 | 4,504.919 | 24.478 | sí | 3,128.885 | 4,101.784 | 1.311 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2022 | 0.000 | 2016-08 | 53 | 12 | 252.006 | 2,572.193 | 10.207 | sí | 3,349.164 | 1,986.098 | 0.593 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2022 | 1.000 | 2016-08 | 53 | 12 | 265.815 | 2,416.349 | 9.090 | sí | 3,349.164 | 1,986.098 | 0.593 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2022 | 2.000 | 2016-08 | 53 | 12 | 251.536 | 2,809.682 | 11.170 | sí | 3,349.164 | 1,986.098 | 0.593 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2022 | 3.000 | 2016-08 | 53 | 12 | 243.533 | 2,612.152 | 10.726 | sí | 3,349.164 | 1,986.098 | 0.593 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2022 | 4.000 | 2016-08 | 53 | 12 | 245.982 | 2,501.867 | 10.171 | sí | 3,349.164 | 1,986.098 | 0.593 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2022 | 5.000 | 2016-08 | 53 | 12 | 238.846 | 2,553.907 | 10.693 | sí | 3,349.164 | 1,986.098 | 0.593 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2022 | 6.000 | 2016-08 | 53 | 12 | 265.067 | 2,415.371 | 9.112 | sí | 3,349.164 | 1,986.098 | 0.593 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2022 | 7.000 | 2016-08 | 53 | 12 | 244.659 | 2,639.295 | 10.788 | sí | 3,349.164 | 1,986.098 | 0.593 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2022 | 8.000 | 2016-08 | 53 | 12 | 243.102 | 2,439.944 | 10.037 | sí | 3,349.164 | 1,986.098 | 0.593 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2022 | 9.000 | 2016-08 | 53 | 12 | 276.112 | 2,583.801 | 9.358 | sí | 3,349.164 | 1,986.098 | 0.593 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2023 | 0.000 | 2016-08 | 65 | 12 | 325.498 | 4,465.913 | 13.720 | sí | 3,097.521 | 3,762.176 | 1.215 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2023 | 1.000 | 2016-08 | 65 | 12 | 366.503 | 4,392.210 | 11.984 | sí | 3,097.521 | 3,762.176 | 1.215 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2023 | 2.000 | 2016-08 | 65 | 12 | 320.477 | 4,425.103 | 13.808 | sí | 3,097.521 | 3,762.176 | 1.215 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2023 | 3.000 | 2016-08 | 65 | 12 | 343.803 | 4,673.487 | 13.594 | sí | 3,097.521 | 3,762.176 | 1.215 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2023 | 4.000 | 2016-08 | 65 | 12 | 349.470 | 4,604.030 | 13.174 | sí | 3,097.521 | 3,762.176 | 1.215 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2023 | 5.000 | 2016-08 | 65 | 12 | 314.079 | 4,457.198 | 14.191 | sí | 3,097.521 | 3,762.176 | 1.215 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2023 | 6.000 | 2016-08 | 65 | 12 | 328.825 | 4,612.675 | 14.028 | sí | 3,097.521 | 3,762.176 | 1.215 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2023 | 7.000 | 2016-08 | 65 | 12 | 346.316 | 4,506.108 | 13.012 | sí | 3,097.521 | 3,762.176 | 1.215 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2023 | 8.000 | 2016-08 | 65 | 12 | 354.695 | 4,410.519 | 12.435 | sí | 3,097.521 | 3,762.176 | 1.215 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2023 | 9.000 | 2016-08 | 65 | 12 | 328.629 | 4,461.284 | 13.575 | sí | 3,097.521 | 3,762.176 | 1.215 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2024 | 0.000 | 2016-08 | 77 | 12 | 457.499 | 4,230.593 | 9.247 | sí | 3,201.103 | 4,589.653 | 1.434 | no | no | no | sí | — | — |
| XGB-43 | sutil | 2024 | 1.000 | 2016-08 | 77 | 12 | 446.451 | 4,065.346 | 9.106 | sí | 3,201.103 | 4,589.653 | 1.434 | no | no | no | sí | — | — |
| XGB-43 | sutil | 2024 | 2.000 | 2016-08 | 77 | 12 | 486.674 | 4,147.526 | 8.522 | sí | 3,201.103 | 4,589.653 | 1.434 | no | no | no | sí | — | — |
| XGB-43 | sutil | 2024 | 3.000 | 2016-08 | 77 | 12 | 485.610 | 3,919.192 | 8.071 | sí | 3,201.103 | 4,589.653 | 1.434 | no | no | no | sí | — | — |
| XGB-43 | sutil | 2024 | 4.000 | 2016-08 | 77 | 12 | 478.450 | 3,665.529 | 7.661 | sí | 3,201.103 | 4,589.653 | 1.434 | no | no | no | sí | — | — |
| XGB-43 | sutil | 2024 | 5.000 | 2016-08 | 77 | 12 | 465.339 | 4,167.193 | 8.955 | sí | 3,201.103 | 4,589.653 | 1.434 | no | no | no | sí | — | — |
| XGB-43 | sutil | 2024 | 6.000 | 2016-08 | 77 | 12 | 491.333 | 3,784.260 | 7.702 | sí | 3,201.103 | 4,589.653 | 1.434 | no | no | no | sí | — | — |
| XGB-43 | sutil | 2024 | 7.000 | 2016-08 | 77 | 12 | 472.087 | 4,000.714 | 8.475 | sí | 3,201.103 | 4,589.653 | 1.434 | no | no | no | sí | — | — |
| XGB-43 | sutil | 2024 | 8.000 | 2016-08 | 77 | 12 | 486.800 | 3,727.157 | 7.656 | sí | 3,201.103 | 4,589.653 | 1.434 | no | no | no | sí | — | — |
| XGB-43 | sutil | 2024 | 9.000 | 2016-08 | 77 | 12 | 470.499 | 3,847.969 | 8.178 | sí | 3,201.103 | 4,589.653 | 1.434 | no | no | no | sí | — | — |
| XGB-43 | sutil | 2025 | 0.000 | 2016-08 | 89 | 12 | 602.421 | 5,152.138 | 8.552 | sí | 3,388.324 | 3,078.133 | 0.908 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2025 | 1.000 | 2016-08 | 89 | 12 | 635.060 | 4,622.186 | 7.278 | sí | 3,388.324 | 3,078.133 | 0.908 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2025 | 2.000 | 2016-08 | 89 | 12 | 626.243 | 4,757.790 | 7.597 | sí | 3,388.324 | 3,078.133 | 0.908 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2025 | 3.000 | 2016-08 | 89 | 12 | 639.397 | 5,018.742 | 7.849 | sí | 3,388.324 | 3,078.133 | 0.908 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2025 | 4.000 | 2016-08 | 89 | 12 | 670.401 | 4,810.868 | 7.176 | sí | 3,388.324 | 3,078.133 | 0.908 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2025 | 5.000 | 2016-08 | 89 | 12 | 603.973 | 4,930.746 | 8.164 | sí | 3,388.324 | 3,078.133 | 0.908 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2025 | 6.000 | 2016-08 | 89 | 12 | 597.117 | 4,919.135 | 8.238 | sí | 3,388.324 | 3,078.133 | 0.908 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2025 | 7.000 | 2016-08 | 89 | 12 | 633.641 | 4,602.969 | 7.264 | sí | 3,388.324 | 3,078.133 | 0.908 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2025 | 8.000 | 2016-08 | 89 | 12 | 606.313 | 5,109.246 | 8.427 | sí | 3,388.324 | 3,078.133 | 0.908 | sí | no | sí | sí | — | — |
| XGB-43 | sutil | 2025 | 9.000 | 2016-08 | 89 | 12 | 622.370 | 5,183.939 | 8.329 | sí | 3,388.324 | 3,078.133 | 0.908 | sí | no | sí | sí | — | — |

### T20_sarima_sel_candidatos.csv — T20 candidatos: los 5 candidatos por AIC de SARIMA-sel en cada ventana

`06_metricas/por_ventana/T20_sarima_sel_candidatos.csv` — 50 filas × 10 columnas.

| posicion_aic | indice_rejilla | order | seasonal_order | aic_rejilla_maxiter200 | aic_maxiter500 | MAE_val | convergio_maxiter500 | cultivar | anio_test |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 306 | (2, 0, 1) | (0, 0, 0, 12) | 467.527 | 467.527 | 57.917 | sí | dulce | 2021 |
| 2 | 342 | (2, 0, 3) | (0, 0, 0, 12) | 470.143 | 470.143 | 36.757 | sí | dulce | 2021 |
| 3 | 450 | (3, 0, 1) | (0, 0, 0, 12) | 475.410 | 475.410 | 62.004 | sí | dulce | 2021 |
| 4 | 324 | (2, 0, 2) | (0, 0, 0, 12) | 475.893 | 475.893 | 62.039 | sí | dulce | 2021 |
| 5 | 468 | (3, 0, 2) | (0, 0, 0, 12) | 478.807 | 478.807 | 61.424 | sí | dulce | 2021 |
| 1 | 342 | (2, 0, 3) | (0, 0, 0, 12) | 590.733 | 590.733 | 25.995 | sí | dulce | 2022 |
| 2 | 147 | (1, 0, 0) | (0, 1, 0, 12) | 594.276 | 594.276 | 13.562 | sí | dulce | 2022 |
| 3 | 60 | (0, 0, 3) | (1, 0, 0, 12) | 595.811 | 595.811 | 14.980 | sí | dulce | 2022 |
| 4 | 306 | (2, 0, 1) | (0, 0, 0, 12) | 595.961 | 595.961 | 28.505 | sí | dulce | 2022 |
| 5 | 291 | (2, 0, 0) | (0, 1, 0, 12) | 596.608 | 596.608 | 13.975 | sí | dulce | 2022 |
| 1 | 147 | (1, 0, 0) | (0, 1, 0, 12) | 700.254 | 700.254 | 12.211 | sí | dulce | 2023 |
| 2 | 60 | (0, 0, 3) | (1, 0, 0, 12) | 701.325 | 701.325 | 16.393 | sí | dulce | 2023 |
| 3 | 42 | (0, 0, 2) | (1, 0, 0, 12) | 702.584 | 702.584 | 16.828 | sí | dulce | 2023 |
| 4 | 291 | (2, 0, 0) | (0, 1, 0, 12) | 702.601 | 702.601 | 11.980 | sí | dulce | 2023 |
| 5 | 165 | (1, 0, 1) | (0, 1, 0, 12) | 702.608 | 702.608 | 12.069 | sí | dulce | 2023 |
| 1 | 147 | (1, 0, 0) | (0, 1, 0, 12) | 803.637 | 803.637 | 18.947 | sí | dulce | 2024 |
| 2 | 291 | (2, 0, 0) | (0, 1, 0, 12) | 805.749 | 805.749 | 17.326 | sí | dulce | 2024 |
| 3 | 165 | (1, 0, 1) | (0, 1, 0, 12) | 805.816 | 805.816 | 17.427 | sí | dulce | 2024 |
| 4 | 60 | (0, 0, 3) | (1, 0, 0, 12) | 806.433 | 806.433 | 19.745 | sí | dulce | 2024 |
| 5 | 309 | (2, 0, 1) | (0, 1, 0, 12) | 807.741 | 807.741 | 17.352 | sí | dulce | 2024 |
| 1 | 147 | (1, 0, 0) | (0, 1, 0, 12) | 911.155 | 911.155 | 26.082 | sí | dulce | 2025 |
| 2 | 291 | (2, 0, 0) | (0, 1, 0, 12) | 911.487 | 911.487 | 25.881 | sí | dulce | 2025 |
| 3 | 165 | (1, 0, 1) | (0, 1, 0, 12) | 911.700 | 911.700 | 25.895 | sí | dulce | 2025 |
| 4 | 309 | (2, 0, 1) | (0, 1, 0, 12) | 913.486 | 913.486 | 25.862 | sí | dulce | 2025 |
| 5 | 60 | (0, 0, 3) | (1, 0, 0, 12) | 914.095 | 914.095 | 27.339 | sí | dulce | 2025 |
| 1 | 556 | (3, 1, 2) | (2, 1, 1, 12) | 954.397 | 954.397 | 2,668.640 | sí | sutil | 2021 |
| 2 | 81 | (0, 1, 0) | (1, 1, 0, 12) | 954.415 | 954.415 | 3,151.221 | sí | sutil | 2021 |
| 3 | 376 | (2, 1, 0) | (2, 1, 1, 12) | 954.420 | 954.420 | 2,256.733 | sí | sutil | 2021 |
| 4 | 232 | (1, 1, 0) | (2, 1, 1, 12) | 954.469 | 954.469 | 2,306.424 | sí | sutil | 2021 |
| 5 | 88 | (0, 1, 0) | (2, 1, 1, 12) | 954.481 | 954.481 | 2,483.482 | sí | sutil | 2021 |
| 1 | 287 | (1, 1, 3) | (2, 1, 2, 12) | 1,182.132 | 1,182.132 | 2,035.086 | sí | sutil | 2022 |
| 2 | 269 | (1, 1, 2) | (2, 1, 2, 12) | 1,182.757 | 1,182.757 | 2,187.990 | sí | sutil | 2022 |
| 3 | 267 | (1, 1, 2) | (2, 1, 0, 12) | 1,183.476 | 1,183.476 | 2,497.765 | sí | sutil | 2022 |
| 4 | 557 | (3, 1, 2) | (2, 1, 2, 12) | 1,183.610 | 1,183.610 | 1,942.182 | sí | sutil | 2022 |
| 5 | 387 | (2, 1, 1) | (1, 1, 0, 12) | 1,183.759 | 1,183.759 | 2,466.572 | sí | sutil | 2022 |
| 1 | 268 | (1, 1, 2) | (2, 1, 1, 12) | 1,405.851 | 1,405.851 | 2,538.916 | sí | sutil | 2023 |
| 2 | 286 | (1, 1, 3) | (2, 1, 1, 12) | 1,406.295 | 1,406.295 | 2,514.291 | sí | sutil | 2023 |
| 3 | 269 | (1, 1, 2) | (2, 1, 2, 12) | 1,406.908 | 1,406.908 | 2,626.444 | sí | sutil | 2023 |
| 4 | 287 | (1, 1, 3) | (2, 1, 2, 12) | 1,407.276 | 1,407.276 | 2,561.468 | sí | sutil | 2023 |
| 5 | 412 | (2, 1, 2) | (2, 1, 1, 12) | 1,407.290 | 1,407.290 | 2,527.332 | sí | sutil | 2023 |
| 1 | 268 | (1, 1, 2) | (2, 1, 1, 12) | 1,635.000 | 1,635.000 | 4,175.170 | sí | sutil | 2024 |
| 2 | 412 | (2, 1, 2) | (2, 1, 1, 12) | 1,636.163 | 1,636.163 | 4,272.281 | sí | sutil | 2024 |
| 3 | 269 | (1, 1, 2) | (2, 1, 2, 12) | 1,636.678 | 1,636.678 | 4,252.791 | sí | sutil | 2024 |
| 4 | 556 | (3, 1, 2) | (2, 1, 1, 12) | 1,636.687 | 1,636.687 | 4,266.265 | sí | sutil | 2024 |
| 5 | 413 | (2, 1, 2) | (2, 1, 2, 12) | 1,637.789 | 1,637.789 | 4,318.246 | sí | sutil | 2024 |
| 1 | 268 | (1, 1, 2) | (2, 1, 1, 12) | 1,872.831 | 1,872.831 | 3,291.035 | sí | sutil | 2025 |
| 2 | 267 | (1, 1, 2) | (2, 1, 0, 12) | 1,873.967 | 1,873.967 | 2,991.104 | sí | sutil | 2025 |
| 3 | 412 | (2, 1, 2) | (2, 1, 1, 12) | 1,874.889 | 1,874.889 | 3,347.438 | sí | sutil | 2025 |
| 4 | 285 | (1, 1, 3) | (2, 1, 0, 12) | 1,874.931 | 1,874.931 | 2,880.513 | sí | sutil | 2025 |
| 5 | 269 | (1, 1, 2) | (2, 1, 2, 12) | 1,874.992 | 1,874.992 | 3,271.866 | sí | sutil | 2025 |

### T03_descripcion_particiones.csv — T03 completa: descripción por partición, 2018–2025

`06_metricas/descripcion_series/T03_descripcion_particiones.csv` — 48 filas × 11 columnas.

| cultivar | anio_test | particion | inicio | fin | n | media | DE | min | max | CV |
|---|---|---|---|---|---|---|---|---|---|---|
| sutil | 2018 | train | 2016-07 | 2016-12 | 6 | 19,410.469 | 1,865.617 | 16,714.142 | 21,609.215 | 0.096 |
| sutil | 2018 | val | 2017-01 | 2017-12 | 12 | 13,584.195 | 6,314.928 | 4,851.691 | 22,283.255 | 0.465 |
| sutil | 2018 | test | 2018-01 | 2018-12 | 12 | 21,508.722 | 6,499.445 | 12,761.937 | 29,894.931 | 0.302 |
| sutil | 2019 | train | 2016-07 | 2017-12 | 18 | 15,526.287 | 5,900.378 | 4,851.691 | 22,283.255 | 0.380 |
| sutil | 2019 | val | 2018-01 | 2018-12 | 12 | 21,508.722 | 6,499.445 | 12,761.937 | 29,894.931 | 0.302 |
| sutil | 2019 | test | 2019-01 | 2019-12 | 12 | 24,204.928 | 6,927.318 | 12,990.996 | 33,259.076 | 0.286 |
| sutil | 2020 | train | 2016-07 | 2018-12 | 30 | 17,919.261 | 6,731.811 | 4,851.691 | 29,894.931 | 0.376 |
| sutil | 2020 | val | 2019-01 | 2019-12 | 12 | 24,204.928 | 6,927.318 | 12,990.996 | 33,259.076 | 0.286 |
| sutil | 2020 | test | 2020-01 | 2020-12 | 12 | 25,131.794 | 6,673.009 | 14,809.668 | 35,010.363 | 0.266 |
| sutil | 2021 | train | 2016-07 | 2019-12 | 42 | 19,715.166 | 7,293.031 | 4,851.691 | 33,259.076 | 0.370 |
| sutil | 2021 | val | 2020-01 | 2020-12 | 12 | 25,131.794 | 6,673.009 | 14,809.668 | 35,010.363 | 0.266 |
| sutil | 2021 | test | 2021-01 | 2021-12 | 12 | 27,980.456 | 4,361.778 | 22,838.582 | 35,179.894 | 0.156 |
| sutil | 2022 | train | 2016-07 | 2020-12 | 54 | 20,918.861 | 7,453.476 | 4,851.691 | 35,010.363 | 0.356 |
| sutil | 2022 | val | 2021-01 | 2021-12 | 12 | 27,980.456 | 4,361.778 | 22,838.582 | 35,179.894 | 0.156 |
| sutil | 2022 | test | 2022-01 | 2022-12 | 12 | 30,558.091 | 8,003.630 | 20,729.512 | 41,867.719 | 0.262 |
| sutil | 2023 | train | 2016-07 | 2021-12 | 66 | 22,202.787 | 7,486.654 | 4,851.691 | 35,179.894 | 0.337 |
| sutil | 2023 | val | 2022-01 | 2022-12 | 12 | 30,558.091 | 8,003.630 | 20,729.512 | 41,867.719 | 0.262 |
| sutil | 2023 | test | 2023-01 | 2023-12 | 12 | 23,066.544 | 8,319.475 | 9,388.396 | 36,552.314 | 0.361 |
| sutil | 2024 | train | 2016-07 | 2022-12 | 78 | 23,488.219 | 8,103.822 | 4,851.691 | 41,867.719 | 0.345 |
| sutil | 2024 | val | 2023-01 | 2023-12 | 12 | 23,066.544 | 8,319.475 | 9,388.396 | 36,552.314 | 0.361 |
| sutil | 2024 | test | 2024-01 | 2024-12 | 12 | 32,208.767 | 8,549.900 | 23,811.288 | 44,161.843 | 0.265 |
| sutil | 2025 | train | 2016-07 | 2023-12 | 90 | 23,431.995 | 8,086.567 | 4,851.691 | 41,867.719 | 0.345 |
| sutil | 2025 | val | 2024-01 | 2024-12 | 12 | 32,208.767 | 8,549.900 | 23,811.288 | 44,161.843 | 0.265 |
| sutil | 2025 | test | 2025-01 | 2025-12 | 12 | 31,908.272 | 9,103.221 | 18,017.175 | 42,119.744 | 0.285 |
| dulce | 2018 | train | 2016-07 | 2016-12 | 6 | 289.644 | 117.340 | 135.700 | 462.117 | 0.405 |
| dulce | 2018 | val | 2017-01 | 2017-12 | 12 | 406.195 | 138.630 | 199.100 | 630.728 | 0.341 |
| dulce | 2018 | test | 2018-01 | 2018-12 | 12 | 410.163 | 155.347 | 164.900 | 616.059 | 0.379 |
| dulce | 2019 | train | 2016-07 | 2017-12 | 18 | 367.344 | 140.290 | 135.700 | 630.728 | 0.382 |
| dulce | 2019 | val | 2018-01 | 2018-12 | 12 | 410.163 | 155.347 | 164.900 | 616.059 | 0.379 |
| dulce | 2019 | test | 2019-01 | 2019-12 | 12 | 389.636 | 150.087 | 166.300 | 614.860 | 0.385 |
| dulce | 2020 | train | 2016-07 | 2018-12 | 30 | 384.472 | 145.418 | 135.700 | 630.728 | 0.378 |
| dulce | 2020 | val | 2019-01 | 2019-12 | 12 | 389.636 | 150.087 | 166.300 | 614.860 | 0.385 |
| dulce | 2020 | test | 2020-01 | 2020-12 | 12 | 379.511 | 144.560 | 180.680 | 573.589 | 0.381 |
| dulce | 2021 | train | 2016-07 | 2019-12 | 42 | 385.947 | 144.935 | 135.700 | 630.728 | 0.376 |
| dulce | 2021 | val | 2020-01 | 2020-12 | 12 | 379.511 | 144.560 | 180.680 | 573.589 | 0.381 |
| dulce | 2021 | test | 2021-01 | 2021-12 | 12 | 393.793 | 143.990 | 205.930 | 600.290 | 0.366 |
| dulce | 2022 | train | 2016-07 | 2020-12 | 54 | 384.517 | 143.508 | 135.700 | 630.728 | 0.373 |
| dulce | 2022 | val | 2021-01 | 2021-12 | 12 | 393.793 | 143.990 | 205.930 | 600.290 | 0.366 |
| dulce | 2022 | test | 2022-01 | 2022-12 | 12 | 406.399 | 154.543 | 205.780 | 636.740 | 0.380 |
| dulce | 2023 | train | 2016-07 | 2021-12 | 66 | 386.204 | 142.528 | 135.700 | 630.728 | 0.369 |
| dulce | 2023 | val | 2022-01 | 2022-12 | 12 | 406.399 | 154.543 | 205.780 | 636.740 | 0.380 |
| dulce | 2023 | test | 2023-01 | 2023-12 | 12 | 406.482 | 159.876 | 206.380 | 663.150 | 0.393 |
| dulce | 2024 | train | 2016-07 | 2022-12 | 78 | 389.311 | 143.576 | 135.700 | 636.740 | 0.369 |
| dulce | 2024 | val | 2023-01 | 2023-12 | 12 | 406.482 | 159.876 | 206.380 | 663.150 | 0.393 |
| dulce | 2024 | test | 2024-01 | 2024-12 | 12 | 448.290 | 161.374 | 229.400 | 675.798 | 0.360 |
| dulce | 2025 | train | 2016-07 | 2023-12 | 90 | 391.600 | 145.011 | 135.700 | 663.150 | 0.370 |
| dulce | 2025 | val | 2024-01 | 2024-12 | 12 | 448.290 | 161.374 | 229.400 | 675.798 | 0.360 |
| dulce | 2025 | test | 2025-01 | 2025-12 | 12 | 467.800 | 177.270 | 228.650 | 730.430 | 0.379 |

### T04_acf_adf_kpss_train.csv — T04 completa: ACF, ADF y KPSS (estadísticos, p y retardos)

`06_metricas/descripcion_series/T04_acf_adf_kpss_train.csv` — 16 filas × 18 columnas.

| cultivar | anio_test | n_train | n_D12 | ACF1 | ACF12 | ADF_nivel_est | ADF_nivel_p | ADF_nivel_lags | KPSS_nivel_est | KPSS_nivel_p | KPSS_nivel_p_acotado | ADF_D12_est | ADF_D12_p | ADF_D12_lags | KPSS_D12_est | KPSS_D12_p | KPSS_D12_p_acotado |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| sutil | 2018 | 6 | 0 | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| sutil | 2019 | 18 | 12 | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| sutil | 2020 | 30 | 24 | 0.822 | 0.045 | -2.615 | 0.090 | 1.000 | 0.086 | 0.100 | sí | -3.118 | 0.025 | 8.000 | 0.442 | 0.059 | no |
| sutil | 2021 | 42 | 36 | 0.839 | 0.334 | -3.407 | 0.011 | 1.000 | 0.185 | 0.100 | sí | -4.589 | 0.000 | 8.000 | 0.405 | 0.075 | no |
| sutil | 2022 | 54 | 48 | 0.812 | 0.489 | -3.706 | 0.004 | 1.000 | 0.313 | 0.100 | sí | -4.156 | 0.001 | 8.000 | 0.276 | 0.100 | sí |
| sutil | 2023 | 66 | 60 | 0.840 | 0.545 | -3.859 | 0.002 | 1.000 | 0.528 | 0.035 | no | -3.243 | 0.018 | 1.000 | 0.270 | 0.100 | sí |
| sutil | 2024 | 78 | 72 | 0.855 | 0.559 | -0.635 | 0.863 | 9.000 | 0.675 | 0.016 | no | -2.742 | 0.067 | 12.000 | 0.250 | 0.100 | sí |
| sutil | 2025 | 90 | 84 | 0.849 | 0.585 | -1.273 | 0.641 | 9.000 | 0.513 | 0.039 | no | -1.652 | 0.456 | 12.000 | 0.180 | 0.100 | sí |
| dulce | 2018 | 6 | 0 | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| dulce | 2019 | 18 | 12 | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| dulce | 2020 | 30 | 24 | 0.781 | 0.527 | -5.207 | 0.000 | 5.000 | 0.080 | 0.100 | sí | 0.502 | 0.985 | 9.000 | 0.293 | 0.100 | sí |
| dulce | 2021 | 42 | 36 | 0.794 | 0.667 | -2.046 | 0.267 | 10.000 | 0.058 | 0.100 | sí | -2.902 | 0.045 | 0.000 | 0.566 | 0.027 | no |
| dulce | 2022 | 54 | 48 | 0.801 | 0.743 | -0.371 | 0.915 | 11.000 | 0.049 | 0.100 | sí | -3.610 | 0.006 | 0.000 | 0.534 | 0.034 | no |
| dulce | 2023 | 66 | 60 | 0.809 | 0.786 | -0.928 | 0.779 | 11.000 | 0.036 | 0.100 | sí | -4.084 | 0.001 | 0.000 | 0.312 | 0.100 | sí |
| dulce | 2024 | 78 | 72 | 0.815 | 0.808 | -1.671 | 0.446 | 12.000 | 0.026 | 0.100 | sí | -4.421 | 0.000 | 0.000 | 0.224 | 0.100 | sí |
| dulce | 2025 | 90 | 84 | 0.818 | 0.832 | -1.807 | 0.377 | 12.000 | 0.022 | 0.100 | sí | -5.074 | 0.000 | 0.000 | 0.195 | 0.100 | sí |

### barrido_por_modelo.csv — Barrido mensual completo: modelo × percentil

`07_barrido_umbral/mensual/barrido_por_modelo.csv` — 380 filas × 13 columnas.

| cultivar | tipo | percentil | modelo | n_shock | MAE_shock | MAE_normal | Delta_s | razon_shock_normal | posicion | primero | dif_vs_mejor_lo | dif_vs_mejor_hi |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| sutil | mensual | 0 | Naive | 60 | 3,624.070 | — | 0.000 | — | 4 | no | 403.507 | 1,555.865 |
| sutil | mensual | 0 | Seasonal Naive | 60 | 6,074.886 | — | 0.000 | — | 8 | no | 2,444.779 | 4,367.800 |
| sutil | mensual | 0 | Chronos | 60 | 2,648.547 | — | 0.000 | — | 1 | sí | 0.000 | 0.000 |
| sutil | mensual | 0 | SARIMA | 60 | 3,360.787 | — | 0.000 | — | 3 | no | 143.018 | 1,264.060 |
| sutil | mensual | 0 | SARIMA-sel | 60 | 3,205.876 | — | 0.000 | — | 2 | sí | -82.699 | 1,193.595 |
| sutil | mensual | 0 | Ridge | 60 | 4,925.136 | — | 0.000 | — | 7 | no | 1,150.943 | 3,504.549 |
| sutil | mensual | 0 | ElasticNet | 60 | 4,871.911 | — | 0.000 | — | 5 | no | 1,164.437 | 3,356.463 |
| sutil | mensual | 0 | XGB-37 | 60 | 4,881.450 | — | 0.000 | — | 6 | no | 1,351.795 | 3,110.266 |
| sutil | mensual | 0 | GC3 | 60 | 6,361.305 | — | 0.000 | — | 9 | no | 2,517.657 | 4,919.015 |
| sutil | mensual | 0 | GE | 60 | 6,743.530 | — | 0.000 | — | 10 | no | 2,847.076 | 5,360.660 |
| sutil | mensual | 10 | Naive | 51 | 4,228.721 | 197.716 | 16.684 | 21.388 | 4 | no | 890.639 | 2,083.374 |
| sutil | mensual | 10 | Seasonal Naive | 51 | 5,729.885 | 8,029.890 | -5.679 | 0.714 | 8 | no | 1,922.922 | 4,002.522 |
| sutil | mensual | 10 | Chronos | 51 | 2,747.859 | 2,085.775 | 3.750 | 1.317 | 1 | sí | 0.000 | 0.000 |
| sutil | mensual | 10 | SARIMA | 51 | 3,305.505 | 3,674.053 | -1.645 | 0.900 | 3 | sí | -54.688 | 1,154.298 |
| sutil | mensual | 10 | SARIMA-sel | 51 | 3,140.260 | 3,577.700 | -2.047 | 0.878 | 2 | sí | -283.691 | 1,055.271 |
| sutil | mensual | 10 | Ridge | 51 | 5,198.728 | 3,374.779 | 5.555 | 1.540 | 7 | no | 1,170.797 | 3,831.271 |
| sutil | mensual | 10 | ElasticNet | 51 | 5,129.982 | 3,409.513 | 5.297 | 1.505 | 6 | no | 1,184.463 | 3,648.939 |
| sutil | mensual | 10 | XGB-37 | 51 | 4,883.691 | 4,868.751 | 0.046 | 1.003 | 5 | no | 1,212.180 | 3,029.799 |
| sutil | mensual | 10 | GC3 | 51 | 6,430.617 | 5,968.534 | 1.090 | 1.077 | 9 | no | 2,462.227 | 4,860.422 |
| sutil | mensual | 10 | GE | 51 | 6,816.594 | 6,329.500 | 1.083 | 1.077 | 10 | no | 2,733.944 | 5,316.879 |
| sutil | mensual | 15 | Naive | 47 | 4,540.890 | 309.417 | 25.298 | 14.676 | 4 | no | 1,083.953 | 2,256.115 |
| sutil | mensual | 15 | Seasonal Naive | 47 | 5,711.376 | 7,389.115 | -5.984 | 0.773 | 8 | no | 1,853.497 | 3,830.851 |
| sutil | mensual | 15 | Chronos | 47 | 2,867.830 | 1,855.752 | 8.279 | 1.545 | 1 | sí | 0.000 | 0.000 |
| sutil | mensual | 15 | SARIMA | 47 | 3,344.572 | 3,419.411 | -0.482 | 0.978 | 3 | sí | -174.805 | 1,098.010 |
| sutil | mensual | 15 | SARIMA-sel | 47 | 3,107.692 | 3,560.851 | -3.063 | 0.873 | 2 | sí | -464.781 | 915.666 |
| sutil | mensual | 15 | Ridge | 47 | 5,350.974 | 3,385.569 | 8.646 | 1.581 | 7 | no | 1,131.275 | 3,943.344 |
| sutil | mensual | 15 | ElasticNet | 47 | 5,260.394 | 3,467.395 | 7.974 | 1.517 | 6 | no | 1,144.184 | 3,709.160 |
| sutil | mensual | 15 | XGB-37 | 47 | 4,939.617 | 4,671.153 | 1.192 | 1.057 | 5 | no | 1,167.072 | 2,968.269 |
| sutil | mensual | 15 | GC3 | 47 | 6,369.986 | 6,329.917 | 0.136 | 1.006 | 9 | no | 2,316.423 | 4,690.902 |
| sutil | mensual | 15 | GE | 47 | 6,829.152 | 6,433.974 | 1.270 | 1.061 | 10 | no | 2,696.979 | 5,231.606 |
| sutil | mensual | 20 | Naive | 45 | 4,694.896 | 411.594 | 29.548 | 11.407 | 4 | no | 1,169.791 | 2,358.458 |
| sutil | mensual | 20 | Seasonal Naive | 45 | 5,786.185 | 6,940.988 | -4.752 | 0.834 | 8 | no | 1,867.043 | 3,824.007 |
| sutil | mensual | 20 | Chronos | 45 | 2,931.889 | 1,798.519 | 10.698 | 1.630 | 1 | sí | 0.000 | 0.000 |
| sutil | mensual | 20 | SARIMA | 45 | 3,456.683 | 3,073.101 | 2.853 | 1.125 | 3 | sí | -126.676 | 1,155.078 |
| sutil | mensual | 20 | SARIMA-sel | 45 | 3,102.302 | 3,516.601 | -3.231 | 0.882 | 2 | sí | -528.389 | 862.669 |
| sutil | mensual | 20 | Ridge | 45 | 5,454.310 | 3,337.612 | 10.744 | 1.634 | 7 | no | 1,121.681 | 4,047.597 |
| sutil | mensual | 20 | ElasticNet | 45 | 5,397.119 | 3,296.288 | 10.780 | 1.637 | 6 | no | 1,190.708 | 3,846.262 |
| sutil | mensual | 20 | XGB-37 | 45 | 4,837.021 | 5,014.735 | -0.910 | 0.965 | 5 | no | 999.419 | 2,804.117 |
| sutil | mensual | 20 | GC3 | 45 | 6,272.545 | 6,627.583 | -1.395 | 0.946 | 9 | no | 2,147.975 | 4,541.362 |
| sutil | mensual | 20 | GE | 45 | 6,658.688 | 6,998.055 | -1.258 | 0.952 | 10 | no | 2,423.717 | 5,011.108 |
| sutil | mensual | 25 | Naive | 43 | 4,868.834 | 475.551 | 34.347 | 10.238 | 4 | no | 1,244.790 | 2,452.101 |
| sutil | mensual | 25 | Seasonal Naive | 43 | 5,794.152 | 6,784.978 | -4.621 | 0.854 | 8 | no | 1,749.422 | 3,820.815 |
| sutil | mensual | 25 | Chronos | 43 | 3,009.338 | 1,735.958 | 13.622 | 1.734 | 1 | sí | 0.000 | 0.000 |
| sutil | mensual | 25 | SARIMA | 43 | 3,477.083 | 3,066.627 | 3.460 | 1.134 | 3 | sí | -208.515 | 1,126.907 |
| sutil | mensual | 25 | SARIMA-sel | 43 | 3,159.705 | 3,322.662 | -1.440 | 0.951 | 2 | sí | -586.093 | 885.809 |
| sutil | mensual | 25 | Ridge | 43 | 5,592.074 | 3,238.176 | 13.542 | 1.727 | 7 | no | 1,084.447 | 4,196.199 |
| sutil | mensual | 25 | ElasticNet | 43 | 5,541.281 | 3,178.800 | 13.739 | 1.743 | 6 | no | 1,166.393 | 3,995.275 |
| sutil | mensual | 25 | XGB-37 | 43 | 5,035.678 | 4,491.343 | 3.159 | 1.121 | 5 | no | 1,109.222 | 2,932.711 |
| sutil | mensual | 25 | GC3 | 43 | 6,471.266 | 6,083.167 | 1.729 | 1.064 | 9 | no | 2,252.125 | 4,690.243 |
| sutil | mensual | 25 | GE | 43 | 6,840.843 | 6,497.384 | 1.443 | 1.053 | 10 | no | 2,531.881 | 5,129.608 |
| sutil | mensual | 30 | Naive | 38 | 5,284.030 | 756.868 | 45.804 | 6.981 | 5 | no | 1,178.556 | 3,117.674 |
| sutil | mensual | 30 | Seasonal Naive | 38 | 5,888.081 | 6,397.548 | -3.075 | 0.920 | 6 | no | 1,729.221 | 3,789.143 |
| sutil | mensual | 30 | Chronos | 38 | 3,143.154 | 1,794.224 | 18.675 | 1.752 | 2 | sí | -752.085 | 792.914 |
| sutil | mensual | 30 | SARIMA | 38 | 3,350.658 | 3,378.282 | -0.301 | 0.992 | 3 | sí | -478.420 | 884.322 |
| sutil | mensual | 30 | SARIMA-sel | 38 | 3,132.586 | 3,332.468 | -2.286 | 0.940 | 1 | sí | 0.000 | 0.000 |
| sutil | mensual | 30 | Ridge | 38 | 5,946.258 | 3,161.380 | 20.733 | 1.881 | 8 | no | 1,085.144 | 4,667.979 |
| sutil | mensual | 30 | ElasticNet | 38 | 5,941.098 | 3,025.134 | 21.946 | 1.964 | 7 | no | 1,264.750 | 4,477.310 |
| sutil | mensual | 30 | XGB-37 | 38 | 5,183.097 | 4,360.423 | 6.179 | 1.189 | 4 | no | 1,067.699 | 3,090.654 |
| sutil | mensual | 30 | GC3 | 38 | 6,467.158 | 6,178.466 | 1.664 | 1.047 | 9 | no | 2,108.385 | 4,583.245 |
| sutil | mensual | 30 | GE | 38 | 6,548.173 | 7,080.965 | -2.897 | 0.925 | 10 | no | 2,161.086 | 4,725.512 |
| sutil | mensual | 35 | Naive | 36 | 5,453.898 | 879.329 | 50.491 | 6.202 | 5 | no | 1,556.808 | 2,819.709 |
| sutil | mensual | 35 | Seasonal Naive | 36 | 5,950.730 | 6,261.120 | -2.044 | 0.950 | 6 | no | 1,562.021 | 3,846.330 |
| sutil | mensual | 35 | Chronos | 36 | 3,259.770 | 1,731.711 | 23.078 | 1.882 | 1 | sí | 0.000 | 0.000 |
| sutil | mensual | 35 | SARIMA | 36 | 3,361.885 | 3,359.140 | 0.033 | 1.001 | 3 | sí | -617.656 | 785.201 |
| sutil | mensual | 35 | SARIMA-sel | 36 | 3,287.561 | 3,083.350 | 2.548 | 1.066 | 2 | sí | -781.530 | 850.268 |
| sutil | mensual | 35 | Ridge | 36 | 5,988.983 | 3,329.366 | 21.600 | 1.799 | 7 | no | 1,093.552 | 4,542.794 |
| sutil | mensual | 35 | ElasticNet | 36 | 6,031.832 | 3,132.030 | 23.808 | 1.926 | 8 | no | 1,254.924 | 4,413.667 |
| sutil | mensual | 35 | XGB-37 | 36 | 4,925.019 | 4,816.095 | 0.893 | 1.023 | 4 | no | 703.076 | 2,547.936 |
| sutil | mensual | 35 | GC3 | 36 | 6,334.804 | 6,401.055 | -0.417 | 0.990 | 9 | no | 1,813.863 | 4,365.758 |
| sutil | mensual | 35 | GE | 36 | 6,393.631 | 7,268.379 | -5.189 | 0.880 | 10 | no | 1,836.431 | 4,424.911 |
| sutil | mensual | 40 | Naive | 32 | 5,747.467 | 1,197.332 | 58.591 | 4.800 | 5 | no | 1,477.580 | 3,463.888 |
| sutil | mensual | 40 | Seasonal Naive | 32 | 6,317.005 | 5,798.179 | 3.986 | 1.089 | 8 | no | 1,957.693 | 4,163.233 |
| sutil | mensual | 40 | Chronos | 32 | 3,378.692 | 1,814.095 | 27.568 | 1.862 | 2 | sí | -729.919 | 929.822 |
| sutil | mensual | 40 | SARIMA | 32 | 3,476.124 | 3,228.973 | 3.432 | 1.077 | 3 | sí | -527.599 | 886.846 |
| sutil | mensual | 40 | SARIMA-sel | 32 | 3,272.319 | 3,129.942 | 2.073 | 1.045 | 1 | sí | 0.000 | 0.000 |
| sutil | mensual | 40 | Ridge | 32 | 6,629.376 | 2,977.433 | 34.603 | 2.227 | 9 | no | 1,474.693 | 5,373.495 |
| sutil | mensual | 40 | ElasticNet | 32 | 6,636.479 | 2,855.262 | 36.219 | 2.324 | 10 | no | 1,666.539 | 5,160.223 |
| sutil | mensual | 40 | XGB-37 | 32 | 4,835.542 | 4,933.916 | -0.940 | 0.980 | 4 | no | 588.013 | 2,503.909 |
| sutil | mensual | 40 | GC3 | 32 | 6,288.059 | 6,445.013 | -1.151 | 0.976 | 7 | no | 1,910.911 | 4,145.844 |
| sutil | mensual | 40 | GE | 32 | 6,264.310 | 7,291.210 | -7.106 | 0.859 | 6 | no | 1,861.600 | 4,131.959 |
| sutil | mensual | 45 | Naive | 29 | 6,021.010 | 1,381.772 | 66.139 | 4.357 | 5 | no | 1,646.621 | 3,696.866 |
| sutil | mensual | 45 | Seasonal Naive | 29 | 6,077.552 | 6,072.392 | 0.044 | 1.001 | 6 | no | 1,570.199 | 3,889.571 |
| sutil | mensual | 45 | Chronos | 29 | 3,538.684 | 1,815.837 | 33.609 | 1.949 | 2 | sí | -663.376 | 1,059.165 |
| sutil | mensual | 45 | SARIMA | 29 | 3,635.765 | 3,103.550 | 8.182 | 1.171 | 3 | sí | -532.952 | 1,002.688 |
| sutil | mensual | 45 | SARIMA-sel | 29 | 3,361.657 | 3,060.146 | 4.859 | 1.099 | 1 | sí | 0.000 | 0.000 |
| sutil | mensual | 45 | Ridge | 29 | 6,887.424 | 3,089.447 | 39.842 | 2.229 | 9 | no | 1,453.481 | 5,789.983 |
| sutil | mensual | 45 | ElasticNet | 29 | 6,898.785 | 2,975.804 | 41.603 | 2.318 | 10 | no | 1,686.063 | 5,548.444 |
| sutil | mensual | 45 | XGB-37 | 29 | 4,894.672 | 4,869.081 | 0.271 | 1.005 | 4 | no | 523.576 | 2,529.365 |
| sutil | mensual | 45 | GC3 | 29 | 6,218.033 | 6,495.333 | -2.252 | 0.957 | 8 | no | 1,774.834 | 3,945.956 |
| sutil | mensual | 45 | GE | 29 | 6,135.792 | 7,312.059 | -9.012 | 0.839 | 7 | no | 1,680.944 | 3,902.749 |
| sutil | mensual | 50 | Naive | 29 | 6,021.010 | 1,381.772 | 66.139 | 4.357 | 5 | no | 1,646.621 | 3,696.866 |
| sutil | mensual | 50 | Seasonal Naive | 29 | 6,077.552 | 6,072.392 | 0.044 | 1.001 | 6 | no | 1,570.199 | 3,889.571 |
| sutil | mensual | 50 | Chronos | 29 | 3,538.684 | 1,815.837 | 33.609 | 1.949 | 2 | sí | -663.376 | 1,059.165 |
| sutil | mensual | 50 | SARIMA | 29 | 3,635.765 | 3,103.550 | 8.182 | 1.171 | 3 | sí | -532.952 | 1,002.688 |
| sutil | mensual | 50 | SARIMA-sel | 29 | 3,361.657 | 3,060.146 | 4.859 | 1.099 | 1 | sí | 0.000 | 0.000 |
| sutil | mensual | 50 | Ridge | 29 | 6,887.424 | 3,089.447 | 39.842 | 2.229 | 9 | no | 1,453.481 | 5,789.983 |
| sutil | mensual | 50 | ElasticNet | 29 | 6,898.785 | 2,975.804 | 41.603 | 2.318 | 10 | no | 1,686.063 | 5,548.444 |
| sutil | mensual | 50 | XGB-37 | 29 | 4,894.672 | 4,869.081 | 0.271 | 1.005 | 4 | no | 523.576 | 2,529.365 |
| sutil | mensual | 50 | GC3 | 29 | 6,218.033 | 6,495.333 | -2.252 | 0.957 | 8 | no | 1,774.834 | 3,945.956 |
| sutil | mensual | 50 | GE | 29 | 6,135.792 | 7,312.059 | -9.012 | 0.839 | 7 | no | 1,680.944 | 3,902.749 |
| sutil | mensual | 55 | Naive | 28 | 6,131.808 | 1,429.800 | 69.197 | 4.289 | 5 | no | 1,714.577 | 3,808.018 |
| sutil | mensual | 55 | Seasonal Naive | 28 | 6,277.330 | 5,897.747 | 3.332 | 1.064 | 7 | no | 1,745.274 | 4,070.602 |
| sutil | mensual | 55 | Chronos | 28 | 3,655.531 | 1,767.435 | 38.020 | 2.068 | 2 | sí | -565.670 | 1,157.546 |
| sutil | mensual | 55 | SARIMA | 28 | 3,692.081 | 3,070.905 | 9.858 | 1.202 | 3 | sí | -487.553 | 1,078.481 |
| sutil | mensual | 55 | SARIMA-sel | 28 | 3,371.949 | 3,060.563 | 5.180 | 1.102 | 1 | sí | 0.000 | 0.000 |
| sutil | mensual | 55 | Ridge | 28 | 7,093.334 | 3,027.962 | 44.023 | 2.343 | 10 | no | 1,603.323 | 6,027.620 |
| sutil | mensual | 55 | ElasticNet | 28 | 7,080.376 | 2,939.505 | 45.331 | 2.409 | 9 | no | 1,808.198 | 5,771.551 |
| sutil | mensual | 55 | XGB-37 | 28 | 5,007.565 | 4,771.099 | 2.584 | 1.050 | 4 | no | 596.263 | 2,650.409 |
| sutil | mensual | 55 | GC3 | 28 | 6,312.041 | 6,404.410 | -0.774 | 0.986 | 8 | no | 1,836.017 | 4,110.914 |
| sutil | mensual | 55 | GE | 28 | 6,268.533 | 7,159.152 | -7.044 | 0.876 | 6 | no | 1,780.044 | 4,088.382 |
| sutil | mensual | 60 | Naive | 25 | 6,433.814 | 1,617.110 | 77.530 | 3.979 | 8 | no | 1,840.011 | 4,075.390 |
| sutil | mensual | 60 | Seasonal Naive | 25 | 6,319.781 | 5,899.961 | 4.031 | 1.071 | 5 | no | 1,570.146 | 4,144.209 |
| sutil | mensual | 60 | Chronos | 25 | 3,773.724 | 1,844.848 | 42.483 | 2.046 | 3 | sí | -618.258 | 1,246.077 |
| sutil | mensual | 60 | SARIMA | 25 | 3,524.969 | 3,243.514 | 4.885 | 1.087 | 2 | sí | -783.449 | 828.495 |
| sutil | mensual | 60 | SARIMA-sel | 25 | 3,477.513 | 3,011.850 | 8.473 | 1.155 | 1 | sí | 0.000 | 0.000 |
| sutil | mensual | 60 | Ridge | 25 | 7,496.933 | 3,088.138 | 52.218 | 2.428 | 10 | no | 1,595.045 | 6,643.578 |
| sutil | mensual | 60 | ElasticNet | 25 | 7,426.237 | 3,047.393 | 52.430 | 2.437 | 9 | no | 1,801.490 | 6,290.072 |
| sutil | mensual | 60 | XGB-37 | 25 | 5,217.449 | 4,641.450 | 6.883 | 1.124 | 4 | no | 649.767 | 2,814.538 |
| sutil | mensual | 60 | GC3 | 25 | 6,385.458 | 6,344.052 | 0.380 | 1.007 | 6 | no | 1,724.458 | 4,091.050 |
| sutil | mensual | 60 | GE | 25 | 6,401.773 | 6,987.642 | -5.068 | 0.916 | 7 | no | 1,741.591 | 4,124.713 |
| sutil | mensual | 65 | Naive | 21 | 6,895.427 | 1,862.571 | 90.267 | 3.702 | 8 | no | 2,529.895 | 4,767.202 |
| sutil | mensual | 65 | Seasonal Naive | 21 | 5,953.180 | 6,140.420 | -2.003 | 0.970 | 5 | no | 1,279.229 | 4,202.692 |
| sutil | mensual | 65 | Chronos | 21 | 3,737.563 | 2,062.153 | 41.117 | 1.812 | 3 | sí | -560.005 | 1,565.505 |
| sutil | mensual | 65 | SARIMA | 21 | 3,571.229 | 3,247.472 | 6.262 | 1.100 | 2 | sí | -552.043 | 1,150.154 |
| sutil | mensual | 65 | SARIMA-sel | 21 | 3,226.015 | 3,195.032 | 0.628 | 1.010 | 1 | sí | 0.000 | 0.000 |
| sutil | mensual | 65 | Ridge | 21 | 7,985.893 | 3,277.036 | 62.146 | 2.437 | 10 | no | 2,217.068 | 7,554.409 |
| sutil | mensual | 65 | ElasticNet | 21 | 7,797.523 | 3,296.582 | 60.051 | 2.365 | 9 | no | 2,216.267 | 7,088.205 |
| sutil | mensual | 65 | XGB-37 | 21 | 5,029.324 | 4,801.825 | 3.029 | 1.047 | 4 | no | 682.534 | 2,912.526 |
| sutil | mensual | 65 | GC3 | 21 | 6,555.666 | 6,256.648 | 3.055 | 1.048 | 6 | no | 2,128.953 | 4,648.897 |
| sutil | mensual | 65 | GE | 21 | 6,783.727 | 6,721.885 | 0.596 | 1.009 | 7 | no | 2,409.989 | 4,816.304 |
| sutil | mensual | 70 | Naive | 12 | 7,807.214 | 2,578.285 | 115.427 | 3.028 | 8 | no | 1,925.118 | 5,284.568 |
| sutil | mensual | 70 | Seasonal Naive | 12 | 5,102.588 | 6,317.960 | -16.005 | 0.808 | 4 | sí | -949.346 | 2,982.758 |
| sutil | mensual | 70 | Chronos | 12 | 4,458.241 | 2,196.123 | 68.328 | 2.030 | 2 | sí | -1,233.347 | 1,751.692 |
| sutil | mensual | 70 | SARIMA | 12 | 4,574.794 | 3,057.285 | 36.123 | 1.496 | 3 | sí | -851.120 | 1,500.700 |
| sutil | mensual | 70 | SARIMA-sel | 12 | 4,149.047 | 2,970.084 | 29.420 | 1.397 | 1 | sí | 0.000 | 0.000 |
| sutil | mensual | 70 | Ridge | 12 | 9,390.971 | 3,808.677 | 90.674 | 2.466 | 10 | no | 1,682.199 | 9,009.256 |
| sutil | mensual | 70 | ElasticNet | 12 | 8,860.548 | 3,874.752 | 81.870 | 2.287 | 9 | no | 1,577.548 | 8,011.336 |
| sutil | mensual | 70 | XGB-37 | 12 | 5,204.750 | 4,800.625 | 6.623 | 1.084 | 5 | sí | -566.498 | 2,620.975 |
| sutil | mensual | 70 | GC3 | 12 | 5,890.889 | 6,478.908 | -7.395 | 0.909 | 6 | no | 399.959 | 3,171.640 |
| sutil | mensual | 70 | GE | 12 | 6,318.271 | 6,849.845 | -6.306 | 0.922 | 7 | no | 744.228 | 3,691.428 |
| sutil | mensual | 75 | Naive | 10 | 8,506.195 | 2,647.646 | 134.714 | 3.213 | 9 | no | 3,101.807 | 4,319.284 |
| sutil | mensual | 75 | Seasonal Naive | 10 | 5,034.450 | 6,282.973 | -17.127 | 0.801 | 3 | sí | -1,966.386 | 2,657.895 |
| sutil | mensual | 75 | Chronos | 10 | 4,783.522 | 2,221.552 | 80.609 | 2.153 | 1 | sí | 0.000 | 0.000 |
| sutil | mensual | 75 | SARIMA | 10 | 5,130.719 | 3,006.801 | 52.664 | 1.706 | 4 | sí | -354.521 | 1,101.942 |
| sutil | mensual | 75 | SARIMA-sel | 10 | 4,935.734 | 2,859.905 | 53.959 | 1.726 | 2 | sí | -1,385.200 | 1,820.692 |
| sutil | mensual | 75 | Ridge | 10 | 8,556.902 | 4,198.783 | 73.739 | 2.038 | 10 | no | 992.553 | 7,654.036 |
| sutil | mensual | 75 | ElasticNet | 10 | 8,153.740 | 4,215.546 | 67.362 | 1.934 | 8 | no | 715.515 | 6,570.561 |
| sutil | mensual | 75 | XGB-37 | 10 | 5,955.201 | 4,666.700 | 21.997 | 1.276 | 5 | sí | -869.236 | 2,809.948 |
| sutil | mensual | 75 | GC3 | 10 | 6,074.460 | 6,418.674 | -4.509 | 0.946 | 6 | sí | -174.890 | 2,747.427 |
| sutil | mensual | 75 | GE | 10 | 6,826.646 | 6,726.907 | 1.233 | 1.015 | 7 | no | 78.054 | 3,911.162 |
| sutil | mensual | 80 | Naive | 8 | 8,737.194 | 2,837.436 | 141.088 | 3.079 | 8 | no | 2,860.420 | 4,337.823 |
| sutil | mensual | 80 | Seasonal Naive | 8 | 5,765.152 | 6,122.537 | -5.099 | 0.942 | 2 | sí | -1,976.738 | 3,474.123 |
| sutil | mensual | 80 | Chronos | 8 | 5,125.562 | 2,267.467 | 93.524 | 2.260 | 1 | sí | 0.000 | 0.000 |
| sutil | mensual | 80 | SARIMA | 8 | 6,103.563 | 2,938.822 | 81.611 | 2.077 | 4 | no | 364.620 | 1,471.878 |
| sutil | mensual | 80 | SARIMA-sel | 8 | 5,846.347 | 2,799.650 | 82.363 | 2.088 | 3 | sí | -803.261 | 2,500.924 |
| sutil | mensual | 80 | Ridge | 8 | 10,221.224 | 4,110.353 | 107.532 | 2.487 | 10 | no | 1,784.671 | 9,975.024 |
| sutil | mensual | 80 | ElasticNet | 8 | 9,837.658 | 4,107.950 | 101.926 | 2.395 | 9 | no | 1,546.522 | 8,657.367 |
| sutil | mensual | 80 | XGB-37 | 8 | 6,684.993 | 4,603.982 | 36.947 | 1.452 | 5 | sí | -1,053.994 | 3,301.467 |
| sutil | mensual | 80 | GC3 | 8 | 7,057.765 | 6,254.157 | 10.948 | 1.128 | 6 | no | 277.442 | 3,477.230 |
| sutil | mensual | 80 | GE | 8 | 8,009.619 | 6,548.747 | 18.775 | 1.223 | 7 | no | 700.014 | 4,853.949 |
| sutil | mensual | 85 | Naive | 7 | 9,036.655 | 2,909.201 | 149.351 | 3.106 | 8 | no | 2,989.818 | 4,285.745 |
| sutil | mensual | 85 | Seasonal Naive | 7 | 6,481.888 | 6,021.131 | 6.700 | 1.077 | 2 | sí | -1,900.848 | 3,749.657 |
| sutil | mensual | 85 | Chronos | 7 | 5,502.592 | 2,271.597 | 107.759 | 2.422 | 1 | sí | 0.000 | 0.000 |
| sutil | mensual | 85 | SARIMA | 7 | 6,811.895 | 2,904.980 | 102.687 | 2.345 | 4 | no | 1,040.270 | 1,502.580 |
| sutil | mensual | 85 | SARIMA-sel | 7 | 6,666.192 | 2,748.853 | 107.937 | 2.425 | 3 | sí | -389.348 | 2,996.751 |
| sutil | mensual | 85 | Ridge | 7 | 11,135.082 | 4,104.954 | 126.087 | 2.713 | 10 | no | 2,645.550 | 10,223.235 |
| sutil | mensual | 85 | ElasticNet | 7 | 10,759.924 | 4,094.249 | 120.856 | 2.628 | 9 | no | 2,235.287 | 8,820.657 |
| sutil | mensual | 85 | XGB-37 | 7 | 6,897.775 | 4,615.143 | 41.306 | 1.495 | 5 | sí | -1,529.949 | 3,282.880 |
| sutil | mensual | 85 | GC3 | 7 | 7,014.717 | 6,275.005 | 10.272 | 1.118 | 6 | sí | -292.669 | 3,316.920 |
| sutil | mensual | 85 | GE | 7 | 7,918.072 | 6,588.402 | 17.417 | 1.202 | 7 | no | 37.738 | 4,622.325 |
| sutil | mensual | 90 | Naive | 6 | 8,695.623 | 3,060.565 | 139.941 | 2.841 | 7 | no | 2,624.312 | 4,190.570 |
| sutil | mensual | 90 | Seasonal Naive | 6 | 7,309.129 | 5,937.748 | 20.317 | 1.231 | 4 | sí | -1,359.316 | 5,104.858 |
| sutil | mensual | 90 | Chronos | 6 | 5,436.358 | 2,338.790 | 105.258 | 2.324 | 1 | sí | 0.000 | 0.000 |
| sutil | mensual | 90 | SARIMA | 6 | 6,764.376 | 2,982.611 | 101.274 | 2.268 | 2 | no | 987.263 | 1,545.143 |
| sutil | mensual | 90 | SARIMA-sel | 6 | 7,095.584 | 2,773.687 | 121.331 | 2.558 | 3 | no | 97.723 | 3,574.510 |
| sutil | mensual | 90 | Ridge | 6 | 11,681.953 | 4,174.378 | 137.190 | 2.798 | 10 | no | 2,866.127 | 11,601.463 |
| sutil | mensual | 90 | ElasticNet | 6 | 10,856.235 | 4,206.986 | 122.833 | 2.581 | 9 | no | 2,525.649 | 9,574.760 |
| sutil | mensual | 90 | XGB-37 | 6 | 7,964.134 | 4,538.929 | 63.151 | 1.755 | 6 | no | 1,929.270 | 3,106.661 |
| sutil | mensual | 90 | GC3 | 6 | 7,906.910 | 6,189.571 | 24.297 | 1.277 | 5 | no | 805.271 | 4,407.900 |
| sutil | mensual | 90 | GE | 6 | 8,942.238 | 6,499.229 | 32.605 | 1.376 | 8 | no | 2,113.770 | 5,124.965 |
| sutil | mensual | 95 | Naive | 3 | 9,429.234 | 3,318.535 | 160.184 | 2.841 | 10 | no | 3,523.223 | 3,978.031 |
| sutil | mensual | 95 | Seasonal Naive | 3 | 6,994.790 | 6,026.470 | 15.143 | 1.161 | 4 | sí | -1,220.043 | 3,852.410 |
| sutil | mensual | 95 | Chronos | 3 | 5,678.607 | 2,489.070 | 114.405 | 2.281 | 1 | sí | 0.000 | 0.000 |
| sutil | mensual | 95 | SARIMA | 3 | 7,100.263 | 3,163.973 | 111.268 | 2.244 | 5 | no | 1,410.815 | 1,432.496 |
| sutil | mensual | 95 | SARIMA-sel | 3 | 6,250.219 | 3,045.648 | 94.961 | 2.052 | 2 | sí | -451.472 | 1,594.696 |
| sutil | mensual | 95 | Ridge | 3 | 7,619.570 | 4,783.324 | 54.708 | 1.593 | 7 | no | 1,097.825 | 2,784.101 |
| sutil | mensual | 95 | ElasticNet | 3 | 6,875.058 | 4,766.482 | 41.116 | 1.442 | 3 | no | 375.587 | 2,017.315 |
| sutil | mensual | 95 | XGB-37 | 3 | 9,159.728 | 4,656.277 | 87.644 | 1.967 | 8 | no | 3,463.444 | 3,498.796 |
| sutil | mensual | 95 | GC3 | 3 | 7,240.992 | 6,315.005 | 13.829 | 1.147 | 6 | no | 1,398.185 | 1,726.583 |
| sutil | mensual | 95 | GE | 3 | 9,277.919 | 6,610.141 | 37.583 | 1.404 | 9 | no | 2,781.420 | 4,417.204 |
| dulce | mensual | 0 | Naive | 60 | 77.522 | — | 0.000 | — | 10 | no | 46.088 | 72.497 |
| dulce | mensual | 0 | Seasonal Naive | 60 | 24.503 | — | 0.000 | — | 3 | no | 2.572 | 9.485 |
| dulce | mensual | 0 | Chronos | 60 | 30.819 | — | 0.000 | — | 4 | no | 6.033 | 18.704 |
| dulce | mensual | 0 | SARIMA | 60 | 18.412 | — | 0.000 | — | 1 | sí | 0.000 | 0.000 |
| dulce | mensual | 0 | SARIMA-sel | 60 | 20.629 | — | 0.000 | — | 2 | sí | -0.757 | 5.136 |
| dulce | mensual | 0 | Ridge | 60 | 53.070 | — | 0.000 | — | 7 | no | 24.819 | 45.154 |
| dulce | mensual | 0 | ElasticNet | 60 | 50.248 | — | 0.000 | — | 6 | no | 22.047 | 42.277 |
| dulce | mensual | 0 | XGB-37 | 60 | 48.260 | — | 0.000 | — | 5 | no | 20.516 | 39.560 |
| dulce | mensual | 0 | GC3 | 60 | 56.669 | — | 0.000 | — | 8 | no | 28.027 | 48.976 |
| dulce | mensual | 0 | GE | 60 | 56.734 | — | 0.000 | — | 9 | no | 28.405 | 48.725 |
| dulce | mensual | 10 | Naive | 59 | 78.764 | 4.250 | 1.602 | 18.533 | 10 | no | 46.849 | 73.772 |
| dulce | mensual | 10 | Seasonal Naive | 59 | 24.538 | 22.451 | 0.142 | 1.093 | 3 | no | 2.300 | 9.351 |
| dulce | mensual | 10 | Chronos | 59 | 31.220 | 7.118 | 1.303 | 4.386 | 4 | no | 5.924 | 19.099 |
| dulce | mensual | 10 | SARIMA | 59 | 18.628 | 5.682 | 1.172 | 3.279 | 1 | sí | 0.000 | 0.000 |
| dulce | mensual | 10 | SARIMA-sel | 59 | 20.921 | 3.374 | 1.418 | 6.201 | 2 | sí | -0.755 | 5.173 |
| dulce | mensual | 10 | Ridge | 59 | 53.924 | 2.673 | 1.610 | 20.174 | 7 | no | 25.218 | 45.697 |
| dulce | mensual | 10 | ElasticNet | 59 | 51.037 | 3.694 | 1.570 | 13.818 | 6 | no | 22.332 | 42.770 |
| dulce | mensual | 10 | XGB-37 | 59 | 48.850 | 13.486 | 1.221 | 3.622 | 5 | no | 20.479 | 39.834 |
| dulce | mensual | 10 | GC3 | 59 | 56.721 | 53.633 | 0.091 | 1.058 | 9 | no | 27.520 | 48.619 |
| dulce | mensual | 10 | GE | 59 | 56.546 | 67.879 | -0.333 | 0.833 | 8 | no | 27.762 | 48.281 |
| dulce | mensual | 15 | Naive | 53 | 85.289 | 18.719 | 10.018 | 4.556 | 10 | no | 52.867 | 80.466 |
| dulce | mensual | 15 | Seasonal Naive | 53 | 23.568 | 31.586 | -3.818 | 0.746 | 3 | no | 0.909 | 8.310 |
| dulce | mensual | 15 | Chronos | 53 | 33.506 | 10.470 | 8.720 | 3.200 | 4 | no | 7.807 | 21.397 |
| dulce | mensual | 15 | SARIMA | 53 | 18.829 | 15.257 | 2.263 | 1.234 | 1 | sí | 0.000 | 0.000 |
| dulce | mensual | 15 | SARIMA-sel | 53 | 20.823 | 19.157 | 0.942 | 1.087 | 2 | sí | -1.262 | 5.138 |
| dulce | mensual | 15 | Ridge | 53 | 52.409 | 58.071 | -1.245 | 0.903 | 7 | no | 22.833 | 44.833 |
| dulce | mensual | 15 | ElasticNet | 53 | 49.449 | 56.295 | -1.589 | 0.878 | 6 | no | 19.896 | 41.769 |
| dulce | mensual | 15 | XGB-37 | 53 | 47.366 | 55.032 | -1.853 | 0.861 | 5 | no | 18.417 | 38.751 |
| dulce | mensual | 15 | GC3 | 53 | 53.284 | 82.303 | -5.974 | 0.647 | 8 | no | 24.022 | 45.259 |
| dulce | mensual | 15 | GE | 53 | 53.383 | 82.108 | -5.907 | 0.650 | 9 | no | 24.494 | 45.039 |
| dulce | mensual | 20 | Naive | 51 | 87.902 | 18.702 | 13.390 | 4.700 | 10 | no | 54.794 | 82.957 |
| dulce | mensual | 20 | Seasonal Naive | 51 | 24.277 | 25.782 | -0.921 | 0.942 | 3 | no | 1.278 | 8.690 |
| dulce | mensual | 20 | Chronos | 51 | 34.296 | 11.113 | 11.284 | 3.086 | 4 | no | 8.083 | 22.045 |
| dulce | mensual | 20 | SARIMA | 51 | 19.116 | 14.424 | 3.822 | 1.325 | 1 | sí | 0.000 | 0.000 |
| dulce | mensual | 20 | SARIMA-sel | 51 | 20.135 | 23.426 | -2.393 | 0.860 | 2 | sí | -1.886 | 3.834 |
| dulce | mensual | 20 | Ridge | 51 | 53.927 | 48.210 | 1.616 | 1.119 | 7 | no | 23.610 | 46.179 |
| dulce | mensual | 20 | ElasticNet | 51 | 50.878 | 46.676 | 1.255 | 1.090 | 6 | no | 20.666 | 43.116 |
| dulce | mensual | 20 | XGB-37 | 51 | 48.120 | 49.057 | -0.291 | 0.981 | 5 | no | 18.463 | 39.450 |
| dulce | mensual | 20 | GC3 | 51 | 54.712 | 67.758 | -3.453 | 0.807 | 9 | no | 24.812 | 46.268 |
| dulce | mensual | 20 | GE | 51 | 54.560 | 69.058 | -3.833 | 0.790 | 8 | no | 25.019 | 45.981 |
| dulce | mensual | 25 | Naive | 44 | 96.405 | 25.596 | 24.357 | 3.766 | 10 | no | 62.048 | 91.321 |
| dulce | mensual | 25 | Seasonal Naive | 44 | 25.516 | 21.717 | 4.135 | 1.175 | 3 | no | 1.779 | 9.399 |
| dulce | mensual | 25 | Chronos | 44 | 35.409 | 18.195 | 14.895 | 1.946 | 4 | no | 7.822 | 23.195 |
| dulce | mensual | 25 | SARIMA | 44 | 19.786 | 14.632 | 7.465 | 1.352 | 1 | sí | 0.000 | 0.000 |
| dulce | mensual | 25 | SARIMA-sel | 44 | 21.114 | 19.294 | 2.352 | 1.094 | 2 | sí | -2.065 | 4.544 |
| dulce | mensual | 25 | Ridge | 44 | 56.747 | 42.958 | 6.929 | 1.321 | 9 | no | 24.812 | 49.680 |
| dulce | mensual | 25 | ElasticNet | 44 | 53.196 | 42.142 | 5.866 | 1.262 | 7 | no | 21.333 | 46.057 |
| dulce | mensual | 25 | XGB-37 | 44 | 48.842 | 46.663 | 1.204 | 1.047 | 5 | no | 17.916 | 40.417 |
| dulce | mensual | 25 | GC3 | 44 | 53.958 | 64.125 | -4.784 | 0.841 | 8 | no | 22.962 | 45.573 |
| dulce | mensual | 25 | GE | 44 | 53.102 | 66.725 | -6.403 | 0.796 | 6 | no | 22.368 | 44.413 |
| dulce | mensual | 30 | Naive | 42 | 98.612 | 28.313 | 27.205 | 3.483 | 10 | no | 66.073 | 94.918 |
| dulce | mensual | 30 | Seasonal Naive | 42 | 25.077 | 23.165 | 2.341 | 1.083 | 3 | no | 2.975 | 10.412 |
| dulce | mensual | 30 | Chronos | 42 | 35.811 | 19.169 | 16.200 | 1.868 | 4 | no | 10.401 | 24.754 |
| dulce | mensual | 30 | SARIMA | 42 | 18.181 | 18.951 | -1.255 | 0.959 | 1 | sí | 0.000 | 0.000 |
| dulce | mensual | 30 | SARIMA-sel | 42 | 19.635 | 22.948 | -4.819 | 0.856 | 2 | sí | -2.081 | 4.709 |
| dulce | mensual | 30 | Ridge | 42 | 58.187 | 41.129 | 9.643 | 1.415 | 9 | no | 28.197 | 52.568 |
| dulce | mensual | 30 | ElasticNet | 42 | 54.710 | 39.836 | 8.880 | 1.373 | 8 | no | 24.871 | 48.933 |
| dulce | mensual | 30 | XGB-37 | 42 | 50.330 | 43.431 | 4.289 | 1.159 | 5 | no | 21.418 | 43.499 |
| dulce | mensual | 30 | GC3 | 42 | 54.322 | 62.146 | -4.142 | 0.874 | 7 | no | 25.182 | 47.188 |
| dulce | mensual | 30 | GE | 42 | 53.285 | 64.784 | -6.080 | 0.823 | 6 | no | 24.372 | 46.010 |
| dulce | mensual | 35 | Naive | 38 | 102.202 | 34.894 | 31.836 | 2.929 | 10 | no | 68.982 | 99.581 |
| dulce | mensual | 35 | Seasonal Naive | 38 | 23.855 | 25.622 | -2.643 | 0.931 | 3 | no | 1.686 | 9.658 |
| dulce | mensual | 35 | Chronos | 38 | 37.083 | 19.999 | 20.326 | 1.854 | 4 | no | 11.348 | 26.873 |
| dulce | mensual | 35 | SARIMA | 38 | 17.965 | 19.185 | -2.430 | 0.936 | 1 | sí | 0.000 | 0.000 |
| dulce | mensual | 35 | SARIMA-sel | 38 | 20.262 | 21.263 | -1.780 | 0.953 | 2 | sí | -1.095 | 5.250 |
| dulce | mensual | 35 | Ridge | 38 | 56.679 | 46.835 | 6.801 | 1.210 | 9 | no | 26.231 | 52.381 |
| dulce | mensual | 35 | ElasticNet | 38 | 53.018 | 45.464 | 5.512 | 1.166 | 8 | no | 22.557 | 48.584 |
| dulce | mensual | 35 | XGB-37 | 38 | 47.390 | 49.764 | -1.804 | 0.952 | 5 | no | 18.613 | 40.942 |
| dulce | mensual | 35 | GC3 | 38 | 48.944 | 70.012 | -13.632 | 0.699 | 7 | no | 21.005 | 41.403 |
| dulce | mensual | 35 | GE | 38 | 47.668 | 72.395 | -15.981 | 0.658 | 6 | no | 19.804 | 40.140 |
| dulce | mensual | 40 | Naive | 34 | 108.772 | 36.657 | 40.311 | 2.967 | 10 | no | 75.721 | 106.336 |
| dulce | mensual | 40 | Seasonal Naive | 34 | 24.572 | 24.412 | 0.283 | 1.007 | 3 | no | 2.459 | 11.107 |
| dulce | mensual | 40 | Chronos | 34 | 39.046 | 20.060 | 26.696 | 1.946 | 4 | no | 13.043 | 29.488 |
| dulce | mensual | 40 | SARIMA | 34 | 17.618 | 19.451 | -4.315 | 0.906 | 1 | sí | 0.000 | 0.000 |
| dulce | mensual | 40 | SARIMA-sel | 34 | 19.831 | 21.672 | -3.867 | 0.915 | 2 | sí | -1.204 | 4.628 |
| dulce | mensual | 40 | Ridge | 34 | 58.302 | 46.227 | 9.860 | 1.261 | 9 | no | 27.543 | 54.897 |
| dulce | mensual | 40 | ElasticNet | 34 | 54.616 | 44.536 | 8.693 | 1.226 | 8 | no | 23.871 | 51.215 |
| dulce | mensual | 40 | XGB-37 | 34 | 49.570 | 46.549 | 2.713 | 1.065 | 5 | no | 20.233 | 44.000 |
| dulce | mensual | 40 | GC3 | 34 | 51.762 | 63.087 | -8.660 | 0.820 | 7 | no | 23.616 | 45.124 |
| dulce | mensual | 40 | GE | 34 | 50.060 | 65.463 | -11.765 | 0.765 | 6 | no | 22.042 | 43.416 |
| dulce | mensual | 45 | Naive | 29 | 114.916 | 42.541 | 48.237 | 2.701 | 10 | no | 84.632 | 114.647 |
| dulce | mensual | 45 | Seasonal Naive | 29 | 20.502 | 28.246 | -16.330 | 0.726 | 3 | no | 0.484 | 9.505 |
| dulce | mensual | 45 | Chronos | 29 | 38.544 | 23.592 | 25.065 | 1.634 | 4 | no | 14.136 | 32.171 |
| dulce | mensual | 45 | SARIMA | 29 | 15.328 | 21.297 | -16.749 | 0.720 | 1 | sí | 0.000 | 0.000 |
| dulce | mensual | 45 | SARIMA-sel | 29 | 18.059 | 23.032 | -12.455 | 0.784 | 2 | sí | -1.294 | 5.493 |
| dulce | mensual | 45 | Ridge | 29 | 58.399 | 48.084 | 10.043 | 1.215 | 9 | no | 28.396 | 59.021 |
| dulce | mensual | 45 | ElasticNet | 29 | 54.745 | 46.041 | 8.950 | 1.189 | 8 | no | 24.549 | 55.286 |
| dulce | mensual | 45 | XGB-37 | 29 | 47.249 | 49.207 | -2.096 | 0.960 | 6 | no | 18.503 | 45.542 |
| dulce | mensual | 45 | GC3 | 29 | 48.430 | 64.377 | -14.539 | 0.752 | 7 | no | 21.032 | 45.756 |
| dulce | mensual | 45 | GE | 29 | 47.121 | 65.728 | -16.945 | 0.717 | 5 | no | 20.033 | 44.437 |
| dulce | mensual | 50 | Naive | 28 | 117.017 | 42.965 | 50.946 | 2.724 | 10 | no | 87.556 | 117.346 |
| dulce | mensual | 50 | Seasonal Naive | 28 | 20.366 | 28.123 | -16.885 | 0.724 | 3 | no | 0.912 | 10.266 |
| dulce | mensual | 50 | Chronos | 28 | 39.460 | 23.258 | 28.038 | 1.697 | 4 | no | 15.735 | 33.548 |
| dulce | mensual | 50 | SARIMA | 28 | 14.631 | 21.721 | -20.538 | 0.674 | 1 | sí | 0.000 | 0.000 |
| dulce | mensual | 50 | SARIMA-sel | 28 | 17.553 | 23.320 | -14.910 | 0.753 | 2 | sí | -1.168 | 5.791 |
| dulce | mensual | 50 | Ridge | 28 | 57.746 | 48.978 | 8.811 | 1.179 | 9 | no | 27.913 | 59.458 |
| dulce | mensual | 50 | ElasticNet | 28 | 54.063 | 46.910 | 7.593 | 1.153 | 8 | no | 24.116 | 55.808 |
| dulce | mensual | 50 | XGB-37 | 28 | 47.689 | 48.761 | -1.185 | 0.978 | 5 | no | 19.724 | 46.818 |
| dulce | mensual | 50 | GC3 | 28 | 49.178 | 63.224 | -13.219 | 0.778 | 7 | no | 22.252 | 47.593 |
| dulce | mensual | 50 | GE | 28 | 47.768 | 64.580 | -15.804 | 0.740 | 6 | no | 20.958 | 46.084 |
| dulce | mensual | 55 | Naive | 25 | 122.603 | 45.322 | 58.152 | 2.705 | 10 | no | 95.213 | 123.670 |
| dulce | mensual | 55 | Seasonal Naive | 25 | 21.593 | 26.581 | -11.875 | 0.812 | 3 | no | 4.450 | 12.032 |
| dulce | mensual | 55 | Chronos | 25 | 41.504 | 23.187 | 34.670 | 1.790 | 4 | no | 19.556 | 36.799 |
| dulce | mensual | 55 | SARIMA | 25 | 13.256 | 22.095 | -28.003 | 0.600 | 1 | sí | 0.000 | 0.000 |
| dulce | mensual | 55 | SARIMA-sel | 25 | 17.059 | 23.178 | -17.303 | 0.736 | 2 | sí | -0.808 | 6.905 |
| dulce | mensual | 55 | Ridge | 25 | 58.153 | 49.439 | 9.578 | 1.176 | 9 | no | 31.834 | 59.207 |
| dulce | mensual | 55 | ElasticNet | 25 | 54.079 | 47.512 | 7.624 | 1.138 | 8 | no | 27.575 | 55.395 |
| dulce | mensual | 55 | XGB-37 | 25 | 51.263 | 46.116 | 6.221 | 1.112 | 7 | no | 25.037 | 51.199 |
| dulce | mensual | 55 | GC3 | 25 | 50.938 | 60.763 | -10.113 | 0.838 | 6 | no | 26.126 | 50.114 |
| dulce | mensual | 55 | GE | 25 | 49.229 | 62.096 | -13.229 | 0.793 | 5 | no | 24.414 | 48.934 |
| dulce | mensual | 60 | Naive | 23 | 125.066 | 47.968 | 61.330 | 2.607 | 10 | no | 96.304 | 125.854 |
| dulce | mensual | 60 | Seasonal Naive | 23 | 21.908 | 26.116 | -10.591 | 0.839 | 3 | no | 3.803 | 11.984 |
| dulce | mensual | 60 | Chronos | 23 | 41.940 | 23.906 | 36.084 | 1.754 | 4 | no | 19.256 | 36.554 |
| dulce | mensual | 60 | SARIMA | 23 | 13.893 | 21.221 | -24.545 | 0.655 | 1 | sí | 0.000 | 0.000 |
| dulce | mensual | 60 | SARIMA-sel | 23 | 16.184 | 23.392 | -21.546 | 0.692 | 2 | sí | -2.442 | 5.435 |
| dulce | mensual | 60 | Ridge | 23 | 56.904 | 50.687 | 7.224 | 1.123 | 9 | no | 28.704 | 58.506 |
| dulce | mensual | 60 | ElasticNet | 23 | 54.053 | 47.882 | 7.573 | 1.129 | 8 | no | 25.706 | 56.059 |
| dulce | mensual | 60 | XGB-37 | 23 | 53.115 | 45.243 | 10.058 | 1.174 | 6 | no | 24.957 | 53.913 |
| dulce | mensual | 60 | GC3 | 23 | 53.247 | 58.797 | -6.039 | 0.906 | 7 | no | 26.634 | 52.827 |
| dulce | mensual | 60 | GE | 23 | 50.460 | 60.635 | -11.059 | 0.832 | 5 | no | 23.855 | 50.344 |
| dulce | mensual | 65 | Naive | 22 | 124.718 | 50.199 | 60.880 | 2.484 | 10 | no | 95.169 | 125.825 |
| dulce | mensual | 65 | Seasonal Naive | 22 | 22.586 | 25.613 | -7.823 | 0.882 | 3 | no | 3.895 | 12.379 |
| dulce | mensual | 65 | Chronos | 22 | 41.521 | 24.623 | 34.726 | 1.686 | 4 | no | 18.318 | 35.840 |
| dulce | mensual | 65 | SARIMA | 22 | 14.374 | 20.750 | -21.930 | 0.693 | 1 | sí | 0.000 | 0.000 |
| dulce | mensual | 65 | SARIMA-sel | 22 | 16.770 | 22.863 | -18.707 | 0.733 | 2 | sí | -2.563 | 5.692 |
| dulce | mensual | 65 | Ridge | 22 | 58.918 | 49.684 | 11.019 | 1.186 | 9 | no | 29.959 | 60.869 |
| dulce | mensual | 65 | ElasticNet | 22 | 55.978 | 46.930 | 11.404 | 1.193 | 8 | no | 26.663 | 58.190 |
| dulce | mensual | 65 | XGB-37 | 22 | 53.176 | 45.415 | 10.185 | 1.171 | 6 | no | 24.055 | 54.131 |
| dulce | mensual | 65 | GC3 | 22 | 55.042 | 57.611 | -2.871 | 0.955 | 7 | no | 27.441 | 54.752 |
| dulce | mensual | 65 | GE | 22 | 52.011 | 59.469 | -8.326 | 0.875 | 5 | no | 24.391 | 51.961 |
| dulce | mensual | 70 | Naive | 17 | 125.025 | 58.742 | 61.276 | 2.128 | 10 | no | 95.841 | 127.399 |
| dulce | mensual | 70 | Seasonal Naive | 17 | 22.282 | 25.381 | -9.065 | 0.878 | 3 | no | 4.717 | 12.000 |
| dulce | mensual | 70 | Chronos | 17 | 45.629 | 24.963 | 48.057 | 1.828 | 4 | no | 22.607 | 40.477 |
| dulce | mensual | 70 | SARIMA | 17 | 13.757 | 20.252 | -25.282 | 0.679 | 1 | sí | 0.000 | 0.000 |
| dulce | mensual | 70 | SARIMA-sel | 17 | 18.695 | 21.393 | -9.374 | 0.874 | 2 | no | 3.847 | 6.189 |
| dulce | mensual | 70 | Ridge | 17 | 67.509 | 47.361 | 27.207 | 1.425 | 9 | no | 38.748 | 69.733 |
| dulce | mensual | 70 | ElasticNet | 17 | 64.650 | 44.554 | 28.662 | 1.451 | 8 | no | 35.418 | 67.489 |
| dulce | mensual | 70 | XGB-37 | 17 | 62.500 | 42.631 | 29.506 | 1.466 | 7 | no | 34.499 | 63.752 |
| dulce | mensual | 70 | GC3 | 17 | 56.618 | 56.689 | -0.090 | 0.999 | 6 | no | 29.795 | 56.508 |
| dulce | mensual | 70 | GE | 17 | 54.071 | 57.787 | -4.694 | 0.936 | 5 | no | 25.639 | 55.698 |
| dulce | mensual | 75 | Naive | 15 | 131.622 | 59.489 | 69.786 | 2.213 | 10 | no | 103.014 | 133.375 |
| dulce | mensual | 75 | Seasonal Naive | 15 | 24.503 | 24.503 | -0.001 | 1.000 | 3 | no | 7.208 | 13.529 |
| dulce | mensual | 75 | Chronos | 15 | 48.199 | 25.025 | 56.394 | 1.926 | 4 | no | 24.855 | 42.693 |
| dulce | mensual | 75 | SARIMA | 15 | 13.978 | 19.890 | -24.083 | 0.703 | 1 | sí | 0.000 | 0.000 |
| dulce | mensual | 75 | SARIMA-sel | 15 | 19.691 | 20.941 | -4.547 | 0.940 | 2 | no | 4.475 | 7.129 |
| dulce | mensual | 75 | Ridge | 15 | 69.694 | 47.528 | 31.325 | 1.466 | 9 | no | 38.914 | 74.342 |
| dulce | mensual | 75 | ElasticNet | 15 | 67.230 | 44.587 | 33.796 | 1.508 | 8 | no | 35.768 | 72.471 |
| dulce | mensual | 75 | XGB-37 | 15 | 65.849 | 42.398 | 36.445 | 1.553 | 7 | no | 37.127 | 66.769 |
| dulce | mensual | 75 | GC3 | 15 | 60.748 | 55.310 | 7.197 | 1.098 | 6 | no | 32.452 | 61.866 |
| dulce | mensual | 75 | GE | 15 | 57.883 | 56.352 | 2.025 | 1.027 | 5 | no | 27.912 | 61.091 |
| dulce | mensual | 80 | Naive | 12 | 130.178 | 64.358 | 67.924 | 2.023 | 10 | no | 100.137 | 136.152 |
| dulce | mensual | 80 | Seasonal Naive | 12 | 25.081 | 24.359 | 2.358 | 1.030 | 3 | no | 10.120 | 14.500 |
| dulce | mensual | 80 | Chronos | 12 | 50.514 | 25.895 | 63.906 | 1.951 | 4 | no | 30.545 | 45.339 |
| dulce | mensual | 80 | SARIMA | 12 | 12.606 | 19.864 | -31.536 | 0.635 | 1 | sí | 0.000 | 0.000 |
| dulce | mensual | 80 | SARIMA-sel | 12 | 20.119 | 20.756 | -2.471 | 0.969 | 2 | no | 6.145 | 9.246 |
| dulce | mensual | 80 | Ridge | 12 | 72.645 | 48.176 | 36.885 | 1.508 | 9 | no | 41.237 | 80.826 |
| dulce | mensual | 80 | ElasticNet | 12 | 71.213 | 45.007 | 41.722 | 1.582 | 8 | no | 40.887 | 78.823 |
| dulce | mensual | 80 | XGB-37 | 12 | 68.933 | 43.092 | 42.835 | 1.600 | 7 | no | 42.347 | 70.096 |
| dulce | mensual | 80 | GC3 | 12 | 65.540 | 54.452 | 15.653 | 1.204 | 6 | no | 36.936 | 70.333 |
| dulce | mensual | 80 | GE | 12 | 62.020 | 55.413 | 9.316 | 1.119 | 5 | no | 31.824 | 69.230 |
| dulce | mensual | 85 | Naive | 9 | 129.085 | 68.423 | 66.514 | 1.887 | 10 | no | 94.758 | 137.557 |
| dulce | mensual | 85 | Seasonal Naive | 9 | 25.456 | 24.335 | 3.887 | 1.046 | 3 | no | 9.149 | 12.943 |
| dulce | mensual | 85 | Chronos | 9 | 47.390 | 27.894 | 53.770 | 1.699 | 4 | no | 26.549 | 40.043 |
| dulce | mensual | 85 | SARIMA | 9 | 14.410 | 19.118 | -21.738 | 0.754 | 1 | sí | 0.000 | 0.000 |
| dulce | mensual | 85 | SARIMA-sel | 9 | 24.267 | 19.987 | 17.637 | 1.214 | 2 | no | 8.036 | 12.262 |
| dulce | mensual | 85 | Ridge | 9 | 67.536 | 50.517 | 27.259 | 1.337 | 8 | no | 33.288 | 73.037 |
| dulce | mensual | 85 | ElasticNet | 9 | 66.465 | 47.386 | 32.274 | 1.403 | 7 | no | 30.419 | 72.652 |
| dulce | mensual | 85 | XGB-37 | 9 | 69.969 | 44.430 | 44.983 | 1.575 | 9 | no | 40.586 | 70.534 |
| dulce | mensual | 85 | GC3 | 9 | 57.512 | 56.521 | 1.487 | 1.018 | 6 | no | 31.333 | 54.872 |
| dulce | mensual | 85 | GE | 9 | 55.943 | 56.874 | -1.396 | 0.984 | 5 | no | 28.293 | 58.610 |
| dulce | mensual | 90 | Naive | 5 | 110.728 | 74.504 | 42.833 | 1.486 | 10 | no | 78.443 | 127.149 |
| dulce | mensual | 90 | Seasonal Naive | 5 | 21.412 | 24.784 | -12.615 | 0.864 | 2 | no | 10.305 | 11.075 |
| dulce | mensual | 90 | Chronos | 5 | 38.023 | 30.164 | 23.375 | 1.261 | 4 | no | 17.072 | 39.886 |
| dulce | mensual | 90 | SARIMA | 5 | 10.715 | 19.112 | -41.805 | 0.561 | 1 | sí | 0.000 | 0.000 |
| dulce | mensual | 90 | SARIMA-sel | 5 | 29.101 | 19.858 | 41.071 | 1.465 | 3 | no | 15.109 | 22.872 |
| dulce | mensual | 90 | Ridge | 5 | 46.586 | 53.659 | -12.217 | 0.868 | 8 | no | 24.414 | 47.199 |
| dulce | mensual | 90 | ElasticNet | 5 | 45.876 | 50.645 | -8.701 | 0.906 | 7 | no | 27.543 | 44.784 |
| dulce | mensual | 90 | XGB-37 | 5 | 56.950 | 47.471 | 18.005 | 1.200 | 9 | no | 27.387 | 65.039 |
| dulce | mensual | 90 | GC3 | 5 | 39.424 | 58.237 | -30.432 | 0.677 | 5 | no | 18.802 | 39.993 |
| dulce | mensual | 90 | GE | 5 | 39.559 | 58.296 | -30.273 | 0.679 | 6 | no | 15.085 | 51.132 |
| dulce | mensual | 95 | Naive | 1 | 85.650 | 77.385 | 10.484 | 1.107 | 10 | no | 80.386 | 80.386 |
| dulce | mensual | 95 | Seasonal Naive | 1 | 16.280 | 24.642 | -33.559 | 0.661 | 3 | no | 11.016 | 11.016 |
| dulce | mensual | 95 | Chronos | 1 | 23.132 | 30.949 | -24.941 | 0.747 | 5 | no | 17.869 | 17.869 |
| dulce | mensual | 95 | SARIMA | 1 | 5.264 | 18.635 | -71.413 | 0.282 | 1 | sí | 0.000 | 0.000 |
| dulce | mensual | 95 | SARIMA-sel | 1 | 43.307 | 20.244 | 109.933 | 2.139 | 9 | no | 38.043 | 38.043 |
| dulce | mensual | 95 | Ridge | 1 | 43.092 | 53.239 | -18.801 | 0.809 | 8 | no | 37.829 | 37.829 |
| dulce | mensual | 95 | ElasticNet | 1 | 41.125 | 50.403 | -18.157 | 0.816 | 7 | no | 35.861 | 35.861 |
| dulce | mensual | 95 | XGB-37 | 1 | 11.794 | 48.879 | -75.561 | 0.241 | 2 | no | 6.531 | 6.531 |
| dulce | mensual | 95 | GC3 | 1 | 28.130 | 57.153 | -50.362 | 0.492 | 6 | no | 22.866 | 22.866 |
| dulce | mensual | 95 | GE | 1 | 21.818 | 57.326 | -61.543 | 0.381 | 4 | no | 16.555 | 16.555 |

### barrido_por_modelo.csv — Barrido interanual completo: modelo × percentil

`07_barrido_umbral/interanual/barrido_por_modelo.csv` — 380 filas × 13 columnas.

| cultivar | tipo | percentil | modelo | n_shock | MAE_shock | MAE_normal | Delta_s | razon_shock_normal | posicion | primero | dif_vs_mejor_lo | dif_vs_mejor_hi |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| sutil | interanual | 0 | Naive | 60 | 3,624.070 | — | 0.000 | — | 4 | no | 403.507 | 1,555.865 |
| sutil | interanual | 0 | Seasonal Naive | 60 | 6,074.886 | — | 0.000 | — | 8 | no | 2,444.779 | 4,367.800 |
| sutil | interanual | 0 | Chronos | 60 | 2,648.547 | — | 0.000 | — | 1 | sí | 0.000 | 0.000 |
| sutil | interanual | 0 | SARIMA | 60 | 3,360.787 | — | 0.000 | — | 3 | no | 143.018 | 1,264.060 |
| sutil | interanual | 0 | SARIMA-sel | 60 | 3,205.876 | — | 0.000 | — | 2 | sí | -82.699 | 1,193.595 |
| sutil | interanual | 0 | Ridge | 60 | 4,925.136 | — | 0.000 | — | 7 | no | 1,150.943 | 3,504.549 |
| sutil | interanual | 0 | ElasticNet | 60 | 4,871.911 | — | 0.000 | — | 5 | no | 1,164.437 | 3,356.463 |
| sutil | interanual | 0 | XGB-37 | 60 | 4,881.450 | — | 0.000 | — | 6 | no | 1,351.795 | 3,110.266 |
| sutil | interanual | 0 | GC3 | 60 | 6,361.305 | — | 0.000 | — | 9 | no | 2,517.657 | 4,919.015 |
| sutil | interanual | 0 | GE | 60 | 6,743.530 | — | 0.000 | — | 10 | no | 2,847.076 | 5,360.660 |
| sutil | interanual | 10 | Naive | 52 | 3,630.110 | 3,584.812 | 0.167 | 1.013 | 4 | no | 248.817 | 1,509.988 |
| sutil | interanual | 10 | Seasonal Naive | 52 | 6,925.327 | 547.016 | 13.999 | 12.660 | 9 | no | 3,262.098 | 5,073.805 |
| sutil | interanual | 10 | Chronos | 52 | 2,750.784 | 1,984.003 | 3.860 | 1.386 | 1 | sí | 0.000 | 0.000 |
| sutil | interanual | 10 | SARIMA | 52 | 3,516.257 | 2,350.234 | 4.626 | 1.496 | 3 | no | 119.038 | 1,384.283 |
| sutil | interanual | 10 | SARIMA-sel | 52 | 3,384.634 | 2,043.955 | 5.576 | 1.656 | 2 | sí | -85.792 | 1,341.880 |
| sutil | interanual | 10 | Ridge | 52 | 4,901.707 | 5,077.421 | -0.476 | 0.965 | 5 | no | 1,008.718 | 3,354.434 |
| sutil | interanual | 10 | ElasticNet | 52 | 4,948.863 | 4,371.727 | 1.579 | 1.132 | 6 | no | 1,096.424 | 3,344.254 |
| sutil | interanual | 10 | XGB-37 | 52 | 5,025.500 | 3,945.120 | 2.951 | 1.274 | 7 | no | 1,330.280 | 3,245.814 |
| sutil | interanual | 10 | GC3 | 52 | 6,821.227 | 3,371.810 | 7.230 | 2.023 | 8 | no | 2,806.331 | 5,354.684 |
| sutil | interanual | 10 | GE | 52 | 7,238.890 | 3,523.689 | 7.346 | 2.054 | 10 | no | 3,152.714 | 5,844.595 |
| sutil | interanual | 15 | Naive | 51 | 3,682.539 | 3,292.747 | 1.613 | 1.118 | 4 | no | 278.836 | 1,519.626 |
| sutil | interanual | 15 | Seasonal Naive | 51 | 7,045.707 | 573.565 | 15.981 | 12.284 | 9 | no | 3,331.190 | 5,175.672 |
| sutil | interanual | 15 | Chronos | 51 | 2,784.407 | 1,878.673 | 5.130 | 1.482 | 1 | sí | 0.000 | 0.000 |
| sutil | interanual | 15 | SARIMA | 51 | 3,562.168 | 2,219.631 | 5.992 | 1.605 | 3 | no | 135.351 | 1,411.272 |
| sutil | interanual | 15 | SARIMA-sel | 51 | 3,426.904 | 1,953.387 | 6.894 | 1.754 | 2 | sí | -79.914 | 1,368.221 |
| sutil | interanual | 15 | Ridge | 51 | 4,945.713 | 4,808.531 | 0.418 | 1.029 | 5 | no | 1,010.141 | 3,436.293 |
| sutil | interanual | 15 | ElasticNet | 51 | 5,005.068 | 4,117.358 | 2.733 | 1.216 | 6 | no | 1,101.884 | 3,428.690 |
| sutil | interanual | 15 | XGB-37 | 51 | 5,111.315 | 3,578.881 | 4.709 | 1.428 | 7 | no | 1,350.846 | 3,313.694 |
| sutil | interanual | 15 | GC3 | 51 | 6,924.244 | 3,171.313 | 8.849 | 2.183 | 8 | no | 2,844.555 | 5,456.246 |
| sutil | interanual | 15 | GE | 51 | 7,349.147 | 3,311.702 | 8.981 | 2.219 | 10 | no | 3,165.137 | 5,989.695 |
| sutil | interanual | 20 | Naive | 44 | 3,517.689 | 3,916.618 | -2.935 | 0.898 | 4 | no | 101.417 | 1,390.860 |
| sutil | interanual | 20 | Seasonal Naive | 44 | 7,798.888 | 1,333.880 | 28.379 | 5.847 | 10 | no | 4,029.019 | 5,972.738 |
| sutil | interanual | 20 | Chronos | 44 | 2,779.026 | 2,289.728 | 4.926 | 1.214 | 1 | sí | 0.000 | 0.000 |
| sutil | interanual | 20 | SARIMA | 44 | 3,454.401 | 3,103.349 | 2.785 | 1.113 | 3 | sí | -16.877 | 1,326.324 |
| sutil | interanual | 20 | SARIMA-sel | 44 | 3,381.860 | 2,721.921 | 5.489 | 1.242 | 2 | sí | -210.396 | 1,408.811 |
| sutil | interanual | 20 | Ridge | 44 | 5,034.543 | 4,624.266 | 2.221 | 1.089 | 6 | no | 957.917 | 3,700.332 |
| sutil | interanual | 20 | ElasticNet | 44 | 5,198.499 | 3,973.796 | 6.703 | 1.308 | 7 | no | 1,168.036 | 3,786.644 |
| sutil | interanual | 20 | XGB-37 | 44 | 4,926.659 | 4,757.124 | 0.926 | 1.036 | 5 | no | 1,133.268 | 3,236.282 |
| sutil | interanual | 20 | GC3 | 44 | 6,711.919 | 5,397.115 | 5.512 | 1.244 | 8 | no | 2,593.640 | 5,345.856 |
| sutil | interanual | 20 | GE | 44 | 6,765.647 | 6,682.710 | 0.328 | 1.012 | 9 | no | 2,636.609 | 5,406.004 |
| sutil | interanual | 25 | Naive | 42 | 3,537.034 | 3,827.155 | -2.402 | 0.924 | 4 | sí | -8.682 | 1,346.762 |
| sutil | interanual | 25 | Seasonal Naive | 42 | 8,037.723 | 1,494.932 | 32.311 | 5.377 | 10 | no | 4,148.499 | 6,166.791 |
| sutil | interanual | 25 | Chronos | 42 | 2,877.360 | 2,114.648 | 8.639 | 1.361 | 1 | sí | 0.000 | 0.000 |
| sutil | interanual | 25 | SARIMA | 42 | 3,486.418 | 3,067.650 | 3.738 | 1.137 | 3 | sí | -112.831 | 1,288.996 |
| sutil | interanual | 25 | SARIMA-sel | 42 | 3,400.807 | 2,751.039 | 6.080 | 1.236 | 2 | sí | -312.217 | 1,376.722 |
| sutil | interanual | 25 | Ridge | 42 | 5,259.478 | 4,145.003 | 6.788 | 1.269 | 6 | no | 1,018.426 | 3,888.523 |
| sutil | interanual | 25 | ElasticNet | 42 | 5,415.114 | 3,604.439 | 11.150 | 1.502 | 7 | no | 1,232.550 | 3,973.631 |
| sutil | interanual | 25 | XGB-37 | 42 | 4,964.457 | 4,687.765 | 1.700 | 1.059 | 5 | no | 1,024.895 | 3,188.256 |
| sutil | interanual | 25 | GC3 | 42 | 6,879.522 | 5,152.130 | 8.146 | 1.335 | 8 | no | 2,583.757 | 5,474.241 |
| sutil | interanual | 25 | GE | 42 | 7,001.313 | 6,142.036 | 3.823 | 1.140 | 9 | no | 2,705.569 | 5,595.634 |
| sutil | interanual | 30 | Naive | 38 | 3,325.685 | 4,139.463 | -8.233 | 0.803 | 2 | sí | -221.462 | 1,195.539 |
| sutil | interanual | 30 | Seasonal Naive | 38 | 8,435.470 | 1,997.513 | 38.858 | 4.223 | 10 | no | 4,525.152 | 6,664.581 |
| sutil | interanual | 30 | Chronos | 38 | 2,848.693 | 2,302.839 | 7.557 | 1.237 | 1 | sí | 0.000 | 0.000 |
| sutil | interanual | 30 | SARIMA | 38 | 3,549.115 | 3,035.493 | 5.604 | 1.169 | 4 | sí | -65.932 | 1,425.003 |
| sutil | interanual | 30 | SARIMA-sel | 38 | 3,464.782 | 2,758.676 | 8.076 | 1.256 | 3 | sí | -239.170 | 1,471.830 |
| sutil | interanual | 30 | Ridge | 38 | 5,675.951 | 3,628.273 | 15.245 | 1.564 | 6 | no | 1,360.585 | 4,404.486 |
| sutil | interanual | 30 | ElasticNet | 38 | 5,813.947 | 3,244.759 | 19.336 | 1.792 | 7 | no | 1,553.565 | 4,458.169 |
| sutil | interanual | 30 | XGB-37 | 38 | 4,978.996 | 4,712.961 | 1.998 | 1.056 | 5 | no | 1,034.056 | 3,240.615 |
| sutil | interanual | 30 | GC3 | 38 | 7,032.561 | 5,201.862 | 10.552 | 1.352 | 8 | no | 2,641.311 | 5,728.596 |
| sutil | interanual | 30 | GE | 38 | 7,114.669 | 6,102.472 | 5.504 | 1.166 | 9 | no | 2,749.224 | 5,778.011 |
| sutil | interanual | 35 | Naive | 34 | 3,289.398 | 4,061.718 | -9.235 | 0.810 | 2 | sí | -312.238 | 1,070.981 |
| sutil | interanual | 35 | Seasonal Naive | 34 | 8,893.243 | 2,389.342 | 46.394 | 3.722 | 10 | no | 4,880.294 | 7,066.298 |
| sutil | interanual | 35 | Chronos | 34 | 2,916.101 | 2,298.668 | 10.102 | 1.269 | 1 | sí | 0.000 | 0.000 |
| sutil | interanual | 35 | SARIMA | 34 | 3,702.321 | 2,914.166 | 10.162 | 1.270 | 4 | sí | -38.364 | 1,552.647 |
| sutil | interanual | 35 | SARIMA-sel | 34 | 3,650.827 | 2,624.017 | 13.879 | 1.391 | 3 | sí | -191.824 | 1,639.566 |
| sutil | interanual | 35 | Ridge | 34 | 5,973.111 | 3,554.707 | 21.278 | 1.680 | 6 | no | 1,462.408 | 4,807.033 |
| sutil | interanual | 35 | ElasticNet | 34 | 6,157.802 | 3,190.362 | 26.394 | 1.930 | 7 | no | 1,721.824 | 4,886.943 |
| sutil | interanual | 35 | XGB-37 | 34 | 5,175.579 | 4,496.819 | 6.025 | 1.151 | 5 | no | 1,105.711 | 3,466.160 |
| sutil | interanual | 35 | GC3 | 34 | 7,580.459 | 4,767.026 | 19.165 | 1.590 | 8 | no | 3,103.216 | 6,313.644 |
| sutil | interanual | 35 | GE | 34 | 7,634.223 | 5,578.778 | 13.208 | 1.368 | 9 | no | 3,184.109 | 6,318.612 |
| sutil | interanual | 40 | Naive | 33 | 3,215.354 | 4,123.612 | -11.278 | 0.780 | 2 | sí | -406.604 | 1,026.081 |
| sutil | interanual | 40 | Seasonal Naive | 33 | 9,012.171 | 2,484.870 | 48.351 | 3.627 | 10 | no | 5,034.370 | 7,093.675 |
| sutil | interanual | 40 | Chronos | 33 | 2,922.461 | 2,313.763 | 10.342 | 1.263 | 1 | sí | 0.000 | 0.000 |
| sutil | interanual | 40 | SARIMA | 33 | 3,809.177 | 2,812.755 | 13.342 | 1.354 | 4 | no | 49.161 | 1,644.664 |
| sutil | interanual | 40 | SARIMA-sel | 33 | 3,648.299 | 2,665.137 | 13.800 | 1.369 | 3 | sí | -219.439 | 1,658.066 |
| sutil | interanual | 40 | Ridge | 33 | 5,966.584 | 3,652.255 | 21.146 | 1.634 | 6 | no | 1,383.374 | 4,886.037 |
| sutil | interanual | 40 | ElasticNet | 33 | 6,128.378 | 3,336.230 | 25.790 | 1.837 | 7 | no | 1,623.353 | 4,922.213 |
| sutil | interanual | 40 | XGB-37 | 33 | 5,177.235 | 4,519.935 | 6.059 | 1.145 | 5 | no | 1,062.164 | 3,456.601 |
| sutil | interanual | 40 | GC3 | 33 | 7,423.911 | 5,062.563 | 16.704 | 1.466 | 8 | no | 2,873.472 | 6,174.963 |
| sutil | interanual | 40 | GE | 33 | 7,473.468 | 5,851.383 | 10.824 | 1.277 | 9 | no | 2,954.591 | 6,196.413 |
| sutil | interanual | 45 | Naive | 27 | 3,739.405 | 3,529.706 | 3.182 | 1.059 | 2 | sí | -333.451 | 1,388.969 |
| sutil | interanual | 45 | Seasonal Naive | 27 | 9,881.423 | 2,960.446 | 62.660 | 3.338 | 10 | no | 5,421.514 | 7,846.867 |
| sutil | interanual | 45 | Chronos | 27 | 3,224.453 | 2,177.350 | 21.744 | 1.481 | 1 | sí | 0.000 | 0.000 |
| sutil | interanual | 45 | SARIMA | 27 | 3,950.295 | 2,878.463 | 17.541 | 1.372 | 3 | sí | -257.887 | 1,658.108 |
| sutil | interanual | 45 | SARIMA-sel | 27 | 4,074.758 | 2,494.973 | 27.103 | 1.633 | 4 | sí | -279.661 | 1,972.636 |
| sutil | interanual | 45 | Ridge | 27 | 5,951.363 | 4,085.496 | 20.837 | 1.457 | 6 | no | 1,044.967 | 4,612.310 |
| sutil | interanual | 45 | ElasticNet | 27 | 6,212.692 | 3,774.909 | 27.521 | 1.646 | 7 | no | 1,302.720 | 4,817.218 |
| sutil | interanual | 45 | XGB-37 | 27 | 5,269.854 | 4,563.665 | 7.957 | 1.155 | 5 | no | 639.573 | 3,476.390 |
| sutil | interanual | 45 | GC3 | 27 | 7,861.178 | 5,134.135 | 23.578 | 1.531 | 9 | no | 2,657.169 | 6,632.018 |
| sutil | interanual | 45 | GE | 27 | 7,857.553 | 5,832.057 | 16.520 | 1.347 | 8 | no | 2,702.149 | 6,560.077 |
| sutil | interanual | 50 | Naive | 25 | 3,679.645 | 3,584.374 | 1.533 | 1.027 | 2 | sí | -422.379 | 1,435.119 |
| sutil | interanual | 50 | Seasonal Naive | 25 | 10,057.020 | 3,230.504 | 65.551 | 3.113 | 10 | no | 5,783.795 | 7,941.902 |
| sutil | interanual | 50 | Chronos | 25 | 3,191.476 | 2,260.740 | 20.499 | 1.412 | 1 | sí | 0.000 | 0.000 |
| sutil | interanual | 50 | SARIMA | 25 | 3,941.818 | 2,945.765 | 17.289 | 1.338 | 3 | sí | -245.818 | 1,670.329 |
| sutil | interanual | 50 | SARIMA-sel | 25 | 4,063.475 | 2,593.306 | 26.751 | 1.567 | 4 | sí | -242.861 | 2,008.755 |
| sutil | interanual | 50 | Ridge | 25 | 5,834.370 | 4,275.683 | 18.461 | 1.365 | 6 | no | 951.661 | 4,602.452 |
| sutil | interanual | 50 | ElasticNet | 25 | 6,073.024 | 4,013.974 | 24.654 | 1.513 | 7 | no | 1,182.942 | 4,789.494 |
| sutil | interanual | 50 | XGB-37 | 25 | 5,185.590 | 4,664.206 | 6.231 | 1.112 | 5 | no | 485.977 | 3,537.278 |
| sutil | interanual | 50 | GC3 | 25 | 7,649.418 | 5,441.224 | 20.249 | 1.406 | 9 | no | 2,436.335 | 6,537.508 |
| sutil | interanual | 50 | GE | 25 | 7,639.401 | 6,103.622 | 13.285 | 1.252 | 8 | no | 2,446.280 | 6,483.851 |
| sutil | interanual | 55 | Naive | 21 | 3,913.288 | 3,468.338 | 7.980 | 1.128 | 2 | sí | -253.201 | 1,746.091 |
| sutil | interanual | 55 | Seasonal Naive | 21 | 10,689.995 | 3,589.827 | 75.970 | 2.978 | 10 | no | 6,270.067 | 8,685.397 |
| sutil | interanual | 55 | Chronos | 21 | 3,212.862 | 2,344.684 | 21.307 | 1.370 | 1 | sí | 0.000 | 0.000 |
| sutil | interanual | 55 | SARIMA | 21 | 3,995.604 | 3,018.963 | 18.889 | 1.324 | 3 | sí | -368.314 | 1,860.223 |
| sutil | interanual | 55 | SARIMA-sel | 21 | 4,468.341 | 2,526.088 | 39.380 | 1.769 | 4 | sí | -40.167 | 2,563.114 |
| sutil | interanual | 55 | Ridge | 21 | 6,156.458 | 4,262.116 | 25.001 | 1.444 | 6 | no | 1,035.900 | 5,178.570 |
| sutil | interanual | 55 | ElasticNet | 21 | 6,423.989 | 4,036.177 | 31.858 | 1.592 | 7 | no | 1,298.637 | 5,417.193 |
| sutil | interanual | 55 | XGB-37 | 21 | 4,964.535 | 4,836.712 | 1.702 | 1.026 | 5 | no | 312.753 | 3,295.491 |
| sutil | interanual | 55 | GC3 | 21 | 7,742.114 | 5,617.792 | 21.706 | 1.378 | 8 | no | 2,301.742 | 6,846.461 |
| sutil | interanual | 55 | GE | 21 | 7,836.914 | 6,154.785 | 16.214 | 1.273 | 9 | no | 2,499.001 | 6,851.535 |
| sutil | interanual | 60 | Naive | 18 | 3,373.593 | 3,731.418 | -6.911 | 0.904 | 2 | sí | -433.525 | 1,801.064 |
| sutil | interanual | 60 | Seasonal Naive | 18 | 10,963.068 | 3,979.951 | 80.465 | 2.755 | 10 | no | 6,897.263 | 9,612.485 |
| sutil | interanual | 60 | Chronos | 18 | 2,710.426 | 2,622.027 | 2.336 | 1.034 | 1 | sí | 0.000 | 0.000 |
| sutil | interanual | 60 | SARIMA | 18 | 3,665.977 | 3,229.992 | 9.081 | 1.135 | 3 | sí | -396.136 | 2,203.522 |
| sutil | interanual | 60 | SARIMA-sel | 18 | 4,227.914 | 2,767.860 | 31.880 | 1.528 | 4 | no | 20.906 | 2,969.481 |
| sutil | interanual | 60 | Ridge | 18 | 5,893.281 | 4,510.217 | 19.657 | 1.307 | 6 | no | 972.370 | 5,711.894 |
| sutil | interanual | 60 | ElasticNet | 18 | 6,208.986 | 4,298.879 | 27.445 | 1.444 | 7 | no | 1,268.109 | 5,976.444 |
| sutil | interanual | 60 | XGB-37 | 18 | 5,011.340 | 4,825.783 | 2.661 | 1.038 | 5 | no | 788.490 | 3,958.101 |
| sutil | interanual | 60 | GC3 | 18 | 7,969.970 | 5,671.876 | 25.288 | 1.405 | 8 | no | 2,864.621 | 7,828.936 |
| sutil | interanual | 60 | GE | 18 | 8,171.084 | 6,131.721 | 21.169 | 1.333 | 9 | no | 3,180.759 | 7,912.190 |
| sutil | interanual | 65 | Naive | 16 | 3,537.289 | 3,655.627 | -2.395 | 0.968 | 3 | sí | -233.524 | 1,824.034 |
| sutil | interanual | 65 | Seasonal Naive | 16 | 11,381.204 | 4,145.316 | 87.348 | 2.746 | 10 | no | 7,085.688 | 10,114.055 |
| sutil | interanual | 65 | Chronos | 16 | 2,764.580 | 2,606.353 | 4.381 | 1.061 | 1 | sí | 0.000 | 0.000 |
| sutil | interanual | 65 | SARIMA | 16 | 3,497.570 | 3,311.048 | 4.070 | 1.056 | 2 | sí | -568.423 | 1,910.509 |
| sutil | interanual | 65 | SARIMA-sel | 16 | 4,509.143 | 2,731.961 | 40.652 | 1.651 | 4 | no | 137.655 | 3,314.177 |
| sutil | interanual | 65 | Ridge | 16 | 6,049.647 | 4,516.223 | 22.832 | 1.340 | 6 | no | 862.596 | 6,140.126 |
| sutil | interanual | 65 | ElasticNet | 16 | 6,252.587 | 4,369.847 | 28.340 | 1.431 | 7 | no | 1,090.115 | 6,265.182 |
| sutil | interanual | 65 | XGB-37 | 16 | 5,289.831 | 4,732.947 | 8.366 | 1.118 | 5 | no | 962.355 | 4,269.472 |
| sutil | interanual | 65 | GC3 | 16 | 8,038.905 | 5,751.268 | 26.372 | 1.398 | 8 | no | 2,626.138 | 8,164.564 |
| sutil | interanual | 65 | GE | 16 | 8,185.040 | 6,219.344 | 21.376 | 1.316 | 9 | no | 2,903.799 | 8,173.901 |
| sutil | interanual | 70 | Naive | 13 | 2,726.424 | 3,872.356 | -24.769 | 0.704 | 2 | sí | -680.664 | 1,687.957 |
| sutil | interanual | 70 | Seasonal Naive | 13 | 11,855.416 | 4,476.016 | 95.155 | 2.649 | 10 | no | 7,789.216 | 11,350.185 |
| sutil | interanual | 70 | Chronos | 13 | 2,278.172 | 2,750.991 | -13.984 | 0.828 | 1 | sí | 0.000 | 0.000 |
| sutil | interanual | 70 | SARIMA | 13 | 3,408.527 | 3,347.583 | 1.420 | 1.018 | 3 | no | 6.300 | 2,228.124 |
| sutil | interanual | 70 | SARIMA-sel | 13 | 4,431.398 | 2,866.902 | 38.227 | 1.546 | 4 | no | 468.663 | 3,855.219 |
| sutil | interanual | 70 | Ridge | 13 | 4,878.250 | 4,938.104 | -0.952 | 0.988 | 6 | no | 871.906 | 4,479.750 |
| sutil | interanual | 70 | ElasticNet | 13 | 5,206.772 | 4,779.290 | 6.873 | 1.089 | 7 | no | 1,092.704 | 4,966.648 |
| sutil | interanual | 70 | XGB-37 | 13 | 4,855.529 | 4,888.619 | -0.531 | 0.993 | 5 | no | 647.142 | 4,707.959 |
| sutil | interanual | 70 | GC3 | 13 | 8,106.009 | 5,878.727 | 27.427 | 1.379 | 8 | no | 2,693.113 | 9,300.815 |
| sutil | interanual | 70 | GE | 13 | 8,419.464 | 6,279.974 | 24.852 | 1.341 | 9 | no | 3,127.244 | 9,439.776 |
| sutil | interanual | 75 | Naive | 10 | 3,171.846 | 3,714.515 | -12.478 | 0.854 | 2 | sí | -90.077 | 2,851.978 |
| sutil | interanual | 75 | Seasonal Naive | 10 | 12,508.067 | 4,788.250 | 105.898 | 2.612 | 10 | no | 8,351.592 | 12,904.867 |
| sutil | interanual | 75 | Chronos | 10 | 1,864.113 | 2,805.433 | -29.618 | 0.664 | 1 | sí | 0.000 | 0.000 |
| sutil | interanual | 75 | SARIMA | 10 | 3,232.720 | 3,386.401 | -3.811 | 0.955 | 3 | no | 399.107 | 2,223.819 |
| sutil | interanual | 75 | SARIMA-sel | 10 | 4,078.830 | 3,031.286 | 27.230 | 1.346 | 4 | no | 115.027 | 4,343.427 |
| sutil | interanual | 75 | Ridge | 10 | 4,946.068 | 4,920.950 | 0.425 | 1.005 | 6 | no | 1,092.543 | 5,265.942 |
| sutil | interanual | 75 | ElasticNet | 10 | 5,403.723 | 4,765.549 | 10.916 | 1.134 | 7 | no | 1,279.184 | 6,034.041 |
| sutil | interanual | 75 | XGB-37 | 10 | 4,816.485 | 4,894.443 | -1.331 | 0.984 | 5 | no | 446.460 | 5,673.369 |
| sutil | interanual | 75 | GC3 | 10 | 9,166.116 | 5,800.342 | 44.092 | 1.580 | 8 | no | 3,189.903 | 11,742.247 |
| sutil | interanual | 75 | GE | 10 | 9,796.027 | 6,133.031 | 45.266 | 1.597 | 9 | no | 3,968.769 | 12,152.721 |
| sutil | interanual | 80 | Naive | 7 | 3,821.136 | 3,598.043 | 5.438 | 1.062 | 3 | no | 218.562 | 3,815.591 |
| sutil | interanual | 80 | Seasonal Naive | 7 | 13,556.723 | 5,086.719 | 123.160 | 2.665 | 10 | no | 9,376.906 | 14,288.989 |
| sutil | interanual | 80 | Chronos | 7 | 1,821.825 | 2,757.736 | -31.214 | 0.661 | 1 | sí | 0.000 | 0.000 |
| sutil | interanual | 80 | SARIMA | 7 | 3,563.975 | 3,333.951 | 6.046 | 1.069 | 2 | no | 936.148 | 2,528.215 |
| sutil | interanual | 80 | SARIMA-sel | 7 | 4,649.536 | 3,015.204 | 45.032 | 1.542 | 5 | no | 475.541 | 5,163.202 |
| sutil | interanual | 80 | Ridge | 7 | 4,403.546 | 4,994.025 | -10.590 | 0.882 | 4 | no | 643.740 | 4,863.497 |
| sutil | interanual | 80 | ElasticNet | 7 | 4,972.970 | 4,858.564 | 2.074 | 1.024 | 7 | no | 997.927 | 5,737.289 |
| sutil | interanual | 80 | XGB-37 | 7 | 4,927.737 | 4,875.336 | 0.948 | 1.011 | 6 | no | 434.843 | 6,377.203 |
| sutil | interanual | 80 | GC3 | 7 | 9,105.299 | 5,998.890 | 43.136 | 1.518 | 8 | no | 2,962.554 | 12,246.695 |
| sutil | interanual | 80 | GE | 7 | 9,959.703 | 6,318.752 | 47.693 | 1.576 | 9 | no | 4,074.347 | 12,819.341 |
| sutil | interanual | 85 | Naive | 7 | 3,821.136 | 3,598.043 | 5.438 | 1.062 | 3 | no | 218.562 | 3,815.591 |
| sutil | interanual | 85 | Seasonal Naive | 7 | 13,556.723 | 5,086.719 | 123.160 | 2.665 | 10 | no | 9,376.906 | 14,288.989 |
| sutil | interanual | 85 | Chronos | 7 | 1,821.825 | 2,757.736 | -31.214 | 0.661 | 1 | sí | 0.000 | 0.000 |
| sutil | interanual | 85 | SARIMA | 7 | 3,563.975 | 3,333.951 | 6.046 | 1.069 | 2 | no | 936.148 | 2,528.215 |
| sutil | interanual | 85 | SARIMA-sel | 7 | 4,649.536 | 3,015.204 | 45.032 | 1.542 | 5 | no | 475.541 | 5,163.202 |
| sutil | interanual | 85 | Ridge | 7 | 4,403.546 | 4,994.025 | -10.590 | 0.882 | 4 | no | 643.740 | 4,863.497 |
| sutil | interanual | 85 | ElasticNet | 7 | 4,972.970 | 4,858.564 | 2.074 | 1.024 | 7 | no | 997.927 | 5,737.289 |
| sutil | interanual | 85 | XGB-37 | 7 | 4,927.737 | 4,875.336 | 0.948 | 1.011 | 6 | no | 434.843 | 6,377.203 |
| sutil | interanual | 85 | GC3 | 7 | 9,105.299 | 5,998.890 | 43.136 | 1.518 | 8 | no | 2,962.554 | 12,246.695 |
| sutil | interanual | 85 | GE | 7 | 9,959.703 | 6,318.752 | 47.693 | 1.576 | 9 | no | 4,074.347 | 12,819.341 |
| sutil | interanual | 90 | Naive | 4 | 1,538.943 | 3,773.008 | -57.536 | 0.408 | 2 | sí | -872.232 | 1,946.963 |
| sutil | interanual | 90 | Seasonal Naive | 4 | 15,258.750 | 5,418.896 | 151.178 | 2.816 | 10 | no | 10,697.834 | 16,638.532 |
| sutil | interanual | 90 | Chronos | 4 | 1,116.204 | 2,758.000 | -57.856 | 0.405 | 1 | sí | 0.000 | 0.000 |
| sutil | interanual | 90 | SARIMA | 4 | 3,725.435 | 3,334.741 | 10.850 | 1.117 | 3 | no | 1,722.092 | 3,294.135 |
| sutil | interanual | 90 | SARIMA-sel | 4 | 5,506.388 | 3,041.554 | 71.759 | 1.810 | 6 | no | 2,270.739 | 6,509.629 |
| sutil | interanual | 90 | Ridge | 4 | 4,169.104 | 4,979.138 | -15.350 | 0.837 | 4 | no | 348.179 | 5,942.954 |
| sutil | interanual | 90 | ElasticNet | 4 | 4,817.704 | 4,875.783 | -1.113 | 0.988 | 5 | no | 439.913 | 6,974.822 |
| sutil | interanual | 90 | XGB-37 | 4 | 5,555.691 | 4,833.290 | 13.812 | 1.149 | 7 | sí | -322.930 | 9,201.904 |
| sutil | interanual | 90 | GC3 | 4 | 10,211.615 | 6,086.282 | 60.527 | 1.678 | 8 | no | 1,533.800 | 16,657.022 |
| sutil | interanual | 90 | GE | 4 | 11,299.378 | 6,418.112 | 67.559 | 1.761 | 9 | no | 3,132.745 | 17,233.604 |
| sutil | interanual | 95 | Naive | 3 | 1,723.387 | 3,724.106 | -52.446 | 0.463 | 2 | sí | -1,201.234 | 2,777.028 |
| sutil | interanual | 95 | Seasonal Naive | 3 | 14,460.969 | 5,633.513 | 138.045 | 2.567 | 10 | no | 8,946.383 | 15,952.188 |
| sutil | interanual | 95 | Chronos | 3 | 1,379.199 | 2,715.354 | -47.926 | 0.508 | 1 | sí | 0.000 | 0.000 |
| sutil | interanual | 95 | SARIMA | 3 | 3,783.372 | 3,338.546 | 12.574 | 1.133 | 6 | no | 1,221.321 | 3,363.863 |
| sutil | interanual | 95 | SARIMA-sel | 3 | 5,204.209 | 3,100.701 | 62.333 | 1.678 | 7 | no | 1,009.937 | 6,933.553 |
| sutil | interanual | 95 | Ridge | 3 | 2,900.635 | 5,031.689 | -41.105 | 0.576 | 3 | sí | -133.579 | 3,867.951 |
| sutil | interanual | 95 | ElasticNet | 3 | 3,327.435 | 4,953.200 | -31.702 | 0.672 | 4 | sí | -135.578 | 4,964.882 |
| sutil | interanual | 95 | XGB-37 | 3 | 3,374.301 | 4,960.773 | -30.875 | 0.680 | 5 | sí | -1,014.621 | 6,631.168 |
| sutil | interanual | 95 | GC3 | 3 | 7,204.723 | 6,316.914 | 13.259 | 1.141 | 8 | no | 935.279 | 14,408.970 |
| sutil | interanual | 95 | GE | 3 | 8,484.475 | 6,651.901 | 25.817 | 1.275 | 9 | no | 2,371.432 | 15,050.339 |
| dulce | interanual | 0 | Naive | 60 | 77.522 | — | 0.000 | — | 10 | no | 46.088 | 72.497 |
| dulce | interanual | 0 | Seasonal Naive | 60 | 24.503 | — | 0.000 | — | 3 | no | 2.572 | 9.485 |
| dulce | interanual | 0 | Chronos | 60 | 30.819 | — | 0.000 | — | 4 | no | 6.033 | 18.704 |
| dulce | interanual | 0 | SARIMA | 60 | 18.412 | — | 0.000 | — | 1 | sí | 0.000 | 0.000 |
| dulce | interanual | 0 | SARIMA-sel | 60 | 20.629 | — | 0.000 | — | 2 | sí | -0.757 | 5.136 |
| dulce | interanual | 0 | Ridge | 60 | 53.070 | — | 0.000 | — | 7 | no | 24.819 | 45.154 |
| dulce | interanual | 0 | ElasticNet | 60 | 50.248 | — | 0.000 | — | 6 | no | 22.047 | 42.277 |
| dulce | interanual | 0 | XGB-37 | 60 | 48.260 | — | 0.000 | — | 5 | no | 20.516 | 39.560 |
| dulce | interanual | 0 | GC3 | 60 | 56.669 | — | 0.000 | — | 8 | no | 28.027 | 48.976 |
| dulce | interanual | 0 | GE | 60 | 56.734 | — | 0.000 | — | 9 | no | 28.405 | 48.725 |
| dulce | interanual | 10 | Naive | 52 | 79.403 | 65.299 | 2.426 | 1.216 | 10 | no | 45.607 | 74.961 |
| dulce | interanual | 10 | Seasonal Naive | 52 | 27.958 | 2.047 | 14.099 | 13.656 | 3 | no | 4.699 | 12.035 |
| dulce | interanual | 10 | Chronos | 52 | 31.149 | 28.673 | 1.071 | 1.086 | 4 | no | 4.491 | 18.877 |
| dulce | interanual | 10 | SARIMA | 52 | 19.459 | 11.609 | 5.685 | 1.676 | 1 | sí | 0.000 | 0.000 |
| dulce | interanual | 10 | SARIMA-sel | 52 | 22.285 | 9.866 | 8.027 | 2.259 | 2 | sí | -0.581 | 6.064 |
| dulce | interanual | 10 | Ridge | 52 | 55.071 | 40.065 | 3.770 | 1.375 | 7 | no | 25.320 | 46.163 |
| dulce | interanual | 10 | ElasticNet | 52 | 51.993 | 38.908 | 3.472 | 1.336 | 6 | no | 22.206 | 42.836 |
| dulce | interanual | 10 | XGB-37 | 52 | 49.962 | 37.202 | 3.525 | 1.343 | 5 | no | 20.222 | 41.006 |
| dulce | interanual | 10 | GC3 | 52 | 60.814 | 29.729 | 7.314 | 2.046 | 9 | no | 29.971 | 52.734 |
| dulce | interanual | 10 | GE | 52 | 60.191 | 34.264 | 6.093 | 1.757 | 8 | no | 29.498 | 51.980 |
| dulce | interanual | 15 | Naive | 49 | 75.120 | 88.225 | -3.099 | 0.851 | 10 | no | 41.152 | 69.113 |
| dulce | interanual | 15 | Seasonal Naive | 49 | 29.154 | 3.783 | 18.983 | 7.706 | 3 | no | 4.889 | 12.587 |
| dulce | interanual | 15 | Chronos | 49 | 30.077 | 34.122 | -2.406 | 0.881 | 4 | no | 2.752 | 17.033 |
| dulce | interanual | 15 | SARIMA | 49 | 20.236 | 10.287 | 9.906 | 1.967 | 1 | sí | 0.000 | 0.000 |
| dulce | interanual | 15 | SARIMA-sel | 49 | 22.768 | 11.099 | 10.371 | 2.051 | 2 | sí | -1.039 | 5.969 |
| dulce | interanual | 15 | Ridge | 49 | 56.310 | 38.636 | 6.106 | 1.457 | 7 | no | 25.427 | 47.015 |
| dulce | interanual | 15 | ElasticNet | 49 | 53.139 | 37.368 | 5.754 | 1.422 | 6 | no | 22.171 | 43.814 |
| dulce | interanual | 15 | XGB-37 | 49 | 49.003 | 44.952 | 1.539 | 1.090 | 5 | no | 18.072 | 39.256 |
| dulce | interanual | 15 | GC3 | 49 | 62.617 | 30.174 | 10.496 | 2.075 | 9 | no | 30.179 | 54.333 |
| dulce | interanual | 15 | GE | 49 | 61.621 | 34.969 | 8.612 | 1.762 | 8 | no | 29.503 | 53.240 |
| dulce | interanual | 20 | Naive | 45 | 77.472 | 77.675 | -0.066 | 0.997 | 10 | no | 42.437 | 72.777 |
| dulce | interanual | 20 | Seasonal Naive | 45 | 30.604 | 6.200 | 24.899 | 4.936 | 3 | no | 6.521 | 14.406 |
| dulce | interanual | 20 | Chronos | 45 | 30.743 | 31.048 | -0.247 | 0.990 | 4 | no | 2.916 | 18.405 |
| dulce | interanual | 20 | SARIMA | 45 | 19.964 | 13.755 | 8.431 | 1.451 | 1 | sí | 0.000 | 0.000 |
| dulce | interanual | 20 | SARIMA-sel | 45 | 22.230 | 15.825 | 7.762 | 1.405 | 2 | sí | -1.550 | 5.938 |
| dulce | interanual | 20 | Ridge | 45 | 57.822 | 38.814 | 8.954 | 1.490 | 7 | no | 26.520 | 49.650 |
| dulce | interanual | 20 | ElasticNet | 45 | 54.153 | 38.535 | 7.770 | 1.405 | 6 | no | 22.925 | 45.946 |
| dulce | interanual | 20 | XGB-37 | 45 | 50.622 | 41.177 | 4.893 | 1.229 | 5 | no | 19.278 | 41.821 |
| dulce | interanual | 20 | GC3 | 45 | 63.586 | 35.920 | 12.205 | 1.770 | 9 | no | 30.505 | 56.314 |
| dulce | interanual | 20 | GE | 45 | 61.956 | 41.069 | 9.204 | 1.509 | 8 | no | 29.104 | 54.513 |
| dulce | interanual | 25 | Naive | 42 | 75.524 | 82.184 | -2.577 | 0.919 | 10 | no | 39.095 | 70.470 |
| dulce | interanual | 25 | Seasonal Naive | 42 | 31.826 | 7.416 | 29.887 | 4.292 | 4 | no | 6.494 | 15.077 |
| dulce | interanual | 25 | Chronos | 42 | 30.048 | 32.618 | -2.502 | 0.921 | 3 | no | 1.332 | 16.923 |
| dulce | interanual | 25 | SARIMA | 42 | 20.807 | 12.823 | 13.009 | 1.623 | 1 | sí | 0.000 | 0.000 |
| dulce | interanual | 25 | SARIMA-sel | 42 | 22.472 | 16.327 | 8.936 | 1.376 | 2 | sí | -2.203 | 5.693 |
| dulce | interanual | 25 | Ridge | 42 | 59.658 | 37.698 | 12.414 | 1.583 | 7 | no | 26.755 | 51.323 |
| dulce | interanual | 25 | ElasticNet | 42 | 55.746 | 37.418 | 10.942 | 1.490 | 6 | no | 22.882 | 47.393 |
| dulce | interanual | 25 | XGB-37 | 42 | 51.463 | 40.789 | 6.635 | 1.262 | 5 | no | 18.584 | 42.757 |
| dulce | interanual | 25 | GC3 | 42 | 65.383 | 36.339 | 15.375 | 1.799 | 9 | no | 30.438 | 58.155 |
| dulce | interanual | 25 | GE | 42 | 63.468 | 41.023 | 11.868 | 1.547 | 8 | no | 28.891 | 55.928 |
| dulce | interanual | 30 | Naive | 40 | 77.009 | 78.549 | -0.662 | 0.980 | 10 | no | 39.818 | 73.018 |
| dulce | interanual | 30 | Seasonal Naive | 40 | 32.936 | 7.637 | 34.416 | 4.313 | 4 | no | 8.307 | 15.898 |
| dulce | interanual | 30 | Chronos | 40 | 31.057 | 30.342 | 0.774 | 1.024 | 3 | no | 2.282 | 18.134 |
| dulce | interanual | 30 | SARIMA | 40 | 20.650 | 13.936 | 12.154 | 1.482 | 1 | sí | 0.000 | 0.000 |
| dulce | interanual | 30 | SARIMA-sel | 40 | 21.360 | 19.165 | 3.547 | 1.115 | 2 | sí | -2.659 | 4.156 |
| dulce | interanual | 30 | Ridge | 40 | 61.993 | 35.223 | 16.815 | 1.760 | 7 | no | 28.952 | 53.898 |
| dulce | interanual | 30 | ElasticNet | 40 | 57.998 | 34.748 | 15.423 | 1.669 | 6 | no | 25.103 | 49.524 |
| dulce | interanual | 30 | XGB-37 | 40 | 53.786 | 37.210 | 11.449 | 1.445 | 5 | no | 20.931 | 44.752 |
| dulce | interanual | 30 | GC3 | 40 | 67.562 | 34.883 | 19.222 | 1.937 | 9 | no | 33.094 | 60.135 |
| dulce | interanual | 30 | GE | 40 | 65.461 | 39.281 | 15.382 | 1.666 | 8 | no | 31.469 | 57.907 |
| dulce | interanual | 35 | Naive | 37 | 80.550 | 72.651 | 3.906 | 1.109 | 10 | no | 41.201 | 76.307 |
| dulce | interanual | 35 | Seasonal Naive | 37 | 34.150 | 8.983 | 39.372 | 3.802 | 4 | no | 8.047 | 15.982 |
| dulce | interanual | 35 | Chronos | 37 | 32.921 | 27.437 | 6.820 | 1.200 | 3 | no | 2.177 | 19.366 |
| dulce | interanual | 35 | SARIMA | 37 | 21.933 | 12.748 | 19.122 | 1.720 | 1 | sí | 0.000 | 0.000 |
| dulce | interanual | 35 | SARIMA-sel | 37 | 22.763 | 17.195 | 10.348 | 1.324 | 2 | sí | -2.757 | 4.351 |
| dulce | interanual | 35 | Ridge | 37 | 63.963 | 35.546 | 20.526 | 1.799 | 7 | no | 28.712 | 55.259 |
| dulce | interanual | 35 | ElasticNet | 37 | 59.645 | 35.132 | 18.701 | 1.698 | 6 | no | 24.523 | 50.698 |
| dulce | interanual | 35 | XGB-37 | 37 | 55.910 | 35.954 | 15.851 | 1.555 | 5 | no | 20.903 | 46.546 |
| dulce | interanual | 35 | GC3 | 37 | 69.042 | 36.765 | 21.834 | 1.878 | 9 | no | 32.415 | 60.906 |
| dulce | interanual | 35 | GE | 37 | 66.452 | 41.102 | 17.128 | 1.617 | 8 | no | 30.450 | 58.119 |
| dulce | interanual | 40 | Naive | 35 | 79.475 | 74.789 | 2.519 | 1.063 | 10 | no | 39.554 | 74.643 |
| dulce | interanual | 40 | Seasonal Naive | 35 | 34.811 | 10.072 | 42.068 | 3.456 | 4 | no | 8.251 | 16.394 |
| dulce | interanual | 40 | Chronos | 35 | 32.876 | 27.938 | 6.677 | 1.177 | 3 | no | 1.560 | 18.891 |
| dulce | interanual | 40 | SARIMA | 35 | 22.346 | 12.905 | 21.364 | 1.732 | 1 | sí | 0.000 | 0.000 |
| dulce | interanual | 40 | SARIMA-sel | 35 | 22.426 | 18.113 | 8.711 | 1.238 | 2 | sí | -3.537 | 3.756 |
| dulce | interanual | 40 | Ridge | 35 | 65.246 | 36.024 | 22.943 | 1.811 | 7 | no | 28.948 | 56.643 |
| dulce | interanual | 40 | ElasticNet | 35 | 60.261 | 36.230 | 19.926 | 1.663 | 6 | no | 24.250 | 51.208 |
| dulce | interanual | 40 | XGB-37 | 35 | 54.564 | 39.435 | 13.062 | 1.384 | 5 | no | 19.257 | 44.585 |
| dulce | interanual | 40 | GC3 | 35 | 69.237 | 39.075 | 22.177 | 1.772 | 9 | no | 32.016 | 61.016 |
| dulce | interanual | 40 | GE | 35 | 66.638 | 42.869 | 17.456 | 1.554 | 8 | no | 29.999 | 58.143 |
| dulce | interanual | 45 | Naive | 30 | 79.511 | 75.534 | 2.565 | 1.053 | 10 | no | 36.462 | 75.398 |
| dulce | interanual | 45 | Seasonal Naive | 30 | 36.780 | 12.226 | 50.103 | 3.008 | 4 | no | 8.433 | 17.203 |
| dulce | interanual | 45 | Chronos | 30 | 31.558 | 30.079 | 2.400 | 1.049 | 3 | sí | -1.251 | 16.253 |
| dulce | interanual | 45 | SARIMA | 30 | 23.790 | 13.035 | 29.206 | 1.825 | 1 | sí | 0.000 | 0.000 |
| dulce | interanual | 45 | SARIMA-sel | 30 | 24.377 | 16.881 | 18.169 | 1.444 | 2 | sí | -3.688 | 4.764 |
| dulce | interanual | 45 | Ridge | 30 | 63.441 | 42.699 | 19.542 | 1.486 | 7 | no | 25.909 | 53.504 |
| dulce | interanual | 45 | ElasticNet | 30 | 58.045 | 42.451 | 15.518 | 1.367 | 6 | no | 20.339 | 48.287 |
| dulce | interanual | 45 | XGB-37 | 30 | 52.431 | 44.090 | 8.641 | 1.189 | 5 | no | 15.022 | 42.478 |
| dulce | interanual | 45 | GC3 | 30 | 65.811 | 47.528 | 16.132 | 1.385 | 9 | no | 26.988 | 57.107 |
| dulce | interanual | 45 | GE | 30 | 63.686 | 49.783 | 12.253 | 1.279 | 8 | no | 25.485 | 54.389 |
| dulce | interanual | 50 | Naive | 29 | 81.292 | 73.995 | 4.863 | 1.099 | 10 | no | 37.517 | 77.027 |
| dulce | interanual | 50 | Seasonal Naive | 29 | 37.605 | 12.246 | 53.471 | 3.071 | 4 | no | 8.657 | 17.687 |
| dulce | interanual | 50 | Chronos | 29 | 31.745 | 29.952 | 3.006 | 1.060 | 3 | sí | -1.981 | 16.404 |
| dulce | interanual | 50 | SARIMA | 29 | 24.212 | 12.986 | 31.500 | 1.864 | 1 | sí | 0.000 | 0.000 |
| dulce | interanual | 50 | SARIMA-sel | 29 | 24.851 | 16.679 | 20.467 | 1.490 | 2 | sí | -3.783 | 4.971 |
| dulce | interanual | 50 | Ridge | 29 | 64.909 | 41.994 | 22.310 | 1.546 | 8 | no | 26.439 | 54.977 |
| dulce | interanual | 50 | ElasticNet | 29 | 59.471 | 41.620 | 18.356 | 1.429 | 6 | no | 21.078 | 49.734 |
| dulce | interanual | 50 | XGB-37 | 29 | 53.069 | 43.762 | 9.964 | 1.213 | 5 | no | 14.521 | 43.087 |
| dulce | interanual | 50 | GC3 | 29 | 67.134 | 46.880 | 18.467 | 1.432 | 9 | no | 27.773 | 57.567 |
| dulce | interanual | 50 | GE | 29 | 64.902 | 49.094 | 14.397 | 1.322 | 7 | no | 25.801 | 55.095 |
| dulce | interanual | 55 | Naive | 28 | 78.271 | 76.867 | 0.966 | 1.018 | 10 | no | 34.482 | 73.078 |
| dulce | interanual | 55 | Seasonal Naive | 28 | 37.797 | 12.870 | 54.256 | 2.937 | 4 | no | 8.474 | 17.625 |
| dulce | interanual | 55 | Chronos | 28 | 30.538 | 31.065 | -0.911 | 0.983 | 3 | sí | -3.286 | 14.654 |
| dulce | interanual | 55 | SARIMA | 28 | 24.586 | 13.010 | 33.534 | 1.890 | 1 | sí | 0.000 | 0.000 |
| dulce | interanual | 55 | SARIMA-sel | 28 | 25.248 | 16.587 | 22.392 | 1.522 | 2 | sí | -3.920 | 5.110 |
| dulce | interanual | 55 | Ridge | 28 | 63.209 | 44.198 | 19.106 | 1.430 | 7 | no | 24.708 | 51.690 |
| dulce | interanual | 55 | ElasticNet | 28 | 57.597 | 43.818 | 14.625 | 1.314 | 6 | no | 19.159 | 46.449 |
| dulce | interanual | 55 | XGB-37 | 28 | 50.227 | 46.540 | 4.075 | 1.079 | 5 | no | 11.938 | 39.237 |
| dulce | interanual | 55 | GC3 | 28 | 67.169 | 47.482 | 18.528 | 1.415 | 9 | no | 27.336 | 57.091 |
| dulce | interanual | 55 | GE | 28 | 64.787 | 49.689 | 14.193 | 1.304 | 8 | no | 25.374 | 54.576 |
| dulce | interanual | 60 | Naive | 23 | 78.514 | 76.906 | 1.279 | 1.021 | 10 | no | 29.132 | 74.452 |
| dulce | interanual | 60 | Seasonal Naive | 23 | 40.061 | 14.832 | 63.494 | 2.701 | 4 | no | 7.231 | 19.426 |
| dulce | interanual | 60 | Chronos | 23 | 30.371 | 31.097 | -1.454 | 0.977 | 3 | sí | -6.740 | 13.792 |
| dulce | interanual | 60 | SARIMA | 23 | 27.152 | 12.979 | 47.471 | 2.092 | 2 | sí | -4.238 | 4.061 |
| dulce | interanual | 60 | SARIMA-sel | 23 | 26.385 | 17.050 | 27.905 | 1.547 | 1 | sí | 0.000 | 0.000 |
| dulce | interanual | 60 | Ridge | 23 | 66.540 | 44.697 | 25.381 | 1.489 | 9 | no | 23.483 | 56.630 |
| dulce | interanual | 60 | ElasticNet | 23 | 59.820 | 44.298 | 19.050 | 1.350 | 6 | no | 16.701 | 50.356 |
| dulce | interanual | 60 | XGB-37 | 23 | 50.745 | 46.716 | 5.149 | 1.086 | 5 | no | 8.849 | 40.271 |
| dulce | interanual | 60 | GC3 | 23 | 65.344 | 51.277 | 15.308 | 1.274 | 8 | no | 22.366 | 55.323 |
| dulce | interanual | 60 | GE | 23 | 62.704 | 53.024 | 10.521 | 1.183 | 7 | no | 20.376 | 52.095 |
| dulce | interanual | 65 | Naive | 21 | 76.736 | 77.946 | -1.015 | 0.984 | 10 | no | 25.409 | 72.833 |
| dulce | interanual | 65 | Seasonal Naive | 21 | 40.561 | 15.857 | 65.533 | 2.558 | 4 | no | 6.850 | 18.825 |
| dulce | interanual | 65 | Chronos | 21 | 30.790 | 30.834 | -0.093 | 0.999 | 3 | sí | -7.698 | 13.647 |
| dulce | interanual | 65 | SARIMA | 21 | 27.410 | 13.567 | 48.871 | 2.020 | 1 | sí | 0.000 | 0.000 |
| dulce | interanual | 65 | SARIMA-sel | 21 | 27.821 | 16.756 | 34.867 | 1.660 | 2 | sí | -3.122 | 4.027 |
| dulce | interanual | 65 | Ridge | 21 | 66.131 | 46.037 | 24.611 | 1.436 | 9 | no | 22.006 | 56.004 |
| dulce | interanual | 65 | ElasticNet | 21 | 58.705 | 45.695 | 16.830 | 1.285 | 6 | no | 14.592 | 49.032 |
| dulce | interanual | 65 | XGB-37 | 21 | 49.362 | 47.667 | 2.283 | 1.036 | 5 | no | 6.518 | 38.558 |
| dulce | interanual | 65 | GC3 | 21 | 62.486 | 53.537 | 10.264 | 1.167 | 8 | no | 18.161 | 52.159 |
| dulce | interanual | 65 | GE | 21 | 60.178 | 54.880 | 6.070 | 1.097 | 7 | no | 16.565 | 48.930 |
| dulce | interanual | 70 | Naive | 19 | 75.268 | 78.567 | -2.908 | 0.958 | 10 | no | 22.828 | 72.802 |
| dulce | interanual | 70 | Seasonal Naive | 19 | 40.426 | 17.124 | 64.983 | 2.361 | 4 | no | 5.689 | 18.518 |
| dulce | interanual | 70 | Chronos | 19 | 30.269 | 31.074 | -1.784 | 0.974 | 3 | sí | -9.121 | 13.634 |
| dulce | interanual | 70 | SARIMA | 19 | 28.079 | 13.932 | 52.502 | 2.015 | 1 | sí | 0.000 | 0.000 |
| dulce | interanual | 70 | SARIMA-sel | 19 | 28.594 | 16.938 | 38.611 | 1.688 | 2 | sí | -3.365 | 4.492 |
| dulce | interanual | 70 | Ridge | 19 | 65.393 | 47.359 | 23.221 | 1.381 | 9 | no | 21.739 | 53.537 |
| dulce | interanual | 70 | ElasticNet | 19 | 57.498 | 46.888 | 14.429 | 1.226 | 8 | no | 13.679 | 46.351 |
| dulce | interanual | 70 | XGB-37 | 19 | 43.874 | 50.293 | -9.090 | 0.872 | 5 | no | 3.603 | 27.951 |
| dulce | interanual | 70 | GC3 | 19 | 56.320 | 56.831 | -0.617 | 0.991 | 7 | no | 14.049 | 42.790 |
| dulce | interanual | 70 | GE | 19 | 54.483 | 57.778 | -3.968 | 0.943 | 6 | no | 12.430 | 40.214 |
| dulce | interanual | 75 | Naive | 16 | 83.176 | 75.467 | 7.293 | 1.102 | 10 | no | 28.493 | 83.352 |
| dulce | interanual | 75 | Seasonal Naive | 16 | 42.393 | 17.998 | 73.010 | 2.355 | 5 | no | 7.276 | 21.992 |
| dulce | interanual | 75 | Chronos | 16 | 33.195 | 29.955 | 7.711 | 1.108 | 3 | sí | -6.945 | 18.002 |
| dulce | interanual | 75 | SARIMA | 16 | 27.391 | 15.147 | 48.764 | 1.808 | 1 | sí | 0.000 | 0.000 |
| dulce | interanual | 75 | SARIMA-sel | 16 | 28.377 | 17.811 | 37.560 | 1.593 | 2 | sí | -3.614 | 5.678 |
| dulce | interanual | 75 | Ridge | 16 | 66.417 | 48.216 | 25.150 | 1.377 | 9 | no | 20.658 | 57.661 |
| dulce | interanual | 75 | ElasticNet | 16 | 57.322 | 47.676 | 14.078 | 1.202 | 7 | no | 11.355 | 49.479 |
| dulce | interanual | 75 | XGB-37 | 16 | 42.312 | 50.424 | -12.327 | 0.839 | 4 | no | 0.509 | 29.584 |
| dulce | interanual | 75 | GC3 | 16 | 58.191 | 56.116 | 2.686 | 1.037 | 8 | no | 14.004 | 47.185 |
| dulce | interanual | 75 | GE | 16 | 56.062 | 56.979 | -1.185 | 0.984 | 6 | no | 12.084 | 44.763 |
| dulce | interanual | 80 | Naive | 9 | 79.392 | 77.192 | 2.412 | 1.028 | 10 | no | 18.699 | 79.628 |
| dulce | interanual | 80 | Seasonal Naive | 9 | 47.814 | 20.389 | 95.137 | 2.345 | 6 | no | 12.315 | 30.106 |
| dulce | interanual | 80 | Chronos | 9 | 27.880 | 31.337 | -9.535 | 0.890 | 1 | sí | 0.000 | 0.000 |
| dulce | interanual | 80 | SARIMA | 9 | 34.378 | 15.595 | 86.712 | 2.204 | 2 | sí | -3.086 | 16.832 |
| dulce | interanual | 80 | SARIMA-sel | 9 | 36.413 | 17.843 | 76.515 | 2.041 | 4 | sí | -0.840 | 17.983 |
| dulce | interanual | 80 | Ridge | 9 | 62.027 | 51.489 | 16.878 | 1.205 | 9 | no | 24.143 | 43.831 |
| dulce | interanual | 80 | ElasticNet | 9 | 49.208 | 50.432 | -2.070 | 0.976 | 7 | no | 14.727 | 25.457 |
| dulce | interanual | 80 | XGB-37 | 9 | 34.505 | 50.688 | -28.502 | 0.681 | 3 | sí | -5.125 | 21.842 |
| dulce | interanual | 80 | GC3 | 9 | 51.023 | 57.666 | -9.963 | 0.885 | 8 | no | 14.182 | 30.886 |
| dulce | interanual | 80 | GE | 9 | 46.144 | 58.603 | -18.667 | 0.787 | 5 | no | 10.798 | 24.252 |
| dulce | interanual | 85 | Naive | 6 | 65.750 | 78.830 | -15.186 | 0.834 | 10 | sí | -6.967 | 74.599 |
| dulce | interanual | 85 | Seasonal Naive | 6 | 55.700 | 21.037 | 127.319 | 2.648 | 8 | no | 16.131 | 43.239 |
| dulce | interanual | 85 | Chronos | 6 | 27.009 | 31.242 | -12.360 | 0.865 | 1 | sí | 0.000 | 0.000 |
| dulce | interanual | 85 | SARIMA | 6 | 47.417 | 15.189 | 157.529 | 3.122 | 3 | no | 8.401 | 32.414 |
| dulce | interanual | 85 | SARIMA-sel | 6 | 49.141 | 17.461 | 138.214 | 2.814 | 6 | no | 10.440 | 33.822 |
| dulce | interanual | 85 | Ridge | 6 | 57.664 | 52.559 | 8.657 | 1.097 | 9 | no | 19.266 | 39.758 |
| dulce | interanual | 85 | ElasticNet | 6 | 48.368 | 50.457 | -3.741 | 0.959 | 5 | no | 11.764 | 26.883 |
| dulce | interanual | 85 | XGB-37 | 6 | 34.712 | 49.766 | -28.074 | 0.698 | 2 | sí | -4.856 | 30.528 |
| dulce | interanual | 85 | GC3 | 6 | 54.297 | 56.933 | -4.186 | 0.954 | 7 | no | 13.205 | 38.112 |
| dulce | interanual | 85 | GE | 6 | 48.153 | 57.688 | -15.125 | 0.835 | 4 | no | 10.592 | 30.116 |
| dulce | interanual | 90 | Naive | 4 | 60.260 | 78.755 | -22.268 | 0.765 | 8 | sí | -1.010 | 58.034 |
| dulce | interanual | 90 | Seasonal Naive | 4 | 68.645 | 21.350 | 180.149 | 3.215 | 10 | no | 28.628 | 45.166 |
| dulce | interanual | 90 | Chronos | 4 | 31.748 | 30.752 | 3.014 | 1.032 | 1 | sí | 0.000 | 0.000 |
| dulce | interanual | 90 | SARIMA | 4 | 59.264 | 15.494 | 221.877 | 3.825 | 6 | no | 17.072 | 37.960 |
| dulce | interanual | 90 | SARIMA-sel | 4 | 53.607 | 18.273 | 159.868 | 2.934 | 4 | no | 11.854 | 31.865 |
| dulce | interanual | 90 | Ridge | 4 | 56.546 | 52.821 | 6.550 | 1.071 | 5 | no | 17.962 | 31.635 |
| dulce | interanual | 90 | ElasticNet | 4 | 49.410 | 50.308 | -1.668 | 0.982 | 3 | no | 10.375 | 24.950 |
| dulce | interanual | 90 | XGB-37 | 4 | 43.591 | 48.594 | -9.676 | 0.897 | 2 | sí | -5.579 | 29.265 |
| dulce | interanual | 90 | GC3 | 4 | 67.527 | 55.894 | 19.159 | 1.208 | 9 | no | 31.996 | 39.562 |
| dulce | interanual | 90 | GE | 4 | 59.397 | 56.544 | 4.692 | 1.050 | 7 | no | 23.953 | 31.345 |
| dulce | interanual | 95 | Naive | 1 | 57.491 | 77.862 | -25.839 | 0.738 | 1 | sí | 0.000 | 0.000 |
| dulce | interanual | 95 | Seasonal Naive | 1 | 123.711 | 22.822 | 404.880 | 5.421 | 7 | no | 66.220 | 66.220 |
| dulce | interanual | 95 | Chronos | 1 | 103.001 | 29.595 | 234.216 | 3.480 | 5 | no | 45.510 | 45.510 |
| dulce | interanual | 95 | SARIMA | 1 | 88.114 | 17.231 | 378.565 | 5.114 | 2 | no | 30.623 | 30.623 |
| dulce | interanual | 95 | SARIMA-sel | 1 | 88.236 | 19.483 | 327.733 | 4.529 | 3 | no | 30.745 | 30.745 |
| dulce | interanual | 95 | Ridge | 1 | 156.782 | 51.312 | 195.427 | 3.055 | 10 | no | 99.291 | 99.291 |
| dulce | interanual | 95 | ElasticNet | 1 | 144.966 | 48.643 | 188.501 | 2.980 | 9 | no | 87.475 | 87.475 |
| dulce | interanual | 95 | XGB-37 | 1 | 90.149 | 47.551 | 86.797 | 1.896 | 4 | no | 32.658 | 32.658 |
| dulce | interanual | 95 | GC3 | 1 | 135.643 | 55.331 | 139.359 | 2.451 | 8 | no | 78.152 | 78.152 |
| dulce | interanual | 95 | GE | 1 | 123.461 | 55.604 | 117.612 | 2.220 | 6 | no | 65.970 | 65.970 |

### n_shock_por_ventana.csv — n_shock por ventana y percentil (mensual)

`07_barrido_umbral/mensual/n_shock_por_ventana.csv` — 190 filas × 6 columnas.

| cultivar | tipo | percentil | anio_test | n_shock | informativa |
|---|---|---|---|---|---|
| sutil | mensual | 0 | 2021 | 12 | sí |
| sutil | mensual | 0 | 2022 | 12 | sí |
| sutil | mensual | 0 | 2023 | 12 | sí |
| sutil | mensual | 0 | 2024 | 12 | sí |
| sutil | mensual | 0 | 2025 | 12 | sí |
| sutil | mensual | 10 | 2021 | 7 | sí |
| sutil | mensual | 10 | 2022 | 11 | sí |
| sutil | mensual | 10 | 2023 | 12 | sí |
| sutil | mensual | 10 | 2024 | 9 | sí |
| sutil | mensual | 10 | 2025 | 12 | sí |
| sutil | mensual | 15 | 2021 | 7 | sí |
| sutil | mensual | 15 | 2022 | 10 | sí |
| sutil | mensual | 15 | 2023 | 12 | sí |
| sutil | mensual | 15 | 2024 | 7 | sí |
| sutil | mensual | 15 | 2025 | 11 | sí |
| sutil | mensual | 20 | 2021 | 7 | sí |
| sutil | mensual | 20 | 2022 | 9 | sí |
| sutil | mensual | 20 | 2023 | 12 | sí |
| sutil | mensual | 20 | 2024 | 7 | sí |
| sutil | mensual | 20 | 2025 | 10 | sí |
| sutil | mensual | 25 | 2021 | 7 | sí |
| sutil | mensual | 25 | 2022 | 8 | sí |
| sutil | mensual | 25 | 2023 | 12 | sí |
| sutil | mensual | 25 | 2024 | 6 | sí |
| sutil | mensual | 25 | 2025 | 10 | sí |
| sutil | mensual | 30 | 2021 | 6 | sí |
| sutil | mensual | 30 | 2022 | 8 | sí |
| sutil | mensual | 30 | 2023 | 11 | sí |
| sutil | mensual | 30 | 2024 | 6 | sí |
| sutil | mensual | 30 | 2025 | 7 | sí |
| sutil | mensual | 35 | 2021 | 5 | sí |
| sutil | mensual | 35 | 2022 | 7 | sí |
| sutil | mensual | 35 | 2023 | 11 | sí |
| sutil | mensual | 35 | 2024 | 6 | sí |
| sutil | mensual | 35 | 2025 | 7 | sí |
| sutil | mensual | 40 | 2021 | 3 | sí |
| sutil | mensual | 40 | 2022 | 7 | sí |
| sutil | mensual | 40 | 2023 | 11 | sí |
| sutil | mensual | 40 | 2024 | 6 | sí |
| sutil | mensual | 40 | 2025 | 5 | sí |
| sutil | mensual | 45 | 2021 | 2 | sí |
| sutil | mensual | 45 | 2022 | 7 | sí |
| sutil | mensual | 45 | 2023 | 11 | sí |
| sutil | mensual | 45 | 2024 | 4 | sí |
| sutil | mensual | 45 | 2025 | 5 | sí |
| sutil | mensual | 50 | 2021 | 2 | sí |
| sutil | mensual | 50 | 2022 | 7 | sí |
| sutil | mensual | 50 | 2023 | 11 | sí |
| sutil | mensual | 50 | 2024 | 4 | sí |
| sutil | mensual | 50 | 2025 | 5 | sí |
| sutil | mensual | 55 | 2021 | 2 | sí |
| sutil | mensual | 55 | 2022 | 6 | sí |
| sutil | mensual | 55 | 2023 | 11 | sí |
| sutil | mensual | 55 | 2024 | 4 | sí |
| sutil | mensual | 55 | 2025 | 5 | sí |
| sutil | mensual | 60 | 2021 | 2 | sí |
| sutil | mensual | 60 | 2022 | 4 | sí |
| sutil | mensual | 60 | 2023 | 10 | sí |
| sutil | mensual | 60 | 2024 | 4 | sí |
| sutil | mensual | 60 | 2025 | 5 | sí |
| sutil | mensual | 65 | 2021 | 1 | no |
| sutil | mensual | 65 | 2022 | 4 | sí |
| sutil | mensual | 65 | 2023 | 8 | sí |
| sutil | mensual | 65 | 2024 | 4 | sí |
| sutil | mensual | 65 | 2025 | 4 | sí |
| sutil | mensual | 70 | 2021 | 0 | no |
| sutil | mensual | 70 | 2022 | 3 | sí |
| sutil | mensual | 70 | 2023 | 5 | sí |
| sutil | mensual | 70 | 2024 | 0 | no |
| sutil | mensual | 70 | 2025 | 4 | sí |
| sutil | mensual | 75 | 2021 | 0 | no |
| sutil | mensual | 75 | 2022 | 3 | sí |
| sutil | mensual | 75 | 2023 | 4 | sí |
| sutil | mensual | 75 | 2024 | 0 | no |
| sutil | mensual | 75 | 2025 | 3 | sí |
| sutil | mensual | 80 | 2021 | 0 | no |
| sutil | mensual | 80 | 2022 | 1 | no |
| sutil | mensual | 80 | 2023 | 4 | sí |
| sutil | mensual | 80 | 2024 | 0 | no |
| sutil | mensual | 80 | 2025 | 3 | sí |
| sutil | mensual | 85 | 2021 | 0 | no |
| sutil | mensual | 85 | 2022 | 1 | no |
| sutil | mensual | 85 | 2023 | 3 | sí |
| sutil | mensual | 85 | 2024 | 0 | no |
| sutil | mensual | 85 | 2025 | 3 | sí |
| sutil | mensual | 90 | 2021 | 0 | no |
| sutil | mensual | 90 | 2022 | 1 | no |
| sutil | mensual | 90 | 2023 | 3 | sí |
| sutil | mensual | 90 | 2024 | 0 | no |
| sutil | mensual | 90 | 2025 | 2 | sí |
| sutil | mensual | 95 | 2021 | 0 | no |
| sutil | mensual | 95 | 2022 | 0 | no |
| sutil | mensual | 95 | 2023 | 1 | no |
| sutil | mensual | 95 | 2024 | 0 | no |
| sutil | mensual | 95 | 2025 | 2 | sí |
| dulce | mensual | 0 | 2021 | 12 | sí |
| dulce | mensual | 0 | 2022 | 12 | sí |
| dulce | mensual | 0 | 2023 | 12 | sí |
| dulce | mensual | 0 | 2024 | 12 | sí |
| dulce | mensual | 0 | 2025 | 12 | sí |
| dulce | mensual | 10 | 2021 | 11 | sí |
| dulce | mensual | 10 | 2022 | 12 | sí |
| dulce | mensual | 10 | 2023 | 12 | sí |
| dulce | mensual | 10 | 2024 | 12 | sí |
| dulce | mensual | 10 | 2025 | 12 | sí |
| dulce | mensual | 15 | 2021 | 10 | sí |
| dulce | mensual | 15 | 2022 | 11 | sí |
| dulce | mensual | 15 | 2023 | 11 | sí |
| dulce | mensual | 15 | 2024 | 10 | sí |
| dulce | mensual | 15 | 2025 | 11 | sí |
| dulce | mensual | 20 | 2021 | 9 | sí |
| dulce | mensual | 20 | 2022 | 10 | sí |
| dulce | mensual | 20 | 2023 | 11 | sí |
| dulce | mensual | 20 | 2024 | 10 | sí |
| dulce | mensual | 20 | 2025 | 11 | sí |
| dulce | mensual | 25 | 2021 | 9 | sí |
| dulce | mensual | 25 | 2022 | 9 | sí |
| dulce | mensual | 25 | 2023 | 8 | sí |
| dulce | mensual | 25 | 2024 | 8 | sí |
| dulce | mensual | 25 | 2025 | 10 | sí |
| dulce | mensual | 30 | 2021 | 8 | sí |
| dulce | mensual | 30 | 2022 | 9 | sí |
| dulce | mensual | 30 | 2023 | 8 | sí |
| dulce | mensual | 30 | 2024 | 8 | sí |
| dulce | mensual | 30 | 2025 | 9 | sí |
| dulce | mensual | 35 | 2021 | 7 | sí |
| dulce | mensual | 35 | 2022 | 7 | sí |
| dulce | mensual | 35 | 2023 | 8 | sí |
| dulce | mensual | 35 | 2024 | 8 | sí |
| dulce | mensual | 35 | 2025 | 8 | sí |
| dulce | mensual | 40 | 2021 | 5 | sí |
| dulce | mensual | 40 | 2022 | 6 | sí |
| dulce | mensual | 40 | 2023 | 8 | sí |
| dulce | mensual | 40 | 2024 | 8 | sí |
| dulce | mensual | 40 | 2025 | 7 | sí |
| dulce | mensual | 45 | 2021 | 5 | sí |
| dulce | mensual | 45 | 2022 | 5 | sí |
| dulce | mensual | 45 | 2023 | 7 | sí |
| dulce | mensual | 45 | 2024 | 6 | sí |
| dulce | mensual | 45 | 2025 | 6 | sí |
| dulce | mensual | 50 | 2021 | 5 | sí |
| dulce | mensual | 50 | 2022 | 5 | sí |
| dulce | mensual | 50 | 2023 | 6 | sí |
| dulce | mensual | 50 | 2024 | 6 | sí |
| dulce | mensual | 50 | 2025 | 6 | sí |
| dulce | mensual | 55 | 2021 | 5 | sí |
| dulce | mensual | 55 | 2022 | 5 | sí |
| dulce | mensual | 55 | 2023 | 4 | sí |
| dulce | mensual | 55 | 2024 | 6 | sí |
| dulce | mensual | 55 | 2025 | 5 | sí |
| dulce | mensual | 60 | 2021 | 4 | sí |
| dulce | mensual | 60 | 2022 | 5 | sí |
| dulce | mensual | 60 | 2023 | 4 | sí |
| dulce | mensual | 60 | 2024 | 5 | sí |
| dulce | mensual | 60 | 2025 | 5 | sí |
| dulce | mensual | 65 | 2021 | 4 | sí |
| dulce | mensual | 65 | 2022 | 4 | sí |
| dulce | mensual | 65 | 2023 | 4 | sí |
| dulce | mensual | 65 | 2024 | 5 | sí |
| dulce | mensual | 65 | 2025 | 5 | sí |
| dulce | mensual | 70 | 2021 | 3 | sí |
| dulce | mensual | 70 | 2022 | 4 | sí |
| dulce | mensual | 70 | 2023 | 3 | sí |
| dulce | mensual | 70 | 2024 | 4 | sí |
| dulce | mensual | 70 | 2025 | 3 | sí |
| dulce | mensual | 75 | 2021 | 3 | sí |
| dulce | mensual | 75 | 2022 | 3 | sí |
| dulce | mensual | 75 | 2023 | 2 | sí |
| dulce | mensual | 75 | 2024 | 4 | sí |
| dulce | mensual | 75 | 2025 | 3 | sí |
| dulce | mensual | 80 | 2021 | 3 | sí |
| dulce | mensual | 80 | 2022 | 2 | sí |
| dulce | mensual | 80 | 2023 | 1 | no |
| dulce | mensual | 80 | 2024 | 3 | sí |
| dulce | mensual | 80 | 2025 | 3 | sí |
| dulce | mensual | 85 | 2021 | 3 | sí |
| dulce | mensual | 85 | 2022 | 2 | sí |
| dulce | mensual | 85 | 2023 | 1 | no |
| dulce | mensual | 85 | 2024 | 2 | sí |
| dulce | mensual | 85 | 2025 | 1 | no |
| dulce | mensual | 90 | 2021 | 3 | sí |
| dulce | mensual | 90 | 2022 | 1 | no |
| dulce | mensual | 90 | 2023 | 0 | no |
| dulce | mensual | 90 | 2024 | 1 | no |
| dulce | mensual | 90 | 2025 | 0 | no |
| dulce | mensual | 95 | 2021 | 1 | no |
| dulce | mensual | 95 | 2022 | 0 | no |
| dulce | mensual | 95 | 2023 | 0 | no |
| dulce | mensual | 95 | 2024 | 0 | no |
| dulce | mensual | 95 | 2025 | 0 | no |

### n_shock_por_ventana.csv — n_shock por ventana y percentil (interanual)

`07_barrido_umbral/interanual/n_shock_por_ventana.csv` — 190 filas × 6 columnas.

| cultivar | tipo | percentil | anio_test | n_shock | informativa |
|---|---|---|---|---|---|
| sutil | interanual | 0 | 2021 | 12 | sí |
| sutil | interanual | 0 | 2022 | 12 | sí |
| sutil | interanual | 0 | 2023 | 12 | sí |
| sutil | interanual | 0 | 2024 | 12 | sí |
| sutil | interanual | 0 | 2025 | 12 | sí |
| sutil | interanual | 10 | 2021 | 10 | sí |
| sutil | interanual | 10 | 2022 | 9 | sí |
| sutil | interanual | 10 | 2023 | 10 | sí |
| sutil | interanual | 10 | 2024 | 11 | sí |
| sutil | interanual | 10 | 2025 | 12 | sí |
| sutil | interanual | 15 | 2021 | 10 | sí |
| sutil | interanual | 15 | 2022 | 8 | sí |
| sutil | interanual | 15 | 2023 | 10 | sí |
| sutil | interanual | 15 | 2024 | 11 | sí |
| sutil | interanual | 15 | 2025 | 12 | sí |
| sutil | interanual | 20 | 2021 | 9 | sí |
| sutil | interanual | 20 | 2022 | 8 | sí |
| sutil | interanual | 20 | 2023 | 10 | sí |
| sutil | interanual | 20 | 2024 | 11 | sí |
| sutil | interanual | 20 | 2025 | 6 | sí |
| sutil | interanual | 25 | 2021 | 9 | sí |
| sutil | interanual | 25 | 2022 | 7 | sí |
| sutil | interanual | 25 | 2023 | 10 | sí |
| sutil | interanual | 25 | 2024 | 11 | sí |
| sutil | interanual | 25 | 2025 | 5 | sí |
| sutil | interanual | 30 | 2021 | 9 | sí |
| sutil | interanual | 30 | 2022 | 5 | sí |
| sutil | interanual | 30 | 2023 | 9 | sí |
| sutil | interanual | 30 | 2024 | 11 | sí |
| sutil | interanual | 30 | 2025 | 4 | sí |
| sutil | interanual | 35 | 2021 | 6 | sí |
| sutil | interanual | 35 | 2022 | 5 | sí |
| sutil | interanual | 35 | 2023 | 9 | sí |
| sutil | interanual | 35 | 2024 | 10 | sí |
| sutil | interanual | 35 | 2025 | 4 | sí |
| sutil | interanual | 40 | 2021 | 6 | sí |
| sutil | interanual | 40 | 2022 | 5 | sí |
| sutil | interanual | 40 | 2023 | 9 | sí |
| sutil | interanual | 40 | 2024 | 9 | sí |
| sutil | interanual | 40 | 2025 | 4 | sí |
| sutil | interanual | 45 | 2021 | 3 | sí |
| sutil | interanual | 45 | 2022 | 3 | sí |
| sutil | interanual | 45 | 2023 | 8 | sí |
| sutil | interanual | 45 | 2024 | 9 | sí |
| sutil | interanual | 45 | 2025 | 4 | sí |
| sutil | interanual | 50 | 2021 | 3 | sí |
| sutil | interanual | 50 | 2022 | 3 | sí |
| sutil | interanual | 50 | 2023 | 7 | sí |
| sutil | interanual | 50 | 2024 | 8 | sí |
| sutil | interanual | 50 | 2025 | 4 | sí |
| sutil | interanual | 55 | 2021 | 2 | sí |
| sutil | interanual | 55 | 2022 | 1 | no |
| sutil | interanual | 55 | 2023 | 7 | sí |
| sutil | interanual | 55 | 2024 | 8 | sí |
| sutil | interanual | 55 | 2025 | 3 | sí |
| sutil | interanual | 60 | 2021 | 2 | sí |
| sutil | interanual | 60 | 2022 | 0 | no |
| sutil | interanual | 60 | 2023 | 6 | sí |
| sutil | interanual | 60 | 2024 | 8 | sí |
| sutil | interanual | 60 | 2025 | 2 | sí |
| sutil | interanual | 65 | 2021 | 2 | sí |
| sutil | interanual | 65 | 2022 | 0 | no |
| sutil | interanual | 65 | 2023 | 5 | sí |
| sutil | interanual | 65 | 2024 | 8 | sí |
| sutil | interanual | 65 | 2025 | 1 | no |
| sutil | interanual | 70 | 2021 | 2 | sí |
| sutil | interanual | 70 | 2022 | 0 | no |
| sutil | interanual | 70 | 2023 | 3 | sí |
| sutil | interanual | 70 | 2024 | 8 | sí |
| sutil | interanual | 70 | 2025 | 0 | no |
| sutil | interanual | 75 | 2021 | 0 | no |
| sutil | interanual | 75 | 2022 | 0 | no |
| sutil | interanual | 75 | 2023 | 2 | sí |
| sutil | interanual | 75 | 2024 | 8 | sí |
| sutil | interanual | 75 | 2025 | 0 | no |
| sutil | interanual | 80 | 2021 | 0 | no |
| sutil | interanual | 80 | 2022 | 0 | no |
| sutil | interanual | 80 | 2023 | 1 | no |
| sutil | interanual | 80 | 2024 | 6 | sí |
| sutil | interanual | 80 | 2025 | 0 | no |
| sutil | interanual | 85 | 2021 | 0 | no |
| sutil | interanual | 85 | 2022 | 0 | no |
| sutil | interanual | 85 | 2023 | 1 | no |
| sutil | interanual | 85 | 2024 | 6 | sí |
| sutil | interanual | 85 | 2025 | 0 | no |
| sutil | interanual | 90 | 2021 | 0 | no |
| sutil | interanual | 90 | 2022 | 0 | no |
| sutil | interanual | 90 | 2023 | 0 | no |
| sutil | interanual | 90 | 2024 | 4 | sí |
| sutil | interanual | 90 | 2025 | 0 | no |
| sutil | interanual | 95 | 2021 | 0 | no |
| sutil | interanual | 95 | 2022 | 0 | no |
| sutil | interanual | 95 | 2023 | 0 | no |
| sutil | interanual | 95 | 2024 | 3 | sí |
| sutil | interanual | 95 | 2025 | 0 | no |
| dulce | interanual | 0 | 2021 | 12 | sí |
| dulce | interanual | 0 | 2022 | 12 | sí |
| dulce | interanual | 0 | 2023 | 12 | sí |
| dulce | interanual | 0 | 2024 | 12 | sí |
| dulce | interanual | 0 | 2025 | 12 | sí |
| dulce | interanual | 10 | 2021 | 11 | sí |
| dulce | interanual | 10 | 2022 | 10 | sí |
| dulce | interanual | 10 | 2023 | 8 | sí |
| dulce | interanual | 10 | 2024 | 12 | sí |
| dulce | interanual | 10 | 2025 | 11 | sí |
| dulce | interanual | 15 | 2021 | 10 | sí |
| dulce | interanual | 15 | 2022 | 9 | sí |
| dulce | interanual | 15 | 2023 | 7 | sí |
| dulce | interanual | 15 | 2024 | 12 | sí |
| dulce | interanual | 15 | 2025 | 11 | sí |
| dulce | interanual | 20 | 2021 | 9 | sí |
| dulce | interanual | 20 | 2022 | 9 | sí |
| dulce | interanual | 20 | 2023 | 5 | sí |
| dulce | interanual | 20 | 2024 | 11 | sí |
| dulce | interanual | 20 | 2025 | 11 | sí |
| dulce | interanual | 25 | 2021 | 8 | sí |
| dulce | interanual | 25 | 2022 | 8 | sí |
| dulce | interanual | 25 | 2023 | 4 | sí |
| dulce | interanual | 25 | 2024 | 11 | sí |
| dulce | interanual | 25 | 2025 | 11 | sí |
| dulce | interanual | 30 | 2021 | 7 | sí |
| dulce | interanual | 30 | 2022 | 8 | sí |
| dulce | interanual | 30 | 2023 | 4 | sí |
| dulce | interanual | 30 | 2024 | 11 | sí |
| dulce | interanual | 30 | 2025 | 10 | sí |
| dulce | interanual | 35 | 2021 | 6 | sí |
| dulce | interanual | 35 | 2022 | 6 | sí |
| dulce | interanual | 35 | 2023 | 4 | sí |
| dulce | interanual | 35 | 2024 | 11 | sí |
| dulce | interanual | 35 | 2025 | 10 | sí |
| dulce | interanual | 40 | 2021 | 5 | sí |
| dulce | interanual | 40 | 2022 | 6 | sí |
| dulce | interanual | 40 | 2023 | 3 | sí |
| dulce | interanual | 40 | 2024 | 11 | sí |
| dulce | interanual | 40 | 2025 | 10 | sí |
| dulce | interanual | 45 | 2021 | 4 | sí |
| dulce | interanual | 45 | 2022 | 6 | sí |
| dulce | interanual | 45 | 2023 | 2 | sí |
| dulce | interanual | 45 | 2024 | 11 | sí |
| dulce | interanual | 45 | 2025 | 7 | sí |
| dulce | interanual | 50 | 2021 | 4 | sí |
| dulce | interanual | 50 | 2022 | 6 | sí |
| dulce | interanual | 50 | 2023 | 2 | sí |
| dulce | interanual | 50 | 2024 | 11 | sí |
| dulce | interanual | 50 | 2025 | 6 | sí |
| dulce | interanual | 55 | 2021 | 4 | sí |
| dulce | interanual | 55 | 2022 | 5 | sí |
| dulce | interanual | 55 | 2023 | 2 | sí |
| dulce | interanual | 55 | 2024 | 11 | sí |
| dulce | interanual | 55 | 2025 | 6 | sí |
| dulce | interanual | 60 | 2021 | 3 | sí |
| dulce | interanual | 60 | 2022 | 4 | sí |
| dulce | interanual | 60 | 2023 | 1 | no |
| dulce | interanual | 60 | 2024 | 10 | sí |
| dulce | interanual | 60 | 2025 | 5 | sí |
| dulce | interanual | 65 | 2021 | 2 | sí |
| dulce | interanual | 65 | 2022 | 4 | sí |
| dulce | interanual | 65 | 2023 | 1 | no |
| dulce | interanual | 65 | 2024 | 10 | sí |
| dulce | interanual | 65 | 2025 | 4 | sí |
| dulce | interanual | 70 | 2021 | 2 | sí |
| dulce | interanual | 70 | 2022 | 3 | sí |
| dulce | interanual | 70 | 2023 | 1 | no |
| dulce | interanual | 70 | 2024 | 10 | sí |
| dulce | interanual | 70 | 2025 | 3 | sí |
| dulce | interanual | 75 | 2021 | 2 | sí |
| dulce | interanual | 75 | 2022 | 2 | sí |
| dulce | interanual | 75 | 2023 | 0 | no |
| dulce | interanual | 75 | 2024 | 9 | sí |
| dulce | interanual | 75 | 2025 | 3 | sí |
| dulce | interanual | 80 | 2021 | 2 | sí |
| dulce | interanual | 80 | 2022 | 1 | no |
| dulce | interanual | 80 | 2023 | 0 | no |
| dulce | interanual | 80 | 2024 | 5 | sí |
| dulce | interanual | 80 | 2025 | 1 | no |
| dulce | interanual | 85 | 2021 | 2 | sí |
| dulce | interanual | 85 | 2022 | 0 | no |
| dulce | interanual | 85 | 2023 | 0 | no |
| dulce | interanual | 85 | 2024 | 3 | sí |
| dulce | interanual | 85 | 2025 | 1 | no |
| dulce | interanual | 90 | 2021 | 1 | no |
| dulce | interanual | 90 | 2022 | 0 | no |
| dulce | interanual | 90 | 2023 | 0 | no |
| dulce | interanual | 90 | 2024 | 2 | sí |
| dulce | interanual | 90 | 2025 | 1 | no |
| dulce | interanual | 95 | 2021 | 0 | no |
| dulce | interanual | 95 | 2022 | 0 | no |
| dulce | interanual | 95 | 2023 | 0 | no |
| dulce | interanual | 95 | 2024 | 1 | no |
| dulce | interanual | 95 | 2025 | 0 | no |

### estabilizacion.csv — Estabilización del ranking

`07_barrido_umbral/estabilizacion.csv` — 4 filas × 5 columnas.

| cultivar | tipo | primer_lugar_estable_desde | modelo_estable | todos_empatan_desde |
|---|---|---|---|---|
| sutil | mensual | 75 | Chronos | — |
| sutil | interanual | 0 | Chronos | — |
| dulce | mensual | 0 | SARIMA | — |
| dulce | interanual | 95 | Naive | — |

### comprobacion_P0.csv — Comprobación de P0: las 240 comprobaciones

`07_barrido_umbral/comprobacion_P0.csv` — 240 filas × 8 columnas.

| cultivar | tipo | modelo | ventana | n_shock | Delta_s | Delta_s_es_0_exacto | n_shock_esperado |
|---|---|---|---|---|---|---|---|
| sutil | mensual | Naive | 2021 | 12 | 0 | sí | 12 |
| sutil | mensual | Naive | 2022 | 12 | 0 | sí | 12 |
| sutil | mensual | Naive | 2023 | 12 | 0 | sí | 12 |
| sutil | mensual | Naive | 2024 | 12 | 0 | sí | 12 |
| sutil | mensual | Naive | 2025 | 12 | 0 | sí | 12 |
| sutil | mensual | Naive | agregado | 60 | 0 | sí | 60 |
| sutil | mensual | Seasonal Naive | 2021 | 12 | 0 | sí | 12 |
| sutil | mensual | Seasonal Naive | 2022 | 12 | 0 | sí | 12 |
| sutil | mensual | Seasonal Naive | 2023 | 12 | 0 | sí | 12 |
| sutil | mensual | Seasonal Naive | 2024 | 12 | 0 | sí | 12 |
| sutil | mensual | Seasonal Naive | 2025 | 12 | 0 | sí | 12 |
| sutil | mensual | Seasonal Naive | agregado | 60 | 0 | sí | 60 |
| sutil | mensual | Chronos | 2021 | 12 | 0 | sí | 12 |
| sutil | mensual | Chronos | 2022 | 12 | 0 | sí | 12 |
| sutil | mensual | Chronos | 2023 | 12 | 0 | sí | 12 |
| sutil | mensual | Chronos | 2024 | 12 | 0 | sí | 12 |
| sutil | mensual | Chronos | 2025 | 12 | 0 | sí | 12 |
| sutil | mensual | Chronos | agregado | 60 | 0 | sí | 60 |
| sutil | mensual | SARIMA | 2021 | 12 | 0 | sí | 12 |
| sutil | mensual | SARIMA | 2022 | 12 | 0 | sí | 12 |
| sutil | mensual | SARIMA | 2023 | 12 | 0 | sí | 12 |
| sutil | mensual | SARIMA | 2024 | 12 | 0 | sí | 12 |
| sutil | mensual | SARIMA | 2025 | 12 | 0 | sí | 12 |
| sutil | mensual | SARIMA | agregado | 60 | 0 | sí | 60 |
| sutil | mensual | SARIMA-sel | 2021 | 12 | 0 | sí | 12 |
| sutil | mensual | SARIMA-sel | 2022 | 12 | 0 | sí | 12 |
| sutil | mensual | SARIMA-sel | 2023 | 12 | 0 | sí | 12 |
| sutil | mensual | SARIMA-sel | 2024 | 12 | 0 | sí | 12 |
| sutil | mensual | SARIMA-sel | 2025 | 12 | 0 | sí | 12 |
| sutil | mensual | SARIMA-sel | agregado | 60 | 0 | sí | 60 |
| sutil | mensual | Ridge | 2021 | 12 | 0 | sí | 12 |
| sutil | mensual | Ridge | 2022 | 12 | 0 | sí | 12 |
| sutil | mensual | Ridge | 2023 | 12 | 0 | sí | 12 |
| sutil | mensual | Ridge | 2024 | 12 | 0 | sí | 12 |
| sutil | mensual | Ridge | 2025 | 12 | 0 | sí | 12 |
| sutil | mensual | Ridge | agregado | 60 | 0 | sí | 60 |
| sutil | mensual | ElasticNet | 2021 | 12 | 0 | sí | 12 |
| sutil | mensual | ElasticNet | 2022 | 12 | 0 | sí | 12 |
| sutil | mensual | ElasticNet | 2023 | 12 | 0 | sí | 12 |
| sutil | mensual | ElasticNet | 2024 | 12 | 0 | sí | 12 |
| sutil | mensual | ElasticNet | 2025 | 12 | 0 | sí | 12 |
| sutil | mensual | ElasticNet | agregado | 60 | 0 | sí | 60 |
| sutil | mensual | XGB-37 | 2021 | 12 | 0 | sí | 12 |
| sutil | mensual | XGB-37 | 2022 | 12 | 0 | sí | 12 |
| sutil | mensual | XGB-37 | 2023 | 12 | 0 | sí | 12 |
| sutil | mensual | XGB-37 | 2024 | 12 | 0 | sí | 12 |
| sutil | mensual | XGB-37 | 2025 | 12 | 0 | sí | 12 |
| sutil | mensual | XGB-37 | agregado | 60 | 0 | sí | 60 |
| sutil | mensual | GC3 | 2021 | 12 | 0 | sí | 12 |
| sutil | mensual | GC3 | 2022 | 12 | 0 | sí | 12 |
| sutil | mensual | GC3 | 2023 | 12 | 0 | sí | 12 |
| sutil | mensual | GC3 | 2024 | 12 | 0 | sí | 12 |
| sutil | mensual | GC3 | 2025 | 12 | 0 | sí | 12 |
| sutil | mensual | GC3 | agregado | 60 | 0 | sí | 60 |
| sutil | mensual | GE | 2021 | 12 | 0 | sí | 12 |
| sutil | mensual | GE | 2022 | 12 | 0 | sí | 12 |
| sutil | mensual | GE | 2023 | 12 | 0 | sí | 12 |
| sutil | mensual | GE | 2024 | 12 | 0 | sí | 12 |
| sutil | mensual | GE | 2025 | 12 | 0 | sí | 12 |
| sutil | mensual | GE | agregado | 60 | 0 | sí | 60 |
| sutil | interanual | Naive | 2021 | 12 | 0 | sí | 12 |
| sutil | interanual | Naive | 2022 | 12 | 0 | sí | 12 |
| sutil | interanual | Naive | 2023 | 12 | 0 | sí | 12 |
| sutil | interanual | Naive | 2024 | 12 | 0 | sí | 12 |
| sutil | interanual | Naive | 2025 | 12 | 0 | sí | 12 |
| sutil | interanual | Naive | agregado | 60 | 0 | sí | 60 |
| sutil | interanual | Seasonal Naive | 2021 | 12 | 0 | sí | 12 |
| sutil | interanual | Seasonal Naive | 2022 | 12 | 0 | sí | 12 |
| sutil | interanual | Seasonal Naive | 2023 | 12 | 0 | sí | 12 |
| sutil | interanual | Seasonal Naive | 2024 | 12 | 0 | sí | 12 |
| sutil | interanual | Seasonal Naive | 2025 | 12 | 0 | sí | 12 |
| sutil | interanual | Seasonal Naive | agregado | 60 | 0 | sí | 60 |
| sutil | interanual | Chronos | 2021 | 12 | 0 | sí | 12 |
| sutil | interanual | Chronos | 2022 | 12 | 0 | sí | 12 |
| sutil | interanual | Chronos | 2023 | 12 | 0 | sí | 12 |
| sutil | interanual | Chronos | 2024 | 12 | 0 | sí | 12 |
| sutil | interanual | Chronos | 2025 | 12 | 0 | sí | 12 |
| sutil | interanual | Chronos | agregado | 60 | 0 | sí | 60 |
| sutil | interanual | SARIMA | 2021 | 12 | 0 | sí | 12 |
| sutil | interanual | SARIMA | 2022 | 12 | 0 | sí | 12 |
| sutil | interanual | SARIMA | 2023 | 12 | 0 | sí | 12 |
| sutil | interanual | SARIMA | 2024 | 12 | 0 | sí | 12 |
| sutil | interanual | SARIMA | 2025 | 12 | 0 | sí | 12 |
| sutil | interanual | SARIMA | agregado | 60 | 0 | sí | 60 |
| sutil | interanual | SARIMA-sel | 2021 | 12 | 0 | sí | 12 |
| sutil | interanual | SARIMA-sel | 2022 | 12 | 0 | sí | 12 |
| sutil | interanual | SARIMA-sel | 2023 | 12 | 0 | sí | 12 |
| sutil | interanual | SARIMA-sel | 2024 | 12 | 0 | sí | 12 |
| sutil | interanual | SARIMA-sel | 2025 | 12 | 0 | sí | 12 |
| sutil | interanual | SARIMA-sel | agregado | 60 | 0 | sí | 60 |
| sutil | interanual | Ridge | 2021 | 12 | 0 | sí | 12 |
| sutil | interanual | Ridge | 2022 | 12 | 0 | sí | 12 |
| sutil | interanual | Ridge | 2023 | 12 | 0 | sí | 12 |
| sutil | interanual | Ridge | 2024 | 12 | 0 | sí | 12 |
| sutil | interanual | Ridge | 2025 | 12 | 0 | sí | 12 |
| sutil | interanual | Ridge | agregado | 60 | 0 | sí | 60 |
| sutil | interanual | ElasticNet | 2021 | 12 | 0 | sí | 12 |
| sutil | interanual | ElasticNet | 2022 | 12 | 0 | sí | 12 |
| sutil | interanual | ElasticNet | 2023 | 12 | 0 | sí | 12 |
| sutil | interanual | ElasticNet | 2024 | 12 | 0 | sí | 12 |
| sutil | interanual | ElasticNet | 2025 | 12 | 0 | sí | 12 |
| sutil | interanual | ElasticNet | agregado | 60 | 0 | sí | 60 |
| sutil | interanual | XGB-37 | 2021 | 12 | 0 | sí | 12 |
| sutil | interanual | XGB-37 | 2022 | 12 | 0 | sí | 12 |
| sutil | interanual | XGB-37 | 2023 | 12 | 0 | sí | 12 |
| sutil | interanual | XGB-37 | 2024 | 12 | 0 | sí | 12 |
| sutil | interanual | XGB-37 | 2025 | 12 | 0 | sí | 12 |
| sutil | interanual | XGB-37 | agregado | 60 | 0 | sí | 60 |
| sutil | interanual | GC3 | 2021 | 12 | 0 | sí | 12 |
| sutil | interanual | GC3 | 2022 | 12 | 0 | sí | 12 |
| sutil | interanual | GC3 | 2023 | 12 | 0 | sí | 12 |
| sutil | interanual | GC3 | 2024 | 12 | 0 | sí | 12 |
| sutil | interanual | GC3 | 2025 | 12 | 0 | sí | 12 |
| sutil | interanual | GC3 | agregado | 60 | 0 | sí | 60 |
| sutil | interanual | GE | 2021 | 12 | 0 | sí | 12 |
| sutil | interanual | GE | 2022 | 12 | 0 | sí | 12 |
| sutil | interanual | GE | 2023 | 12 | 0 | sí | 12 |
| sutil | interanual | GE | 2024 | 12 | 0 | sí | 12 |
| sutil | interanual | GE | 2025 | 12 | 0 | sí | 12 |
| sutil | interanual | GE | agregado | 60 | 0 | sí | 60 |
| dulce | mensual | Naive | 2021 | 12 | 0 | sí | 12 |
| dulce | mensual | Naive | 2022 | 12 | 0 | sí | 12 |
| dulce | mensual | Naive | 2023 | 12 | 0 | sí | 12 |
| dulce | mensual | Naive | 2024 | 12 | 0 | sí | 12 |
| dulce | mensual | Naive | 2025 | 12 | 0 | sí | 12 |
| dulce | mensual | Naive | agregado | 60 | 0 | sí | 60 |
| dulce | mensual | Seasonal Naive | 2021 | 12 | 0 | sí | 12 |
| dulce | mensual | Seasonal Naive | 2022 | 12 | 0 | sí | 12 |
| dulce | mensual | Seasonal Naive | 2023 | 12 | 0 | sí | 12 |
| dulce | mensual | Seasonal Naive | 2024 | 12 | 0 | sí | 12 |
| dulce | mensual | Seasonal Naive | 2025 | 12 | 0 | sí | 12 |
| dulce | mensual | Seasonal Naive | agregado | 60 | 0 | sí | 60 |
| dulce | mensual | Chronos | 2021 | 12 | 0 | sí | 12 |
| dulce | mensual | Chronos | 2022 | 12 | 0 | sí | 12 |
| dulce | mensual | Chronos | 2023 | 12 | 0 | sí | 12 |
| dulce | mensual | Chronos | 2024 | 12 | 0 | sí | 12 |
| dulce | mensual | Chronos | 2025 | 12 | 0 | sí | 12 |
| dulce | mensual | Chronos | agregado | 60 | 0 | sí | 60 |
| dulce | mensual | SARIMA | 2021 | 12 | 0 | sí | 12 |
| dulce | mensual | SARIMA | 2022 | 12 | 0 | sí | 12 |
| dulce | mensual | SARIMA | 2023 | 12 | 0 | sí | 12 |
| dulce | mensual | SARIMA | 2024 | 12 | 0 | sí | 12 |
| dulce | mensual | SARIMA | 2025 | 12 | 0 | sí | 12 |
| dulce | mensual | SARIMA | agregado | 60 | 0 | sí | 60 |
| dulce | mensual | SARIMA-sel | 2021 | 12 | 0 | sí | 12 |
| dulce | mensual | SARIMA-sel | 2022 | 12 | 0 | sí | 12 |
| dulce | mensual | SARIMA-sel | 2023 | 12 | 0 | sí | 12 |
| dulce | mensual | SARIMA-sel | 2024 | 12 | 0 | sí | 12 |
| dulce | mensual | SARIMA-sel | 2025 | 12 | 0 | sí | 12 |
| dulce | mensual | SARIMA-sel | agregado | 60 | 0 | sí | 60 |
| dulce | mensual | Ridge | 2021 | 12 | 0 | sí | 12 |
| dulce | mensual | Ridge | 2022 | 12 | 0 | sí | 12 |
| dulce | mensual | Ridge | 2023 | 12 | 0 | sí | 12 |
| dulce | mensual | Ridge | 2024 | 12 | 0 | sí | 12 |
| dulce | mensual | Ridge | 2025 | 12 | 0 | sí | 12 |
| dulce | mensual | Ridge | agregado | 60 | 0 | sí | 60 |
| dulce | mensual | ElasticNet | 2021 | 12 | 0 | sí | 12 |
| dulce | mensual | ElasticNet | 2022 | 12 | 0 | sí | 12 |
| dulce | mensual | ElasticNet | 2023 | 12 | 0 | sí | 12 |
| dulce | mensual | ElasticNet | 2024 | 12 | 0 | sí | 12 |
| dulce | mensual | ElasticNet | 2025 | 12 | 0 | sí | 12 |
| dulce | mensual | ElasticNet | agregado | 60 | 0 | sí | 60 |
| dulce | mensual | XGB-37 | 2021 | 12 | 0 | sí | 12 |
| dulce | mensual | XGB-37 | 2022 | 12 | 0 | sí | 12 |
| dulce | mensual | XGB-37 | 2023 | 12 | 0 | sí | 12 |
| dulce | mensual | XGB-37 | 2024 | 12 | 0 | sí | 12 |
| dulce | mensual | XGB-37 | 2025 | 12 | 0 | sí | 12 |
| dulce | mensual | XGB-37 | agregado | 60 | 0 | sí | 60 |
| dulce | mensual | GC3 | 2021 | 12 | 0 | sí | 12 |
| dulce | mensual | GC3 | 2022 | 12 | 0 | sí | 12 |
| dulce | mensual | GC3 | 2023 | 12 | 0 | sí | 12 |
| dulce | mensual | GC3 | 2024 | 12 | 0 | sí | 12 |
| dulce | mensual | GC3 | 2025 | 12 | 0 | sí | 12 |
| dulce | mensual | GC3 | agregado | 60 | 0 | sí | 60 |
| dulce | mensual | GE | 2021 | 12 | 0 | sí | 12 |
| dulce | mensual | GE | 2022 | 12 | 0 | sí | 12 |
| dulce | mensual | GE | 2023 | 12 | 0 | sí | 12 |
| dulce | mensual | GE | 2024 | 12 | 0 | sí | 12 |
| dulce | mensual | GE | 2025 | 12 | 0 | sí | 12 |
| dulce | mensual | GE | agregado | 60 | 0 | sí | 60 |
| dulce | interanual | Naive | 2021 | 12 | 0 | sí | 12 |
| dulce | interanual | Naive | 2022 | 12 | 0 | sí | 12 |
| dulce | interanual | Naive | 2023 | 12 | 0 | sí | 12 |
| dulce | interanual | Naive | 2024 | 12 | 0 | sí | 12 |
| dulce | interanual | Naive | 2025 | 12 | 0 | sí | 12 |
| dulce | interanual | Naive | agregado | 60 | 0 | sí | 60 |
| dulce | interanual | Seasonal Naive | 2021 | 12 | 0 | sí | 12 |
| dulce | interanual | Seasonal Naive | 2022 | 12 | 0 | sí | 12 |
| dulce | interanual | Seasonal Naive | 2023 | 12 | 0 | sí | 12 |
| dulce | interanual | Seasonal Naive | 2024 | 12 | 0 | sí | 12 |
| dulce | interanual | Seasonal Naive | 2025 | 12 | 0 | sí | 12 |
| dulce | interanual | Seasonal Naive | agregado | 60 | 0 | sí | 60 |
| dulce | interanual | Chronos | 2021 | 12 | 0 | sí | 12 |
| dulce | interanual | Chronos | 2022 | 12 | 0 | sí | 12 |
| dulce | interanual | Chronos | 2023 | 12 | 0 | sí | 12 |
| dulce | interanual | Chronos | 2024 | 12 | 0 | sí | 12 |
| dulce | interanual | Chronos | 2025 | 12 | 0 | sí | 12 |
| dulce | interanual | Chronos | agregado | 60 | 0 | sí | 60 |
| dulce | interanual | SARIMA | 2021 | 12 | 0 | sí | 12 |
| dulce | interanual | SARIMA | 2022 | 12 | 0 | sí | 12 |
| dulce | interanual | SARIMA | 2023 | 12 | 0 | sí | 12 |
| dulce | interanual | SARIMA | 2024 | 12 | 0 | sí | 12 |
| dulce | interanual | SARIMA | 2025 | 12 | 0 | sí | 12 |
| dulce | interanual | SARIMA | agregado | 60 | 0 | sí | 60 |
| dulce | interanual | SARIMA-sel | 2021 | 12 | 0 | sí | 12 |
| dulce | interanual | SARIMA-sel | 2022 | 12 | 0 | sí | 12 |
| dulce | interanual | SARIMA-sel | 2023 | 12 | 0 | sí | 12 |
| dulce | interanual | SARIMA-sel | 2024 | 12 | 0 | sí | 12 |
| dulce | interanual | SARIMA-sel | 2025 | 12 | 0 | sí | 12 |
| dulce | interanual | SARIMA-sel | agregado | 60 | 0 | sí | 60 |
| dulce | interanual | Ridge | 2021 | 12 | 0 | sí | 12 |
| dulce | interanual | Ridge | 2022 | 12 | 0 | sí | 12 |
| dulce | interanual | Ridge | 2023 | 12 | 0 | sí | 12 |
| dulce | interanual | Ridge | 2024 | 12 | 0 | sí | 12 |
| dulce | interanual | Ridge | 2025 | 12 | 0 | sí | 12 |
| dulce | interanual | Ridge | agregado | 60 | 0 | sí | 60 |
| dulce | interanual | ElasticNet | 2021 | 12 | 0 | sí | 12 |
| dulce | interanual | ElasticNet | 2022 | 12 | 0 | sí | 12 |
| dulce | interanual | ElasticNet | 2023 | 12 | 0 | sí | 12 |
| dulce | interanual | ElasticNet | 2024 | 12 | 0 | sí | 12 |
| dulce | interanual | ElasticNet | 2025 | 12 | 0 | sí | 12 |
| dulce | interanual | ElasticNet | agregado | 60 | 0 | sí | 60 |
| dulce | interanual | XGB-37 | 2021 | 12 | 0 | sí | 12 |
| dulce | interanual | XGB-37 | 2022 | 12 | 0 | sí | 12 |
| dulce | interanual | XGB-37 | 2023 | 12 | 0 | sí | 12 |
| dulce | interanual | XGB-37 | 2024 | 12 | 0 | sí | 12 |
| dulce | interanual | XGB-37 | 2025 | 12 | 0 | sí | 12 |
| dulce | interanual | XGB-37 | agregado | 60 | 0 | sí | 60 |
| dulce | interanual | GC3 | 2021 | 12 | 0 | sí | 12 |
| dulce | interanual | GC3 | 2022 | 12 | 0 | sí | 12 |
| dulce | interanual | GC3 | 2023 | 12 | 0 | sí | 12 |
| dulce | interanual | GC3 | 2024 | 12 | 0 | sí | 12 |
| dulce | interanual | GC3 | 2025 | 12 | 0 | sí | 12 |
| dulce | interanual | GC3 | agregado | 60 | 0 | sí | 60 |
| dulce | interanual | GE | 2021 | 12 | 0 | sí | 12 |
| dulce | interanual | GE | 2022 | 12 | 0 | sí | 12 |
| dulce | interanual | GE | 2023 | 12 | 0 | sí | 12 |
| dulce | interanual | GE | 2024 | 12 | 0 | sí | 12 |
| dulce | interanual | GE | 2025 | 12 | 0 | sí | 12 |
| dulce | interanual | GE | agregado | 60 | 0 | sí | 60 |
