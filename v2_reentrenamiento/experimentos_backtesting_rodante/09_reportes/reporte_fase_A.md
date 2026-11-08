# Reporte — Fase 0 (cierre) y Fase A

**Fecha:** 2026-10-25. **Estado:** PAUSA, esperando aprobación del plan.

## Hecho
- Se creó el árbol aprobado: 46 `README.md` y `.gitignore` local (pesos `.keras`, `.joblib`, `.pkl`, `.ubj` y `model.xgboost.json` excluidos de git).
- Plan completo: `00_plan/plan_fase_A.md`.
- Borrador del preregistro: `00_plan/borrador_preregistro.md` (no escrito en DECISIONES).
- Mapa de evidencia: `00_plan/mapa_evidencia.md`.
- No se ejecutó ningún entrenamiento ni evaluación. Solo un cálculo de solo lectura sobre los pesos geográficos para medir la fuga (plan, A2-f).

## Verificaciones de código (anexo)

### (a) Ponderación de NASA e INDECI a escala nacional
- **Por superficie, no por producción:** `verde_actual_ha` (D14), en `v2_reentrenamiento/src/features/pesos_geograficos.py:5-7`.
- **Pesos fijos:** media de la superficie en TRAIN 2016-01..2023-12 (D15, l. 8-9 y 30-33), con w_p = área media_p / Σ área media (l. 87-95).
- **Ventana usada:** `00_pesos_geograficos.ipynb` celda 2, `VentanaTrain(2016,1,2023,12)`.
- **Aplicación:** `02_fusion_dataset_maestro.ipynb` celda 6, con `AgregadorEspacial`: C_t = Σ_p w_p·C_{p,t}, renormalizado por la masa de peso presente cada mes (`agregacion_espacial.py:57-69`).
- **Vectores independientes por cultivo** (D16).
- **NLP no se pondera geográficamente:** es una serie nacional mensual (`02_fusion` celda 8).
- **Consecuencia para el backtest:** los pesos usan datos hasta 2023, así que hay fuga en las ventanas ≤2024. La fuga es pequeña en Sutil y relevante en Dulce para Y ≤ 2021 (decisión DA3).

### (b) Orden SARIMA-Sutil
- **Rejilla de exp_002:** 576 combinaciones; top-5 por AIC en train; se elige por MAE de validación (`02_gc1_sarima_prophet.ipynb` celdas 7 y 9). Resultado: (1,1,3)(2,1,0,12).
- **Adopción de exp_002b** en `02b_diagnostico_sarima_sutil.ipynb`:
  - celda 0: el notebook se abre citando las métricas de TEST de exp_002 como motivo;
  - celdas 14-15: comparan "ganador" contra "simple" **en test 2025** (12 031.69 frente a 3 638.14);
  - celda 20: se decide registrar el simple (1,1,1)(1,1,0,12).
- **Sí, el test influyó.** El `config.yaml` de exp_002b dice "no hubo búsqueda sobre val ni sobre test", pero la adopción fue posterior a ver el test.
- **Atenuante:** el simple también gana en validación (4 824 frente a 8 440).
- SARIMA rolling hereda ese orden (D49, `DECISIONES_METODOLOGICAS.md:1500-1520`).

### (c) Parámetros y variables por rama

| Modelo | Parámetros | Rama A | Rama B | Total de inputs |
|---|---:|---|---|---:|
| GC3 | 6 273 | 4: producción t y lags 1/3/6 | 33: mes_sin, mes_cos, t_index + 5 NASA × 3 lags + 5 INDECI × 3 lags | 37 |
| GE | 6 657 | 4 | 39: las 33 de GC3 + 6 NLP (avg_sentiment y n_noticias × lags 1/3/6) | 43 |

- Parámetros: `v2_reentrenamiento/src/models/dual_lstm_attention.py:28-31`.
- Rama A: `features_gc3_ge.py:70-76`. Rama B de GC3: l. 79-80 (constantes en l. 12-29). Rama B de GE: l. 83-84 (NLP en l. 21-28).
- Configuración (`dual_lstm_attention.py:19-26`): lookback 6, LSTM 16, atención 16, Dense (16, 8), dropout 0.2.

### (d) Código que regenere `limon_*_nacional_mensual.csv` desde el xlsx
- **No existe en el repo.** La búsqueda en todo el repo solo encontró consumidores:
  - `00_pesos_geograficos` celda 4;
  - `02_fusion_dataset_maestro` celda 8;
  - `09_resumen_fase1` celda 3;
  - `resultados_v2_final/figuras_articulo/auditoria/generar_mapa_peru_en.py`.
- Los CSV de distrito, provincia y nación se subieron directamente en el commit `ee5f9be` (2026-09-03), sin el código que los genera.
- D21 lo declara (`DECISIONES_METODOLOGICAS.md:568`).
- El historial de git no muestra ningún script borrado que los generara.
- **No verificado:** si existió en una carpeta temporal fuera del repo.

## Resumen en lenguaje simple

**Qué hice.** Creé las carpetas y escribí el plan sin entrenar nada. Revisé el código oficial, v3, v4 y v5, y respondí las cuatro verificaciones.

**Qué encontré.**
- Se puede reutilizar el código oficial, pero hay que reescribir tres piezas pequeñas con fechas fijas. Una prueba exigirá que, en 2025, el resultado sea idéntico al oficial.
- 2018–2020 no tienen datos suficientes para los modelos entrenados.
- Con 2021–2025 quedan 10 meses de shock en Sutil y 15 en Dulce.
- v5 tiene una fuga: sus LSTM usan el año de test para decidir cuándo parar el entrenamiento.
- v3, v4 y v5 usan tres fórmulas distintas para Δs.
- Los pesos geográficos oficiales usan datos hasta 2023, lo que es fuga en ventanas anteriores: pequeña en Sutil y de hasta un 15 % en INDECI-Dulce.
- El orden de SARIMA-Sutil se adoptó después de ver el test 2025.
- No existe el código que crea las series nacionales desde el Excel.

**Problemas y cómo los resolví.** Ninguno bloqueante. Cada punto ambiguo quedó como decisión DA1–DA7, sin resolverlo por mi cuenta.

**Por qué cada decisión recomendada.**
- DA1(a): reproduce el protocolo oficial y permite comprobarlo en 2025.
- DA2 (36 meses): tres ciclos estacionales.
- DA3(a): elimina la fuga de los pesos.
- DA4(a): respeta los hiperparámetros congelados.
- DA5(a): un denominador estable.
- DA7(a): bootstrap simple y pareado.

**Qué no es confiable.**
- Las métricas de shock de Sutil, con solo 10 meses en total.
- Las ventanas 2021 y 2024 de Sutil, que no tienen shocks P75.
- Cualquier conclusión con un Diebold-Mariano restringido a shocks, por su baja potencia.

**No verificado.**
- La duración de SARIMA, Ridge, ElasticNet, el bootstrap y las figuras (se medirá en la Fase B).
- Si la limpieza de INDECI/NASA imputó con datos de todo el periodo.
- Si Chronos es determinista.

**Qué necesita tu aprobación.** DA1–DA7, la definición de P0 con ≥ 0 y que la robustez se juzgue solo con los 4 umbrales mensuales.
