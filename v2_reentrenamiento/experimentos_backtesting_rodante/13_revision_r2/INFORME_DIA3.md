# Revisión G7, ronda 2 — Día 3: cierre de análisis y material para el manuscrito (T11–T16)

**Todo lo de este informe es posterior al protocolo**. Se reporta como robustez, diagnóstico o material de
redacción y **no modifica el ranking principal** de 10 modelos. Las cifras salen de CSV: los de
`13_revision_r2/resultados/`, generados por los scripts de `13_revision_r2/scripts/`, y los publicados que esos
scripts reproducen. No se tocó ningún archivo congelado. En el repositorio antiguo solo se usaron `git log`,
`git show`, `git status`, `git rev-parse` y `git branch -r --contains`, todos de lectura; su `git status` es el mismo
antes y después. En este repositorio no se hizo ninguna operación git.

**Convenciones:** las del Día 2. MAE en toneladas; IC 95 %: bootstrap pareado de meses dentro de cada ventana,
B = 10 000, semilla 42; * = primero o empatado con el primero; DM: Diebold–Mariano con corrección HLN.

## 1. T11 — Figura 7 reducida (obs. 10a)

- **Script:** `scripts/t11_fig20_main.py`.
- **Salidas:** `figuras/fig20_real_vs_pred_2025_main_{sutil,dulce}.pdf`, más `.png`, `.csv` (datos dibujados) y
  `.txt` (pie sugerido).
- **Contenido:**
  - serie observada: línea negra gruesa con halo;
  - GC3: media de las 10 semillas en cada mes; el script falla si no hay 10;
  - Chronos, SARIMA y Seasonal Naive (este, discontinuo con cuadrados huecos);
  - meses de shock MoM P75 sombreados en gris, con la historia hasta el origen: sutil 01, 07 y 11; dulce 01, 02 y 03.
- **Estilo:** no se reescribió el dibujo. El script carga `02_scripts/14_fig20_reducida_2025.py`, que a su vez usa
  el estilo de `10_figuras.py`, y solo redirige la carpeta de salida. No escribe nada en `08_graficos/`.
- **Control:** el CSV de datos dibujados debe ser idéntico (SHA-256, CRLF → LF) al publicado en
  `08_graficos/predicciones/`, que está registrado en `expected_outputs_sha256.json`. Coincide en los dos cultivos.
- **`reproduce.py`:** es un paso nuevo, solo en el modo con figuras.

## 2. T12 — Ventanas 2018–2020 (obs. 10e)

- **Script:** `scripts/t12_ventanas_2018_2020.py`.
- **Salidas:** `resultados/T12_ventanas_2018_2020.csv` y `resultados/tablas_T12.md`.
- **Tabla LaTeX:** `latex/tab_r2_2018_2020.tex`.
- **Método:** el mismo de la evaluación del artículo (`r2eval`: bootstrap estratificado por ventana, ranking con
  empates). Una fila extra da el pool 2018–2020.
- **Control:** el MAE, el MAE_shock y n_shock de cada ventana coinciden con
  `06_metricas/agregadas/T17_descriptivo_2018_2020_{c}.csv` (18 filas). Los IC son lo nuevo.

<!-- copiado sin editar de resultados/tablas_T12.md -->
#### T12 — Ventanas 2018–2020: modelos sin entrenamiento (MAE en t, IC 95 % bootstrap)

* = primero o empatado con el primero entre los tres modelos. MASE vacío en 2018: no hay denominador (la historia hasta el origen no tiene 12 meses con y_(t−12)).

**sutil**

| ventana | modelo | MAE todos (IC95) | MASE | n shock | MAE shock MoM P75 (IC95) |
|---|---|---|---|---|---|
| 2018 | Naive | 2,727 (1,384–4,264) | — | 4 | 6,237 (5,221–6,857) |
| 2018 | Seasonal Naive | 8,317 (6,535–10,001) | — | 4 | 7,601 (4,039–10,013)* |
| 2018 | Chronos | 1,973 (885–3,252)* | — | 4 | 4,787 (3,678–5,576)* |
| 2019 | Naive | 3,562 (2,166–5,119)* | 0.37 | 3 | 7,245 (5,122–8,961) |
| 2019 | Seasonal Naive | 3,728 (2,468–5,075)* | 0.38 | 3 | 2,250 (559–4,966)* |
| 2019 | Chronos | 2,702 (1,578–3,922)* | 0.28 | 3 | 4,697 (2,734–7,212)* |
| 2020 | Naive | 4,102 (2,401–6,030) | 0.45 | 3 | 7,809 (4,180–11,561)* |
| 2020 | Seasonal Naive | 2,443 (1,425–3,722)* | 0.27 | 3 | 4,516 (2,725–7,966)* |
| 2020 | Chronos | 2,931 (1,676–4,309)* | 0.32 | 3 | 5,848 (3,988–7,556)* |
| 2018-2020 | Naive | 3,464 (2,563–4,406) | — | 10 | 7,011 (5,830–8,198)* |
| 2018-2020 | Seasonal Naive | 4,829 (4,011–5,634) | — | 10 | 5,070 (3,425–6,635)* |
| 2018-2020 | Chronos | 2,535 (1,842–3,274)* | — | 10 | 5,078 (4,200–5,973)* |

**dulce**

| ventana | modelo | MAE todos (IC95) | MASE | n shock | MAE shock MoM P75 (IC95) |
|---|---|---|---|---|---|
| 2018 | Naive | 72.3 (46.5–97.4) | — | 4 | 112.0 (89.8–135.9) |
| 2018 | Seasonal Naive | 28.0 (20.2–36.4)* | — | 4 | 33.6 (20.5–52.6)* |
| 2018 | Chronos | 31.8 (20.2–43.6)* | — | 4 | 48.7 (38.2–57.6)* |
| 2019 | Naive | 74.9 (52.8–97.8) | 1.98 | 4 | 118.5 (102.6–138.7) |
| 2019 | Seasonal Naive | 29.4 (16.1–43.8)* | 0.78 | 4 | 21.4 (10.4–41.6)* |
| 2019 | Chronos | 33.5 (25.1–41.5)* | 0.89 | 4 | 35.9 (20.5–46.7)* |
| 2020 | Naive | 66.7 (38.7–96.0) | 2.03 | 4 | 118.2 (90.6–153.8) |
| 2020 | Seasonal Naive | 17.1 (10.4–25.8)* | 0.52 | 4 | 8.8 (2.9–14.1)* |
| 2020 | Chronos | 28.8 (19.1–39.3) | 0.88 | 4 | 27.7 (12.9–42.6) |
| 2018-2020 | Naive | 71.3 (56.2–86.2) | — | 12 | 116.2 (102.3–131.0) |
| 2018-2020 | Seasonal Naive | 24.8 (19.2–30.9)* | — | 12 | 21.3 (13.9–30.0)* |
| 2018-2020 | Chronos | 31.4 (25.6–37.2)* | — | 12 | 37.5 (29.5–45.0) |

**Lectura:**
- **Sutil:**
  - Chronos tiene el menor MAE de todos los meses en 2018, 2019 y el pool.
  - En 2020 el menor es Seasonal Naive (2,443 t), empatado con Chronos.
  - En los meses de shock (3–4 por año) los IC son muy anchos y los tres modelos quedan empatados casi siempre.
- **Dulce:**
  - Seasonal Naive tiene el menor MAE en todos los años y en el pool.
  - Chronos empata con él en 2018 y 2019, pero no en 2020 ni en los shocks del pool.
  - Naive es el peor en todos los casos.
- **Pool 2018–2020:** sin MASE, porque 2018 no tiene denominador.
- **Patrón:** es el mismo de 2021–2025 en los dos cultivos (sutil: Chronos al frente; dulce: los modelos
  estacionales al frente). Con 12 meses por ventana, la evidencia por año es débil.

## 3. T13 — Inicio de la serie en enero de 2016 (obs. 7)

### ¿Hay una justificación escrita?

**No.** No hay en la documentación del proyecto ningún texto que explique por qué la serie empieza en
**enero de 2016** y no en 2015. La ventana 2016–2025 aparece siempre como un dato fijado, sin justificación. Se
revisaron:
- `DECISIONES_METODOLOGICAS.md`;
- `01_configuracion/`;
- los README del repositorio, de `etl/` y de las etapas;
- `09_reportes/` (incluidas las fases G7);
- los comentarios del código de `etl/` y `src/data_collection/`;
- además, solo lectura, el repositorio antiguo.

Textos exactos donde se fija la ventana:

| Dónde | Texto exacto | ¿Justifica 2016? |
|---|---|---|
| `v2_reentrenamiento/etl/01_sisagri_a_series.py:44` | `ANIO_INI, ANIO_FIN = 2016, 2025` | No: constante sin comentario |
| `v2_reentrenamiento/etl/01_sisagri_a_series.py:82` | `"""Filtra el cultivo y 2016-2025; orden estable por AÑO, MES, COD_UBIGEO (orden de hojas dentro de la clave).` | No |
| `v2_reentrenamiento/etl/README.md:48` | `2. **distrito_crudo:** `PRODUCTO` ∈ {LIMON SUTIL, LIMON DULCE}, años 2016–2025, sin otro filtro.` | No |
| `experimentos_backtesting_rodante/01_configuracion/ventanas.json:7` | `"inicio_serie": "2016-01",` | No: es el valor preregistrado, sin campo de motivo |
| `v2_reentrenamiento/src/data_collection/agraria_scraper_v2.py:5` | `ventana 2016-2025 del reentrenamiento v2.` | No |
| `v2_reentrenamiento/src/data_collection/nasa_power_downloader_v2.py:138` | `df, errores = downloader.download(2016, 2025)` | No |
| `v2_reentrenamiento/DECISIONES_METODOLOGICAS.md:66` | `**Decisión:** Split cronológico train=2016-2023 (96 meses), val=2024 (12 meses), test=2025 (12 meses). 2026 excluido por cobertura geográfica incompleta (año en curso).` | Solo justifica el fin (excluir 2026), no el inicio |
| `v2_reentrenamiento/DECISIONES_METODOLOGICAS.md:88-90` | `Tras generar lags t-6, los primeros 6 meses (2016-01 a 2016-06) se eliminan por no tener historial completo dentro del dataset (dropna, mismo criterio que v1). Train pasa de 96 a 90 meses (2016-07 a 2023-12).` | No: explica 2016-07, dando 2016-01 por fijo |
| `v2_reentrenamiento/DECISIONES_METODOLOGICAS.md:1487-1490` | `No se amplia retrospectivamente a 2016-01. La razon es que ese fue el periodo efectivamente usado por GC1 vigente; modificarlo despues del cierre del modelo redefiniria la muestra de estimacion.` | No: compara 2016-07 con 2016-01, no con 2015 |
| `v2_reentrenamiento/DECISIONES_METODOLOGICAS.md:196-198` | `**Decisión:** usar este único archivo como fuente completa de INDECI 2016-2025, reemplazando los .dbf de 2019-2020, …` | No. El archivo de INDECI es `BD_2003-2025_EMERGENCIAS.csv`: INDECI no limitaba el inicio |
| `09_reportes/revision_g7/fase5/INFORME_FASE5.md:90-91` | `Se leyeron 72,045 filas de limón de 2015–2026: 61,741 de sutil y 10,304 de dulce. Tras filtrar 2016–2025 quedan 57,445 y 9,568.` | No: confirma que el Excel tiene filas de 2015 y que el ETL las descarta, sin motivo |

**Contexto, solo en el repositorio antiguo (privado, v1; no es justificación de v2):**
- La versión v1 leía otro archivo, `Sisagri_2016_2025.xlsx` (`src/data_processing/midagri_etl.py:68`,
  `pipeline/README.md:43`). El notebook `pipeline/actividad_02_lectura_datos.ipynb` dice: «El archivo contiene datos
  desde 2016 hasta 2020 en esta versión».
- **Hipótesis (sin texto que la confirme):** la ventana 2016–2025 parece heredada de ese archivo de v1. Al pasar a
  `sisagri_2015_2026.xlsx` en v2, el filtro siguió siendo 2016–2025.
- **Lo que no se pudo comprobar:** que el Excel cubra desde febrero de 2015. El Excel no se redistribuye y no está
  en esta PC. Solo consta que su primera hoja se llama «2015–2018» (`etl/README.md:45`) y que tiene filas de limón
  de 2015–2026 (INFORME_FASE5).

### Desde qué mes existe cada fuente en los datos congelados

Generado por `scripts/t13_cobertura_datos.py` → `resultados/T13_cobertura_datos.csv`. Antes de leer cada archivo, el
script comprueba su SHA-256 contra `hashes_congelados.json`, salvo en los distritales, que no están registrados.

| Fuente | Archivo | Primer mes | Último mes | Meses | Primer mes con valor > 0 | Meses en 0 |
|---|---|---|---|---|---|---|
| Producción nacional, sutil | `data/interim/limon_sutil_nacional_mensual.csv` | 2016-01 | 2025-12 | 120 | 2016-01 | — |
| Producción nacional, dulce | `data/interim/limon_dulce_nacional_mensual.csv` | 2016-01 | 2025-12 | 120 | 2016-01 | — |
| Producción distrital (sutil y dulce) | `data/interim/limon_{c}_distrito_crudo.csv` | 2016-01 | 2025-12 | 120 | 2016-01 | — |
| Clima NASA POWER (109 provincias) | `data/raw/nasa_power/por_provincia/clima_nasa_power_2016_2025.csv` | 2016-01 | 2025-12 | 120 | (no aplica) | — |
| Emergencias INDECI | `data/interim/indeci_limpio_2016_2025.csv` | 2016-01 | 2025-12 | 120 | 2016-01 | — |
| Noticias Agraria.pe (n.º de artículos) | `data/interim/noticias/sentimiento_mensual_2016_2025.csv` | 2016-01 | 2025-12 | 120 | **2016-03** | 2016-01, 2016-02 |

- **Todas las fuentes congeladas empiezan en 2016-01.** Ninguna tiene datos de 2015.
- **Noticias:** existen como filas desde 2016-01, pero sin artículos en 2016-01 y 2016-02 (sentimiento 0). Es la
  limitación declarada en `DECISIONES_METODOLOGICAS.md:267`.
- **Uso en los modelos:**
  - SARIMA y features desde 2016-07 (`ventanas.json`: `inicio_features`, `inicio_train_sarima`);
  - objetivos tabulares desde 2016-08;
  - objetivos LSTM desde 2017-01;
  - Chronos usa el contexto desde 2016-01.
- **Consecuencia:** los dos meses sin noticias no entran en ningún entrenamiento como objetivo. Sí pueden entrar como
  rezago: `lag6` de la fila 2016-07 = 2016-01.

## 4. T14 — Historial del protocolo (obs. 8)

- **Acceso:** sí había un clon del repositorio antiguo en esta PC, en la rama `revision-experimento-v2`, también
  presente como `origin/revision-experimento-v2`.
- **Script:** `scripts/t14_historial_protocolo.py --repo <clon>`. Usa solo `git log` y `git show`.
- **Salidas:** **`13_revision_r2/HISTORIAL_PROTOCOLO.md`** y `resultados/T14_historial_protocolo.csv`.
- **Por qué no en `01_configuracion/`:** esa carpeta está preregistrada y congelada.
- **Archivos cubiertos (16):**
  - `00_plan/` (borrador_preregistro, plan_fase_A, mapa_evidencia, nota_chronos_pesos);
  - los 7 JSON de `01_configuracion/`;
  - `DECISIONES_METODOLOGICAS.md`;
  - `09_reportes/` (DESVIACIONES, reporte_fase_A, reporte_fase_B, nota_v5_v3).
- **Contenido:** 30 versiones. Para cada una:
  - hash completo del commit;
  - fecha de autor (`%ad`) y de commit (`%cd`);
  - mensaje;
  - tamaño;
  - SHA-256 en bytes y con CRLF → LF;
  - si es igual al archivo publicado.
- **No es un paso de `reproduce.py`:** el repositorio antiguo no se distribuye.

**Cronología:**

| Fecha (−05:00) | Commit | Qué |
|---|---|---|
| 2026-10-25 22:16:40 | `344134b` | «preregistro D-BR1 a D-BR10 antes de la Fase C»: primera versión de los 11 archivos de `00_plan/` y `01_configuracion/` y de los reportes de las Fases A y B |
| 2026-10-25 22:22:33 | `db32108` | «preregistro final copiado a DECISIONES_METODOLOGICAS antes de la Fase C»: versión final de `borrador_preregistro.md` (**idéntica a la publicada**) y su copia en `DECISIONES_METODOLOGICAS.md` |
| 2026-10-28 19:02:43 | `ddb8d4a` | enmienda E-BR1 (DESV-02), añadida al final de `DECISIONES_METODOLOGICAS.md` sin reescribir D-BR7; cambio del método de hash (DESV-01) en `hashes_congelados.json`; `DESVIACIONES.md` creado |
| 2026-10-28 19:03:18 → 20:13:01 | — | las 488 unidades de la Fase C terminan (campo `fin` de los `completado.json` de `04_modelos/` de este repositorio) |
| 2026-10-28 20:16:48 | `09b0945` | salidas de la Fase C («predicciones congeladas antes de la Fase D») |

- **Sin cambios desde el 25-oct:** `ventanas.json`, `umbrales.json`, `hiperparametros_congelados.json`,
  `rutas_datos.json`, `estilo_figuras.json`, `plan_fase_A.md`, `mapa_evidencia.md`, `nota_chronos_pesos.md`,
  `reporte_fase_A.md` y `reporte_fase_B.md` tienen una sola versión (la del commit `344134b`), igual byte a byte
  (CRLF → LF) a la publicada.
- **`DESVIACIONES.md`:** la publicada no coincide con ninguna versión del repositorio antiguo, porque se le añadieron
  entradas después (revisión G7). Es esperado: es el registro de cambios.
- **Fechas:**
  - son las que guarda git y se pueden fijar a mano;
  - lo mismo vale para los `completado.json`, que escribe el propio código;
  - la prueba independiente sería el registro de push de GitHub del repositorio privado, que no se consultó (sin red).

Comando para regenerarlo (YesaR, en su PC), desde la raíz de este repositorio:

```bash
venv\Scripts\python.exe v2_reentrenamiento\experimentos_backtesting_rodante\13_revision_r2\scripts\t14_historial_protocolo.py --repo C:\Machine-learming\Machine-Learning-Multimodal--Agro-NLP-Clima-
```

O, archivo por archivo, solo con git (en el clon antiguo):

```bash
git log --follow --format="%H %ad %s" --date=iso -- v2_reentrenamiento/experimentos_backtesting_rodante/00_plan/borrador_preregistro.md
git show <commit>:v2_reentrenamiento/experimentos_backtesting_rodante/00_plan/borrador_preregistro.md | sha256sum
```

## 5. T15 — Tablas LaTeX para el manuscrito

- **Generador:** `scripts/t15_latex.py`. Lee solo los CSV de `resultados/` y escribe `latex/tab_r2_*.tex` y
  `latex/indice.json`.
- **Formato:**
  - booktabs, en inglés, `\resizebox{\linewidth}`;
  - paquetes: `booktabs`, `graphicx` y `float`;
  - separador de miles «,»;
  - toneladas sin decimales en sutil y con 1 decimal en dulce;
  - MASE con 2 decimales y Δs con 1;
  - p con 3 decimales y `$<$0.001`;
  - IC entre corchetes `[lo; hi]`, como en las tablas publicadas.
- **Leyenda:** cada tabla tiene `\caption`, `\label{tab:r2_…}` y una nota final. La nota dice que todo es posterior
  al protocolo; † marca ETS y Theta («added after the protocol»).

| Archivo | `\label` | Contenido | CSV de origen |
|---|---|---|---|
| `tab_r2_accuracy.tex` | `tab:r2_accuracy_ets_theta` | Tabla 3 con ETS† y Theta†. Columnas: MAE todos / normal / shock MoM con IC, Δs, MASE_shock, MAE shock YoY con IC, MASE_shock YoY | `T1_metricas_12_modelos_2021_2025.csv` |
| `tab_r2_ranking.tex` | `tab:r2_ranking_consistently_top` | Posición en P50–P90, MoM y YoY, 12 modelos; «Top (of 4)» y «Consistently»; la nota compara con los 10 originales | `T1_ranking_shock_P50_P90.csv`, `T1_robustez_3de4.csv` |
| `tab_r2_2025.tex` | `tab:r2_ranking_2025` | MAE 2025 con IC, posición 2025 y posición en el pool, para todos los meses y shock MoM/YoY | `T2_ranking_2025.csv` |
| `tab_r2_e5_ablation.tex` | `tab:r2_e5_seasonal_lag` y `tab:r2_block_ablation` | Dos tablas: E5 (diferencia con IC, efecto de solo y_(T−12), semillas, DM p) y ablación por bloques (diferencia con el conjunto anterior, con IC) | `T6_E5_y12_tabulares.csv`, `T7_ablacion_bloques.csv` |
| `tab_r2_sarimax.tex` | `tab:r2_sarimax` | SARIMA, SARIMAX-PC y SARIMAX-30: MAE con IC, MASE, diferencia con IC, DM-HLN, p; convergencia en la nota | `T7_sarimax_vs_sarima.csv`, `unidades_d2/sarimax_info.csv` |
| `tab_r2_exante.tex` | `tab:r2_ex_ante_shocks` | Definiciones A y B (P75: MAE con IC, MASE, «Consistently») y C (El Niño costero: MAE, MASE, posición); n.º de meses y coincidencias con los shocks ex post en la cabecera de cada cultivo; nota sobre el ICEN y el evento 2023-03..2024-02, leído de la lista del IGP | `T8_metricas_ex_ante.csv`, `T8_robustez_ex_ante.csv`, `datos_externos/igp_icen/lista_eventos_ICEN.html` |
| `tab_r2_h2.tex` | `tab:r2_horizon_h2` | h = 2 frente a h = 1, todos los meses y shock MoM, posición y regla de 3 de 4 | `T9_metricas_h2.csv`, `T9_robustez_h2.csv` |
| `tab_r2_crps.tex` | `tab:r2_crps` | CRPS_Q, twCRPS_Q y CRPS normal exacto: media con IC, diferencia con SARIMA con IC, DM p; cobertura 10–90 % en la cabecera | `T10_crps_resumen.csv`, `T10_crps_por_mes.csv` |
| `tab_r2_2018_2020.tex` | `tab:r2_windows_2018_2020` | La tabla de T12 | `T12_ventanas_2018_2020.csv` |
| `tab_r2_sarima_sel_fallback.tex` | `tab:r2_sarima_sel_fallback` | E1 con las dos reglas: regla 1 (siguiente por AIC, Día 1) y regla 2 (siguiente por MAE de validación, Día 2); pool y ventana sutil 2021 | `T5_SARIMA_sel_Y1_pool.csv`, `T3_3_*.csv`, `T5_regla_respaldo_por_ventana.csv`, `05_predicciones/errores_test_promediados_semillas.csv` (MAE 2021 de SARIMA-sel) |

**Controles del generador:**
- en la tabla de respaldo, las cifras compartidas por `T3_3` (Día 1) y `T5` (Día 2) deben coincidir: el E1
  publicado y la «alternativa B» = regla 2;
- la regla debe actuar en una sola unidad, la misma en los dos CSV.

**Revisión estructural** (script auxiliar, no incluido):
- en cada fila, la suma de columnas, contando `\multicolumn`, es igual a la especificación del `tabular`;
- llaves balanceadas;
- sin `%`, `#` ni `_` sin escapar fuera de modo matemático o de `\label`/`\ref`.

**Decisiones de formato:**
- **Columnas de la Tabla 3:** no está el `.tex` del manuscrito en el repositorio, así que se usaron las columnas
  de T1.a del Día 1 («formato Tabla 3»). Si la Tabla 3 del artículo tiene otras columnas, hay que ajustar
  `t_accuracy()`.
- **Regla 1 sin IC:** sus predicciones no se guardaron en el Día 1 (solo el MAE, en `T3_3`). Así se indica en la
  nota de la tabla.

## 6. T16 — Cifras clave

- **Script y salida:** `scripts/t16_cifras_clave.py` → **`13_revision_r2/CIFRAS_CLAVE.md`**.
- **Contenido:** 244 líneas en inglés, una cifra o un grupo de cifras por línea, con la tabla LaTeX y el CSV de
  origen.
- **Secciones:**
  - T1: ETS/Theta y referencias; DM; «consistently top-ranked» con 10 y con 12 modelos;
  - T2: primer lugar en 2025;
  - T3: constante del SARIMA;
  - T5: reglas de respaldo;
  - T6: E5;
  - T7: ablación por bloques y SARIMAX;
  - T8: ex ante y El Niño;
  - T9: h = 2;
  - T10: CRPS y cobertura;
  - T12: 2018–2020;
  - T13: cobertura de los datos.
- **Origen de las cifras:** todas se copian de los CSV con el mismo formato que las tablas; ninguna se escribió a
  mano.

## 7. Archivos creados o modificados

Nuevos (todos en `13_revision_r2/`):
- **Scripts** (en `scripts/`):
  - `t11_fig20_main.py`, `t12_ventanas_2018_2020.py`, `t13_cobertura_datos.py`;
  - `t14_historial_protocolo.py`, `t15_latex.py`, `t16_cifras_clave.py`;
  - `empaquetar_manuscrito.py`.
- `figuras/fig20_real_vs_pred_2025_main_{sutil,dulce}.{pdf,png,csv,txt}`.
- `resultados/T12_ventanas_2018_2020.csv`, `resultados/tablas_T12.md`, `resultados/T13_cobertura_datos.csv` y
  `resultados/T14_historial_protocolo.csv`.
- `latex/tab_r2_*.tex` (10 archivos, 11 tablas) y `latex/indice.json`.
- `CIFRAS_CLAVE.md`, `HISTORIAL_PROTOCOLO.md`, `INFORME_DIA3.md` y `paquete_manuscrito.zip`.

Modificados:
- `reproduce.py` (raíz): pasos R2 nuevos, en este orden:
  1. `t12_ventanas_2018_2020.py` y `t13_cobertura_datos.py`, después de T10;
  2. `t11_fig20_main.py`, solo con figuras;
  3. `t15_latex.py` y `t16_cifras_clave.py`.
- `13_revision_r2/README.md`: sección del Día 3.

## 8. Resultado de `reproduce.py` (modo con figuras)

Ejecutado con `venv\Scripts\python.exe reproduce.py` en esta PC, modo con figuras, exit code 0:

```
[OK] integrity: SHA-256 of official code, frozen data and Chronos (hashes_congelados.json) (0 s)
[OK] leakage test, backtesting (test_fuga.py) (33 s)
[OK] leakage test, diagnostic experiments (test_fuga_g7.py) (54 s)
[OK] phase D1: metrics, bootstrap, Diebold-Mariano, threshold sweep (run_all.py --fase D1) (18 s)
[OK] diagnostic experiments (G7): evaluation T1-T10 (evaluar.py) (6 s)
[OK] first-round diagnostic tables (09_reportes/revision_g7/fase1, g7_fase1.py): regenerate and compare cell by cell (4 s)
[OK] phase D2: figures (run_all.py --fase D2) (29 s)
[OK] figures: 11_figuras_d3.py (11 s)
[OK] figures: 13_figura_workflow.py (4 s)
[OK] figures: 14_fig20_reducida_2025.py (2 s)
[OK] review R2 (13_revision_r2): ETS and Theta, rolling origin 2021-2025 (t1_ets_theta.py) (18 s)
[OK] review R2 (13_revision_r2): ETS/Theta metrics, 12-model ranking and 2025-only ranking (t1_t2_evaluar.py) (3 s)
[OK] review R2 (13_revision_r2): SARIMA constant, no-constant sensitivity and SARIMA-sel fallback rule (t3_sarima.py) (6 s)
[OK] review R2 (13_revision_r2): predictor lags, fig20 content and Seasonal Naive check (t4_verificaciones.py) (4 s)
[OK] review R2 (13_revision_r2): SARIMA-sel fallback rule by validation MAE (E1) (t5_respaldo_sarima_sel.py) (8 s)
[OK] review R2 (13_revision_r2): E5 (y_t-12 in tabular models) and block ablation (t6_t7_tabulares.py) (25 s)
[OK] review R2 (13_revision_r2): SARIMAX with lagged exogenous variables (t7_sarimax.py) (33 s)
[OK] review R2 (13_revision_r2): ex-ante large-change months and El Nino costero months (t8_ex_ante.py) (3 s)
[OK] review R2 (13_revision_r2): two-step-ahead horizon (t9_h2.py) (57 s)
[OK] review R2 (13_revision_r2): CRPS and threshold-weighted CRPS (t10_crps.py) (11 s)
[OK] review R2 (13_revision_r2): models without training in the 2018-2020 windows, with bootstrap CIs (t12_ventanas_2018_2020.py) (1 s)
[OK] review R2 (13_revision_r2): first and last month of each frozen input table (t13_cobertura_datos.py) (1 s)
[OK] review R2 (13_revision_r2): reduced Figure 7, test year 2025 (t11_fig20_main.py) (2 s)
[OK] review R2 (13_revision_r2): LaTeX tables for the manuscript (t15_latex.py) (1 s)
[OK] review R2 (13_revision_r2): key figures for the manuscript text (t16_cifras_clave.py) (1 s)
Compared 2231 files (160 regenerated by this run): {'IDENTICAL': 2231}; max |difference| = 0. Report: reproduction_report.json
09_reportes/revision_g7/fase1: 15 of 15 tables identical cell by cell.
```

Efectos secundarios de la corrida, revisados y deshechos:

1. **Los 66 PDF de `08_graficos/`:** el modo con figuras los reescribe. Con cada versión de git tienen el mismo
   tamaño y difieren en ≤ 9 bytes, solo en `CreationDate`. Se restauraron sus bytes versionados (`git show
   HEAD:<ruta> > <ruta>`, que no cambia el estado de git). Los Días 1 y 2 corrieron `--no-figures` y por eso no lo
   vieron.
2. **Cinco CSV de R2 con Chronos en T9/T10** (`T9_metricas_h2.csv`, `T9_controles_h1.csv`, `unidades_d2/h2.csv`,
   `T10_crps_resumen.csv`, `T10_crps_por_mes.csv`):
   - cambiaron en el 7.º u 8.º dígito significativo (p. ej., MAE h = 2 de Chronos en sutil: 3,668.566076 →
     3,668.566369);
   - es aritmética float32 de Chronos en otra CPU: los controles de tolerancia de T9 y T10 pasan;
   - se restauraron sus bytes versionados, igual que los PDF;
   - comprobación: `t15_latex.py` y `t16_cifras_clave.py` dan exactamente los mismos `.tex` y `CIFRAS_CLAVE.md`
     con los valores de esta corrida y con los versionados; no cambia ninguna cifra publicable.

Tras restaurar, `git status` solo muestra `reproduce.py` y `13_revision_r2/README.md` modificados, más los archivos
nuevos del Día 3.

## 9. Paquete para el manuscrito

`13_revision_r2/paquete_manuscrito.zip`, generado por `scripts/empaquetar_manuscrito.py`. Es un zip determinista:
orden fijo y fecha fija en las entradas. Contiene:
- `latex/tab_r2_*.tex` (10 archivos);
- `figuras/fig20_real_vs_pred_2025_main_{sutil,dulce}.pdf`, más el `.png` y el `.txt` de pie sugerido de cada una;
- `CIFRAS_CLAVE.md`;
- `INFORME_DIA1.md`, `INFORME_DIA2.md`, `INFORME_DIA3.md`;
- `HISTORIAL_PROTOCOLO.md`.

## 10. Lo que no se pudo hacer o quedó limitado

- **LaTeX sin compilar:** no hay distribución de LaTeX en esta PC. Las tablas pasaron solo la revisión estructural
  de la sección 5.
- **Tabla 3:** no se pudo comparar con el `.tex` del manuscrito, que no está en el repositorio (ver la sección 5).
- **Excel de MIDAGRI (T13):** no está en esta PC. No se pudo comprobar que cubra desde febrero de 2015 ni contar sus
  meses de 2015.
- **Fechas de T14:** son autodeclaradas (git y `completado.json`). No se consultó el registro de push de GitHub.
- **Regla 1 de respaldo:** sin IC (sus predicciones no se guardaron en el Día 1).
- **Git:** en este repositorio, ninguna operación. En el antiguo, solo comandos de lectura.
