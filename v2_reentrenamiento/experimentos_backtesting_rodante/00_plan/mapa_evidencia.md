# Mapa de evidencia

Cada tabla y figura que saldrá del experimento, con el script que la genera y de qué depende.
Estado: **plan** (nada generado todavía).

**Convenciones:**
- `{c}` = `sutil` | `dulce` (un archivo por cultivo); `{w}` = año de la ventana.
- Cada figura tendrá `.png` (300 dpi), `.pdf`, `.csv` con los números y `.txt` con el pie sugerido y una lectura de 2 líneas.
- Cada tabla tendrá `.csv` en su carpeta de `06_metricas/` y `.tex` más una nota `.md` en `06_metricas/tablas_latex/`.

## Etapas (scripts en `02_scripts/`)

| Script | Hace | Depende de |
|---|---|---|
| `00_verificar_entorno.py` | variables de entorno, semillas, SHA-256 de `src/`, datos y snapshot de Chronos; escribe `manifest.json` | — |
| `01_construir_ventanas.py` | ventanas, umbrales P0..P95 (mensual e interanual), pesos geográficos por ventana, denominador MASE → `03_ventanas/` | 00 |
| `02_features_por_ventana.py` | agregación NASA/INDECI con pesos de la ventana + `FeaturesTemporales` (en memoria; solo guarda hashes) | 01 |
| `03_modelos_sin_ajuste.py` | Naive, Seasonal Naive, Chronos → `05_predicciones/` | 01 |
| `04_sarima_rolling.py` | SARIMA por ventana | 01 |
| `05_lineales.py` | Ridge, ElasticNet | 02 |
| `06_xgb.py` | XGB-37 (y XGB-43 exploratorio) | 02 |
| `07_lstm.py` | GC3, GE (`history.csv` por semilla) | 02 |
| `08_metricas.py` | métricas, bootstrap, DM-HLN, ablación, descripción de series, tablas LaTeX | 03–07 |
| `09_barrido_umbral.py` | barrido P0..P95 mensual e interanual | 03–07, 01 |
| `10_figuras.py` | todas las figuras del backtesting | 08, 09 |
| `figuras_independientes/fi01..fi05_*.py` | figuras que no dependen del backtesting | artefactos v2 existentes |
| `run_all.py` | ejecuta 00→10 y las pruebas de `tests/` | todo |
| `tests/test_fuga.py`, `tests/test_p0.py`, `tests/test_equivalencia_2025.py` | fuga (a–f), Δs(P0)=0, reproducción del split/scaler/pesos oficiales | 01–07 |

## Tablas

| ID | Contenido | Carpeta (CSV) | Script |
|---|---|---|---|
| T01 | Inventario de ventanas: fechas de train/val/test, n por modelo, "no aplica" | `03_ventanas/` | 01 |
| T02 | Umbrales y n_shock por ventana × percentil (mensual e interanual) | `03_ventanas/` | 01 |
| T03 | Descripción de las series por partición (media, DE, mín., máx., CV) | `06_metricas/descripcion_series/` | 08 |
| T04 | ACF (rezagos 1 y 12), ADF y KPSS (nivel y Δ12) en TRAIN | `06_metricas/descripcion_series/` | 08 |
| T05 | Métricas por modelo × ventana (MAE, RMSE, MASE, MAE normal/shock, Δs, razón) | `06_metricas/por_ventana/` | 08 |
| T06 | Métricas agregadas 2021–2025 con IC bootstrap (umbral principal P75) | `06_metricas/agregadas/` | 08 |
| T07 | Métricas por semilla (modelos estocásticos) | `06_metricas/por_semilla/` | 08 |
| T08 | Ranking y empates en P50/P60/P75/P90 + regla de robustez | `06_metricas/agregadas/` | 08 |
| T09 | Diebold-Mariano-HLN por pares (global y solo shocks) | `06_metricas/significancia/` | 08 |
| T10 | MCS (opcional) | `06_metricas/significancia/` | 08 |
| T11 | Ablación NLP GE − GC3 emparejada por semilla, por ventana y agregada | `06_metricas/ablacion_nlp/` | 08 |
| T12 | Δs quitando un mes de shock (por modelo y ventana) | `06_metricas/agregadas/` | 08 |
| T13 | MAE por cuartiles/tercios de \|Δy/y\| | `06_metricas/agregadas/` | 08 |
| T14 | Reproducibilidad: ElasticNet v3 y Chronos v4 frente a lo registrado | `06_metricas/reproducibilidad/` | Fase B |
| T15 | Diagnóstico de ajuste: MAE train/val, brecha, banderas de sobreajuste/subajuste, época de parada | `06_metricas/por_semilla/` | 08 |
| T16 | Exploratorios (XGB-43) en tabla aparte | `06_metricas/agregadas/` | 08 |
| T17 | Naive, Seasonal Naive y Chronos en 2018–2025 (descriptivo) | `06_metricas/agregadas/` | 08 |
| T18 | Parámetros y variables por rama de GC3/GE | `06_metricas/descripcion_series/` | fi02 |
| T19 | Sensibilidad DA2: T06, T08 y T09 repetidas solo con las ventanas 2023–2025 | `06_metricas/agregadas/` | 08 |
| T20 | SARIMA-sel: orden elegido por ventana y cultivo, **posición en AIC (1–5)**, AIC y MAE de validación de los 5 candidatos, órdenes fallidos, convergencia | `06_metricas/por_ventana/` | 04 |
| T21 | Ridge/ElasticNet: α (y l1) elegidos por ventana y cultivo con su MAE de validación; control 2025 frente a los valores de v3 | `06_metricas/por_ventana/` | 05 |

**Modelos (enmienda DA9):** SARIMA-sel entra en todas las tablas y figuras de comparación junto al SARIMA congelado, con color propio (`#F0E442`).
**Fase B (hecho):** T14 y las verificaciones están en `06_metricas/reproducibilidad/` y `10_logs/verificaciones/`.

## Figuras

| Fig | Archivo base | Carpeta | Script | Datos |
|---|---|---|---|---|
| 01 | `fig01_loss_curves_{gc3,ge}_{c}` | `diagnostico_ajuste/` | 10 | `history.csv` (media ± banda entre semillas; un panel por ventana) |
| 02 | `fig02_train_val_gap_{c}` | `diagnostico_ajuste/` | 10 | T15 |
| 03 | `fig03_early_stopping_epoch_{c}` | `diagnostico_ajuste/` | 10 | T15 |
| 04 | `fig04_delta_s_vs_percentile_{c}` | `sensibilidad_umbral/` | 10 | 07 mensual |
| 05 | `fig05_mae_shock_vs_percentile_{c}` | `sensibilidad_umbral/` | 10 | 07 |
| 06 | `fig06_ratio_shock_normal_vs_percentile_{c}` | `sensibilidad_umbral/` | 10 | 07 |
| 07 | `fig07_rank_heatmap_model_percentile_{c}` | `sensibilidad_umbral/` | 10 | 07 |
| 08 | `fig08_rank_bump_chart_{c}` | `sensibilidad_umbral/` | 10 | 07 |
| 09 | `fig09_n_shock_vs_percentile_{c}` | `sensibilidad_umbral/` | 10 | T02 |
| 10 | `fig10_n_shock_heatmap_window_percentile_{c}` | `sensibilidad_umbral/` | 10 | T02 |
| 11 | `fig11_bootstrap_ci_mae_shock_report_points_{c}` | `sensibilidad_umbral/` | 10 | T06/T08 |
| 12 | `fig12_yoy_vs_mom_threshold_{c}` | `sensibilidad_umbral/` | 10 | 07 mensual + interanual |
| 13 | `fig13_mae_normal_vs_shock_bars_{c}` | `comparacion_modelos/` | 10 | T06 |
| 14 | `fig14_mae_shock_heatmap_model_window_{c}` | `comparacion_modelos/` | 10 | T05 |
| 15 | `fig15_seed_boxplots_{c}` | `comparacion_modelos/` | 10 | T07 |
| 16 | `fig16_mae_by_change_quartile_{c}` | `comparacion_modelos/` | 10 | T13 |
| 17 | `fig17_leave_one_shock_out_delta_s_{c}` | `comparacion_modelos/` | 10 | T12 |
| 18 | `fig18_nlp_ablation_paired_{c}` | `comparacion_modelos/` | 10 | T11 |
| 19 | `fig19_dm_pvalue_matrix_{c}` | `comparacion_modelos/` | 10 | T09 |
| 20 | `fig20_real_vs_pred_{w}_{c}` (una por ventana) | `predicciones/` | 10 | `05_predicciones/` |
| 21 | `fig21_abs_error_monthly_{c}` | `errores/` | 10 | `05_predicciones/` |
| 22 | `fig22_residual_histogram_{c}` | `errores/` | 10 | `05_predicciones/` |
| 23 | `fig23_residual_acf_{c}` | `errores/` | 10 | `05_predicciones/` |
| 24 | `fig24_series_with_shocks_{c}` | `figuras_independientes/` | fi01 | `master_dataset_{c}_v2.csv` + T02 |
| 25 | `fig25_architecture_dual_lstm` | `figuras_independientes/` | fi02 | `dual_lstm_attention.py` (esquema dibujado con matplotlib; sin graphviz) |
| 26 | `fig26_shap_group_importance_{c}` | `figuras_independientes/` | fi03 | `resultados_v2_final/shap/interpretacion/tabla_grupos_completa.csv` |
| 27 | `fig27_shap_top_variables_{c}` | `figuras_independientes/` | fi04 | `resultados_v2_final/shap/official_test_2025/{c}/*/seed_variability_all_aggregates.json` |
| 28 | `fig28_test2025_trajectories_{c}` | `figuras_independientes/` | fi05 | predicciones oficiales de test 2025 (v2) |

**Notas:**
- Las figuras 26–28 usan artefactos oficiales de TEST 2025, no del backtesting; su pie lo dirá.
- `paper_mdpi/` solo recibe la selección que apruebes.
