"""Etapa 09b (Fase D1): arma 09_reportes/reporte_fase_D1.md con TODAS las tablas en texto, sin recortar filas.

Contenido, en orden:
  1. indice con la ruta de cada CSV y de cada .tex (vistas de 08/09, comprobacion de 2025, CSV completos y datos);
  2. texto del reporte (09_reportes/reporte_fase_D1_narrativa.md, escrito a mano);
  3. comprobacion de 2025 frente a resultados_v2_final (resumen y por corrida);
  4. todas las vistas que generan 08_metricas.py y 09_barrido_umbral.py (incluidas las que no salen en el .md resumido);
  5. anexo: cada CSV completo (formato largo), todas sus filas.
No calcula nada: solo lee lo que ya escribieron las etapas anteriores.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.entorno import BR, preparar_entorno  # noqa: E402

preparar_entorno()

import json  # noqa: E402

import pandas as pd  # noqa: E402

from lib.evaluacion import a_texto  # noqa: E402

REP = BR / "09_reportes"
REPRO = "06_metricas/reproducibilidad"
COMPLETOS = [  # (ruta relativa a la carpeta del experimento, descripcion)
    ("06_metricas/por_ventana/T05_metricas_por_ventana.csv", "T05 completa: modelo × cultivo × ventana × tipo × percentil de reporte"),
    ("06_metricas/agregadas/T06_agregadas_IC.csv", "T06 completa: agregadas con IC iid y por bloques, ambos conjuntos, P50/P60/P75/P90, mensual e interanual"),
    ("06_metricas/agregadas/T08_ranking_empates.csv", "T08 completa: ranking, diferencia con el mejor e indicador 'primero' (iid y bloques)"),
    ("06_metricas/significancia/T09_diebold_mariano_hln.csv", "T09 completa: DM-HLN por pares, con Holm exploratorio"),
    ("06_metricas/por_semilla/T07_metricas_por_semilla.csv", "T07 completa: métricas por semilla, por ventana y agregadas (P75 mensual)"),
    ("06_metricas/ablacion_nlp/T11_ablacion_GE_menos_GC3.csv", "T11 completa: ablación GE − GC3 con la diferencia de cada semilla"),
    ("06_metricas/agregadas/T12_delta_s_quitando_un_shock.csv", "T12 completa: Δs quitando un mes de shock, por ventana y agregado"),
    ("06_metricas/agregadas/T13_mae_por_cuartil_cambio.csv", "T13 completa: MAE por cuartiles y tercios de |Δy/y|"),
    ("06_metricas/por_semilla/T15_diagnostico_ajuste.csv", "T15 completa: diagnóstico D-BR8 por corrida, con mejor época"),
    ("06_metricas/por_ventana/T20_sarima_sel_candidatos.csv", "T20 candidatos: los 5 candidatos por AIC de SARIMA-sel en cada ventana"),
    ("06_metricas/descripcion_series/T03_descripcion_particiones.csv", "T03 completa: descripción por partición, 2018–2025"),
    ("06_metricas/descripcion_series/T04_acf_adf_kpss_train.csv", "T04 completa: ACF, ADF y KPSS (estadísticos, p y retardos)"),
    ("07_barrido_umbral/mensual/barrido_por_modelo.csv", "Barrido mensual completo: modelo × percentil"),
    ("07_barrido_umbral/interanual/barrido_por_modelo.csv", "Barrido interanual completo: modelo × percentil"),
    ("07_barrido_umbral/mensual/n_shock_por_ventana.csv", "n_shock por ventana y percentil (mensual)"),
    ("07_barrido_umbral/interanual/n_shock_por_ventana.csv", "n_shock por ventana y percentil (interanual)"),
    ("07_barrido_umbral/estabilizacion.csv", "Estabilización del ranking"),
    ("07_barrido_umbral/comprobacion_P0.csv", "Comprobación de P0: las 240 comprobaciones"),
]
DATOS = [  # archivos de datos que no son tablas de resultados (se indexan pero no se imprimen)
    ("05_predicciones/predicciones_consolidadas.csv", "Predicciones de todas las particiones y semillas (Fase C), consolidadas"),
    ("05_predicciones/errores_test_promediados_semillas.csv", "Error absoluto de test promediado entre semillas (D-BR6), base de todas las métricas"),
    (f"{REPRO}/metricas_2025_vs_oficial.json", "Comprobación de 2025: veredictos, máscaras y SHA-256 de los archivos oficiales"),
    ("07_barrido_umbral/comprobacion_P0.json", "Comprobación de P0: veredicto"),
]


def main() -> None:
    vistas = []
    for parte in ("08", "09"):
        vistas += json.loads((REP / f"tablas_fase_D1_{parte}.indice.json").read_text(encoding="utf-8"))
    eq_res = pd.read_csv(BR / REPRO / "metricas_2025_vs_oficial.csv")
    eq_run = pd.read_csv(BR / REPRO / "metricas_2025_vs_oficial_por_corrida.csv")
    eq_json = json.loads((BR / REPRO / "metricas_2025_vs_oficial.json").read_text(encoding="utf-8"))

    def existe(r: str) -> str:
        return r if (BR / r).exists() else f"{r} (NO EXISTE)"

    ind = ["## Índice de archivos", "",
           "Rutas relativas a `v2_reentrenamiento/experimentos_backtesting_rodante/`.", "",
           "### Vistas (texto en este reporte, CSV y LaTeX)", "", "| # | Tabla | CSV | LaTeX |", "|---|---|---|---|"]
    for i, v in enumerate(vistas, 1):
        ind.append(f"| {i} | {v['nombre']} | `{existe(v['csv'])}` | `{existe(v['tex'])}` |")
    ind += ["", "### Comprobación de 2025 (CSV; sin .tex)", "", "| Tabla | CSV |", "|---|---|",
            f"| Resumen por cultivo y modelo | `{existe(REPRO + '/metricas_2025_vs_oficial.csv')}` |",
            f"| Por corrida (62 filas: GC3, GE y XGB-37 × 10 semillas + SARIMA, por cultivo) | `{existe(REPRO + '/metricas_2025_vs_oficial_por_corrida.csv')}` |",
            "", "### Tablas completas en formato largo (anexo; CSV, sin .tex)", "", "| Tabla | CSV |", "|---|---|"]
    ind += [f"| {d} | `{existe(r)}` |" for r, d in COMPLETOS]
    ind += ["", "### Datos (indexados, no impresos)", "", "| Contenido | Archivo |", "|---|---|"]
    ind += [f"| {d} | `{existe(r)}` |" for r, d in DATOS]

    eq_cols = ["cultivar", "modelo", "n_corridas"] + [c for c in eq_res.columns if c.startswith("maxdif_")] + \
              ["max_dif_relativa", "OK_criterio_original_rel_1e-6", "OK"]
    eq = ["## Comprobación previa: ventana 2025 frente a `resultados_v2_final`", "",
          f"- Veredicto (criterio DESV-05): **{'OK' if eq_json['OK'] else 'FALLA'}**. Criterio original (relativa ≤ 1e-6 en todo): "
          f"**{'OK' if eq_json['OK_criterio_original'] else 'no se cumple'}**.",
          f"- Meses de shock oficiales 2025: {eq_json['meses_shock_oficiales_2025']}.",
          f"- Máscara P75 del backtesting 2025: {eq_json['mascara_P75_backtesting_2025']} (coincide: {eq_json['coincide_mascara']}).",
          f"- MAE del Naive t−1: {eq_json['MAE_Naive_t1']}.", "",
          "### Resumen por cultivo y modelo (diferencias máximas absolutas; métricas oficiales D35)", "",
          "Valores exactos (sin redondear; las diferencias son de 1e-16 a 1e-4, por eso no se redondean):", "", "```",
          eq_res[[c for c in eq_cols if c in eq_res.columns]].to_string(index=False), "```", "",
          "### Por corrida (nuevo y oficial)", "", a_texto(eq_run, 4), ""]

    tablas = ["## Tablas de resultados (vistas)", ""] + [v["texto"] for v in vistas]
    anexo = ["## Anexo: tablas completas en formato largo (todas las filas)", ""]
    for r, d in COMPLETOS:
        df = pd.read_csv(BR / r)
        anexo += [f"### {Path(r).name} — {d}", "", f"`{r}` — {len(df)} filas × {df.shape[1]} columnas.", "", a_texto(df, 3), ""]

    narrativa = (REP / "reporte_fase_D1_narrativa.md").read_text(encoding="utf-8")
    cab = ["# Reporte — Fase D1 (tablas y estadística, sin figuras)", "",
           "Generado por `02_scripts/09b_reporte_fase_D1.py` a partir de los CSV de la Fase D1. "
           "El texto del reporte está en `09_reportes/reporte_fase_D1_narrativa.md`. Las vistas redondean; los CSV tienen precisión completa.", ""]
    (REP / "reporte_fase_D1.md").write_text("\n".join(cab + ind + ["", narrativa, ""] + eq + tablas + anexo), encoding="utf-8")
    faltan = [r for r in [v["csv"] for v in vistas] + [v["tex"] for v in vistas] + [r for r, _ in COMPLETOS + DATOS] if not (BR / r).exists()]
    print(f"reporte_fase_D1.md: {len(vistas)} vistas, {len(COMPLETOS)} tablas completas; archivos que faltan: {faltan or 'ninguno'}")
    if faltan:
        raise SystemExit("Faltan archivos del indice.")


if __name__ == "__main__":
    main()
