# Revisión G7 — Fase 2 (solo lectura)

- **Fecha:** 2026-10-31. **Rama:** `revision-experimento-v2`.
- **Alcance:** no se reentrenó nada ni se modificó ningún archivo existente. Solo se crearon los archivos de esta carpeta.
- **Script:** `g7_fase2.py`, en esta misma carpeta. Se ejecuta con `venv/Scripts/python.exe -I g7_fase2.py <raiz_repo>` (unos 40 s; statsmodels 0.14.6).

**Fuentes:**
- Errores: `05_predicciones/errores_test_promediados_semillas.csv`, columna `ae` (media mensual sobre las 10 semillas en XGB-37, GC3, GE y XGB-43).
- Serie: `v2_reentrenamiento/data/interim/limon_{c}_nacional_mensual.csv`.
- Denominador MASE: `03_ventanas/denominador_mase_por_ventana.csv`.
- Provincias: `limon_{c}_provincia.csv`.
- Excel: `v2_reentrenamiento/data/raw/midagri/sisagri_2015_2026.xlsx`, leído en streaming sin escribir nada.

**Controles (pasan los tres):**
1. MoM e YoY recalculados son **idénticos** a `03_ventanas/umbrales_y_mascaras.csv`: 0 diferencias en meses y umbrales, en 2 cultivos × 5 ventanas × 4 percentiles × 2 definiciones.
2. El bootstrap "primero o empatado" (copia de `lib/evaluacion.py:112-158`) reproduce `06_metricas/agregadas/T08_ranking_empates.csv` (MoM, principal, iid, shock): **0 de 80** banderas distintas; diferencia máxima en los IC de 4×10⁻⁷.
3. Las filas de limón del Excel (2016–2025) coinciden con `limon_{c}_distrito_crudo.csv`: dulce 9,568 = 9,568 filas y 48,994.080 t; sutil 57,445 = 57,445 filas y 3,032,377.426 t.

**Archivos:**

| Bloque | CSV |
|---|---|
| 1 | `00_umbrales_P75_y_control_STL.csv`, `01_definiciones_alternativas_metricas.csv` (640 filas: 2 cultivos × 2 pools × 4 definiciones × 4 percentiles × 10 modelos), `01b_distribucion_mes_calendario.csv`, `01c_sutil_2023_capturados.csv`, `01d_robustez_primero_o_empatado.csv`, `01e_calendario_P75_todas_definiciones.csv` |
| 2 | `02_evento_2023.csv` |
| 3 | `03a_cinco_provincias_dulce_mensual_excel.csv`, `03a_cinco_provincias_por_mes_calendario.csv`, `03b_paneles_balanceados.csv`, `03b_calendario_MoM_P75_paneles.csv` |
| 4 | `04_inicio_vs_continuacion.csv` |

## 1. Definiciones alternativas de shock

**Definiciones.** Para cada ventana Y, el umbral es el percentil lineal de la historia hasta dic Y−1, y hay shock si r_t > umbral (comparación estricta, como en `lib/shocks.py:45-60`):

| Def. | r_t | Historia del umbral |
|---|---|---|
| a) MoM | \|y_t − y_{t−1}\| / y_{t−1} | 2016-02..origen |
| b) YoY | \|y_t − y_{t−12}\| / y_{t−12} | 2017-01..origen |
| c) STL | STL robusta ajustada en y[2016-01..origen] con `period=12, seasonal=13, robust=True` (resto por defecto: trend automático, low_pass = 13). En la historia, a_t = y_t − S_t con la estacionalidad in-sample. En el test, a_t = y_t − S_origen(mes), donde S_origen(m) es la estacionalidad del mes m en el año Y−1. r_t = \|a_t − a_{t−1}\| / a_{t−1}; el a de dic Y−1 es el de la historia | 2016-02..origen |
| d) 3M | \|y_t − y_{t−3}\| / y_{t−3} | 2016-04..origen |

La serie desestacionalizada es siempre positiva: mínimo 5,557 t en sutil y 327 t en dulce, en historia y test (`00_umbrales_P75_y_control_STL.csv`).

**Umbral P75 por ventana 2021→2025** (`00_umbrales_P75_y_control_STL.csv`):

| Cultivo | MoM | YoY | STL | 3M |
|---|---|---|---|---|
| Sutil | 25.9 → 23.2 % | 54.4 → 43.0 % | 16.4 → 14.3 % | 51.4 → 46.0 % |
| Dulce | 33.8 → 32.8 % | 9.2 → 8.7 % | 3.9 → 5.3 % | 59.4 % en todas |

En dulce 3M el umbral es idéntico en todas las ventanas. Es correcto: (n−1)·0.75 cae siempre en el mismo estadístico de orden, porque cada año suma 3 cambios por encima y 9 por debajo.

**1.1 Número de meses de shock, pool 2021–2025 (de 60)** (`01b_distribucion_mes_calendario.csv`)

| Cultivo | Def. | P50 | P60 | P75 | P90 |
|---|---|---|---|---|---|
| Sutil | MoM | 29 | 25 | 10 | 6 |
| Sutil | YoY | 25 | 18 | 10 | 4 |
| Sutil | STL | **43** | **35** | **20** | 5 |
| Sutil | 3M | 31 | 27 | 15 | 6 |
| Dulce | MoM | 28 | 23 | 15 | 5 |
| Dulce | YoY | 29 | 23 | 16 | 4 |
| Dulce | STL | **40** | **33** | **27** | 6 |
| Dulce | 3M | 27 | 18 | 15 | 5 |

**La STL no está calibrada.** Con P75 marca el 33 % (sutil) y el 45 % (dulce) de los meses, frente al 25 % nominal. La causa es que la STL in-sample absorbe parte del ruido de la historia, así que los cambios históricos son más pequeños que los del test, donde la estacionalidad está fijada al origen. MoM, YoY y 3M salen cerca del nominal.

**1.2 Distribución P75 por mes calendario, pool 2021–2025** (resto de percentiles en `01b`)

| Cultivo | Def. | E | F | M | A | M | J | J | A | S | O | N | D |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sutil | MoM | 2 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 2 | 2 |
| Sutil | YoY | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 0 | 0 |
| Sutil | STL | 4 | 0 | 1 | 0 | 1 | 3 | 3 | 2 | 1 | 1 | 3 | 1 |
| Sutil | 3M | 3 | 4 | 1 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 2 | 2 |
| Dulce | MoM | 4 | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| Dulce | YoY | 2 | 0 | 1 | 0 | 0 | 1 | 2 | 2 | 3 | 1 | 2 | 2 |
| Dulce | STL | 3 | 0 | 1 | 2 | 2 | 4 | 3 | 2 | 3 | 5 | 2 | 0 |
| Dulce | 3M | 0 | 5 | 5 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

En dulce, la 3M sigue capturando solo la subida de campaña (feb–abr, 15 de 15). La YoY y la STL reparten los shocks a lo largo del año.

**1.3 Sutil, cuántos meses de mar–dic de 2023 captura cada definición** (`01c_sutil_2023_capturados.csv`)

| Def. | P50 | P60 | P75 | P90 |
|---|---|---|---|---|
| MoM | 10 (todos) | 9 | 4 (ago, sep, nov, dic) | 3 |
| YoY | 7 (mar–sep) | 6 (abr–sep) | 2 (ago, sep) | 0 |
| STL | 7 | 6 | 4 (mar, jun, ago, nov) | 1 (nov) |
| 3M | 6 | 6 | 3 (ago, nov, dic) | 2 |

Con P75, solo la STL marca **marzo de 2023**, el primer mes de la caída. La YoY necesita P50–P60 para cubrir la caída de mar/abr–sep.

**1.4 Métricas P75, pool 2021–2025** (`01_definiciones_alternativas_metricas.csv`)

Cada celda lista los modelos ordenados por MAE_shock (t). En **negrita**, los que son primeros o están empatados con el primero (IC95 bootstrap pareado de la diferencia con el mejor que contiene 0).

| Cultivo | Def. (n) | Orden por MAE_shock (t) | MAE_shock rel. SNaive: GC3 / GE | MASE_shock: mejor; SNaive; GC3; GE |
|---|---|---|---|---|
| Sutil | MoM (10) | **Chr 4,784**, **SSel 4,936**, **SN 5,034**, **SAR 5,131**, **X37 5,955**, **GC3 6,074**, GE 6,827, EN 8,154, Nv 8,506, Rdg 8,557 | 1.21 / 1.36 | 0.82; 0.86; 1.04; 1.17 |
| Sutil | YoY (10) | **Chr 1,864**, **Nv 3,172**, SAR 3,233, SSel 4,079, X37 4,816, Rdg 4,946, EN 5,404, GC3 9,166, GE 9,796, SN 12,508 | 0.73 / 0.78 | 0.33; 2.26; 1.65; 1.77 |
| Sutil | STL (20) | **Chr 3,626**, **X37 4,394**, **SN 4,761**, SAR 4,818, **GC3 4,944**, SSel 5,069, **GE 5,084**, Nv 5,183, EN 5,791, Rdg 5,845 | 1.04 / 1.07 | 0.61; 0.79; 0.85; 0.87 |
| Sutil | 3M (15) | **Chr 3,377**, **SSel 3,791**, **SAR 4,155**, Nv 5,134, SN 5,782, X37 6,098, EN 6,264, Rdg 6,584, GC3 8,238, GE 9,476 | 1.42 / 1.64 | 0.59; 1.00; 1.44; 1.65 |
| Dulce | MoM (15) | **SAR 14.0**, SSel 19.7, SN 24.5, Chr 48.2, GE 57.9, GC3 60.7, X37 65.8, EN 67.2, Rdg 69.7, Nv 131.6 | 2.48 / 2.36 | 0.54; 0.94; 2.38; 2.25 |
| Dulce | YoY (16) | **SAR 27.4**, **SSel 28.4**, **Chr 33.2**, X37 42.3, SN 42.4, GE 56.1, EN 57.3, GC3 58.2, Rdg 66.4, Nv 83.2 | 1.37 / 1.32 | 1.08; 1.67; 2.32; 2.25 |
| Dulce | STL (27) | **SSel 23.1**, **SAR 24.5**, **SN 25.7**, **Chr 29.4**, X37 42.7, EN 50.2, GC3 52.9, Rdg 53.0, GE 53.9, Nv 74.2 | 2.06 / 2.10 | 0.86; 0.97; 2.03; 2.06 |
| Dulce | 3M (15) | **SAR 15.9**, **SSel 17.5**, SN 27.5, Chr 45.1, EN 77.5, Rdg 77.8, X37 78.1, GE 85.9, GC3 86.1, Nv 118.9 | 3.13 / 3.13 | 0.61; 1.05; 3.37; 3.34 |

Abreviaturas: Chr = Chronos, SAR = SARIMA, SSel = SARIMA-sel, SN = Seasonal Naive, Nv = Naive, Rdg = Ridge, EN = ElasticNet, X37 = XGB-37.

La tabla completa, con MAE_normal, toneladas de más, rango e IC de cada modelo, umbral y pool, está en `01_definiciones_alternativas_metricas.csv`.
- **Sutil STL:** las "toneladas de más" de GC3 y GE salen negativas (−2,126 y −2,489 t), porque su MAE_normal (7,070 y 7,573) es el más alto de todos.
- **Sutil YoY:** el Seasonal Naive es el peor modelo en shock (12,508 t). Eso explica que el MAE_shock relativo de GC3/GE sea menor que 1 en ese caso.

**1.5 Pool 2023–2025, P75: primeros o empatados**

| Cultivo | MoM (n) | YoY (n) | STL (n) | 3M (n) |
|---|---|---|---|---|
| Sutil | Chr, SSel, SN, X37, GC3 (7) | Chr, Nv (10) | Chr, X37, SN, GC3, GE (11) | Chr, SSel, SAR (14) |
| Dulce | SSel, SAR (9) | SAR, SSel, Chr, X37 (12) | SSel, SN (17) | SSel, SAR (9) |

**1.6 Criterio robusto: primero o empatado en ≥ 3 de 4 umbrales** (`01d_robustez_primero_o_empatado.csv`)

| Cultivo | Pool | MoM | YoY | STL | 3M |
|---|---|---|---|---|---|
| Sutil | 2021–2025 | Chronos 4, SARIMA 3, SARIMA-sel 3 | Chronos 4, Naive 4 | Chronos 4 | Chronos 4, SARIMA-sel 4 |
| Sutil | 2023–2025 | Chronos 4, SARIMA-sel 4 | Chronos 4, Naive 4 | Chronos 3 | Chronos 4, SARIMA-sel 4, SARIMA 3 |
| Dulce | 2021–2025 | SARIMA 4 | Chronos 4, SARIMA 3, SARIMA-sel 3 | SARIMA-sel 4, SARIMA 3, SNaive 3 | SARIMA 4, SARIMA-sel 3 |
| Dulce | 2023–2025 | SARIMA 3, SARIMA-sel 3 | Chronos 4, SARIMA 3, SARIMA-sel 3 | SARIMA-sel 4 | SARIMA-sel 4, SARIMA 3 |

**GC3 y GE no son robustos con ninguna definición, cultivo ni pool.** Lo máximo que logran es 2 de 4, en sutil STL 2021–2025. XGB-37 llega como mucho a 2 de 4 (sutil MoM 2023–2025 y dulce YoY 2023–2025).

## 2. Evento 2023 (Niño costero / ciclón Yaku)

Fuente: `02_evento_2023.csv`. Error absoluto en toneladas; para los modelos con semilla, media sobre las semillas.

**Limón sutil**

| Modelo | Mar | Abr | May | Jun | Jul | Ago | Sep | Oct | Nov | Dic | MAE mar–dic 2023 | mar–dic 2022 | mar–dic 2024 | **MAE mar–may 2023** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 5,651 | 5,377 | 3,475 | 2,684 | 3,649 | 6,328 | 4,390 | 3,224 | 7,156 | 6,641 | 4,858 | 3,237 | 2,374 | 4,834 |
| Seasonal Naive | 10,804 | 11,182 | 13,446 | 6,990 | 7,720 | 13,548 | 10,114 | 3,727 | 131 | 748 | 7,841 | 3,194 | 10,579 | 11,811 |
| Chronos | 6,973 | 7,168 | 3,552 | 182 | 831 | 4,745 | 3,474 | 1,680 | 3,112 | 2,486 | 3,420 | 1,743 | 1,592 | 5,898 |
| SARIMA | 7,182 | 342 | 1,677 | 5,590 | 3,299 | 5,278 | 4,925 | 2,089 | 4,771 | 1,145 | 3,630 | 2,334 | 3,066 | **3,067** |
| SARIMA-sel | 7,293 | 2,041 | 6,177 | 2,514 | 3,118 | 10,307 | 2,737 | 24 | 3,482 | 107 | 3,780 | 2,103 | 3,312 | 5,170 |
| Ridge | 9,925 | 5,203 | 3,559 | 9,065 | 22,763 | 11,283 | 9,182 | 23,223 | 26,568 | 3,824 | 12,459 | 2,155 | 3,388 | 6,229 |
| ElasticNet | 9,542 | 5,651 | 5,056 | 10,376 | 22,054 | 12,224 | 8,540 | 20,397 | 23,080 | 3,382 | 12,030 | 2,017 | 3,700 | 6,750 |
| XGB-37 | **1,932** | 6,495 | 5,568 | 3,015 | 3,014 | 5,578 | 3,088 | 415 | 5,099 | 5,196 | 3,940 | 3,353 | 4,269 | 4,665 |
| GC3 | 2,893 | 7,271 | 8,883 | 7,822 | 8,329 | 12,128 | 6,602 | 4,179 | 3,126 | 7,359 | 6,859 | 3,952 | 7,549 | 6,349 |
| GE | 2,153 | 5,925 | 7,078 | 6,142 | 5,997 | 10,968 | 5,881 | 3,626 | 3,436 | 8,650 | 5,986 | 3,872 | 8,458 | 5,052 |
| XGB-43 (exploratorio) | **1,899** | 6,032 | 5,160 | 2,892 | 2,085 | 5,503 | 2,356 | 537 | 5,190 | 5,577 | 3,723 | 3,477 | 4,635 | 4,363 |

**Respuesta para sutil:**
- **Marzo de 2023 sí:** XGB-43 (1,899), XGB-37 (1,932), GE (2,153) y GC3 (2,893) se equivocan bastante menos que el mejor univariado (Naive 5,651; SARIMA 7,182; Chronos 6,973).
- **Abril y mayo no:** SARIMA (342 y 1,677) y Chronos (en mayo, 3,552) superan a todos.
- **En el bloque mar–may:** el mejor es SARIMA (3,067), seguido de XGB-43 (4,363), XGB-37 (4,665), Naive (4,834) y GE (5,052).
- **En el bloque mar–dic 2023:** Chronos (3,420) y SARIMA (3,630) son los mejores; GC3 y GE quedan en 6,859 y 5,986, y Ridge y ElasticNet por encima de 12,000.

Es un solo episodio y, en el mes favorable, un solo mes: el resultado es descriptivo y no permite inferencia.

**Limón dulce:**
- No hay caída en 2023: YoY entre −8.6 % y +4.9 % según la Fase 1. Mar–dic 2023 se pronostica mejor que mar–dic 2024 en los 11 modelos, y de forma parecida o algo peor que mar–dic 2022 (salvo el Seasonal Naive, que mejora).
- Mejor modelo mar–may 2023: Seasonal Naive (15.4), luego SARIMA-sel (19.9) y SARIMA (20.9).
- Modelos con exógenas: entre 47.9 (Ridge) y 71.4 (XGB-37); GC3 59.0 y GE 64.5. **Ningún modelo con clima, INDECI o noticias se equivoca menos que los univariados** en mar–may 2023 ni en marzo solo: el Seasonal Naive tiene 3.2 en marzo.

## 3. Efecto del registro en limón dulce

**3a. Las 5 provincias que "entran" en enero**

Fuentes: Excel → `03a_cinco_provincias_dulce_mensual_excel.csv` (120 meses × 5 provincias) y `03a_cinco_provincias_por_mes_calendario.csv`.

- **Hay filas en todos los meses.** Las 5 provincias tienen filas de distrito en los 120 meses (0 meses sin filas). En los meses previos a enero, las filas existen con **producción 0** y con **área en producción (VERDE_ACTUAL) constante y mayor que 0**. Por ejemplo, Satipo en nov–dic 2023: 9 filas, 0 t, 170 ha; en ene 2024: 97 t y 169 ha.
- **Es un calendario de cosecha, no un alta de registro.** Satipo produce ene–oct (máximo en abril, 284 t de media) y casi nada en nov–dic. Jaén produce feb–oct y nada en nov–dic. Maynas y Alto Amazonas solo producen ene–abr. Chota produce todo el año, con más en ene–jun.
- **Columna COSECHA (ha):** en estas provincias se registra casi solo en abr–oct, al cierre de cada campaña. No acompaña mes a mes a la producción (Satipo: 0 ha cosechadas de enero a junio, con 70–284 t). Es una particularidad del registro SISAGRI que no puedo interpretar más con estos datos.

Esto **corrige el hallazgo 7 de la Fase 1** y su interpretación en G: los saltos de enero en dulce no son altas de registro. Son el inicio estacional de la cosecha en provincias con campaña corta, lo que la Fase 1 dejó como "no verificable" (punto 4).

**3b. Paneles balanceados** (`03b_paneles_balanceados.csv`, `03b_calendario_MoM_P75_paneles.csv`; MoM P75, umbral calculado con la historia de cada panel hasta el origen)

| Cultivo | Panel | Provincias | % de las t de 2016–2025 |
|---|---|---|---|
| Dulce | Producción > 0 los 120 meses | 5 | 52.1 % |
| Dulce | Con filas los 120 meses | 23 | 99.6 % |
| Sutil | Producción > 0 los 120 meses | 36 | 96.9 % |
| Sutil | Con filas los 120 meses | 95 | 99.6 % |

**Dulce, panel "producción > 0 los 120 meses"** (umbral 21.9–26.4 %):
- Los shocks de enero **desaparecen en 2021, 2022 y 2024**, y persisten en 2025.
- Aparece 2023-01 (24.6 % frente a un umbral de 23.5 %).
- Febrero solo sigue siendo shock en 2025; marzo, en 2021 y 2022.
- Hay dos shocks nuevos fuera de campaña: 2024-09 (+45.5 %) y 2024-10.
- De los 15 shocks de la serie nacional quedan 6, y aparecen 2 nuevos.

**Dulce, panel "con filas los 120 meses":** reproduce los **15 shocks** de la serie nacional, idénticos, porque incluye a las provincias de campaña corta con sus meses de 0 t.

**Conclusión de 3b:** los shocks MoM de enero–marzo en dulce los produce la composición estacional de las provincias, no las altas o bajas del registro. Sin las provincias de campaña corta, la subida de enero deja de superar el umbral en la mayoría de los años.

**3c. Sutil:** los dos paneles reproducen casi exactamente el calendario nacional.
- Panel "producción > 0" (36 provincias, 96.9 % de las t): 9 de los 10 shocks se mantienen; 2022-12 se pierde por 0.1 puntos (25.1 % frente a 25.2 %) y aparece 2023-10.
- Panel "con filas": los 10 shocks, idénticos.

En sutil, la composición provincial no influye en los shocks.

## 4. Inicio frente a continuación, definiciones c) y d)

Fuente: `04_inicio_vs_continuacion.csv`. MAE (t), P75, pool 2021–2025. "Inicio" significa que el mes anterior no fue shock con la misma definición; para enero se usó la máscara de la ventana Y−1.

| Cultivo | Def., episodio | n | Naive | SNaive | Chronos | SARIMA | SARIMA-sel | Ridge | ElasticNet | XGB-37 | GC3 | GE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sutil | STL, inicio | 14 | 5,966 | 5,573 | **4,157** | 5,254 | 5,736 | 7,168 | 6,927 | 5,776 | 5,990 | 6,429 |
| Sutil | STL, continuación | 6 | 3,356 | 2,864 | 2,388 | 3,802 | 3,512 | 2,759 | 3,141 | **1,169** | 2,505 | 1,948 |
| Sutil | 3M, inicio | 7 | 6,667 | 6,878 | **4,047** | 5,248 | 5,107 | 9,397 | 8,723 | 7,143 | 7,103 | 7,808 |
| Sutil | 3M, continuación | 8 | 3,794 | 4,822 | 2,791 | 3,198 | **2,640** | 4,123 | 4,112 | 5,184 | 9,231 | 10,936 |
| Dulce | STL, inicio | 12 | 70.2 | 33.0 | 34.4 | **26.7** | 27.6 | 65.7 | 62.3 | 58.4 | 65.3 | 64.3 |
| Dulce | STL, continuación | 15 | 77.3 | 19.8 | 25.3 | 22.7 | **19.5** | 42.8 | 40.4 | 30.1 | 43.0 | 45.5 |
| Dulce | 3M, inicio | 5 | 121.2 | 22.7 | 33.6 | **10.3** | 15.9 | 39.8 | 39.3 | 45.7 | 52.5 | 45.2 |
| Dulce | 3M, continuación | 10 | 117.8 | 29.9 | 50.8 | 18.7 | **18.3** | 96.8 | 96.7 | 94.3 | 102.9 | 106.2 |

Las filas de MoM e YoY repiten la Fase 1 y también están en el CSV.
- **En los meses de inicio**, el mejor es siempre univariado: Chronos en sutil, SARIMA en dulce.
- **En la continuación de sutil STL**, XGB-37 (1,169) y GE (1,948) son los mejores, pero con n = 6 y sin intervalo.

---

## QUÉ DEFINICIÓN RECOMIENDO Y POR QUÉ

**Primaria: YoY P75.** Mantendría la MoM P75 preregistrada como referencia y usaría la STL, recalibrada, como sensibilidad.

1. **La MoM no sirve en dulce.** Confunde la estacionalidad (y la composición de provincias de campaña corta) con shocks: 14 de 15 meses en ene–mar (§1.2, §3b). En sutil funciona razonablemente, pero no ve las caídas graduales: 0 de 5 meses de mar–jul 2023 en P75 (§1.3).
2. **La 3M no resuelve dulce:** 15 de 15 en feb–abr.
3. **La STL**, tal como está especificada aquí, **no está calibrada**: marca el 33–45 % de los meses con P75 y el 67–72 % con P50 (§1.1). Para usarla habría que calibrar el umbral con cambios pseudo-fuera de muestra (STL reajustada en cada origen histórico). Eso es trabajo nuevo, de la Fase 3.
4. **La YoY:**
   - elimina la estacionalidad por construcción;
   - es transparente y ya estaba preregistrada como definición secundaria (D-BR7/E-BR1, `06_metricas` la reporta);
   - sale calibrada (10 y 16 meses con P75);
   - y es la que mejor recoge el episodio de 2023 a umbrales moderados (P60: abr–sep).
5. **Las conclusiones sobre modelos casi no dependen de la definición** (§1.6). Chronos es robusto en sutil con las cuatro; SARIMA o SARIMA-sel lo son en dulce con las cuatro; GC3 y GE no lo son con ninguna.

**Elegir una definición después de ver los resultados es una desviación.** Hay que declararla como tal, y la recomendación no altera el ranking. Lo honesto es presentar la MoM como lo preregistrado, mostrar sus limitaciones en dulce y reportar la YoY (y la STL calibrada si se hace) como análisis de robustez.

## HALLAZGOS QUE CAMBIAN EL MANUSCRITO

1. **Corrección de la Fase 1.** Los saltos de enero en dulce **no son altas de registro**. Las 5 provincias tienen filas los 120 meses, con 0 t y área en producción > 0 fuera de su campaña (§3a). Son el inicio de cosecha de provincias con campaña corta. La "intermitencia" de la Fase 1 (G) es estacionalidad provincial, no un problema de cobertura del registro, y el texto debe decirlo así.
2. **Los shocks MoM de dulce son, en su mayoría, estacionalidad de composición.** En el panel de las 5 provincias que producen todo el año, quedan 6 de los 15 shocks (§3b). Δs y el "desempeño en shock" de dulce con MoM no miden respuesta a eventos.
3. **El ranking en shock es robusto a la definición:** Chronos en sutil, SARIMA o SARIMA-sel en dulce. **GC3 y GE no son primeros ni empatados de forma robusta con ninguna** de las 4 definiciones × 4 umbrales × 2 pools. En unidades escaladas tienen entre 1.04 y 1.64 veces el MAE_shock del Seasonal Naive en sutil (salvo YoY, donde el Seasonal Naive es el peor modelo) y entre 1.32 y 3.13 veces en dulce (§1.4).
4. **El episodio de 2023 en sutil** tiene un único dato favorable a los modelos con exógenas: el error de **marzo de 2023**, 1.9–2.9 mil t frente a ≥ 5.7 mil t de los univariados. Desde abril, SARIMA y Chronos son mejores. En mar–may el mejor es SARIMA (3,067), y en mar–dic Chronos (3,420) (§2). Si el manuscrito habla de "capacidad ante el ciclón", solo se sostiene para el primer mes, como observación descriptiva.
5. **Las caídas graduales no se ven con MoM P75.** Si se quiere evaluar 2023 como shock climático, hay que usar YoY P50/P60 o una definición desestacionalizada calibrada (§1.3).
6. **Toneladas de más y razón shock/normal siguen siendo engañosas para GC3/GE.** En sutil STL dan "−2,126 t" y "−2,489 t" porque el MAE_normal es el más alto (§1.4). Hay que reportarlas junto a MAE_shock relativo o MASE_shock.

## NO VERIFICABLE

1. **Sentido de COSECHA (ha) en SISAGRI.** En las provincias de campaña corta, la columna COSECHA no acompaña a la producción mensual (se registra al cierre de la campaña). No hay en el repo un diccionario de variables de SISAGRI para confirmar su definición.
2. **Producción 0 frente a "sin dato".** Las filas con 0 t y área en producción > 0 son consistentes con meses sin cosecha, pero el Excel no distingue un 0 informado de un 0 por omisión.
3. **STL:** los parámetros `seasonal=13` y `robust=True` son una elección razonable mía. El protocolo no fija ninguna especificación STL, y otra ventana estacional cambiaría los umbrales. No probé alternativas, para no hacer búsqueda sobre los resultados.
4. **Inferencia sobre 2023:** con 1 episodio y, en el mes clave, n = 1, no hay inferencia posible sobre marzo de 2023. Las cifras de §2 son descriptivas.
5. **Inicio frente a continuación** (§4): no tiene IC, y varias celdas tienen n ≤ 6.
6. **El bootstrap** replica el del pipeline, pero las cifras de las definiciones STL y 3M son nuevas: no existen en `06_metricas`.
