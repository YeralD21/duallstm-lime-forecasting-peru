# Revisión G7 — Fase 5: ETL reproducible, texto de figuras, fig20 reducida, calendario de shocks, verificación de tablas y DESV-10 a DESV-14

- **Fecha:** 2026-10-31. **Rama:** `revision-experimento-v2`. Sin commit, push ni tag, y sin cambio de rama.
- **Archivos modificados:** solo los autorizados en B (3 scripts de figuras) y F (`DESVIACIONES.md`). Lo demás
  son archivos nuevos o figuras regeneradas. Ninguna tabla congelada ni ningún resultado se sobrescribió.
- **Integridad:** los 93 archivos de `01_configuracion/hashes_congelados.json` (código oficial, datos,
  referencias y Chronos) tienen el mismo SHA-256 al terminar (93 OK, 0 diferencias). Todos los CSV de
  `08_graficos/` (datos de figuras e índices) son idénticos antes y después.

---

## A. ETL reproducible (observación 12)

### A.1 Qué se encontró

**No existe en el repositorio ni en su historial código que genere estos archivos.**

- **Búsqueda en el árbol:** todo el repositorio menos `venv/`, incluidos v1, `src/`, `sources/`, `notebooks/`,
  `pipeline/` y `scratch/`. Se buscaron los nombres `distrito_crudo`, `nacional_mensual`, `_provincia.csv`,
  `indeci_limpio_2016_2025`, `coordenadas_provincias_completo`, `sisagri_2015_2026` y
  `BD_2003-2025_EMERGENCIAS`. Todos los resultados son consumidores (notebooks de la Fase 2 de v2, scripts del
  backtesting, `nasa_power_downloader_v2.py`) o documentos.
- **Historial:** `git log --all -S <nombre>` sobre las 9 ramas locales y remotas (64 commits), con los mismos
  nombres. Ningún commit añade código productor. `distrito_crudo` no aparece en ningún diff. En
  `v2_reentrenamiento/notebooks/fase1_recoleccion/` solo se versionaron `09_resumen_fase1*.ipynb` (commit
  `ee5f9be`); los notebooks 01–08 de la Fase 1 nunca entraron en git. No hay stash.
- **Lo que sí está documentado:** las reglas, en `DECISIONES_METODOLOGICAS.md` (deduplicación de Ayacucho,
  agregación distrito→provincia, fuente y filtros de INDECI, coordenadas por fallback departamental) y en D21
  ("no es reproducible… inputs congelados").
- **Coordenadas, origen trazable en v1:**
  - las 99 "exactas" son, carácter por carácter, las `lat`/`lon` de `data/interim/nasa/clima_dataset_final.csv`
    de v1;
  - las 10 de fallback son el diccionario `COORDS_DEPTO` de `notebooks/fase2/_build_act02_time.py` de v1
    (commit `7dbd515`, 2026-05-14).
- **Nunca documentado:** el origen primario de las 99 coordenadas de v1. Ningún código las genera y sus
  decimales sugieren una conversión manual desde grados, minutos y segundos.

**Hallazgo — el "centroide del departamento" no lo es.** `DECISIONES_METODOLOGICAS.md` habla de "centroide del
departamento" y el código de v1 de "centroide aproximado". Los 10 valores de fallback son en realidad las
coordenadas de la **capital** del departamento (Lima ciudad, Iquitos, Huaraz, Trujillo, Chiclayo, Piura, Ica,
Huánuco). El texto del manuscrito debería decir "departmental capital".

### A.2 Scripts creados: `v2_reentrenamiento/etl/`

| Archivo | Función |
|---|---|
| `_comun.py` | Rutas; carpeta de salida (se niega a escribir dentro de `data/interim/`); SHA-256 con el método 2 de `hashes_congelados.json`; comparación fila a fila y celda a celda como texto |
| `01_sisagri_a_series.py` | Excel SISAGRI → `distrito_crudo` → `distrito_dedup` → `provincia` → `nacional_mensual`, para sutil y dulce |
| `02_indeci_a_panel.py` | `BD_2003-2025_EMERGENCIAS.csv` → panel provincia × mes 2016–2025; los meses sin registro se codifican como 0 |
| `03_coordenadas.py` | Coordenadas de las 109 provincias desde v1 y validación de punto en polígono con geoBoundaries ADM2 |
| `README.md` | Uso, reglas, fuentes y limitaciones |

Los scripts se escribieron de nuevo porque no había código que recuperar. Las reglas siguen
`DECISIONES_METODOLOGICAS.md`. Los detalles que esa fuente no fija se dedujeron comparando con los congelados y
están marcados como empíricos en el README:
- regla de formato de las filas deduplicadas: 2 decimales; SIEMBRA y COSECHA `0.0` si todo el grupo es 0;
- orden de cálculo: provincia desde el CSV dedup escrito, nacional desde el CSV provincial redondeado;
- redondeo de Python (`f"{x:.2f}"`) y no de numpy.

Detalles necesarios para la reproducción:
- **Dimensiones falsas del Excel:** 4 de las 5 hojas declaran `A1:A1`. Sin `reset_dimensions()`, openpyxl en
  modo `read_only` solo lee 1 fila de esas hojas. Las 5 hojas son 2015–2018, 2018–2020, 2020–2023, 2023–2025 y
  2025–2026, con 4 × 1,048,002 + 90,783 filas.
- **Coordenadas, universo:** unión de provincias de sutil (107) y dulce (28) = 109.
- **INDECI, universo:** solo las 107 provincias de sutil. CARHUAZ y YUNGAY (Áncash), que solo tienen dulce, no
  están en el panel congelado. Es coherente con la cobertura INDECI < 100 % de la masa de pesos que
  DECISIONES documenta para dulce.

### A.3 Comparación con las tablas congeladas

Los scripts se ejecutaron sobre la carpeta temporal `%TEMP%\etl_v2_salida` (no sobre `data/interim`).
- **Tolerancia:** 0. Igualdad de texto celda a celda; no hizo falta tolerancia de redondeo.
- **SHA-256:** método 2 (CRLF → LF), comparado con el archivo en disco y, si existe, con `hashes_congelados.json`.

| Archivo congelado (`data/interim/`) | Filas (nuevo/congelado) | Celdas distintas | SHA-256 = disco | SHA-256 = `hashes_congelados.json` |
|---|---|---:|---|---|
| `limon_sutil_distrito_crudo.csv` | 57,445 / 57,445 | 0 | sí | no registrado |
| `limon_sutil_distrito_dedup.csv` | 55,822 / 55,822 | 0 | sí | no registrado |
| `limon_sutil_provincia.csv` | 12,425 / 12,425 | 0 | sí | **sí** |
| `limon_sutil_nacional_mensual.csv` | 120 / 120 | 0 | sí | **sí** |
| `limon_dulce_distrito_crudo.csv` | 9,568 / 9,568 | 0 | sí | no registrado |
| `limon_dulce_distrito_dedup.csv` | 9,568 / 9,568 | 0 | sí | no registrado |
| `limon_dulce_provincia.csv` | 3,128 / 3,128 | 0 | sí | **sí** |
| `limon_dulce_nacional_mensual.csv` | 120 / 120 | 0 | sí | **sí** |
| `indeci_limpio_2016_2025.csv` | 12,840 / 12,840 | 0 | sí | **sí** |
| `coordenadas_provincias_completo.csv` | 109 / 109 | 0 | sí | no registrado (igual al de `HEAD`) |

**Ninguna diferencia.** Los 10 archivos se reproducen byte a byte (con fin de línea normalizado), y los 5 que
figuran en `hashes_congelados.json` coinciden con el hash registrado.
- **01 (SISAGRI):** 9 min 55 s leyendo el Excel completo, sin caché. Se leyeron 72,045 filas de limón de
  2015–2026: 61,741 de sutil y 10,304 de dulce. Tras filtrar 2016–2025 quedan 57,445 y 9,568. Hay 1,623 filas
  sobrantes en 1,061 claves duplicadas, todas de Ayacucho, que dan 55,822 filas tras la deduplicación.
- **02 (INDECI):** 65,129 registros climáticos de 2016–2025 y 5,609 provincia-mes sin registro codificados
  como 0. Las 89 provincias con registros fuera del universo (no limoneras) se descartan.

**Validación de coordenadas** (fuente documentada): geoBoundaries gbOpen PER ADM2.
- **Fuente:** IGN Perú vía OCHA ROLAC/HDX, CC BY 3.0 IGO, boundaryID `PER-ADM2-86281439`, 196 provincias.
- **Versión:** fijada en el commit `90a1d52` (el mismo del ADM1 de `11_geometria_externa`), SHA-256 `4986d514…`.
  Se descargó a la carpeta temporal; no se guardó en el repositorio.
- **Exactas:** 99/99 caen dentro del polígono de su provincia. FERREÑAFE solo se empareja tras reparar el
  mojibake del nombre en el GeoJSON.
- **Fallback:** 2/10 caen dentro de su provincia (LIMA y CHICLAYO, que son provincias capitales). Las otras 8
  caen en la provincia capital del departamento, a esta distancia de su polígono propio:

| Provincia (dep.) | Cae en | km al polígono propio |
|---|---|---:|
| Carhuaz (Áncash) | Huaraz | 14.8 |
| Yungay (Áncash) | Huaraz | 28.3 |
| Marañón (Huánuco) | Huánuco | 100.9 |
| Nasca (Ica) | Ica | 69.2 |
| Ascope (La Libertad) | Trujillo | 13.4 |
| Cañete (Lima) | Lima | 49.9 |
| Datem del Marañón (Loreto) | Maynas | 309.9 |
| Talara (Piura) | Piura | 55.1 |

### A.4 Archivos crudos

**No falta ningún archivo crudo:**
- el Excel `sisagri_2015_2026.xlsx` (229 MB, sin versionar por tamaño, fecha en disco 2026-08-29);
- el INDECI consolidado `BD_2003-2025_EMERGENCIAS.csv` (27 MB). Pese a estar en la carpeta
  `oficial_2016_2018`, cubre 2003–2025;
- el `clima_dataset_final.csv` de v1.

**Sin documentar:** la fecha de descarga del Excel SISAGRI y la del CSV de INDECI. DECISIONES dice "actualizado
2026-08-26" para el INDECI; no se inventa ninguna fecha. Tampoco hay URL de descarga del Excel en el repositorio.

---

## B. Texto dentro de las figuras (observaciones 2 y 3)

**Cambios de texto** (solo cadenas, sin cambiar la lógica):

| Script | Línea aprox. | Antes → después |
|---|---|---|
| `10_figuras.py` | 171 (fig05, TXT) | "…per month (D-BR6)." → "…per month." |
| | 356 (fig12, TXT) | "…reported separately (D-BR7)." → "…reported separately." |
| | 456 (fig15, TXT) | "…bootstrap intervals (D-BR6)." → "…bootstrap intervals." |
| | 565 (fig02 sutil, **dentro de la figura**) | "…by the level shift (D-BR8)." → "…by the level shift." |
| | 574 (fig02, TXT) | "As pre-declared (D-BR8), the 2.0 flag" → "As specified in the protocol, the 2.0 flag" |
| | 581 (fig02, TXT) | "overfitting flag at 2.0 (D-BR8)." → "overfitting flag at 2.0, specified in the protocol." |
| | 798 (fig18b, **dentro de la figura**) | "not part of the preregistered ranking" → "not part of the ranking specified in the protocol" |
| | 809 (fig18b, TXT) | "…of the preregistered analysis." → "…of the analysis specified in the protocol." |
| | 817 (fig18b, TXT) | "not part of the preregistered ranking" → "not part of the ranking specified in the protocol" |
| | 868 (fig19b, TXT) | "not part of the pre-registration." → "not part of the protocol." |
| `11_figuras_d3.py` | 207 (fig30, TXT) | "a pre-registered sensitivity analysis" → "a sensitivity analysis specified in the protocol" |
| | 209 (fig30, TXT) | "…excluded from the count), as in D-BR1." → "…), as specified in the protocol." |
| `13_figura_workflow.py` | 169 (TXT) | "is a pre-registered sensitivity set" → "is a sensitivity set specified in the protocol" |
| | 179 (TXT) | "follows the pre-registration." → "follows the protocol." |

Antes de cambiar nada, `pdftotext` sobre los 116 PDF de `08_graficos/` encontró texto prohibido **dentro de
3 figuras** (fig02_sutil y fig18b sutil/dulce) y sus copias en Overleaf. Las demás cadenas solo estaban en los TXT.

**Regeneradas (solo las afectadas), 14 figuras:**
- `10_figuras.py --solo fig05 fig12 fig15 fig02 fig18b fig19b`: 12 figuras;
- `fig30()` de `11_figuras_d3.py`;
- `13_figura_workflow.py`: fig_workflow.

**Cambiaron 31 archivos:**
- 14 PDF y 14 TXT;
- 3 PNG: fig02_sutil y fig18b sutil/dulce, las únicas con texto dentro de la imagen.

Los otros PNG son idénticos byte a byte. Los PDF cambian solo por los metadatos de creación. Los CSV de datos,
`indice_figuras.csv` e `indice_figuras_d3.csv` son idénticos.

Lista de archivos regenerados (`08_graficos/`):
```
diagnostico_ajuste/fig02_train_val_gap_{sutil,dulce}.{pdf,txt}      (+ png sutil)
sensibilidad_umbral/fig05_mae_shock_vs_percentile_{sutil,dulce}.{pdf,txt}
sensibilidad_umbral/fig12_yoy_vs_mom_threshold_{sutil,dulce}.{pdf,txt}
comparacion_modelos/fig15_seed_boxplots_{sutil,dulce}.{pdf,txt}
comparacion_modelos/fig18b_xgb43_vs_xgb37_exploratory_{sutil,dulce}.{pdf,png,txt}
comparacion_modelos/fig19b_dm_pvalue_matrix_holm_{sutil,dulce}.{pdf,txt}
figuras_independientes/fig30_rolling_origin_scheme.{pdf,txt}
figuras_independientes/fig_workflow.{pdf,txt}
```

**Incidencia (corregida).** Para regenerar solo fig30 se importó `11_figuras_d3.py`. Su `preparar_entorno()`
relanza el proceso con `sys.argv`, así que se ejecutó el `main()` completo:
- se reescribieron también fig24, fig25, fig29 y TS1, con PNG, CSV, TXT y `.tex` idénticos byte a byte;
- los 4 PDF de fig24 (×2), fig25 y fig29 cambiaron de bytes solo por los metadatos.

Esos 4 PDF se restauraron con los bytes de `HEAD`, y su SHA-256 coincide con el de antes. Resultado final:
fig24, fig25, fig29 y TS1 están exactamente como antes.

**Copia a Overleaf:** los 14 PDF regenerados que ya estaban en el paquete se copiaron a
`08_graficos/paper_mdpi/overleaf/figures/` (fig02 ×2, fig05 ×2, fig12 ×2, fig15 ×2, fig18b ×2, fig19b ×2, fig30
y fig_workflow), más las 2 fig20 reducidas de C.

**Verificación con `pdftotext`:** ningún PDF contiene "D-BR", "pre-regist" ni "preregist":
- 0 de los 118 PDF de `08_graficos/` (incluidos los 58 de `overleaf/figures/`);
- 0 de los TXT de `08_graficos/`.

**Pendiente fuera del alcance autorizado (no se tocó):**
- `paper_mdpi/overleaf/captions.tex` aún contiene 10 apariciones de "pre-registered/preregistered". Las genera
  `12_paquete_overleaf.py`, que sustituye "(D-BR8)" y "(D-BR6)" por "(pre-registered)" (DESV-08, punto 29).
  `resultados_v2_completo.tex`, `main_v2_listo12.tex` y las tablas no tienen ninguna.
- `figures_overleaf.zip` (sin versionar) contiene los PDF anteriores y no se regeneró.
- Los códigos D-BR siguen en columnas internas de trazabilidad que no se dibujan: la columna `fuente` del CSV
  de fig_workflow e `indice_figuras_d3.csv`.

---

## C. Figura 2025 reducida

- **Script nuevo:** `02_scripts/14_fig20_reducida_2025.py`. Reutiliza los datos, el estilo y las funciones de
  `10_figuras.py` importándolo, sin ejecutar su `main()`.
- **Salida:** `08_graficos/predicciones/fig20_real_vs_pred_2025_main_{sutil,dulce}.{png,pdf,csv,txt}`. Los
  PDF también se copiaron a `overleaf/figures/`.
- **Contenido:** 4 paneles en una fila (GC3, Chronos, SARIMA, Seasonal Naive) con Observed en cada uno.
  - Estilo de fig20: Observed negra gruesa con halo; shocks P75 mensuales sombreados; color y marcador por
    modelo; Seasonal Naive discontinuo con cuadrados huecos.
  - GC3 = media de las 10 semillas por mes (comprobado: 10 semillas por mes; columna `n_semillas_promediadas`
    en el CSV).
- **Sin cambios:** las fig20 originales y `indice_figuras.csv` (no se añadieron filas).

---

## D. Tabla suplementaria del calendario de shocks

- **Archivo:** `09_reportes/revision_g7/fase5/TS_shock_calendar.tex`.
- **Script:** `fase5/scripts/D_ts_shock_calendar.py`, desde `fase1/B1_calendario_shocks_P75.csv`.
- **Formato:** inglés, `booktabs` + `longtable`, `\label{tab:shock_calendar}`.
- **Contenido:** 51 meses, en dos bloques por cultivar.
  - Sour lime: 20 (MoM 10, YoY 10). Sweet lime: 31 (MoM 15, YoY 16).
  - Columnas: fecha, definición, mes de referencia, cambio % con signo, umbral % e inicio o continuación.
  - El pie define MoM e YoY, el umbral (P75 del cambio absoluto con la historia hasta el origen; se compara
    con ">"), "Onset" y "Continuation".
- **Control:** los 51 cambios y los 51 umbrales del `.tex`, redondeados a 1 decimal, coinciden con el CSV.

---

## E. Verificación de `tablas_revision_g7.tex`

- **Script:** `fase5/scripts/E_verificar_tablas.py`.
- **Salida completa:** `fase5/E_verificacion_tablas.csv`, con una fila por celda: tabla, fila, columna, valor
  del .tex, valor del CSV con precisión completa, archivo y coincidencia.
- **Criterio:** |CSV − tex| ≤ 0,5·10⁻ᵈ (d = decimales mostrados). "<0.001" se comprueba como p < 0,001.
- **Fuentes:**
  - `12_revision_g7/resultados/T1_metricas_P75_MoM_YoY.csv`: MAE, IC, RMSE, MASE y métricas de shock.
  - `T5_DM_HLN_vs_mejor_univariado.csv`: d̄ y p.
  - `09_reportes/revision_g7/fase1/E2_razon_val_train_gt2.csv`: sobreajuste.
  - `errores_test_promediados_semillas_g7.csv`: nota (a).
  - Los rangos R1 y R2 son el orden de la columna MAE de T1 en cada pool.
- **Control:** T1 coincide con `06_metricas/agregadas/T06_agregadas_IC.csv` para los 10 modelos originales
  (P75 mensual), con max |dif| = 2,9·10⁻⁶.

**Resultado: 426 comprobaciones, 423 coinciden y 3 no.**

| Tabla | Comprobaciones | No coinciden |
|---|---:|---:|
| `tab:shock_scaled` | 132 (120 celdas + 8 negritas = mínimo de la columna + 4 n de shocks del pie) | 0 |
| `tab:diag_experiments` | 84 (incluida la nota (a): 73,706 y 3,183) | 2 |
| `tab:supp_metrics` | 210 | 1 |

| Celda | Valor en el .tex | Valor en el CSV | Archivo |
|---|---|---|---|
| `tab:diag_experiments`, GE-Y1, sour lime, d̄ | +3,892 | 3,891.49 → **+3,891** | `12_revision_g7/resultados/T5_DM_HLN_vs_mejor_univariado.csv` (global, principal) |
| `tab:diag_experiments`, ElasticNet-Y1, sour lime, d̄ | +1,728 | 1,727.47 → **+1,727** | ídem |
| `tab:supp_metrics`, GC3, sweet lime, CI iid (límite superior) | 67.0 | 66.95 → **66.9** | `12_revision_g7/resultados/T1_metricas_P75_MoM_YoY.csv` (también T06) |

Las 3 diferencias son de una unidad en el último dígito. Las dos de d̄ parecen calculadas como resta de MAE ya
redondeados (6,540 − 2,649 = 3,891; 4,376 − 2,649 = 1,727) o con otro redondeo. El valor correcto es el del CSV.

**Problemas de LaTeX** (no numéricos):
- `tab:supp_metrics` tiene `\bottomrule \\` en mitad de la tabla (l. 93, tras el bloque de sour lime) y dos
  `\bottomrule` seguidos al final (l. 106–107). Lo habitual sería `\midrule` entre bloques y un solo `\bottomrule`.
- Las tres tablas usan `adjustwidth` y `\extralength`, que existen en la plantilla MDPI.
- La cabecera del archivo dice "PENDIENTE (Fase 5): regenerar estas tablas por script". No se regeneraron:
  solo se pidió verificarlas.

---

## F. Desviaciones aprobadas

Se añadieron al final de `09_reportes/DESVIACIONES.md` DESV-10 a DESV-14, con el texto de `INFORME_FASE3.md` §4:
- mismo formato que las anteriores (separador `---`, título `## DESV-NN — …`, viñetas `**Fecha:**`, `**Estado:**`);
- fin de línea CRLF, como el resto del archivo;
- estado "APROBADA por YesaR el 31-10-2026".

Se quitó "Estado: pendiente de aprobación" del título de cada borrador; el resto del texto no cambió.
**Ninguna otra DESV cambió:** los primeros 34,651 bytes del archivo (todo el contenido anterior) son idénticos
a la copia previa (`cmp`).

---

## Archivos creados y modificados

**Modificados (autorizados):**
- `02_scripts/10_figuras.py`, `02_scripts/11_figuras_d3.py`, `02_scripts/13_figura_workflow.py`: solo texto (B).
- `09_reportes/DESVIACIONES.md`: solo se añadió texto al final (F).
- Figuras regeneradas en `08_graficos/` (B; lista arriba) y copias de PDF en `paper_mdpi/overleaf/figures/`.

**Nuevos:**
- `v2_reentrenamiento/etl/{_comun.py, 01_sisagri_a_series.py, 02_indeci_a_panel.py, 03_coordenadas.py, README.md}`
- `02_scripts/14_fig20_reducida_2025.py`
- `08_graficos/predicciones/fig20_real_vs_pred_2025_main_{sutil,dulce}.{png,pdf,csv,txt}`
- `09_reportes/revision_g7/fase5/`: `INFORME_FASE5.md`, `TS_shock_calendar.tex`, `E_verificacion_tablas.csv`,
  `scripts/D_ts_shock_calendar.py` y `scripts/E_verificar_tablas.py`

**Fuera del repositorio** (salidas del ETL, temporales): `%TEMP%\etl_v2_salida\`. Contiene los CSV regenerados,
`comparacion_0X_*.json`, `validacion_coordenadas_adm2.csv`, el GeoJSON ADM2 y la caché de filas de limón.

---

## NO VERIFICABLE

- **Código original del ETL:** no existe en el repositorio ni en el historial de git. Los scripts nuevos
  reproducen los bytes, pero no prueban que el procedimiento original fuera idéntico. Las reglas de formato y
  orden de cálculo son empíricas.
- **Origen primario de las 99 coordenadas de v1:** sin documentar. Solo se validan contra los límites ADM2 del IGN.
- **Fechas de descarga** del Excel MIDAGRI-SISAGRI y del CSV de INDECI, y URL del Excel: no documentadas. Por
  eso el "accessed [____]" de fig24, fig29 y TS1 sigue en blanco.
- **Compilación LaTeX** de `TS_shock_calendar.tex` y de las tablas: no hay LaTeX instalado.
- **`tab:supp_metrics`:** el texto del pie "MASE with a single denominator per window" no se puede comprobar
  contra los CSV, que no guardan el denominador. Las cifras de MASE sí coinciden.

---

## Para subir a Overleaf

Figuras (desde `08_graficos/paper_mdpi/overleaf/figures/`, ya copiadas):
```
fig02_train_val_gap_sutil.pdf            fig02_train_val_gap_dulce.pdf
fig05_mae_shock_vs_percentile_sutil.pdf  fig05_mae_shock_vs_percentile_dulce.pdf
fig12_yoy_vs_mom_threshold_sutil.pdf     fig12_yoy_vs_mom_threshold_dulce.pdf
fig15_seed_boxplots_sutil.pdf            fig15_seed_boxplots_dulce.pdf
fig18b_xgb43_vs_xgb37_exploratory_sutil.pdf  fig18b_xgb43_vs_xgb37_exploratory_dulce.pdf
fig19b_dm_pvalue_matrix_holm_sutil.pdf   fig19b_dm_pvalue_matrix_holm_dulce.pdf
fig30_rolling_origin_scheme.pdf
fig_workflow.pdf
fig20_real_vs_pred_2025_main_sutil.pdf   fig20_real_vs_pred_2025_main_dulce.pdf   (NUEVAS)
```
Tabla: `09_reportes/revision_g7/fase5/TS_shock_calendar.tex` (requiere `\usepackage{longtable}` y `booktabs`).

**Cambio visible:** solo fig02_sutil y fig18b (sutil y dulce). En las demás PDF solo cambian los metadatos;
subirlas es opcional. Los pies del manuscrito que copian el texto de los TXT o de `captions.tex` deben
actualizarse a mano: `captions.tex` todavía dice "pre-registered".
