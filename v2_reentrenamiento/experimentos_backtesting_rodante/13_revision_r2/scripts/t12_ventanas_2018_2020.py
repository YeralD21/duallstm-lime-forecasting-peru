"""R2-T12 (obs. 10e): ventanas descriptivas 2018-2020 de los tres modelos sin entrenamiento. POSTERIOR AL PROTOCOLO.

Naive, Seasonal Naive y Chronos (los unicos con predicciones en 2018-2020: los modelos entrenados necesitan >= 36 meses
de train, ventanas.json). Por cultivo y por ventana (2018, 2019, 2020) y, como referencia, en el pool 2018-2020:
MAE en todos los meses y en los meses de shock MoM P75 (mascaras del articulo, historia hasta el origen), IC 95 %
bootstrap pareado (meses remuestreados dentro de cada ventana, B = 10 000, semilla 42), MASE y posicion entre los tres
(* = primero o empatado: el IC 95 % de la diferencia con el mejor contiene 0).
Control: MAE, MAE_shock y n_shock por ventana deben coincidir con 06_metricas/agregadas/T17_descriptivo_2018_2020_*.csv.
Salidas: resultados/T12_ventanas_2018_2020.csv y tablas_T12.md.
Uso: python 13_revision_r2/scripts/t12_ventanas_2018_2020.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import r2lib as R  # noqa: E402
from lib.entorno import preparar_entorno  # noqa: E402

preparar_entorno()

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

import r2eval as E  # noqa: E402
from lib import evaluacion as ev  # noqa: E402

MODELOS = list(ev.SIN_AJUSTE)  # Naive, Seasonal Naive, Chronos
ANIOS = list(ev.VENTANAS_DESCRIPTIVAS)  # 2018, 2019, 2020
ERR = pd.read_csv(R.BR / "05_predicciones" / "errores_test_promediados_semillas.csv", dtype={"fecha": str})

filas = []
for c in E.CULT:
    for alcance, anios in [(str(a), [a]) for a in ANIOS] + [("2018-2020", ANIOS)]:
        pv, claves, est, Dv = E.matriz(ERR, MODELOS, c, anios)
        shock = E.vec(claves, E.mascara_mom(c, anios))
        for meses, sub in (("todos", np.ones(len(claves), bool)), ("shock_MoM_P75", shock)):
            res = E.resumen(pv, est, Dv, sub, MODELOS)
            rk = E.ranking(pv, est, sub, MODELOS).set_index("modelo") if sub.any() else None
            for r in res.itertuples(index=False):
                filas.append({"cultivo": c, "ventana": alcance, "meses": meses, "modelo": r.modelo, "n_meses": r.n_meses,
                              "MAE": r.MAE, "IC_lo": r.IC_lo, "IC_hi": r.IC_hi, "MASE": r.MASE,
                              "posicion": int(rk.loc[r.modelo, "posicion"]) if rk is not None else None,
                              "primero_o_empate": bool(rk.loc[r.modelo, "primero"]) if rk is not None else None})
T = pd.DataFrame(filas)

# control contra la tabla publicada T17
for c in E.CULT:
    t17 = pd.read_csv(R.BR / "06_metricas" / "agregadas" / f"T17_descriptivo_2018_2020_{c}.csv")
    for r in t17.itertuples(index=False):
        if r.modelo not in MODELOS:
            continue
        x = T[(T.cultivo == c) & (T.ventana == str(r.anio_test)) & (T.modelo == r.modelo)].set_index("meses")
        for col, val in (("todos", r.MAE), ("shock_MoM_P75", r.MAE_shock)):
            if not np.isclose(x.loc[col, "MAE"], val, rtol=1e-9, atol=1e-9):
                raise SystemExit(f"T12 {c} {r.anio_test} {r.modelo} {col}: {x.loc[col, 'MAE']} != T17 {val}")
        if int(x.loc["shock_MoM_P75", "n_meses"]) != int(r.n_shock):
            raise SystemExit(f"T12 {c} {r.anio_test} {r.modelo}: n_shock distinto de T17")
print("Control: MAE, MAE_shock y n_shock coinciden con T17_descriptivo_2018_2020 (18 filas).")

T.to_csv(R.RES / "T12_ventanas_2018_2020.csv", index=False, lineterminator="\n")

txt = ["<!-- generado por t12_ventanas_2018_2020.py -->",
       "#### T12 — Ventanas 2018–2020: modelos sin entrenamiento (MAE en t, IC 95 % bootstrap)", "",
       "* = primero o empatado con el primero entre los tres modelos. MASE vacío en 2018: no hay denominador "
       "(la historia hasta el origen no tiene 12 meses con y_(t−12)).", ""]
for c in E.CULT:
    d = E.DEC[c]
    x = T[T.cultivo == c]
    tab = []
    for (v, m), g in x.groupby(["ventana", "modelo"], sort=False):
        a, s = g.set_index("meses").loc["todos"], g.set_index("meses").loc["shock_MoM_P75"]
        tab.append({"ventana": v, "modelo": m, "MAE todos (IC95)": E.ic_txt(a.MAE, a.IC_lo, a.IC_hi, d) + ("*" if a.primero_o_empate else ""),
                    "MASE": E.num(a.MASE, 2), "n shock": int(s.n_meses),
                    "MAE shock MoM P75 (IC95)": E.ic_txt(s.MAE, s.IC_lo, s.IC_hi, d) + ("*" if s.primero_o_empate else "")})
    txt += [f"**{c}**", "", E.md(pd.DataFrame(tab)), ""]
(R.RES / "tablas_T12.md").write_text("\n".join(txt) + "\n", encoding="utf-8", newline="\n")
print("\n".join(txt))
