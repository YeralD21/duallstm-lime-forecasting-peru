"""R2-T8 (obs. 2): meses de cambio grande definidos ex ante (conocidos en t-1). POSTERIOR AL PROTOCOLO.

Definiciones (todas con la historia hasta el origen de la ventana, dic Y-1, como las mascaras del articulo, D-BR3):
  A. "SN anticipado": a_t = |y_(t-12) - y_(t-1)| / y_(t-1). Alerta en el mes de test t si a_t > percentil p de a en la
     historia (meses 2017-01..dic Y-1, los primeros con y_(t-12)). Conocido en t-1.
  B. "SARIMA anticipado": b_t = |yhat_t - y_(t-1)| / y_(t-1), con yhat_t el pronostico a 1 paso del SARIMA fijo de la
     ventana (04_modelos/sarima_rolling). Historia: pronosticos a 1 paso dentro del train (fit.predict, sin los 13
     primeros meses, que dependen de la inicializacion difusa con d + 12·D diferencias) y los de validacion. Conocido en t-1.
  C. "El Niño costero (ENFEN/IGP)": meses dentro de un evento El Niño Costero de la lista oficial del IGP
     (ICEN, ENFEN 2024), datos_externos/igp_icen/lista_eventos_ICEN.html. NO es ex ante: el ICEN es una media
     corrida de 3 meses centrada y el evento se declara despues; se reporta como estado contemporaneo.
Para A y B: percentiles 50, 60, 75, 90 y regla "consistently top-ranked" (>= 3 de 4). Para C, un solo conjunto.
Modelos: los 10 del articulo + ETS + Theta. Salidas: resultados/T8_*.csv y tablas_T8.md.
Uso: python 13_revision_r2/scripts/t8_ex_ante.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import r2lib as R  # noqa: E402
from lib.entorno import preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import html  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

import r2eval as E  # noqa: E402
from lib.datos import ConstructorDatosVentana  # noqa: E402
from lib.modelos_series import _ajustar, _particiones  # noqa: E402
from lib.ventanas import Ventana  # noqa: E402

CFG = json.loads((R.BR / "01_configuracion" / "hiperparametros_congelados.json").read_text(encoding="utf-8"))["sarima_congelado"]
ICEN_DIR = R.R2 / "datos_externos" / "igp_icen"
QUEMADO = 13


def umbral(hist: pd.Series, p: int) -> float:
    return float(np.percentile(hist.to_numpy(), p, method="linear"))


def eventos_nino() -> list[tuple[str, str]]:
    txt = html.unescape(re.sub(r"<[^>]+>", " ", (ICEN_DIR / "lista_eventos_ICEN.html").read_text(encoding="latin-1", errors="replace")))
    bloque = txt.split("El Niño Costero", 1)[1].split("La Niña Costera", 1)[0]
    ev = []
    for a0, m0, a1, m1 in re.findall(r"\b(19\d\d|20\d\d)\s+(\d{1,2})\s+(19\d\d|20\d\d)\s+(\d{1,2})\s+\d+\s+\w+", bloque):
        ev.append((f"{a0}-{int(m0):02d}", f"{a1}-{int(m1):02d}"))
    return ev


datos = ConstructorDatosVentana()
mask = {}   # (definicion, cultivo, p) -> set de meses
filas_u = []
for c in R.CULTIVARES:
    s = datos.serie(c).sort_index().astype(float)
    a_t = (s.shift(12) - s.shift(1)).abs() / s.shift(1)
    for an in R.VENTANAS:
        v = Ventana(an)
        # A
        hA = a_t[(a_t.index >= "2017-01") & (a_t.index <= v.origen)].dropna()
        # B
        pr = pd.read_csv(R.BR / "04_modelos" / "sarima_rolling" / c / str(an) / "predicciones.csv", dtype={"fecha": str})
        _, train, _ = _particiones(s, v)
        fit, _ = _ajustar(train.to_numpy(), CFG[c]["order"], CFG[c]["seasonal_order"], dict(CFG["opciones"]))
        ins = pd.Series(np.asarray(fit.predict(), float), index=train.index).iloc[QUEMADO:]
        val = pr[pr.particion == "val"].set_index("fecha").y_pred
        tst = pr[pr.particion == "test"].set_index("fecha").y_pred
        yhat = pd.concat([ins, val, tst])
        b_t = (yhat - s.shift(1).reindex(yhat.index)).abs() / s.shift(1).reindex(yhat.index)
        hB = b_t[b_t.index <= v.origen]
        for p in E.PCTS:
            uA, uB = umbral(hA, p), umbral(hB, p)
            mA = {m for m in v.meses_test if a_t[m] > uA}
            mB = {m for m in v.meses_test if b_t[m] > uB}
            mask.setdefault(("A_SN_anticipado", c, p), set()).update(mA)
            mask.setdefault(("B_SARIMA_anticipado", c, p), set()).update(mB)
            filas_u.append({"cultivo": c, "anio_test": an, "percentil": p, "umbral_A": uA, "n_hist_A": len(hA), "n_A": len(mA),
                            "umbral_B": uB, "n_hist_B": len(hB), "historia_B": f"{hB.index.min()}..{hB.index.max()}", "n_B": len(mB),
                            "meses_A": ";".join(sorted(mA)), "meses_B": ";".join(sorted(mB))})
U = pd.DataFrame(filas_u)
R.escribir(U, R.RES / "T8_umbrales_y_meses.csv")
ev_n = eventos_nino()
nino = {m for i, f in ev_n for m in pd.period_range(i, f, freq="M").astype(str)}
for c in R.CULTIVARES:
    mask[("C_Nino_costero", c, None)] = {m for m in nino if m[:4].isdigit() and 2021 <= int(m[:4]) <= 2025}

ES, ERR = E.errores(E.originales(), E.r2_dia1())
filas, rob_rows = [], []
for c in R.CULTIVARES:
    pv, cl, est, Dv = E.matriz(ERR, E.MOD12, c)
    real = E.mascara_mom(c)
    for dfn in ("A_SN_anticipado", "B_SARIMA_anticipado", "C_Nino_costero"):
        ps = [None] if dfn.startswith("C") else E.PCTS
        subs = {}
        for p in ps:
            sub = E.vec(cl, mask[(dfn, c, p)])
            subs[p] = sub
            r = E.resumen(pv, est, Dv, sub)
            rk = E.ranking(pv, est, sub).set_index("modelo")
            marcados = {f for (_, f), x in zip(cl, sub) if x}
            for x in r.itertuples():
                filas.append({"definicion": dfn, "cultivo": c, "percentil": p, "modelo": x.modelo, "n_meses": x.n_meses, "MAE": x.MAE,
                              "IC_lo": x.IC_lo, "IC_hi": x.IC_hi, "MASE": x.MASE, "posicion": rk.loc[x.modelo, "posicion"],
                              "primero_o_empate": bool(rk.loc[x.modelo, "primero"]),
                              "coinciden_con_shock_MoM_P75_real": len(marcados & real), "n_shock_MoM_P75_real": len(real)})
        if not dfn.startswith("C"):
            rb = E.robustez(pv, est, subs)
            rb.insert(0, "cultivo", c)
            rb.insert(0, "definicion", dfn)
            rob_rows.append(rb)
T8 = pd.DataFrame(filas)
R.escribir(T8, R.RES / "T8_metricas_ex_ante.csv")
RB = pd.concat(rob_rows, ignore_index=True)
R.escribir(RB, R.RES / "T8_robustez_ex_ante.csv")

NOM = {"A_SN_anticipado": "A. Cambio anticipado por Seasonal Naive", "B_SARIMA_anticipado": "B. Cambio anticipado por SARIMA fijo",
       "C_Nino_costero": "C. Meses de El Niño costero (lista oficial IGP/ENFEN, no ex ante)"}
txt = ["<!-- generado por t8_ex_ante.py -->", f"Eventos El Niño costero leídos de la lista IGP: {', '.join(f'{i}..{f}' for i, f in ev_n)}.", ""]
for dfn, nom in NOM.items():
    txt += [f"#### {nom}", ""]
    for c in R.CULTIVARES:
        d = E.DEC[c]
        q = T8[(T8.definicion == dfn) & (T8.cultivo == c)]
        pref = 75 if not dfn.startswith("C") else None
        q75 = q[q.percentil == pref] if pref else q[q.percentil.isna()]
        n75 = int(q75.n_meses.iloc[0])
        coin = int(q75.coinciden_con_shock_MoM_P75_real.iloc[0])
        extra = (f"n marcados (P50/P60/P75/P90): " + "/".join(str(int(q[q.percentil == p].n_meses.iloc[0])) for p in E.PCTS)
                 if pref else f"n marcados: {n75}")
        txt += [f"**{c}** — {extra}; de los {n75} meses {'P75 ' if pref else ''}marcados, {coin} son shock MoM P75 ex post "
                f"(de {int(q75.n_shock_MoM_P75_real.iloc[0])}).", ""]
        v = []
        for m in E.MOD12:
            x = q75[q75.modelo == m].iloc[0]
            fila = {"modelo": f"{m} †" if m in R.NUEVOS else m, "MAE (IC95)" + (" P75" if pref else ""): E.ic_txt(x.MAE, x.IC_lo, x.IC_hi, d),
                    "MASE": E.num(x.MASE, 2)}
            if pref:
                rb = RB[(RB.definicion == dfn) & (RB.cultivo == c) & (RB.modelo == m)].iloc[0]
                for p in E.PCTS:
                    fila[f"P{p}"] = rb[f"P{p}"]
                fila["1º/empate (de 4)"] = int(rb.primero_o_empate_de_4)
                fila["robusto"] = "Sí" if rb.consistently_top_ranked else "No"
            else:
                fila["posición"] = f"{int(x.posicion)}{'*' if x.primero_o_empate else ''}"
            v.append(fila)
        txt += [E.md(pd.DataFrame(v)), ""]
(R.RES / "tablas_T8.md").write_text("\n".join(txt) + "\n", encoding="utf-8", newline="\n")
print("escrito tablas_T8.md")
