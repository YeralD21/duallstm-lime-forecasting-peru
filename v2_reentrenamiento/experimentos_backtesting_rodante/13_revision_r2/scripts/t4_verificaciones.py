"""R2-T4 (obs. 3 y 10): verificaciones leidas del codigo y de los CSV; no reentrena nada.

1. Predictores de Ridge, ElasticNet y XGB-37 (37) con indice explicito respecto del mes objetivo T, y entradas de
   GC3/GE (ventana de 6 meses). Se comprueba con los datos (no solo con los nombres) que cada columna es el valor
   que se declara: y_{T-12} en tabulares y en la red.
2. fig20_real_vs_pred_2025_{sutil,dulce}: modelos y lineas que contiene realmente (CSV de datos de la figura) y
   posicion en el paquete del articulo (02_scripts/12_paquete_overleaf.py), frente a la version reducida "main".
3. Seasonal Naive en limon dulce: MAE en todos los meses, normales y de shock (MoM P75) con mas decimales;
   comprobacion de la asignacion de meses (prediccion = y_{t-12}; mascaras = 03_ventanas publicadas).

Salidas en 13_revision_r2/resultados/T4_*.csv y T4_resumen.json.
Uso: python 13_revision_r2/scripts/t4_verificaciones.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import r2lib as R  # noqa: E402
from lib.entorno import preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import ast  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from lib import evaluacion as ev  # noqa: E402
from lib.datos import ConstructorDatosVentana  # noqa: E402
from lib.preparacion import pares_tabulares, secuencias  # noqa: E402
from lib.ventanas import Ventana  # noqa: E402
from v2_reentrenamiento.src.models.features_gc2_xgboost import gc2_predictors  # noqa: E402
from v2_reentrenamiento.src.models.features_gc3_ge import build_feature_spec  # noqa: E402
from v2_reentrenamiento.src.training.config_gc3_ge import OFFICIAL_TRAINING_CONFIG as CFG  # noqa: E402

resumen = {}


def guardar(df, nombre):
    R.escribir(df, R.RES / nombre)
    print("escrito", nombre, df.shape)


def per(f: str, k: int) -> str:
    return str(pd.Period(f, "M") - k)


# ----------------------------------------------------------------------------- 1. predictores
datos = ConstructorDatosVentana()
filas = []
for c in R.CULTIVARES:
    y = f"produccion_t_{c}"
    feats = datos.features(c, 2023)  # ventana 2025 (sin escalar: Ridge/EN lo estandarizan despues; XGB usa el escalado)
    maestro = datos.maestro(c, 2023)
    clave_m = maestro["año"].astype(int).astype(str) + "-" + maestro["mes"].astype(int).map("{:02d}".format)
    mae = maestro.set_index(clave_m)
    p = pares_tabulares(feats, gc2_predictors(c), y, Ventana(2025))
    q = p["test"]
    for j, nombre in enumerate(gc2_predictors(c)):
        if nombre == y:
            var, k = "y", 0
        elif nombre.startswith(y + "_lag"):
            var, k = "y", int(nombre.rsplit("lag", 1)[1])
        elif nombre in ("mes_sin", "mes_cos", "t_index"):
            var, k = nombre, 0
        else:
            var, k = nombre.rsplit("_lag", 1)[0], int(nombre.rsplit("lag", 1)[1])
        rezago = 1 + k  # X de la fila t predice y_{t+1}: la columna con rezago k de la fila t es el valor en T-1-k
        # comprobacion con los datos en los 12 meses de test de 2025
        ok = []
        for i, T in enumerate(f"{t:%Y-%m}" for t in q.fechas_objetivo):
            fuente = per(T, rezago)
            if var == "y":
                esperado = mae.loc[fuente, y]
            elif var == "mes_sin":
                esperado = np.sin(2 * np.pi * int(fuente[5:]) / 12)
            elif var == "mes_cos":
                esperado = np.cos(2 * np.pi * int(fuente[5:]) / 12)
            elif var == "t_index":
                esperado = 12 * (int(fuente[:4]) - 2016) + int(fuente[5:]) - 1 - 6
            else:
                esperado = mae.loc[fuente, var]
            ok.append(bool(np.isclose(q.X[i, j], esperado, rtol=0, atol=1e-9)))
        filas.append({"cultivo": c, "modelo": "Ridge / ElasticNet / XGB-37", "n": j + 1, "columna": nombre,
                      "valor_usado": ("y" if var == "y" else var) + f"_(T-{rezago})", "rezago_respecto_de_T": rezago,
                      "verificado_con_datos_test_2025": all(ok)})
TAB = pd.DataFrame(filas)
if not TAB.verificado_con_datos_test_2025.all():
    raise AssertionError("Algun predictor no coincide con el valor declarado")
guardar(TAB, "T4_1_predictores_tabulares.csv")
resumen["tabulares_n_predictores"] = int(TAB.groupby("cultivo").size().iloc[0])
resumen["tabulares_rezagos_de_y"] = sorted(TAB[TAB.valor_usado.str.startswith("y_")].rezago_respecto_de_T.unique().tolist())
resumen["tabulares_y_T_menos_12"] = bool((TAB.valor_usado.str.startswith("y_") & (TAB.rezago_respecto_de_T == 12)).any())
resumen["tabulares_rezago_maximo_cualquier_variable"] = int(TAB.rezago_respecto_de_T.max())

filas = []
for c in R.CULTIVARES:
    y = f"produccion_t_{c}"
    s = datos.serie(c)
    feats = datos.features(c, 2023)
    for red in ("GC3", "GE"):
        spec = build_feature_spec(c, red)
        p = secuencias(feats, spec.rama_a, spec.rama_b, y, Ventana(2025), lookback=CFG.lookback)
        q = p["test"]
        rezagos = set()
        for i, T in enumerate(f"{t:%Y-%m}" for t in q.fechas_objetivo):
            for paso in range(CFG.lookback):  # fila paso -> mes T - (lookback - paso)
                fila_mes = CFG.lookback - paso
                for j, nombre in enumerate(spec.rama_a):
                    k = 0 if nombre == y else int(nombre.rsplit("lag", 1)[1])
                    rezago = fila_mes + k
                    if not np.isclose(q.X_a[i, paso, j], s[per(T, rezago)], rtol=0, atol=1e-9):
                        raise AssertionError(f"{red} {c}: rama A {nombre} paso {paso} no es y_(T-{rezago})")
                    rezagos.add(rezago)
        for paso in range(CFG.lookback):
            fila_mes = CFG.lookback - paso
            for nombre in spec.rama_a:
                k = 0 if nombre == y else int(nombre.rsplit("lag", 1)[1])
                filas.append({"cultivo": c, "red": red, "rama": "A", "paso_secuencia": paso + 1, "fila_mes": f"T-{fila_mes}",
                              "columna": nombre, "valor_usado": f"y_(T-{fila_mes + k})", "rezago_respecto_de_T": fila_mes + k})
        exo = sorted({int(n.rsplit("lag", 1)[1]) for n in spec.rama_b if "_lag" in n})
        resumen[f"{red}_{c}"] = {"lookback": CFG.lookback, "rama_A": list(spec.rama_a), "rezagos_y_rama_A": sorted(rezagos),
                                 "y_T_menos_12_en_rama_A": 12 in rezagos, "n_entradas_rama_B": len(spec.rama_b),
                                 "rezagos_columna_exogenas_rama_B": exo,
                                 "rango_meses_exogenas_rama_B": f"T-{1 + min(exo)} .. T-{CFG.lookback + max(exo)}",
                                 "y_en_rama_B": any(n.startswith(y) for n in spec.rama_b)}
guardar(pd.DataFrame(filas), "T4_1_entradas_rama_A_lstm.csv")

# ----------------------------------------------------------------------------- 2. fig20
G = ev.BR / "08_graficos" / "predicciones"
filas = []
for c in R.CULTIVARES:
    for version, f in (("fig20 (paquete del artículo)", f"fig20_real_vs_pred_2025_{c}.csv"),
                       ("fig20 main (reducida, 14_fig20_reducida_2025.py)", f"fig20_real_vs_pred_2025_main_{c}.csv")):
        d = pd.read_csv(G / f)
        for m, g in d.groupby("modelo", sort=False):
            n_lineas = g.semilla.nunique() if "semilla" in g and g.semilla.notna().any() else 1
            filas.append({"cultivo": c, "version": version, "archivo": f, "modelo": m, "n_lineas": int(n_lineas),
                          "promedio_de_semillas": bool("n_semillas_promediadas" in g and (g.n_semillas_promediadas > 1).any()),
                          "n_meses": int(g.fecha.nunique())})
F20 = pd.DataFrame(filas)
guardar(F20, "T4_2_fig20_contenido.csv")
txt = (ev.BR / "02_scripts" / "12_paquete_overleaf.py").read_text(encoding="utf-8")
principal = ast.literal_eval(re.search(r"PRINCIPAL = (\[.*?\n\])", txt, flags=re.S).group(1))
pos = [i + 1 for i, t in enumerate(principal) if any("fig20_real_vs_pred_2025" in x for x in t)]
resumen["fig20_en_paquete"] = {"posicion_en_PRINCIPAL": pos, "n_figuras_PRINCIPAL": len(principal),
                               "entrada": [list(principal[i - 1]) for i in pos],
                               "main_en_paquete": any("_main_" in x for t in principal for x in t)}
resumen["fig20_pie_txt"] = {c: (G / f"fig20_real_vs_pred_2025_{c}.txt").read_text(encoding="utf-8").splitlines()[0] for c in R.CULTIVARES}

# ----------------------------------------------------------------------------- 3. Seasonal Naive, dulce
S = ev.series()
pred = pd.read_csv(ev.BR / "05_predicciones" / "predicciones_consolidadas.csv", dtype={"fecha": str})
sn = pred[(pred.modelo == "Seasonal Naive") & (pred.cultivar == "dulce") & (pred.particion == "test") & pred.anio_test.isin(R.VENTANAS)]
sn = sn.assign(y_t_menos_12=[S["dulce"][per(f, 12)] for f in sn.fecha], y_canon=[S["dulce"][f] for f in sn.fecha])
asig_ok = bool(np.allclose(sn.y_pred, sn.y_t_menos_12, rtol=0, atol=1e-9) and np.allclose(sn.y_true, sn.y_canon, rtol=0, atol=1e-6))
mas = pd.read_csv(ev.BR / "03_ventanas" / "umbrales_y_mascaras.csv")
mas = mas[(mas.cultivar == "dulce") & (mas.tipo == "mensual") & (mas.percentil == 75) & mas.anio_test.isin(R.VENTANAS)]
pub = {m for x in mas.meses_shock.dropna() for m in str(x).split(";") if m}
M = ev.mascaras(S, R.VENTANAS, [75])
rec = {m for a in R.VENTANAS for m in M[("dulce", a, "mensual", 75)]}
sn = sn.assign(ae=(sn.y_pred - sn.y_true).abs(), shock=sn.fecha.isin(pub)).sort_values("fecha")
res3 = {"prediccion_es_y_t_menos_12_en_60_meses": asig_ok, "mascara_publicada_igual_a_recalculada": pub == rec,
        "n_meses": len(sn), "n_shock": int(sn.shock.sum()),
        "MAE_todos": float(sn.ae.mean()), "MAE_shock": float(sn.ae[sn.shock].mean()), "MAE_normal": float(sn.ae[~sn.shock].mean()),
        "Delta_s_pct": float((sn.ae[sn.shock].mean() - sn.ae.mean()) / sn.ae.mean() * 100),
        "suma_ae_shock": float(sn.ae[sn.shock].sum()), "suma_ae_normal": float(sn.ae[~sn.shock].sum())}
# control: si las mascaras estuvieran desplazadas un mes, el MAE de shock cambiaria
for d in (-1, 1):
    desp = {per(m, -d) for m in pub}
    res3[f"MAE_shock_mascara_desplazada_{d:+d}_mes"] = float(sn.ae[sn.fecha.isin(desp)].mean())
res3["MAE_shock_otros_modelos"] = {}
err = pd.read_csv(ev.BR / "05_predicciones" / "errores_test_promediados_semillas.csv", dtype={"fecha": str})
for m in ("Naive", "SARIMA", "Chronos"):
    e = err[(err.modelo == m) & (err.cultivar == "dulce") & err.anio_test.isin(R.VENTANAS)]
    res3["MAE_shock_otros_modelos"][m] = {"MAE_todos": float(e.ae.mean()), "MAE_shock": float(e.ae[e.fecha.isin(pub)].mean())}
resumen["seasonal_naive_dulce"] = res3
guardar(sn[["anio_test", "fecha", "y_true", "y_pred", "y_t_menos_12", "ae", "shock"]], "T4_3_seasonal_naive_dulce_meses.csv")
R.escribir_json(resumen, R.RES / "T4_resumen.json")
print(json.dumps(resumen, indent=1, ensure_ascii=False, default=str))
