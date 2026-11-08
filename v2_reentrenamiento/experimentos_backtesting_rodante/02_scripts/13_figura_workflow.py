"""Etapa 13: fig_workflow, diagrama del flujo de trabajo del estudio (diseño A: 5 bloques horizontales).

Sin resultados: los textos salen de la configuración y del código (ventanas.json, ventanas_viabilidad.csv, umbrales.json,
hiperparametros_congelados.json, lib/evaluacion.py, src/models/features_gc3_ge.py) y de D-BR1..D-BR5 y DESV-07.
Mismo estilo que fig25 y fig30 (01_configuracion/estilo_figuras.json). Salida: 08_graficos/figuras_independientes/
fig_workflow.{png,pdf,csv,txt}; el CSV guarda cada texto con su fuente. Se registra en indice_figuras_d3.csv.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.entorno import BR, preparar_entorno  # noqa: E402

preparar_entorno()

import csv  # noqa: E402
import io  # noqa: E402
import json  # noqa: E402

import pandas as pd  # noqa: E402

from lib.evaluacion import B, EXPLORATORIOS, MODELOS_RANKING, SIN_AJUSTE  # noqa: E402
from lib.figuras import COLORES, aplicar_estilo, guardar  # noqa: E402

aplicar_estilo()
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

CM = 1 / 2.54
W_PAG, H_FIG = 17 * CM, 7.6 * CM
SALIDA = BR / "08_graficos" / "figuras_independientes"
CFG = BR / "01_configuracion"
CITA_MIDAGRI = "MIDAGRI–SISAGRI (accessed [____])"  # igual que fig24, fig29 y TS1
BASE = "fig_workflow"


def leer_config() -> dict:
    from v2_reentrenamiento.src.models.features_gc3_ge import LAGS

    v = json.loads((CFG / "ventanas.json").read_text(encoding="utf-8"))
    u = json.loads((CFG / "umbrales.json").read_text(encoding="utf-8"))
    h = json.loads((CFG / "hiperparametros_congelados.json").read_text(encoding="utf-8"))
    via = pd.read_csv(BR / "03_ventanas" / "ventanas_viabilidad.csv")
    aplica = via[via.estado == "aplica"].groupby("anio_test").modelo.apply(set)
    solo_sin_ajuste = [a for a in v["anios_test"] if aplica[a] == set(SIN_AJUSTE)]
    semillas = h["semillas_estocasticas"]
    t7 = pd.read_csv(BR / "06_metricas" / "por_semilla" / "T07_metricas_por_semilla.csv", usecols=["modelo"])
    con_semilla = [m for m in MODELOS_RANKING if m in set(t7.modelo)]
    if len(MODELOS_RANKING) != 10 or "SARIMA-sel" not in MODELOS_RANKING:
        raise SystemExit("La lista de modelos del ranking no es la esperada (D-BR2)")
    if u["principal"] != 75 or list(u["puntos_reporte"]) != [50, 60, 75, 90]:
        raise SystemExit("Umbrales distintos de D-BR4")
    return dict(lags=LAGS, anios=v["anios_test"], ranking=v["ventanas_ranking"], sens=v["ventanas_sensibilidad_DA2"],
                inicio=v["inicio_serie"], excluido=v["anio_excluido"], min_train=v["minimo_train_meses"],
                solo_sin_ajuste=solo_sin_ajuste, semillas=semillas, con_semilla=con_semilla, umbrales=u)


def rango(a: list) -> str:
    return f"{min(a)}–{max(a)}"


def main() -> None:
    c = leer_config()
    ini_anio, fin_anio = int(c["inicio"][:4]), c["excluido"] - 1
    lags = ", ".join(map(str, c["lags"]))
    sem = f"{len(c['semillas'])} seeds ({min(c['semillas'])}–{max(c['semillas'])})"
    sin_aj = [m for m in MODELOS_RANKING if m in SIN_AJUSTE]
    resto = [m for m in MODELOS_RANKING if m not in SIN_AJUSTE]
    if resto[:4] != ["SARIMA", "SARIMA-sel", "Ridge", "ElasticNet"] or resto[4:] != c["con_semilla"]:
        raise SystemExit(f"Orden o grupos de modelos inesperados: {resto}, con semilla {c['con_semilla']}")
    # (bloque, título, [(texto, fuente, estilo)]); estilo "x" = caja discontinua del exploratorio
    bloques = [
        ("1", "Data", [
            (f"Monthly, {ini_anio}–{fin_anio}", "ventanas.json: inicio_serie, anio_excluido", ""),
            ("MIDAGRI–SISAGRI:\nlime production (t)","rutas_datos.json: produccion_nacional", ""),
            ("NASA POWER climate", "rutas_datos.json: nasa_provincial", ""),
            ("INDECI disasters", "rutas_datos.json: indeci_provincial; pie de fig25", ""),
            ("Agraria.pe news:\nsentiment\n(RoBERTuito)\nand news count","notebooks/fase2_features/01_nlp_sentimiento_ejecutado.ipynb; DESV-09 punto 3", ""),
        ]),
        ("2", "Preparation\nper window", [
            (f"Lags {lags}", "src/models/features_gc3_ge.py: LAGS", ""),
            ("Scaler and\ngeographic weights:\ntraining data only\n(to Dec Y−2)","D-BR3", ""),
            ("Shock threshold:\nhistory up to the\norigin (Dec Y−1)", "D-BR3; D-BR4; umbrales.json: historia_umbral", ""),
        ]),
        ("3", "Rolling-origin\nwindows", [
            ("Origin: Dec Y−1", "D-BR1; ventanas.json", ""),
            ("Train: to Dec Y−2\nValidation: Y−1\nTest: Y", "D-BR1; ventanas.json", ""),
            (f"Test years:\n{rango(c['anios'])}","ventanas.json: anios_test", ""),
            (f"{rango(c['solo_sin_ajuste'])}: Naive,\nSeasonal Naive,\nChronos only","03_ventanas/ventanas_viabilidad.csv; D-BR1 (mínimo 36 meses de train)", ""),
            (f"Ranking:\n{rango(c['ranking'])}\nSensitivity:\n{rango(c['sens'])}","ventanas.json: ventanas_ranking, ventanas_sensibilidad_DA2; D-BR1", ""),
        ]),
        ("4", f"Models ({len(MODELOS_RANKING)})", [
            (f"{sin_aj[0]},\n{sin_aj[1]},\n{sin_aj[2]} (zero-shot)","lib/evaluacion.py: MODELOS_RANKING, SIN_AJUSTE; D-BR2", ""),
            (f"{resto[0]}, {resto[1]}", "lib/evaluacion.py: MODELOS_RANKING; D-BR2, D-BR10", ""),
            (f"{resto[2]}, {resto[3]}", "lib/evaluacion.py: MODELOS_RANKING; D-BR2", ""),
            (f"{', '.join(c['con_semilla'])}:\n{sem}", "lib/evaluacion.py; hiperparametros_congelados.json: semillas_estocasticas; D-BR6", ""),
            (f"{EXPLORATORIOS[0]}\n(exploratory)","lib/evaluacion.py: EXPLORATORIOS; D-BR2", "x"),
        ]),
        ("5", "Evaluation", [
            ("MAE: all,\nshock and\nnormal months","D-BR5", ""),
            ("Δs (%)", "D-BR5", ""),
            ("Paired bootstrap\n95% CI", f"D-BR5; lib/evaluacion.py: B = {B}", ""),
            ("Diebold–Mariano\n(HLN)", "D-BR5", ""),
            ("Holm adjustment\n(exploratory)", "DESV-07", ""),
        ]),
    ]

    fig, ax = plt.subplots(figsize=(W_PAG, H_FIG))
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 40)
    ax.axis("off")
    rend = fig.canvas.get_renderer()

    def medir(t) -> tuple[float, float]:
        """Ancho y alto reales del texto en unidades de datos (medidos con el renderizador, no estimados)."""
        bb = t.get_window_extent(rend).transformed(ax.transData.inverted())
        return bb.width, bb.height

    FS_T, FS, INTER, GAP = 6.3, 5.6, 1.2, 1.5
    W, SEP, Y1 = 17.4, 3.25, 39.0
    PAD_X = 1.2  # margen horizontal mínimo entre el texto y el borde de la caja
    filas, fondos, cajas_x = [], [], []
    for i, (num, tit, items) in enumerate(bloques):
        x = i * (W + SEP)
        t = ax.text(x + W / 2, Y1 - 1.0, f"{num}  {tit}", ha="center", va="top", fontsize=FS_T, fontweight="bold", linespacing=1.1)
        y = Y1 - 1.0 - medir(t)[1] - 1.0
        ax.plot([x + 2.0, x + W - 2.0], [y, y], color="0.6", lw=0.4)
        y -= 1.2
        for k, (txt, fuente, est) in enumerate(items):
            expl = est == "x"
            color = COLORES[EXPLORATORIOS[0]] if expl else "black"
            if expl:
                y -= 0.5
            t = ax.text(x + W / 2, y, txt, ha="center", va="top", fontsize=FS, linespacing=INTER, color=color)
            w, h = medir(t)
            lim = W - 2 * PAD_X - (1.6 if expl else 0)
            if w > lim:
                raise SystemExit(f"Texto demasiado ancho en el bloque {num} ({w:.1f} > {lim:.1f}): {txt!r}")
            if expl:
                cajas_x.append(FancyBboxPatch((x + W / 2 - w / 2 - 0.9, y - h - 0.5), w + 1.8, h + 1.0,
                                              boxstyle="round,pad=0.1,rounding_size=0.6", fc="white", ec=color, lw=0.9, ls=(0, (3, 2))))
            filas.append({"bloque": f"{num} {tit.replace(chr(10), ' ')}", "orden": k + 1, "texto": txt.replace("\n", " "), "fuente": fuente})
            y -= h + GAP
        fondos.append(y)
    Y0 = min(fondos) - 0.2  # todas las cajas con la misma altura, ajustada al bloque más largo
    if Y0 < 0.5:
        raise SystemExit("El contenido no cabe en la altura de la figura")
    for i in range(len(bloques)):
        x = i * (W + SEP)
        ax.add_patch(FancyBboxPatch((x + 0.4, Y0), W - 0.8, Y1 - Y0, boxstyle="round,pad=0.25,rounding_size=0.8",
                                    fc="#F2F2F2" if i == 0 else "white", ec="black", lw=0.7, zorder=0))
        if i < len(bloques) - 1:
            ax.annotate("", xy=(x + W + SEP - 0.1, (Y0 + Y1) / 2), xytext=(x + W - 0.2, (Y0 + Y1) / 2),
                        arrowprops=dict(arrowstyle="-|>", lw=0.8, color="black", shrinkA=0, shrinkB=0))
    for p in cajas_x:
        ax.add_patch(p)
    ax.set_ylim(Y0 - 0.8, 40)  # sin franja vacía debajo de las cajas
    fig.set_size_inches(W_PAG, H_FIG * (40 - Y0 + 0.8) / 40)

    u = c["umbrales"]
    pie = (f"Study workflow. (1) Monthly data, {ini_anio}–{fin_anio}: national lime production ({CITA_MIDAGRI}), NASA POWER climate, "
           "INDECI disaster records and agricultural news from Agraria.pe, scored with the pysentimiento RoBERTuito sentiment model "
           f"(monthly mean sentiment and number of news items). (2) In each window, predictors enter with lags {lags.replace(', 6', ' and 6')} months; "
           "the scaler and the geographic weights are fitted on the training data only (up to December of Y−2), and the shock threshold "
           "is computed with the history up to the forecast origin (December of Y−1). (3) Rolling-origin evaluation with the origin in "
           f"December of Y−1: training up to December of Y−2, validation in year Y−1 and test in year Y, for test years {rango(c['anios'])}. "
           f"In {rango(c['solo_sin_ajuste'])} only Naive, Seasonal Naive and Chronos are run (trained models need at least {c['min_train']} "
           f"training months). The model ranking uses {rango(c['ranking'])}; {rango(c['sens'])} is a sensitivity set specified in the protocol. "
           f"(4) {len(MODELOS_RANKING)} models: {', '.join(MODELOS_RANKING[:-1])} and {MODELOS_RANKING[-1]}. {', '.join(c['con_semilla'][:-1])} and "
           f"{c['con_semilla'][-1]} are run with {sem}, and their monthly absolute errors are averaged over seeds. {EXPLORATORIOS[0]} (dashed) "
           "is an exploratory, post hoc model outside the ranking. (5) MAE over all, shock and normal months; "
           "Δs = (MAE_shock − MAE)/MAE × 100; paired bootstrap 95% confidence intervals (months resampled within windows, "
           f"B = {B:,}); Diebold–Mariano tests with the Harvey–Leybourne–Newbold correction. The Holm adjustment is exploratory. "
           f"Shock month (main definition): month-on-month change |y_t − y_(t−1)|/y_(t−1) above the {u['principal']}th percentile of the "
           "changes observed up to the forecast origin; the 50th, 60th and 90th percentiles and the year-on-year change are reported as "
           "sensitivity. No results are shown in this figure.")
    lec = ("Five stages from data to evaluation; every text is read from the configuration or the code (see the CSV, column 'fuente').\n"
           "Only XGB-43 and the Holm adjustment are exploratory; everything else follows the protocol.")
    datos = pd.DataFrame(filas)
    guardar(fig, SALIDA, BASE, datos, pie, lec)

    # índice: se añade una línea al final si no está (las filas existentes no se reescriben)
    idx = SALIDA / "indice_figuras_d3.csv"
    crudo = idx.read_bytes()
    fin = b"\r\n" if b"\r\n" in crudo else b"\n"
    fila = [BASE, "08_graficos/figuras_independientes", "What is the workflow of the study, from data to evaluation?",
            "01_configuracion/ventanas.json; 01_configuracion/umbrales.json; 01_configuracion/hiperparametros_congelados.json; "
            "03_ventanas/ventanas_viabilidad.csv; 02_scripts/lib/evaluacion.py; v2_reentrenamiento/src/models/features_gc3_ge.py"]
    if BASE not in set(pd.read_csv(idx).figura):
        buf = io.StringIO()
        csv.writer(buf, lineterminator=fin.decode()).writerow(fila)
        idx.write_bytes(crudo + (b"" if crudo.endswith(fin) else fin) + buf.getvalue().encode("utf-8"))
    print(json.dumps({"lineas_de_texto": len(datos), "indice_filas": len(pd.read_csv(idx))}, ensure_ascii=False))


if __name__ == "__main__":
    main()
