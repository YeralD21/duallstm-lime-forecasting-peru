"""R2-T6 (E5, obs. 3) y R2-T7.1 (ablacion por bloques, obs. 3 / RQ3). POSTERIOR AL PROTOCOLO.

Control previo: r2lib.correr_tabular con los 37 predictores reproduce las predicciones congeladas de Ridge, ElasticNet
y XGB-37 (10 semillas) en las 10 unidades (cultivo x ventana); si no, se detiene.

T6 / E5: los 37 predictores + y_(T-12) (columna produccion_t_<c>_y12) en Ridge, ElasticNet y XGB-37, con el mismo
protocolo (pares X_t -> y_(t+1), estandarizacion del train, alpha/l1 por MAE de validacion, parametros XGB oficiales,
semillas 0..9). y_(T-12) solo existe desde el objetivo 2017-01: los pares de train con objetivo 2016-08..2016-12 se
descartan. Para separar ese efecto se corre tambien el modelo original con esas mismas filas ("filas E5").
T7.1: Ridge y XGB-37 con conjuntos acumulativos: (a) produccion + calendario + y_(T-12); (b) + clima; (c) + emergencias
(= E5, mismo orden de columnas); (d) + noticias (avg_sentiment y n_noticias, rezagos 1, 3, 6).
Salidas: resultados/unidades_d2/tabulares_h1.csv, resultados/T6_*.csv, T7_ablacion_*.csv, tablas_T6_T7.md.
Uso: python 13_revision_r2/scripts/t6_t7_tabulares.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import r2lib as R  # noqa: E402
from lib.entorno import preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

import r2eval as E  # noqa: E402
from lib.datos import ConstructorDatosVentana  # noqa: E402
from lib.ventanas import Ventana  # noqa: E402
from v2_reentrenamiento.src.models.features_gc2_xgboost import gc2_predictors  # noqa: E402

FAM = {"Ridge": "Ridge", "ElasticNet": "ElasticNet", "XGB-37": "XGB"}


def conjuntos(c):
    B = R.BLOQUES
    y12 = (R.col_y12(c),)
    a = B["produccion"](c) + B["calendario"](c)
    return {"(a) producción+calendario+y12": a + y12, "(b) +clima": a + B["clima"](c) + y12,
            "(c) +emergencias": a + B["clima"](c) + B["emergencias"](c) + y12,
            "(d) +noticias": a + B["clima"](c) + B["emergencias"](c) + y12 + B["noticias"](c)}


datos = ConstructorDatosVentana()
orig = E.originales()
frames, infos = [], []
for c in R.CULTIVARES:
    g37 = tuple(gc2_predictors(c))
    cj = conjuntos(c)
    if cj["(c) +emergencias"] != g37 + (R.col_y12(c),):
        raise AssertionError("(c) debe ser exactamente E5 (37 + y12, mismo orden)")
    for a in R.VENTANAS:
        v = Ventana(a)
        for mod, fam in FAM.items():
            # control: 37 predictores reproducen lo congelado
            p, inf = R.correr_tabular(datos, c, v, fam, g37, nombre=mod)
            ref = orig[(orig.modelo == mod) & (orig.cultivar == c) & (orig.anio_test == a) & (orig.particion == "test")]
            mm = p.merge(ref, on=["fecha", "semilla"] if fam == "XGB" else ["fecha"], suffixes=("", "_ref"))
            dmax = float((mm.y_pred - mm.y_pred_ref).abs().max())
            if len(mm) != len(ref) or dmax > 1e-6:
                raise AssertionError(f"Control {mod} {c} {a}: no reproduce lo congelado (n={len(mm)}/{len(ref)}, dif={dmax})")
            infos += [{**i, "control_dif_max_t": dmax} for i in inf]
            for nombre, pred, filtro in ((f"{mod}+y12", g37 + (R.col_y12(c),), False), (f"{mod} (filas E5)", g37, True)):
                p, inf = R.correr_tabular(datos, c, v, fam, pred, filtro_y12=filtro, nombre=nombre)
                frames.append(p)
                infos += inf
        for fam, mod in (("Ridge", "Ridge"), ("XGB", "XGB-37")):
            for k, pred in cj.items():
                if k.startswith("(c)"):
                    continue  # = E5
                p, inf = R.correr_tabular(datos, c, v, fam, pred, nombre=f"{mod} {k[:3]}")
                frames.append(p)
                infos += inf
        print(f"{c} {a}: control OK y modelos E5/ablacion ajustados")
NUEVOS = pd.concat(frames, ignore_index=True)
R.escribir(NUEVOS, R.RES / "unidades_d2" / "tabulares_h1.csv")
R.escribir(pd.DataFrame(infos), R.RES / "unidades_d2" / "tabulares_h1_info.csv")
# (c) = E5
alias = [NUEVOS[NUEVOS.modelo == f"{m}+y12"].assign(modelo=f"{m} (c)") for m in ("Ridge", "XGB-37")]
ES, ERR = E.errores(orig, E.r2_dia1(), NUEVOS, *alias)

# ----------------------------------------------------------------------------- T6
filas, dif_rows = [], []
for c in R.CULTIVARES:
    mods = []
    for m in FAM:
        mods += [m, f"{m}+y12", f"{m} (filas E5)"]
    pv, cl, est, Dv = E.matriz(ERR, mods + [E.MEJOR[c]], c)
    for alc, sub in (("todos", np.ones(len(cl), bool)), ("shock_MoM_P75", E.vec(cl, E.mascara_mom(c))),
                     ("shock_YoY_P75", E.vec(cl, E.mascara_mom(c, tipo="interanual")))):
        r = E.resumen(pv, est, Dv, sub, mods).set_index("modelo")
        meses = [f for (_, f), s_ in zip(cl, sub) if s_]
        for m in FAM:
            k_o, k_n = E.dm(pv, m, E.MEJOR[c], sub), E.dm(pv, f"{m}+y12", E.MEJOR[c], sub)
            d = E.dif(pv, f"{m}+y12", m, est, sub)
            d_f = E.dif(pv, f"{m} (filas E5)", m, est, sub)
            d_y = E.dif(pv, f"{m}+y12", f"{m} (filas E5)", est, sub)
            fila = {"cultivo": c, "alcance": alc, "modelo": m, "n_meses": int(sub.sum()),
                    "MAE_original": r.loc[m, "MAE"], "IC_orig_lo": r.loc[m, "IC_lo"], "IC_orig_hi": r.loc[m, "IC_hi"],
                    "MAE_E5": r.loc[f"{m}+y12", "MAE"], "IC_E5_lo": r.loc[f"{m}+y12", "IC_lo"], "IC_E5_hi": r.loc[f"{m}+y12", "IC_hi"],
                    "dif_E5_menos_orig": d["dif"], "IC_dif_lo": d["IC_lo"], "IC_dif_hi": d["IC_hi"],
                    "dif_filas_E5_menos_orig": d_f["dif"], "dif_y12_mismas_filas": d_y["dif"], "IC_dif_y12_lo": d_y["IC_lo"],
                    "IC_dif_y12_hi": d_y["IC_hi"], "mejor": E.MEJOR[c],
                    "DM_orig_vs_mejor_p": k_o["p"], "DM_E5_vs_mejor_HLN": k_n["HLN"], "DM_E5_vs_mejor_p": k_n["p"]}
            if m == "XGB-37":
                fila["semillas_E5_mejoran_de_10"] = E.semillas_mejoran(ES, "XGB-37+y12", "XGB-37", c, E.POOL, meses)
            filas.append(fila)
T6 = pd.DataFrame(filas)
R.escribir(T6, R.RES / "T6_E5_y12_tabulares.csv")

# ----------------------------------------------------------------------------- T7.1
filas = []
for c in R.CULTIVARES:
    for mod in ("Ridge", "XGB-37"):
        etapas = [f"{mod} (a)", f"{mod} (b)", f"{mod} (c)", f"{mod} (d)"]
        pv, cl, est, Dv = E.matriz(ERR, etapas, c)
        for alc, sub in (("todos", np.ones(len(cl), bool)), ("shock_MoM_P75", E.vec(cl, E.mascara_mom(c)))):
            r = E.resumen(pv, est, Dv, sub, etapas).set_index("modelo")
            meses = [f for (_, f), s_ in zip(cl, sub) if s_]
            for i, m in enumerate(etapas):
                fila = {"cultivo": c, "modelo": mod, "conjunto": list(conjuntos(c))[i], "n_predictores": len(list(conjuntos(c).values())[i]),
                        "alcance": alc, "n_meses": int(sub.sum()), "MAE": r.loc[m, "MAE"], "IC_lo": r.loc[m, "IC_lo"], "IC_hi": r.loc[m, "IC_hi"]}
                if i:
                    d = E.dif(pv, m, etapas[i - 1], est, sub)
                    fila.update({"dif_vs_anterior": d["dif"], "IC_dif_lo": d["IC_lo"], "IC_dif_hi": d["IC_hi"]})
                    if mod == "XGB-37":
                        fila["semillas_mejoran_vs_anterior_de_10"] = E.semillas_mejoran(ES, m, etapas[i - 1], c, E.POOL, meses)
                filas.append(fila)
T7 = pd.DataFrame(filas)
R.escribir(T7, R.RES / "T7_ablacion_bloques.csv")

# ----------------------------------------------------------------------------- markdown
txt = ["<!-- generado por t6_t7_tabulares.py -->", "#### T6 — E5: y_(T−12) en los modelos tabulares (pool 2021–2025)", "",
       "Diferencia = E5 − original (negativa = E5 mejor), IC 95 % bootstrap pareado. «Solo y12» = E5 − original con las mismas "
       "filas de entrenamiento (aísla el efecto de y_(T−12) del de perder los pares con objetivo 2016-08..2016-12). "
       "DM-HLN de E5 frente al mejor modelo del cultivo (sutil: Chronos; dulce: SARIMA).", ""]
v = []
for r in T6.itertuples():
    d = E.DEC[r.cultivo]
    v.append({"cultivo": r.cultivo, "alcance": r.alcance, "modelo": r.modelo, "n": r.n_meses,
              "MAE original (IC95)": E.ic_txt(r.MAE_original, r.IC_orig_lo, r.IC_orig_hi, d),
              "MAE E5 (IC95)": E.ic_txt(r.MAE_E5, r.IC_E5_lo, r.IC_E5_hi, d),
              "dif E5−orig (IC95)": E.ic_txt(r.dif_E5_menos_orig, r.IC_dif_lo, r.IC_dif_hi, d),
              "solo y12 (IC95)": E.ic_txt(r.dif_y12_mismas_filas, r.IC_dif_y12_lo, r.IC_dif_y12_hi, d),
              "semillas E5 mejor (de 10)": "—" if pd.isna(getattr(r, "semillas_E5_mejoran_de_10", np.nan)) else int(r.semillas_E5_mejoran_de_10),
              "DM E5 vs mejor (HLN; p)": f"{E.num(r.DM_E5_vs_mejor_HLN, 2)}; {E.num(r.DM_E5_vs_mejor_p, 3)}",
              "p DM orig vs mejor": E.num(r.DM_orig_vs_mejor_p, 3)})
txt += [E.md(pd.DataFrame(v)), "", "#### T7.1 — Ablación por bloques acumulativos (pool 2021–2025)", "",
        "Diferencia = conjunto − conjunto anterior (negativa = el bloque añadido mejora). (c) = E5.", ""]
v = []
for r in T7.itertuples():
    d = E.DEC[r.cultivo]
    v.append({"cultivo": r.cultivo, "modelo": r.modelo, "conjunto": r.conjunto, "k": r.n_predictores, "alcance": r.alcance,
              "MAE (IC95)": E.ic_txt(r.MAE, r.IC_lo, r.IC_hi, d),
              "dif vs anterior (IC95)": "—" if pd.isna(r.dif_vs_anterior) else E.ic_txt(r.dif_vs_anterior, r.IC_dif_lo, r.IC_dif_hi, d),
              "semillas mejoran (de 10)": "—" if pd.isna(getattr(r, "semillas_mejoran_vs_anterior_de_10", np.nan)) else int(r.semillas_mejoran_vs_anterior_de_10)})
txt.append(E.md(pd.DataFrame(v)))
(R.RES / "tablas_T6_T7.md").write_text("\n".join(txt) + "\n", encoding="utf-8", newline="\n")
print("escrito tablas_T6_T7.md")
