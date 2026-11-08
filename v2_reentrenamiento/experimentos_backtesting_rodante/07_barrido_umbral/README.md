# 07_barrido_umbral — barrido de umbral de shock (Fase D1)

Generado por `02_scripts/09_barrido_umbral.py` sobre las predicciones congeladas (sin reentrenar). Percentiles P0, P10..P95, mensual e interanual, ventanas 2021–2025; el umbral de cada ventana se calcula con la historia hasta su origen (D-BR4).

| Archivo | Contenido |
|---|---|
| `mensual/barrido_por_modelo.csv`, `interanual/barrido_por_modelo.csv` | por cultivo, percentil y modelo: n_shock agregado, MAE_shock, MAE normal, Δs, razón, posición, "primero" (empate = IC 95 % iid de la diferencia con el mejor contiene 0) |
| `mensual/n_shock_por_ventana.csv`, `interanual/n_shock_por_ventana.csv` | n_shock por ventana y percentil; `informativa` = al menos 2 shocks |
| `mensual/T_barrido_*.csv`, `interanual/T_barrido_*.csv` | vistas: posiciones, Δs y n_shock por percentil |
| `estabilizacion.csv`, `T_barrido_estabilizacion.csv` | percentil desde el cual el primer lugar no cambia y desde el cual todos empatan |
| `comprobacion_P0.csv`, `comprobacion_P0.json`, `T_comprobacion_P0.csv` | P0 con datos reales: Δs = 0 exacto en las 240 comprobaciones |

Las vistas tienen su `.tex` en `06_metricas/tablas_latex/`. Todas las tablas en texto: `09_reportes/reporte_fase_D1.md`.
