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
