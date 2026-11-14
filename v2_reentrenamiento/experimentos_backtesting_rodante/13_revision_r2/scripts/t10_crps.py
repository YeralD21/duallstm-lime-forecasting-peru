"""R2-T10 (obs. 2, opcional): evaluacion probabilistica de Chronos, SARIMA y SARIMA-sel. POSTERIOR AL PROTOCOLO.

Distribucion predictiva a 1 paso de cada mes de test 2021-2025:
  * Chronos-Bolt-tiny: sus 9 cuantiles nativos (0.1, ..., 0.9), mismo contexto que el articulo (2016-01..t-1);
  * SARIMA y SARIMA-sel: normal con media y desviacion de get_forecast(1) del mismo ajuste y estado del articulo;
    se toman los mismos 9 cuantiles para comparar en igualdad de condiciones.
CRPS_Q = (2/K) * sum_k QS_tau_k (perdida de cuantil): aproximacion del CRPS con K = 9 niveles.
twCRPS_Q (ponderado por umbral): peso w(z) = 1 si |z/y_(t-1) - 1| > u y 0 si no, con u el umbral P75 del cambio
  mensual de la ventana (03_ventanas, conocido en el origen). Se aplica con la funcion de encadenamiento
  v(z) = min(z, r1) + max(z - r2, 0), r1 = y_(t-1)(1-u), r2 = y_(t-1)(1+u): twCRPS = CRPS de v(X) frente a v(y);
  como v es monotona, los cuantiles de v(X) son v(cuantiles).
Control: la mediana de Chronos y la media de SARIMA / SARIMA-sel reproducen las predicciones congeladas.
Ademas, para SARIMA y SARIMA-sel, el CRPS exacto de la normal (referencia de la aproximacion con 9 cuantiles).
Salidas: resultados/T10_*.csv y tablas_T10.md.
Uso: python 13_revision_r2/scripts/t10_crps.py
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
from scipy import stats  # noqa: E402

import r2eval as E  # noqa: E402
from lib.datos import ConstructorDatosVentana  # noqa: E402
from lib.modelos_series import _ajustar, _particiones  # noqa: E402
from lib.ventanas import Ventana  # noqa: E402

HP = json.loads((R.BR / "01_configuracion" / "hiperparametros_congelados.json").read_text(encoding="utf-8"))
MODS = ["Chronos", "SARIMA", "SARIMA-sel"]
datos = ConstructorDatosVentana()
orig = E.originales()
ch = R.ChronosFijo()
TAU = np.array(ch.cuantiles)
UMB = pd.read_csv(R.BR / "03_ventanas" / "umbrales_y_mascaras.csv")
UMB = UMB[(UMB.tipo == "mensual") & (UMB.percentil == 75)].set_index(["cultivar", "anio_test"]).umbral


def crps_q(q: np.ndarray, y: float) -> float:
    return float(2 * np.mean(((y < q).astype(float) - TAU) * (q - y)))


def cadena(z, r1, r2):
    return np.minimum(z, r1) + np.maximum(np.asarray(z) - r2, 0.0)


def crps_normal(mu, sd, y) -> float:
    z = (y - mu) / sd
    return float(sd * (z * (2 * stats.norm.cdf(z) - 1) + 2 * stats.norm.pdf(z) - 1 / np.sqrt(np.pi)))


filas = []
for c in R.CULTIVARES:
    s = datos.serie(c).sort_index().astype(float)
    for a in R.VENTANAS:
        v = Ventana(a)
        u = float(UMB[(c, a)])
        _, train, val = _particiones(s, v)
        ajustes = {"SARIMA": (HP["sarima_congelado"][c]["order"], HP["sarima_congelado"][c]["seasonal_order"], dict(HP["sarima_congelado"]["opciones"]))}
        i0 = json.loads((R.BR / "04_modelos" / "sarima_sel" / c / str(a) / "info.json").read_text(encoding="utf-8"))
        sel = HP["sarima_seleccion_por_ventana_DA9"]
        ajustes["SARIMA-sel"] = (i0["order"], i0["seasonal_order"], {**sel["opciones_ajuste"], "maxiter": sel["maxiter_candidatos_y_final"]})
        estados = {}
        for m, (o, so, op) in ajustes.items():
            fit, _ = _ajustar(train.to_numpy(), o, so, op)
            estados[m] = fit.append(val.to_numpy(), refit=False)
        for mes in v.meses_test:
            y, y1 = float(s[mes]), float(s[R.per(mes, 1)])
            r1, r2 = y1 * (1 - u), y1 * (1 + u)
            qs = {"Chronos": ch.cuantiles_h(s[s.index < mes].to_numpy(), 1)}
            punto = {"Chronos": float(qs["Chronos"][ch.i_mediana])}
            normal = {}
            for m in ("SARIMA", "SARIMA-sel"):
                f = estados[m].get_forecast(1)
                mu, sd = float(np.asarray(f.predicted_mean)[0]), float(np.asarray(f.se_mean)[0])
                qs[m], punto[m], normal[m] = mu + sd * stats.norm.ppf(TAU), mu, (mu, sd)
                estados[m] = estados[m].append([y], refit=False)
            for m in MODS:
                filas.append({"modelo": m, "cultivar": c, "anio_test": a, "fecha": mes, "y_true": y, "y_prev": y1, "u_P75": u,
                              "punto": punto[m], "CRPS_Q": crps_q(qs[m], y), "twCRPS_Q": crps_q(cadena(qs[m], r1, r2), float(cadena(y, r1, r2))),
                              "CRPS_normal_exacto": crps_normal(*normal[m], y) if m in normal else np.nan,
                              "cobertura_80": bool(qs[m][0] <= y <= qs[m][-1]), "fuera_banda_u": abs(y / y1 - 1) > u})
T = pd.DataFrame(filas)
# control de puntos
for m in MODS:
    ref = orig[(orig.modelo == m) & (orig.particion == "test") & orig.anio_test.isin(R.VENTANAS)]
    mm = T[T.modelo == m].merge(ref, on=["cultivar", "anio_test", "fecha"])
    dmax = float((mm.punto - mm.y_pred).abs().max())
    tol = float(2 * 2.0 ** -23 * mm.y_pred.abs().max()) if m == "Chronos" else 1e-6  # Chronos en float32: 2 ULP
    if len(mm) != 120 or dmax > tol:
        raise AssertionError(f"Control T10 {m}: n={len(mm)}, dif={dmax}")
R.escribir(T, R.RES / "T10_crps_por_mes.csv")

filas = []
for c in R.CULTIVARES:
    for met in ("CRPS_Q", "twCRPS_Q", "CRPS_normal_exacto"):
        pv = T[T.cultivar == c].pivot_table(index=["anio_test", "fecha"], columns="modelo", values=met, aggfunc="first").sort_index()
        mods = [m for m in MODS if m in pv.columns and pv[m].notna().all()]
        pv = pv[mods]
        cl = list(pv.index)
        est = np.array([a for a, _ in cl])
        for alc, sub in (("todos", np.ones(len(cl), bool)), ("shock_MoM_P75", E.vec(cl, E.mascara_mom(c)))):
            r = E.resumen(pv, est, np.ones(len(cl)), sub).set_index("modelo")
            for m in mods:
                fila = {"cultivo": c, "metrica": met, "alcance": alc, "modelo": m, "n_meses": int(sub.sum()), "media": r.loc[m, "MAE"],
                        "IC_lo": r.loc[m, "IC_lo"], "IC_hi": r.loc[m, "IC_hi"]}
                if m != "SARIMA":
                    d, k = E.dif(pv, m, "SARIMA", est, sub), E.dm(pv, m, "SARIMA", sub)
                    fila.update({"dif_vs_SARIMA": d["dif"], "IC_dif_lo": d["IC_lo"], "IC_dif_hi": d["IC_hi"], "DM_p": k["p"]})
                filas.append(fila)
S = pd.DataFrame(filas)
R.escribir(S, R.RES / "T10_crps_resumen.csv")
cob = T.groupby(["cultivar", "modelo"]).cobertura_80.mean().reset_index()
v = [{"cultivo": r.cultivo, "métrica": r.metrica, "alcance": r.alcance, "modelo": r.modelo, "n": r.n_meses,
      "media (IC95)": E.ic_txt(r.media, r.IC_lo, r.IC_hi, E.DEC[r.cultivo]),
      "dif vs SARIMA (IC95)": "—" if pd.isna(getattr(r, "dif_vs_SARIMA", np.nan)) else E.ic_txt(r.dif_vs_SARIMA, r.IC_dif_lo, r.IC_dif_hi, E.DEC[r.cultivo]),
      "DM p": "—" if pd.isna(getattr(r, "DM_p", np.nan)) else E.num(r.DM_p, 3)} for r in S.itertuples()]
txt = ["<!-- generado por t10_crps.py -->", "#### T10 — CRPS y CRPS ponderado por umbral (pool 2021–2025, t)", "",
       f"Niveles de cuantil: {', '.join(f'{t:.1f}' for t in TAU)}. Menor = mejor.", "", E.md(pd.DataFrame(v)), "",
       "Cobertura empírica del intervalo 10–90 % (nominal 80 %):", "",
       E.md(cob.assign(cobertura_80=cob.cobertura_80.map(lambda x: f"{100 * x:.1f} %")))]
(R.RES / "tablas_T10.md").write_text("\n".join(txt) + "\n", encoding="utf-8", newline="\n")
print("escrito tablas_T10.md")
