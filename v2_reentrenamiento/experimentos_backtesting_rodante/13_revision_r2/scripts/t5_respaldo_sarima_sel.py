"""R2-T5 (obs. 11): regla de respaldo de SARIMA-sel coherente con el criterio de seleccion del protocolo.

POSTERIOR AL PROTOCOLO. Regla (r2lib.REGLA_RESPALDO, funcion general r2lib.elegir_con_respaldo): si el orden elegido por
MAE de validacion entre los 5 de menor AIC no converge en el ajuste final, se usa el siguiente con menor MAE de
validacion entre los que convergen. Se aplica a todas las ventanas de:
  - el protocolo original (ajuste final = ajuste en train con maxiter 500): control, no debe cambiar nada;
  - E1 / SARIMA-sel-Y1 (ajuste final = reajuste con datos hasta dic Y-1, mismo orden y opciones que 12_revision_g7).
Salidas: resultados/T5_*.csv y unidades_d2/SARIMA-sel-Y1-R/<cultivo>/<anio>/predicciones.csv.
Uso: python 13_revision_r2/scripts/t5_respaldo_sarima_sel.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import r2lib as R  # noqa: E402
from lib.entorno import preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import json  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

import r2eval as E  # noqa: E402
from lib.datos import ConstructorDatosVentana  # noqa: E402
from lib.modelos_series import _a_un_paso, _ajustar  # noqa: E402

BR = R.BR
HP = json.loads((BR / "01_configuracion" / "hiperparametros_congelados.json").read_text(encoding="utf-8"))["sarima_seleccion_por_ventana_DA9"]
OPC = {**HP["opciones_ajuste"], "maxiter": HP["maxiter_candidatos_y_final"]}
NOMBRE = "SARIMA-sel-Y1-R"   # SARIMA-sel-Y1 con la regla de respaldo
UNI = R.RES / "unidades_d2"


def ajustador(y):
    def f(o, so):
        fit, _ = _ajustar(y, o, so, OPC)
        return fit, bool(fit.mle_retvals.get("converged", False)) if isinstance(fit.mle_retvals, dict) else None
    return f


datos = ConstructorDatosVentana()
filas, preds = [], []
for c in R.CULTIVARES:
    s = datos.serie(c).sort_index().astype(float)
    for a in R.VENTANAS:
        i0 = json.loads((BR / "04_modelos" / "sarima_sel" / c / str(a) / "info.json").read_text(encoding="utf-8"))
        cand = pd.read_csv(BR / "04_modelos" / "sarima_sel" / c / str(a) / "candidatos.csv")
        meses = [f"{a}-{m:02d}" for m in range(1, 13)]
        # protocolo original (control)
        tr0 = s[(s.index >= "2016-07") & (s.index <= f"{a - 2}-12")].to_numpy()
        r0 = R.elegir_con_respaldo(cand, ajustador(tr0))
        if (r0["order"], r0["seasonal_order"]) != (i0["order"], i0["seasonal_order"]):
            raise AssertionError(f"La regla cambia el SARIMA-sel original de {c} {a}")
        # E1
        tr1 = s[(s.index >= "2016-07") & (s.index <= f"{a - 1}-12")].to_numpy()
        r1 = R.elegir_con_respaldo(cand, ajustador(tr1))
        fl, _ = _a_un_paso(r1["fit"], meses, [s[m] for m in meses])
        p = pd.DataFrame(fl).assign(modelo=NOMBRE, cultivar=c, anio_test=a, semilla=None, particion="test")
        pub = pd.read_csv(R.G7 / "resultados" / "unidades" / "SARIMA-sel-Y1" / c / str(a) / "predicciones.csv", dtype={"fecha": str})
        if not r1["respaldo_usado"] and not np.allclose(p.y_pred.to_numpy(), pub.y_pred.to_numpy(), rtol=0, atol=1e-6):
            raise AssertionError(f"Sin respaldo, {c} {a} deberia reproducir la unidad publicada de E1")
        R.escribir(p[E.COLS], UNI / NOMBRE / c / str(a) / "predicciones.csv")
        preds.append(p)
        filas.append({"cultivo": c, "anio_test": a, "orden_elegido_protocolo": f"{tuple(i0['order'])}{tuple(i0['seasonal_order'])}",
                      "posicion_aic_elegido": i0["posicion_aic_elegido"], "original_converge": r0["intentos"][0]["convergio"],
                      "original_respaldo_usado": r0["respaldo_usado"], "E1_respaldo_usado": r1["respaldo_usado"],
                      "E1_sin_convergencia": r1["sin_convergencia"],
                      "E1_orden_final": f"{tuple(r1['order'])}{tuple(r1['seasonal_order'])}", "E1_posicion_aic_final": r1["posicion_aic"],
                      "E1_intentos": json.dumps(r1["intentos"]),
                      "MAE_test_publicado_E1": float(np.mean(np.abs(pub.y_true - pub.y_pred))),
                      "MAE_test_regla_T5": float(np.mean(np.abs(p.y_true - p.y_pred)))})
T5 = pd.DataFrame(filas)
R.escribir(T5, R.RES / "T5_regla_respaldo_por_ventana.csv")
print(T5[["cultivo", "anio_test", "E1_respaldo_usado", "E1_orden_final", "MAE_test_publicado_E1", "MAE_test_regla_T5"]].to_string(index=False))

# ----------------------------------------------------------------------------- pool 2021-2025
g7 = []
for c in R.CULTIVARES:
    for a in R.VENTANAS:
        q = pd.read_csv(R.G7 / "resultados" / "unidades" / "SARIMA-sel-Y1" / c / str(a) / "predicciones.csv", dtype={"fecha": str})
        g7.append(q.assign(modelo="SARIMA-sel-Y1", cultivar=c, anio_test=a, semilla=None))
ES, ERR = E.errores(E.originales(), pd.concat(g7), pd.concat(preds))
filas = []
mods = ["SARIMA-sel", "SARIMA-sel-Y1", NOMBRE]
for c in R.CULTIVARES:
    pv, cl, est, Dv = E.matriz(ERR, mods + [E.MEJOR[c]], c)
    for alc, sub in (("todos", np.ones(len(cl), bool)), ("shock_MoM_P75", E.vec(cl, E.mascara_mom(c))),
                     ("shock_YoY_P75", E.vec(cl, E.mascara_mom(c, tipo="interanual")))):
        r = E.resumen(pv, est, Dv, sub, mods).set_index("modelo")
        for m in mods:
            k = E.dm(pv, m, E.MEJOR[c], sub)
            filas.append({"cultivo": c, "alcance": alc, "modelo": m, **r.loc[m].to_dict(), "mejor": E.MEJOR[c],
                          "MAE_mejor": float(pv[E.MEJOR[c]].to_numpy()[sub].mean()), "DM_HLN": k["HLN"], "DM_p": k["p"]})
T5P = pd.DataFrame(filas)
T5P["n_meses"] = T5P.n_meses.astype(int)
R.escribir(T5P, R.RES / "T5_SARIMA_sel_Y1_pool.csv")
vista = T5P.assign(**{"MAE (IC95)": [E.ic_txt(r.MAE, r.IC_lo, r.IC_hi, E.DEC[r.cultivo]) for r in T5P.itertuples()],
                      "DM vs mejor (HLN; p)": [f"{E.num(r.DM_HLN, 2)}; {E.num(r.DM_p, 3)}" for r in T5P.itertuples()]})
txt = ["<!-- generado por t5_respaldo_sarima_sel.py -->", "#### Por ventana (E1)", "",
       E.md(T5[["cultivo", "anio_test", "orden_elegido_protocolo", "E1_respaldo_usado", "E1_orden_final", "E1_posicion_aic_final"]]
            .assign(**{"MAE publicado E1": T5.MAE_test_publicado_E1.map(lambda v: E.num(v, 1)),
                       "MAE regla T5": T5.MAE_test_regla_T5.map(lambda v: E.num(v, 1))})),
       "", "#### Pool 2021–2025", "",
       E.md(vista[["cultivo", "alcance", "modelo", "n_meses", "MAE (IC95)", "mejor", "DM vs mejor (HLN; p)"]])]
(R.RES / "tablas_T5.md").write_text("\n".join(txt) + "\n", encoding="utf-8", newline="\n")
print(vista[["cultivo", "alcance", "modelo", "MAE (IC95)", "DM vs mejor (HLN; p)"]].to_string(index=False))
