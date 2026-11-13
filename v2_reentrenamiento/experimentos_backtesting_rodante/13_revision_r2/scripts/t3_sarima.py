"""R2-T3 (obs. 11): SARIMA, constante y no convergencia. POSTERIOR AL PROTOCOLO (diagnostico).

1. Constante (trend='c') del SARIMA fijo de limon sutil (1,1,1)(1,1,0)12: parametros en el train de cada ventana,
   media implicita de w_t = (1-L)(1-L^12) y_t y comprobacion numerica de que la constante produce, en niveles, una
   componente determinista cuadratica (ΔΔ12 de la diferencia de pronosticos con y sin constante -> media implicita).
2. Sensibilidad: el mismo SARIMA fijo de sutil SIN constante (trend='n'), mismo protocolo rolling; MAE en todos
   los meses y en shock MoM P75 (y YoY P75) frente al original, con IC bootstrap pareado de la diferencia.
3. Regla de respaldo para SARIMA-sel cuando el ajuste final no converge, aplicada a E1 (SARIMA-sel-Y1).

Salidas en 13_revision_r2/resultados/T3_*.csv y T3_resumen.json.
Uso: python 13_revision_r2/scripts/t3_sarima.py
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

from lib import evaluacion as ev  # noqa: E402
from lib.datos import ConstructorDatosVentana  # noqa: E402
from lib.modelos_series import _a_un_paso, _ajustar, _particiones, sarima_rolling  # noqa: E402
from lib.ventanas import Ventana  # noqa: E402

HP = json.loads((ev.BR / "01_configuracion" / "hiperparametros_congelados.json").read_text(encoding="utf-8"))
CFG = HP["sarima_congelado"]
SEL = HP["sarima_seleccion_por_ventana_DA9"]
POOL = list(R.VENTANAS)
S = ev.series()
M = ev.mascaras(S, POOL, [75])
ERR = pd.read_csv(ev.BR / "05_predicciones" / "errores_test_promediados_semillas.csv", dtype={"fecha": str})
ERR_G7 = pd.read_csv(R.G7 / "resultados" / "errores_test_promediados_semillas_g7.csv", dtype={"fecha": str})
resumen = {}


def guardar(df, nombre):
    R.escribir(df, R.RES / nombre)
    print("escrito", nombre, df.shape)


def mae_sub(ae: pd.Series, c: str, tipo: str | None) -> float:
    """ae indexado por (anio, fecha)."""
    if tipo is None:
        return float(ae.mean())
    sh = ev.vector_shock(list(ae.index), M, c, tipo, 75)
    return float(ae.to_numpy()[sh].mean())


def ic_dif(a: pd.Series, b: pd.Series, c: str, tipo: str | None) -> tuple[float, float]:
    claves = list(a.index)
    est = np.array([x for x, _ in claves])
    sub = np.ones(len(claves), bool) if tipo is None else ev.vector_shock(claves, M, c, tipo, 75)
    d = (a - b).to_numpy()
    idx = ev.indices_iid(est, sub, np.random.default_rng(ev.SEMILLA_BOOT))
    return ev.ic(d[idx].mean(axis=1))


# ----------------------------------------------------------------------------- 1. constante
c = "sutil"
s = ConstructorDatosVentana().serie(c).sort_index().astype(float)
o, so, op = CFG[c]["order"], CFG[c]["seasonal_order"], dict(CFG["opciones"])
filas = []
for a in POOL:
    _, train, _ = _particiones(s, Ventana(a))
    fit, avisos = _ajustar(train.to_numpy(), o, so, op)
    p = pd.Series(np.asarray(fit.params, float), index=fit.model.param_names)
    mu = p["intercept"] / ((1 - p["ar.L1"]) * (1 - p["ar.S.L12"]))
    w = (train - train.shift(1)) - (train.shift(12) - train.shift(13))
    # comprobacion numerica: mismos parametros con intercepto 0 -> diferencia de pronosticos a 240 pasos
    p0 = p.copy()
    p0["intercept"] = 0.0
    f_c = np.asarray(fit.forecast(240), float)
    f_0 = np.asarray(fit.model.filter(p0.to_numpy()).forecast(240), float)
    dif = f_c - f_0
    dd = (dif[13:] - dif[12:-1]) - (dif[1:-12] - dif[:-13])  # (1-L)(1-L^12) de la diferencia
    filas.append({"cultivo": c, "anio_test": a, "train": f"{train.index.min()}..{train.index.max()}", "n_train": len(train),
                  "intercepto_c": p["intercept"], "ar_L1": p["ar.L1"], "ma_L1": p["ma.L1"], "ar_S_L12": p["ar.S.L12"],
                  "media_implicita_w": mu, "media_empirica_w_train": float(w.dropna().mean()), "n_w": int(w.notna().sum()),
                  "coef_cuadratico_niveles_mu_24": mu / 24, "DDdif_pronostico_h_200_240_media": float(dd[-40:].mean()),
                  "dif_pronostico_h12": float(dif[11]), "dif_pronostico_h60": float(dif[59]), "dif_pronostico_h240": float(dif[239]),
                  "convergio": bool(fit.mle_retvals.get("converged")) if isinstance(fit.mle_retvals, dict) else None})
T3a = pd.DataFrame(filas)
guardar(T3a, "T3_1_constante_parametros.csv")
t = np.arange(40, dtype=float) ** 2
resumen["DD12_de_t2"] = float(np.unique(((t[13:] - t[12:-1]) - (t[1:-12] - t[:-13])).round(12))[0])

# ----------------------------------------------------------------------------- 2. sin constante
filas, pred_c, pred_n = [], [], []
for a in POOL:
    v = Ventana(a)
    pc, ic_ = sarima_rolling(s, v, o, so, {**op, "trend": "c"})
    pn, in_ = sarima_rolling(s, v, o, so, {**op, "trend": "n"})
    pred_c.append(pc.assign(anio=a))
    pred_n.append(pn.assign(anio=a))
    filas.append({"anio_test": a, "convergio_con_c": ic_["convergio"], "convergio_sin_c": in_["convergio"],
                  "MAE_con_c": float(np.mean(np.abs(pc.y_true - pc.y_pred))), "MAE_sin_c": float(np.mean(np.abs(pn.y_true - pn.y_pred))),
                  "avisos_sin_c": ";".join(in_["avisos"])})
pc = pd.concat(pred_c).set_index(["anio", "fecha"])
pn = pd.concat(pred_n).set_index(["anio", "fecha"])
ref = ERR[(ERR.modelo == "SARIMA") & (ERR.cultivar == c) & ERR.anio_test.isin(POOL)].set_index(["anio_test", "fecha"]).ae
ae_c, ae_n = (pc.y_pred - pc.y_true).abs(), (pn.y_pred - pn.y_true).abs()
ae_c.index.names = ae_n.index.names = ["anio_test", "fecha"]
dmax = float((ae_c - ref).abs().max())
if dmax > 1e-6:
    raise AssertionError(f"El SARIMA con constante no reproduce las predicciones congeladas (dif. max {dmax})")
resumen["SARIMA_con_c_reproduce_congelado_dif_max_t"] = dmax
por_ventana = pd.DataFrame(filas)
guardar(por_ventana, "T3_2_sin_constante_por_ventana.csv")
filas = []
for alc, tipo in (("todos", None), ("shock_MoM_P75", "mensual"), ("shock_YoY_P75", "interanual")):
    lo, hi = ic_dif(ae_n, ae_c, c, tipo)
    filas.append({"cultivo": c, "alcance": alc, "MAE_original_con_c": mae_sub(ae_c, c, tipo), "MAE_sin_c": mae_sub(ae_n, c, tipo),
                  "dif_sin_menos_con": mae_sub(ae_n, c, tipo) - mae_sub(ae_c, c, tipo), "IC95_dif_lo": lo, "IC95_dif_hi": hi,
                  "n_meses": int(len(ae_c) if tipo is None else ev.vector_shock(list(ae_c.index), M, c, tipo, 75).sum())})
guardar(pd.DataFrame(filas), "T3_2_sin_constante_pool.csv")

# ----------------------------------------------------------------------------- 3. regla de respaldo (E1)
REGLA = ("Si el ajuste final del orden elegido por SARIMA-sel no converge (mle_retvals['converged'] = False), se toma el "
         "siguiente orden en el orden de AIC entre los 5 preseleccionados (posiciones k+1, ..., 5 y, si ninguno converge, "
         "k-1, ..., 1, con k la posicion del elegido) cuyo ajuste, con las mismas opciones y datos, si converja. "
         "Si ninguno converge se conserva el elegido y se marca.")
filas, sust, sust_b = [], {}, {}
for cc in R.CULTIVARES:
    sc = ConstructorDatosVentana().serie(cc).sort_index().astype(float)
    for a in POOL:
        i0 = json.loads((ev.BR / "04_modelos" / "sarima_sel" / cc / str(a) / "info.json").read_text(encoding="utf-8"))
        iy = json.loads((R.G7 / "resultados" / "unidades" / "SARIMA-sel-Y1" / cc / str(a) / "info.json").read_text(encoding="utf-8"))
        fila = {"cultivo": cc, "anio_test": a, "orden_elegido": f"{tuple(i0['order'])}{tuple(i0['seasonal_order'])}",
                "posicion_aic_elegido": i0["posicion_aic_elegido"], "convergio_protocolo_original": i0["convergio"],
                "convergio_E1_Y1": iy["convergio"], "regla_aplicada": False}
        if iy["convergio"] is False:
            cand = pd.read_csv(ev.BR / "04_modelos" / "sarima_sel" / cc / str(a) / "candidatos.csv")
            k = int(i0["posicion_aic_elegido"])
            orden_prueba = list(range(k + 1, 6)) + list(range(k - 1, 0, -1))
            train = sc[(sc.index >= "2016-07") & (sc.index <= f"{a - 1}-12")]
            opc = {**SEL["opciones_ajuste"], "maxiter": SEL["maxiter_candidatos_y_final"]}
            intentos = []
            # control: el elegido, reajustado aqui, reproduce la unidad de E1 y su no convergencia
            fit_k, _ = _ajustar(train.to_numpy(), i0["order"], i0["seasonal_order"], opc)
            filas_k, _ = _a_un_paso(fit_k, [f"{a}-{m:02d}" for m in range(1, 13)], [sc[f"{a}-{m:02d}"] for m in range(1, 13)])
            pe = pd.read_csv(R.G7 / "resultados" / "unidades" / "SARIMA-sel-Y1" / cc / str(a) / "predicciones.csv", dtype={"fecha": str})
            if not np.allclose([f["y_pred"] for f in filas_k], pe.y_pred.to_numpy(), rtol=0, atol=1e-6):
                raise AssertionError("El reajuste del elegido no reproduce la unidad de E1")
            def probar(orden_prueba, intentos):
                for pos in orden_prueba:
                    r = cand[cand.posicion_aic == pos].iloc[0]
                    oo = json.loads(r.order.replace("(", "[").replace(")", "]"))
                    ss = json.loads(r.seasonal_order.replace("(", "[").replace(")", "]"))
                    fit, av = _ajustar(train.to_numpy(), oo, ss, opc)
                    conv = bool(fit.mle_retvals.get("converged", False))
                    intentos.append({"posicion_aic": pos, "orden": f"{tuple(oo)}{tuple(ss)}", "convergio": conv, "avisos": av})
                    if conv:
                        meses = [f"{a}-{m:02d}" for m in range(1, 13)]
                        fl, _ = _a_un_paso(fit, meses, [sc[m] for m in meses])
                        return pos, f"{tuple(oo)}{tuple(ss)}", pd.DataFrame(fl)
                return None

            elegido = probar(orden_prueba, intentos)
            intentos_b = []
            alt = probar([x for x in range(1, 6) if x != k], intentos_b)
            fila.update(regla_aplicada=True, intentos=json.dumps(intentos), posicion_aic_respaldo=elegido[0] if elegido else None,
                        orden_respaldo=elegido[1] if elegido else None,
                        alternativa_B_intentos=json.dumps(intentos_b), alternativa_B_posicion=alt[0] if alt else None,
                        alternativa_B_orden=alt[1] if alt else None)
            if elegido:
                sust[(cc, a)] = elegido[2]
            if alt:
                sust_b[(cc, a)] = alt[2]
        filas.append(fila)
guardar(pd.DataFrame(filas), "T3_3_regla_respaldo_convergencia.csv")
filas = []
for cc in R.CULTIVARES:
    e = ERR_G7[(ERR_G7.modelo == "SARIMA-sel-Y1") & (ERR_G7.cultivar == cc) & ERR_G7.anio_test.isin(POOL)].set_index(["anio_test", "fecha"]).ae.sort_index()
    def sustituir(sus):
        out = e.copy()
        for (c2, a), df in sus.items():
            if c2 == cc:
                for r in df.itertuples():
                    out.loc[(a, r.fecha)] = abs(r.y_pred - S[cc][r.fecha])
        return out

    nuevo, nuevo_b = sustituir(sust), sustituir(sust_b)
    for alc, tipo in (("todos", None), ("shock_MoM_P75", "mensual"), ("shock_YoY_P75", "interanual")):
        fila = {"cultivo": cc, "alcance": alc, "MAE_SARIMA_sel_Y1_publicado_G7": mae_sub(e, cc, tipo),
                "MAE_SARIMA_sel_Y1_con_regla": mae_sub(nuevo, cc, tipo),
                "MAE_SARIMA_sel_Y1_alternativa_B": mae_sub(nuevo_b, cc, tipo)}
        if any(k[0] == cc for k in sust):
            v21 = nuevo.loc[[k for k in nuevo.index if k[0] == 2021]]
            e21 = e.loc[[k for k in e.index if k[0] == 2021]]
            b21 = nuevo_b.loc[[k for k in nuevo_b.index if k[0] == 2021]]
            fila.update({"MAE_2021_publicado": float(e21.mean()), "MAE_2021_con_regla": float(v21.mean()),
                         "MAE_2021_alternativa_B": float(b21.mean())} if tipo is None else {})
        filas.append(fila)
guardar(pd.DataFrame(filas), "T3_3_SARIMA_sel_Y1_con_regla_pool.csv")
resumen["regla"] = REGLA
resumen["alternativa_B"] = ("Lectura alternativa (sensibilidad): el primer orden que converge recorriendo los 5 preseleccionados "
                            "desde la posicion 1 de AIC, excluido el elegido.")
R.escribir_json(resumen, R.RES / "T3_resumen.json")
print(json.dumps(resumen, indent=1, ensure_ascii=False))
