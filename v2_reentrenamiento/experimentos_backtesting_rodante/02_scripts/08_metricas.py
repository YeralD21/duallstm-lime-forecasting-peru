"""Etapa 08 (Fase D1): metricas, bootstrap, Diebold-Mariano-HLN, ablacion NLP, descripcion de series y diagnostico.

Solo lee las predicciones congeladas de la Fase C (05_predicciones/, 04_modelos/) y 03_ventanas/; no reentrena.
Exige antes que tests/test_equivalencia_metricas_2025.py haya dado OK.
Cada tabla se guarda en CSV (precision completa), en LaTeX (06_metricas/tablas_latex/) y en texto
(09_reportes/tablas_fase_D1.md). Conjuntos: principal 2021-2025; sensibilidad 2023-2025; 2018-2020 solo descriptivo
para Naive, Seasonal Naive y Chronos. XGB-43: exploratorio, tabla aparte (T16), fuera del ranking.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.entorno import BR, CONFIG, preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import itertools  # noqa: E402
import json  # noqa: E402
import warnings  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from lib import evaluacion as ev  # noqa: E402
from lib.integridad import Integridad  # noqa: E402
from lib.ventanas import Ventana  # noqa: E402

UMB = json.loads((CONFIG / "umbrales.json").read_text(encoding="utf-8"))
T = ev.Tablas()
TIPOS = ("mensual", "interanual")
CONJUNTOS = {"principal_2021_2025": ev.VENTANAS_PRINCIPAL, "sensibilidad_2023_2025": ev.VENTANAS_SENSIBILIDAD}
NOMBRE_C = {"sutil": "Sutil", "dulce": "Dulce"}


def f_ic(lo, hi, dec=1) -> str:
    return "—" if not np.isfinite(lo) else f"[{lo:,.{dec}f}; {hi:,.{dec}f}]"


def dec_de(c: str) -> int:
    return 0 if c == "sutil" else 1


def main() -> None:
    Integridad().verificar()
    eq = json.loads((BR / "06_metricas" / "reproducibilidad" / "metricas_2025_vs_oficial.json").read_text(encoding="utf-8"))
    if not eq["OK"]:
        raise SystemExit("La comprobacion de 2025 no dio OK: no se calculan metricas.")
    pred = ev.cargar_predicciones()
    s = ev.series()
    es = ev.errores_por_semilla(pred, s, "test")
    err = ev.promediar_semillas(es)
    Dt = ev.denominadores_mase()
    D = {(r.cultivar, int(r.anio_test)): float(r.D_mase) for r in Dt.itertuples()}
    M = ev.mascaras(s, range(2018, 2026), ev.PUNTOS_REPORTE)
    todos = ev.MODELOS_RANKING + ev.EXPLORATORIOS

    # (a) consolidado ----------------------------------------------------------------------------------------
    pred.to_csv(BR / "05_predicciones" / "predicciones_consolidadas.csv", index=False, float_format="%.17g")
    err.to_csv(BR / "05_predicciones" / "errores_test_promediados_semillas.csv", index=False, float_format="%.17g")
    resumen_a = err.groupby(["modelo"]).agg(ventanas=("anio_test", lambda x: f"{x.min()}–{x.max()}"),
                                            meses_test=("fecha", "size"), semillas=("n_semillas", "max")).reset_index()
    resumen_a["modelo"] = pd.Categorical(resumen_a.modelo, categories=todos, ordered=True)
    resumen_a = resumen_a.sort_values("modelo")
    T.guardar(resumen_a, "05_predicciones", "Ta_consolidado_resumen",
              "Consolidado de predicciones de test: error absoluto promediado entre semillas (D-BR6)")

    def D_vec(c, claves):
        return np.array([D[(c, a)] for a, _ in claves])

    # (b, c) metricas por ventana (T05) y descriptivo 2018-2020 (T17) -----------------------------------------
    filas = []
    for c in ev.CULTIVARES:
        for m in todos:
            anios = range(2018, 2026) if m in ev.SIN_AJUSTE else ev.VENTANAS_PRINCIPAL
            for a in anios:
                pv = ev.matriz(err, [m], c, [a])
                claves, ae = list(pv.index), pv[m].to_numpy()
                rm = ev.rmse_semillas(es, m, c, [a])
                for t in TIPOS:
                    for p in ev.PUNTOS_REPORTE:
                        k = ev.metricas(ae, ev.vector_shock(claves, M, c, t, p), D_vec(c, claves), rm)
                        filas.append({"cultivar": c, "modelo": m, "anio_test": a, "tipo": t, "percentil": p, **k,
                                      "informativa": k["n_shock"] >= UMB["minimo_shocks_ventana_informativa"],
                                      "conjunto": "principal" if a >= 2021 else "descriptivo_2018_2020",
                                      "exploratorio": m in ev.EXPLORATORIOS})
    t05 = pd.DataFrame(filas)
    t05.to_csv(BR / "06_metricas" / "por_ventana" / "T05_metricas_por_ventana.csv", index=False, float_format="%.10g")
    for c in ev.CULTIVARES:
        v = t05[(t05.cultivar == c) & (t05.tipo == "mensual") & (t05.percentil == 75) & (t05.anio_test >= 2021)]
        for col, nom in (("MAE", "MAE"), ("MAE_shock", "MAE_shock")):
            piv = v.pivot(index="modelo", columns="anio_test", values=col).reindex(todos).reset_index()
            piv.columns = ["modelo"] + [str(x) for x in piv.columns[1:]]
            ns = v.drop_duplicates("anio_test").set_index("anio_test")["n_shock"]
            if col == "MAE_shock":
                piv.columns = ["modelo"] + [f"{a} (n={ns[int(a)]})" for a in piv.columns[1:]]
            T.guardar(piv, "06_metricas/por_ventana", f"T05_{col}_P75_por_ventana_{c}",
                      f"{nom} por ventana, P75 mensual, {NOMBRE_C[c]} (t)", dec=dec_de(c))
        v = t05[(t05.cultivar == c) & (t05.tipo == "mensual") & (t05.percentil == 75) & (t05.anio_test <= 2020)]
        vista = v[["modelo", "anio_test", "MAE", "RMSE", "MASE", "MAE_normal", "MAE_shock", "n_shock", "Delta_s", "informativa"]]
        T.guardar(vista, "06_metricas/agregadas", f"T17_descriptivo_2018_2020_{c}",
                  f"Descriptivo 2018-2020 (sin ranking), modelos sin entrenamiento, P75 mensual, {NOMBRE_C[c]}", dec=dec_de(c))

    # (b, c, d) agregadas con IC (T06), ranking (T08), robustez ------------------------------------------------
    filas6, filas8 = [], []
    for nom_conj, anios in CONJUNTOS.items():
        for c in ev.CULTIVARES:
            pv = ev.matriz(err, todos, c, anios)
            claves = list(pv.index)
            est = np.array([a for a, _ in claves])
            AE = pv.to_numpy().T
            Dv = D_vec(c, claves)
            rms = {m: ev.rmse_semillas(es, m, c, anios) for m in todos}
            for t in TIPOS:
                for p in ev.PUNTOS_REPORTE:
                    sh = ev.vector_shock(claves, M, c, t, p)
                    boots = {}
                    rng = lambda: np.random.default_rng(ev.SEMILLA_BOOT)  # noqa: E731
                    boots["iid_global"] = AE[:, ev.indices_iid(est, np.ones_like(sh), rng())].mean(axis=2)
                    boots["iid_shock"] = AE[:, ev.indices_iid(est, sh, rng())].mean(axis=2) if sh.any() else None
                    boots["iid_normal"] = AE[:, ev.indices_iid(est, ~sh, rng())].mean(axis=2) if (~sh).any() else None
                    ib = ev.indices_bloques(est, rng())
                    boots["bloq_global"] = AE[:, ib].mean(axis=2)
                    boots["bloq_shock"] = ev.remuestrear(AE, sh, ib)
                    boots["bloq_normal"] = ev.remuestrear(AE, ~sh, ib)
                    for i, m in enumerate(todos):
                        k = ev.metricas(AE[i], sh, Dv, rms[m])
                        fila = {"conjunto": nom_conj, "cultivar": c, "tipo": t, "percentil": p, "modelo": m, **k,
                                "exploratorio": m in ev.EXPLORATORIOS}
                        for nb, bt in boots.items():
                            lo, hi = ev.ic(bt[i]) if bt is not None else (np.nan, np.nan)
                            fila[f"{nb}_lo"], fila[f"{nb}_hi"] = lo, hi
                        if boots["bloq_shock"] is not None:
                            fila["bloq_shock_remuestreos_sin_shock"] = int(np.isnan(boots["bloq_shock"][i]).sum())
                        filas6.append(fila)
                    idx_r = [todos.index(m) for m in ev.MODELOS_RANKING]
                    for crit, sub in (("shock", sh), ("normal", ~sh)):
                        for tb in ("iid", "bloques"):
                            r = ev.ranking(AE[idx_r], ev.MODELOS_RANKING, est, sub, tb)
                            r.insert(0, "bootstrap", tb)
                            r.insert(0, "criterio", crit)
                            r.insert(0, "percentil", p)
                            r.insert(0, "tipo", t)
                            r.insert(0, "cultivar", c)
                            r.insert(0, "conjunto", nom_conj)
                            filas8.append(r)
    t06 = pd.DataFrame(filas6)
    t06.to_csv(BR / "06_metricas" / "agregadas" / "T06_agregadas_IC.csv", index=False, float_format="%.10g")
    t08 = pd.concat(filas8, ignore_index=True)
    t08.to_csv(BR / "06_metricas" / "agregadas" / "T08_ranking_empates.csv", index=False, float_format="%.10g")

    for nom_conj in CONJUNTOS:
        for c in ev.CULTIVARES:
            d = dec_de(c)
            v = t06[(t06.conjunto == nom_conj) & (t06.cultivar == c) & (t06.tipo == "mensual") & (t06.percentil == 75)
                    & ~t06.exploratorio]
            vista = pd.DataFrame({
                "modelo": v.modelo, "MAE": v.MAE, "IC95 MAE": [f_ic(a, b, d) for a, b in zip(v.iid_global_lo, v.iid_global_hi)],
                "MAE normal": v.MAE_normal, "IC95 normal": [f_ic(a, b, d) for a, b in zip(v.iid_normal_lo, v.iid_normal_hi)],
                "MAE shock": v.MAE_shock, "IC95 shock": [f_ic(a, b, d) for a, b in zip(v.iid_shock_lo, v.iid_shock_hi)],
                "IC95 shock (bloques)": [f_ic(a, b, d) for a, b in zip(v.bloq_shock_lo, v.bloq_shock_hi)],
                "n shock": v.n_shock, "Δs %": v.Delta_s, "shock/normal": v.razon_shock_normal, "MASE": v.MASE, "RMSE": v.RMSE})
            etiqueta = "2021-2025" if nom_conj.startswith("principal") else "2023-2025 (sensibilidad)"
            T.guardar(vista, "06_metricas/agregadas", f"T06_agregadas_P75_{nom_conj}_{c}",
                      f"Métricas agregadas {etiqueta}, P75 mensual, {NOMBRE_C[c]} (t; IC bootstrap pareado 95 %)", dec=d)
            # Ranking en los 4 puntos de reporte + regla de robustez (D-BR7 con enmienda E-BR1)
            r = t08[(t08.conjunto == nom_conj) & (t08.cultivar == c) & (t08.bootstrap == "iid")]
            tab = pd.DataFrame({"modelo": list(ev.MODELOS_RANKING)})
            for crit in ("shock", "normal"):
                for t in TIPOS:
                    cuenta = np.zeros(len(tab), int)
                    for p in ev.PUNTOS_REPORTE:
                        rr = r[(r.criterio == crit) & (r.tipo == t) & (r.percentil == p)].set_index("modelo").reindex(tab.modelo)
                        tab[f"{crit[:2]}-{t[:3]}-P{p}"] = [f"{int(x)}{'*' if y else ''}" for x, y in zip(rr.posicion, rr.primero)]
                        cuenta += rr.primero.to_numpy(int)
                    tab[f"{crit[:2]}-{t[:3]} primero en"] = cuenta
                    if crit == "shock":
                        tab[f"robusto {t[:3]}"] = cuenta >= 3
            rb = t08[(t08.conjunto == nom_conj) & (t08.cultivar == c) & (t08.bootstrap == "bloques") & (t08.criterio == "shock") & (t08.tipo == "mensual")]
            tab["robusto men (bloques)"] = rb.groupby("modelo").primero.sum().reindex(tab.modelo).to_numpy() >= 3
            cols_sh = ["modelo"] + [x for x in tab.columns if x.startswith("sh-")] + ["robusto men", "robusto int", "robusto men (bloques)"]
            cols_no = ["modelo"] + [x for x in tab.columns if x.startswith("no-")]
            T.guardar(tab[cols_sh], "06_metricas/agregadas", f"T08_ranking_shock_{nom_conj}_{c}",
                      f"Ranking por MAE_shock ({etiqueta}, {NOMBRE_C[c]}): posición; * = primero o empatado con el primero (IC95 iid de la diferencia contiene 0)")
            T.guardar(tab[cols_no], "06_metricas/agregadas", f"T08_ranking_normal_{nom_conj}_{c}",
                      f"Ranking por MAE normal ({etiqueta}, {NOMBRE_C[c]}): posición; * = primero o empatado")

    # (e) Diebold-Mariano-HLN (T09) ---------------------------------------------------------------------------
    filas9 = []
    for nom_conj, anios in CONJUNTOS.items():
        for c in ev.CULTIVARES:
            pv = ev.matriz(err, ev.MODELOS_RANKING, c, anios)
            claves = list(pv.index)
            sh = ev.vector_shock(claves, M, c, "mensual", 75)
            for alcance, sel in (("global", np.ones(len(claves), bool)), ("shock_P75_mensual", sh)):
                for a_, b_ in itertools.combinations(ev.MODELOS_RANKING, 2):
                    k = ev.dm_hln(pv[a_].to_numpy()[sel], pv[b_].to_numpy()[sel])
                    filas9.append({"conjunto": nom_conj, "cultivar": c, "alcance": alcance, "modelo_A": a_, "modelo_B": b_, **k})
    t09 = pd.DataFrame(filas9)
    # EXPLORATORIO (DESV-07): Holm sobre los 45 pares de cada familia (conjunto x cultivo x alcance)
    from statsmodels.stats.multitest import multipletests

    t09["p_holm_exploratorio"] = np.nan
    for _, idx in t09.groupby(["conjunto", "cultivar", "alcance"]).groups.items():
        sub = t09.loc[idx]
        ok = sub.p.notna()
        if ok.any():
            t09.loc[sub.index[ok], "p_holm_exploratorio"] = multipletests(sub.p[ok].to_numpy(), method="holm")[1]
    t09["n_pares_familia_holm"] = t09.groupby(["conjunto", "cultivar", "alcance"]).p.transform(lambda x: int(x.notna().sum()))
    t09.to_csv(BR / "06_metricas" / "significancia" / "T09_diebold_mariano_hln.csv", index=False, float_format="%.10g")
    abrev = {"Naive": "Nv", "Seasonal Naive": "SN", "Chronos": "Chr", "SARIMA": "SAR", "SARIMA-sel": "SSel", "Ridge": "Rdg",
             "ElasticNet": "EN", "XGB-37": "X37", "GC3": "GC3", "GE": "GE"}
    for col_p, sufijo, etiqueta in (("p", "", "p-valor sin ajustar"),
                                    ("p_holm_exploratorio", "_holm", "p-valor ajustado por Holm (EXPLORATORIO, DESV-07; familia = 45 pares)")):
        for nom_conj in CONJUNTOS:
            for c in ev.CULTIVARES:
                mat = pd.DataFrame("—", index=ev.MODELOS_RANKING, columns=[abrev[m] for m in ev.MODELOS_RANKING])
                for r in t09[(t09.conjunto == nom_conj) & (t09.cultivar == c)].itertuples():
                    i, j = ev.MODELOS_RANKING.index(r.modelo_A), ev.MODELOS_RANKING.index(r.modelo_B)
                    pv_ = getattr(r, col_p)
                    # signo respecto a la FILA: "+" = el modelo de la fila tiene mas error medio que el de la columna
                    if not np.isfinite(pv_):
                        continue
                    if r.alcance == "global":   # triangulo inferior: fila = B, columna = A; d = A - B
                        mat.iloc[j, i] = f"{pv_:.3f}{'+' if r.d_media < 0 else '−'}"
                    else:                       # triangulo superior: fila = A, columna = B
                        mat.iloc[i, j] = f"{pv_:.3f}{'+' if r.d_media > 0 else '−'}"
                mat.insert(0, "modelo", ev.MODELOS_RANKING)
                n_s = int(t09[(t09.conjunto == nom_conj) & (t09.cultivar == c) & (t09.alcance != "global")].n.iloc[0])
                n_g = int(t09[(t09.conjunto == nom_conj) & (t09.cultivar == c) & (t09.alcance == "global")].n.iloc[0])
                T.guardar(mat, "06_metricas/significancia", f"T09_DM{sufijo}_matriz_{nom_conj}_{c}",
                          f"DM-HLN, {etiqueta} ({nom_conj}, {NOMBRE_C[c]}). Bajo la diagonal: global (n={n_g}); sobre la diagonal: "
                          f"solo shocks P75 mensual (n={n_s}). Signo: + = el modelo de la fila tiene más error que el de la columna")
    resumen_holm = t09.assign(sig_p=t09.p < 0.05, sig_holm=t09.p_holm_exploratorio < 0.05).groupby(
        ["conjunto", "cultivar", "alcance"]).agg(pares=("p", lambda x: int(x.notna().sum())), p_menor_005=("sig_p", "sum"),
                                                 holm_menor_005=("sig_holm", "sum")).reset_index()
    T.guardar(resumen_holm, "06_metricas/significancia", "T09_holm_resumen",
              "EXPLORATORIO (DESV-07): pares con p < 0,05 antes y después de Holm, por familia")

    # (g) ablacion GE - GC3 emparejada por semilla (T11) ------------------------------------------------------
    filas11 = []
    for c in ev.CULTIVARES:
        for nom_conj, anios in {**{str(a): (a,) for a in ev.VENTANAS_PRINCIPAL}, **CONJUNTOS}.items():
            sub = es[(es.cultivar == c) & es.anio_test.isin(anios) & es.modelo.isin(["GC3", "GE"])]
            w = sub.pivot_table(index=["anio_test", "fecha", "semilla"], columns="modelo", values="ae").reset_index()
            w["dif"] = w.GE - w.GC3
            claves = sorted(set(zip(w.anio_test, w.fecha)))
            sh = ev.vector_shock(claves, M, c, "mensual", 75)
            mapa_sh = dict(zip(claves, sh))
            w["shock"] = [mapa_sh[(a, f)] for a, f in zip(w.anio_test, w.fecha)]
            difm = w.groupby(["anio_test", "fecha"]).dif.mean().reindex(pd.MultiIndex.from_tuples(claves)).to_numpy()
            est = np.array([a for a, _ in claves])
            for alcance, sel in (("global", np.ones(len(claves), bool)), ("shock_P75", sh), ("normal_P75", ~sh)):
                if not sel.any():
                    filas11.append({"cultivar": c, "conjunto": nom_conj, "alcance": alcance, "n_meses": 0})
                    continue
                ws = w[w.shock] if alcance == "shock_P75" else (w[~w.shock] if alcance == "normal_P75" else w)
                por_sem = ws.groupby("semilla").dif.mean()
                bt = difm[ev.indices_iid(est, sel, np.random.default_rng(ev.SEMILLA_BOOT))].mean(axis=1)
                lo, hi = ev.ic(bt)
                filas11.append({"cultivar": c, "conjunto": nom_conj, "alcance": alcance, "n_meses": int(sel.sum()),
                                "dif_media_GE_menos_GC3": float(difm[sel].mean()), "IC95_lo": lo, "IC95_hi": hi,
                                "sd_entre_semillas": float(por_sem.std()), "min_semilla": float(por_sem.min()),
                                "max_semilla": float(por_sem.max()), "semillas_GE_mejor": int((por_sem < 0).sum()),
                                **{f"seed_{int(k):02d}": float(v) for k, v in por_sem.items()}})
    t11 = pd.DataFrame(filas11)
    t11.to_csv(BR / "06_metricas" / "ablacion_nlp" / "T11_ablacion_GE_menos_GC3.csv", index=False, float_format="%.10g")
    for c in ev.CULTIVARES:
        d = dec_de(c)
        v = t11[t11.cultivar == c]
        vista = pd.DataFrame({"conjunto": v.conjunto, "alcance": v.alcance, "n meses": v.n_meses,
                              "GE−GC3 (t)": v.dif_media_GE_menos_GC3,
                              "IC95": [f_ic(a, b, d) for a, b in zip(v.IC95_lo, v.IC95_hi)],
                              "DE semillas": v.sd_entre_semillas, "semillas GE mejor (de 10)": v.semillas_GE_mejor.astype("Int64")})
        T.guardar(vista, "06_metricas/ablacion_nlp", f"T11_ablacion_{c}",
                  f"Ablación NLP: MAE(GE) − MAE(GC3) emparejado por semilla, {NOMBRE_C[c]} (t; negativo = GE mejor)", dec=d)

    # (c) Δs quitando un mes de shock (T12) -------------------------------------------------------------------
    filas12 = []
    for c in ev.CULTIVARES:
        for m in todos:
            for a in (*ev.VENTANAS_PRINCIPAL, "agregado_2021_2025"):
                anios = ev.VENTANAS_PRINCIPAL if a == "agregado_2021_2025" else (a,)
                pv = ev.matriz(err, [m], c, anios)
                claves = list(pv.index)
                sh = ev.vector_shock(claves, M, c, "mensual", 75)
                ae = pv[m].to_numpy()
                completo = (ae[sh].mean() - ae.mean()) / ae.mean() * 100 if sh.any() else np.nan
                loo = ev.delta_s_loo(ae, sh)
                meses = [f for (aa, f), x in zip(claves, sh) if x]
                filas12.append({"cultivar": c, "modelo": m, "ventana": str(a), "n_shock": int(sh.sum()), "Delta_s": completo,
                                "Delta_s_loo_min": float(np.nanmin(loo)) if len(loo) else np.nan,
                                "Delta_s_loo_max": float(np.nanmax(loo)) if len(loo) else np.nan,
                                "mes_que_mas_cambia": meses[int(np.nanargmax(np.abs(loo - completo)))] if len(loo) else None,
                                "Delta_s_loo": ";".join(f"{f}:{x:.4f}" for f, x in zip(meses, loo)),
                                "exploratorio": m in ev.EXPLORATORIOS})
    t12 = pd.DataFrame(filas12)
    t12.to_csv(BR / "06_metricas" / "agregadas" / "T12_delta_s_quitando_un_shock.csv", index=False, float_format="%.10g")
    for c in ev.CULTIVARES:
        v = t12[(t12.cultivar == c) & (t12.ventana == "agregado_2021_2025") & ~t12.exploratorio]
        T.guardar(v[["modelo", "n_shock", "Delta_s", "Delta_s_loo_min", "Delta_s_loo_max", "mes_que_mas_cambia"]],
                  "06_metricas/agregadas", f"T12_loo_agregado_{c}",
                  f"Δs (%) agregado 2021-2025 quitando un mes de shock P75 a la vez, {NOMBRE_C[c]}", dec=1)

    # (c) MASE ya en T05/T06. MAE por cuartiles y tercios de |Δy/y| (T13) -------------------------------------
    filas13 = []
    for c in ev.CULTIVARES:
        r = (s[c] - s[c].shift(1)).abs() / s[c].shift(1)
        pv = ev.matriz(err, todos, c, ev.VENTANAS_PRINCIPAL)
        rv = np.array([r[f] for _, f in pv.index])
        for nq, nombre in ((4, "cuartil"), (3, "tercio")):
            q = pd.qcut(rv, nq, labels=False)
            bordes = np.quantile(rv, np.linspace(0, 1, nq + 1))
            for k in range(nq):
                sel = q == k
                for m in todos:
                    filas13.append({"cultivar": c, "agrupacion": nombre, "grupo": k + 1,
                                    "rango_cambio": f"{bordes[k]:.3f}-{bordes[k + 1]:.3f}", "n_meses": int(sel.sum()),
                                    "modelo": m, "MAE": float(pv[m].to_numpy()[sel].mean()), "exploratorio": m in ev.EXPLORATORIOS})
    t13 = pd.DataFrame(filas13)
    t13.to_csv(BR / "06_metricas" / "agregadas" / "T13_mae_por_cuartil_cambio.csv", index=False, float_format="%.10g")
    for c in ev.CULTIVARES:
        v = t13[(t13.cultivar == c) & (t13.agrupacion == "cuartil") & ~t13.exploratorio]
        piv = v.pivot(index="modelo", columns="grupo", values="MAE").reindex(ev.MODELOS_RANKING).reset_index()
        rangos = v.drop_duplicates("grupo").set_index("grupo")["rango_cambio"]
        piv.columns = ["modelo"] + [f"Q{g} ({rangos[g]})" for g in piv.columns[1:]]
        T.guardar(piv, "06_metricas/agregadas", f"T13_cuartiles_{c}",
                  f"MAE por cuartil de |Δy/y| mensual en test 2021-2025 (15 meses por cuartil), {NOMBRE_C[c]} (t)", dec=dec_de(c))

    # T07 por semilla -----------------------------------------------------------------------------------------
    filas7 = []
    for c in ev.CULTIVARES:
        for m in ev.CON_SEMILLA:
            for a in (*ev.VENTANAS_PRINCIPAL, "agregado_2021_2025"):
                anios = ev.VENTANAS_PRINCIPAL if a == "agregado_2021_2025" else (a,)
                sub = es[(es.modelo == m) & (es.cultivar == c) & es.anio_test.isin(anios)]
                for sem, g in sub.groupby("semilla"):
                    claves = list(zip(g.anio_test, g.fecha))
                    sh = ev.vector_shock(claves, M, c, "mensual", 75)
                    k = ev.metricas(g.ae.to_numpy(), sh, D_vec(c, claves), float(np.sqrt(np.mean(g.e.to_numpy() ** 2))))
                    filas7.append({"cultivar": c, "modelo": m, "ventana": str(a), "semilla": int(sem), **k})
    t07 = pd.DataFrame(filas7)
    t07.to_csv(BR / "06_metricas" / "por_semilla" / "T07_metricas_por_semilla.csv", index=False, float_format="%.10g")
    v = t07[t07.ventana == "agregado_2021_2025"].groupby(["cultivar", "modelo"]).agg(
        MAE_media=("MAE", "mean"), MAE_DE=("MAE", "std"), MAE_min=("MAE", "min"), MAE_max=("MAE", "max"),
        MAE_shock_media=("MAE_shock", "mean"), MAE_shock_DE=("MAE_shock", "std"), Delta_s_media=("Delta_s", "mean"),
        Delta_s_DE=("Delta_s", "std")).reset_index()
    T.guardar(v, "06_metricas/por_semilla", "T07_dispersion_semillas",
              "Dispersión entre las 10 semillas, agregado 2021-2025, P75 mensual (t; fuera de los IC, D-BR6)", dec=1)

    # (i) diagnostico de ajuste (T15) y mejor epoca -----------------------------------------------------------
    tr = ev.errores_por_semilla(pred, s, "train")
    va = ev.errores_por_semilla(pred, s, "val")
    nv_tr, nv_va = tr[tr.modelo == "Naive"], va[va.modelo == "Naive"]
    filas15 = []
    for m in ("Ridge", "ElasticNet", "XGB-37", "GC3", "GE", "XGB-43"):
        for (c, a, sem), g in tr[tr.modelo == m].groupby(["cultivar", "anio_test", tr.semilla.fillna(-1)]):
            gv = va[(va.modelo == m) & (va.cultivar == c) & (va.anio_test == a) & (va.semilla.fillna(-1) == sem)]
            n_tr = nv_tr[(nv_tr.cultivar == c) & (nv_tr.anio_test == a) & nv_tr.fecha.isin(g.fecha)]
            n_va = nv_va[(nv_va.cultivar == c) & (nv_va.anio_test == a) & nv_va.fecha.isin(gv.fecha)]
            if len(n_tr) != len(g) or len(n_va) != len(gv):
                raise AssertionError(f"Naive no cubre los meses de train/val de {m} {c} {a}")
            mt, mv, nt, nvv = g.ae.mean(), gv.ae.mean(), n_tr.ae.mean(), n_va.ae.mean()
            filas15.append({"modelo": m, "cultivar": c, "anio_test": int(a), "semilla": None if sem == -1 else int(sem),
                            "train_inicio": g.fecha.min(), "n_train": len(g), "n_val": len(gv), "MAE_train": mt, "MAE_val": mv,
                            "razon_val_train": mv / mt, "sobreajuste_razon_gt_2": mv / mt > 2.0,
                            "Naive_MAE_train": nt, "Naive_MAE_val": nvv, "Naive_razon": nvv / nt,
                            "no_supera_naive": bool(mt >= nt or mv >= nvv), "no_supera_naive_train": bool(mt >= nt),
                            "no_supera_naive_val": bool(mv >= nvv), "exploratorio": m in ev.EXPLORATORIOS})
    t15 = pd.DataFrame(filas15)
    ep = []
    for f in (BR / "04_modelos").glob("*_lstm_*/*/*/seed_*/estado_final.json"):
        d = json.loads(f.read_text(encoding="utf-8"))
        ep.append({"modelo": d["modelo"], "cultivar": d["cultivar"], "anio_test": d["anio_test"], "semilla": d["semilla"],
                   "mejor_epoca": d["mejor_epoca"], "epocas_corridas": d["epocas_corridas"]})
    ep = pd.DataFrame(ep)
    t15 = t15.merge(ep, on=["modelo", "cultivar", "anio_test", "semilla"], how="left")
    t15.to_csv(BR / "06_metricas" / "por_semilla" / "T15_diagnostico_ajuste.csv", index=False, float_format="%.10g")
    for c in ev.CULTIVARES:
        g = t15[t15.cultivar == c].groupby(["modelo", "anio_test"], sort=False)
        v = g.agg(MAE_train=("MAE_train", "mean"), MAE_val=("MAE_val", "mean"), razon_mediana=("razon_val_train", "median"),
                  sobreajuste=("sobreajuste_razon_gt_2", "sum"), no_supera_naive=("no_supera_naive", "sum"),
                  corridas=("MAE_train", "size"), Naive_razon=("Naive_razon", "first")).reset_index()
        v["modelo"] = pd.Categorical(v.modelo, ["Ridge", "ElasticNet", "XGB-37", "GC3", "GE", "XGB-43"], ordered=True)
        v = v.sort_values(["modelo", "anio_test"])
        v["sobreajuste"] = [f"{int(x)}/{n}" for x, n in zip(v.sobreajuste, v.corridas)]
        v["no_supera_naive"] = [f"{int(x)}/{n}" for x, n in zip(v.no_supera_naive, v.corridas)]
        T.guardar(v.drop(columns="corridas"), "06_metricas/por_semilla", f"T15_diagnostico_{c}",
                  f"Diagnóstico de ajuste D-BR8, {NOMBRE_C[c]}: MAE (t) medio entre semillas, razón val/train (mediana), "
                  f"corridas con razón > 2, corridas que no superan al Naive, y razón del Naive (XGB-43 exploratorio)", dec=dec_de(c))
    e2 = ep.groupby(["modelo", "cultivar", "anio_test"]).agg(
        mediana=("mejor_epoca", "median"), q1=("mejor_epoca", lambda x: x.quantile(0.25)), q3=("mejor_epoca", lambda x: x.quantile(0.75)),
        minimo=("mejor_epoca", "min"), maximo=("mejor_epoca", "max"), epocas_corridas_mediana=("epocas_corridas", "median"),
        epocas_corridas_max=("epocas_corridas", "max")).reset_index()
    T.guardar(e2, "06_metricas/por_semilla", "T15_mejor_epoca_por_ventana",
              "Mejor época (early stopping, paciencia 15) por ventana: distribución entre las 10 semillas", dec=1)

    # (h) descripcion de las series (T03, T04) ----------------------------------------------------------------
    from statsmodels.tsa.stattools import acf, adfuller, kpss

    filas3, filas4 = [], []
    for c in ev.CULTIVARES:
        y = s[c]
        for a in range(2018, 2026):
            v = Ventana(a)
            partes = {"train": y[(y.index >= "2016-07") & (y.index <= v.fin_train)],
                      "val": y[(y.index >= v.val[0]) & (y.index <= v.val[1])], "test": y[(y.index >= v.test[0]) & (y.index <= v.test[1])]}
            for nom, x in partes.items():
                filas3.append({"cultivar": c, "anio_test": a, "particion": nom, "inicio": x.index.min(), "fin": x.index.max(),
                               "n": len(x), "media": x.mean(), "DE": x.std(), "min": x.min(), "max": x.max(), "CV": x.std() / x.mean()})
            x = partes["train"]
            yy = y[y.index <= v.fin_train]
            d12 = (yy - yy.shift(12)).dropna()
            d12 = d12[d12.index >= "2016-07"]
            fila = {"cultivar": c, "anio_test": a, "n_train": len(x), "n_D12": len(d12)}
            if len(x) >= 24:
                ac = acf(x.to_numpy(), nlags=12, fft=False)
                fila.update(ACF1=ac[1], ACF12=ac[12])
            for nom, z in (("nivel", x), ("D12", d12)):
                if len(z) < 24:
                    continue
                with warnings.catch_warnings(record=True) as w:
                    warnings.simplefilter("always")
                    adf = adfuller(z.to_numpy(), autolag="AIC", regression="c")
                    kp = kpss(z.to_numpy(), regression="c", nlags="auto")
                fila.update({f"ADF_{nom}_est": adf[0], f"ADF_{nom}_p": adf[1], f"ADF_{nom}_lags": adf[2],
                             f"KPSS_{nom}_est": kp[0], f"KPSS_{nom}_p": kp[1],
                             f"KPSS_{nom}_p_acotado": any("InterpolationWarning" in type(i.message).__name__ for i in w)})
            filas4.append(fila)
    t03, t04 = pd.DataFrame(filas3), pd.DataFrame(filas4)
    t03.to_csv(BR / "06_metricas" / "descripcion_series" / "T03_descripcion_particiones.csv", index=False, float_format="%.10g")
    t04.to_csv(BR / "06_metricas" / "descripcion_series" / "T04_acf_adf_kpss_train.csv", index=False, float_format="%.10g")
    for c in ev.CULTIVARES:
        v = t03[(t03.cultivar == c) & (t03.anio_test >= 2021)]
        T.guardar(v.drop(columns="cultivar"), "06_metricas/descripcion_series", f"T03_particiones_{c}",
                  f"Descripción de la serie por partición (train desde 2016-07), {NOMBRE_C[c]} (t)", dec=dec_de(c))
        v = t04[t04.cultivar == c]
        cols = ["anio_test", "n_train", "ACF1", "ACF12", "ADF_nivel_p", "KPSS_nivel_p", "n_D12", "ADF_D12_p", "KPSS_D12_p"]
        T.guardar(v[[x for x in cols if x in v.columns]], "06_metricas/descripcion_series", f"T04_estacionariedad_{c}",
                  f"ACF, ADF y KPSS (p) en TRAIN, nivel y Δ12, {NOMBRE_C[c]} (KPSS p acotado a [0.01, 0.10]; '—' = n < 24)", dec=3)

    # (j) SARIMA-sel (T20) y lineales (T21) -------------------------------------------------------------------
    filas20, cand = [], []
    for f in sorted((BR / "04_modelos" / "sarima_sel").glob("*/*/info.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        u = d["unidad"]
        filas20.append({"cultivar": u["cultivar"], "anio_test": u["anio"], "orden": str(tuple(d["order"])),
                        "orden_estacional": str(tuple(d["seasonal_order"])), "posicion_AIC": d["posicion_aic_elegido"],
                        "AIC": d["aic_elegido"], "MAE_val": d["MAE_val_elegido"], "convergio": d["convergio"],
                        "fallidos": d["n_fallidos"], "AIC_no_finito": d["n_aic_no_finito"], "no_conv_rejilla": d["n_no_convergidos_rejilla"]})
        cand.append(pd.read_csv(f.parent / "candidatos.csv").assign(cultivar=u["cultivar"], anio_test=u["anio"]))
    t20 = pd.DataFrame(filas20).sort_values(["cultivar", "anio_test"], ascending=[False, True])
    T.guardar(t20, "06_metricas/por_ventana", "T20_sarima_sel", "SARIMA-sel: orden elegido por ventana (D-BR10) y posición en AIC", dec=1)
    pd.concat(cand).to_csv(BR / "06_metricas" / "por_ventana" / "T20_sarima_sel_candidatos.csv", index=False, float_format="%.10g")
    filas21 = []
    for f in sorted((BR / "04_modelos").glob("[re][il]*/*/*/info.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        u = d["unidad"]
        ctl = d.get("control_2025_v3", {})
        filas21.append({"modelo": u["modelo"], "cultivar": u["cultivar"], "anio_test": u["anio"], "alpha": d["alpha"],
                        "l1_ratio": d["l1_ratio"], "MAE_val": d["MAE_val_elegido"],
                        "control_v3_coincide": ctl.get("coincide_con_elegido")})
    T.guardar(pd.DataFrame(filas21).sort_values(["modelo", "cultivar", "anio_test"], ascending=[False, False, True]),
              "06_metricas/por_ventana", "T21_lineales_hiperparametros", "Ridge y ElasticNet: α (y l1) elegidos con la validación Y−1", dec=2)

    # T16 exploratorio XGB-43 ---------------------------------------------------------------------------------
    filas16 = []
    for c in ev.CULTIVARES:
        pv = ev.matriz(err, ["XGB-37", "XGB-43"], c, ev.VENTANAS_PRINCIPAL)
        claves = list(pv.index)
        est = np.array([a for a, _ in claves])
        sh = ev.vector_shock(claves, M, c, "mensual", 75)
        dif = (pv["XGB-43"] - pv["XGB-37"]).to_numpy()
        for alcance, sel in (("global", np.ones(len(claves), bool)), ("shock_P75", sh), ("normal_P75", ~sh)):
            bt = dif[ev.indices_iid(est, sel, np.random.default_rng(ev.SEMILLA_BOOT))].mean(axis=1)
            lo, hi = ev.ic(bt)
            filas16.append({"cultivar": c, "alcance": alcance, "n_meses": int(sel.sum()),
                            "MAE_XGB37": float(pv["XGB-37"].to_numpy()[sel].mean()), "MAE_XGB43": float(pv["XGB-43"].to_numpy()[sel].mean()),
                            "dif_43_menos_37": float(dif[sel].mean()), "IC95_lo": lo, "IC95_hi": hi})
    t16 = pd.DataFrame(filas16)
    T.guardar(t16, "06_metricas/agregadas", "T16_exploratorio_xgb43",
              "EXPLORATORIO (post-hoc): XGB-43 frente a XGB-37, 2021-2025, P75 mensual (t)", dec=1)

    T.escribir_texto(BR / "09_reportes" / "tablas_fase_D1_08.md")
    print("08_metricas: OK")


if __name__ == "__main__":
    main()
