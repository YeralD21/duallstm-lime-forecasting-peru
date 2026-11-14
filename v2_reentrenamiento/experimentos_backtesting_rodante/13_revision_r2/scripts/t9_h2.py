"""R2-T9 (obs. 14): horizonte h = 2 (origen t-2 para el mes t; no se usa y_(t-1)). POSTERIOR AL PROTOCOLO.

Modelos que no requieren reentrenar redes: Naive (y_(t-2)), Seasonal Naive (y_(t-12), igual que en h = 1), SARIMA,
SARIMA-sel, ETS, Theta (mismos ajustes de train; estado actualizado hasta t-2; pronostico a 2 pasos), Chronos
(contexto hasta t-2, prediction_length = 2, mediana del paso 2) y Ridge, ElasticNet y XGB-37 (estrategia directa:
pares X_(t-2) -> y_t con los 37 predictores de la fila t-2, que solo contienen informacion hasta t-2; se reentrenan
con la misma busqueda de hiperparametros por validacion; r2lib.pares_h verifica que cada par tenga exactamente
2 meses de separacion). GC3 y GE quedan fuera (habria que reentrenar las redes).
Controles: cada modelo, corrido con h = 1 por este mismo codigo, reproduce sus predicciones congeladas.
Salidas: resultados/unidades_d2/h2.csv, resultados/T9_*.csv y tablas_T9.md.
Uso: python 13_revision_r2/scripts/t9_h2.py
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
from lib.modelos_series import _ajustar, _particiones  # noqa: E402
from lib.ventanas import Ventana  # noqa: E402
from v2_reentrenamiento.src.models.features_gc2_xgboost import gc2_predictors  # noqa: E402

HP = json.loads((R.BR / "01_configuracion" / "hiperparametros_congelados.json").read_text(encoding="utf-8"))
MODELOS_H2 = ["Naive", "Seasonal Naive", "Chronos", "SARIMA", "SARIMA-sel", "Ridge", "ElasticNet", "XGB-37", "ETS", "Theta"]
datos = ConstructorDatosVentana()
orig = E.originales()
r2 = E.r2_dia1()
chronos = R.ChronosFijo()


def chronos_h(ctx: np.ndarray, h: int) -> float:
    return float(chronos.cuantiles_h(ctx, h)[chronos.i_mediana])


def sarima_h(s, v, order, so, opc, h):
    _, train, _ = _particiones(s, v)
    fit, _ = _ajustar(train.to_numpy(), order, so, opc)
    despues = [m for m in s.index if m > train.index.max()]
    filas = []
    for m in v.meses_test:
        nuevos = [x for x in despues if x <= R.per(m, h)]
        est = fit.append(s[nuevos].to_numpy(), refit=False) if nuevos else fit
        filas.append({"fecha": m, "y_true": float(s[m]), "y_pred": float(np.asarray(est.forecast(h), float)[-1])})
    return pd.DataFrame(filas)


def comparar(p: pd.DataFrame, ref: pd.DataFrame, nombre: str, tol=1e-6):
    mm = p.merge(ref, on=[k for k in ("fecha", "semilla") if k in p and k in ref and (k != "semilla" or ref.semilla.notna().any())],
                 suffixes=("", "_ref"))
    dmax = float((mm.y_pred - mm.y_pred_ref).abs().max())
    tol = max(tol, 1e-9 * float(mm.y_pred_ref.abs().max()))  # las unidades R2 se guardan con 10 cifras significativas (%.10g)
    if nombre.startswith("Chronos"):  # Chronos trabaja en float32: se admiten 2 ULP de float32 del valor (2 * 2^-23 relativo)
        tol = float(2 * 2.0 ** -23 * mm.y_pred_ref.abs().max())
    if len(mm) != len(ref) or dmax > tol:
        raise AssertionError(f"Control h=1 {nombre}: n={len(mm)}/{len(ref)}, dif={dmax}")
    return dmax


frames, controles = [], []
for c in R.CULTIVARES:
    s = datos.serie(c).sort_index().astype(float)
    for a in R.VENTANAS:
        v = Ventana(a)
        base = {"cultivar": c, "anio_test": a, "particion": "test"}
        ref = {m: orig[(orig.modelo == m) & (orig.cultivar == c) & (orig.anio_test == a) & (orig.particion == "test")] for m in MODELOS_H2[:8]}
        ref.update({m: r2[(r2.modelo == m) & (r2.cultivar == c) & (r2.anio_test == a) & (r2.particion == "test")] for m in ("ETS", "Theta")})
        for h in (1, 2):
            out = {}
            out["Naive"] = pd.DataFrame([{"fecha": m, "y_true": s[m], "y_pred": s[R.per(m, h)]} for m in v.meses_test])
            out["Seasonal Naive"] = pd.DataFrame([{"fecha": m, "y_true": s[m], "y_pred": s[R.per(m, 12)]} for m in v.meses_test])
            out["Chronos"] = pd.DataFrame([{"fecha": m, "y_true": s[m], "y_pred": chronos_h(s[s.index <= R.per(m, h)].to_numpy(), h)}
                                           for m in v.meses_test])
            cfg = HP["sarima_congelado"]
            out["SARIMA"] = sarima_h(s, v, cfg[c]["order"], cfg[c]["seasonal_order"], dict(cfg["opciones"]), h)
            i0 = json.loads((R.BR / "04_modelos" / "sarima_sel" / c / str(a) / "info.json").read_text(encoding="utf-8"))
            sel = HP["sarima_seleccion_por_ventana_DA9"]
            out["SARIMA-sel"] = sarima_h(s, v, i0["order"], i0["seasonal_order"], {**sel["opciones_ajuste"], "maxiter": sel["maxiter_candidatos_y_final"]}, h)
            out["ETS"] = R.ets_h(s, v, h)[0]
            out["Theta"] = R.theta_h(s, v, h)[0]
            for mod, fam in (("Ridge", "Ridge"), ("ElasticNet", "ElasticNet"), ("XGB-37", "XGB")):
                out[mod] = R.correr_tabular(datos, c, v, fam, tuple(gc2_predictors(c)), h=h, nombre=mod)[0]
            for m, p in out.items():
                p = p.assign(modelo=m, **base)
                if "semilla" not in p:
                    p["semilla"] = None
                if h == 1:
                    controles.append({"modelo": m, "cultivar": c, "anio_test": a, "dif_max_h1_vs_congelado": comparar(p, ref[m], f"{m} {c} {a}")})
                else:
                    frames.append(p[E.COLS])
        print(f"{c} {a}: controles h=1 OK; h=2 calculado", flush=True)
H2 = pd.concat(frames, ignore_index=True)
R.escribir(H2, R.RES / "unidades_d2" / "h2.csv")
R.escribir(pd.DataFrame(controles), R.RES / "T9_controles_h1.csv")

ES2, ERR2 = E.errores(H2)
ES1, ERR1 = E.errores(orig, r2)
filas, rob = [], []
for c in R.CULTIVARES:
    pv, cl, est, Dv = E.matriz(ERR2, MODELOS_H2, c)
    pv1, *_ = E.matriz(ERR1, MODELOS_H2, c)
    for alc, sub in (("todos", np.ones(len(cl), bool)), ("shock_MoM_P75", E.vec(cl, E.mascara_mom(c)))):
        r = E.resumen(pv, est, Dv, sub).set_index("modelo")
        rk = E.ranking(pv, est, sub).set_index("modelo")
        for m in MODELOS_H2:
            filas.append({"cultivo": c, "alcance": alc, "modelo": m, **r.loc[m].to_dict(), "posicion": int(rk.loc[m, "posicion"]),
                          "primero_o_empate": bool(rk.loc[m, "primero"]), "MAE_h1": float(pv1[m].to_numpy()[sub].mean())})
    subs = {p: E.vec(cl, E.mascara_mom(c, p=p)) for p in E.PCTS}
    rb = E.robustez(pv, est, subs)
    rb.insert(0, "cultivo", c)
    rob.append(rb)
T9 = pd.DataFrame(filas)
R.escribir(T9, R.RES / "T9_metricas_h2.csv")
RB = pd.concat(rob, ignore_index=True)
R.escribir(RB, R.RES / "T9_robustez_h2.csv")
txt = ["<!-- generado por t9_h2.py -->", "#### T9 — Horizonte h = 2 (pool 2021–2025; 10 modelos sin redes)", "",
       "* = primero o empatado con el primero. «Robusto» = primero o empatado en ≥ 3 de P50, P60, P75 y P90 (MoM). "
       "MAE h = 1: el del artículo / T1 (Día 1), como referencia.", ""]
for c in R.CULTIVARES:
    d = E.DEC[c]
    v = []
    for m in MODELOS_H2:
        a_ = T9[(T9.cultivo == c) & (T9.alcance == "todos") & (T9.modelo == m)].iloc[0]
        b_ = T9[(T9.cultivo == c) & (T9.alcance == "shock_MoM_P75") & (T9.modelo == m)].iloc[0]
        rb = RB[(RB.cultivo == c) & (RB.modelo == m)].iloc[0]
        v.append({"modelo": f"{m} †" if m in R.NUEVOS else m, "MAE h2 todos (IC95)": E.ic_txt(a_.MAE, a_.IC_lo, a_.IC_hi, d),
                  "pos.": f"{a_.posicion}{'*' if a_.primero_o_empate else ''}", "MAE h1 todos": E.num(a_.MAE_h1, d),
                  "MAE h2 shock MoM P75 (IC95)": E.ic_txt(b_.MAE, b_.IC_lo, b_.IC_hi, d), "pos. shock": f"{b_.posicion}{'*' if b_.primero_o_empate else ''}",
                  "MAE h1 shock": E.num(b_.MAE_h1, d), "1º/empate MoM (de 4)": int(rb.primero_o_empate_de_4),
                  "robusto": "Sí" if rb.consistently_top_ranked else "No"})
    txt += [f"**{c}** (60 meses; {int(T9[(T9.cultivo == c) & (T9.alcance == 'shock_MoM_P75')].n_meses.iloc[0])} de shock MoM P75)", "",
            E.md(pd.DataFrame(v)), ""]
(R.RES / "tablas_T9.md").write_text("\n".join(txt) + "\n", encoding="utf-8", newline="\n")
print("escrito tablas_T9.md")
