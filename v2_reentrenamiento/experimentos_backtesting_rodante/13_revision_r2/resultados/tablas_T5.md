<!-- generado por t5_respaldo_sarima_sel.py -->
#### Por ventana (E1)

| cultivo | anio_test | orden_elegido_protocolo | E1_respaldo_usado | E1_orden_final | E1_posicion_aic_final | MAE publicado E1 | MAE regla T5 |
|---|---|---|---|---|---|---|---|
| sutil | 2021 | (2, 1, 0)(2, 1, 1, 12) | True | (3, 1, 2)(2, 1, 1, 12) | 1 | 73,706.1 | 19,503.2 |
| sutil | 2022 | (3, 1, 2)(2, 1, 2, 12) | False | (3, 1, 2)(2, 1, 2, 12) | 4 | 2,612.1 | 2,612.1 |
| sutil | 2023 | (1, 1, 3)(2, 1, 1, 12) | False | (1, 1, 3)(2, 1, 1, 12) | 2 | 4,027.4 | 4,027.4 |
| sutil | 2024 | (1, 1, 2)(2, 1, 1, 12) | False | (1, 1, 2)(2, 1, 1, 12) | 1 | 3,291.0 | 3,291.0 |
| sutil | 2025 | (1, 1, 3)(2, 1, 0, 12) | False | (1, 1, 3)(2, 1, 0, 12) | 4 | 3,680.1 | 3,680.1 |
| dulce | 2021 | (2, 0, 3)(0, 0, 0, 12) | False | (2, 0, 3)(0, 0, 0, 12) | 2 | 26.0 | 26.0 |
| dulce | 2022 | (1, 0, 0)(0, 1, 0, 12) | False | (1, 0, 0)(0, 1, 0, 12) | 2 | 12.2 | 12.2 |
| dulce | 2023 | (2, 0, 0)(0, 1, 0, 12) | False | (2, 0, 0)(0, 1, 0, 12) | 4 | 17.3 | 17.3 |
| dulce | 2024 | (2, 0, 0)(0, 1, 0, 12) | False | (2, 0, 0)(0, 1, 0, 12) | 2 | 25.9 | 25.9 |
| dulce | 2025 | (2, 0, 1)(0, 1, 0, 12) | False | (2, 0, 1)(0, 1, 0, 12) | 4 | 18.4 | 18.4 |

#### Pool 2021–2025

| cultivo | alcance | modelo | n_meses | MAE (IC95) | mejor | DM vs mejor (HLN; p) |
|---|---|---|---|---|---|---|
| sutil | todos | SARIMA-sel | 60 | 3,206 (2,563–3,880) | Chronos | 1.66; 0.102 |
| sutil | todos | SARIMA-sel-Y1 | 60 | 17,463 (12,375–23,510) | Chronos | 3.18; 0.002 |
| sutil | todos | SARIMA-sel-Y1-R | 60 | 6,623 (5,263–8,145) | Chronos | 3.59; 0.001 |
| sutil | shock_MoM_P75 | SARIMA-sel | 10 | 4,936 (2,866–7,242) | Chronos | 0.17; 0.867 |
| sutil | shock_MoM_P75 | SARIMA-sel-Y1 | 10 | 4,994 (3,200–6,985) | Chronos | 0.27; 0.791 |
| sutil | shock_MoM_P75 | SARIMA-sel-Y1-R | 10 | 4,994 (3,200–6,985) | Chronos | 0.27; 0.791 |
| sutil | shock_YoY_P75 | SARIMA-sel | 10 | 4,079 (2,145–6,099) | Chronos | 1.97; 0.081 |
| sutil | shock_YoY_P75 | SARIMA-sel-Y1 | 10 | 4,167 (2,556–5,887) | Chronos | 2.34; 0.044 |
| sutil | shock_YoY_P75 | SARIMA-sel-Y1-R | 10 | 4,167 (2,556–5,887) | Chronos | 2.34; 0.044 |
| dulce | todos | SARIMA-sel | 60 | 20.6 (16.5–25.2) | SARIMA | 1.29; 0.203 |
| dulce | todos | SARIMA-sel-Y1 | 60 | 20.0 (15.9–24.5) | SARIMA | 0.94; 0.351 |
| dulce | todos | SARIMA-sel-Y1-R | 60 | 20.0 (15.9–24.5) | SARIMA | 0.94; 0.351 |
| dulce | shock_MoM_P75 | SARIMA-sel | 15 | 19.7 (15.6–23.6) | SARIMA | 1.68; 0.115 |
| dulce | shock_MoM_P75 | SARIMA-sel-Y1 | 15 | 18.3 (14.8–21.6) | SARIMA | 1.30; 0.216 |
| dulce | shock_MoM_P75 | SARIMA-sel-Y1-R | 15 | 18.3 (14.8–21.6) | SARIMA | 1.30; 0.216 |
| dulce | shock_YoY_P75 | SARIMA-sel | 16 | 28.4 (17.3–41.2) | SARIMA | 0.34; 0.737 |
| dulce | shock_YoY_P75 | SARIMA-sel-Y1 | 16 | 28.5 (17.4–41.5) | SARIMA | 0.40; 0.698 |
| dulce | shock_YoY_P75 | SARIMA-sel-Y1-R | 16 | 28.5 (17.4–41.5) | SARIMA | 0.40; 0.698 |
