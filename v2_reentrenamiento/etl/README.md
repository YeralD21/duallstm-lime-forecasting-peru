# ETL reproducible de los insumos congelados (revisión G7, observación 12)

Scripts que regeneran, desde los archivos crudos, los CSV de `v2_reentrenamiento/data/interim/` que el
backtesting usa como insumos congelados (D21 los declaraba "no reproducibles").

**El código original no existe.** Se buscó en todo el árbol (incluidos v1, `src/`, `sources/`, notebooks y
`scratch/`) y en el historial de git de todas las ramas locales y remotas (`git log --all -S` con los nombres de
los archivos de salida y de entrada). Solo hay consumidores de estos CSV. En v2 solo se versionó
`notebooks/fase1_recoleccion/09_resumen_fase1*.ipynb`; los notebooks 01–08 de la Fase 1 nunca entraron en git.
Por eso estos scripts se **escribieron de nuevo**. Las reglas salen de `DECISIONES_METODOLOGICAS.md`, y los
detalles que esa fuente no fija (orden, redondeo, formato) se ajustaron comparando con los CSV congelados.
Cada regla está documentada en el docstring de su script.

| Script | Entrada cruda | Salidas | Resultado frente al congelado |
|---|---|---|---|
| `01_sisagri_a_series.py` | `data/raw/midagri/sisagri_2015_2026.xlsx` (5 hojas) | `limon_{c}_distrito_crudo.csv`, `limon_{c}_distrito_dedup.csv`, `limon_{c}_provincia.csv`, `limon_{c}_nacional_mensual.csv` (c = sutil, dulce) | SHA-256 idéntico en los 8 archivos (ver informe de la Fase 5) |
| `02_indeci_a_panel.py` | `data/raw/indeci/oficial_2016_2018/BD_2003-2025_EMERGENCIAS.csv` | `indeci_limpio_2016_2025.csv` | SHA-256 idéntico; igual al de `hashes_congelados.json` |
| `03_coordenadas.py` | v1 `data/interim/nasa/clima_dataset_final.csv` + `COORDS_DEPTO` de v1 `notebooks/fase2/_build_act02_time.py` | `coordenadas_provincias_completo.csv` + `validacion_coordenadas_adm2.csv` | SHA-256 idéntico (no figura en `hashes_congelados.json`) |

## Uso

```powershell
venv\Scripts\python.exe v2_reentrenamiento\etl\01_sisagri_a_series.py   # ~9 min (lee el Excel de 229 MB)
venv\Scripts\python.exe v2_reentrenamiento\etl\02_indeci_a_panel.py
venv\Scripts\python.exe v2_reentrenamiento\etl\03_coordenadas.py        # descarga el GeoJSON ADM2 (4.3 MB) si no se da --adm2
```

- **Salida:** `--salida CARPETA` (por defecto `%TEMP%\etl_v2_salida`). `_comun.carpeta_salida` **se niega a
  escribir dentro de `data/interim/`**.
- **Comparación automática:** cada script compara su salida con el CSV congelado de `data/interim/`. La
  comparación es fila a fila y celda a celda como texto, con **tolerancia 0**. El SHA-256 se calcula con el
  método 2 de `hashes_congelados.json` (CRLF → LF) y se compara con el archivo en disco y con el valor
  registrado en `hashes_congelados.json` cuando existe. El resultado se escribe en
  `comparacion_0X_*.json`, en la carpeta de salida.
- **Fuentes:** el link, la ruta esperada, el tamaño y el SHA-256 de cada archivo crudo están en
  `data_sources.json` (raíz del repositorio). Si falta el crudo, el script termina con un mensaje que indica el
  link y la ruta. Si el SHA-256 no coincide, advierte que no es el archivo usado en el artículo y sigue;
  `--estricto` lo detiene.
- `01` guarda las filas de limón del Excel en `_sisagri_limon_filas.csv` (caché). Si la caché existe, se
  reutiliza; `--cache-limon` indica otra ruta.

## Reglas reconstruidas

### 01 — SISAGRI
1. **Lectura:** las 5 hojas del Excel (`Exportar Hoja de Trabajo` 2015–2018, `Sheet1` 2018–2020, `Sheet2`
   2020–2023, `Sheet3` 2023–2025, `Sheet4` 2025–2026). 4 de las 5 hojas declaran la dimensión `A1:A1`; sin
   `reset_dimensions()`, openpyxl en modo `read_only` solo lee 1 fila de esas hojas.
2. **distrito_crudo:** `PRODUCTO` ∈ {LIMON SUTIL, LIMON DULCE}, años 2016–2025, sin otro filtro. Orden
   estable por AÑO, MES, COD_UBIGEO. Se conservan las celdas vacías: PRODUCCION vacía en 117 filas (sutil) y
   52 (dulce).
3. **distrito_dedup:** las claves AÑO+MES+COD_UBIGEO+COD_PRODUCTO duplicadas (1,061 claves, todas de Ayacucho,
   todas de sutil) se reducen a una fila con la **media** de cada variable numérica (DECISIONES, "Deduplicación
   Ayacucho"). Formato de las filas agregadas: 2 decimales; SIEMBRA y COSECHA se escriben `0.0` cuando todo el
   grupo es 0. Esta regla de formato es empírica: se fijó para reproducir el congelado.
4. **provincia:** SUMA de PRODUCCION y VERDE_ACTUAL. El precio es la media ponderada por producción
   (DECISIONES). Si la producción provincial es 0: precio 0 y `precio_es_fallback = 1`. Formato: `%.3f` y `%.6f`.
   El cálculo se hace sobre el CSV dedup tal como se escribió.
5. **nacional:** SUMA de produccion_t. El precio es la media ponderada por produccion_t, calculada sobre el
   CSV provincial ya redondeado. `n_provincias_reportando` = provincias con produccion_t > 0.

### 02 — INDECI
Años 2016–2025. Solo entran los 10 peligros climáticos de DECISIONES. Normalización de Lima:
LIMA METROPOLITANA y LIMA PROVINCIAS → LIMA en departamento, y LIMA METROPOLITANA → LIMA en provincia.
Agregación por provincia y mes:
- `num_emergencias` = número de registros;
- suma de AFECTADOS, DAMNIFICADOS y de las hectáreas destruidas y afectadas (hectáreas redondeadas a 2
  decimales);
- `total_afectados` = afectadas + damnificadas.

**Meses sin registro:** el panel cubre las 107 provincias de sutil × 120 meses. Los 5,609 provincia-mes sin
ningún registro climático se codifican como **0**, no como faltante. CARHUAZ y YUNGAY (Áncash), que solo
tienen limón dulce, no están en el panel congelado. El script respeta el congelado y lo informa.

### 03 — Coordenadas
- **99 provincias "exactas":** se copian como texto de la tabla climática de v1. Esas coordenadas **no
  tienen origen documentado** en el repositorio.
- **10 de "fallback":** se toman de `COORDS_DEPTO` de v1, que el código llama "centroide aproximado". En
  realidad son las coordenadas de la **capital del departamento** (Lima ciudad, Iquitos, Huaraz, Trujillo,
  Chiclayo, Piura, Ica, Huánuco), no un centroide.
- **Validación con fuente documentada:** geoBoundaries gbOpen PER ADM2, fijado en el commit `90a1d52` (IGN
  Perú vía OCHA ROLAC/HDX, CC BY 3.0 IGO, `PER-ADM2-86281439`, 196 provincias, SHA-256 verificado). Prueba de
  punto en polígono:
  - las 99 coordenadas exactas caen dentro de su provincia;
  - de las 10 de fallback, 2 caen dentro (LIMA y CHICLAYO, que son provincias capitales) y 8 caen en la
    provincia capital del departamento, a entre 13 y 310 km del polígono propio. El detalle está en
    `validacion_coordenadas_adm2.csv`.

## Limitaciones

- Las reglas 01.3 (formato) y 01.4/01.5 (orden de cálculo y redondeo) se dedujeron del resultado. Son
  suficientes para reproducir los bytes, pero no prueban que el código original fuera igual.
- La fecha de descarga del Excel SISAGRI y la del CSV de INDECI no están documentadas. Fechas de modificación
  en disco: Excel, 2026-08-29; INDECI, 2026-09-11 (fecha del clon). DECISIONES dice que el CSV de INDECI
  estaba "actualizado 2026-08-26".
- El origen primario de las 99 coordenadas de v1 sigue sin documentar. Solo se valida que sean coherentes
  con los límites provinciales del IGN.
