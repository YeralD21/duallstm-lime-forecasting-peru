# 13_revision_r2 — Segunda ronda de revisión (Día 1)

Análisis pedidos por el revisor en la segunda ronda de observaciones (manuscrito del 13-nov-2026). **Todo lo de esta
carpeta es posterior al protocolo**: se reporta como robustez o diagnóstico, con la lógica de la Sec. 2.7 y de E1–E4
(`12_revision_g7/`), y **no modifica el ranking principal** de 10 modelos. No se modificó ningún archivo registrado en
`01_configuracion/hashes_congelados.json` ni ninguna salida publicada: los scripts solo leen `03_ventanas/`,
`04_modelos/`, `05_predicciones/`, `06_metricas/`, `08_graficos/`, `12_revision_g7/` y `data/interim/`, y escriben solo
en `13_revision_r2/resultados/`.

Informe: [`INFORME_DIA1.md`](INFORME_DIA1.md).

## Estructura

```
scripts/
  r2lib.py               ETS y Theta con el esquema de ajuste y actualización de SARIMA (lib/modelos_series.py)
  t1_ets_theta.py        T1: ETS y Theta, ventanas 2021-2025, dos cultivos -> resultados/unidades/{ETS,Theta}/
  t1_t2_evaluar.py       T1: métricas, IC, DM-HLN y ranking con 12 modelos; T2: ranking solo en 2025
  t3_sarima.py           T3: constante del SARIMA de sutil, sensibilidad sin constante, regla de respaldo de SARIMA-sel
  t4_verificaciones.py   T4: rezagos de los predictores, contenido de fig20, Seasonal Naive en dulce
resultados/
  unidades/              predicciones (val y test) e info.json por modelo, cultivo y ventana; rejilla_ets.csv
  T1_*.csv, T2_*.csv, T3_*.csv, T4_*.csv, T3_resumen.json, T4_resumen.json
  tablas_T1_T2.md        tablas de T1 y T2 en markdown (generadas; no editar a mano)
```

## Ejecución

Los cuatro scripts son pasos de `reproduce.py` (después de los existentes) y también se pueden correr solos, en este
orden, con el venv de la raíz:

```bash
venv\Scripts\python.exe v2_reentrenamiento\experimentos_backtesting_rodante\13_revision_r2\scripts\t1_ets_theta.py
venv\Scripts\python.exe v2_reentrenamiento\experimentos_backtesting_rodante\13_revision_r2\scripts\t1_t2_evaluar.py
venv\Scripts\python.exe v2_reentrenamiento\experimentos_backtesting_rodante\13_revision_r2\scripts\t3_sarima.py
venv\Scripts\python.exe v2_reentrenamiento\experimentos_backtesting_rodante\13_revision_r2\scripts\t4_verificaciones.py
```

No hace falta ninguna librería nueva (statsmodels 0.14.6 ya está en `requirements.txt`), así que no hay
`requirements-r2.txt`. Duración total: menos de 2 minutos en CPU.

## Controles incluidos en el código

- `t1_t2_evaluar.py` recalcula las métricas y el ranking de los 10 modelos originales con los mismos índices bootstrap
  y **exige** que coincidan con `06_metricas/agregadas/T06_agregadas_IC.csv` (440 celdas) y `T08_ranking_empates.csv`
  (160 filas: posición y primero/empate). Así, ETS y Theta se evalúan con el procedimiento exacto del artículo.
- `r2lib.py` verifica que la actualización con parámetros fijos reproduce, en el origen, el pronóstico de statsmodels
  (ETS: `smooth(params)` = `forecast(1)` del ajuste; Theta: recursión manual = `ThetaModelResults.forecast(1)`), y
  que los parámetros no cambian durante la validación y el test.
- `t3_sarima.py` exige que el SARIMA con constante, recalculado, reproduzca las predicciones congeladas, y que el
  reajuste del orden no convergente de E1 reproduzca la unidad publicada de `12_revision_g7`.
- `t4_verificaciones.py` comprueba con los datos (no solo con los nombres de columna) cada rezago declarado.

## ETS y Theta: protocolo y diferencias inevitables con SARIMA-sel

Igual que SARIMA / SARIMA-sel (`lib/modelos_series.py`): train 2016-07..dic Y−2, validación Y−1, test Y; parámetros
estimados una sola vez en train; en validación y test, pronóstico a 1 paso y luego el valor real entra como estado
**sin reestimar** (equivalente a `append(refit=False)`).

1. **Selección de ETS.** Por AICc en train entre 12 especificaciones (error A/M × tendencia N/A/Ad × estacionalidad
   A/M, período 12), como se pidió. SARIMA-sel, en cambio, toma los 5 mejores por AIC y elige por MAE de validación.
   En ETS la validación solo actualiza el estado. Las 12 especificaciones son válidas porque las series son
   positivas.
2. **Actualización de ETS.** `ETSModel` no tiene `append`. Se usa `ETSModel(y_hasta_t−1).smooth(params_train)`, que
   filtra la serie extendida con los mismos parámetros, incluidos los estados iniciales estimados. Es la misma
   operación que `append(refit=False)`.
3. **Theta.** `ThetaModel(period=12)` con sus opciones por defecto (test de estacionalidad, descomposición
   multiplicativa si procede, θ = 2, `fit(use_mle=False)`). No tiene `append`: la actualización con b0, α y factores
   estacionales fijos se programa con las fórmulas de `statsmodels/tsa/forecasting/theta.py`, y en el origen
   reproduce `forecast(1)`. El test de estacionalidad de statsmodels se aplica solo con el train, y en una ventana no
   rechaza la ausencia de estacionalidad (ver `info.json`). En esa ventana Theta no desestacionaliza: es el
   comportamiento por defecto, no se forzó.
4. **No convergencia.** Se registra (`info.json`, `rejilla_ets.csv`), igual que en SARIMA. No se fuerza otro modelo.
