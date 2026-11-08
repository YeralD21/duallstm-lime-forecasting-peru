# 06_metricas — tablas de la Fase D1

Generadas por `02_scripts/08_metricas.py` (y la comprobación de 2025, `02_scripts/tests/test_equivalencia_metricas_2025.py`) a partir de las predicciones congeladas de la Fase C. Todo en toneladas reales.
Reporte completo con todas las tablas en texto e índice de archivos: `09_reportes/reporte_fase_D1.md`.

| Carpeta | Contenido |
|---|---|
| `por_ventana/` | T05 (métricas por modelo × ventana × tipo × percentil de reporte, y vistas de MAE y MAE_shock P75); T20 (SARIMA-sel: orden, posición en AIC y los 5 candidatos); T21 (α y l1 de Ridge y ElasticNet) |
| `agregadas/` | T06 (agregadas 2021–2025 y 2023–2025 con IC bootstrap iid y por bloques); T08 (ranking, empates y robustez por MAE_shock y por MAE normal); T12 (Δs quitando un mes de shock); T13 (MAE por cuartiles y tercios de \|Δy/y\|); T16 (XGB-43 exploratorio); T17 (descriptivo 2018–2020) |
| `por_semilla/` | T07 (métricas por semilla y dispersión); T15 (diagnóstico de ajuste D-BR8 por corrida y mejor época) |
| `significancia/` | T09 (Diebold-Mariano-HLN por pares, global y solo shocks P75; con la columna `p_holm_exploratorio`, DESV-07); matrices sin ajustar y con Holm; resumen de Holm. MCS no calculado |
| `ablacion_nlp/` | T11 (GE − GC3 emparejado por semilla, por ventana y agregado, con IC) |
| `descripcion_series/` | T03 (descripción por partición); T04 (ACF, ADF y KPSS en TRAIN, nivel y Δ12) |
| `bootstrap/` | vacía: los intervalos bootstrap están en `agregadas/T06_agregadas_IC.csv` y `agregadas/T08_ranking_empates.csv` |
| `reproducibilidad/` | Fase B (Chronos v4, ElasticNet v3) y Fase D1 (`metricas_2025_vs_oficial*.csv/.json`: 2025 frente a `resultados_v2_final`) |
| `tablas_latex/` | un `.tex` (booktabs, redondeado) por cada vista; los CSV conservan la precisión completa |

Decisiones de implementación: `09_reportes/DESVIACIONES.md` (DESV-05, DESV-06 y DESV-07).
