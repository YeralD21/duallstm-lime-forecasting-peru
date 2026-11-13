<!-- generado por t1_t2_evaluar.py; no editar a mano -->

## T1.a Precisión agregada 2021–2025 (formato Tabla 3, 12 modelos)

MAE en toneladas con IC 95 % bootstrap pareado (meses remuestreados dentro de cada ventana, B = 10 000, semilla 42). Δs = (MAE_shock − MAE)/MAE × 100. MASE_shock con los denominadores por ventana del artículo (03_ventanas/denominador_mase_por_ventana.csv). † = añadido posterior al protocolo (revisión R2); no altera el ranking principal. * = primero o empatado con el primero (IC 95 % bootstrap pareado de la diferencia con el mejor contiene 0).


### sutil (60 meses; shock MoM P75: 10; shock YoY P75: 10)

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

### dulce (60 meses; shock MoM P75: 15; shock YoY P75: 16)

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


## T1.b Diebold–Mariano HLN (pérdida absoluta, h = 1) de ETS y Theta frente al mejor

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


## T1.c Ranking por MAE en meses de shock, 12 modelos (formato Tabla 4)

† = añadido posterior al protocolo (revisión R2); no altera el ranking principal. * = primero o empatado con el primero (IC 95 % bootstrap pareado de la diferencia con el mejor contiene 0).


### sutil

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

### dulce

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


## T2 Ranking solo en 2025 (12 modelos)

† = añadido posterior al protocolo (revisión R2); no altera el ranking principal. * = primero o empatado con el primero (IC 95 % bootstrap pareado de la diferencia con el mejor contiene 0). IC con remuestreo de los meses de 2025 (un estrato).


### sutil

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

### dulce

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


### Primer lugar: 2025 frente al pool 2021–2025

| cultivo | criterio | n_meses_2025 | 1º 2025 (12 mod.) | 1º pool (12 mod.) | 1º 2025 (10 mod.) | 1º pool (10 mod.) | mismo 1º (12) | mismo 1º (10) | empatados con el 1º en 2025 |
|---|---|---|---|---|---|---|---|---|---|
| sutil | todos | 12 | ElasticNet | Chronos | ElasticNet | Chronos | No | No | ElasticNet, Ridge, Chronos, ETS, Theta, SARIMA-sel, SARIMA, Seasonal Naive, XGB-37 |
| sutil | shock_MoM_P75 | 3 | Seasonal Naive | ETS | Seasonal Naive | Chronos | No | No | Seasonal Naive, GC3, Theta, Chronos, Ridge, ElasticNet, SARIMA, XGB-37 |
| sutil | shock_YoY_P75 | 0 | — (sin meses) | Chronos | — (sin meses) | Chronos | — | — | — |
| dulce | todos | 12 | ETS | SARIMA | SARIMA-sel | SARIMA | No | No | ETS, Theta, SARIMA-sel, SARIMA, Chronos |
| dulce | shock_MoM_P75 | 3 | Theta | SARIMA | SARIMA-sel | SARIMA | No | No | Theta, ETS, SARIMA-sel |
| dulce | shock_YoY_P75 | 3 | Theta | SARIMA | XGB-37 | SARIMA | No | No | Theta, XGB-37, ElasticNet, Ridge, ETS, SARIMA-sel, SARIMA |
