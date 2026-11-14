"""R2-T7.2 (obs. 3, RQ3): SARIMAX con los ordenes fijos del SARIMA de cada cultivo y exogenas rezagadas. POSTERIOR AL PROTOCOLO.

ELECCION FIJADA ANTES DE VER RESULTADOS (registrada tambien en README.md e INFORME_DIA2.md):
  * Exogenas: clima (T2M, T2M_MAX, WS2M, PRECTOTCORR, RH2M) y emergencias INDECI (num_emergencias, personas_afectadas,
    personas_damnificadas, hectareas_cultivo_perdidas, hectareas_cultivo_afectadas), agregados nacionales con los pesos
    geograficos del protocolo para la ventana (ConstructorDatosVentana.maestro(c, Y-2)).
  * Rezagos: los mismos que los modelos tabulares. Para el mes objetivo T se usan x_(T-2), x_(T-4) y x_(T-7) (columnas
    lag1, lag3, lag6 de la fila T-1): nada del mes T ni de T-1, igual que en el protocolo (D6).
  * Version PRINCIPAL "SARIMAX-PC": 30 exogenas son demasiadas para 42-90 meses de train, asi que se usan 2: la primera
    componente principal del clima y la de las emergencias, cada una solo en el rezago 1 (x_(T-2)). PCA (SVD) sobre las
    variables estandarizadas con media y desviacion de los meses de train; signo: carga positiva en T2M / num_emergencias.
  * Version SECUNDARIA "SARIMAX-30": las 30 exogenas (10 variables x 3 rezagos), estandarizadas con el train; se reporta
    como sensibilidad, marcada como sobreparametrizada. Su train empieza en 2016-08 (x_(T-7) no existe antes).
  * Orden y opciones: los del SARIMA congelado (hiperparametros_congelados.json, sarima_congelado); ajuste unico en train,
    validacion y test a 1 paso con append(refit=False), igual que lib/modelos_series.sarima_rolling.
Salidas: resultados/unidades_d2/sarimax.csv, resultados/T7_sarimax_*.csv, tablas_T7_sarimax.md.
Uso: python 13_revision_r2/scripts/t7_sarimax.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import r2lib as R  # noqa: E402
from lib.entorno import preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import json  # noqa: E402
import warnings  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

import r2eval as E  # noqa: E402
from lib.datos import ConstructorDatosVentana  # noqa: E402
from lib.ventanas import Ventana  # noqa: E402

CFG = json.loads((R.BR / "01_configuracion" / "hiperparametros_congelados.json").read_text(encoding="utf-8"))["sarima_congelado"]
CLIMA = ["T2M", "T2M_MAX", "WS2M", "PRECTOTCORR", "RH2M"]
EMERG = ["num_emergencias", "personas_afectadas", "personas_damnificadas", "hectareas_cultivo_perdidas", "hectareas_cultivo_afectadas"]
REZAGOS = (2, 4, 7)  # respecto del mes objetivo T


def exogenas(maestro: pd.DataFrame, meses, train_meses, version: str) -> pd.DataFrame:
    clave = maestro["año"].astype(int).astype(str) + "-" + maestro["mes"].astype(int).map("{:02d}".format)
    x = maestro.set_index(clave)[CLIMA + EMERG].astype(float)

    def rez(k):
        return pd.DataFrame([x.loc[R.per(m, k)].to_numpy() for m in meses], index=meses, columns=x.columns)

    if version == "SARIMAX-30":
        X = pd.concat({k: rez(k) for k in REZAGOS}, axis=1)
        X.columns = [f"{v}_T-{k}" for k, v in X.columns]
        tr = X.loc[train_meses]
        return (X - tr.mean()) / tr.std(ddof=0)
    X1 = rez(2)
    out = {}
    for nombre, cols in (("PC1_clima_T-2", CLIMA), ("PC1_emergencias_T-2", EMERG)):
        tr = X1.loc[train_meses, cols]
        mu, sd = tr.mean(), tr.std(ddof=0)
        Z = ((X1[cols] - mu) / sd).to_numpy()
        _, _, vt = np.linalg.svd(Z[[meses.index(m) for m in train_meses]], full_matrices=False)
        w = vt[0] * np.sign(vt[0][0])
        out[nombre] = Z @ w
    return pd.DataFrame(out, index=meses)


def sarimax_rolling(s: pd.Series, X: pd.DataFrame, v: Ventana, c: str, inicio: str):
    from statsmodels.tsa.statespace.sarimax import SARIMAX

    op = dict(CFG["opciones"])
    maxiter = op.pop("maxiter")
    tr = [m for m in s.index if inicio <= m <= v.fin_train]
    va = [m for m in s.index if v.val[0] <= m <= v.val[1]]
    with warnings.catch_warnings(record=True) as av:
        warnings.simplefilter("always")
        fit = SARIMAX(s[tr].to_numpy(), exog=X.loc[tr].to_numpy(), order=tuple(CFG[c]["order"]),
                      seasonal_order=tuple(CFG[c]["seasonal_order"]), **op).fit(disp=False, maxiter=maxiter)
    p0 = np.asarray(fit.params, float).copy()
    est = fit.append(s[va].to_numpy(), exog=X.loc[va].to_numpy(), refit=False)
    filas = []
    for m in v.meses_test:
        xm = X.loc[[m]].to_numpy()
        filas.append({"fecha": m, "y_true": float(s[m]), "y_pred": float(np.asarray(est.forecast(1, exog=xm))[0])})
        est = est.append([float(s[m])], exog=xm, refit=False)
    if not np.allclose(np.asarray(est.params, float), p0, rtol=0, atol=1e-10):
        raise AssertionError("SARIMAX: parametros cambiaron durante append")
    conv = bool(fit.mle_retvals.get("converged", False)) if isinstance(fit.mle_retvals, dict) else None
    return pd.DataFrame(filas), {"convergio": conv, "n_train": len(tr), "n_exog": X.shape[1], "avisos": sorted({a.category.__name__ for a in av}),
                                 "parametros": dict(zip(fit.model.param_names, p0.tolist()))}


datos = ConstructorDatosVentana()
frames, infos = [], []
for c in R.CULTIVARES:
    s = datos.serie(c).sort_index().astype(float)
    for a in R.VENTANAS:
        v = Ventana(a)
        maestro = datos.maestro(c, v.anio_fin_train)
        for version, inicio in (("SARIMAX-PC", "2016-07"), ("SARIMAX-30", "2016-08")):
            meses = [m for m in s.index if inicio <= m <= v.test[1]]
            train_meses = [m for m in meses if m <= v.fin_train]
            X = exogenas(maestro, meses, train_meses, version)
            p, inf = sarimax_rolling(s, X, v, c, inicio)
            frames.append(p.assign(modelo=version, cultivar=c, anio_test=a, semilla=None, particion="test"))
            infos.append({"modelo": version, "cultivar": c, "anio_test": a, **{k: (json.dumps(x) if isinstance(x, (dict, list)) else x)
                                                                              for k, x in inf.items()}})
            print(version, c, a, "conv", inf["convergio"], "MAE", round(float(np.mean(np.abs(p.y_true - p.y_pred))), 2))
NUEVOS = pd.concat(frames, ignore_index=True)
R.escribir(NUEVOS, R.RES / "unidades_d2" / "sarimax.csv")
R.escribir(pd.DataFrame(infos), R.RES / "unidades_d2" / "sarimax_info.csv")
ES, ERR = E.errores(E.originales(), NUEVOS)
filas = []
for c in R.CULTIVARES:
    mods = ["SARIMA", "SARIMAX-PC", "SARIMAX-30"]
    pv, cl, est, Dv = E.matriz(ERR, mods, c)
    for alc, sub in (("todos", np.ones(len(cl), bool)), ("shock_MoM_P75", E.vec(cl, E.mascara_mom(c))),
                     ("shock_YoY_P75", E.vec(cl, E.mascara_mom(c, tipo="interanual")))):
        r = E.resumen(pv, est, Dv, sub, mods).set_index("modelo")
        for m in mods:
            fila = {"cultivo": c, "alcance": alc, "modelo": m, **r.loc[m].to_dict()}
            if m != "SARIMA":
                d, k = E.dif(pv, m, "SARIMA", est, sub), E.dm(pv, m, "SARIMA", sub)
                fila.update({"dif_vs_SARIMA": d["dif"], "IC_dif_lo": d["IC_lo"], "IC_dif_hi": d["IC_hi"], "DM_HLN": k["HLN"], "DM_p": k["p"]})
            filas.append(fila)
T = pd.DataFrame(filas)
R.escribir(T, R.RES / "T7_sarimax_vs_sarima.csv")
conv = pd.DataFrame(infos).groupby(["modelo", "cultivar"]).convergio.apply(lambda x: f"{int(x.sum())}/{len(x)}").reset_index()
v = [{"cultivo": r.cultivo, "alcance": r.alcance, "modelo": r.modelo, "n": int(r.n_meses), "MAE (IC95)": E.ic_txt(r.MAE, r.IC_lo, r.IC_hi, E.DEC[r.cultivo]),
      "dif vs SARIMA (IC95)": "—" if pd.isna(getattr(r, "dif_vs_SARIMA", np.nan)) else E.ic_txt(r.dif_vs_SARIMA, r.IC_dif_lo, r.IC_dif_hi, E.DEC[r.cultivo]),
      "DM vs SARIMA (HLN; p)": "—" if pd.isna(getattr(r, "DM_p", np.nan)) else f"{E.num(r.DM_HLN, 2)}; {E.num(r.DM_p, 3)}"} for r in T.itertuples()]
txt = ["<!-- generado por t7_sarimax.py -->", "#### T7.2 — SARIMAX frente a SARIMA (pool 2021–2025)", "", E.md(pd.DataFrame(v)), "",
       "Convergencia del ajuste en train (ventanas que convergen):", "", E.md(conv)]
(R.RES / "tablas_T7_sarimax.md").write_text("\n".join(txt) + "\n", encoding="utf-8", newline="\n")
print("escrito tablas_T7_sarimax.md")
