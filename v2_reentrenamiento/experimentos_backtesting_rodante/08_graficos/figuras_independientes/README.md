Figuras de la Fase D3 que no salen de las métricas del backtesting. Las genera `02_scripts/11_figuras_d3.py` solo a partir de datos ya guardados; el índice está en `indice_figuras_d3.csv`.

- `fig24_series_with_shocks_{sutil,dulce}`: serie nacional 2016–2025 con los meses de shock P75 mensual de cada ventana de test 2021–2025.
- `fig25_architecture_dual_lstm`: arquitectura de GC3 y GE desde el código oficial v2 (parámetros leídos del modelo Keras).
- `fig29_study_area_map`: provincias productoras, un panel por cultivar (% sobre el total de cada cultivar). Geometría en `11_geometria_externa/`.
- `fig30_rolling_origin_scheme`: esquema de ventanas 2018–2025 desde `03_ventanas/ventanas_viabilidad.csv` y D-BR1.
- `TS1_provinces`: tabla suplementaria de las 109 provincias (CSV, LaTeX y pie).

Pendientes del mapa de evidencia: fig26–fig28 (SHAP y trayectorias del test oficial 2025) no se han generado. Estado de la Fase D3: pendiente de aprobación (DESV-09).
