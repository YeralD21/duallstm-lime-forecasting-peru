# Desviaciones respecto del preregistro (D-BR12)

Cada cambio posterior al preregistro D-BR1..D-BR12 (`DECISIONES_METODOLOGICAS.md`, commit `db32108`) se registra aquí.
Tipos: **implementación** (no cambia qué se estima ni cómo se evalúa) o **protocolo** (cambia el análisis).

---

## DESV-01 — Hash SHA-256 con fin de línea normalizado

- **Fecha:** 2026-10-28. **Tipo:** cambio de implementación, no de protocolo. **Aprobado por:** el autor, antes de la Fase C.
- **Afecta a:** D-BR11 (verificación de integridad). No cambia datos, código oficial, modelos ni métricas.
- **Motivo:** el repositorio usa `core.autocrlf=true`. Git guarda los archivos de texto con LF y en Windows los escribe con CRLF, así que el hash de los bytes depende de la máquina donde se clona. Con el método anterior, un clon en otro sistema abortaría la verificación sin que hubiera cambiado nada.
- **Método nuevo (versión 2):**
  - Archivos de texto, por extensión (`.py`, `.csv`, `.json`, `.md`, `.txt`, `.mjs`, `.cfg`, `.toml`, `.yaml`, `.yml`, `.ini`): se reemplaza CRLF por LF y luego se calcula el SHA-256.
  - Cualquier otra extensión (por ejemplo `.joblib`, `.safetensors`) es binaria: SHA-256 de los bytes tal cual. `model.safetensors` contiene bytes 0D 0A propios del formato y por eso no se normaliza.
  - El método queda escrito en `01_configuracion/hashes_congelados.json`, clave `_metodo`.
- **Procedimiento (una sola vez):** `02_scripts/00_verificar_entorno.py --normalizar-hashes`.
  1. Verificó los 93 archivos byte a byte contra el archivo anterior: 0 diferencias.
  2. Guardó el archivo anterior como `01_configuracion/hashes_congelados_v1_bytes.json`.
  3. Regeneró `hashes_congelados.json` con el método 2 y volvió a verificar: 93 archivos, 0 diferencias.
  4. El script se niega a repetir la operación si el archivo ya tiene `_metodo`.
- **Archivos cuyo hash cambió de valor:** 41 que tenían CRLF en disco (23 de `v2_reentrenamiento/src`, 18 de datos y referencias). El contenido no cambió.
- **Comprobación:** para los 89 archivos que están en `HEAD`, el hash normalizado coincide con el SHA-256 del contenido guardado en git (`git show HEAD:<ruta>`). Los 2 que no están en `HEAD` y los 2 de la caché de Hugging Face no se pueden comprobar así.

---

## DESV-02 — Enmienda E-BR1 a D-BR7 (definición de "robusto")

- **Fecha:** 2026-10-28. **Tipo:** cambio de protocolo (criterio de interpretación), hecho antes de ejecutar la Fase C. **Aprobado por:** el autor.
- **Texto:** al final de `v2_reentrenamiento/DECISIONES_METODOLOGICAS.md` ("Enmienda E-BR1 a D-BR7 del preregistro D-BR1..D-BR12"). El texto original de D-BR7 (línea 1818) no se reescribe.
- **Cambio:** se anula solo la cláusula "se exige un MAE_shock bajo en toneladas"; se conserva "Un Δs bajo por sí solo no es evidencia de resiliencia". Robusto = primero, o empatado con el primero, en al menos 3 de P50, P60, P75 y P90 (variación mensual); interanual aparte; por cultivo.
- **Motivo:** la cláusula no formaba parte del criterio pedido por el autor.
- **Efecto en el código:** ninguno. `01_configuracion/umbrales.json` ("robustez") ya definía solo la regla de 3 de 4 umbrales.
- **Textos de planificación que conservan la frase anterior** (históricos, no se editan): `00_plan/plan_fase_A.md:266` y `00_plan/borrador_preregistro.md:118`.

---

## DESV-03 — Pruebas b02 y b04 de la Fase B leen `control_2025_v3`

- **Fecha:** 2026-10-28. **Tipo:** cambio de implementación, no de protocolo.
- **Problema:** al revisar DA4 (α reelegido por ventana), `hiperparametros_congelados.json` pasó a guardar los valores de v3 en `ridge.control_2025_v3.<cultivo>` y `elasticnet.control_2025_v3.<cultivo>`. `b02_reproducir_elasticnet_v3.py` (l. 85) y `b04_medir_tiempos.py` (l. 89-90) seguían leyendo `HP["elasticnet"][cultivo]` y `HP["ridge"][cultivo]`, que ya no existen, y fallaban con `KeyError`. Así, `run_all.py --fase B` no se podía repetir.
- **Corrección:** las tres lecturas usan ahora `["control_2025_v3"][cultivo]`. Los valores son los mismos (Ridge α Sutil 10, Dulce 100; ElasticNet Sutil 0.1/0.5, Dulce 1/0.2).
- **Comprobación:** se reejecutaron solo esas dos pruebas (código de salida 0 en ambas). `elasticnet_predicciones_2025.csv` es idéntico byte a byte al de la Fase B, y `elasticnet_reproduccion.json` es idéntico salvo los tiempos medidos. `tiempos_fase_b.json` se reescribió con tiempos nuevos, del mismo orden que los anteriores.

---

## DESV-04 — SARIMA-sel: órdenes con AIC no finito

- **Fecha:** 2026-10-28. **Tipo:** cambio de implementación (precisión de un caso que D-BR10 no cubre).
- **D-BR10, paso 2:** se descartan y se cuentan los órdenes cuyo ajuste lanza una excepción.
- **Caso no previsto:** un ajuste que **no** lanza excepción pero devuelve AIC NaN o ±inf. No se puede ordenar por AIC.
- **Tratamiento:** esos órdenes quedan fuera del ranking por AIC (paso 3), se cuentan aparte en `info.json` (`n_aic_no_finito`) y siguen en `rejilla.csv` con su AIC tal como salió. No se cuentan como "fallidos" (`n_fallidos` = solo excepciones).
- **Efecto:** si quedan al menos 5 órdenes con AIC finito, el top-5 se forma solo con ellos; si quedaran menos de 5, se toman los que haya y se registra. En la prueba de la ventana 2021 no hubo ninguno: 0 fallidos y 0 AIC no finitos de 576 en ambos cultivos (78 y 30 sin convergencia en la rejilla, que no se excluyen, como en GC1).
- **Regla de elección completa (D-BR10, pasos 3-5), tal como está implementada en `lib/modelos_series.py::sarima_sel`:**
  1. Top-5: AIC de train con maxiter 200 ascendente; empate → orden de la rejilla (`itertools.product(p, d, q, P, D, Q)`).
  2. Cada uno de los 5 se reajusta en train con maxiter 500 y se calcula su MAE de validación a 1 paso sobre Y−1.
  3. Elegido: menor MAE de validación; empate → menor AIC (el de la rejilla, maxiter 200, que es el que define la posición 1-5); empate → orden de la rejilla.
  4. Se registra también el AIC con maxiter 500 de cada candidato (`candidatos.csv`), pero no se usa para elegir.

---

## DESV-05 — Criterio de equivalencia 2025 de la Fase D1 ajustado para Δs (decidido después de ver el resultado)

- **Fecha:** 2026-10-28. **Tipo:** cambio de implementación (criterio de una prueba), **decidido después de ver el resultado**.
- **Prueba:** `02_scripts/tests/test_equivalencia_metricas_2025.py` compara la ventana 2025 del backtesting con `resultados_v2_final` (GC3, GE y XGB-37 por semilla; SARIMA rolling).
- **Criterio original** (fijado al escribir la prueba): diferencia relativa ≤ 1e-6 en todas las métricas. **No se cumplió** en Dulce GC3 (1,18e-6) y GE (1,43e-6), y solo en Δs (p. ej. GE semilla 4: 3,08605 % frente a 3,08605 % oficial; diferencia absoluta 4,4e-6 puntos porcentuales).
- **Causa:** Δs es un porcentaje cercano a 0, así que la diferencia relativa se amplifica. El origen es la diferencia ya conocida desde la Fase B: las predicciones de GC3/GE difieren ≤ 5e-4 t de las oficiales por redondeo float32; los pesos entrenados son idénticos bit a bit.
- **Criterio aplicado:** relativa ≤ 1e-6 en todas las métricas salvo Δs, y absoluta ≤ 1e-4 puntos porcentuales en Δs. Con él, los 8 casos cultivo×modelo dan OK. El veredicto con el criterio original también queda guardado (`OK_criterio_original: false` en `06_metricas/reproducibilidad/metricas_2025_vs_oficial.json`).

---

## DESV-06 — Decisiones de implementación de la Fase D1 no fijadas en D-BR5/D-BR7

- **Fecha:** 2026-10-28. **Tipo:** implementación. Se fijaron al escribir `lib/evaluacion.py`, `08_metricas.py` y `09_barrido_umbral.py`, antes de calcular las tablas; ninguna depende de los resultados.
- **Estado:** PENDIENTE DE APROBACIÓN del autor (texto presentado el 2026-10-28).

1. **RMSE con semillas:** RMSE de cada semilla sobre los meses del conjunto, y media entre semillas. Paralelo a "MAE = media de los MAE por semilla" (A3).
2. **Bootstrap iid:** MAE global sobre todos los meses; MAE_shock y MAE normal remuestreando solo dentro de los meses de shock o de normalidad de cada ventana (A5). Mismos índices para todos los modelos; generador nuevo con semilla 42 en cada llamada.
3. **Bootstrap por bloques (sensibilidad):** bloques móviles circulares de 3 meses dentro de cada ventana (4 bloques = 12 meses). MAE_shock y MAE normal se calculan como cociente sobre los meses remuestreados de cada tipo; los remuestreos sin ningún mes de ese tipo se descartan y se cuentan (`bloq_shock_remuestreos_sin_shock`).
4. **Empates y "primero":** con el IC iid de la diferencia con el mejor (principal). La columna "robusto men (bloques)" repite la regla con bloques. **Exploratorio:** D-BR5 prevé los bloques para los intervalos, no para la regla de robustez.
5. **Diebold-Mariano-HLN:** h = 1, pérdida absoluta sobre el error promediado entre semillas, ventanas agrupadas (n = 60 por cultivo en la principal, 36 en la sensibilidad), t(n−1) bilateral. "Solo shocks" usa la máscara P75 mensual. **Sin corrección por comparaciones múltiples** (no preregistrada); se reportan los p-valores sin ajustar, con la advertencia de baja potencia. La corrección de Holm se añadió aparte como análisis exploratorio (DESV-07).
6. **Model Confidence Set:** opcional en D-BR5; **no se calculó**.
7. **Cuartiles y tercios de |Δy/y|:** cortes = cuantiles del cambio mensual sobre los 60 meses de test agrupados de cada cultivo (`pd.qcut`); 15 o 20 meses por grupo.
8. **Descripción de las series:** train desde 2016-07 (inicio de features y SARIMA, D-BR1). ACF, ADF y KPSS solo si n ≥ 24 (por eso no hay valores en las ventanas 2018 y 2019). ADF con constante y retardos por AIC; KPSS con constante y `nlags="auto"`; el p de KPSS está acotado a [0,01; 0,10] por la tabla de statsmodels.
9. **D-BR8:** el MAE de train y de validación del Naive de referencia se calcula en los mismos meses objetivo de cada modelo (tabulares desde 2016-08; LSTM desde 2017-01).
10. **MASE:** en la ventana 2018, D_w no está definido (el train no tiene meses con y_(t−12)) y MASE queda vacío.
11. **Δs quitando un mes:** el mes sale a la vez de los shocks y del MAE global.
12. **Estabilización del barrido:** "primer lugar estable desde k" = menor k tal que el modelo de menor MAE_shock es el mismo en todos los percentiles ≥ k; "todos empatan desde k" = menor k tal que en todos los percentiles ≥ k todos los modelos son "primero". Con pocos shocks (P95: 1–3 meses) el resultado es degenerado y se interpreta con esa cautela.
13. **Formato:** los CSV tienen precisión completa; las vistas en texto y LaTeX se redondean.

---

## DESV-07 — Corrección de Holm sobre Diebold-Mariano (EXPLORATORIO)

- **Fecha:** 2026-10-28. **Tipo:** análisis adicional **exploratorio**, pedido por el autor después de ver los resultados de la Fase D1. No forma parte del preregistro (D-BR5 no prevé corrección por comparaciones múltiples) ni de la regla de "mejor" (D-BR7), que se basa en el bootstrap.
- **Qué se calcula:** Holm (`statsmodels.stats.multitest.multipletests`, `method="holm"`) sobre los p-valores DM-HLN de cada familia = conjunto (2021–2025 o 2023–2025) × cultivo × alcance (global o solo shocks P75 mensual). Cada familia tiene 45 pares (10 modelos); se excluyen los pares sin p-valor (no hubo ninguno).
- **Salida:** columna `p_holm_exploratorio` en `06_metricas/significancia/T09_diebold_mariano_hln.csv`; matrices `T09_DM_holm_matriz_*`; resumen `T09_holm_resumen` (pares con p < 0,05 antes y después). Los p-valores sin ajustar no cambian.
- **Model Confidence Set:** sigue sin calcularse, por decisión del autor.

---

## DESV-08 — Implementación de las figuras de la Fase D2 frente a `00_plan/mapa_evidencia.md`

- **Fecha:** 2026-10-28. **Tipo:** implementación (presentación). Ninguna cifra cambia: todas las figuras se dibujan desde CSV ya guardados.
- **Estado:** pendiente de aprobación del autor.

1. **fig01 (curvas de pérdida):** el mapa decía "media ± banda entre semillas". Se dibuja **una línea por semilla** (y su mejor época), porque las semillas paran en épocas distintas y una media por época sería una cifra nueva que no está en ningún CSV.
2. **fig20:** los modelos con semilla se muestran con una línea por semilla, no con la media de predicciones (el protocolo no usa ensambles, A3).
3. **fig11:** IC marginales de MAE_shock solo en P50, P60, P75 y P90. Para los demás percentiles no hay IC por modelo guardados (el barrido guarda solo el IC de la diferencia con el mejor).
4. **fig21:** la escala de color logarítmica empieza en el percentil 2 de los errores de cada cultivo; los errores menores se pintan con el color mínimo (`extend="min"`). Es solo escala de color; el CSV conserva los valores.
5. **fig02:** la razón del Naive dibujada es la de los meses de los modelos tabulares; en los meses de las LSTM (desde 2017-01) difiere como máximo en 0,030 (Sutil) y 0,015 (Dulce). Se indica en el pie.
6. **No generadas** (fuera de la especificación de la Fase D2): fig22 y fig23 (residuos) y fig24–fig28 (figuras independientes). fig18 y fig19 se generaron después, a pedido del autor (puntos 9 y 10).
7. **XGB-43** (exploratorio, post-hoc): XGB-43 no se incluye en ningún resultado del texto principal; aparece solo en fig18b y, como caja exploratoria discontinua, en fig_workflow. Tampoco entra en el ranking, en Diebold-Mariano (fig19) ni en Holm (fig19b) (puntos 27 y 30). Estado: aprobado por el autor (2026-10-29).
8. **Leyendas** fuera del área de datos, lo que corrige lo señalado en la figura de prueba de la Fase B.
9. **fig18 (ablación GE − GC3):** desde `06_metricas/ablacion_nlp/T11_ablacion_GE_menos_GC3.csv`. Muestra las 10 diferencias por semilla emparejada (puntos) y la media con su IC bootstrap pareado guardado (rombo), por ventana y agregado (2021–2025 y 2023–2025), en tres paneles: todos los meses, shocks P75 y meses normales. "n/a" donde no hay meses de shock (Sutil 2021 y 2024).
10. **fig19 (matriz Diebold-Mariano-HLN):** desde `06_metricas/significancia/T09_diebold_mariano_hln.csv`, solo con el conjunto principal 2021–2025 (la sensibilidad 2023–2025 queda en la tabla). Bajo la diagonal: todos los meses; sobre la diagonal: solo shocks P75. Color por tramos de p (< 0,01; < 0,05; < 0,10; ≥ 0,10) y signo "+" si el modelo de la fila tiene más error. **La versión con Holm (exploratoria, DESV-07) va en un archivo aparte**, `fig19b_dm_pvalue_matrix_holm_{cultivo}`, marcada como EXPLORATORY en la leyenda y el pie. Así fig19 tiene dos archivos por cultivo.

**Lote de regeneración de figuras D2 (2026-10-29). Estado: pendiente de aprobación.** Solo presentación: se regeneraron 39 figuras desde los mismos CSV con `10_figuras.py --solo <prefijos>`; el SHA-256 de los 55 CSV de `08_graficos/` (54 de figura + `indice_figuras.csv`) es idéntico antes y después. No se reescribió ningún archivo de fig01, fig04, fig05, fig07, fig11, fig16_sutil ni fig17.

11. **fig20 (10):** Observed en trazo negro grueso continuo con halo blanco (debajo de los pronósticos); Seasonal Naive discontinuo con sus cuadrados. Colores por modelo sin cambio. Sin meses de shock en el año (solo Sutil 2021 y 2024) la leyenda dice "Shock month (monthly P75) (none this year)". Eje y con miles separados por coma.
12. **Mapas de color:** fig14 y fig21 con `cividis_r` (amarillo = menor error); fig10 con `Blues`. En fig14 y fig10 el color del texto (negro/blanco) se elige por la luminancia relativa de la celda (WCAG, umbral 0,18). fig07 sin cambios. Las barras de color logarítmicas de fig14 y fig21 usan marcas 1-2-5 con coma de miles (más densas si el rango es menor de una década, como en fig14 Sutil).
13. **fig02 (2):** eje y "MAE_val / MAE_train (log scale)" (sin "t"); barras del Naive en el gris del Naive (#999999) en el gráfico y la leyenda; el pie dice "grey bars". Marcas del eje log legibles (1, 2, 5, 10, 20) en lugar de 10⁰/10¹ (añadido no pedido explícitamente, por coherencia con el punto 15).
14. **fig06 (2):** eje y logarítmico sin `set_ylim` (no se recorta ningún punto; todas las razones son positivas, NaN solo en P0, como antes), línea en 1. Rótulo "MAE ratio, shock / normal months (log scale)"; el pie añade una frase sobre la escala log.
15. **fig09 (2):** etiquetas del eje x giradas 90°. **fig12 (2):** más separación entre paneles (`wspace=0.55`) y miles con coma, sin invasión del panel vecino. **fig16_dulce:** marcas 20, 50, 100 en el eje log (10 queda fuera del rango de los datos).
16. **fig18 (2):** "n/a" desplazado 7 puntos por encima de la línea de cero; etiquetas del panel (b) con el n de meses de shock, p. ej. "2023 (n=4)", también en los agregados; leyenda "One seed: MAE(GE, seed k) − MAE(GC3, seed k)" en lugar de "(s with s)"; leyenda bajada para no tocar las etiquetas.
17. **fig13 (2):** bigotes de los IC dibujados encima de las barras (zorder 5) con borde blanco, visibles sobre la barra negra de Seasonal Naive.
18. **fig15 (2):** "n/a" en los huecos del panel (b) (Sutil 2021 y 2024); leyendas con parches de color en fig15 y fig03; fig08 añade a la leyenda el círculo "First or tied with first".
19. **fig19 y fig19b (4):** p < 0,001 se rotula "<0.001" (antes "0.000"). Solo la etiqueta; T09 no cambia.
20. **Rótulos:** miles con coma en fig14 (celdas de ambos cultivos) y en los ejes de toneladas de las figuras regeneradas; "MAE_shock" pasa a "MAE in shock months (t)" en fig12, fig14 y fig15, y a "Rank by MAE in shock months" en fig08; los meses de shock se rotulan "monthly P75 (MoM)" en fig13, fig14 y fig15. **Quedan con "MAE_shock" las figuras que no se tocan:** fig04 (eje y), fig07 (barra de color) y fig11 (eje x), y los textos de lectura de los TXT.
21. **Unificación del rótulo "MAE_shock" (2026-10-29, estado: pendiente de aprobación):** fig11 (2), con el eje x "MAE in shock months (t)", y fig07 (2), con la barra de color "Rank by MAE in shock months (1 = lowest)", regeneradas con `--solo fig07 fig11`. **Excepción:** en fig04 el símbolo MAE_shock se mantiene dentro de la fórmula del eje y, "Δs (%) = (MAE_shock − MAE) / MAE", porque el pie lo define. Ese es el único lugar de fig04 donde aparece, así que fig04 no tiene cambios y no se regeneró (sus archivos siguen siendo los del commit 5567ba2). Los textos de lectura de los TXT conservan "MAE_shock". SHA-256 de los 55 CSV idéntico al del lote anterior; solo se reescribieron los PNG y PDF de fig07 y fig11.

**Lote final de figuras (2026-10-29). Estado: pendiente de aprobación.** Solo presentación. Se regeneraron 16 figuras desde los mismos CSV: `10_figuras.py --solo fig05 fig11 fig18_nlp_ablation_paired_sutil fig20` y, para el mapa, solo `fig29_y_ts1()` de `11_figuras_d3.py`; la TS1 de esa llamada se escribió fuera de `08_graficos/` y es idéntica byte a byte a la guardada. El SHA-256 de los 62 CSV de `08_graficos/` (incluidos los índices) es idéntico antes y después. Cambiaron solo PNG y PDF de esas 16 figuras y el TXT de fig05 dulce, fig11 dulce y las 10 fig20. fig04 y fig07 no se regeneraron: fig04 tiene un eje lineal con valores menores de 200 y fig07 muestra rangos del 1 al 10, así que ninguna necesita coma de miles ni marcas logarítmicas.

22. **fig11 (2):** Sutil con las marcas del eje x con coma de miles ("4,000", "10,000"); Dulce con marcas 1-2-5 legibles en el eje log (10, 20, 50, 100), sin notación 10ⁿ, y rótulo "(t, log scale)". El rótulo del eje x va en dos líneas en ambos cultivos para que no se toquen los de paneles vecinos. El pie de Dulce añade "Logarithmic x-axis."
23. **fig05 (2):** Sutil con coma de miles en el eje y; Dulce con marcas 1-2-5 (5, 10, 20, 50, 100) en el eje log, rótulo "MAE in shock months (t, log scale)" y "Logarithmic y-axis." en el pie.
24. **fig18 Sutil:** en el panel (b) el eje x empieza en −0.8 cuando la primera posición (2021) no tiene meses de shock, para que "n/a" no pise el eje vertical; sigue 7 puntos por encima de la línea de cero. fig18 Dulce no cambia (su primera posición tiene datos).
25. **fig29:** el rótulo de Utcubamba se mueve al este (sin marcadores ni bordes debajo), unido al punto con una línea guía. Solo cambia la posición del rótulo; datos, porcentaje y geometría no cambian. (Figura de la Fase D3, DESV-09.)
26. **fig20 (10):** Seasonal Naive se dibuja con línea discontinua y cuadrados huecos (relleno blanco, borde negro), para que la línea gruesa de Observed siga visible debajo. Observed no cambia. El pie añade "Observed: thick black line; Seasonal Naive: dashed black line with open squares."
27. **fig18b_xgb43_vs_xgb37_exploratory_{sutil,dulce}: generada en versión reducida (2026-10-29). Estado: pendiente de aprobación.** En `08_graficos/comparacion_modelos/`, con la función `fig18b` de `10_figuras.py` (`--solo fig18b`), mismo estilo que fig18. **Por qué reducida:** T16 solo guarda la media y el IC del agregado 2021–2025; no hay media ni IC por ventana ni agregado 2023–2025, y no se calculan cifras nuevas. Por eso: (i) **puntos** = MAE(XGB-43) − MAE(XGB-37) por semilla emparejada en cada ventana 2021–2025 y en el agregado 2021–2025 (fila `agregado_2021_2025`), como resta simple de T07 (`MAE`, `MAE_shock`, `MAE_normal`), en tres paneles (todos los meses, shocks P75 MoM, meses normales; T07 tiene los tres alcances); (ii) **rombo con IC solo en el agregado 2021–2025**, con los valores de T16 (bootstrap pareado, meses remuestreados dentro de cada ventana, B = 10.000), y la nota "CI shown for pooled 2021–2025 only" en la figura; sin rombos por ventana y sin agregado 2023–2025. Los puntos del agregado se añadieron a pedido del autor (2026-10-29), como en fig18. Valores del CSV redondeados a 6 decimales. "n/a" donde no hay meses de shock (Sutil 2021 y 2024); n de meses de shock en las etiquetas del panel (b), como en fig18. **Marca** "EXPLORATORY (post-hoc; not part of the preregistered ranking)" dentro de la figura. **Estilo de XGB-43:** color #44AA99 (Tol) y marcador pentágono, los ya fijados para XGB-43 en `01_configuracion/estilo_figuras.json`, distintos del verde #009E73 y la X de XGB-37. El pie (TXT) dice qué es XGB-43 (37 predictores de XGB-37 + 6 NLP rezagados, avg_sentiment y n_noticias en rezagos 1, 3 y 6, mismos hiperparámetros), que es post-hoc y que no entra en ranking, Diebold-Mariano ni Holm. **Control:** la media de las 10 restas por semilla del agregado 2021–2025 de T07 coincide con `dif_43_menos_37` de T16 en los 6 casos (2 cultivares × 3 alcances; solo comprobación, no se guarda). **Integridad:** SHA-256 de los 62 CSV previos de `08_graficos/` idéntico antes y después, salvo `indice_figuras.csv` (2 filas nuevas de fig18b); ningún otro archivo cambió. Total: 61 PNG y 61 PDF. Búsqueda de texto: "XGB-43" aparece solo en los PDF de fig18b (61 PDF leídos con `pdftotext`); en CSV/TXT, además de fig18b, en `indice_figuras.csv`, en el TXT de fig30 (que dice que XGB-43 se excluye del recuento) y en `08_graficos/README.md`.
28. **Selección para el artículo y paquete Overleaf (2026-10-29). Estado: pendiente de aprobación.** Selección del autor (sustituye a `08_graficos/paper_mdpi/PROPUESTA_SELECCION.md`, que tenía fig18 en el suplementario y figuras separadas por cultivo). **Texto principal, en orden:** fig29, fig24, fig30, fig25, fig13, fig07, fig05, fig04, fig10, fig20 de 2025, fig18 y fig02. **Suplementario:** fig20 del año con más shocks P75 (Sutil 2023 y Dulce 2024, en una misma figura), fig19, fig19b (EXPLORATORY), fig18b (EXPLORATORY), fig01 (GC3 y GE, dos figuras), fig03, fig06, fig08, fig09, fig11, fig12, fig14, fig15, fig16, fig17 y fig21, y las tablas TS1 y T16. **Subfiguras:** cada pareja Sutil/Dulce va en un solo entorno `figure`, (a) Sutil y (b) Dulce, apiladas en vertical si el PDF mide más de 4 pulgadas de ancho (todas salvo fig09, que va lado a lado); fig29, fig30 y fig25 van como figura única. El `\caption` de una figura doble contiene los dos pies de los TXT sin cambios, "(a) … (b) …"; cada subfigura lleva solo el nombre del cultivar. fig19b lleva "EXPLORATORY." al inicio del `\caption` (su TXT no lo tenía en mayúsculas); el de fig18b ya empezaba así. **Tablas:** `00_plan/mapa_evidencia.md` no designa principal o suplementaria; TS1 y T16 quedan como suplementarias (propuesta, marcada en el README del paquete). En las copias del paquete, TS1 lleva `\%` en lugar de `%` (en el original, el `%` sin escapar de las cabeceras "share (%)" comenta el resto de la línea y rompe la tabla) y la fecha de MIDAGRI como `\midagridate{}`; el original no se modificó. **Paquete:** `08_graficos/paper_mdpi/overleaf/` (55 PDF, `captions.tex`, `figures_{main,supp}.tex`, `tables_{main,supp}.tex`, `test_article.tex`, README), generado con `02_scripts/12_paquete_overleaf.py`, y copia en el Escritorio (`overleaf_mdpi/` y su zip). No se compiló: no hay LaTeX instalado.
29. **Ajustes del paquete Overleaf (2026-10-29). Estado: pendiente de aprobación.** Paquete aprobado por el autor, con estos cambios (`02_scripts/12_paquete_overleaf.py`; sin cifras nuevas):
    - **Tablas del texto principal**, escritas por script desde los CSV (inglés, booktabs):
      - TM1: series descriptivas por ventana 2021–2025, desde T03 (partición test: media, DE, CV) y T04 (train: n, ACF(1), ACF(12), ADF *p* y KPSS *p* en nivel; KPSS *p* acotado se muestra como "> 0.10").
      - TM2: agregados 2021–2025, mensual P75, desde T06. Contiene MAE global y MAE en meses de shock con IC 95 % bootstrap iid, Δs y n de meses en el título de cada bloque, para los 10 modelos (sin XGB-43). **Δs va sin IC: ningún CSV lo guarda**, y calcularlo sería una cifra nueva.
      - TM3: ranking por MAE en meses de shock en P50, P60, P75 y P90 y robustez E-BR1 (MoM e YoY), desde `T08_ranking_shock_principal_2021_2025_{c}.csv`.
    - **Suplementario:** TS1, T16, T05 (MAE y MAE en meses de shock por ventana), T09 (matriz DM sin ajustar, principal) y T11, copiados de sus `.tex`. T05, T09 y T11 siguen en español, y T05 incluye XGB-43.
    - **TS1:** el "%" sin escapar se corrige también en el original (`08_graficos/figuras_independientes/TS1_provinces.tex`; 4 apariciones, ningún otro cambio) y en `11_figuras_d3.py`, que ahora lo escapa al escribir la tabla. El CSV no cambia.
    - **Subfiguras sin letra** (`\captionsetup[subfigure]{labelformat=empty}`), con subtítulos "Sour lime" y "Sweet lime" (en la fig20 suplementaria, con el año). En el `\caption`, "*Sour lime:* … *Sweet lime:* …" en lugar de "(a) … (b) …".
    - **Pies sin referencias internas**, solo en el paquete (los TXT no cambian): "(D-BR8)" y "(D-BR6)" → "(pre-registered)"; "DESV-07; " se quita; "(v2 official implementation)" se quita.
    - **T16:** título y cabeceras traducidos en la copia del paquete.
    - **Verificación del script:** `\includegraphics` e `\input` existentes, sin "D-BR", "DESV" ni "v2 official" en `captions.tex` ni en las tablas, y 270 celdas de TM1–TM3 iguales a sus CSV (muestra de 5 en el informe al autor). No se compiló: no hay LaTeX instalado.
30. **fig_workflow (2026-10-29). Estado: aprobado por el autor (2026-10-29).** Diagrama del flujo de trabajo, diseño A (5 bloques horizontales), aprobado por el autor. Script: `02_scripts/13_figura_workflow.py`. Salida: `08_graficos/figuras_independientes/fig_workflow.{png,pdf,csv,txt}` (PNG 300 dpi), registrada al final de `indice_figuras_d3.csv`; las filas existentes no cambian.
    - **Sin resultados.** Cada texto se lee de la configuración o del código: `ventanas.json`, `umbrales.json`, `hiperparametros_congelados.json`, `03_ventanas/ventanas_viabilidad.csv`, `lib/evaluacion.py` y `src/models/features_gc3_ge.py`. El CSV guarda cada texto con su fuente (D-BR1 a D-BR6, D-BR10 y DESV-07).
    - **Correcciones aprobadas respecto del texto inicial:** el scaler y los pesos geográficos se ajustan solo con el train (hasta diciembre de Y−2), y el umbral con la historia hasta el origen (D-BR3); SARIMA-sel se añade (10 modelos); Holm figura como exploratorio (DESV-07); 2018–2020 corre solo Naive, Seasonal Naive y Chronos, y hay sensibilidad 2023–2025 (D-BR1); se usa "INDECI disasters", como en fig25.
    - **Opcionales incluidos:** particiones (train hasta Y−2, validación Y−1, test Y) en el bloque 3; "10 seeds (0–9)" para XGB-37, GC3 y GE en el bloque 4. La definición de shock va solo en el pie (TXT).
    - **XGB-43** aparece en una caja discontinua con su color (#44AA99), marcado "exploratory", a pedido del autor. **Esto contradice el punto 7** ("XGB-43 aparece solo en la exploratoria fig18b") y `08_graficos/README.md`; los dos quedan por actualizar si el autor aprueba este punto.
    - **Copias:** PDF y PNG en `paper_mdpi/overleaf/figures/` y en el Escritorio (`overleaf_mdpi/figures/`). Inclusión en el paquete: punto 31.
31. **fig_workflow en el paquete Overleaf (2026-10-29). Estado: aprobado por el autor (2026-10-29).**
    - **`12_paquete_overleaf.py`:** fig_workflow entra en el texto principal como figura única, entre fig24 y fig30. La posición es una decisión de implementación, no indicada por el autor.
    - **Archivo único y zip:** el script genera ahora `resultados_v2_completo.tex`, `figures_overleaf.zip` y `lista_figuras.md`, antes hechos con un script temporal, con la misma verificación: sin `\input` ni `\usepackage`, cada `\includegraphics` presente en el zip, ningún PDF sobrante, sin referencias internas, y llaves y entornos balanceados. Resultado: 30 figuras y 56 PDF.
    - **PNG:** se copia `fig_workflow.png` a `figures/` para el main.tex antiguo; no entra en el zip ni en el `.tex`.
    - **`11_figuras_d3.py`:** al reescribir `indice_figuras_d3.csv` conserva las filas de figuras que no genera él (fig_workflow). Probado sobre una copia: el índice resultante es idéntico al actual.
    - **Punto 7 y `08_graficos/README.md`:** dicen ahora "XGB-43 aparece solo en fig18b y, como caja exploratoria discontinua, en fig_workflow".

## DESV-09 — Figuras independientes y tabla suplementaria de la Fase D3

- **Fecha:** 2026-10-29. **Tipo:** implementación (presentación) y una descarga de datos externos (geometría). No se calcula ninguna métrica ni se cambia ningún CSV de las Fases C, D1 o D2.
- **Estado:** pendiente de aprobación del autor.
- **Script:** `02_scripts/11_figuras_d3.py`. **Salida:** `08_graficos/figuras_independientes/` (PNG 300 dpi + PDF + CSV + TXT; índice `indice_figuras_d3.csv`). Los 225 archivos de `08_graficos/` fuera de esa carpeta (Fase D2) tienen el mismo SHA-256 antes y después.

1. **fig24_series_with_shocks_{sutil,dulce}:** serie de `limon_{c}_nacional_mensual.csv` y meses de shock de `03_ventanas/umbrales_y_mascaras.csv` (mensual, P75, ventanas 2021–2025). Shocks: 10 (Sutil) y 15 (Dulce). El umbral de cada año se rotula sobre el panel (valor de la columna `umbral`, ya guardado). En Dulce, 14 de los 15 meses de shock caen en enero–marzo (recuento sobre las máscaras); el pie lo dice en una frase neutra. En Sutil son 2 de 10, sin frase.
2. **fig30_rolling_origin_scheme:** desde `03_ventanas/ventanas_viabilidad.csv` y D-BR1, sin resultados. Ventanas 2018–2020 atenuadas, con la nota de que solo corren Naive, Seasonal Naive y Chronos. Recuento de D-BR1 (118 viables, 42 no aplica) reproducido: el CSV no tiene columna de cultivar (88 filas = 8 ventanas × 11 modelos); 118 = 2 cultivares × 59 y 42 = 2 × 21, excluyendo XGB-43 (exploratorio).
3. **fig25_architecture_dual_lstm:** parámetros por capa leídos del modelo Keras de `build_gc3_ge_model` y comprobados con `expected_parameter_count`: GC3 6,273 y GE 6,657 (diferencia 384, solo en la LSTM de la rama B). **Modelo NLP verificado:** `v2_reentrenamiento/notebooks/fase2_features/01_nlp_sentimiento_ejecutado.ipynb` (celda 9) usa `pysentimiento.create_analyzer(task='sentiment', lang='es')`, que en el pysentimiento instalado corresponde a `pysentimiento/robertuito-sentiment-analysis` (`analyzer.py`, l. 27); escribe `data/interim/noticias/sentimiento_mensual_2016_2025.csv`, que es el `sentimiento_mensual` de `01_configuracion/rutas_datos.json`. DECISIONES_METODOLOGICAS.md (l. 276) dice "RoBERTuito". El pie cita solo RoBERTuito/pysentimiento; "BETO" aparece únicamente en nombres de variables y en código antiguo de v1 (`src/scraping/news_scraper.py`).
4. **fig29_study_area_map:** dos paneles; % sobre el total de cada cultivar (3,030,544 t Sutil; 48,994 t Dulce, 2016–2025); categorías 82/21/2/4; área del círculo proporcional a las toneladas del cultivar; rótulos de las 5 primeras provincias por cultivar; sin recuadro de zonas ni temperatura. Las 10 provincias con coordenada de departamento llevan un anillo discontinuo (entre ellas, las 2 de solo Dulce y las 4 sin cosecha). Los acentos de Morropón, Jaén y San Ignacio en los rótulos son solo de presentación (diccionario `ETIQUETA`); los datos conservan los nombres de MIDAGRI. Ñ verificada en CAÑETE, MARAÑON, DATEM DEL MARAÑON y FERREÑAFE (lectura con `utf-8-sig`).
5. **Geometría (descarga externa):** `11_geometria_externa/` (sin versionar; URL, fecha, tamaño y SHA-256 en su README). geoBoundaries gbOpen PER ADM1 (`PER-ADM1-1875124`, **Public Domain**, origen Wikimedia Commons, límites de 2008; cita Runfola et al., 2020) y Natural Earth 1:10m Admin 0 (dominio público). El ADM1 tiene 26 unidades: "Lima" y "Municipalidad Metropolitana de Lima" se unen en LIMA, como en MIDAGRI; "El Callao" queda como CALLAO, sin datos de producción. Resultado: 25 polígonos.
6. **Punto en polígono:** 108 de 109 coordenadas caen en su departamento. La excepción es **Tahuamanu (Madre de Dios, coordenada de provincia)**: Iñapari, en la frontera con Brasil, queda a 0.49 km fuera del polígono simplificado (Natural Earth la sitúa en Brasil). Es un efecto de la simplificación de los límites; no se cambia la coordenada.
7. **TS1_provinces:** 109 provincias más fila de totales; columnas: departamento, provincia, latitud, longitud, tipo de coordenada, categoría, toneladas 2016–2025, % del cultivar y meses con producción > 0 (de 120), para cada cultivar. Los meses con producción son un dato descriptivo nuevo (recuento directo, aprobado por el autor).
8. **Fecha de consulta de MIDAGRI–SISAGRI:** no está documentada en el repositorio (D21 ya declara que la cadena desde `sisagri_2015_2026.xlsx` no es reproducible). Se deja en blanco ("accessed [____]") en los pies de fig24, fig29 y TS1.

---

## DESV-10 — Definición de shock YoY con igual peso; STL y 3M como robustez

- **Fecha:** 2026-10-31. **Origen:** revisión G7, `09_reportes/revision_g7/fase3/INFORME_FASE3.md` §4.
- **Estado:** APROBADA por YesaR el 31-10-2026.
- **Motivo (revisión G7, Fases 1 y 2):** con MoM P75, 14 de 15 shocks de dulce caen en enero–marzo y son estacionalidad de composición (provincias de campaña corta). Además, la MoM no detecta las caídas graduales (sutil mar–jul 2023).
- **Cambio:** la YoY P75 (D-BR7, hoy secundaria) se reporta con el mismo peso que la MoM P75 en el texto principal: tablas de MAE_shock, MASE_shock, MAE_shock relativo al Seasonal Naive y robustez ≥ 3 de 4.
- **Robustez:** la desestacionalizada (STL, `period=12, seasonal=13, robust=True`, estacionalidad fijada al origen) y el cambio a 3 meses se reportan en el suplementario. La STL va con la advertencia de que no está calibrada (marca el 33–45 % de los meses con P75).
- **Se decidió después de ver los resultados.** La conclusión principal no cambia con ninguna definición (Fase 2, §1.6; Fase 3, §2.2).

---

## DESV-11 — Reajuste final con Y−1 (E1)

- **Fecha:** 2026-10-31. **Origen:** revisión G7, `09_reportes/revision_g7/fase3/INFORME_FASE3.md` §4.
- **Estado:** APROBADA por YesaR el 31-10-2026.
- **Motivo:** asimetría de información. Los modelos entrenados usaban coeficientes estimados hasta Y−2, mientras que Naive, Seasonal Naive y Chronos usan la historia hasta t−1.
- **Cambio:** variante "-Y1". Los hiperparámetros se eligen como en el preregistro (validación Y−1) y el ajuste final usa los datos hasta dic Y−1 (scaler y pesos geográficos incluidos).
  - SARIMA: mismo orden, coeficientes reestimados.
  - GC3/GE: tantas épocas como la mejor época de la corrida original, sin early stopping, con el calendario de LR de la corrida original vía `LearningRateScheduler`.
- **Incidencia:** SARIMA-sel-Y1 no converge en sutil 2021 (maxiter 500) y diverge. Se reporta sin respaldo. La sensibilidad que usa el ajuste original en ese caso es post-hoc.
- **Uso:** análisis de robustez; el ranking preregistrado se mantiene.

---

## DESV-12 — LSTM univariada (LSTM-U)

- **Fecha:** 2026-10-31. **Origen:** revisión G7, `09_reportes/revision_g7/fase3/INFORME_FASE3.md` §4.
- **Estado:** APROBADA por YesaR el 31-10-2026.
- **Motivo:** separar el efecto de la arquitectura del efecto de las exógenas.
- **Modelo:** una rama con la arquitectura de la rama A de GC3 y 6 entradas (producción y lags 1, 3 y 6, mes sin y cos), 2,417 parámetros, entrenamiento idéntico a GC3, en protocolos original y −Y1.
- **Uso:** post-hoc, fuera del ranking preregistrado, en tabla aparte.

---

## DESV-13 — DualLSTM residual (GC3-R)

- **Fecha:** 2026-10-31. **Origen:** revisión G7, `09_reportes/revision_g7/fase3/INFORME_FASE3.md` §4.
- **Estado:** APROBADA por YesaR el 31-10-2026.
- **Motivo:** probar si la DualLSTM mejora al aprender solo la desviación respecto del año anterior.
- **Modelo:** GC3 con objetivo r_t = y_t − y_{t−12}, estandarizado con estadísticas del train, y ŷ_t = y_{t−12} + r̂_t, en ambos protocolos.
- **Uso:** post-hoc, fuera del ranking preregistrado.

---

## DESV-14 — Chronos-Bolt small y base

- **Fecha:** 2026-10-31. **Origen:** revisión G7, `09_reportes/revision_g7/fase3/INFORME_FASE3.md` §4.
- **Estado:** APROBADA por YesaR el 31-10-2026.
- **Modelo:** zero-shot con el protocolo de Chronos-Bolt-tiny, ventanas 2018–2025, revisiones HF `772f3d25…` (small) y `5d9f166d…` (base), descargadas una vez y usadas offline.
- **Uso:** sensibilidad al tamaño del modelo fundacional. Chronos-Bolt-tiny sigue siendo el del ranking. El checkpoint no se eligió con ningún resultado.
