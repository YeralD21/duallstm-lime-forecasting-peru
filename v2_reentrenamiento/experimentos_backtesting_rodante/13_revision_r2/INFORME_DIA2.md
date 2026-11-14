# Revisión G7, ronda 2 — Día 2: T5–T10

**Todo lo de este informe es posterior al protocolo**. Se reporta como robustez o diagnóstico y **no modifica el
ranking principal** de 10 modelos. Las cifras salen de `13_revision_r2/resultados/` (CSV generados por los scripts de
`13_revision_r2/scripts/`). Las tablas se copian sin editar de `resultados/tablas_T5.md` … `tablas_T10.md`.

**Convenciones:**
- MAE en toneladas;
- IC 95 %: bootstrap pareado, meses remuestreados dentro de cada ventana, B = 10 000, semilla 42;
- * = primero o empatado con el primero;
- «robusto» = primero o empatado en ≥ 3 de P50, P60, P75 y P90;
- DM: Diebold–Mariano con corrección HLN (pérdida absoluta);
- † = añadido posterior (ETS, Theta);
- «mejor» = menor MAE en todos los meses entre los 10 del artículo: sutil Chronos, dulce SARIMA.

---

## 1. Tablas

### T5 — Regla de respaldo de SARIMA-sel (obs. 11)

**Regla** (`r2lib.REGLA_RESPALDO`, función general `r2lib.elegir_con_respaldo`): «si el orden elegido por MAE de
validación entre los 5 de menor AIC no converge en el ajuste final, se usa el siguiente con menor MAE de validación
entre los que convergen». Empate: menor AIC de la rejilla, luego orden de la rejilla. Si ninguno converge, se conserva
el elegido y se marca.

- **Protocolo original:** se aplicó a las 10 ventanas y no cambia ninguna (todas convergen; el script lo verifica).
- **E1:** solo actúa en **sutil 2021**.
  - Orden de intentos por MAE de validación: AIC#3 (2, 1, 0)(2, 1, 1, 12) (MAE_val 2,256.7 t, no converge); AIC#4 (1, 1, 0)(2, 1, 1, 12) (MAE_val 2,306.4 t, no converge); AIC#5 (0, 1, 0)(2, 1, 1, 12) (MAE_val 2,483.5 t, no converge); AIC#1 (3, 1, 2)(2, 1, 1, 12) (MAE_val 2,668.6 t, converge).
  - Orden resultante: **(3, 1, 2)(2, 1, 1, 12) (AIC#1)**.

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

**Lectura:**
- Con la regla T5, el MAE de sutil 2021 en E1 baja de 73,706 a 19,503 t, y el MAE agrupado de SARIMA-sel-Y1 baja de
  17,463 a 6,623 t.
- Aun así, sigue siendo significativamente peor que Chronos (DM p = 0.001) y que el SARIMA-sel del protocolo
  (3,206 t).
- Los MAE de shock no cambian, porque sutil 2021 no tiene meses de shock P75 (ni MoM ni YoY).
- En dulce, la regla no actúa.
- **Comparación con el Día 1:** la regla "siguiente por AIC" (T3.3) daba AIC#2 y 3,023 t en 2021. El criterio de
  validación del protocolo lleva en cambio a AIC#1, que converge pero pronostica mal ese año. Es la misma cifra que la
  "lectura alternativa B" del Día 1.

### T6 — E5: y_(T−12) en los modelos tabulares (obs. 3)

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

**Lectura de T6:**
- **Sutil, Ridge y ElasticNet:** E5 baja mucho el MAE en shock MoM (Ridge −3,917 t, IC excluye 0). Pero casi toda la
  mejora viene de perder los 5 pares de 2016, no de y_(T−12): con las mismas filas, el efecto de y_(T−12) es +258 t
  en shock MoM y −242 t en todos los meses, y los dos IC contienen 0.
- **Sutil, XGB-37:** mejora en shock MoM (−534 t; 9 de 10 semillas), pero con las mismas filas el efecto de y_(T−12)
  no es significativo.
- **Dulce, XGB-37:** el único efecto claro y atribuible a y_(T−12). Con las mismas filas: −9.4 t en todos los meses y
  −20.2 t en shock MoM, ambos IC excluyen 0; 10 de 10 semillas mejoran.
- **Dulce, Ridge y ElasticNet:** sin cambios significativos en todos los meses.
- **Frente al mejor modelo:**
  - en dulce, los tres E5 siguen siendo significativamente peores que SARIMA (DM p ≤ 0.021);
  - en sutil, siguen siendo peores que Chronos en todos los meses (p ≤ 0.005), pero no en shock MoM.
- **Conclusión:** dar y_(T−12) a los tabulares no los acerca a los modelos estadísticos. Esto es coherente con que la
  red, que ya ve y_(T−12), tampoco lo esté.

### T7.1 — Ablación por bloques (obs. 3, RQ3)

(La tabla de T7.1 va al final del bloque T6, en el mismo fragmento generado.)

**Lectura de T7.1:**
- **Ningún bloque exógeno mejora de forma consistente.** Entre clima, emergencias y noticias, el signo del efecto cambia
  según el modelo y el cultivo, y muchas diferencias están en el borde de la significancia.
- **Efectos significativos (IC excluye 0):**
  - el clima empeora Ridge (+749 t) y XGB (+514 t) en sutil, y XGB en shock en dulce (+11.2 t);
  - las emergencias mejoran Ridge en sutil (−702 t; −2,391 t en shock), pero lo empeoran en dulce (+10.9 t);
  - las noticias mejoran Ridge en dulce (−14.7 t) y XGB en shock en dulce (−4.4 t; 10 de 10 semillas).
- **Conjunto mínimo (a)** (producción + calendario + y_(T−12)): es el mejor de los cuatro en 3 de los 4
  modelo-cultivo (sutil Ridge 3,875 t, sutil XGB 4,251 t, dulce XGB 32.8 t). En dulce Ridge, el mejor es (d), con
  34.5 t.

### T7.2 — SARIMAX (obs. 3, RQ3)

**Elección fijada antes de ver resultados** (docstring de `t7_sarimax.py` y README):
- **Rezagos:** los de los tabulares (x_(T−2), x_(T−4), x_(T−7)).
- **Versión principal:** «SARIMAX-PC», con la PC1 del clima y la PC1 de las emergencias (PCA ajustada solo con el
  train) en el rezago 1.
- **Versión secundaria:** «SARIMAX-30», con las 30 exógenas, marcada como sobreparametrizada.

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

**Lectura:**
- **SARIMAX-PC:** no difiere significativamente de SARIMA en ningún cultivo ni alcance (todos los IC contienen 0,
  DM p ≥ 0.159).
- **SARIMAX-30:** es mucho peor (sutil 19,620 t; dulce 51.6 t). Es la sobreparametrización esperada: 30 exógenas con
  42–90 meses. Además, una ventana (sutil 2022) no converge.
- **Conclusión:** las exógenas agregadas no aportan a un modelo estadístico bien especificado.

### T8 — Meses de cambio grande definidos ex ante (obs. 2)

Eventos El Niño costero leídos de la lista IGP: 1951-05..1951-12, 1953-02..1953-10, 1957-03..1958-07, 1963-08..1963-10, 1965-03..1966-01, 1968-09..1968-11, 1969-03..1970-01, 1972-02..1973-02, 1976-04..1976-12, 1982-07..1983-11, 1986-12..1987-12, 1991-08..1992-06, 1993-03..1993-09, 1994-11..1995-01, 1997-04..1998-08, 2002-03..2002-05, 2006-08..2006-12, 2008-06..2008-09, 2009-06..2009-09, 2012-04..2012-07, 2014-05..2014-11, 2015-04..2016-05, 2017-01..2017-04, 2018-11..2019-01, 2023-03..2024-02.

#### A. Cambio anticipado por Seasonal Naive

**sutil** — n marcados (P50/P60/P75/P90): 27/22/11/1; de los 11 meses P75 marcados, 3 son shock MoM P75 ex post (de 10).

| modelo | MAE (IC95) P75 | MASE | P50 | P60 | P75 | P90 | 1º/empate (de 4) | robusto |
|---|---|---|---|---|---|---|---|---|
| Naive | 4,090 (2,715–5,633) | 0.73 | 6 | 5 | 6 | 5 | 0 | No |
| Seasonal Naive | 11,120 (8,466–13,696) | 1.99 | 12 | 12 | 12 | 12 | 0 | No |
| Chronos | 2,234 (1,731–2,727) | 0.39 | 1* | 1* | 1* | 3 | 3 | Sí |
| SARIMA | 3,492 (2,727–4,224) | 0.62 | 5 | 4 | 4 | 7 | 0 | No |
| SARIMA-sel | 4,088 (2,211–6,076) | 0.73 | 4* | 6 | 5 | 1* | 2 | No |
| Ridge | 8,487 (4,962–12,148) | 1.49 | 11 | 9 | 11 | 11 | 0 | No |
| ElasticNet | 8,353 (5,438–11,402) | 1.47 | 10 | 8 | 10 | 10 | 0 | No |
| XGB-37 | 4,424 (2,647–6,463) | 0.79 | 7 | 7 | 7 | 2 | 0 | No |
| GC3 | 7,866 (4,916–11,156) | 1.41 | 8 | 10 | 8 | 9 | 0 | No |
| GE | 8,158 (5,441–11,188) | 1.46 | 9 | 11 | 9 | 8 | 0 | No |
| ETS † | 2,891 (2,125–3,618) | 0.51 | 2* | 3* | 2* | 6 | 3 | Sí |
| Theta † | 2,895 (2,250–3,498) | 0.51 | 3* | 2* | 3* | 4 | 3 | Sí |

**dulce** — n marcados (P50/P60/P75/P90): 31/24/18/1; de los 18 meses P75 marcados, 13 son shock MoM P75 ex post (de 15).

| modelo | MAE (IC95) P75 | MASE | P50 | P60 | P75 | P90 | 1º/empate (de 4) | robusto |
|---|---|---|---|---|---|---|---|---|
| Naive | 127.8 (111.4–143.7) | 4.93 | 12 | 12 | 12 | 12 | 0 | No |
| Seasonal Naive | 24.6 (21.2–28.3) | 0.96 | 5 | 5 | 5 | 5 | 0 | No |
| Chronos | 42.4 (34.2–51.2) | 1.66 | 6 | 6 | 6 | 6 | 0 | No |
| SARIMA | 14.4 (9.4–20.0) | 0.56 | 1* | 1* | 1* | 8 | 3 | Sí |
| SARIMA-sel | 18.1 (13.7–22.8) | 0.67 | 2* | 2* | 2* | 7 | 3 | Sí |
| Ridge | 69.1 (54.0–85.8) | 2.70 | 11 | 11 | 11 | 11 | 0 | No |
| ElasticNet | 63.3 (47.8–80.7) | 2.47 | 10 | 10 | 10 | 10 | 0 | No |
| XGB-37 | 55.2 (41.8–68.6) | 2.14 | 7 | 9 | 7 | 1* | 1 | No |
| GC3 | 61.6 (48.8–74.7) | 2.44 | 9 | 8 | 9 | 4 | 0 | No |
| GE | 59.2 (45.8–73.5) | 2.33 | 8 | 7 | 8 | 3 | 0 | No |
| ETS † | 20.2 (16.1–24.3) | 0.76 | 3* | 3 | 3* | 2 | 2 | No |
| Theta † | 20.6 (13.3–28.7) | 0.77 | 4* | 4* | 4* | 9 | 3 | Sí |

#### B. Cambio anticipado por SARIMA fijo

**sutil** — n marcados (P50/P60/P75/P90): 32/25/10/2; de los 10 meses P75 marcados, 3 son shock MoM P75 ex post (de 10).

| modelo | MAE (IC95) P75 | MASE | P50 | P60 | P75 | P90 | 1º/empate (de 4) | robusto |
|---|---|---|---|---|---|---|---|---|
| Naive | 3,998 (2,224–5,836) | 0.67 | 6 | 6 | 6 | 2 | 0 | No |
| Seasonal Naive | 4,539 (2,985–6,041) | 0.75 | 10 | 11 | 11 | 9 | 0 | No |
| Chronos | 2,598 (1,681–3,505) | 0.43 | 1* | 1* | 1* | 3 | 3 | Sí |
| SARIMA | 4,461 (3,032–5,889) | 0.74 | 5 | 5* | 10 | 10 | 1 | No |
| SARIMA-sel | 3,653 (2,021–5,310) | 0.60 | 2* | 2* | 3* | 8 | 3 | Sí |
| Ridge | 4,092 (3,018–5,306) | 0.67 | 7 | 8* | 9 | 12 | 1 | No |
| ElasticNet | 3,673 (2,455–5,035) | 0.60 | 8 | 7* | 4* | 11 | 2 | No |
| XGB-37 | 4,080 (2,847–5,318) | 0.67 | 9 | 9 | 8 | 6 | 0 | No |
| GC3 | 4,054 (2,909–4,774) | 0.69 | 11 | 10 | 7* | 7 | 1 | No |
| GE | 4,971 (3,771–6,071) | 0.84 | 12 | 12 | 12 | 4 | 0 | No |
| ETS † | 3,480 (2,397–4,562) | 0.57 | 4* | 4 | 2 | 5 | 1 | No |
| Theta † | 3,875 (2,456–5,294) | 0.65 | 3* | 3* | 5 | 1* | 3 | Sí |

**dulce** — n marcados (P50/P60/P75/P90): 30/24/16/2; de los 16 meses P75 marcados, 14 son shock MoM P75 ex post (de 15).

| modelo | MAE (IC95) P75 | MASE | P50 | P60 | P75 | P90 | 1º/empate (de 4) | robusto |
|---|---|---|---|---|---|---|---|---|
| Naive | 123.2 (106.9–140.7) | 4.64 | 12 | 12 | 12 | 12 | 0 | No |
| Seasonal Naive | 23.0 (19.7–26.5) | 0.86 | 4 | 4 | 5 | 2 | 0 | No |
| Chronos | 46.0 (39.1–53.4) | 1.78 | 6 | 6 | 6 | 4 | 0 | No |
| SARIMA | 13.5 (9.3–18.1) | 0.51 | 1* | 1* | 1* | 1* | 4 | Sí |
| SARIMA-sel | 17.5 (13.5–21.4) | 0.63 | 2* | 2* | 3* | 5 | 3 | Sí |
| Ridge | 63.0 (46.4–81.3) | 2.44 | 11 | 11 | 10 | 11 | 0 | No |
| ElasticNet | 61.7 (45.4–80.0) | 2.38 | 10 | 10 | 9 | 9 | 0 | No |
| XGB-37 | 64.3 (50.9–77.9) | 2.47 | 7 | 8 | 11 | 7 | 0 | No |
| GC3 | 58.6 (44.8–73.2) | 2.27 | 9 | 9 | 8 | 8 | 0 | No |
| GE | 55.8 (40.9–72.2) | 2.16 | 8 | 7 | 7 | 10 | 0 | No |
| ETS † | 18.6 (14.4–22.9) | 0.68 | 3* | 3* | 4 | 3 | 2 | No |
| Theta † | 14.7 (8.8–22.0) | 0.52 | 5* | 5 | 2* | 6 | 2 | No |

#### C. Meses de El Niño costero (lista oficial IGP/ENFEN, no ex ante)

**sutil** — n marcados: 12; de los 12 meses marcados, 4 son shock MoM P75 ex post (de 10).

| modelo | MAE (IC95) | MASE | posición |
|---|---|---|---|
| Naive | 5,147 (4,347–5,953) | 0.90 | 7 |
| Seasonal Naive | 7,568 (5,055–9,884) | 1.32 | 8 |
| Chronos | 3,547 (2,352–4,772) | 0.62 | 4* |
| SARIMA | 3,328 (2,168–4,483) | 0.58 | 1* |
| SARIMA-sel | 3,723 (2,249–5,418) | 0.65 | 5* |
| Ridge | 11,881 (7,797–16,290) | 2.07 | 12 |
| ElasticNet | 11,692 (8,146–15,449) | 2.04 | 11 |
| XGB-37 | 4,682 (3,466–5,862) | 0.82 | 6* |
| GC3 | 8,394 (6,838–10,012) | 1.48 | 10 |
| GE | 7,714 (6,285–9,227) | 1.36 | 9 |
| ETS † | 3,542 (2,466–4,609) | 0.62 | 3* |
| Theta † | 3,347 (2,495–4,175) | 0.58 | 2* |

**dulce** — n marcados: 12; de los 12 meses marcados, 3 son shock MoM P75 ex post (de 15).

| modelo | MAE (IC95) | MASE | posición |
|---|---|---|---|
| Naive | 78.1 (54.6–104.3) | 3.02 | 12 |
| Seasonal Naive | 14.8 (10.0–19.6) | 0.57 | 1* |
| Chronos | 32.5 (22.7–42.4) | 1.26 | 6 |
| SARIMA | 18.9 (13.1–24.6) | 0.73 | 4 |
| SARIMA-sel | 18.0 (12.3–23.6) | 0.69 | 3* |
| Ridge | 51.6 (33.4–75.4) | 1.99 | 10 |
| ElasticNet | 51.9 (33.9–74.9) | 2.00 | 11 |
| XGB-37 | 45.3 (25.1–66.4) | 1.75 | 9 |
| GC3 | 37.1 (27.2–48.6) | 1.43 | 7 |
| GE | 41.6 (31.2–53.6) | 1.60 | 8 |
| ETS † | 17.8 (11.4–24.9) | 0.69 | 2* |
| Theta † | 27.9 (18.5–37.4) | 1.07 | 5 |

**Lectura:**
- **Coincidencia con los shocks ex post** (MoM P75):
  - en dulce, las definiciones A y B marcan casi los mismos meses (13 de 18 y 14 de 16);
  - en sutil coinciden poco (3 de 11 y 3 de 10).
- **Modelos robustos con definición ex ante:**
  - sutil: Chronos (A y B), ETS y Theta (A), SARIMA-sel (B) y Theta (B);
  - dulce: SARIMA (A y B), SARIMA-sel (A y B) y Theta (A).
- **GC3, GE y los tabulares no son robustos con ninguna definición.** El mensaje del artículo se mantiene: con una
  definición que no usa y_t, los modelos estadísticos y Chronos siguen arriba y las redes no.
- **Advertencia sobre B:** es en parte circular para SARIMA, porque marca los meses donde el propio SARIMA anticipa
  un cambio grande.
- **P90:** marca solo 1–2 meses por cultivo, así que esa columna discrimina poco.
- **El Niño costero 2023-03..2024-02** (12 meses; definición contemporánea, no ex ante):
  - en sutil, primero SARIMA (3,328 t), empatado con Theta, ETS, Chronos, SARIMA-sel y XGB-37;
  - en dulce, primero Seasonal Naive (14.8 t), empatado con ETS y SARIMA-sel.

### T9 — Horizonte h = 2 (obs. 14)

#### T9 — Horizonte h = 2 (pool 2021–2025; 10 modelos sin redes)

* = primero o empatado con el primero. «Robusto» = primero o empatado en ≥ 3 de P50, P60, P75 y P90 (MoM). MAE h = 1: el del artículo / T1 (Día 1), como referencia.

**sutil** (60 meses; 10 de shock MoM P75)

| modelo | MAE h2 todos (IC95) | pos. | MAE h1 todos | MAE h2 shock MoM P75 (IC95) | pos. shock | MAE h1 shock | 1º/empate MoM (de 4) | robusto |
|---|---|---|---|---|---|---|---|---|
| Naive | 6,734 (5,620–7,882) | 10 | 3,624 | 11,148 (9,219–12,690) | 10 | 8,506 | 0 | No |
| Seasonal Naive | 6,075 (5,156–6,987) | 9 | 6,075 | 5,034 (2,259–7,928) | 4* | 5,034 | 3 | Sí |
| Chronos | 3,669 (3,114–4,263) | 1* | 2,649 | 4,739 (3,650–5,698) | 3* | 4,784 | 4 | Sí |
| SARIMA | 4,766 (4,015–5,500) | 4 | 3,361 | 5,866 (4,336–7,388) | 6 | 5,131 | 3 | Sí |
| SARIMA-sel | 4,814 (4,038–5,601) | 5 | 3,206 | 6,409 (4,101–8,980) | 7* | 4,936 | 4 | Sí |
| Ridge | 5,790 (4,460–7,197) | 7 | 4,925 | 6,934 (4,666–9,232) | 9* | 8,557 | 1 | No |
| ElasticNet | 5,530 (4,237–6,857) | 6 | 4,872 | 5,581 (3,123–8,581) | 5* | 8,154 | 3 | Sí |
| XGB-37 | 5,802 (4,871–6,748) | 8 | 4,881 | 6,665 (4,310–9,259) | 8* | 5,955 | 3 | Sí |
| ETS † | 3,910 (3,273–4,563) | 2* | 2,939 | 4,662 (2,590–6,753) | 2* | 4,766 | 4 | Sí |
| Theta † | 4,256 (3,567–4,957) | 3* | 3,022 | 4,265 (2,562–6,416) | 1* | 4,767 | 4 | Sí |

**dulce** (60 meses; 15 de shock MoM P75)

| modelo | MAE h2 todos (IC95) | pos. | MAE h1 todos | MAE h2 shock MoM P75 (IC95) | pos. shock | MAE h1 shock | 1º/empate MoM (de 4) | robusto |
|---|---|---|---|---|---|---|---|---|
| Naive | 142.8 (121.5–164.2) | 10 | 77.5 | 199.3 (160.1–239.1) | 10 | 131.6 | 0 | No |
| Seasonal Naive | 24.5 (20.5–29.0) | 3 | 24.5 | 24.5 (21.4–27.8) | 4 | 24.5 | 0 | No |
| Chronos | 35.7 (28.6–43.2) | 5 | 30.8 | 54.1 (41.7–66.7) | 6 | 48.2 | 0 | No |
| SARIMA | 19.0 (15.2–23.4) | 1* | 18.4 | 15.1 (12.0–18.2) | 1* | 14.0 | 4 | Sí |
| SARIMA-sel | 21.4 (16.8–26.4) | 2* | 20.6 | 21.3 (15.3–26.6) | 2 | 19.7 | 2 | No |
| Ridge | 73.3 (63.2–83.9) | 9 | 53.1 | 78.8 (62.3–95.9) | 8 | 69.7 | 0 | No |
| ElasticNet | 72.8 (62.9–83.3) | 8 | 50.2 | 80.7 (64.0–98.1) | 9 | 67.2 | 0 | No |
| XGB-37 | 51.1 (41.4–61.3) | 7 | 48.3 | 71.8 (57.5–86.2) | 7 | 65.8 | 0 | No |
| ETS † | 27.0 (23.0–31.3) | 4 | 22.3 | 23.0 (18.6–27.6) | 3 | 19.0 | 0 | No |
| Theta † | 36.7 (30.8–42.7) | 6 | 28.0 | 26.2 (18.1–35.1) | 5 | 18.2 | 0 | No |

**Lectura:**
- **Sutil:** con h = 2, en todos los meses todos los MAE suben salvo el de Seasonal Naive, que no usa y_(t−1). En
  shock MoM P75, en cambio, varios bajan (Chronos, ETS, Theta, Ridge y ElasticNet). El primer lugar en todos
  los meses es Chronos (3,669 t), empatado con ETS y Theta. En shock MoM P75 hay muchos empates, y 8 de 10 modelos
  son robustos, así que el ranking discrimina poco.
- **Dulce:** SARIMA es primero en todos los meses (19.0 t) y en shock (15.1 t), y es el único robusto, igual que en
  h = 1.
- **Naive:** es el que más empeora (su ventaja en h = 1 era copiar y_(t−1)).
- **Conclusión:** el ordenamiento entre familias de h = 1 se mantiene en h = 2.

### T10 — Evaluación probabilística (obs. 2, opcional)

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

**Lectura:**
- **Sutil:** Chronos tiene menor CRPS que SARIMA en todos los meses (−512 t, p = 0.005) y menor twCRPS (−155 t,
  p = 0.003). En meses de shock la diferencia no es significativa.
- **Dulce:** SARIMA es mejor que Chronos en CRPS y twCRPS, en todos los meses y en shock (p ≤ 0.005).
- **SARIMA-sel frente a SARIMA:** DM no da diferencias significativas. En dulce, en shock, el IC bootstrap de la
  diferencia sí excluye 0 (+2.9 t de CRPS_Q, +3.0 t de twCRPS_Q), pero el DM no (p ≈ 0.12–0.14).
- **Cobertura del intervalo 10–90 %:** entre 75 % y 85 % (nominal 80 %).
- **La lectura coincide con la puntual:** Chronos es mejor en sutil y SARIMA en dulce.
- **Aproximación con 9 cuantiles:** sobrestima el CRPS exacto de la normal en un 9 % aproximadamente (sutil SARIMA:
  2,577 frente a 2,355 t), pero se aplica igual a los tres modelos.

---

## 2. Decisiones tomadas y por qué

1. **T5:** la regla sigue el criterio del protocolo: el MAE de validación decide, y el AIC solo preselecciona y
   desempata. Es general, porque recibe el "ajuste final" de cada protocolo. Se aplicó también al protocolo original
   como control de que no cambia nada publicado.
2. **T6:** y_(T−12) obliga a descartar 5 pares de train (objetivos 2016-08..2016-12). Para no confundir ese efecto
   con el de la variable, se corrió además el modelo original con esas mismas filas («solo y12»). Todo lo demás es
   idéntico al protocolo: el código reproduce las predicciones congeladas antes de cambiar nada.
3. **T7.1:**
   - **Orden de columnas:** se eligió para que (c) sea exactamente E5, porque XGB depende del orden por
     `colsample_bytree`.
   - **Ridge:** reelige alpha en cada conjunto. Es la misma búsqueda del protocolo; un alpha fijo favorecería a un
     conjunto.
   - **XGB:** usa los parámetros oficiales; no tiene búsqueda.
4. **T7.2:** la versión reducida se fijó antes de correrla, porque 30 exógenas no son estimables con 42 meses de
   train. Se eligió la PC1 por bloque y solo el rezago 1, para tener 2 parámetros más. La PCA se ajusta solo con el
   train para que no haya fuga. La versión completa se reporta igualmente, como se pidió.
5. **T8:**
   - **Umbrales:** con la historia hasta el origen, como las máscaras del artículo. Esa información es conocida
     ex ante, y así las definiciones son comparables con la del artículo.
   - **Definición B:** se descartan los 13 primeros pronósticos dentro del train, porque con d = 1 y D = 1 dependen
     de la inicialización difusa.
   - **Definición C:** se usó la lista oficial de eventos (descargable). Se declara como no ex ante.
6. **T9:**
   - **Tabulares:** estrategia directa (X_(t−2) → y_t), porque los predictores exógenos no se pueden pronosticar
     recursivamente sin un modelo para ellos. La fila t−2 solo contiene información hasta t−2, y `pares_h` lo
     verifica par a par.
   - **Modelos de series:** mantienen sus parámetros de train y el estado avanza hasta t−2.
7. **T10:** las tres distribuciones se comparan con los mismos 9 cuantiles, porque Chronos-Bolt solo entrega esos
   niveles y así ningún modelo tiene ventaja por la representación. El peso del twCRPS usa el umbral P75 del cambio
   mensual, que es conocido en el origen, centrado en y_(t−1): es la definición de "cambio grande" del artículo,
   trasladada a la distribución predictiva.
8. **Mejor modelo:** el de menor MAE en todos los meses entre los 10 del artículo. En el Día 1 (T1) la referencia de
   DM en dulce era SARIMA-sel, por seguir a G7. Aquí se usa SARIMA, que es el de menor MAE.
9. **Carga de Chronos:** con la revisión fijada (`r2lib.ChronosFijo`). La clase del pipeline no pasa la revisión y,
   sin red, no encuentra los pesos; `12_revision_g7` hace lo mismo.

## 3. Resultado de `reproduce.py --no-figures`

Ejecutado con `venv\Scripts\python.exe`:

```
[OK] integrity: SHA-256 of official code, frozen data and Chronos (hashes_congelados.json) (0 s)
[OK] leakage test, backtesting (test_fuga.py) (11 s)
[OK] leakage test, diagnostic experiments (test_fuga_g7.py) (86 s)
[OK] phase D1: metrics, bootstrap, Diebold-Mariano, threshold sweep (run_all.py --fase D1) (32 s)
[OK] diagnostic experiments (G7): evaluation T1-T10 (evaluar.py) (11 s)
[OK] first-round diagnostic tables (09_reportes/revision_g7/fase1, g7_fase1.py): regenerate and compare cell by cell (6 s)
[OK] review R2 (13_revision_r2): ETS and Theta, rolling origin 2021-2025 (t1_ets_theta.py) (22 s)
[OK] review R2 (13_revision_r2): ETS/Theta metrics, 12-model ranking and 2025-only ranking (t1_t2_evaluar.py) (5 s)
[OK] review R2 (13_revision_r2): SARIMA constant, no-constant sensitivity and SARIMA-sel fallback rule (t3_sarima.py) (11 s)
[OK] review R2 (13_revision_r2): predictor lags, fig20 content and Seasonal Naive check (t4_verificaciones.py) (8 s)
[OK] review R2 (13_revision_r2): SARIMA-sel fallback rule by validation MAE (E1) (t5_respaldo_sarima_sel.py) (15 s)
[OK] review R2 (13_revision_r2): E5 (y_t-12 in tabular models) and block ablation (t6_t7_tabulares.py) (83 s)
[OK] review R2 (13_revision_r2): SARIMAX with lagged exogenous variables (t7_sarimax.py) (71 s)
[OK] review R2 (13_revision_r2): ex-ante large-change months and El Nino costero months (t8_ex_ante.py) (3 s)
[OK] review R2 (13_revision_r2): two-step-ahead horizon (t9_h2.py) (96 s)
[OK] review R2 (13_revision_r2): CRPS and threshold-weighted CRPS (t10_crps.py) (12 s)
Compared 2231 files (93 regenerated by this run): {'IDENTICAL': 2231}; max |difference| = 0. Report: reproduction_report.json
09_reportes/revision_g7/fase1: 15 of 15 tables identical cell by cell.
```

- Los 6 pasos nuevos (T5–T10) corren después de los existentes y de los 4 del Día 1.
- Los CSV de `resultados/` son idénticos, byte a byte, a los de las corridas previas. Solo cambiaron dos `.md`
  (`tablas_T5.md` y `tablas_T7_sarimax.md`), por una corrección de formato de `n` aplicada antes de esta corrida.
- El paso de integridad da OK: no se modificó ningún archivo congelado.

## 4. Lo que no se pudo hacer o quedó limitado

- **Alertas del ENFEN (T8.3):**
  - no se usaron los comunicados oficiales de alerta, que solo están en PDF, comunicado por comunicado;
  - la definición C usa la lista de eventos basada en el ICEN, que es retrospectiva y no ex ante;
  - la propia página del IGP advierte que, desde 2015, la declaración operativa del ENFEN tiene prelación sobre la
    lista.
- **Redes en h = 2 (T9):** GC3 y GE no se evaluaron (habría que reentrenarlas), como estaba previsto.
- **Colas en T10:** solo hay 9 cuantiles (0.1–0.9). Las colas fuera del intervalo 10–90 % no se representan, así que
  el CRPS y el twCRPS son aproximaciones, para los tres modelos por igual.
- **Circularidad en T8 (definición B):** es parcialmente circular para SARIMA (ver la lectura de T8).
- **Tiempo de ejecución:** la primera corrida de `t6_t7_tabulares.py` tardó unas 20 h de reloj, del 13-nov 16:50 al
  14-nov 13:09. Medido por unidad, el cálculo es de segundos (Ridge 0.4 s, ElasticNet 0.1 s, XGB 2.0 s con
  10 semillas), así que el equipo probablemente estuvo suspendido. En `reproduce.py` el paso tarda 83 s.
- **Git:** no se hizo ninguna operación git.
