<!-- generado por t7_sarimax.py -->
#### T7.2 — SARIMAX frente a SARIMA (pool 2021–2025)

| cultivo | alcance | modelo | n | MAE (IC95) | dif vs SARIMA (IC95) | DM vs SARIMA (HLN; p) |
|---|---|---|---|---|---|---|
| sutil | todos | SARIMA | 60 | 3,361 (2,780–3,970) | — | — |
| sutil | todos | SARIMAX-PC | 60 | 3,497 (2,865–4,151) | 137 (-100–414) | 1.01; 0.316 |
| sutil | todos | SARIMAX-30 | 60 | 19,620 (15,433–24,049) | 16,259 (12,098–20,686) | 6.96; 0.000 |
| sutil | shock_MoM_P75 | SARIMA | 10 | 5,131 (3,759–6,624) | — | — |
| sutil | shock_MoM_P75 | SARIMAX-PC | 10 | 5,082 (3,780–6,650) | -49 (-478–328) | -0.19; 0.857 |
| sutil | shock_MoM_P75 | SARIMAX-30 | 10 | 33,252 (25,831–42,077) | 28,122 (20,790–37,230) | 3.09; 0.013 |
| sutil | shock_YoY_P75 | SARIMA | 10 | 3,233 (2,430–3,968) | — | — |
| sutil | shock_YoY_P75 | SARIMAX-PC | 10 | 3,206 (2,366–3,995) | -27 (-426–440) | -0.10; 0.924 |
| sutil | shock_YoY_P75 | SARIMAX-30 | 10 | 24,881 (17,671–33,282) | 21,648 (14,008–30,728) | 3.63; 0.005 |
| dulce | todos | SARIMA | 60 | 18.4 (14.5–22.8) | — | — |
| dulce | todos | SARIMAX-PC | 60 | 19.7 (15.8–24.0) | 1.3 (-0.4–3.0) | 1.43; 0.159 |
| dulce | todos | SARIMAX-30 | 60 | 51.6 (39.7–64.2) | 33.2 (21.5–46.0) | 4.36; 0.000 |
| dulce | shock_MoM_P75 | SARIMA | 15 | 14.0 (9.8–18.0) | — | — |
| dulce | shock_MoM_P75 | SARIMAX-PC | 15 | 15.3 (10.1–20.7) | 1.3 (-2.1–5.4) | 0.55; 0.593 |
| dulce | shock_MoM_P75 | SARIMAX-30 | 15 | 65.5 (39.5–95.4) | 51.5 (25.0–81.4) | 2.25; 0.041 |
| dulce | shock_YoY_P75 | SARIMA | 16 | 27.4 (16.0–40.5) | — | — |
| dulce | shock_YoY_P75 | SARIMAX-PC | 16 | 27.2 (15.9–40.3) | -0.2 (-1.8–1.2) | -0.20; 0.843 |
| dulce | shock_YoY_P75 | SARIMAX-30 | 16 | 55.4 (45.7–65.6) | 28.0 (16.5–38.3) | 1.87; 0.081 |

Convergencia del ajuste en train (ventanas que convergen):

| modelo | cultivar | convergio |
|---|---|---|
| SARIMAX-30 | dulce | 5/5 |
| SARIMAX-30 | sutil | 4/5 |
| SARIMAX-PC | dulce | 5/5 |
| SARIMAX-PC | sutil | 5/5 |
