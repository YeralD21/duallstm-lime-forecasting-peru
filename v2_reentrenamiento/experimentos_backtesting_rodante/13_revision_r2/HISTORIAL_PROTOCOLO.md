# Historial del protocolo y del preregistro (revisión R2, T14, obs. 8)

<!-- generado por scripts/t14_historial_protocolo.py; no editar a mano -->

Extraído del repositorio antiguo (privado) en modo solo lectura (`git log` y `git show`; sin checkout ni fetch). Está aquí y no en `01_configuracion/`, porque esa carpeta está preregistrada y congelada.

- Rama del clon: `revision-experimento-v2`; HEAD `e30fd323fbd7bfbcd520f634b9137878235442d0`; ramas remotas (refs locales) que contienen HEAD: `origin/revision-experimento-v2`.
- Comando por archivo: `git log --follow --format="%H %ad %s" --date=iso -- <ruta>`. Se añaden la fecha de commit (`%cd`) y la ruta en cada commit (`--name-only`).
- SHA-256 de cada versión: `git show <commit>:<ruta>`, en bytes tal cual y con CRLF → LF (método de `hashes_congelados.json`). «Igual al publicado» compara esa versión con el archivo de este repositorio.
- Las fechas son las que registra git en el clon (zona horaria del autor). No son un sello de tiempo de terceros: git permite fijarlas a mano. La prueba independiente sería la fecha de push en GitHub (registro de eventos del repositorio privado), que no se puede consultar sin red.

## Resumen: primera versión de cada archivo

| archivo | primer commit | fecha (autor) | mensaje | n versiones | última versión igual al publicado |
|---|---|---|---|---|---|
| `00_plan/borrador_preregistro.md` | `344134b041` | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 2 | sí |
| `00_plan/plan_fase_A.md` | `344134b041` | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 1 | sí |
| `00_plan/mapa_evidencia.md` | `344134b041` | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 1 | sí |
| `00_plan/nota_chronos_pesos.md` | `344134b041` | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 1 | sí |
| `01_configuracion/ventanas.json` | `344134b041` | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 1 | sí |
| `01_configuracion/umbrales.json` | `344134b041` | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 1 | sí |
| `01_configuracion/hiperparametros_congelados.json` | `344134b041` | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 1 | sí |
| `01_configuracion/manifest.json` | `344134b041` | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 4 | sí |
| `01_configuracion/hashes_congelados.json` | `344134b041` | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 2 | sí |
| `01_configuracion/rutas_datos.json` | `344134b041` | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 1 | sí |
| `01_configuracion/estilo_figuras.json` | `344134b041` | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 1 | sí |
| `v2_reentrenamiento/DECISIONES_METODOLOGICAS.md` | `ee5f9be562` | 2026-09-03 20:53:07 -0500 | feat(v2): Fases 1-3 completas - recoleccion, features, modelado inicial. Fase 1: MIDAGRI, NASA POWER, INDECI, scraping+NLP (2016-2025). Fase 2: fusion de 5 fuentes, codificacion ciclica, lags, escalado. Fase 3: baseline Naive + GC1 (SARIMA + Prophet). DECISIONES_METODOLOGICAS.md con trazabilidad completa. Excel MIDAGRI excluido via .gitignore (218MB, supera limite GitHub) | 6 | sí |
| `09_reportes/DESVIACIONES.md` | `ddb8d4aefd` | 2026-10-28 19:02:43 -0500 | feat(backtesting): scripts reanudables de la Fase C, enmienda E-BR1, biblioteca lib y registro de desviaciones | 4 | no |
| `09_reportes/reporte_fase_A.md` | `344134b041` | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 1 | sí |
| `09_reportes/reporte_fase_B.md` | `344134b041` | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 1 | sí |
| `09_reportes/nota_v5_v3.md` | `344134b041` | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 2 | sí |

## Cronología frente a la ejecución del experimento (Fase C)

- Commits del preregistro (25-oct-2026): `db32108` 2026-10-25 22:22:33 -0500 «docs(backtesting): preregistro final copiado a DECISIONES_METODOLOGICAS antes de la Fase C»; `344134b` 2026-10-25 22:16:40 -0500 «docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C».
- Unidades rolling-origin terminadas (`04_modelos/**/completado.json` de este repositorio, campo `fin`): 488, entre 2026-10-28T19:03:18-05:00 y 2026-10-28T20:13:01-05:00.
- Versiones posteriores al 25-oct de los archivos listados: ver la tabla de cada archivo (fecha y mensaje del commit). Los cambios de protocolo posteriores están registrados en `09_reportes/DESVIACIONES.md`.

## Historial completo por archivo

### `v2_reentrenamiento/experimentos_backtesting_rodante/00_plan/borrador_preregistro.md`

| commit | fecha (autor, %ad) | fecha (commit, %cd) | mensaje | bytes | SHA-256 (bytes) | SHA-256 (CRLF→LF) | igual al publicado |
|---|---|---|---|---|---|---|---|
| `db321084230df8c313f8eebf56922e79212d71e9` | 2026-10-25 22:22:33 -0500 | 2026-10-25 22:22:33 -0500 | docs(backtesting): preregistro final copiado a DECISIONES_METODOLOGICAS antes de la Fase C | 11805 | `761c4429a12c21c3e72ea5250374c1e3f8c93707fcba14bd3400e9a8fa5f3be1` | `761c4429a12c21c3e72ea5250374c1e3f8c93707fcba14bd3400e9a8fa5f3be1` | sí |
| `344134b0418718529c678473cddb1b6fff8cab4b` | 2026-10-25 22:16:40 -0500 | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 10607 | `127efebaf5072320d0e35ea459a1037d1ed77fc49ab3eb95f3f4769de647222c` | `127efebaf5072320d0e35ea459a1037d1ed77fc49ab3eb95f3f4769de647222c` | no |

### `v2_reentrenamiento/experimentos_backtesting_rodante/00_plan/plan_fase_A.md`

| commit | fecha (autor, %ad) | fecha (commit, %cd) | mensaje | bytes | SHA-256 (bytes) | SHA-256 (CRLF→LF) | igual al publicado |
|---|---|---|---|---|---|---|---|
| `344134b0418718529c678473cddb1b6fff8cab4b` | 2026-10-25 22:16:40 -0500 | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 24129 | `f17c3e85d6be2e92d9aa5221a75f47330bfcdf18cd5fed6c31d266eaa455e1ad` | `f17c3e85d6be2e92d9aa5221a75f47330bfcdf18cd5fed6c31d266eaa455e1ad` | sí |

### `v2_reentrenamiento/experimentos_backtesting_rodante/00_plan/mapa_evidencia.md`

| commit | fecha (autor, %ad) | fecha (commit, %cd) | mensaje | bytes | SHA-256 (bytes) | SHA-256 (CRLF→LF) | igual al publicado |
|---|---|---|---|---|---|---|---|
| `344134b0418718529c678473cddb1b6fff8cab4b` | 2026-10-25 22:16:40 -0500 | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 7538 | `bc34bbdc0d2526c4a54c367c0c95abbd7f43e0e22d62e189470ab1e3294a967a` | `bc34bbdc0d2526c4a54c367c0c95abbd7f43e0e22d62e189470ab1e3294a967a` | sí |

### `v2_reentrenamiento/experimentos_backtesting_rodante/00_plan/nota_chronos_pesos.md`

| commit | fecha (autor, %ad) | fecha (commit, %cd) | mensaje | bytes | SHA-256 (bytes) | SHA-256 (CRLF→LF) | igual al publicado |
|---|---|---|---|---|---|---|---|
| `344134b0418718529c678473cddb1b6fff8cab4b` | 2026-10-25 22:16:40 -0500 | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 2659 | `98b09be497465bd920b84bdf33dbc083c27af60f44f0f58bb8d973112da0f52b` | `98b09be497465bd920b84bdf33dbc083c27af60f44f0f58bb8d973112da0f52b` | sí |

### `v2_reentrenamiento/experimentos_backtesting_rodante/01_configuracion/ventanas.json`

| commit | fecha (autor, %ad) | fecha (commit, %cd) | mensaje | bytes | SHA-256 (bytes) | SHA-256 (CRLF→LF) | igual al publicado |
|---|---|---|---|---|---|---|---|
| `344134b0418718529c678473cddb1b6fff8cab4b` | 2026-10-25 22:16:40 -0500 | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 592 | `a77a2559d05655e83a98de3ed6c7f6d139f07d147f8318289a04dc4dc39807c1` | `a77a2559d05655e83a98de3ed6c7f6d139f07d147f8318289a04dc4dc39807c1` | sí |

### `v2_reentrenamiento/experimentos_backtesting_rodante/01_configuracion/umbrales.json`

| commit | fecha (autor, %ad) | fecha (commit, %cd) | mensaje | bytes | SHA-256 (bytes) | SHA-256 (CRLF→LF) | igual al publicado |
|---|---|---|---|---|---|---|---|
| `344134b0418718529c678473cddb1b6fff8cab4b` | 2026-10-25 22:16:40 -0500 | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 856 | `bd695b1291e8e24e0dfed25e5b3860ba1fd7c039d7563974ce6d7ad4e8dc0f50` | `bd695b1291e8e24e0dfed25e5b3860ba1fd7c039d7563974ce6d7ad4e8dc0f50` | sí |

### `v2_reentrenamiento/experimentos_backtesting_rodante/01_configuracion/hiperparametros_congelados.json`

| commit | fecha (autor, %ad) | fecha (commit, %cd) | mensaje | bytes | SHA-256 (bytes) | SHA-256 (CRLF→LF) | igual al publicado |
|---|---|---|---|---|---|---|---|
| `344134b0418718529c678473cddb1b6fff8cab4b` | 2026-10-25 22:16:40 -0500 | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 5632 | `7863e11bb224e0b46257fa897c69f2ce4b1e121b7bb3faddfff618742766be15` | `7863e11bb224e0b46257fa897c69f2ce4b1e121b7bb3faddfff618742766be15` | sí |

### `v2_reentrenamiento/experimentos_backtesting_rodante/01_configuracion/manifest.json`

| commit | fecha (autor, %ad) | fecha (commit, %cd) | mensaje | bytes | SHA-256 (bytes) | SHA-256 (CRLF→LF) | igual al publicado |
|---|---|---|---|---|---|---|---|
| `09b0945ad6647c908b27fd3cab3b086ac35868ab` | 2026-10-28 20:16:48 -0500 | 2026-10-28 20:16:48 -0500 | data(backtesting): salidas de la Fase C (488 unidades, predicciones congeladas antes de la Fase D) | 3824 | `7560755d15cf34c1d8a3f437af5a7efc18d0e99f12f9cd033b5842b5ab63598c` | `7560755d15cf34c1d8a3f437af5a7efc18d0e99f12f9cd033b5842b5ab63598c` | sí |
| `ddb8d4aefdcea4298152137a9fbc1154a3402828` | 2026-10-28 19:02:43 -0500 | 2026-10-28 19:02:43 -0500 | feat(backtesting): scripts reanudables de la Fase C, enmienda E-BR1, biblioteca lib y registro de desviaciones | 5171 | `5483a892e83c396bf80c59945b364cc3c56e686f837941586f4bbace29f7af78` | `5483a892e83c396bf80c59945b364cc3c56e686f837941586f4bbace29f7af78` | no |
| `db321084230df8c313f8eebf56922e79212d71e9` | 2026-10-25 22:22:33 -0500 | 2026-10-25 22:22:33 -0500 | docs(backtesting): preregistro final copiado a DECISIONES_METODOLOGICAS antes de la Fase C | 1524 | `2976e6f32d8ad7ec917bd255de4e3a058ae614d80438c8210b2b735f62a5e8b0` | `2976e6f32d8ad7ec917bd255de4e3a058ae614d80438c8210b2b735f62a5e8b0` | no |
| `344134b0418718529c678473cddb1b6fff8cab4b` | 2026-10-25 22:16:40 -0500 | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 1524 | `120a99695b0f07269505d5d5739554a406c888a7756128db080f708738185f33` | `120a99695b0f07269505d5d5739554a406c888a7756128db080f708738185f33` | no |

### `v2_reentrenamiento/experimentos_backtesting_rodante/01_configuracion/hashes_congelados.json`

| commit | fecha (autor, %ad) | fecha (commit, %cd) | mensaje | bytes | SHA-256 (bytes) | SHA-256 (CRLF→LF) | igual al publicado |
|---|---|---|---|---|---|---|---|
| `ddb8d4aefdcea4298152137a9fbc1154a3402828` | 2026-10-28 19:02:43 -0500 | 2026-10-28 19:02:43 -0500 | feat(backtesting): scripts reanudables de la Fase C, enmienda E-BR1, biblioteca lib y registro de desviaciones | 13095 | `4678041b70a40caee3ffc33d28fbfb7af4d77dbf0927efef03d15a2a9ff5daee` | `4678041b70a40caee3ffc33d28fbfb7af4d77dbf0927efef03d15a2a9ff5daee` | sí |
| `344134b0418718529c678473cddb1b6fff8cab4b` | 2026-10-25 22:16:40 -0500 | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 12459 | `c96bb3ef40d28410c0f64ff131000b01cd3bcc9965d89728a65796c34df2bde0` | `c96bb3ef40d28410c0f64ff131000b01cd3bcc9965d89728a65796c34df2bde0` | no |

### `v2_reentrenamiento/experimentos_backtesting_rodante/01_configuracion/rutas_datos.json`

| commit | fecha (autor, %ad) | fecha (commit, %cd) | mensaje | bytes | SHA-256 (bytes) | SHA-256 (CRLF→LF) | igual al publicado |
|---|---|---|---|---|---|---|---|
| `344134b0418718529c678473cddb1b6fff8cab4b` | 2026-10-25 22:16:40 -0500 | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 1788 | `f1c95c40045267770464af506d063cc761431ecf22c9421fe06f86c9e0e68708` | `f1c95c40045267770464af506d063cc761431ecf22c9421fe06f86c9e0e68708` | sí |

### `v2_reentrenamiento/experimentos_backtesting_rodante/01_configuracion/estilo_figuras.json`

| commit | fecha (autor, %ad) | fecha (commit, %cd) | mensaje | bytes | SHA-256 (bytes) | SHA-256 (CRLF→LF) | igual al publicado |
|---|---|---|---|---|---|---|---|
| `344134b0418718529c678473cddb1b6fff8cab4b` | 2026-10-25 22:16:40 -0500 | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 784 | `0bf83c32eeaae563e173c0ff582837db34db2cd9f86d3f1cbf9f7d1c8fcab724` | `0bf83c32eeaae563e173c0ff582837db34db2cd9f86d3f1cbf9f7d1c8fcab724` | sí |

### `v2_reentrenamiento/DECISIONES_METODOLOGICAS.md`

| commit | fecha (autor, %ad) | fecha (commit, %cd) | mensaje | bytes | SHA-256 (bytes) | SHA-256 (CRLF→LF) | igual al publicado |
|---|---|---|---|---|---|---|---|
| `ddb8d4aefdcea4298152137a9fbc1154a3402828` | 2026-10-28 19:02:43 -0500 | 2026-10-28 19:02:43 -0500 | feat(backtesting): scripts reanudables de la Fase C, enmienda E-BR1, biblioteca lib y registro de desviaciones | 81637 | `702dbac91867e60a0f68697babc2ded937fec1bc088578579dbc33e8b09bfb0d` | `702dbac91867e60a0f68697babc2ded937fec1bc088578579dbc33e8b09bfb0d` | sí |
| `db321084230df8c313f8eebf56922e79212d71e9` | 2026-10-25 22:22:33 -0500 | 2026-10-25 22:22:33 -0500 | docs(backtesting): preregistro final copiado a DECISIONES_METODOLOGICAS antes de la Fase C | 80642 | `6241379cfcc442c959b6cc1164151bb51aed6621e8bd80637e190c9fd7d8d5fe` | `6241379cfcc442c959b6cc1164151bb51aed6621e8bd80637e190c9fd7d8d5fe` | no |
| `27934652756c79b47a7219ee7eaaa01b22dc0866` | 2026-09-13 17:20:27 -0500 | 2026-09-13 17:20:27 -0500 | feat: cerrar experimento v2, resultados finales y SHAP | 69177 | `dd60ae0ec1e09fedf7e202e015c3032fab62f3906cfaede86e69859b8e41e7fa` | `dd60ae0ec1e09fedf7e202e015c3032fab62f3906cfaede86e69859b8e41e7fa` | no |
| `6a7c6ddd128888408c7709d65371b7b6fc1c0605` | 2026-09-10 23:15:03 -0500 | 2026-09-10 23:15:03 -0500 | feat: cerrar pipeline v2 GC3-GE y auditorias metodologicas | 54202 | `6b3babcd47bc19d481e3764fe51b36560e7f19957ca1d7e5c400ecb35b6ab812` | `6b3babcd47bc19d481e3764fe51b36560e7f19957ca1d7e5c400ecb35b6ab812` | no |
| `bfd19a7c9de7fd5f1acbc8144429169dc3c4000e` | 2026-09-04 08:17:01 -0500 | 2026-09-04 08:17:01 -0500 | fix(gc1): Corregir bug de horizonte SARIMA y establecer SARIMA-Sutil representativo. Bug critico: forecast(steps=12) duplicado hacia el mismo punto causaba que test replicara val. Corregido a forecast(steps=24) con split correcto (val=1-12, test=13-24). Prophet no tenia el bug (verificado identidad byte a byte). exp_002 (SARIMA-Sutil por AIC) sobreajusta y generaliza mal (R2 test=-1.11). Se establece exp_002b (seleccion manual por parsimonia) como modelo representativo en la comparativa oficial (R2 test=0.755, supera al Naive en -22.7%% MAE). Agregado t_index (tendencia lineal) a datasets de features, preparando GC2/GE/GM para capturar la tendencia secular real (~+4%% anual) detectada en la serie de Sutil (Ciclon Yaku 2023 + crecimiento de area/rendimiento, verificado con descomposicion CAGR area+2.22%% x rendimiento+1.75%%=produccion+4.01%%). Documentada limitacion de Delta_s con n_shock=3: la mejora de -79%% en shocks depende en un tercio de un solo mes con error casi cero, no es evidencia robusta de resiliencia. Decision de lags one-step-ahead reescrita sin justificacion operativa no verificada; declarada como limitacion pendiente de validar antes de despliegue. | 27781 | `fbe10755cdc9f5411535c78656cfa970b7e59a17bd3a28419b9c094756179670` | `fbe10755cdc9f5411535c78656cfa970b7e59a17bd3a28419b9c094756179670` | no |
| `ee5f9be56206b9e8618f7480b7be8e6af3f747ea` | 2026-09-03 20:53:07 -0500 | 2026-09-03 20:53:07 -0500 | feat(v2): Fases 1-3 completas - recoleccion, features, modelado inicial. Fase 1: MIDAGRI, NASA POWER, INDECI, scraping+NLP (2016-2025). Fase 2: fusion de 5 fuentes, codificacion ciclica, lags, escalado. Fase 3: baseline Naive + GC1 (SARIMA + Prophet). DECISIONES_METODOLOGICAS.md con trazabilidad completa. Excel MIDAGRI excluido via .gitignore (218MB, supera limite GitHub) | 15716 | `8c61b02ad71cacf6af1af93f145a5bf21d7fe0d0caf508a8d9d128ef41ceafe7` | `8c61b02ad71cacf6af1af93f145a5bf21d7fe0d0caf508a8d9d128ef41ceafe7` | no |

### `v2_reentrenamiento/experimentos_backtesting_rodante/09_reportes/DESVIACIONES.md`

| commit | fecha (autor, %ad) | fecha (commit, %cd) | mensaje | bytes | SHA-256 (bytes) | SHA-256 (CRLF→LF) | igual al publicado |
|---|---|---|---|---|---|---|---|
| `623cb3416d332f5b88814b77ec7cdee5a862f3e7` | 2026-10-31 08:59:02 -0500 | 2026-10-31 08:59:02 -0500 | v2: paquete Overleaf corregido, figuras D3 y workflow, scripts 11-13 para MDPI Forecasting | 34473 | `d7e55bdbc3e20cc9808663874cc72093708eccd84fdec34ac86ba91f48499fe6` | `d7e55bdbc3e20cc9808663874cc72093708eccd84fdec34ac86ba91f48499fe6` | no |
| `5567ba28c850e6c62855c794078c580ac16cb102` | 2026-10-28 21:57:20 -0500 | 2026-10-28 21:57:20 -0500 | data(backtesting): figuras de la Fase D2 (sensibilidad al umbral, comparacion de modelos, diagnostico y ablacion) | 14333 | `e5f7a27a0bbdde48691c5928fffafcd27d33190e449231a3b3aa12e6a114dc3b` | `e5f7a27a0bbdde48691c5928fffafcd27d33190e449231a3b3aa12e6a114dc3b` | no |
| `caa3d1138f9eece1ee19a72d1e994dedd2d5ab1c` | 2026-10-28 20:47:45 -0500 | 2026-10-28 20:47:45 -0500 | data(backtesting): resultados de la Fase D1 (metricas, bootstrap, DM con Holm, barrido de umbrales) | 11652 | `c0522cecdddedfab122a4dd28c8cd40388fb2ef83247e772097cab9499b89008` | `c0522cecdddedfab122a4dd28c8cd40388fb2ef83247e772097cab9499b89008` | no |
| `ddb8d4aefdcea4298152137a9fbc1154a3402828` | 2026-10-28 19:02:43 -0500 | 2026-10-28 19:02:43 -0500 | feat(backtesting): scripts reanudables de la Fase C, enmienda E-BR1, biblioteca lib y registro de desviaciones | 6083 | `51c1aa641a7220eababeb0bcb38fba48dbfdf04094c25136aacb263dea57b09b` | `51c1aa641a7220eababeb0bcb38fba48dbfdf04094c25136aacb263dea57b09b` | no |

### `v2_reentrenamiento/experimentos_backtesting_rodante/09_reportes/reporte_fase_A.md`

| commit | fecha (autor, %ad) | fecha (commit, %cd) | mensaje | bytes | SHA-256 (bytes) | SHA-256 (CRLF→LF) | igual al publicado |
|---|---|---|---|---|---|---|---|
| `344134b0418718529c678473cddb1b6fff8cab4b` | 2026-10-25 22:16:40 -0500 | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 5828 | `3bb7b2847df4402f1ad152d9ecd495e07e85b550b29b581b4a1212d81a112d7b` | `3bb7b2847df4402f1ad152d9ecd495e07e85b550b29b581b4a1212d81a112d7b` | sí |

### `v2_reentrenamiento/experimentos_backtesting_rodante/09_reportes/reporte_fase_B.md`

| commit | fecha (autor, %ad) | fecha (commit, %cd) | mensaje | bytes | SHA-256 (bytes) | SHA-256 (CRLF→LF) | igual al publicado |
|---|---|---|---|---|---|---|---|
| `344134b0418718529c678473cddb1b6fff8cab4b` | 2026-10-25 22:16:40 -0500 | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 13380 | `7ba954ac799022b4dbc98f504db8c417d9847955e7ad7a3d3a315873975fd9cd` | `7ba954ac799022b4dbc98f504db8c417d9847955e7ad7a3d3a315873975fd9cd` | sí |

### `v2_reentrenamiento/experimentos_backtesting_rodante/09_reportes/nota_v5_v3.md`

| commit | fecha (autor, %ad) | fecha (commit, %cd) | mensaje | bytes | SHA-256 (bytes) | SHA-256 (CRLF→LF) | igual al publicado |
|---|---|---|---|---|---|---|---|
| `db321084230df8c313f8eebf56922e79212d71e9` | 2026-10-25 22:22:33 -0500 | 2026-10-25 22:22:33 -0500 | docs(backtesting): preregistro final copiado a DECISIONES_METODOLOGICAS antes de la Fase C | 7276 | `a7915560d872af72900ec2b529179d735c7f868f2e807f08aba806bdb2d4fd0f` | `a7915560d872af72900ec2b529179d735c7f868f2e807f08aba806bdb2d4fd0f` | sí |
| `344134b0418718529c678473cddb1b6fff8cab4b` | 2026-10-25 22:16:40 -0500 | 2026-10-25 22:16:40 -0500 | docs(backtesting): preregistro D-BR1 a D-BR10 antes de la Fase C | 6137 | `3557bd3d806fa43536bab51fce69529e1ffca5341d63635a0f641b7e182ea7c6` | `3557bd3d806fa43536bab51fce69529e1ffca5341d63635a0f641b7e182ea7c6` | no |
