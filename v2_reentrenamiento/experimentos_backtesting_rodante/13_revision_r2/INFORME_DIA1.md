# Revisión G7, ronda 2 — Día 1: análisis rápidos

Manuscrito del 13-nov-2026. **Todo lo de este informe es posterior al protocolo**. Se reporta como robustez o
diagnóstico, con la lógica de la Sec. 2.7 y de E1–E4, y **no modifica el ranking principal** de 10 modelos. Las cifras
salen de `13_revision_r2/resultados/` (CSV y JSON generados por los scripts de `13_revision_r2/scripts/`). Las
tablas de T1 y T2 se copian sin editar de `resultados/tablas_T1_T2.md`. Método y diferencias inevitables:
[`README.md`](README.md).

**Controles.** Para los 10 modelos originales, las métricas y el ranking recalculados coinciden con lo publicado:
440 celdas de `T06_agregadas_IC.csv` y 160 filas de `T08_ranking_empates.csv` (posición y primero/empate). El script
se detiene si no coinciden, así que ETS y Theta se evalúan con el procedimiento exacto del artículo.

---

## 1. Tablas de T1 y T2

### Especificaciones elegidas (T1)

- **ETS** (mínimo AICc en train; las 12 especificaciones se ajustaron sin error en las 10 unidades; el modelo elegido
  converge siempre):
  - sutil: ETS(A,N,M) en las 5 ventanas;
  - dulce: ETS(M,N,A) en 2021–2024 y ETS(A,N,A) en 2025.
  - En dulce hay 1 especificación no convergente (no elegida) en 2021, 2023, 2024 y 2025 (`rejilla_ets.csv`).
- **Theta** (θ = 2): en sutil, α ≈ 1 en todas las ventanas (0.9997–0.9999), es decir, prácticamente un paseo aleatorio
  con deriva sobre la serie desestacionalizada; en dulce, α entre 0.486 y 0.733. Desestacionalización multiplicativa
  en 9 de 10 unidades. En **sutil 2021** el test de estacionalidad de statsmodels (solo con el train 2016-07..2019-12,
  42 meses) no rechaza; esa unidad no se desestacionaliza (comportamiento por defecto, no se forzó).

### T1.a Precisión agregada 2021–2025 (formato Tabla 3, 12 modelos)

MAE en toneladas con IC 95 % bootstrap pareado (meses remuestreados dentro de cada ventana, B = 10 000, semilla 42). Δs = (MAE_shock − MAE)/MAE × 100. MASE_shock con los denominadores por ventana del artículo (03_ventanas/denominador_mase_por_ventana.csv). † = añadido posterior al protocolo (revisión R2); no altera el ranking principal. * = primero o empatado con el primero (IC 95 % bootstrap pareado de la diferencia con el mejor contiene 0).


#### sutil (60 meses; shock MoM P75: 10; shock YoY P75: 10)

| modelo | MAE todos (IC95) | MAE normal MoM (IC95) | MAE shock MoM P75 (IC95) | Δs MoM % | MASE_shock MoM | MAE shock YoY P75 (IC95) | MAE normal YoY | MASE_shock YoY |
|---|---|---|---|---|---|---|---|---|
| Naive | 3,624 (2,920–4,382) | 2,648 (2,102–3,226) | 8,506 (7,724–9,215) | 134.7 | 1.45 | 3,172 (1,674–4,944) | 3,715 | 0.57 |
| Seasonal Naive | 6,075 (5,156–6,987) | 6,283 (5,323–7,211) | 5,034 (2,259–7,928) | -17.1 | 0.86 | 12,508 (10,423–14,593) | 4,788 | 2.26 |
| Chronos | 2,649 (2,171–3,144) | 2,222 (1,786–2,701) | 4,784 (3,963–5,641) | 80.6 | 0.82 | 1,864 (1,420–2,317) | 2,805 | 0.33 |
| SARIMA | 3,361 (2,780–3,970) | 3,007 (2,443–3,589) | 5,131 (3,759–6,624) | 52.7 | 0.88 | 3,233 (2,430–3,968) | 3,386 | 0.58 |
| SARIMA-sel | 3,206 (2,563–3,880) | 2,860 (2,272–3,469) | 4,936 (2,866–7,242) | 54.0 | 0.84 | 4,079 (2,145–6,099) | 3,031 | 0.73 |
| Ridge | 4,925 (3,838–6,074) | 4,199 (3,099–5,331) | 8,557 (5,484–12,360) | 73.7 | 1.47 | 4,946 (3,290–6,789) | 4,921 | 0.88 |
| ElasticNet | 4,872 (3,847–5,950) | 4,216 (3,172–5,298) | 8,154 (5,162–11,484) | 67.4 | 1.40 | 5,404 (3,428–7,594) | 4,766 | 0.97 |
| XGB-37 | 4,881 (4,063–5,732) | 4,667 (3,831–5,544) | 5,955 (3,727–7,965) | 22.0 | 1.02 | 4,816 (2,548–7,254) | 4,894 | 0.87 |
| GC3 | 6,361 (5,292–7,446) | 6,419 (5,215–7,644) | 6,074 (4,085–8,216) | -4.5 | 1.04 | 9,166 (5,192–13,365) | 5,800 | 1.65 |
| GE | 6,744 (5,587–7,894) | 6,727 (5,454–8,024) | 6,827 (4,477–9,213) | 1.2 | 1.17 | 9,796 (6,025–13,767) | 6,133 | 1.77 |
| ETS † | 2,939 (2,464–3,444) | 2,573 (2,090–3,078) | 4,766 (3,673–5,762) | 62.2 | 0.82 | 2,396 (1,969–2,902) | 3,047 | 0.43 |
| Theta † | 3,022 (2,509–3,541) | 2,673 (2,160–3,236) | 4,767 (3,504–5,635) | 57.7 | 0.81 | 2,521 (1,757–3,242) | 3,122 | 0.45 |

#### dulce (60 meses; shock MoM P75: 15; shock YoY P75: 16)

| modelo | MAE todos (IC95) | MAE normal MoM (IC95) | MAE shock MoM P75 (IC95) | Δs MoM % | MASE_shock MoM | MAE shock YoY P75 (IC95) | MAE normal YoY | MASE_shock YoY |
|---|---|---|---|---|---|---|---|---|
| Naive | 77.5 (65.7–89.9) | 59.5 (48.6–71.0) | 131.6 (116.5–147.7) | 69.8 | 5.00 | 83.2 (60.1–107.5) | 75.5 | 3.29 |
| Seasonal Naive | 24.5 (20.5–29.0) | 24.5 (19.3–30.2) | 24.5 (21.4–27.8) | -0.0 | 0.94 | 42.4 (33.0–55.0) | 18.0 | 1.67 |
| Chronos | 30.8 (25.6–36.4) | 25.0 (19.8–30.9) | 48.2 (40.5–56.1) | 56.4 | 1.87 | 33.2 (21.2–46.1) | 30.0 | 1.32 |
| SARIMA | 18.4 (14.5–22.8) | 19.9 (15.0–25.5) | 14.0 (9.8–18.0) | -24.1 | 0.54 | 27.4 (16.0–40.5) | 15.1 | 1.08 |
| SARIMA-sel | 20.6 (16.5–25.2) | 20.9 (15.8–26.9) | 19.7 (15.6–23.6) | -4.5 | 0.72 | 28.4 (17.3–41.2) | 17.8 | 1.11 |
| Ridge | 53.1 (43.4–63.4) | 47.5 (37.2–58.2) | 69.7 (52.0–89.3) | 31.3 | 2.71 | 66.4 (47.7–85.1) | 48.2 | 2.62 |
| ElasticNet | 50.2 (40.7–60.4) | 44.6 (34.4–55.0) | 67.2 (49.5–87.1) | 33.8 | 2.61 | 57.3 (38.2–77.1) | 47.7 | 2.26 |
| XGB-37 | 48.3 (39.8–57.2) | 42.4 (33.3–52.5) | 65.8 (51.6–80.6) | 36.4 | 2.53 | 42.3 (29.6–54.6) | 50.4 | 1.66 |
| GC3 | 56.7 (46.9–66.9) | 55.3 (44.1–67.2) | 60.7 (46.2–76.3) | 7.2 | 2.38 | 58.2 (43.0–74.4) | 56.1 | 2.32 |
| GE | 56.7 (47.5–66.7) | 56.4 (45.5–67.7) | 57.9 (41.8–75.2) | 2.0 | 2.25 | 56.1 (42.5–70.7) | 57.0 | 2.25 |
| ETS † | 22.3 (18.5–26.5) | 23.4 (18.5–28.8) | 19.0 (15.7–22.6) | -14.8 | 0.72 | 35.6 (27.4–45.4) | 17.5 | 1.39 |
| Theta † | 28.0 (22.7–33.3) | 31.3 (25.6–37.1) | 18.2 (9.7–27.7) | -35.1 | 0.66 | 27.7 (18.4–37.6) | 28.1 | 1.07 |


### T1.b Diebold–Mariano HLN (pérdida absoluta, h = 1) de ETS y Theta frente al mejor

| cultivo | modelo | referencia | tipo_referencia | alcance | n | d_media | HLN | p |
|---|---|---|---|---|---|---|---|---|
| sutil | ETS | Chronos | referencia_G7 | todos | 60 | 290.254 | 1.277 | 0.207 |
| sutil | ETS | Chronos | referencia_G7 | shock_MoM_P75 | 10 | -17.379 | -0.025 | 0.981 |
| sutil | ETS | Chronos | referencia_G7 | shock_YoY_P75 | 10 | 531.417 | 1.616 | 0.141 |
| sutil | Theta | Chronos | referencia_G7 | todos | 60 | 373.647 | 1.387 | 0.171 |
| sutil | Theta | Chronos | referencia_G7 | shock_MoM_P75 | 10 | -16.327 | -0.024 | 0.982 |
| sutil | Theta | Chronos | referencia_G7 | shock_YoY_P75 | 10 | 656.787 | 1.521 | 0.163 |
| dulce | ETS | SARIMA-sel | referencia_G7 | todos | 60 | 1.706 | 0.814 | 0.419 |
| dulce | ETS | SARIMA-sel | referencia_G7 | shock_MoM_P75 | 15 | -0.651 | -0.173 | 0.865 |
| dulce | ETS | SARIMA-sel | referencia_G7 | shock_YoY_P75 | 16 | 7.256 | 2.001 | 0.064 |
| dulce | Theta | SARIMA-sel | referencia_G7 | todos | 60 | 7.369 | 2.124 | 0.038 |
| dulce | Theta | SARIMA-sel | referencia_G7 | shock_MoM_P75 | 15 | -1.524 | -0.318 | 0.755 |
| dulce | Theta | SARIMA-sel | referencia_G7 | shock_YoY_P75 | 16 | -0.662 | -0.098 | 0.923 |
| dulce | ETS | SARIMA | menor_MAE_10_modelos | todos | 60 | 3.923 | 2.001 | 0.050 |
| dulce | ETS | SARIMA | menor_MAE_10_modelos | shock_MoM_P75 | 15 | 5.062 | 1.710 | 0.109 |
| dulce | ETS | SARIMA | menor_MAE_10_modelos | shock_YoY_P75 | 16 | 8.242 | 2.280 | 0.038 |
| dulce | Theta | SARIMA | menor_MAE_10_modelos | todos | 60 | 9.585 | 2.923 | 0.005 |
| dulce | Theta | SARIMA | menor_MAE_10_modelos | shock_MoM_P75 | 15 | 4.189 | 0.789 | 0.443 |
| dulce | Theta | SARIMA | menor_MAE_10_modelos | shock_YoY_P75 | 16 | 0.325 | 0.046 | 0.964 |


### T1.c Ranking por MAE en meses de shock, 12 modelos (formato Tabla 4)

† = añadido posterior al protocolo (revisión R2); no altera el ranking principal. * = primero o empatado con el primero (IC 95 % bootstrap pareado de la diferencia con el mejor contiene 0).


#### sutil

| modelo | MoM P50 | MoM P60 | MoM P75 | MoM P90 | 1º/empate MoM (de 4) | Robusto MoM | Robusto MoM (10 modelos, publicado) | 1º/empate YoY (de 4) | Robusto YoY | Robusto YoY (10 modelos, publicado) |
|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 7 | 10 | 11 | 9 | 0 | No | No | 4 | Sí | Sí |
| Seasonal Naive | 8 | 7 | 5* | 6* | 2 | No | No | 0 | No | No |
| Chronos | 2* | 4* | 3* | 1* | 4 | Sí | Sí | 4 | Sí | Sí |
| SARIMA | 4* | 3* | 6* | 4 | 3 | Sí | Sí | 1 | No | No |
| SARIMA-sel | 1* | 2* | 4* | 5 | 3 | Sí | Sí | 1 | No | No |
| Ridge | 11 | 12 | 12 | 12 | 0 | No | No | 0 | No | No |
| ElasticNet | 12 | 11 | 10 | 11 | 0 | No | No | 0 | No | No |
| XGB-37 | 6 | 6 | 7* | 8 | 1 | No | No | 1 | No | No |
| GC3 | 10 | 8 | 8* | 7 | 1 | No | No | 0 | No | No |
| GE | 9 | 9 | 9 | 10 | 0 | No | No | 0 | No | No |
| ETS † | 3* | 1* | 1* | 3* | 4 | Sí | — | 4 | Sí | — |
| Theta † | 5* | 5 | 2* | 2* | 3 | Sí | — | 4 | Sí | — |

#### dulce

| modelo | MoM P50 | MoM P60 | MoM P75 | MoM P90 | 1º/empate MoM (de 4) | Robusto MoM | Robusto MoM (10 modelos, publicado) | 1º/empate YoY (de 4) | Robusto YoY | Robusto YoY (10 modelos, publicado) |
|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 12 | 12 | 12 | 12 | 0 | No | No | 0 | No | No |
| Seasonal Naive | 4 | 4 | 5 | 3 | 0 | No | No | 0 | No | No |
| Chronos | 6 | 6 | 6 | 6 | 0 | No | No | 4 | Sí | Sí |
| SARIMA | 1* | 1* | 1* | 1* | 4 | Sí | Sí | 3 | Sí | Sí |
| SARIMA-sel | 2* | 2* | 4 | 5 | 2 | No | No | 3 | Sí | Sí |
| Ridge | 11 | 11 | 11 | 10 | 0 | No | No | 0 | No | No |
| ElasticNet | 10 | 10 | 10 | 9 | 0 | No | No | 0 | No | No |
| XGB-37 | 7 | 8 | 9 | 11 | 0 | No | No | 0 | No | No |
| GC3 | 9 | 9 | 8 | 7 | 0 | No | No | 0 | No | No |
| GE | 8 | 7 | 7 | 8 | 0 | No | No | 0 | No | No |
| ETS † | 3 | 3 | 3* | 2 | 1 | No | — | 0 | No | — |
| Theta † | 5 | 5 | 2* | 4 | 1 | No | — | 4 | Sí | — |


### T2 Ranking solo en 2025 (12 modelos)

† = añadido posterior al protocolo (revisión R2); no altera el ranking principal. * = primero o empatado con el primero (IC 95 % bootstrap pareado de la diferencia con el mejor contiene 0). IC con remuestreo de los meses de 2025 (un estrato).


#### sutil

| modelo | MAE todos (IC95) | pos. todos | MAE shock MoM P75 (IC95) | pos. shock MoM P75 | MAE shock YoY P75 (IC95) | pos. shock YoY P75 |
|---|---|---|---|---|---|---|
| Naive | 4,704 (2,472–7,198) | 9 | 11,660 (11,083–12,127) | 12 | — (—–—) | — |
| Seasonal Naive | 4,160 (2,746–5,719) | 8* | 4,130 (1,518–9,077) | 1* | — (—–—) | — |
| Chronos | 3,316 (2,095–4,593) | 3* | 6,487 (5,900–6,944) | 5* | — (—–—) | — |
| SARIMA | 3,985 (2,402–5,573) | 7* | 7,824 (7,097–8,367) | 9* | — (—–—) | — |
| SARIMA-sel | 3,947 (2,505–5,487) | 6* | 6,701 (4,090–9,379) | 6 | — (—–—) | — |
| Ridge | 3,232 (1,723–4,876) | 2* | 7,177 (5,411–8,266) | 7* | — (—–—) | — |
| ElasticNet | 3,223 (1,684–5,052) | 1* | 7,423 (4,649–10,182) | 8* | — (—–—) | — |
| XGB-37 | 5,902 (3,797–8,056) | 10* | 8,297 (500–12,385) | 11* | — (—–—) | — |
| GC3 | 7,746 (5,838–9,617) | 11 | 5,594 (1,662–7,644) | 2* | — (—–—) | — |
| GE | 9,426 (6,437–12,187) | 12 | 7,908 (1,773–12,366) | 10 | — (—–—) | — |
| ETS † | 3,536 (2,302–5,007) | 4* | 6,405 (2,749–9,351) | 4 | — (—–—) | — |
| Theta † | 3,725 (2,131–5,546) | 5* | 6,124 (1,721–8,976) | 3* | — (—–—) | — |

#### dulce

| modelo | MAE todos (IC95) | pos. todos | MAE shock MoM P75 (IC95) | pos. shock MoM P75 | MAE shock YoY P75 (IC95) | pos. shock YoY P75 |
|---|---|---|---|---|---|---|
| Naive | 84.7 (58.9–114.1) | 10 | 138.3 (94.3–183.8) | 12 | 93.6 (41.1–160.1) | 12 |
| Seasonal Naive | 30.5 (20.4–40.9) | 5 | 25.9 (15.5–32.2) | 5 | 46.3 (33.2–65.4) | 9 |
| Chronos | 34.6 (25.3–45.9) | 6* | 60.1 (44.8–81.6) | 6 | 25.3 (20.0–35.0) | 5 |
| SARIMA | 21.8 (10.9–36.0) | 4* | 11.6 (2.5–19.2) | 4 | 36.8 (8.0–86.4) | 8* |
| SARIMA-sel | 19.8 (9.3–34.7) | 3* | 11.0 (1.1–18.0) | 3* | 36.8 (6.2–89.2) | 7* |
| Ridge | 50.6 (26.7–78.6) | 8 | 90.9 (42.8–152.0) | 9 | 22.9 (1.2–46.0) | 4* |
| ElasticNet | 49.3 (25.9–76.2) | 7 | 90.7 (48.7–143.5) | 8 | 20.8 (1.2–44.8) | 3* |
| XGB-37 | 59.4 (32.3–88.1) | 9 | 90.1 (82.2–100.3) | 7 | 14.2 (8.0–20.6) | 2* |
| GC3 | 103.4 (65.3–142.9) | 12 | 118.9 (53.0–187.7) | 11 | 77.5 (57.0–106.6) | 11 |
| GE | 95.6 (59.6–133.4) | 11 | 99.9 (36.2–174.7) | 10 | 75.4 (55.3–104.7) | 10 |
| ETS † | 18.9 (10.7–30.2) | 1* | 10.4 (0.5–21.0) | 2* | 36.0 (16.1–69.5) | 6* |
| Theta † | 19.1 (10.8–28.1) | 2* | 5.4 (0.8–13.0) | 1* | 13.8 (3.9–24.9) | 1* |


#### Primer lugar: 2025 frente al pool 2021–2025

| cultivo | criterio | n_meses_2025 | 1º 2025 (12 mod.) | 1º pool (12 mod.) | 1º 2025 (10 mod.) | 1º pool (10 mod.) | mismo 1º (12) | mismo 1º (10) | empatados con el 1º en 2025 |
|---|---|---|---|---|---|---|---|---|---|
| sutil | todos | 12 | ElasticNet | Chronos | ElasticNet | Chronos | No | No | ElasticNet, Ridge, Chronos, ETS, Theta, SARIMA-sel, SARIMA, Seasonal Naive, XGB-37 |
| sutil | shock_MoM_P75 | 3 | Seasonal Naive | ETS | Seasonal Naive | Chronos | No | No | Seasonal Naive, GC3, Theta, Chronos, Ridge, ElasticNet, SARIMA, XGB-37 |
| sutil | shock_YoY_P75 | 0 | — (sin meses) | Chronos | — (sin meses) | Chronos | — | — | — |
| dulce | todos | 12 | ETS | SARIMA | SARIMA-sel | SARIMA | No | No | ETS, Theta, SARIMA-sel, SARIMA, Chronos |
| dulce | shock_MoM_P75 | 3 | Theta | SARIMA | SARIMA-sel | SARIMA | No | No | Theta, ETS, SARIMA-sel |
| dulce | shock_YoY_P75 | 3 | Theta | SARIMA | XGB-37 | SARIMA | No | No | Theta, XGB-37, ElasticNet, Ridge, ETS, SARIMA-sel, SARIMA |

### Lectura de T1

- **El ranking principal no cambia.** Con 12 modelos, cada uno de los 10 originales conserva su condición de
  "consistently top-ranked" (columna "Robusto … (10 modelos, publicado)" frente a "Robusto …"): en sutil, Chronos,
  SARIMA y SARIMA-sel (MoM) y Naive y Chronos (YoY); en dulce, SARIMA (MoM) y Chronos, SARIMA y SARIMA-sel (YoY).
- **Sutil:** ETS y Theta quedan cerca de Chronos y SARIMA en todos los meses (MAE 2,939 y 3,022 t, frente a 2,649 de
  Chronos) y entre los primeros en meses de shock. ETS tiene el menor MAE de shock MoM P75 (4,766 t), empatado con
  Chronos (4,784 t). Los dos cumplen la regla 3 de 4 en MoM (ETS 4/4, Theta 3/4) y en YoY (4/4). DM-HLN frente a
  Chronos: ninguna diferencia significativa (p ≥ 0.14).
- **Dulce:** SARIMA sigue primero en todos los meses y en shock MoM. ETS tiene MAE 22.3 t (todos) y 19.0 t (shock
  MoM); no es robusto (1/4 MoM, 0/4 YoY). Theta tiene MAE 28.0 t en todos los meses, pero es robusto en YoY (4/4).
  DM-HLN: Theta es peor que SARIMA-sel en todos los meses (p = 0.038). Frente a SARIMA (menor MAE de los 10 modelos):
  ETS es peor en todos los meses (p = 0.050) y en shock YoY (p = 0.038), y Theta en todos los meses (p = 0.005).
  En shock MoM no hay diferencias significativas.
- Como en G7, la referencia de DM es el mejor univariado (sutil: Chronos; dulce: SARIMA-sel). En dulce se añade
  SARIMA, que tiene el menor MAE; en sutil Chronos cumple las dos condiciones.

### Lectura de T2 (solo 2025)

- **El primer lugar en 2025 no coincide con el del pool 2021–2025 en ningún caso comparable**, ni con 12 ni con 10
  modelos:
  - **sutil, todos los meses:** ElasticNet en 2025, Chronos en el pool;
  - **sutil, shock MoM P75:** Seasonal Naive en 2025; en el pool, ETS con 12 modelos y Chronos con 10;
  - **dulce, todos los meses:** ETS con 12 modelos y SARIMA-sel con 10 en 2025; SARIMA en el pool;
  - **dulce, shock MoM y YoY P75:** Theta con 12 modelos en 2025 (SARIMA-sel y XGB-37 con 10); SARIMA en el pool.
- **Sutil 2025 no tiene meses de shock YoY P75** (0 meses), así que ese criterio no se puede evaluar.
- **2025 tiene solo 12 meses y 3 de shock.** Los IC son anchos y el empate con el primero es muy frecuente: en sutil,
  9 de 12 modelos empatan con el primero en todos los meses y 8 en shock MoM. Una sola ventana no permite distinguir
  entre la mayoría de los modelos; por eso el pool 2021–2025 es el análisis principal.

---

## 2. Respuestas de T3 y T4

### T3.1 La constante (`trend='c'`) del SARIMA fijo de sutil (1,1,1)(1,1,0)12

**Cómo la implementa statsmodels.** En `SARIMAX`, la constante entra en la ecuación de la serie **diferenciada**, no
en la de niveles (`statsmodels/tsa/statespace/sarimax.py`, Notes de la clase, líneas 210–213, statsmodels 0.14.6):

> φ_p(L) φ̃_P(L^s) Δ^d Δ_s^D y_t = A(t) + θ_q(L) θ̃_Q(L^s) ζ_t

Con `trend='c'`, A(t) = c. Es la ordenada del estado del componente estacionario, después de las diferencias:
"SARIMA trend enters through the a time-varying state intercept, associated with the first row of the stationary
component of the state vector (i.e. the first element of the state vector following any differencing elements)"
(líneas 1651–1654). La otra clase de statsmodels, `ARIMA` (`tsa/arima/model.py`, líneas 168–180), pone la tendencia
en niveles y por eso **rechaza** una constante con d + D > 0: "a constant cannot be included in an ARIMA(1, 1, 1)
model, but including a linear trend, which would have the same effect as fitting a constant to the differenced data,
is allowed".

**Implicación.** Con d = 1 y D = 1, w_t = (1−L)(1−L¹²) y_t sigue un ARMA con media
μ = c / ((1−φ₁)(1−Φ₁)). Como (1−L)(1−L¹²) t² = 24 (comprobado numéricamente: `T3_resumen.json`, `DD12_de_t2` = 24.0),
una media μ ≠ 0 en w_t equivale a una **tendencia determinista cuadrática en niveles**, μ/24 · t², más términos
lineales y estacionales fijados por las condiciones iniciales. Dicho de otro modo: la variación interanual tiene una
tendencia lineal. **Sí implica una tendencia determinista en niveles, y es cuadrática, no lineal.**

**Cifras** (`T3_1_constante_parametros.csv`; ajuste en el train de cada ventana, todos convergen):

| ventana | c | φ₁ | Φ₁ | μ implícita de w_t | media empírica de w_t en train | μ/24 (t/mes²) | efecto de c en el pronóstico a 12 meses (t) |
|---|---|---|---|---|---|---|---|
| 2021 | 518.3 | 0.111 | -0.422 | 410.1 | 440.2 (n = 29) | 17.09 | 6,856 |
| 2022 | 543.0 | 0.035 | -0.416 | 397.6 | 451.7 (n = 41) | 16.56 | 6,627 |
| 2023 | 52.0 | 0.005 | -0.433 | 36.5 | 179.9 (n = 53) | 1.52 | 617 |
| 2024 | 244.1 | -0.063 | -0.448 | 158.6 | 177.1 (n = 65) | 6.61 | 2,723 |
| 2025 | 208.0 | -0.055 | -0.473 | 133.8 | 146.8 (n = 77) | 5.58 | 2,340 |

Comprobación con el modelo ajustado: con los mismos parámetros e intercepto 0, la diferencia entre los pronósticos
con y sin constante cumple (1−L)(1−L¹²)·dif → μ (media en h = 200–240: 410.093 frente a μ = 410.093 en 2021; igual
en todas las ventanas). A 240 pasos la diferencia llega a ≈ 10⁵–10⁶ t. Esto confirma el crecimiento cuadrático.
En el pronóstico a 1 paso, la constante pesa poco: ver T3.2.

### T3.2 Sensibilidad: SARIMA fijo de sutil sin constante

Mismo orden, mismas opciones salvo `trend='n'`, mismo protocolo rolling (ajuste único en train, validación como
estado, test a 1 paso). Como control, el SARIMA con constante, recalculado aquí, reproduce las predicciones
congeladas (diferencia máxima 1.5·10⁻¹¹ t). Todos los ajustes convergen.

| alcance (pool 2021–2025, sutil) | n meses | MAE original (con c) | MAE sin c | diferencia (sin − con) | IC 95 % de la diferencia |
|---|---|---|---|---|---|
| todos | 60 | 3,361 | 3,293 | -68 | [-143; 9] |
| shock_MoM_P75 | 10 | 5,131 | 5,217 | 87 | [-112; 232] |
| shock_YoY_P75 | 10 | 3,233 | 3,228 | -5 | [-115; 106] |

Por ventana (MAE, con c → sin c): 2021: 3,208 → 3,033; 2022: 3,061 → 2,927; 2023: 3,693 → 3,696; 2024: 2,858 → 2,822; 2025: 3,985 → 3,984.
**Conclusión:** quitar la constante no cambia el MAE de forma significativa: los tres IC contienen 0. Baja un poco
en todos los meses (−68 t) y sube en shock MoM (+87 t).

### T3.3 Regla de respaldo cuando SARIMA-sel no converge

**Regla propuesta** (`T3_resumen.json`): si el ajuste final del orden elegido no converge
(`mle_retvals['converged']` = False), se usa el siguiente orden en el orden de AIC entre los 5 preseleccionados
(posiciones k+1, …, 5 y, si ninguno converge, k−1, …, 1, con k la posición del elegido) que sí converja, con las
mismas opciones y datos. Si ninguno converge, se conserva el elegido y se marca.

**Dónde aplica** (`T3_3_regla_respaldo_convergencia.csv`):
- en el protocolo original, los 10 SARIMA-sel convergen, así que la regla no cambia nada publicado;
- en E1 (SARIMA-sel-Y1), solo **sutil 2021** no converge: orden elegido AIC#3 = (2,1,0)(2,1,1)12.

**Aplicación a sutil 2021** (E1):
- AIC#4 (1,1,0)(2,1,1)12: no converge;
- AIC#5 (0,1,0)(2,1,1)12: no converge;
- AIC#2 (0,1,0)(1,1,0)12: **converge** y es el orden de respaldo.

Como control, el reajuste del orden no convergente reproduce la unidad publicada de `12_revision_g7`.

| SARIMA-sel-Y1, sutil | publicado (G7, sin regla) | con la regla | lectura alternativa B |
|---|---|---|---|
| MAE 2021 (12 meses) | 73,706 | 3,023 | 19,503 |
| MAE pool 2021–2025, todos los meses (60) | 17,463 | 3,327 | 6,623 |
| MAE pool, shock MoM P75 (10) | 4,994 | 4,994 | 4,994 |
| MAE pool, shock YoY P75 (10) | 4,167 | 4,167 | 4,167 |

- **Lectura alternativa B** (sensibilidad): primer orden que converge desde AIC#1, excluido el elegido. Es AIC#1,
  (3,1,2)(2,1,1)12.
- **Meses de shock:** sutil 2021 no tiene meses de shock P75, ni MoM ni YoY (`03_ventanas`). Por eso los MAE de shock
  del pool no cambian con ninguna regla.
- **Dulce:** no cambia (todas las unidades convergen).
- **Conclusión:** la regla elimina la divergencia de sutil 2021: el MAE 2021 baja de 73,706 a 3,023 t, y el MAE de
  todos los meses del pool, de 17,463 a 3,327 t. El resultado depende de cómo se lea "siguiente". Con la lectura B
  la ventana queda en 19,503 t, porque AIC#1 converge pero pronostica mal. Conviene fijar la redacción exacta de la
  regla en el texto.

### T4.1 Predictores (índices respecto del mes objetivo T)

**Ridge, ElasticNet y XGB-37** usan los mismos 37 predictores (`gc2_predictors`; Ridge/EN en `05_lineales.py`,
XGB-37 en `06_xgb.py`). Cada par es X_t → y_{t+1}: la fila del mes T−1 predice y_T. Cada rezago se comprobó con los
datos en los 12 meses de test de 2025 (`T4_1_predictores_tabulares.csv`):

| n | predictor | valor usado |
|---|---|---|
| 1 | `produccion_t_{c}` | y(T-1) |
| 2 | `produccion_t_{c}_lag1` | y(T-2) |
| 3 | `produccion_t_{c}_lag3` | y(T-4) |
| 4 | `produccion_t_{c}_lag6` | y(T-7) |
| 5 | `mes_sin` | mes_sin(T-1) |
| 6 | `mes_cos` | mes_cos(T-1) |
| 7 | `t_index` | t_index(T-1) |
| 8 | `T2M_lag1` | T2M(T-2) |
| 9 | `T2M_lag3` | T2M(T-4) |
| 10 | `T2M_lag6` | T2M(T-7) |
| 11 | `T2M_MAX_lag1` | T2M_MAX(T-2) |
| 12 | `T2M_MAX_lag3` | T2M_MAX(T-4) |
| 13 | `T2M_MAX_lag6` | T2M_MAX(T-7) |
| 14 | `WS2M_lag1` | WS2M(T-2) |
| 15 | `WS2M_lag3` | WS2M(T-4) |
| 16 | `WS2M_lag6` | WS2M(T-7) |
| 17 | `PRECTOTCORR_lag1` | PRECTOTCORR(T-2) |
| 18 | `PRECTOTCORR_lag3` | PRECTOTCORR(T-4) |
| 19 | `PRECTOTCORR_lag6` | PRECTOTCORR(T-7) |
| 20 | `RH2M_lag1` | RH2M(T-2) |
| 21 | `RH2M_lag3` | RH2M(T-4) |
| 22 | `RH2M_lag6` | RH2M(T-7) |
| 23 | `num_emergencias_lag1` | num_emergencias(T-2) |
| 24 | `num_emergencias_lag3` | num_emergencias(T-4) |
| 25 | `num_emergencias_lag6` | num_emergencias(T-7) |
| 26 | `personas_afectadas_lag1` | personas_afectadas(T-2) |
| 27 | `personas_afectadas_lag3` | personas_afectadas(T-4) |
| 28 | `personas_afectadas_lag6` | personas_afectadas(T-7) |
| 29 | `personas_damnificadas_lag1` | personas_damnificadas(T-2) |
| 30 | `personas_damnificadas_lag3` | personas_damnificadas(T-4) |
| 31 | `personas_damnificadas_lag6` | personas_damnificadas(T-7) |
| 32 | `hectareas_cultivo_perdidas_lag1` | hectareas_cultivo_perdidas(T-2) |
| 33 | `hectareas_cultivo_perdidas_lag3` | hectareas_cultivo_perdidas(T-4) |
| 34 | `hectareas_cultivo_perdidas_lag6` | hectareas_cultivo_perdidas(T-7) |
| 35 | `hectareas_cultivo_afectadas_lag1` | hectareas_cultivo_afectadas(T-2) |
| 36 | `hectareas_cultivo_afectadas_lag3` | hectareas_cultivo_afectadas(T-4) |
| 37 | `hectareas_cultivo_afectadas_lag6` | hectareas_cultivo_afectadas(T-7) |

- **¿y_{T−12} entra en algún modelo tabular?** **No.** Los rezagos de y son T−1, T−2, T−4 y T−7. El rezago más
  antiguo de cualquier variable es T−7. La estacionalidad solo entra por mes_sin/mes_cos (del mes T−1) y t_index.
- **¿Entra en la red con la ventana de 6 meses?** **Sí.** GC3 y GE reciben 6 filas (meses T−6 … T−1). La rama A
  tiene en cada fila y_r, y_{r−1}, y_{r−3} e y_{r−6}, así que cubre y_{T−1} … y_{T−12} completos: la fila T−6 con su
  lag6 es y_{T−12}. Se comprobó con los datos, valor por valor, en los dos cultivos y en las dos redes
  (`T4_1_entradas_rama_A_lstm.csv`, `T4_resumen.json`).
- La rama B no contiene y. Contiene las exógenas rezagadas 1, 3 y 6 en cada fila (meses T−2 … T−12): 33 entradas
  en GC3 y 39 en GE.

### T4.2 Figura 7 del artículo (fig20_real_vs_pred_2025_sutil/dulce)

Contenido real (CSV de datos de la figura; `T4_2_fig20_contenido.csv`):
- **`fig20_real_vs_pred_2025_{sutil,dulce}`** (la que nombra la pregunta):
  - **10 paneles**, uno por modelo (Naive, Seasonal Naive, Chronos, SARIMA, SARIMA-sel, Ridge, ElasticNet, XGB-37,
    GC3, GE), más la serie observada y los meses de shock P75 MoM sombreados;
  - XGB-37, GC3 y GE se dibujan con **una línea por semilla (10 líneas)**, no con el promedio;
  - su pie dice "Seeded models: one line per seed (10 seeds)";
  - es la figura que `12_paquete_overleaf.py` incluye en el texto principal (entrada 11 de 13 de `PRINCIPAL`).
- **`fig20_real_vs_pred_2025_main_{sutil,dulce}`** (versión reducida de la Fase 5, `14_fig20_reducida_2025.py`):
  - **4 paneles**: GC3, Chronos, SARIMA y Seasonal Naive;
  - GC3 es **una sola línea, la media de las 10 semillas**;
  - **no figura en `PRINCIPAL`** del paquete.

**Comparación con la leyenda** ("GC3, Chronos, SARIMA y Seasonal Naive, con GC3 promediada en 10 semillas"): describe
la versión **main**, no la fig20 que el paquete incluye. Si el manuscrito usa `fig20_real_vs_pred_2025_*`, hay una
discrepancia: la figura muestra 10 modelos, con una línea por semilla para XGB-37, GC3 y GE. Hay que cambiar la figura
por la versión main o la leyenda por la de la figura completa. Para alinearlo, basta añadir `_main` a las dos rutas
de la entrada fig20 de `PRINCIPAL`. No lo cambié porque `12_paquete_overleaf.py` es código publicado.

### T4.3 Seasonal Naive en limón dulce: MAE igual en todos los meses y en shock

Pool 2021–2025, shock MoM P75 (`T4_resumen.json`, `T4_3_seasonal_naive_dulce_meses.csv`):

| | n | MAE (t) |
|---|---|---|
| todos los meses | 60 | 24.503033 |
| meses normales | 45 | 24.503133 |
| meses de shock MoM P75 | 15 | 24.502733 |

- **La coincidencia es real; no es un error de asignación de meses.**
  - La predicción es y_{t−12} en los 60 meses de test (comprobado contra la serie).
  - La máscara publicada (`03_ventanas/umbrales_y_mascaras.csv`) es idéntica a la recalculada.
  - Los tres MAE difieren en la cuarta cifra decimal: Δs = -0.0012 %.
- **Control:** con la máscara desplazada un mes, el MAE de shock sería 26.892 t (un mes antes) o 28.228 t (un mes después). Con la misma máscara, otros modelos sí
  separan shock de normal: Naive 77.5 → 131.6 t; SARIMA 18.4 → 14.0 t; Chronos 30.8 → 48.2 t.
- **Interpretación:** en dulce, el error de Seasonal Naive no depende de si el cambio mensual es grande. El shock MoM
  mide |y_t − y_{t−1}|, y Seasonal Naive usa y_{t−12}.

---

## 3. Archivos creados

Nada se escribió fuera de esta carpeta, salvo `reproduce.py` (4 pasos nuevos al final) y `venv/` (ignorado).

- `13_revision_r2/README.md`, `13_revision_r2/INFORME_DIA1.md`
- `13_revision_r2/scripts/`: `r2lib.py`, `t1_ets_theta.py`, `t1_t2_evaluar.py`, `t3_sarima.py`, `t4_verificaciones.py`
- `13_revision_r2/resultados/`:
  - `unidades/{ETS,Theta}/{sutil,dulce}/{2021..2025}/`: `predicciones.csv` e `info.json`; ETS además `rejilla_ets.csv`;
  - T1: `T1_metricas_12_modelos_2021_2025.csv`, `T1_DM_HLN_vs_mejor.csv`, `T1_ranking_shock_P50_P90.csv`,
    `T1_robustez_3de4.csv`;
  - T2: `T2_ranking_2025.csv`, `T2_primer_lugar_2025_vs_pool.csv`;
  - T3: `T3_1_constante_parametros.csv`, `T3_2_sin_constante_por_ventana.csv`, `T3_2_sin_constante_pool.csv`,
    `T3_3_regla_respaldo_convergencia.csv`, `T3_3_SARIMA_sel_Y1_con_regla_pool.csv`, `T3_resumen.json`;
  - T4: `T4_1_predictores_tabulares.csv`, `T4_1_entradas_rama_A_lstm.csv`, `T4_2_fig20_contenido.csv`,
    `T4_3_seasonal_naive_dulce_meses.csv`, `T4_resumen.json`;
  - `tablas_T1_T2.md`.
- Modificado: `reproduce.py`, con 4 pasos R2 después de los existentes y una nota en el docstring.
- Entorno: `venv/` en la raíz, con `requirements.txt`. No hizo falta `requirements-r2.txt`.

## 4. Resultado de `reproduce.py --no-figures`

Ejecutado con `venv\Scripts\python.exe` (Python 3.11.9, paquetes de `requirements.txt`):

```
[OK] integrity: SHA-256 of official code, frozen data and Chronos (hashes_congelados.json) (0 s)
[OK] leakage test, backtesting (test_fuga.py) (15 s)
[OK] leakage test, diagnostic experiments (test_fuga_g7.py) (90 s)
[OK] phase D1: metrics, bootstrap, Diebold-Mariano, threshold sweep (run_all.py --fase D1) (32 s)
[OK] diagnostic experiments (G7): evaluation T1-T10 (evaluar.py) (11 s)
[OK] first-round diagnostic tables (09_reportes/revision_g7/fase1, g7_fase1.py): regenerate and compare cell by cell (6 s)
[OK] review R2 (13_revision_r2): ETS and Theta, rolling origin 2021-2025 (t1_ets_theta.py) (22 s)
[OK] review R2 (13_revision_r2): ETS/Theta metrics, 12-model ranking and 2025-only ranking (t1_t2_evaluar.py) (5 s)
[OK] review R2 (13_revision_r2): SARIMA constant, no-constant sensitivity and SARIMA-sel fallback rule (t3_sarima.py) (10 s)
[OK] review R2 (13_revision_r2): predictor lags, fig20 content and Seasonal Naive check (t4_verificaciones.py) (8 s)
Compared 2231 files (93 regenerated by this run): {'IDENTICAL': 2231}; max |difference| = 0. Report: reproduction_report.json
09_reportes/revision_g7/fase1: 15 of 15 tables identical cell by cell.
```

- Los 4 pasos R2 corren después de los existentes y no tocan lo publicado.
- Las salidas R2 de esta corrida son idénticas, byte a byte, a las de una corrida previa independiente. Son
  deterministas.
- No se modificó ningún archivo registrado en `hashes_congelados.json`: el paso de integridad da OK.

## 5. Lo que no se pudo hacer o verificar

- **Numeración de la Figura 7.** El manuscrito no está en el repositorio (`paper_mdpi/overleaf` no existe). No pude
  confirmar qué archivo es la "Figura 7": en el orden de `PRINCIPAL`, la fig20 es la figura 11 de 13. La respuesta
  de T4.2 se basa en los archivos y en el paquete, no en el PDF.
- **ETS y la validación.** Por instrucción, ETS se selecciona solo por AICc. No se replicó el paso de SARIMA-sel que
  elige entre los 5 mejores por MAE de validación. Es una diferencia de diseño, documentada en el README.
- **Theta en sutil 2021.** El test de estacionalidad de statsmodels decidió no desestacionalizar. No se forzó la
  desestacionalización. No se evaluó una variante con desestacionalización forzada.
- **Regla de respaldo.** "Siguiente orden por AIC" admite dos lecturas que dan resultados muy distintos en sutil 2021
  (3,023 t frente a 19,503 t). Se reportan las dos; falta decidir la redacción.
- **Figuras.** No se ejecutó `reproduce.py` con figuras (se pidió `--no-figures`). Este trabajo no generó figuras
  nuevas.
- **Git.** No se hizo ninguna operación git. `git status` muestra como modificadas algunas salidas publicadas porque
  `reproduce.py` las reescribe, pero `git diff` está vacío: el contenido es idéntico.
