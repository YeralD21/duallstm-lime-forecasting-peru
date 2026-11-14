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

---

# Día 2 (T5–T10)

Informe: [`INFORME_DIA2.md`](INFORME_DIA2.md). Mismas reglas que el Día 1: todo es posterior al protocolo y no
modifica el ranking principal, y no se toca ningún archivo congelado ni publicado.

## Scripts nuevos

```
scripts/
  r2eval.py                  evaluación común (bootstrap, DM-HLN, ranking y regla 3 de 4, como 08_metricas.py)
  t5_respaldo_sarima_sel.py  T5: regla de respaldo de SARIMA-sel por MAE de validación (general; aplicada a E1)
  t6_t7_tabulares.py         T6 (E5: y_(T-12) en Ridge, ElasticNet, XGB-37) y T7.1 (ablación por bloques)
  t7_sarimax.py              T7.2: SARIMAX con exógenas rezagadas frente a SARIMA
  t8_ex_ante.py              T8: meses de cambio grande definidos ex ante; meses de El Niño costero (IGP/ENFEN)
  t9_h2.py                   T9: horizonte h = 2
  t10_crps.py                T10: CRPS y CRPS ponderado por umbral (Chronos, SARIMA, SARIMA-sel)
datos_externos/igp_icen/     ICEN y lista de eventos El Niño/La Niña costeros del IGP (ver FUENTE.md)
resultados/unidades_d2/      predicciones nuevas (SARIMA-sel-Y1-R, tabulares h=1, SARIMAX, h=2)
resultados/T5_*..T10_*       tablas en CSV; tablas_T5.md ... tablas_T10.md (generadas; no editar a mano)
```

`r2lib.py` gana funciones nuevas: `elegir_con_respaldo`, `correr_tabular`, `pares_h`, `ets_h`, `theta_h` y
`ChronosFijo`. Las funciones del Día 1 conservan su salida byte a byte (comprobado con los hashes de `resultados/`).

## Controles (el script se detiene si fallan)

- **T5:** la regla no cambia ningún SARIMA-sel del protocolo original (todos convergen). Sin respaldo, cada unidad de E1
  reproduce la publicada.
- **T6/T7.1:** `correr_tabular`, con los 37 predictores, reproduce las predicciones congeladas de Ridge, ElasticNet y
  XGB-37 (10 semillas) en las 10 unidades (diferencia ≤ 10⁻⁶ t).
- **T9:** cada modelo, corrido con h = 1 por el mismo código, reproduce sus predicciones congeladas (o las de T1).
  - Tolerancia general: el máximo de 10⁻⁶ t y 10⁻⁹·|y|, porque las unidades R2 se guardan con 10 cifras
    significativas.
  - Chronos: 2 ULP de float32, porque trabaja en float32.
- **T10:** la mediana de Chronos y la media de SARIMA / SARIMA-sel reproducen las predicciones puntuales congeladas.

## Decisiones

1. **T5. Regla:** si el orden elegido por MAE de validación entre los 5 de menor AIC no converge en el ajuste final, se
   usa el siguiente con menor MAE de validación entre los que convergen (empate: AIC, luego orden de la rejilla). Es
   una función general (`r2lib.elegir_con_respaldo`) que recibe el "ajuste final" del protocolo:
   - original: el ajuste en train con maxiter 500;
   - E1: el reajuste con datos hasta Y−1.
2. **T6. E5:**
   - **Columna nueva:** `produccion_t_<c>_y12`. En la fila t, para el objetivo T = t+1, vale y_(T−12) = y_(t−11).
   - **Filas perdidas:** y_(T−12) solo existe desde el objetivo 2017-01, así que se pierden 5 pares de train
     (objetivos 2016-08..2016-12).
   - **Control "filas E5":** para separar ese efecto, se corre el modelo original con esas mismas filas.
   - **Igual que el protocolo:** misma búsqueda de alpha/l1 por MAE de validación, misma estandarización y
     parámetros XGB oficiales con semillas 0..9.
   - **XGB:** la columna nueva se escala con el `EscaladorVentana` del train, igual que las demás.
3. **T7.1. Conjuntos:** el orden de las columnas se eligió para que (c) sea exactamente E5. Así (c) reutiliza las
   predicciones de E5; XGB depende del orden por `colsample_bytree`. Ridge reelige alpha en cada conjunto.
4. **T7.2. SARIMAX (fijado ANTES de ver resultados; también en el docstring de `t7_sarimax.py`):**
   - **Rezagos:** para el objetivo T, x_(T−2), x_(T−4) y x_(T−7), los mismos que los tabulares (columnas lag1/lag3/lag6
     de la fila T−1).
   - **Versión principal:** "SARIMAX-PC", con 2 exógenas: la PC1 del clima y la PC1 de las emergencias. La PCA se ajusta
     solo con el train, y cada componente entra solo en el rezago 1.
   - **Versión secundaria:** "SARIMAX-30", con las 30 exógenas, marcada como sobreparametrizada (42–90 meses de train).
     Su train empieza en 2016-08.
   - **Órdenes y opciones:** los del SARIMA congelado. Ajuste único y append(refit=False).
5. **T8:**
   - **Umbrales:** se calculan con la historia hasta el origen (dic Y−1), como las máscaras del artículo (D-BR3).
   - **Definición B:** usa los pronósticos a 1 paso del SARIMA dentro del train, sin los 13 primeros meses
     (inicialización difusa con d + 12·D diferencias), y los de validación.
   - **Definición C (El Niño costero):** no es ex ante. Usa la lista oficial de eventos basada en el ICEN. No se
     usaron los comunicados de alerta del ENFEN.
6. **T9 (h = 2):**
   - **Modelos estadísticos y Chronos:** mismo ajuste; estado o contexto hasta t−2; pronóstico a 2 pasos.
   - **Tabulares:** estrategia directa (pares X_(t−2) → y_t, reentrenados con la misma búsqueda). `pares_h` verifica que
     cada par tenga exactamente 2 meses de separación.
   - **Seasonal Naive:** es igual que en h = 1.
   - **GC3 y GE:** quedan fuera.
7. **T10:**
   - **Representación común:** las tres distribuciones se representan con los mismos 9 cuantiles. Chronos da sus
     cuantiles nativos; SARIMA y SARIMA-sel, los de la normal de `get_forecast(1)`.
   - **CRPS:** CRPS_Q = (2/K) Σ pérdida de cuantil.
   - **twCRPS:** peso 1 si |z/y_(t−1) − 1| > u, con u el umbral P75 MoM de la ventana. Se aplica con la función de
     encadenamiento v(z) = min(z, r1) + max(z − r2, 0).
   - **Referencia:** se reporta también el CRPS exacto de la normal.
8. **Mejor modelo de cada cultivo (DM):** el de menor MAE en todos los meses entre los 10 del artículo: sutil Chronos,
   dulce SARIMA.
9. **Chronos (T9, T10):** se carga con la revisión fijada en `hiperparametros_congelados.json` (`r2lib.ChronosFijo`),
   igual que `12_revision_g7`, porque `lib/modelo_chronos.py` no pasa la revisión y sin red falla.
