# 08_graficos — figuras de la Fase D2

Generadas por `02_scripts/10_figuras.py` **solo a partir de CSV ya guardados** (Fases C y D1); no se recalcula ninguna métrica ni máscara.
- 56 figuras (28 por cultivo): las 48 iniciales, más fig18 (ablación), fig19 en dos archivos (sin ajustar, y `fig19b_*_holm`, exploratoria) y fig18b (XGB-43 frente a XGB-37, exploratoria). Cada una tiene `figNN_*.png` (300 dpi), `.pdf` (vectorial), `.csv` (datos exactos que dibuja) y `.txt` (pie sugerido y lectura en dos líneas).
- Etiquetas en inglés, sin título dentro de la imagen, un archivo por cultivo, paleta Okabe-Ito con color y marcador fijos por modelo (`01_configuracion/estilo_figuras.json`).
- XGB-43 aparece solo en fig18b y, como caja exploratoria discontinua, en fig_workflow. No entra en el ranking, Diebold-Mariano ni Holm.
- Índice con la pregunta que responde cada figura y sus fuentes: `indice_figuras.csv`.

| Carpeta | Figuras |
|---|---|
| `sensibilidad_umbral/` | fig04 Δs, fig05 MAE_shock y fig06 razón contra percentil (P0–P95; P50, P60, P75 y P90 marcados); fig07 mapa de posiciones modelo × percentil (mensual e interanual); fig08 ranking entre umbrales; fig09 n_shock contra percentil; fig10 n_shock ventana × percentil; fig11 IC bootstrap de MAE_shock en P50, P60, P75 y P90; fig12 mensual contra interanual |
| `comparacion_modelos/` | fig13 MAE normal contra shock (P75) con IC; fig14 mapa MAE_shock modelo × ventana; fig15 cajas entre semillas; fig16 MAE por cuartil de \|Δy/y\|; fig17 Δs quitando un mes de shock; fig18 ablación GE − GC3 emparejada por semilla; fig18b XGB-43 − XGB-37 emparejada por semilla (exploratoria); fig19 matriz Diebold-Mariano-HLN sin ajustar y fig19b con Holm (exploratoria) |
| `diagnostico_ajuste/` | fig01 curvas de pérdida de GC3 y GE (una línea por semilla); fig02 brecha validación/train contra el Naive (con la advertencia de nivel en Sutil); fig03 mejor época por ventana |
| `predicciones/` | fig20 observado contra pronóstico por ventana (2021–2025), con los meses de shock P75 sombreados |
| `errores/` | fig21 error absoluto mes a mes (modelo × mes) |
| `figuras_independientes/` | vacía: fig24–fig28 no forman parte de la especificación de la Fase D2 |
| `paper_mdpi/` | `PROPUESTA_SELECCION.md`: propuesta, pendiente de aprobación (no se copió ninguna figura) |

Decisiones de implementación de las figuras: `09_reportes/DESVIACIONES.md` (DESV-08).
