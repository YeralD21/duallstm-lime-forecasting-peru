<!-- generado por t6_t7_tabulares.py -->
#### T6 — E5: y_(T−12) en los modelos tabulares (pool 2021–2025)

Diferencia = E5 − original (negativa = E5 mejor), IC 95 % bootstrap pareado. «Solo y12» = E5 − original con las mismas filas de entrenamiento (aísla el efecto de y_(T−12) del de perder los pares con objetivo 2016-08..2016-12). DM-HLN de E5 frente al mejor modelo del cultivo (sutil: Chronos; dulce: SARIMA).

| cultivo | alcance | modelo | n | MAE original (IC95) | MAE E5 (IC95) | dif E5−orig (IC95) | solo y12 (IC95) | semillas E5 mejor (de 10) | DM E5 vs mejor (HLN; p) | p DM orig vs mejor |
|---|---|---|---|---|---|---|---|---|---|---|
| sutil | todos | Ridge | 60 | 4,925 (3,838–6,074) | 3,922 (3,188–4,674) | -1,003 (-2,239–144) | -242 (-494–24) | — | 3.09; 0.003 | 0.002 |
| sutil | todos | ElasticNet | 60 | 4,872 (3,847–5,950) | 4,028 (3,159–4,906) | -844 (-1,902–131) | -230 (-601–163) | — | 2.92; 0.005 | 0.002 |
| sutil | todos | XGB-37 | 60 | 4,881 (4,063–5,732) | 4,725 (3,901–5,579) | -156 (-382–68) | 73 (-103–245) | 10 | 4.35; 0.000 | 0.000 |
| sutil | shock_MoM_P75 | Ridge | 10 | 8,557 (5,484–12,360) | 4,640 (3,783–5,616) | -3,917 (-7,740–-818) | 258 (-78–623) | — | -0.25; 0.809 | 0.145 |
| sutil | shock_MoM_P75 | ElasticNet | 10 | 8,154 (5,162–11,484) | 4,931 (3,598–6,274) | -3,223 (-5,773–-750) | 418 (-417–1,310) | — | 0.21; 0.839 | 0.146 |
| sutil | shock_MoM_P75 | XGB-37 | 10 | 5,955 (3,727–7,965) | 5,421 (3,190–7,478) | -534 (-1,083–-21) | -229 (-461–9) | 9 | 0.64; 0.538 | 0.292 |
| sutil | shock_YoY_P75 | Ridge | 10 | 4,946 (3,290–6,789) | 4,390 (2,485–6,386) | -556 (-1,556–423) | 586 (123–1,012) | — | 1.92; 0.087 | 0.035 |
| sutil | shock_YoY_P75 | ElasticNet | 10 | 5,404 (3,428–7,594) | 5,167 (2,515–8,002) | -236 (-1,596–1,108) | 1,055 (256–1,828) | — | 1.85; 0.098 | 0.030 |
| sutil | shock_YoY_P75 | XGB-37 | 10 | 4,816 (2,548–7,254) | 5,215 (2,563–7,995) | 398 (-450–1,230) | 457 (-134–1,089) | 1 | 1.95; 0.082 | 0.080 |
| dulce | todos | Ridge | 60 | 53.1 (43.4–63.4) | 49.2 (42.0–56.6) | -3.9 (-13.4–5.1) | -5.2 (-10.7–0.4) | — | 8.11; 0.000 | 0.000 |
| dulce | todos | ElasticNet | 60 | 50.2 (40.7–60.4) | 48.1 (40.9–55.6) | -2.2 (-11.3–6.5) | -0.6 (-8.1–6.7) | — | 7.96; 0.000 | 0.000 |
| dulce | todos | XGB-37 | 60 | 48.3 (39.8–57.2) | 37.6 (31.6–43.8) | -10.7 (-16.5–-5.1) | -9.4 (-15.6–-3.6) | 10 | 5.23; 0.000 | 0.000 |
| dulce | shock_MoM_P75 | Ridge | 15 | 69.7 (52.0–89.3) | 59.8 (47.8–73.2) | -9.9 (-28.2–6.8) | -14.2 (-21.5–-7.7) | — | 6.11; 0.000 | 0.000 |
| dulce | shock_MoM_P75 | ElasticNet | 15 | 67.2 (49.5–87.1) | 59.0 (46.9–73.0) | -8.2 (-25.2–7.4) | -7.1 (-23.0–7.8) | — | 5.79; 0.000 | 0.000 |
| dulce | shock_MoM_P75 | XGB-37 | 15 | 65.8 (51.6–80.6) | 45.3 (37.9–52.1) | -20.6 (-34.2–-7.5) | -20.2 (-36.4–-5.1) | 10 | 5.50; 0.000 | 0.000 |
| dulce | shock_YoY_P75 | Ridge | 16 | 66.4 (47.7–85.1) | 62.0 (43.7–80.6) | -4.4 (-16.1–8.5) | -2.4 (-10.4–6.4) | — | 3.96; 0.001 | 0.014 |
| dulce | shock_YoY_P75 | ElasticNet | 16 | 57.3 (38.2–77.1) | 57.9 (39.3–77.2) | 0.6 (-11.2–13.7) | 5.0 (-6.0–18.0) | — | 3.62; 0.003 | 0.037 |
| dulce | shock_YoY_P75 | XGB-37 | 16 | 42.3 (29.6–54.6) | 43.5 (34.6–52.7) | 1.2 (-8.1–10.6) | 3.6 (-7.2–14.0) | 4 | 2.58; 0.021 | 0.141 |

#### T7.1 — Ablación por bloques acumulativos (pool 2021–2025)

Diferencia = conjunto − conjunto anterior (negativa = el bloque añadido mejora). (c) = E5.

| cultivo | modelo | conjunto | k | alcance | MAE (IC95) | dif vs anterior (IC95) | semillas mejoran (de 10) |
|---|---|---|---|---|---|---|---|
| sutil | Ridge | (a) producción+calendario+y12 | 8 | todos | 3,875 (3,249–4,484) | — | — |
| sutil | Ridge | (b) +clima | 23 | todos | 4,624 (3,882–5,345) | 749 (374–1,125) | — |
| sutil | Ridge | (c) +emergencias | 38 | todos | 3,922 (3,188–4,674) | -702 (-1,175–-249) | — |
| sutil | Ridge | (d) +noticias | 44 | todos | 4,750 (3,759–5,796) | 828 (-3–1,682) | — |
| sutil | Ridge | (a) producción+calendario+y12 | 8 | shock_MoM_P75 | 6,278 (4,916–8,019) | — | — |
| sutil | Ridge | (b) +clima | 23 | shock_MoM_P75 | 7,031 (5,661–8,492) | 753 (-470–1,974) | — |
| sutil | Ridge | (c) +emergencias | 38 | shock_MoM_P75 | 4,640 (3,783–5,616) | -2,391 (-3,940–-1,131) | — |
| sutil | Ridge | (d) +noticias | 44 | shock_MoM_P75 | 5,303 (2,569–8,692) | 663 (-2,261–4,219) | — |
| sutil | XGB-37 | (a) producción+calendario+y12 | 8 | todos | 4,251 (3,522–4,993) | — | — |
| sutil | XGB-37 | (b) +clima | 23 | todos | 4,765 (3,962–5,596) | 514 (148–875) | 0 |
| sutil | XGB-37 | (c) +emergencias | 38 | todos | 4,725 (3,901–5,579) | -40 (-180–101) | 7 |
| sutil | XGB-37 | (d) +noticias | 44 | todos | 4,851 (4,009–5,717) | 126 (-11–262) | 0 |
| sutil | XGB-37 | (a) producción+calendario+y12 | 8 | shock_MoM_P75 | 5,009 (2,705–7,374) | — | — |
| sutil | XGB-37 | (b) +clima | 23 | shock_MoM_P75 | 5,523 (3,354–7,542) | 514 (-328–1,282) | 0 |
| sutil | XGB-37 | (c) +emergencias | 38 | shock_MoM_P75 | 5,421 (3,190–7,478) | -102 (-471–316) | 7 |
| sutil | XGB-37 | (d) +noticias | 44 | shock_MoM_P75 | 5,617 (3,444–7,620) | 196 (-180–525) | 1 |
| dulce | Ridge | (a) producción+calendario+y12 | 8 | todos | 39.7 (33.8–46.3) | — | — |
| dulce | Ridge | (b) +clima | 23 | todos | 38.3 (32.6–44.2) | -1.5 (-6.4–3.8) | — |
| dulce | Ridge | (c) +emergencias | 38 | todos | 49.2 (42.0–56.6) | 10.9 (4.7–17.1) | — |
| dulce | Ridge | (d) +noticias | 44 | todos | 34.5 (28.7–40.7) | -14.7 (-21.3–-8.1) | — |
| dulce | Ridge | (a) producción+calendario+y12 | 8 | shock_MoM_P75 | 45.4 (37.5–54.2) | — | — |
| dulce | Ridge | (b) +clima | 23 | shock_MoM_P75 | 41.7 (33.2–51.5) | -3.7 (-9.9–2.4) | — |
| dulce | Ridge | (c) +emergencias | 38 | shock_MoM_P75 | 59.8 (47.8–73.2) | 18.1 (6.5–29.6) | — |
| dulce | Ridge | (d) +noticias | 44 | shock_MoM_P75 | 34.6 (25.0–44.8) | -25.3 (-38.3–-13.6) | — |
| dulce | XGB-37 | (a) producción+calendario+y12 | 8 | todos | 32.8 (27.9–38.2) | — | — |
| dulce | XGB-37 | (b) +clima | 23 | todos | 35.5 (29.9–41.4) | 2.7 (-0.8–6.1) | 0 |
| dulce | XGB-37 | (c) +emergencias | 38 | todos | 37.6 (31.6–43.8) | 2.1 (0.5–3.7) | 0 |
| dulce | XGB-37 | (d) +noticias | 44 | todos | 36.4 (30.6–42.6) | -1.2 (-2.7–0.4) | 8 |
| dulce | XGB-37 | (a) producción+calendario+y12 | 8 | shock_MoM_P75 | 30.1 (24.2–35.7) | — | — |
| dulce | XGB-37 | (b) +clima | 23 | shock_MoM_P75 | 41.2 (34.8–47.0) | 11.2 (7.7–14.6) | 0 |
| dulce | XGB-37 | (c) +emergencias | 38 | shock_MoM_P75 | 45.3 (37.9–52.1) | 4.0 (0.7–7.2) | 1 |
| dulce | XGB-37 | (d) +noticias | 44 | shock_MoM_P75 | 40.9 (34.2–47.2) | -4.4 (-6.1–-2.6) | 10 |
