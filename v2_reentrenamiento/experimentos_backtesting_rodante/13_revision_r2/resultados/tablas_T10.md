<!-- generado por t10_crps.py -->
#### T10 — CRPS y CRPS ponderado por umbral (pool 2021–2025, t)

Niveles de cuantil: 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9. Menor = mejor.

| cultivo | métrica | alcance | modelo | n | media (IC95) | dif vs SARIMA (IC95) | DM p |
|---|---|---|---|---|---|---|---|
| sutil | CRPS_Q | todos | Chronos | 60 | 2,065 (1,722–2,431) | -512 (-846–-161) | 0.005 |
| sutil | CRPS_Q | todos | SARIMA | 60 | 2,577 (2,194–2,995) | — | — |
| sutil | CRPS_Q | todos | SARIMA-sel | 60 | 2,564 (2,089–3,089) | -13 (-380–378) | 0.948 |
| sutil | CRPS_Q | shock_MoM_P75 | Chronos | 10 | 3,665 (2,919–4,484) | -309 (-732–132) | 0.305 |
| sutil | CRPS_Q | shock_MoM_P75 | SARIMA | 10 | 3,975 (3,051–5,089) | — | — |
| sutil | CRPS_Q | shock_MoM_P75 | SARIMA-sel | 10 | 4,042 (2,289–6,029) | 68 (-1,053–1,446) | 0.925 |
| sutil | twCRPS_Q | todos | Chronos | 60 | 407 (176–681) | -155 (-256–-72) | 0.003 |
| sutil | twCRPS_Q | todos | SARIMA | 60 | 562 (316–850) | — | — |
| sutil | twCRPS_Q | todos | SARIMA-sel | 60 | 519 (271–815) | -44 (-147–62) | 0.421 |
| sutil | twCRPS_Q | shock_MoM_P75 | Chronos | 10 | 2,283 (1,649–2,945) | -98 (-238–43) | 0.234 |
| sutil | twCRPS_Q | shock_MoM_P75 | SARIMA | 10 | 2,381 (1,738–3,040) | — | — |
| sutil | twCRPS_Q | shock_MoM_P75 | SARIMA-sel | 10 | 2,344 (1,492–3,241) | -37 (-396–375) | 0.866 |
| sutil | CRPS_normal_exacto | todos | SARIMA | 60 | 2,355 (2,009–2,731) | — | — |
| sutil | CRPS_normal_exacto | todos | SARIMA-sel | 60 | 2,348 (1,913–2,829) | -7 (-341–352) | 0.971 |
| sutil | CRPS_normal_exacto | shock_MoM_P75 | SARIMA | 10 | 3,613 (2,779–4,621) | — | — |
| sutil | CRPS_normal_exacto | shock_MoM_P75 | SARIMA-sel | 10 | 3,727 (2,088–5,588) | 114 (-939–1,411) | 0.866 |
| dulce | CRPS_Q | todos | Chronos | 60 | 23.4 (19.7–27.7) | 8.6 (4.0–13.2) | 0.001 |
| dulce | CRPS_Q | todos | SARIMA | 60 | 14.8 (11.9–18.4) | — | — |
| dulce | CRPS_Q | todos | SARIMA-sel | 60 | 16.2 (13.1–19.8) | 1.3 (-0.3–3.0) | 0.179 |
| dulce | CRPS_Q | shock_MoM_P75 | Chronos | 15 | 35.3 (28.6–42.4) | 23.7 (15.7–31.1) | 0.000 |
| dulce | CRPS_Q | shock_MoM_P75 | SARIMA | 15 | 11.6 (8.9–14.5) | — | — |
| dulce | CRPS_Q | shock_MoM_P75 | SARIMA-sel | 15 | 14.5 (11.9–17.2) | 2.9 (1.8–4.0) | 0.138 |
| dulce | twCRPS_Q | todos | Chronos | 60 | 4.3 (2.3–6.6) | 1.9 (0.7–3.2) | 0.005 |
| dulce | twCRPS_Q | todos | SARIMA | 60 | 2.4 (1.4–3.5) | — | — |
| dulce | twCRPS_Q | todos | SARIMA-sel | 60 | 3.0 (1.6–4.6) | 0.6 (-0.1–1.6) | 0.195 |
| dulce | twCRPS_Q | shock_MoM_P75 | Chronos | 15 | 17.1 (12.9–21.4) | 8.7 (5.8–11.5) | 0.000 |
| dulce | twCRPS_Q | shock_MoM_P75 | SARIMA | 15 | 8.5 (6.8–10.4) | — | — |
| dulce | twCRPS_Q | shock_MoM_P75 | SARIMA-sel | 15 | 11.5 (9.3–13.7) | 3.0 (1.5–4.4) | 0.115 |
| dulce | CRPS_normal_exacto | todos | SARIMA | 60 | 13.7 (10.9–17.1) | — | — |
| dulce | CRPS_normal_exacto | todos | SARIMA-sel | 60 | 14.9 (12.0–18.4) | 1.2 (-0.2–2.7) | 0.172 |
| dulce | CRPS_normal_exacto | shock_MoM_P75 | SARIMA | 15 | 10.7 (8.2–13.3) | — | — |
| dulce | CRPS_normal_exacto | shock_MoM_P75 | SARIMA-sel | 15 | 13.2 (10.9–15.6) | 2.6 (1.6–3.6) | 0.142 |

Cobertura empírica del intervalo 10–90 % (nominal 80 %):

| cultivar | modelo | cobertura_80 |
|---|---|---|
| dulce | Chronos | 80.0 % |
| dulce | SARIMA | 85.0 % |
| dulce | SARIMA-sel | 85.0 % |
| sutil | Chronos | 80.0 % |
| sutil | SARIMA | 85.0 % |
| sutil | SARIMA-sel | 75.0 % |
