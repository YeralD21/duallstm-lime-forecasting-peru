## Coordenadas climáticas — granularidad provincial (decisión aprobada, evidencia completa)

**Proceso (3 pasos de investigación previos a la decisión):**
1. Búsqueda de fuente de coordenadas distritales con UBIGEO 6 dígitos.
2. Análisis de heterogeneidad geográfica de distritos productores (top-10
   provincias de Limón Sutil).
3. Estimación de costo del clima a nivel distrito.

**Fuente distrital — SÍ existe (la investigación la encontró, no se asumió su ausencia):**
- `jmcastagnetto/ubigeo-peru-aumentado` → `ubigeo_distrito.csv`
  (`https://raw.githubusercontent.com/jmcastagnetto/ubigeo-peru-aumentado/main/ubigeo_distrito.csv`,
  409,857 bytes, HTTP 200 verificado). Columnas clave: `inei` (UBIGEO INEI
  6 dígitos), `latitude`, `lon`, `altitude`, `capital`, `superficie`. Cruza
  directo con `COD_UBIGEO` de MIDAGRI. No es un archivo oficial de INEI
  (tabulación derivada de CEPLAN/INEI/MINSA, DOI Zenodo, MIT), pero es la
  única fuente con lat/lon ya calculadas listas para cruce.
- Ruta 100% INEI: capa oficial de geometría distrital
  `https://ide.inei.gob.pe/files/Distrito.rar` (GeoPackage, actualizado 2023,
  ~12.4 MB, HTTP 200) con UBIGEO en atributos; el centroide debe computarse
  (requiere geopandas/GDAL). No existe centroide distrital precalculado y
  descargable del INEI; los códigos oficiales (sin coordenadas) están en
  SISCONCODE (`https://webapp.inei.gob.pe:8443/sisconcode/main.htm`).

**Heterogeneidad de distritos productores (Paso 2) — evidencia:**
criterio: distritos con PRODUCCION acumulada 2016-2025 > 0
(`limon_sutil_distrito_dedup.csv`).

| Provincias (top-10) | N distritos | Distrito líder (% de la producción provincial) |
|---|---|---|
| PIURA (#1) | 9 | TAMBO GRANDE 85.4% |
| SULLANA (#2) | 6 | SULLANA 99.3% |
| LAMBAYEQUE (#3) | 6 | OLMOS 52.9% |
| ZARUMILLA (#4) | 4 | MATAPALO 59.4% |
| MORROPON (#5) | 7 | CHULUCANAS 66.7% |
| TUMBES (#6) | 6 | PAMPAS DE HOSPITAL 66.3% |
| CORONEL PORTILLO (#7) | 7 | CAMPOVERDE 27.7% |
| MAYNAS (#8) | 11 | BELEN 36.9% |
| UTCUBAMBA (#9) | 6 | CUMBA 41.2% |
| PADRE ABAD (#10) | 5 | CURIMANA 25.2% |

La producción por provincia está concentrada: 7 de 10 provincias tienen un
distrito líder con ≥53% de su producción; solo CORONEL PORTILLO y PADRE ABAD
muestran reparto relativamente uniforme (líder ≤28%, ≤7 distritos).

**Costo estimado de la opción distrital (Paso 3):**
- Distritos productores únicos (PRODUCCION>0): Sutil 481 + Dulce 72 =
  494 únicos (59 compartidos entre ambos cultivos).
- Llamadas NASA POWER: 494 vs 109 actuales → **385 adicionales**.
- Tiempo estimado (0.7 s delay + ~1.3 s latencia, sin retries): **~16.5 min**
  vs ~3.6 min actuales.
- Limitación del grid: NASA POWER es ~0.5°×0.5° (~55×55 km). Entre las 109
  coordenadas provinciales actuales hay solo 88 celdas distintas (21
  provincias comparten celda); a nivel distrito la cota real de información
  serían las celdas únicas tocadas (no 494).

**Decisión:** mantener la granularidad provincial
(`data/interim/coordenadas_provincias_completo.csv`) como fuente de clima
para el reentrenamiento v2. No se ejecuta descarga distrital.

**Estado de aprobación:** esta decisión fue presentada al usuario con la
evidencia completa de los 3 pasos y fue **APROBADA explícitamente el
30-08-2026** tras su revisión (no fue tomada unilateralmente).

## 2026-XX-XX — Split train/val/test — Limón Sutil y Limón Dulce

**Decisión:** Split cronológico train=2016-2023 (96 meses), val=2024 (12 meses), test=2025 (12 meses). 2026 excluido por cobertura geográfica incompleta (año en curso).

**Verificación de representación de shocks (previa a la decisión):**
- Train: 28% meses de shock (Sutil) / 25% (Dulce)
- Val: 0% (Sutil) ⚠️ / 25% (Dulce)
- Test: 25% (Sutil) / 25% (Dulce)

**SUPERSEDED POR D35-b (2026-09-10):** esta verificacion queda como
trazabilidad historica previa. La definicion oficial v2 de shock y los P75
vigentes son los TRAIN-only documentados en la seccion D35; los porcentajes
anteriores no deben usarse como fuente normativa del umbral.

**Justificación estadística:** Test de chi2 train vs. val+test compatible (Sutil p=0.11, Dulce p=1.00) — no hay sesgo estructural entre particiones.

**Justificación de dominio:** Los shocks detectados (umbral P75 de variación mensual) correlacionan con eventos reales documentados: El Niño 2015-16, El Niño Costero 2017, cuarentena COVID-19 2020, Ciclón Yaku 2023, crisis de precios del limón 2023-24 — no son ruido estadístico.

**Limitación declarada:** VAL-Sutil no contiene meses de shock (2024 fue año de producción récord con baja volatilidad relativa). La validación de hiperparámetros para Sutil mide capacidad de extrapolación a nivel superior, no robustez ante shocks. Las métricas de resiliencia (Δs) se reportan exclusivamente sobre el conjunto de test (2025), que sí tiene representación adecuada (25%).

**Alternativa descartada:** Split train=2016-2022/val=2023/test=2025 con 2024 como buffer no scoreado — descartada por "quemar" un año completo de datos sin ganancia proporcional, dado que el riesgo central (train sin shocks) no se confirmó.

### Actualización — ajuste de train por dropna de lags (features temporales)

Tras generar lags t-6, los primeros 6 meses (2016-01 a 2016-06) se
eliminan por no tener historial completo dentro del dataset (dropna,
mismo criterio que v1). Train pasa de 96 a 90 meses (2016-07 a
2023-12).

**Verificación de shocks re-confirmada:** train mantiene 27.8% Sutil /
24.4% Dulce (vs. 28%/25% original) — cambio marginal, split sigue
sano (chi² train vs val+test: p=0.20).

**Meses eliminados con shock:** 2016-02 (Sutil +26.5%, Dulce +38.3%)
y 2016-06 (Sutil +25.6%) — ambos apenas superan el umbral P75, no
corresponden a eventos climáticos mayores documentados (año de cierre
de El Niño 2015-16, distinto de El Niño Costero 2017). Pérdida de
1-2 shocks marginales de 90 meses, sin comprometer robustez del split.

## 2026-XX-XX — Deduplicación Ayacucho (Limón Sutil)

**Hallazgo:** 1,061 claves duplicadas (AÑO+MES+COD_UBIGEO+COD_PRODUCTO),
exclusivamente en Ayacucho (0 en otros 23 departamentos, 0 en Limón Dulce).
Hasta 7 filas por clave.

**Causa identificada:** 55% son copias casi exactas (mismo PRODUCCION y
PRECIO_CHACRA, solo varía VERDE_ACTUAL) — consistente con
re-declaraciones/capturas repetidas del mismo registro mensual.

**Decisión:** Agregación por MEDIA (no suma, no máximo) para claves
duplicadas de Ayacucho antes de la agregación distrito→provincia.

**Justificación:** Suma infla Ayacucho ~1.75x (artefacto de captura,
no producción real). Media es neutral ante el ruido.

**Impacto en serie nacional:** Ayacucho = 0.11-0.40% de producción
nacional anual → impacto <0.2% en el total agregado, independiente
de la regla elegida. No afecta el modelo principal (serie nacional).

## 2026-XX-XX — Agregación distrito→provincia: VERDE_ACTUAL y PRECIO_CHACRA

**VERDE_ACTUAL — decisión: incluir como feature de contexto (Canal A)**

Justificación: aunque SIEMBRA y COSECHA son siempre 0 (cultivo permanente,
no aplican mes a mes), VERDE_ACTUAL sí varía y mide superficie en
producción activa (hectáreas). Aporta señal no redundante con PRODUCCION:
permite separar "cuánta tierra está en producción" de "cuánto rinde esa
tierra dado el clima" — exactamente la distinción que el modelo necesita
aprender. Una caída abrupta de VERDE_ACTUAL en una provincia (ej. por
desastre que destruye plantaciones) puede funcionar como señal
anticipatoria de caída de producción futura, similar en espíritu a las
variables climáticas exógenas. Se decide incluirla en el dataset de
features y dejar que el análisis SHAP determine empíricamente su aporte
real al modelo, en lugar de descartarla sin haberla probado.

Agregación distrito→provincia: SUMA (es una medida de superficie,
se agrega igual que PRODUCCION).

**PRECIO_CHACRA — decisión: media ponderada por producción**

Opciones evaluadas:
(A) Media simple de los precios de todos los distritos de la provincia.
(B) Media ponderada por producción de cada distrito. [ELEGIDA]

Justificación: la media ponderada es económicamente más representativa
del precio real que enfrenta la cadena de valor de la provincia. Un
distrito que produce 5,000 t no debe pesar lo mismo en el precio
provincial que uno que produce 1 t — la media simple distorsionaría el
precio hacia distritos marginales con baja producción, mientras que la
ponderada refleja el precio efectivo asociado al grueso de la producción
real de la provincia (relevante para simulaciones de impacto económico
tipo PYME, donde el precio que importa es el de donde se concentra el
volumen).

Fórmula: precio_provincia = Σ(precio_distrito × producción_distrito) / Σ(producción_distrito)

Aplica igual para Limón Sutil y Limón Dulce.

## Observación — Lambayeque-Chiclayo (Limón Sutil)

Chiclayo registra VERDE_ACTUAL>0 en los 120 meses (2016-2025) pero
produccion_t=0 en todos ellos. No distorsiona agregados (peso 0 en
media ponderada), pero se documenta como observación de calidad de
datos MIDAGRI para referencia futura — no requiere acción correctiva.

## Coordenadas climáticas — fallback departamental

**Hallazgo:** 8/107 provincias de Sutil y 3/28 de Dulce carecen de
coordenadas exactas en la fuente base (clima_dataset_final.csv, v1).

**Verificación de impacto:** suma de producción de las provincias
faltantes = 0.252% del total nacional (Sutil), 2.819% (Dulce).
4 de las 8 provincias faltantes de Sutil (Chiclayo, Cañete, Lima,
Talara) tienen producción = 0 en todo el periodo 2016-2025.

**Decisión:** usar centroide del departamento como fallback de
coordenadas para estas provincias marginales, en lugar de descartarlas
o buscar una fuente exacta adicional (no se justifica el esfuerzo
dado el impacto <3% en el peor caso).

**Trazabilidad:** columna `fuente` en
`data/interim/coordenadas_provincias_completo.csv` distingue
`provincia_exacta` (99 filas) vs `departamento_fallback` (10 filas).

## Fuente INDECI — reemplazo por dataset consolidado oficial

**Hallazgo:** las URLs originales de Emergencias2016/2017/2018.xls
(datosabiertos.gob.pe) están rotas desde su publicación (confirmado
vía Wayback Machine). La plataforma rediseñada publica un dataset
consolidado `BD_2003-2025_EMERGENCIAS.csv` (142,139 filas, 49 columnas,
actualizado 2026-08-26).

**Decisión:** usar este único archivo como fuente completa de INDECI
2016-2025, reemplazando los .dbf de 2019-2020, el CSV procesado
2021-2023, y descartando el plan de scraping SINPAD para 2024-2025.

**Verificación de cobertura:** 107/107 provincias productoras de
limón tienen registros de emergencia en el rango completo 2016-2025.
Conteos por año dentro de provincias limoneras: 2016=2,862 · 2017=3,764 ·
2018=2,996 · 2019=2,396 · 2020=2,769 · 2021=4,678 · 2022=4,226 ·
2023=7,487 · 2024=8,260 · 2025=9,319 (tendencia creciente, consistente
con mejor reporte reciente, no necesariamente más emergencias reales).

**Adaptaciones aplicadas al integrar:**
1. Mapeo de nombres de columna (esquema .dbf truncado → esquema CSV moderno)
2. Vocabulario de peligros: filtro final de 10 categorías climáticas
   (LLUVIA INTENSA, VIENTOS FUERTES, BAJAS TEMPERATURAS, INUNDACION,
   DESLIZAMIENTO, HUAYCO, SEQUIA, EROSION, TORMENTA ELECTRICA, MAREJADA).
   Las 12 restantes de las 22 únicas se excluyen por no ser climáticas
   (incendios urbanos/forestales, sismos, derrumbes, actividad
   volcánica, biológicas: plagas/epidemias, y humano-inducidas:
   derrames, contaminación, explosiones). Nota: la columna usa "LLUVIA INTENSA"
   (singular), no "LLUVIAS INTENSAS" como el scraper original.
3. Normalización de LIMA: LIMA METROPOLITANA + LIMA PROVINCIAS → LIMA
4. Parseo de doble formato de fecha

## Scraping de noticias — Agraria.pe (categoría agronegocios, 2016-2025)

**Diagnóstico previo:** scraper v1 obsoleto (slugs cambiados, selectores
de listado rotos, fecha ya no en listado). Corregido en
`src/scraping/agraria_scraper_v2.py`.

**Bug crítico descubierto y corregido:** artículos de 2016 usan
`<div style="text-align:justify">` en vez de `<p>` para el cuerpo —
el extractor original devolvía vacío para todo el año 2016 sin dar
error. Se agregó fallback dual `<p>` + `<div>`, verificado sin cambios
en 3 puntos del rango histórico (2016, ~2020, ~2024) — solo existen
esos 2 formatos, no hay un tercero.

**Filtro de relevancia — 2 niveles:**
- Nivel 1 (match directo): limón, limon, piura, sullana, tumbes, niño,
  senamhi, midagri, lluvias, sequía, helada
- Nivel 2 (contexto agrario + mención de fruta/cítrico/región):
  agroexportación, cosecha, campaña agrícola, producción agrícola,
  sector agrario, clima, cambio climático, irrigación, inundación

**Justificación del filtro de 2 niveles:** el filtro original (solo
keywords directas de limón/clima) producía 0 resultados en páginas
históricas de la categoría `agronegocios` porque esas noticias son
mayoritariamente de comercio/industria general. Se amplió para
capturar también el contexto agrario amplio, que puede correlacionar
con sentimiento de mercado sin mencionar limón explícitamente.

**Robustez del scraper:** se agregó backoff exponencial (5 reintentos,
2s→32s) tras 3 crashes por error DNS transitorio durante la corrida
completa. El checkpoint garantizó cero pérdida de datos en cada
interrupción (manual o por crash).

**Resultado final — categoría `agronegocios`, 1900 páginas, 2016-2025:**
- 2,883 artículos guardados, 0 duplicados reales
- Cobertura: 118/120 meses (98.3%) — huecos únicamente en 2016-01 y
  2016-02
- Composición: 12.7% mención directa de limón (Nivel 1), 87.3% contexto
  agrario amplio (Nivel 2)
- Longitud media del cuerpo: 2,872 caracteres
- Distribución por año: 2016=219, 2017=404, 2018=274, 2019=223,
  2020=161, 2021=210, 2022=228, 2023=338, 2024=416, 2025=410

**Decisión:** el corpus de `agronegocios` se considera SUFICIENTE para
la señal NLP mensual. No se agregan categorías o fuentes adicionales
por ahora (decisión pendiente de confirmación explícita del usuario;
ver nota abajo).

**Limitación declarada:** meses 2016-01 y 2016-02 sin cobertura de
noticias — tendrán `avg_sentiment=0`/`n_noticias=0` en el dataset
maestro, igual que se documentó para el corpus v1.

**Archivo final:** `v2_reentrenamiento/data/interim/noticias/corpus_agronegocios_2016_2025.csv`
(2,883 filas)

## Validación cruzada del índice NLP — correlación con eventos reales

**Resultado del análisis de sentimiento (2,883 noticias, RoBERTuito
zero-shot):**
- Distribución: NEU 67.1%, POS 19.7%, NEG 13.2%
- Media global 2016-2025: +0.0923

**Validación cruzada con eventos climáticos documentados:**
- El Niño Costero 2017 (ene-mar 2017): media trimestral -0.1452,
  con enero 2017 como MÍNIMO ABSOLUTO de toda la serie 2016-2025
  (-0.2464) — detectado sin haber diseñado el índice para ese fin.
- Crisis de precios del limón 2023-24 (jul2023-jun2024): enero 2024
  registra el SEGUNDO mínimo global (-0.2176), coincidiendo
  exactamente con el shock ya identificado independientemente en el
  análisis de producción MIDAGRI (percentil 75 de variación mensual).
- COVID-19 (mar-jun 2020): caída atenuada (mínimo -0.0336 en abril
  2020), notablemente menor que los dos eventos climáticos. Se
  atribuye a que el corpus (categoría agronegocios) contiene
  principalmente noticias factuales/logísticas sobre COVID sin
  carga emocional marcada, a diferencia de la cobertura de desastres
  climáticos que sí genera lenguaje evaluativo negativo.

**Significancia:** esta doble confirmación cruzada (señal NLP
independiente vs. shocks detectados en datos de producción) respalda
la validez del índice de sentimiento como proxy de shocks del sector,
más allá de la simple correlación esperada por diseño.


## 2026-09-03 — Bug de horizonte en GC1 (SARIMA): test replicaba val

**Hallazgo:** en `02_gc1_sarima_prophet.ipynb`, el ajuste final de SARIMA
llamaba dos veces a `forecast(steps=12)` sobre el mismo objeto ajustado.
Como `forecast()` de statsmodels siempre proyecta desde el final de la
serie de entrenamiento y no avanza estado entre llamadas, ambas llamadas
devolvían **el mismo vector**. Las "predicciones de test" (2025) eran en
realidad las de val (2024) duplicadas, evaluadas contra los valores reales
de 2025.

**Corrección:** un único forecast de 24 pasos desde el fin de train; val
toma los pasos 1..12 y test los pasos 13..24.

    f_val_test = np.asarray(fit.forecast(steps=N_VAL + N_TEST))
    pred_val   = f_val_test[:N_VAL]
    pred_test  = f_val_test[N_VAL:]

Esto implica que **test se evalúa a horizonte 13-24 meses**, no 1-12. Es
la lectura honesta del diseño: el modelo no ve 2024 en ningún momento, así
que 2025 está a 13-24 pasos del último dato observado. No se re-ajusta con
val (eso sería fuga de información).

**Alcance del bug — confirmación cruzada:** el grid de selección de
candidatos (576 combinaciones) usa `forecast(steps=N_VAL)` y **no estaba
afectado**: solo evalúa val, que es el paso 1..12 y siempre fue correcto.
La selección de hiperparámetros no se contaminó.

**Confirmación cruzada de que el bug era exclusivo de SARIMA:** tras
re-ejecutar el pipeline completo, `exp_003_prophet_sutil` y
`exp_003_prophet_dulce` regeneraron `metricas.json` y `predicciones.csv`
**byte a byte idénticos** a los previos (solo cambió `fecha_ejecucion` en
`config.yaml`). Prophet nunca tuvo el bug porque predice con
`.predict(future_df)` sobre un DataFrame de fechas explícito, no con un
contador de pasos con estado. Los dos experimentos SARIMA sí cambiaron
predicciones y métricas. Esta asimetría es la verificación de que el
diagnóstico fue correcto y la corrección quedó acotada.

**Impacto:** las métricas de test de SARIMA anteriores al 2026-09-03 son
inválidas y fueron reemplazadas. Naive (exp_001) no usa `forecast()` y no
requirió re-ejecución.

## 2026-09-03 — Sobreajuste por AIC en SARIMA-Sutil — exp_002b como representativo

**Hallazgo:** con el horizonte ya corregido, el SARIMA-Sutil seleccionado
por el procedimiento automático (top-5 por AIC en train, desempate por MAE
en val) generaliza mal:

| | orden | AIC train | MAE val | MAE test | R² test |
|---|---|---:|---:|---:|---:|
| exp_002 (AIC) | (1,1,3)(2,1,0,12) | **1874.93** | 8439.79 | 12031.69 | **−1.11** |
| exp_002b (parsimonia) | (1,1,1)(1,1,0,12) | 1886.52 | 4824.13 | **3638.14** | **+0.755** |

El orden con **mejor** AIC produce el **peor** test: R² negativo significa
que predecir la media de test habría sido mejor, y su MAE_test (12031.69)
es 2.6× el del Naive (4704.29). El AIC premia ajuste en muestra; con 90
observaciones y 6 parámetros estacionales el criterio no penaliza lo
suficiente para una serie con cambio de nivel (ver sección siguiente).

**Decisión:** la comparativa oficial GC1 representa SARIMA-Sutil con
**`exp_002b_sarima_sutil_simple`**. `exp_002_sarima_sutil` se conserva en
`experimentos/` como registro auditable del hallazgo, y NO se borra. El
mapeo está explícito en el dict `EXP_COMPARATIVA` del notebook, de modo que
una re-ejecución completa reproduce la comparativa correcta.

**Cómo se eligió exp_002b (importante para la validez del test):** el orden
(1,1,1)(1,1,0,12) se fijó **a priori** como el SARIMA estacional mínimo
razonable — un término AR, una diferencia, un MA, más su contraparte
estacional. NO hubo búsqueda sobre val ni sobre test, ni se probaron
variantes eligiendo la de mejor MAE_test. Es selección por parsimonia, un
criterio declarado antes de mirar el resultado. De haber barrido órdenes
optimizando test, el MAE_test reportado no sería un estimador honesto.

**Diagnóstico de residuos (exp_002b):** Ljung-Box sin autocorrelación
residual (p>0.05 en lags 6, 12, 18, 24); todas las raíces AR y MA fuera del
círculo unitario (AR mín |r|=1.0643, MA |r|=4.4561); sesgo del MSE en test
1.5%. El modelo parsimonioso es estadísticamente adecuado, no solo más
afortunado.

**SARIMA-Dulce no se modifica:** `exp_002_sarima_dulce` (selección por AIC)
da R²_test = 0.885 y MAE_test = 53.40 (−36.9% vs Naive). El problema no
apareció en esa serie, cuya tendencia es mucho más suave (+2.5%/año vs
+4.0%/año, y salto train→test de +18.2% vs +35.5%).

**Efecto sobre la conclusión de GC1:** con exp_002b, los cuatro pares
cultivo×modelo de GC1 superan al Naive en MAE_test (Sutil: SARIMA −22.7%,
Prophet −21.7%; Dulce: SARIMA −36.9%, Prophet −23.8%). Con exp_002, la
celda SARIMA-Sutil era +155.8% PEOR que el Naive. El cambio de experimento
representativo altera la conclusión sustantiva, no solo una cifra.

**Limitación declarada:** el procedimiento de selección automática por AIC
queda invalidado como criterio único para GC1-Sutil. En modelos posteriores
(GC2, GE, GM) la selección debe evaluarse en val con métrica de error, no
por criterios de información en train.

## 2026-09-03 — Salto de nivel: tendencia secular y sus dos consecuencias

**Hallazgo:** la producción de Limón Sutil tiene una tendencia creciente
sostenida que el split cronológico convierte en un problema de
extrapolación, no de interpolación.

Media anual de `produccion_t_sutil` (t/mes):

    2016  22393    2021  27981
    2017  13584    2022  30558
    2018  21509    2023  23067
    2019  24205    2024  32209
    2020  25132    2025  31908

- CAGR 2016→2025: **+4.01%/año** (Dulce: +2.50%/año)
- Pendiente OLS: +1327 t/año ≈ +5.25%/año sobre la media
- Media train (≤2023) = 23554 · val (2024) = 32209 · test (2025) = 31908
- **Salto de nivel train→test: +35.5%** (Dulce: +18.2%)

Todo modelo entrenado hasta 2023-12 debe proyectar a un régimen ~35% más
alto que el que observó. Esto explica el R² negativo de exp_002: sus
predicciones quedan sistemáticamente por debajo del nivel real de 2025
(errores de ~12000 t con signo consistente), y no es un fallo de
implementación sino la respuesta esperada de un modelo sin término de
tendencia adecuado ante un cambio de nivel de esa magnitud.

**Descomposición de la tendencia (área vs. rendimiento):** usando
`verde_actual_ha` de `data/interim/limon_sutil_provincia.csv`, el
crecimiento de producción se descompone en dos factores independientes:

| | 2016 | 2025 | CAGR |
|---|---:|---:|---:|
| Área en producción (ha) | 260.6 | 317.5 | **+2.22%/año** |
| Rendimiento (t/ha) | 1031.3 | 1205.9 | **+1.75%/año** |
| Producción (t) | 268 722 | 382 899 | **+4.01%/año** |

La descomposición cierra: 1.0222 × 1.0175 = 1.0401. La tendencia secular
NO es un artefacto estadístico ni un efecto de precios — responde a
expansión física de superficie más mejora de productividad, ambas
sostenidas. Esto respalda modelar la tendencia explícitamente (t_index)
en vez de tratarla como deriva a diferenciar.

**Nota de interpretación:** parte del salto 2023→2024 es recuperación tras
la caída de 2023 (crisis de precios del limón y Ciclón Yaku, ya
documentados en la sección de shocks), no solo crecimiento estructural. La
tendencia de +4%/año es real pero está superpuesta a volatilidad de nivel
importante; no debe presentarse como crecimiento suave.

### Decisión (a) — feature `t_index`

Se añade `t_index`, índice temporal lineal 0..113, a
`master_dataset_{sutil,dulce}_v2_features.csv` y su versión escalada
(32 → 33 columnas), para dar a los modelos multivariados un canal explícito
de tendencia secular en vez de esperar que la infieran de los lags.

**Escalado sin fuga:** el StandardScaler se ajusta **solo sobre train**
(90 filas, t_index 0..89) y se aplica a las 114. Verificable en el dataset
escalado: `t_index` va de −1.7129 a +2.6367 con media 0.4619 — la media no
es 0 y el máximo excede +2σ precisamente porque val y test caen fuera del
rango de ajuste. Si el scaler se hubiera ajustado sobre las 114 filas, la
media sería 0. Scalers en
`resultados_v2_final/scalers/scaler_{sutil,dulce}_v2b_tindex.joblib`.

**Limitación declarada:** `t_index` extrapola linealmente fuera de train.
Es una ayuda para captar la deriva de nivel, no un modelo de la tendencia;
a horizontes largos su aporte se degrada y puede sobre-proyectar si el
crecimiento se aplana.

**Alcance actual:** GC1 (SARIMA, Prophet) es **univariado** y corre sobre
`master_dataset_*_v2.csv` crudo — NO consume `t_index`. La feature queda
disponible para GC2/GE/GM. Prophet, por su parte, ya modela tendencia
internamente con su término de trend, lo que explica que sea el único
modelo GC1 que sobrevive bien al salto de nivel en Sutil sin ajuste manual
(R²_test 0.792).

### Decisión (b) — lags one-step-ahead

Se evalúan los modelos LSTM (GE, GM) alimentando los lags con valores
REALES del mes anterior (no con la propia predicción recursiva del
modelo), como decisión de diseño experimental para aislar la capacidad
predictiva del modelo del efecto de acumulación de error recursivo.

**Consecuencia:** esto hace que los modelos multivariados (GC2, GE, GM) NO
sean directamente comparables con GC1 (SARIMA, Prophet) en la tabla de
MAE_test, ya que GC1 se evalúa en modo puramente recursivo (forecast puro
sin retroalimentación de datos reales) mientras que los modelos LSTM
reciben información real del mes previo en cada paso.

**Limitación declarada:** no se ha verificado el rezago real de
publicación de datos de MIDAGRI en un escenario operativo — esta decisión
prioriza la evaluación aislada de capacidad predictiva sobre el realismo
del escenario de despliegue. Validar el rezago real de publicación queda
como trabajo futuro antes de cualquier despliegue productivo del modelo.

## 2026-09-03 — Δs con n_shock=3: la cifra es real, la inferencia no

**SUPERSEDED POR D35-b (2026-09-10):** esta seccion conserva la trazabilidad
del hallazgo sobre n_shock=3, pero el umbral 23.2% citado abajo es historico/
heredado y de procedencia temporal no reproducible. La definicion oficial de
shock, los P75 vigentes y la interpretacion formal de Delta_s quedan fijados
en la seccion D35 al final de este documento.

**Contexto:** Δs = (MAE_shock − MAE_global)/MAE_global × 100 se calcula
sobre los meses de test que superan el umbral P75 de variación mensual
(23.2% para Sutil). En test 2025 eso son **3 meses: 2025-01, 2025-07 y
2025-11**.

**Hallazgo:** SARIMA-Sutil (exp_002b) reporta Δs = −79.25%, es decir MAE en
meses de shock (755.01) muy inferior al MAE global (3638.14). La cifra es
aritméticamente correcta pero **no es evidencia de resiliencia ante
shocks**. Desglose de los errores absolutos en test:

- Meses de shock:   2025-01 → 14.1 · 2025-07 → 822.6 · 2025-11 → 1428.3
- Mayores errores:  2025-04 → 7170.8 · 2025-06 → 7094.3 · 2025-05 → 6153.3
  (los tres **fuera** de meses de shock)

El promedio de shock lo domina 2025-01, con un error de 14.1 t sobre 38325 t
reales (**0.04%**) — una coincidencia numérica, no capacidad predictiva.
Excluyendo ese único mes, MAE_shock sube a 1125 y Δs pasa a ≈ −69%: un
tercio del efecto depende de una sola observación.

**Contraste que lo confirma:** exp_002 (el modelo descartado) reporta
MAE_shock = 12066.7 vs MAE_no-shock = 12020.0, Δs = +0.29%. Un modelo
uniformemente malo produce Δs ≈ 0. Es decir, Δs con n=3 refleja
principalmente **sobre qué tres meses cayó el azar**, no la robustez del
modelo ante perturbaciones.

**Decisión:** Δs se sigue reportando (es la métrica de resiliencia definida
para el proyecto) pero **siempre acompañado de n_shock**, y nunca se
presenta un Δs de Sutil como resultado principal ni como mejora
cuantificada. Redacción prohibida: "el modelo mejora 79% ante shocks".
Redacción aceptable: "Δs = −79.25% sobre n_shock = 3, dominado por un único
mes; no interpretable como resiliencia".

**Limitación declarada:** con 12 meses de test y umbral P75, n_shock ≈ 3 es
el máximo estructuralmente posible en este diseño. Δs no admite contraste
de hipótesis con esta muestra. Una evaluación robusta de resiliencia
requeriría walk-forward validation sobre múltiples ventanas de test, lo que
extendería el número de meses de shock evaluados sin alterar el split
declarado. Queda registrado como trabajo pendiente, no ejecutado.

## 2026-09-07 — Corrección de look-ahead y regeneración completa de Fase 2

Auditoría previa (2026-09-05/07) detectó que la agregación provincia→nacional
de NASA e INDECI ponderaba por la **producción provincial del mismo mes t**:

    ANTES:  C_t = Σ_p( C_{p,t} · Y_{p,t} ) / Σ_p( Y_{p,t} )

Calcular `T2M[t]` exigía conocer la producción provincial de *t*, que es
precisamente lo que se quiere predecir. La media ponderada es invariante al
escalado de los pesos, de modo que el **nivel** nacional no entraba
directamente; lo que entraba era la **composición relativa** entre provincias.
Aun así es un look-ahead operacional: en despliegue esas columnas no son
computables antes de observar y_t.

**Magnitud medida del artefacto:** la ponderación por producción elevaba la
correlación clima–producción de 0.24 a 0.66 (T2M) y de −0.07 a +0.65
(T2M_MAX) frente a la media espacial simple. Buena parte de la señal climática
aparente era un efecto de la ponderación, no del clima.

### Decisiones aprobadas y aplicadas

| Id | Decisión |
|---|---|
| **D14** | Ponderador espacial = `verde_actual_ha` (superficie en producción activa). Cobertura 99.97 % de observaciones >0 (vs 74.9 % Sutil / 56.0 % Dulce de la producción), 0 outliers, CV interanual mediano 0.133/0.000. NO se usa producción como ponderador. |
| **D15** | Resumen temporal = **media** sobre **TRAIN 2016-01..2023-12**. Val 2024 y test 2025 excluidos. Pesos congelados. |
| **D16** | **Vectores independientes por cultivar.** El vector combinado queda PROHIBIDO: Sutil aportaba el 98.35 % del peso (2 261 139 t vs 38 001 t en train), de modo que la serie climática del maestro de Limón Dulce estaba determinada casi por completo por las zonas productoras de Sutil, un régimen climático distinto. |
| **D17** | Sin exclusión de provincias, sin piso mínimo, sin suavizado. Resultado: 106/106 (Sutil) y 28/28 (Dulce) provincias con peso estrictamente positivo. |
| **D20-a** | **`n_provincias` ELIMINADA.** Verificado que era exactamente `#{p : produccion[p,t] > 0}` (coincidencia 120/120 meses en ambos cultivos): una transformación contemporánea del target, no una característica agronómica. Rango 60–94 provincias mes a mes sobre 107, incompatible con realidad agronómica; mide cobertura del reporte MIDAGRI. |
| **D20-b/c** | **`precio_chacra_kg` ELIMINADA** del conjunto predictivo. Se agregaba ponderando por producción (verificado en los dos niveles), viaja en el mismo registro MIDAGRI que el target, y sus ceros son no-observación: `precio = 0` ⟺ `produccion = 0` en el 100 % de los casos (3 118/3 118 Sutil, 1 377/1 377 Dulce). Permanece en `data/interim/` para trazabilidad. |
| **D6** | **Protocolo temporal: FORECAST ROLLING ONE-STEP-AHEAD.** Información hasta el cierre de *t* predice y[t+1]. Ninguna exógena del mes objetivo entra en la matriz predictiva; todas aparecen solo como `lag1/lag3/lag6`. No es nowcasting. |
| **D19** | **SHA-256 como convención nueva de v2.** No existía en v1 ni en la Fase 2 v2 original. |
| **D21** | La cadena `sisagri_2015_2026.xlsx → distrito → provincia → nacional` **no es reproducible**: no existe código en el repositorio que la genere (búsqueda repo-wide; los 4 archivos que la mencionan son consumidores). Los CSV interinos se tratan como **inputs congelados**, registrados por SHA-256. La reconstrucción de Fase 1 queda fuera del alcance de esta corrección. |

### Nueva agregación

    AHORA:  C_{cultivar,t} = Σ_p( w_{cultivar,p} · C_{p,t} ),   w fijo, ajustado solo en TRAIN

Espacio y tiempo quedan separados: primero la agregación espacial crop-aware
(Actividad 02), después los rezagos sobre la serie nacional ya agregada
(Actividad 03). Nunca se rezaga a nivel provincial antes de agregar.

**Cobertura de la masa de peso:** NASA 100.000 % en ambos cultivos; INDECI
100.000 % en Sutil y 97.888 % en Dulce (ANCASH|YUNGAY 0.01126 y ANCASH|CARHUAZ
0.00986 no tienen registros INDECI). El agregador renormaliza sobre la masa
realmente presente cada mes; ambos paneles están balanceados.

### `t_index` — definición recuperada y reproducible

La feature existía en los CSV desde el 2026-09-03 pero **ningún código la
generaba**. Se recuperó su definición por reconstrucción aritmética, verificada
contra los tres valores publicados (min −1.7129, max +2.6367, media +0.4619):

    t_index = 12·(año − 2016) + (mes − 1) − 6

Base 2016-07 = 0; rango 0..113. Se genera **después** del dropna de lags y
**antes** del split y del scaler, con `assert` contra `np.arange(len(df))`
(check, no definición) y contra los valores obligatorios 2016-07=0,
2023-12=89, 2024-01=90, 2025-12=113.

### Consecuencia estructural ya conocida

Con `lookback = 6`, las 114 filas producen **84 secuencias de entrenamiento**
(objetivos 2017-01..2023-12), no 90: los seis primeros meses solo pueden actuar
como contexto. Val y test conservan 12 secuencias cada uno; **enero–diciembre
2025 se evalúa completo**, tomando como contexto de 2025-01 los meses
2024-07..2024-12 (observaciones pasadas, no información futura).

### Esquema resultante

| Artefacto | Antes | Después |
|---|---|---|
| `master_dataset_{c}_v2.csv` | 120 × 18 | **120 × 16** |
| `master_dataset_{c}_v2_features.csv` | 114 × 33 | **114 × 48** |
| `master_dataset_{c}_v2_escalado.csv` | 114 × 33 | **114 × 48** (44 escaladas) |
| Scaler vigente | `scaler_{c}_v2b_tindex.joblib` (29) | **`scaler_{c}_v2c.joblib` (44, n_samples_seen_=90)** |

Los scalers anteriores se movieron a `resultados_v2_final/scalers/obsoletos/`
con su README; el estado previo completo con hashes está en
`resultados_v2_final/pesos/REGISTRO_PRE_REGENERACION.json`.

### Verificación de no afectación de GC1 y del baseline Naive

`produccion_t_{cultivar}` es la **suma** provincial y no depende de los pesos.
Verificado `max|dif| = 0.000000000000` contra `limon_{c}_nacional_mensual.csv`,
y contra la serie `real_t` registrada en `exp_002b_sarima_sutil_simple` y
`exp_003_prophet_dulce` la única diferencia es el redondeo a 2 decimales con
que esos CSV fueron escritos. Ningún archivo de `experimentos/` fue modificado.

### Limitación declarada — problema temporal aún abierto

Congelar los pesos elimina el look-ahead **del ponderador espacial**. No
resuelve la disponibilidad del dato climático/desastre del propio mes: con
granularidad mensual, `C_t` es por definición un agregado del mes completo y no
existe hasta que *t* termina. El protocolo one-step-ahead (D6) evita el
problema por diseño al usar solo rezagos. Los rezagos reales de publicación de
MIDAGRI, NASA POWER e INDECI siguen **NO VERIFICADOS**; para INDECI hay
evidencia indirecta de consolidación retrospectiva (conteos anuales crecientes
2016=2 862 → 2025=9 319, atribuidos a mejor reporte). Por eso las variables
INDECI se usan exclusivamente rezagadas y no se asume que sus valores
consolidados estuvieran disponibles en tiempo real.

## 2026-09-10 - D35: metricas globales y evaluacion condicional ante shocks

**Estado:** D35-a CERRADO y D35-b CERRADO.

**Alcance:** decision documental para v2. No entrena modelos, no recalcula
resultados historicos, no modifica datasets, scalers ni notebooks, y no cambia
artefactos de experimentos ya guardados.

**Trazabilidad interna:**

- `v2_reentrenamiento/auditorias/AUDITORIA_D35_ESTACIONALIDAD_TRAIN.md`
- `v2_reentrenamiento/auditorias/AUDITORIA_D35_P75_SHOCKS.md`
- `v2_reentrenamiento/auditorias/RECONSTRUCCION_D35_P75_TRAIN_ONLY.md`

La reconstruccion TRAIN-only es la fuente vigente para P75.

### D35-a - metricas globales

**Estado:** CERRADO.

**Metrica primaria:** MAE.

- Se calcula sobre valores en toneladas, despues de inverse scaling cuando
  corresponda.
- Debe calcularse sobre la misma ventana de evaluacion para todos los modelos
  comparados.
- Es el criterio principal de error predictivo global.
- Su interpretacion es directa en unidades fisicas.

**Metrica complementaria:** RMSE.

- Se calcula tambien en toneladas.
- Complementa MAE dando mayor peso a errores grandes.
- No sustituye a MAE como criterio primario.

**Comparacion directa contra baseline:**

```text
RelMAE_N1 = MAE_modelo / MAE_Naive_t-1
```

Ambos MAE deben calcularse sobre exactamente los mismos meses.

Interpretacion:

- `RelMAE_N1 < 1`: el modelo tiene menor MAE que Naive t-1.
- `RelMAE_N1 = 1`: el modelo tiene el mismo MAE que Naive t-1.
- `RelMAE_N1 > 1`: el modelo tiene mayor MAE que Naive t-1.

Si se expresa `(1 - RelMAE_N1) * 100`, debe denominarse "reduccion relativa
del MAE frente al Naive". No debe llamarse automaticamente "skill score
estandar".

**Metricas escaladas complementarias:** MASE_1 y RMSSE_1.

Se fija `m=1` para ambos cultivares y para ambas metricas. No se selecciona un
`m` distinto por cultivar.

Los denominadores se calculan exclusivamente con la serie objetivo original
TRAIN 2016-01..2023-12, con `N target = 96` meses y 95 diferencias. Nunca se
calculan denominadores MASE/RMSSE usando validation o test.

MASE:

```text
D_MASE_1 = mean(|y_t - y_(t-1)|), TRAIN
MASE_1 = MAE_OOS / D_MASE_1
```

RMSSE:

```text
D_RMSSE_1 = mean((y_t - y_(t-1))^2), TRAIN
RMSSE_1 = sqrt(MSE_OOS / D_RMSSE_1)
```

Equivalente:

```text
RMSSE_1 = RMSE_OOS / sqrt(D_RMSSE_1)
```

Denominadores TRAIN auditados:

| Cultivar | D_MASE_1 | D_RMSSE_1 |
|---|---:|---:|
| Sutil | 3374.5715 | 18749601.6694 |
| Dulce | 73.3380 | 7404.7927 |

**Justificacion de m=1:** la auditoria TRAIN mostro comportamiento estacional
diferente entre cultivares:

| Cultivar | ACF lag12 | Comparacion TRAIN comun | Ratio MAE seasonal/naive |
|---|---:|---|---:|
| Sutil | 0.5652 | Seasonal Naive t-12 peor que Naive t-1 | 1.6882 |
| Dulce | 0.8437 | Seasonal Naive t-12 mejor que Naive t-1 | 0.3180 |

Sin embargo, no se adoptan denominadores distintos por cultivar. Se fija `m=1`
de manera homogenea porque el baseline operacional oficial es Naive t-1, evita
seleccionar post hoc el escalador segun que benchmark funcione mejor en cada
cultivar, mantiene interpretacion comun entre cultivares y documenta la
estacionalidad como propiedad de las series sin convertirla automaticamente en
un denominador diferente.

Seasonal Naive t-12 puede conservarse como diagnostico complementario de
estructura estacional, pero no es el escalador oficial de D35.

**R2:** R2 se conserva como metrica descriptiva secundaria. No debe utilizarse
como criterio principal para declarar superioridad de un modelo. No se eliminan
R2 ni resultados historicos ya registrados.

**Orden recomendado de reporte global:**

1. MAE
2. RMSE
3. RelMAE_N1
4. MASE_1
5. RMSSE_1
6. R2

MAE es la metrica primaria.

### D35-b - evaluacion condicional ante shocks

**Estado:** CERRADO.

Para cada cultivar `c`:

```text
r_t = abs((y_t - y_(t-1)) / y_(t-1))
P75_c = Q_0.75(r_t)
```

`P75_c` se estima exclusivamente usando TRAIN 2016-01..2023-12, con
`N target = 96` meses y `N cambios relativos = 95`. Validation 2024 y test
2025 no participan en la estimacion del P75. Los umbrales quedan congelados
antes de la evaluacion fuera de muestra.

**P75 oficiales v2:**

| Cultivar | P75 oficial, proporcion | P75 oficial, porcentaje |
|---|---:|---:|
| Sutil | 0.240834900212216 | 24.0834900212216% |
| Dulce | 0.320281354618397 | 32.0281354618397% |

La implementacion debe usar el valor de precision completa. Los porcentajes
redondeados son solo para presentacion.

Los antiguos valores Sutil = 23.2% y Dulce = 33.9% quedan identificados como
umbrales historicos/heredados de procedencia temporal no reproducible. No son
los umbrales oficiales v2. Cualquier aparicion previa se conserva solo como
trazabilidad historica superseded.

**Regla de clasificacion:**

```text
shock_t = 1 si r_t > P75_c
shock_t = 0 en otro caso
```

La comparacion es estricta (`>`). Para enero 2025, `y_(t-1)` es la produccion
de diciembre 2024. Ese contexto historico esta permitido para calcular la
variacion enero 2025. El P75 permanece congelado y no se recalibra con 2024 ni
2025.

**Shock mask de test 2025 con P75 TRAIN-only oficial:**

| Cultivar | Shocks test 2025 | n_shock |
|---|---|---:|
| Sutil | 2025-01, 2025-07, 2025-11 | 3 |
| Dulce | 2025-01, 2025-02, 2025-03 | 3 |

Los nuevos P75 exactos difieren de los valores historicos, pero no modifican la
clasificacion de shocks de test 2025. El cambio corrige trazabilidad y
reproducibilidad metodologica sin cambiar los seis meses actualmente
clasificados como shock.

**Metricas condicionales minimas:**

- MAE_global
- MAE_shock
- MAE_nonshock
- n_shock
- n_nonshock
- Delta_s

La formula de Delta_s se mantiene:

```text
Delta_s = ((MAE_shock - MAE_global) / MAE_global) * 100
```

MAE_global incluye todos los meses de evaluacion, incluidos los meses shock.
Por tanto, Delta_s debe interpretarse junto con MAE_shock y MAE_nonshock.

Delta_s queda definido formalmente como indice descriptivo de deterioro
condicional ante shocks propuesto/definido en este estudio. No debe presentarse
como metrica estandar universal de resiliencia, prueba estadistica, estimador
causal ni demostracion general de robustez climatica.

Interpretacion:

- `Delta_s > 0`: el MAE en meses shock fue mayor que el MAE global.
- `Delta_s = 0`: el MAE en meses shock fue igual al MAE global.
- `Delta_s < 0`: el MAE en meses shock fue menor que el MAE global.

Las comparaciones entre modelos pueden describir menor o mayor deterioro
observado.

**Limitacion por n_shock:** test 2025 contiene solo `n_shock = 3` por
cultivar. Por ello, MAE_shock, MAE_nonshock y Delta_s son resultados
descriptivos/condicionales sobre los episodios observados. No debe formularse
"se demostro estadisticamente mayor resiliencia". Preferir formulaciones como
"presento menor deterioro en los episodios de shock observados".

**No DM automatico:** D35 no incorpora automaticamente Diebold-Mariano ni otra
prueba de significancia. Con horizonte final de 12 meses y subconjunto shock de
3 observaciones, la significancia no se usa como requisito de superioridad.
Cualquier inferencia adicional requiere una decision metodologica separada.

**Incertidumbre multi-seed:** si D35 se menciona junto con evaluacion
multi-seed, debe aclararse que la variabilidad entre seeds de modelos
estocasticos no equivale a incertidumbre estadistica por multiples realizaciones
temporales del test. No debe presentarse la distribucion multi-seed como si
aumentara `n=12` o `n_shock=3`. La politica exacta de seeds permanece en su
decision metodologica especifica.

## 2026-09-10 - D4/D36/D7/D3-op: arquitectura neuronal GC3/GE y uso de validation

**Estado:** D4 CERRADO; D36 CERRADO; D7 CERRADO; D3-op CERRADO.

Esta decision formaliza solo el diseno metodologico de GC3 y GE en v2. No
implementa modelos, no entrena redes, no ejecuta HPO y no modifica datasets,
scalers, features, resultados, notebooks ni PPI. La fuente tecnica de apoyo es
`v2_reentrenamiento/auditorias/AUDITORIA_D4_D36_ARQUITECTURA_GC3_GE.md`.
D35 permanece cerrado y no se reabre en esta decision.

### D36 - Estructura funcional GC3/GE

GC3 y GE mantienen dos ramas recurrentes funcionales:

- Rama A: informacion autoregresiva.
- Rama B: informacion exogena.

**Rama A - autoregresiva, comun a GC3 y GE:**

La Rama A contiene exactamente 4 inputs:

- `produccion_t_{cultivar}`
- `produccion_t_{cultivar}_lag1`
- `produccion_t_{cultivar}_lag3`
- `produccion_t_{cultivar}_lag6`

**Rama B GC3 - exogenas no NLP:**

La Rama B de GC3 contiene exactamente 33 inputs:

- `mes_sin`
- `mes_cos`
- `t_index`
- NASA POWER rezagado en `lag1`, `lag3` y `lag6` para 5 variables:
  `T2M`, `T2M_MAX`, `WS2M`, `PRECTOTCORR`, `RH2M`
- INDECI rezagado en `lag1`, `lag3` y `lag6` para 5 variables:
  `num_emergencias`, `personas_afectadas`, `personas_damnificadas`,
  `hectareas_cultivo_perdidas`, `hectareas_cultivo_afectadas`

Total GC3: `4 + 33 = 37` inputs.

**Rama B GE - exogenas no NLP + NLP rezagado:**

La Rama B de GE contiene los mismos 33 inputs de GC3 mas 6 variables NLP
rezagadas:

- `avg_sentiment_lag1`
- `avg_sentiment_lag3`
- `avg_sentiment_lag6`
- `n_noticias_lag1`
- `n_noticias_lag3`
- `n_noticias_lag6`

Total GE: `4 + 39 = 43` inputs.

La comparacion GC3 -> GE queda definida como ablacion del valor incremental de
NLP. GC3 y GE deben mantener identicos:

- arquitectura
- unidades
- attention
- Dense
- dropout
- optimizer
- learning rate
- batch size
- max epochs
- callbacks
- seeds
- shuffle
- split
- scaler
- protocolo de evaluacion

La unica diferencia estructural prevista entre GC3 y GE es la entrada de seis
variables NLP rezagadas adicionales en la Rama B de GE.

**SUPERSEDED POR D36:** cualquier referencia activa o historica a `36 inputs`
para GC3 o `42 inputs` para GE queda obsoleta. Los conteos oficiales v2 son
GC3 = 37 inputs y GE = 43 inputs. En este archivo no se localizo una referencia
activa previa 36/42; si aparece en handoffs, auditorias o documentacion antigua,
debe leerse solo como trazabilidad superseded.

### D4 - Arquitectura neuronal v2

Para cada cultivar y para ambos modelos GC3/GE, la arquitectura neuronal v2
queda cerrada como:

```text
Rama A:
LSTM(16, return_sequences=True)
-> BahdanauAttention con dimension/capacidad 16

Rama B:
LSTM(16, return_sequences=True)
-> BahdanauAttention con dimension/capacidad 16

Concatenate(context_A, context_B)
-> Dense(16, activation='relu')
-> Dropout(0.20)
-> Dense(8, activation='relu')
-> Dense(1)
```

Restricciones arquitectonicas:

- una sola capa LSTM por rama;
- no stacked LSTM;
- no bidirectional LSTM.

Regularizacion:

- `dropout = 0.20`
- `L2 = 0`

Optimizer:

- `Adam`
- `learning_rate = 0.001`

Compilacion conceptual:

- `optimizer = Adam(learning_rate=0.001)`
- `loss = MSE`
- `metric = MAE`

Entrenamiento:

- `batch_size = 8`
- `max_epochs = 300`

Callbacks:

- `EarlyStopping`: `monitor = "val_loss"`, `patience = 15`,
  `restore_best_weights = True`.
- `ReduceLROnPlateau`: `monitor = "val_loss"`, `factor = 0.5`,
  `patience = 8`, `min_lr = 1e-6`.

No se agregan hiperparametros adicionales en esta decision.

#### D4-loss - Loss oficial de entrenamiento GC3/GE

**Estado:** CERRADO.

GC3 y GE usaran:

- Training loss: Mean Squared Error (MSE).
- Metrica auxiliar durante `fit`: Mean Absolute Error (MAE).

La metrica primaria de evaluacion fuera de muestra continua siendo MAE segun
D35-a. Esto no constituye contradiccion: la loss optimiza los pesos durante el
entrenamiento y las metricas oficiales evaluan el desempeno predictivo fuera de
muestra.

En los callbacks:

- `val_loss` = MSE sobre validation 2024.
- `EarlyStopping` monitorea `val_loss`.
- `ReduceLROnPlateau` monitorea `val_loss`.

Validation 2024 se utiliza unicamente conforme a D3-op para EarlyStopping,
ReduceLROnPlateau, restauracion del mejor estado de entrenamiento y diagnostico
de convergencia/generalizacion. No se usa validation para comparar MSE vs MAE
vs Huber u otras losses. No se realiza seleccion retrospectiva de loss.

Justificacion:

1. MSE era la loss historica de GC3/GE v1.
2. MSE es una loss estandar de regresion para forecasting.
3. Se preserva continuidad experimental sin introducir un nuevo hiperparametro
   ni una busqueda adicional.
4. MAE sigue siendo primaria para evaluacion porque D35-a asi lo establece.
5. No se afirma que MSE sea universalmente superior a MAE.
6. No se probo MSE contra otras losses usando validation ni test.

Requisito futuro de `History`: cada corrida GC3/GE debe guardar `loss`,
`val_loss`, `mae`, `val_mae` y `learning_rate` para diagnostico grafico
posterior.

**Justificacion metodologica:** se adopta una arquitectura compacta
preespecificada debido al regimen Small Data (`84` secuencias efectivas TRAIN),
preservando DualLSTM + Attention y evitando una busqueda extensiva de
arquitectura sobre validation de solo 12 meses. La literatura sobre series
individuales cortas respalda la cautela frente a RNN profundas o con muchos
parametros; sin embargo, no se afirma que la literatura recomiende exactamente
16 unidades. La eleccion de 16 unidades es una decision parsimoniosa
preespecificada y justificada para v2.

Conteos auditados de parametros:

| Arquitectura | GC3 params | GE params | Delta GE-GC3 | Incremento relativo |
|---|---:|---:|---:|---:|
| HEREDADA | 68,577 | 70,113 | 1,536 | 2.24% |
| COMPACTA-16 adoptada | 6,273 | 6,657 | 384 | 6.12% |

El cociente parametros/secuencia es un descriptor de complejidad en regimen
Small Data y no constituye un criterio formal de validez o invalidez de una
arquitectura.

### D7 - Shuffle

Para GC3 y GE en v2 se fija:

```text
shuffle = False
```

Motivo: decision conservadora para mantener el orden cronologico y reforzar la
reproducibilidad del entrenamiento.

Debe distinguirse entre:

- mezclar observaciones antes de crear ventanas temporales: no permitido;
- mezclar ventanas ya formadas durante SGD: no implica automaticamente leakage
  si cada ventana esta correctamente construida, pero no se utilizara en v2.

### D3-op - Uso operativo de validation 2024

Validation 2024 no puede utilizarse para:

- escoger entre `LSTM8`, `LSTM16`, `LSTM32` o `LSTM64`;
- seleccionar arquitectura;
- hacer GridSearch;
- hacer RandomSearch;
- ejecutar Optuna;
- ejecutar busqueda bayesiana;
- probar multiples combinaciones y elegir la mejor;
- seleccionar una seed ganadora.

Validation 2024 si puede utilizarse para:

- `EarlyStopping`;
- `ReduceLROnPlateau`;
- checkpoint o restauracion del mismo entrenamiento preespecificado;
- controles tecnicos de convergencia/generalizacion.

Roles por split:

- TRAIN: aprendizaje de parametros.
- VALIDATION 2024: control del proceso de entrenamiento preespecificado.
- TEST 2025: evaluacion final unicamente.

El test nunca interviene en seleccion, arquitectura, hiperparametros,
callbacks, thresholds, seeds ni definicion de metricas.

## 2026-09-10 - D0/D10: reproducibilidad y protocolo multi-seed GC3/GE

**Estado:** D0 CERRADO; D10 CERRADO.

Esta decision formaliza el protocolo de reproducibilidad y multi-seed para GC3
y GE en v2. No implementa modelos, no entrena redes, no ejecuta seeds, no
repara el entorno, no usa validation 2024 ni test 2025, y no modifica datasets,
scalers, features, resultados ni notebooks.

Fuente principal:

- `v2_reentrenamiento/auditorias/AUDITORIA_D0_D10_REPRODUCIBILIDAD_MULTISEED.md`

### D10 - Protocolo multi-seed GC3/GE

Para GC3 y GE se fija antes de cualquier entrenamiento oficial:

```text
seeds = [0,1,2,3,4,5,6,7,8,9]
```

Total: 10 seeds.

La eleccion es un compromiso metodologico entre caracterizar variabilidad
estocastica, evitar dependencia de una unica inicializacion y mantener un costo
computacional razonable. No se afirma que 10 sea un numero universalmente
optimo.

Queda prohibido:

- seleccionar la seed con mejor MAE;
- descartar seeds por bajo rendimiento salvo fallo tecnico verificable;
- cambiar la lista despues de observar resultados.

GC3 y GE deben ejecutarse emparejados por seed:

```text
GC3(seed=s) <-> GE(seed=s), para s = 0..9
```

Las mismas seeds no implican inicializaciones numericamente identicas entre GC3
y GE, porque las dimensiones de entrada difieren. Su finalidad es controlar el
protocolo de aleatoriedad de forma comparable.

Se deben reportar todas las seeds individuales y, como resumen, para MAE y las
demas metricas oficiales cuando corresponda:

- media;
- mediana;
- desviacion estandar;
- minimo;
- maximo.

La variabilidad entre seeds no debe interpretarse como intervalo de confianza
temporal ni como incertidumbre de muestreo de la serie. Describe sensibilidad
del entrenamiento estocastico bajo un mismo protocolo.

### D0 - Reproducibilidad controlada

Para v2, reproducibilidad se define como reproducibilidad controlada dentro de
un entorno software/hardware congelado.

No se promete identidad bit-a-bit entre hardware, sistemas operativos, drivers
o versiones diferentes.

En la implementacion posterior debe existir una unica funcion central de
determinismo. Esa funcion debe controlar como minimo:

- Python `random`;
- NumPy;
- TensorFlow/Keras;
- `PYTHONHASHSEED`;
- operaciones deterministas de TensorFlow cuando sean compatibles.

API preferida segun compatibilidad del entorno final:

```text
keras.utils.set_random_seed(seed)
```

y:

```text
tf.config.experimental.enable_op_determinism()
```

o API equivalente vigente.

`TF_DETERMINISTIC_OPS=1` puede utilizarse cuando corresponda.

`TF_ENABLE_ONEDNN_OPTS=0` se documenta como medida conservadora para el entorno
CPU v2, no como requisito universal de reproducibilidad.

Las variables de entorno que deban actuar antes de inicializar TensorFlow deben
configurarse antes de importar o inicializar TensorFlow.

Metadata minima por corrida:

- seed;
- cultivar;
- modelo;
- Python version;
- TensorFlow version;
- Keras version;
- NumPy version;
- OS;
- CPU/GPU;
- determinism settings;
- oneDNN setting;
- timestamp;
- git commit/hash;
- hashes de datasets;
- hashes de scalers;
- hash/configuracion del modelo.

### Historial de entrenamiento

Como requisito futuro, sin implementarlo todavia, cada corrida GC3/GE debe
preservar:

- epoch;
- loss;
- val_loss;
- learning_rate;
- best_epoch;
- stopped_epoch.

Esto permitira generar curvas TRAIN/VAL y auditar convergencia/sobreajuste sin
seleccionar retrospectivamente arquitecturas.

Cada seed tendra sus propios artefactos y nunca debe sobrescribir otra seed.

### XGBoost / GC2

Esta decision no cierra todavia la aplicacion multi-seed a GC2.

Si la configuracion final GC2 contiene estocasticidad relevante, por ejemplo
`subsample < 1`, `colsample_bytree < 1` u otra fuente equivalente, se evaluara
usar las mismas 10 seeds.

Si la configuracion final GC2 es esencialmente determinista con `random_state`
fijado, no debe repetirse automaticamente 10 veces sin justificacion.

La politica de seeds para GC2 se decidira al cerrar el protocolo GC2.
## 2026-09-11 - D37-D45: protocolo GC2/XGBoost v2

**Estado:** D37, D38, D39, D40, D41, D42, D43, D44 y D45
**CERRADAS**.

Esta decision formaliza el protocolo metodologico de GC2/XGBoost v2. No
entrena XGBoost, no ejecuta `model.fit()`, no hace HPO, no abre TEST 2025, no
modifica datasets ni scalers, no modifica GC3/GE y no altera resultados
oficiales existentes.

GC2 queda definido como XGBoost tabular NO-NLP. La configuracion se documenta
como configuracion v2 preespecificada y congelada, anclada en antecedentes
historicos v1 y completada con defaults explicitos, sin optimizacion sobre v2.
No se afirma que sea optima.

### D37 - Features GC2

GC2/XGBoost usa exactamente las 37 features NO-NLP de GC3.

Produccion:

- `produccion_t_{cultivar}`
- `produccion_t_{cultivar}_lag1`
- `produccion_t_{cultivar}_lag3`
- `produccion_t_{cultivar}_lag6`

Temporales:

- `mes_sin`
- `mes_cos`
- `t_index`

NASA POWER rezagado en `lag1`, `lag3` y `lag6`:

- `T2M`
- `T2M_MAX`
- `WS2M`
- `PRECTOTCORR`
- `RH2M`

INDECI rezagado en `lag1`, `lag3` y `lag6`:

- `num_emergencias`
- `personas_afectadas`
- `personas_damnificadas`
- `hectareas_cultivo_perdidas`
- `hectareas_cultivo_afectadas`

Quedan excluidos explicitamente:

- NLP;
- `precio_chacra_kg`;
- `n_provincias`;
- `total_afectados`;
- exogenas contemporaneas;
- `lag2`;
- rolling mean/std;
- cualquier feature nueva post-TEST.

### D38 - Representacion temporal

GC2/XGBoost es tabular y usa:

```text
X_t -> y_(t+1)
```

No se construyen ventanas LSTM.

TRAIN:

- X: 2016-07..2023-11
- targets: 2016-08..2023-12
- n = 89 pares

VAL:

- X: 2023-12..2024-11
- targets: 2024-01..2024-12
- n = 12 pares

No se restringe XGBoost artificialmente a las 84 observaciones de la LSTM. La
comparacion con GC3/GE exige misma informacion disponible, target, horizonte y
periodo de evaluacion, no identico `n` TRAIN cuando las arquitecturas tienen
requerimientos diferentes.

### D39 - Scaling

GC2 usa exclusivamente:

```text
master_dataset_{cultivar}_v2_escalado.csv
```

No se vuelve a escalar y no se refittea scaler. El scaling se conserva por
trazabilidad y consistencia de pipeline, no porque XGBoost lo necesite
algoritmicamente. El target se modela en escala estandarizada. En evaluacion
futura, las predicciones y valores reales se invertiran a toneladas con el
scaler v2c TRAIN-only.

### D40 - Estrategia de hiperparametros

No hay HPO, no hay grid y no hay seleccion mediante TimeSeriesSplit. La
configuracion queda preespecificada antes del entrenamiento GC2. No se usan
resultados TEST de GC3/GE para justificarla.

### D41 - Configuracion oficial XGBoost

Configuracion oficial:

```text
objective = "reg:squarederror"
eval_metric = "mae"
booster = "gbtree"
max_depth = 2
min_child_weight = 1
learning_rate = 0.05
n_estimators = 200
subsample = 0.8
colsample_bytree = 0.8
reg_alpha = 0.0
reg_lambda = 1.0
gamma = 0.0
tree_method = "hist"
n_jobs = 1
random_state = seed
```

`min_child_weight=1` queda cerrado explicitamente. No usar `3`.

### D42 - Early stopping

No se usa early stopping. `n_estimators` queda fijo en 200. VAL 2024 no
selecciona `best_iteration`.

### D43 - Seeds/stochasticity

Seeds oficiales GC2:

```text
0,1,2,3,4,5,6,7,8,9
```

Se usan porque `subsample=0.8` y `colsample_bytree=0.8` introducen
stochasticity real. El total futuro esperado es:

```text
2 cultivares x 10 seeds = 20 corridas
```

No se selecciona best seed. La variabilidad entre seeds describe sensibilidad
a la stochasticity del boosting, no incertidumbre temporal.

### D44 - Validacion

VAL 2024 se usa solo como diagnostico/pre-flight. No se usa para HPO,
seleccion de hiperparametros, early stopping, seleccion de seed ni seleccion
de `n_estimators`. No se usa TRAIN-only CV porque D40 cierra la configuracion
sin tuning. TEST 2025 permanece prohibido hasta autorizacion de evaluacion
final.

### D45 - Reproducibilidad y artefactos

Cada futura corrida oficial debe guardar como minimo:

- config;
- metadata;
- modelo;
- feature_list;
- seed y random_state;
- versiones;
- OS;
- CPU/GPU;
- tree_method;
- n_jobs;
- hash dataset;
- hash scaler;
- hash modelo;
- hash codigo/git;
- timing;
- logs;
- predicciones VAL diagnosticas;
- metricas VAL diagnosticas;
- estado de corrida.

Debe registrar ademas:

- `train_first_x`;
- `train_first_target`;
- `train_last_x`;
- `train_last_target`;
- `train_n`;
- `val_first_x`;
- `val_first_target`;
- `val_last_x`;
- `val_last_target`;
- `val_n`;
- `test_loaded = false`;
- `hpo_performed = false`;
- `early_stopping = false`;
- `best_seed_selection = false`;
- lista de exclusiones verificadas.

## 2026-09-12 - D46-D50: protocolo SARIMA rolling one-step v2

**Estado:** D46, D47, D48, D49 y D50 **CERRADAS**.

Esta decision formaliza el protocolo SARIMA rolling one-step para la futura
comparacion principal v2. No abre TEST 2025, no genera forecasts TEST, no
calcula metricas TEST, no re-selecciona ordenes y no modifica los resultados
fixed-origin existentes de GC1.

### D46 - Mecanismo rolling

El mecanismo aprobado es:

```text
forecast(steps=1)
SARIMAXResults.append([y_real], refit=False)
```

Los parametros SARIMA permanecen congelados. No se permite refit mensual. La
actualizacion secuencial incorpora la observacion real ya disponible para
actualizar el estado del filtro, no para reestimar coeficientes.

### D47 - Periodo de estimacion

Se mantiene exactamente el TRAIN historico real de GC1:

```text
2016-07..2023-12
```

No se amplia retrospectivamente a 2016-01. La razon es que ese fue el periodo
efectivamente usado por GC1 vigente; modificarlo despues del cierre del modelo
redefiniria la muestra de estimacion. La comparabilidad entre familias exige el
mismo horizonte y origen informativo, no identico numero de observaciones de
entrenamiento.

### D48 - Tratamiento de VAL 2024

VAL 2024 se usa exclusivamente como flujo observado para actualizacion
secuencial de estado:

```text
modelo ajustado en TRAIN hasta 2023-12
append Jan-2024 con refit=False
...
append Dec-2024 con refit=False
```

VAL no se usa para reestimar parametros, seleccionar hiperparametros,
seleccionar modelos ni modificar GC1. Al finalizar, el estado queda actualizado
hasta 2024-12 con los mismos coeficientes estimados originalmente.

### D49 - Especificacion por cultivar

No se impone una unica especificacion SARIMA a ambos cultivares. Se conservan
las especificaciones GC1 ya existentes y congeladas:

```text
SUTIL:
order = (1,1,1)
seasonal_order = (1,1,0,12)
fuente = exp_002b_sarima_sutil_simple

DULCE:
order = (1,0,0)
seasonal_order = (0,1,0,12)
fuente = exp_002_sarima_dulce
```

No se ejecuta grid search, auto_arima, AIC/BIC ni ningun criterio de
re-seleccion.

### D50 - Reproducibilidad

La futura evaluacion rolling debe registrar como minimo:

- cultivar;
- order;
- seasonal_order;
- train_first;
- train_last;
- train_n;
- val_first;
- val_last;
- val_n;
- statsmodels_version;
- fit_params iniciales;
- hash dataset;
- hash codigo;
- git hash;
- timestamp.

Y por cada actualizacion:

- observed_date;
- observed_y;
- forecast_origin;
- forecast_target;
- append_refit = false.

Debe verificarse que los parametros despues de cada `append(refit=False)` son
identicos a los parametros iniciales dentro de tolerancia numerica.

### Pre-flight final

El pre-flight final corregido se ejecuto solo con TRAIN+VAL:

```text
v2_reentrenamiento/auditorias/AUDITORIA_PREFLIGHT_FINAL_SARIMA_ROLLING.md
v2_reentrenamiento/auditorias/sarima_rolling_preflight_final.json
```

Resultado:

```text
status = approved
38/38 controles OK
TEST 2025 cargado = NO
forecasts TEST = NO
metricas TEST = NO
refit durante VAL = NO
```

## 2026-09-12 - D51-D61: cierre formal del protocolo SHAP v2

**Estado: D51-D61 CERRADAS por aprobacion expresa del usuario.** Este cierre
es documental. SHAP TEST OFICIAL TODAVIA NO EJECUTADO. La siguiente sesion
debe comenzar por la auditoria/preflight del script oficial; solo despues
de verificarlo procede la ejecucion post-hoc prevista. No se ejecuta hoy.

### Decisiones aprobadas

| ID | Decision cerrada | Estado |
|---|---|---|
| D51 | SHAP para GC3, GE y XGBoost. No forzar SHAP en Naive/SARIMA. | CERRADA |
| D52 | GC3/GE: PermutationExplainer, RNG=1729, max_evals GC3=7120 y GE=8272. Fallback SamplingExplainer nsamples=65536, mismo background, exclusivamente por fallo tecnico real. | CERRADA |
| D53 | XGBoost: TreeExplainer. | CERRADA |
| D54 | Todas las 10 seeds oficiales 0..9, por cultivar/modelo. No best seed ni seed representativa. | CERRADA |
| D55 | 32 referencias exclusivamente TRAIN por cultivar; indices aproximadamente equiespaciados, seleccion determinista, mismos indices entre seeds correspondientes. Guardar indices exactos y hashes. | CERRADA |
| D56 | Preservar SHAP firmado elemental sample x timestep x feature antes de agregar. | CERRADA |
| D57 | Grupos: produccion historica, temporalidad, NASA/clima, INDECI, NLP solo GE; nombres de builders oficiales. | CERRADA |
| D58 | Shock/nonshock solo descriptivo; n_shock=3 por cultivar, n_nonshock=9. | CERRADA |
| D59 | NLP: mean absolute SHAP, participacion relativa en total absoluto, ranking de seis variables y shock/nonshock; sin causalidad. | CERRADA |
| D60 | Attention solo como diagnostico separado si posteriormente se decide implementarlo. No attention=explanation. | CERRADA |
| D61 | Reproducibilidad completa: versiones, hashes, background, parametros, shapes, tiempos, seeds, outputs y errores de reconstruccion. | CERRADA |

### D52 - Justificacion previa al SHAP oficial TEST

PermutationExplainer se eligio **antes** del SHAP oficial TEST y solo por
compatibilidad con GC3/GE, reproducibilidad, estabilidad numerica,
fidelidad/reconstruccion, ausencia de warnings/excepciones de los explainers
y coste viable. No se eligio por resultados cientificos, ranking deseado de
variables, apariencia de figuras ni desempeno predictivo TEST.

Evidencia: `auditorias/AUDITORIA_BENCHMARK_EXPLAINER_SHAP_V2.md` y
`auditorias/shap_v2_explainer_benchmark.json`. Benchmark solo TRAIN+VAL,
ambos cultivares, GC3/GE seed 0 como centinela tecnico; dos objetivos VAL
(2024-01, 2024-07) por centinela. 156 corridas neuronales y 12 TreeExplainer.
TEST no se uso para generar SHAP ni para elegir explainer/background.

- Maximo error de reconstruccion neuronal observado: 1.30385160446167e-7
  (aproximadamente 1.30e-7), en unidades escaladas.
- Repetir igual RNG/config produjo SHAP identico.
- Spearman del ranking elemental entre RNG para Permutation con N=32 y
  presupuesto alto: 0.9835..0.9920.
- Coste extrapolado de 480 explicaciones neuronales: 602.84 s, mas IO/informes.
- Sin warnings/excepciones de explainers en el benchmark final. Los warnings
  de entorno/carga Keras se documentan por separado; no se modificaron capas.

**Limitacion:** dos muestras VAL por centinela no certifican estabilidad de
todas las futuras explicaciones, meses o seeds. Aditividad pequena no prueba
convergencia de cada atribucion. El enmascaramiento marginal puede romper
dependencias entre lags; no implica causalidad.

Se conserva la implementacion tecnica probada: wrapper flatten/unflatten de
las dos ramas, inferencia `training=False`, link identity,
`Independent(background, max_samples=32)`, `batch_size=1024`.
`max_evals=16*(2*P+1)`, P=222 para GC3 y P=258 para GE. El RNG del explainer
1729 es distinto de las seeds 0..9 de los modelos. XGBoost se explica con
TreeExplainer sobre el modelo escalado, output raw y background explicito
interventional, conforme al benchmark.

Fallback aprobado solo por fallo tecnico real documentado (excepcion,
shape/no-finitos o reconstruccion fuera de tolerancia tecnica 1e-5 escalado):
SamplingExplainer, nsamples=65536, min_samples_per_feature=100, RNG=1729,
mismo wrapper y background. Detener/registrar el fallo antes de sustituir;
no mezclar metodos silenciosamente ni cambiar por resultados cientificos.

### D55 - Background oficial e integridad

32 referencias exclusivamente TRAIN por cultivar. Cobertura temporal mas
representativa que primeros-N, seleccion determinista/reproducible y coste
viable, independiente de resultados TEST. VAL y TEST quedan excluidos del
background oficial. La regla exacta, sin muestreo aleatorio, es:

```text
indices = np.rint(np.linspace(0, n_train - 1, 32)).astype(int)

GC3/GE: n_train=84 ventanas, objetivos 2017-01..2023-12
[0, 3, 5, 8, 11, 13, 16, 19, 21, 24, 27, 29, 32, 35, 37, 40,
 43, 46, 48, 51, 54, 56, 59, 62, 64, 67, 70, 72, 75, 78, 80, 83]

XGBoost: n_train=89 pares, objetivos 2016-08..2023-12
[0, 3, 6, 9, 11, 14, 17, 20, 23, 26, 28, 31, 34, 37, 40, 43,
 45, 48, 51, 54, 57, 60, 62, 65, 68, 71, 74, 77, 79, 82, 85, 88]
```

GC3/GE comparten fechas y valores de sus features comunes; conservar los
mismos indices en todas las seeds. Cada cultivar tiene sus propios valores.
N=32 cubre los doce meses objetivo pero no es una muestra estacionalmente
balanceada; no se afirma que sea optima ni identica a TRAIN completo.

Hashes SHA256 del array background (shape/dtype/bytes, funcion `array_hash`
del benchmark; no confundir con hash del archivo NPZ):

| Cultivar | Modelo | SHA256 background N=32 |
|---|---|---|
| sutil | GC3 | 4d95df53dfeaa745e0752465ead086efced9947d7af4d83ee64d6fcc14d8c5a3 |
| sutil | GE | a8a25c6720e2e3d1a8c9dd5ca111cade33260403d4ea92637d3072a8ade36818 |
| dulce | GC3 | d3c84a671da84253c3e5fb0a8edb7af3d7ac3f8c8dc4bd96c3fcd216d20bd32c |
| dulce | GE | 01895908a544ead3ab1dcb359b3de99cb0e057d64e09d52c87800248846de69e |
| sutil | XGBoost | 71d3dbb62dc1fa60e8362b73296b6be423f13fa03f78e57af898c0114ead9980 |
| dulce | XGBoost | 41021ad468e00e8b23dcfc710e6e2922c2539349b84ab616bdbec3546b774be2 |

Indices, fechas, arrays y hashes de archivo se conservan en el JSON y en
`auditorias/shap_v2_benchmark_arrays/`. Esas evidencias tecnicas se preservan
sin reescribir su estado historico pendiente: esta seccion registra la
aprobacion posterior. JSON SHA256:
`c29b4ffa1fa7b03daa15db52a770214ba92587fd4d152cbaa3cd82cea7f18641`.

### Correccion del lector y restriccion futura

El lector neuronal anterior podia cargar el CSV completo antes de filtrar
TEST. Por ello su `test_loaded=False` no acreditaba ausencia de carga.
El benchmark final corrigio la lectura con `csv.DictReader` e `islice(...,102)`:
solo se parsean las 102 filas TRAIN+VAL 2016-07..2024-12, sin pedir el registro
103; fechas exactas verificadas. No basta cargar todo y filtrar despues.
La lectura binaria para hashing no usa valores TEST para analisis.

La incidencia **no produjo SHAP TEST oficial, no modifico modelos ni
predicciones y no intervino en seleccion mediante resultados TEST**.
Todo futuro preflight debe mantener el lector acotado; no reutilizar el
lector anterior ni ejecutar sus generadores para reconstruir este cierre.

### Continuidad

Consultar `HANDOFF_SESION.md`, que reemplaza el punto de reanudacion obsoleto
de `HANDOFF_CONTEXTO_ACTUAL.md`. No entrenar, tunear, modificar modelos ni
predicciones, ni ejecutar SHAP TEST durante este cierre. No commit ni push.

---

## 2026-10-25 - D-BR1..D-BR12: preregistro del backtesting rodante v2

**Estado:** PRERREGISTRADO antes de cualquier entrenamiento o evaluación del backtesting (Fase C).
**Carpeta:** `v2_reentrenamiento/experimentos_backtesting_rodante/` (plan en `00_plan/`, configuración en `01_configuracion/`).
**Advertencia:** TEST 2025 ya fue inspeccionado en v2–v9. Las ventanas 2018–2024 son de robustez retrospectiva.
- Los hiperparámetros de GC3, GE y XGB-37 se fijaron con datos hasta 2024.
- El orden del SARIMA congelado de Sutil se adoptó después de ver TEST 2025 (`02b_diagnostico_sarima_sutil.ipynb` celdas 0, 14-15, 20).

**Verificación previa (Fase B):**
- Con Y = 2025 el código reproduce bit a bit los artefactos oficiales v2 (pesos, maestro, features, scaler v2c, secuencias, pares) y los pesos entrenados de GC3 semilla 0.
- La prueba automática de fuga pasa en las 16 combinaciones ventana×cultivo.
- Δs(P0) = 0 exacto.

### D-BR1 - Ventanas
- Origen = diciembre de Y−1; test = enero..diciembre de Y; Y = 2018..2025. 2026 queda excluido.
- Particiones para todos los modelos:

| Partición | Meses |
|---|---|
| Train | hasta diciembre de Y−2 |
| Validación | año Y−1 |
| Test | año Y |

- Inicio del train: features y SARIMA desde 2016-07; objetivos tabulares desde 2016-08; objetivos LSTM desde 2017-01 (lookback 6).
- Mínimo de train para modelos entrenados: 36 meses. Por debajo, la combinación es "no aplica" y no se fuerza.
- Resultado: 118 combinaciones viables y 42 "no aplica" (`03_ventanas/ventanas_viabilidad.csv`).
- **Ranking principal:** ventanas comunes 2021–2025.
- **Sensibilidad preregistrada:** se repiten todas las conclusiones (ranking, empates, robustez, DM) usando solo las ventanas 2023–2025.

### D-BR2 - Modelos
Las semillas, donde hay aleatoriedad, son 0..9. No hay selección de semilla ni de modelo con ningún test.

**Sin ajuste**
- Naive: ŷ_t = y_{t−1}.
- Seasonal Naive: ŷ_t = y_{t−12}.
- Chronos-Bolt-tiny zero-shot: `amazon/chronos-bolt-tiny`, revisión `a0e552de…`, mediana, contexto 2016-01..t−1, copia de `v4_benchmark_moderno/vendor`, sin red. Es determinista.

**SARIMA congelado**
- Sutil (1,1,1)(1,1,0,12); Dulce (1,0,0)(0,1,0,12).
- `trend='c'`, `approximate_diffuse`, `maxiter=500`.
- Ajuste único en train; la validación se añade como estado y el test se pronostica a 1 paso con `append(refit=False)`.

**SARIMA-sel:** regla D-BR10.

**Ridge y ElasticNet (DA4 revisada)**
- En **cada ventana** se reelige α (Ridge) o (α, l1_ratio) (ElasticNet) por el **MAE en toneladas sobre la validación de esa ventana (año Y−1)**.
- Rejilla de v3: α ∈ {0.001, 0.01, 0.1, 1, 10, 100}; l1 ∈ {0.2, 0.5, 0.8}.
- Cada candidato se ajusta **solo con el train** de la ventana. X: 37 predictores de XGB-37 estandarizados con media y desviación poblacional del train; y en toneladas.
- El modelo final es el ajuste en train con los valores elegidos: **no se reajusta con la validación**.
- Empate en el MAE de validación: primero en el orden de la rejilla (α creciente; luego l1 creciente).
- Implementación: sklearn `Ridge` y `ElasticNet(max_iter=100000, tol=1e-10)`.
- Los valores de v3 (Ridge α Sutil 10 / Dulce 100; ElasticNet Sutil 0.1/0.5, Dulce 1/0.2) se usan **solo como control en la ventana 2025**: se reporta si coinciden con los elegidos y la diferencia de MAE.

**XGB-37, GC3 y GE**
- Configuración oficial v2 (`config_gc2_xgboost.py`, `config_gc3_ge.py`, `dual_lstm_attention.py`), sin cambios.
- GC3/GE: early stopping y ReduceLROnPlateau sobre la validación Y−1; predicción con el checkpoint de la mejor época; cada corrida en un proceso nuevo con `configure_determinism(semilla)`.

**Exploratorios**
- XGB-43 (37 predictores + 6 NLP rezagados; mismos parámetros): **post-hoc**, en tabla aparte, fuera del ranking.
- Variantes de v9: excluidas (posible Fase E).

### D-BR3 - Prevención de fuga
Se ajustan **solo con el train de cada ventana**:
- el StandardScaler;
- los pesos geográficos de NASA e INDECI (`PesosGeograficos` con `VentanaTrain(2016-01, diciembre de Y−2)`);
- el denominador de MASE;
- los hiperparámetros reelegidos de Ridge, ElasticNet y SARIMA-sel (con train para ajustar y validación Y−1 para elegir).

Además:
- El umbral de shock se calcula con la historia hasta el origen.
- La validación es siempre anterior al test.
- Los lags de test usan valores observados (un paso adelante).

Prueba automática: `02_scripts/tests/test_fuga.py`, con controles negativos.

### D-BR4 - Definición de shock
- **Mensual:** r_t = |y_t − y_{t−1}|/y_{t−1}. **Interanual:** r_t = |y_t − y_{t−12}|/y_{t−12}.
- Para k = 10..95: shock si r_t > P_k (comparación estricta), con P_k el percentil k (numpy, lineal) de r calculado con los cambios fechados entre el inicio de la serie y el origen (diciembre de Y−1).
- **Principal:** P75 mensual. **Reporte:** P50, P60, P90 e interanual.
- **Barrido:** P0, P10..P95 cada 5.
- **P0 (verificación de código, no es un umbral de análisis):** se define explícitamente como umbral = 0 con comparación **r_t ≥ 0**. Como r_t es un valor absoluto, la condición se cumple siempre, así que **todos** los meses de test son shock. Entonces MAE_shock = MAE_global y **Δs(P0) = 0 exactamente**; si no da 0, hay un error de código y la corrida se detiene. P0 **no** se calcula como el percentil 0 de la historia con comparación estricta: con r_t > mín(historia), los meses de test con un cambio menor o igual que el mínimo histórico quedarían fuera y Δs no sería 0 sin que hubiera error. Para P10..P95 se mantiene la comparación estricta r_t > P_k. La razón MAE_shock/MAE_normal no está definida en P0, porque no hay meses normales.
- Una ventana con menos de 2 shocks en un umbral se marca "no informativa" en las métricas por ventana; sus meses de shock cuentan en el agregado.

### D-BR5 - Métricas
Todas en toneladas reales.
- MAE global, RMSE, MAE normal, MAE shock, n_shock, n_normal.
- Δs = (MAE_shock − MAE_global)/MAE_global × 100.
- Razón MAE_shock/MAE_normal.
- Δs quitando un mes de shock a la vez.
- MASE con denominador D_w = media de |y_t − y_{t−12}| para t entre 2017-01 y diciembre de Y−2, común a todos los modelos de la ventana. En el agregado, cada mes se normaliza con el D_w de su ventana.
- MAE por tercios y cuartiles de |Δy/y| en test.

**Intervalos:** bootstrap pareado iid sobre meses (los mismos índices para todos los modelos), estratificado por ventana, B = 10 000, semilla 42, percentiles 2.5–97.5. Sensibilidad con bloques de 3 meses.

**Significancia:**
- Diebold-Mariano con corrección HLN (h = 1, pérdida absoluta), por pares, sobre las ventanas agrupadas y restringido a meses de shock. Se declara la baja potencia.
- Model Confidence Set opcional (α = 0.10).

**Ablación NLP:** GE − GC3 con semillas emparejadas (s con s), por ventana y agregada.

### D-BR6 - Agregación de semillas
- La serie de error de un modelo con 10 semillas es el **promedio mensual del error absoluto entre las 10 semillas**.
- El bootstrap y el Diebold-Mariano usan ese promedio.
- La dispersión entre semillas se reporta aparte (cajas y DE) y no entra en los intervalos.

### D-BR7 - Regla de "mejor"
- **Mejor en shocks** = menor MAE_shock agregado, evaluado por separado en cada umbral. **Mejor en meses normales** = menor MAE normal.
- **Empate:** el IC 95 % bootstrap pareado de la diferencia de MAE entre dos modelos incluye 0. "Primero" = el de menor MAE junto con todos los que empatan con él.
- **Robusto:** un modelo es robusto si queda primero, o empatado con el primero, en al menos 3 de P50, P60, P75 y P90 (variación mensual); el interanual va aparte. Se evalúa por cultivo.
- Un Δs bajo por sí solo no es evidencia de resiliencia: se exige un MAE_shock bajo en toneladas.
- Si el ranking cambia con el umbral, se reporta como resultado; no se elige el umbral que favorezca a un modelo.
- **Barrido:** se reporta el percentil desde el cual el primer lugar ya no cambia y desde el cual todos los modelos empatan.

### D-BR8 - Diagnóstico de ajuste
- **Sobreajuste:** MAE_val/MAE_train > 2.0 (toneladas; LSTM con los pesos de la mejor época; resto con el ajuste final).
- **Señal complementaria:** la razón MAE_val/MAE_train del **Naive en la misma ventana y cultivo**. Se reporta junto a la de cada modelo como referencia del cambio de nivel y dificultad entre el train y el año de validación, que no depende de ningún ajuste.
- **Señal aparte:** "no supera al Naive" (MAE_train ≥ MAE_train del Naive, o MAE_val ≥ MAE_val del Naive).
- **Advertencia en los gráficos:** en Sutil la validación 2024 tiene un nivel medio mayor que el train, lo que infla la razón.
- **Declaración:** el umbral 2.0 **marcará como sobreajustados a casi todos los modelos entrenados**. La razón oficial de XGB-37 en 2025 ya es ≈7.0 en Sutil y ≈7.8 en Dulce. El umbral se fijó conociendo esos valores, y la bandera se interpreta junto a la razón del Naive, no por sí sola.

### D-BR9 - Exclusiones y no comparables
- No se mezclan resultados de v3, v4 ni v5. Ridge, ElasticNet y Chronos se recalculan con este protocolo.
- Las ventanas A y B de v5 tienen fuga de validación en GC3/GE (`09_reportes/nota_v5_v3.md`).

### D-BR10 - SARIMA-sel: selección del orden por ventana (DA10 = opción b)
En cada ventana y cultivo:
1. Se ajustan en train los 576 órdenes (p 0–3, d 0–1, q 0–3, P 0–2, D 0–1, Q 0–2, m = 12) con las opciones de GC1 (`enforce_stationarity=False`, `enforce_invertibility=False`, `approximate_diffuse`, `trend='c'`, `maxiter=200`; `02_gc1_sarima_prophet.ipynb` celda 7).
2. Los órdenes que fallan (excepción) se descartan y se cuentan. No se excluye ningún candidato por la bandera de convergencia, igual que en GC1.
3. Se ordenan por AIC de train ascendente (empate: orden de la rejilla) y se toman los 5 primeros.
4. Cada uno de los 5 se reajusta en train con `maxiter=500`. Con sus parámetros fijos se calcula el MAE de validación **a 1 paso** sobre el año Y−1 (`forecast(steps=1)` y luego `append([y_real], refit=False)`).
5. Se elige el de menor MAE de validación (empate: menor AIC).
6. El modelo final es ese mismo ajuste (`maxiter=500`). Sigue con el test exactamente como el SARIMA congelado: estado actualizado con la validación y pronóstico a 1 paso con `append(refit=False)`.
7. Se registran, por ventana y cultivo: el orden elegido, **su posición en AIC (1–5)** y su AIC, el AIC y el MAE de validación de los 5 candidatos, el número de órdenes fallidos y la convergencia del elegido.

**Limitación declarada:** el AIC de órdenes con distinto d/D no es estrictamente comparable (cambia la serie diferenciada). Se mantiene por fidelidad a GC1.

### D-BR11 - Reproducibilidad
- Un solo comando: `02_scripts/run_all.py`.
- Cada script verifica la integridad (SHA-256) de `v2_reentrenamiento/src`, de los datos y de Chronos frente a `01_configuracion/hashes_congelados.json` y aborta si cambian.
- Variables: PYTHONHASHSEED=42, TF_ENABLE_ONEDNN_OPTS=0, TF_DETERMINISTIC_OPS=1, HF_HUB_OFFLINE=1. Las versiones y el hardware van en `manifest.json`.
- Durante la corrida se reporta el progreso por ventana. Ante cualquier fallo la corrida se detiene y no se cambia el protocolo.

### D-BR12 - Desviaciones
Cualquier cambio posterior a este preregistro se registra en `experimentos_backtesting_rodante/09_reportes/DESVIACIONES.md`; este texto no se reescribe.

---

## 2026-10-28 - Enmienda E-BR1 a D-BR7 del preregistro D-BR1..D-BR12

**Estado:** enmienda al preregistro D-BR1..D-BR12 (commit `db32108`), escrita antes de ejecutar la Fase C. El texto original de D-BR7 no se reescribe; esta enmienda prevalece sobre él.
**Registro:** `experimentos_backtesting_rodante/09_reportes/DESVIACIONES.md`, DESV-02.

- **Se anula** solo la cláusula "se exige un MAE_shock bajo en toneladas" de D-BR7 (frase "Un Δs bajo por sí solo no es evidencia de resiliencia: se exige un MAE_shock bajo en toneladas.").
- **Se conserva:** "Un Δs bajo por sí solo no es evidencia de resiliencia."
- **Robusto** queda definido solo así: un modelo es robusto si queda primero, o empatado con el primero, en al menos 3 de P50, P60, P75 y P90 (variación mensual); el interanual va aparte; se evalúa por cultivo. No se agrega ningún otro requisito.
- El resto de D-BR7 (mejor en shocks, mejor en meses normales, empate, "primero", ranking por umbral y barrido) no cambia.
