"""Etapa 09 (Fase D1): barrido de umbral P0, P10..P95, mensual e interanual (D-BR4, D-BR7), ventanas 2021-2025.

Solo recalcula mascaras sobre las predicciones congeladas. Por cultivo, tipo y percentil:
  - por modelo: MAE_shock, MAE_normal, Δs, razon shock/normal, n_shock agregado, posicion y "primero" (empate =
    IC 95 % del bootstrap pareado iid de la diferencia con el mejor, dentro de los meses de shock, por ventana);
  - por ventana: n_shock y marca de no informativa (< 2 shocks);
  - estabilizacion: percentil desde el cual el primer lugar ya no cambia y desde el cual todos los modelos empatan.
P0 (verificacion de codigo): todos los meses de test son shock; Δs debe ser exactamente 0 en cada modelo, ventana y
agregado. Si no, se detiene.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.entorno import BR, preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import json  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from lib import evaluacion as ev  # noqa: E402
from lib.integridad import Integridad  # noqa: E402
from lib.shocks import MIN_INFORMATIVA, PERCENTILES  # noqa: E402

T = ev.Tablas()
NOMBRE_C = {"sutil": "Sutil", "dulce": "Dulce"}
SAL = BR / "07_barrido_umbral"


def estabilizacion(tab: pd.DataFrame) -> dict:
    """tab: filas = percentiles en orden creciente; columnas 'mejor' y 'todos_empatan'."""
    ps = list(tab.index)
    desde_mejor = None
    for i, p in enumerate(ps):
        resto = tab.loc[ps[i:], "mejor"]
        if resto.notna().all() and resto.nunique() == 1:
            desde_mejor = p
            break
    desde_empate = None
    for i, p in enumerate(ps):
        if tab.loc[ps[i:], "todos_empatan"].all():
            desde_empate = p
            break
    return {"primer_lugar_estable_desde": desde_mejor,
            "modelo_estable": tab.loc[desde_mejor, "mejor"] if desde_mejor is not None else None,
            "todos_empatan_desde": desde_empate}


def main() -> None:
    Integridad().verificar()
    s = ev.series()
    es = ev.errores_por_semilla(ev.cargar_predicciones(), s, "test")
    err = ev.promediar_semillas(es)
    M = ev.mascaras(s, ev.VENTANAS_PRINCIPAL, PERCENTILES)
    filas, filas_v, est_rows, p0 = [], [], [], []
    for c in ev.CULTIVARES:
        pv = ev.matriz(err, ev.MODELOS_RANKING, c, ev.VENTANAS_PRINCIPAL)
        claves = list(pv.index)
        est = np.array([a for a, _ in claves])
        AE = pv.to_numpy().T
        for t in ("mensual", "interanual"):
            resumen = {}
            for p in PERCENTILES:
                sh = ev.vector_shock(claves, M, c, t, p)
                for a in ev.VENTANAS_PRINCIPAL:
                    n = int(sh[est == a].sum())
                    filas_v.append({"cultivar": c, "tipo": t, "percentil": p, "anio_test": a, "n_shock": n, "informativa": n >= MIN_INFORMATIVA})
                r = ev.ranking(AE, ev.MODELOS_RANKING, est, sh, "iid")
                for i, m in enumerate(ev.MODELOS_RANKING):
                    ae = AE[i]
                    mg = ae.mean()
                    ms = ae[sh].mean() if sh.any() else np.nan
                    mn = ae[~sh].mean() if (~sh).any() else np.nan
                    ds = (ms - mg) / mg * 100 if sh.any() else np.nan
                    rr = r.iloc[i]
                    filas.append({"cultivar": c, "tipo": t, "percentil": p, "modelo": m, "n_shock": int(sh.sum()),
                                  "MAE_shock": ms, "MAE_normal": mn, "Delta_s": ds, "razon_shock_normal": ms / mn if np.isfinite(mn) else np.nan,
                                  "posicion": rr.posicion, "primero": bool(rr.primero),
                                  "dif_vs_mejor_lo": rr.dif_vs_mejor_lo, "dif_vs_mejor_hi": rr.dif_vs_mejor_hi})
                    if p == 0:
                        for a in ev.VENTANAS_PRINCIPAL:
                            w = est == a
                            dsw = (ae[w][sh[w]].mean() - ae[w].mean()) / ae[w].mean() * 100
                            p0.append({"cultivar": c, "tipo": t, "modelo": m, "ventana": str(a), "n_shock": int(sh[w].sum()), "Delta_s": float(dsw)})
                        p0.append({"cultivar": c, "tipo": t, "modelo": m, "ventana": "agregado", "n_shock": int(sh.sum()), "Delta_s": float(ds)})
                mejor = r.loc[r.MAE.idxmin(), "modelo"] if sh.any() else None
                resumen[p] = {"mejor": mejor, "todos_empatan": bool(r.primero.all()) if sh.any() else False}
            e = estabilizacion(pd.DataFrame.from_dict(resumen, orient="index"))
            est_rows.append({"cultivar": c, "tipo": t, **e})
    t = pd.DataFrame(filas)
    tv = pd.DataFrame(filas_v)
    te = pd.DataFrame(est_rows)
    tp0 = pd.DataFrame(p0)
    tp0["Delta_s_es_0_exacto"] = tp0.Delta_s == 0.0
    tp0["n_shock_esperado"] = np.where(tp0.ventana == "agregado", 60, 12)
    ok_p0 = bool(tp0.Delta_s_es_0_exacto.all() and (tp0.n_shock == tp0.n_shock_esperado).all())
    for sub in ("mensual", "interanual"):
        (SAL / sub).mkdir(parents=True, exist_ok=True)
        t[t.tipo == sub].to_csv(SAL / sub / "barrido_por_modelo.csv", index=False, float_format="%.10g")
        tv[tv.tipo == sub].to_csv(SAL / sub / "n_shock_por_ventana.csv", index=False)
    te.to_csv(SAL / "estabilizacion.csv", index=False)
    tp0.to_csv(SAL / "comprobacion_P0.csv", index=False, float_format="%.17g")
    (SAL / "comprobacion_P0.json").write_text(json.dumps({"OK": ok_p0, "n_comprobaciones": len(tp0),
                                                          "max_abs_Delta_s": float(tp0.Delta_s.abs().max())}, indent=2), encoding="utf-8")
    if not ok_p0:
        raise SystemExit("P0: Δs no es exactamente 0 en algun caso: error de codigo, se detiene.")

    # Vistas de texto/LaTeX
    for c in ev.CULTIVARES:
        for tipo in ("mensual", "interanual"):
            v = t[(t.cultivar == c) & (t.tipo == tipo)]
            pos = v.pivot(index="modelo", columns="percentil", values="posicion").reindex(ev.MODELOS_RANKING)
            pri = v.pivot(index="modelo", columns="percentil", values="primero").reindex(ev.MODELOS_RANKING)
            vista = pd.DataFrame({"modelo": ev.MODELOS_RANKING})
            for p in PERCENTILES:
                vista[f"P{p}"] = [("—" if pd.isna(x) else f"{int(x)}{'*' if y else ''}") for x, y in zip(pos[p], pri[p])]
            ns = v.drop_duplicates("percentil").set_index("percentil")["n_shock"]
            pie = pd.DataFrame([["n_shock"] + [str(int(ns[p])) for p in PERCENTILES]], columns=vista.columns)
            T.guardar(pd.concat([vista, pie], ignore_index=True), f"07_barrido_umbral/{tipo}", f"T_barrido_posiciones_{tipo}_{c}",
                      f"Posición por MAE_shock en cada percentil, {tipo}, {NOMBRE_C[c]}, 2021-2025 (* = primero o empatado con el primero)")
            ds = v.pivot(index="modelo", columns="percentil", values="Delta_s").reindex(ev.MODELOS_RANKING).reset_index()
            ds.columns = ["modelo"] + [f"P{p}" for p in PERCENTILES]
            T.guardar(ds, f"07_barrido_umbral/{tipo}", f"T_barrido_delta_s_{tipo}_{c}",
                      f"Δs (%) por percentil, {tipo}, {NOMBRE_C[c]}, 2021-2025", dec=0)
            nv = tv[(tv.cultivar == c) & (tv.tipo == tipo)].pivot(index="anio_test", columns="percentil", values="n_shock").reset_index()
            nv.columns = ["ventana"] + [f"P{p}" for p in PERCENTILES]
            T.guardar(nv, f"07_barrido_umbral/{tipo}", f"T_barrido_n_shock_{tipo}_{c}",
                      f"n_shock por ventana y percentil, {tipo}, {NOMBRE_C[c]} (< 2 = ventana no informativa)", mostrar=False)
    T.guardar(te, "07_barrido_umbral", "T_barrido_estabilizacion",
              "Estabilización del ranking por MAE_shock (percentil desde el cual el primer lugar no cambia / todos empatan)")
    resumen_p0 = tp0.groupby(["cultivar", "tipo"]).agg(comprobaciones=("Delta_s", "size"), max_abs_Delta_s=("Delta_s", lambda x: float(x.abs().max())),
                                                     todos_cero_exacto=("Delta_s_es_0_exacto", "all")).reset_index()
    T.guardar(resumen_p0, "07_barrido_umbral", "T_comprobacion_P0", "Comprobación de P0 con datos reales: Δs debe ser exactamente 0", dec=3)
    T.escribir_texto(BR / "09_reportes" / "tablas_fase_D1_09.md")
    print(f"09_barrido_umbral: OK (P0: {len(tp0)} comprobaciones, Delta_s = 0 exacto en todas)")


if __name__ == "__main__":
    main()
