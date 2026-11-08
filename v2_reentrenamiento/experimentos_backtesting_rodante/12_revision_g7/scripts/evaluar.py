"""Evaluacion de la Fase 3 (G7) con la metodologia del pipeline (lib/evaluacion.py), sin modificar nada existente.

Lee 05_predicciones/predicciones_consolidadas.csv (originales) y 12_revision_g7/resultados/unidades (nuevos).
Escribe CSV en 12_revision_g7/resultados/.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "02_scripts"))
from lib.entorno import preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import glob  # noqa: E402
import json  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
import g7lib as G  # noqa: E402
from lib import evaluacion as ev  # noqa: E402

OUT = G.RES
ORIG10 = list(ev.MODELOS_RANKING)
NUEVOS = ["Ridge-Y1", "ElasticNet-Y1", "XGB-37-Y1", "SARIMA-Y1", "SARIMA-sel-Y1", "GC3-Y1", "GE-Y1", "LSTM-U", "LSTM-U-Y1", "GC3-R", "GC3-R-Y1"]
CHRX = ["Chronos-small", "Chronos-base"]
TODOS = ORIG10 + NUEVOS
CULT = ["sutil", "dulce"]
POOLS = {"principal_2021_2025": [2021, 2022, 2023, 2024, 2025], "sensibilidad_2023_2025": [2023, 2024, 2025]}
PCTS = [50, 60, 75, 90]
TIPOS = {"mensual": "MoM", "interanual": "YoY"}
REF = {"sutil": "Chronos", "dulce": "SARIMA-sel"}


def guardar(df, nombre):
    df.to_csv(OUT / nombre, index=False, encoding="utf-8")
    print("escrito", nombre, df.shape)


# ----------------------------------------------------------------------------- errores por semilla y promediados
S = ev.series()
orig = pd.read_csv(ev.BR / "05_predicciones" / "predicciones_consolidadas.csv", dtype={"fecha": str})
orig["semilla"] = orig["semilla"].astype("Int64")
nuevos = []
for ruta in glob.glob(str(G.UNI / "*" / "*" / "*" / "**" / "predicciones.csv"), recursive=True):
    info = json.loads((Path(ruta).parent / "info.json").read_text(encoding="utf-8"))
    p = pd.read_csv(ruta, dtype={"fecha": str})
    p["modelo"], p["cultivar"], p["anio_test"] = info["modelo"], info["cultivar"], int(info["anio_test"])
    p["semilla"] = info["semilla"]
    nuevos.append(p[["modelo", "cultivar", "anio_test", "semilla", "particion", "fecha", "y_true", "y_pred"]])
nuevos = pd.concat(nuevos, ignore_index=True)
nuevos["semilla"] = nuevos["semilla"].astype("Int64")
pred = pd.concat([orig, nuevos], ignore_index=True)
ES = ev.errores_por_semilla(pred, S, "test")  # verifica y_true contra la serie
ERR = ev.promediar_semillas(ES)
guardar(ERR, "errores_test_promediados_semillas_g7.csv")
cnt = nuevos[nuevos.particion == "test"].groupby(["modelo", "cultivar"]).agg(n_filas=("fecha", "size"), n_semillas=("semilla", "nunique")).reset_index()
guardar(cnt, "control_unidades.csv")

D = ev.denominadores_mase().set_index(["cultivar", "anio_test"]).D_mase
M = ev.mascaras(S, sorted({a for v in POOLS.values() for a in v}), PCTS)


def matriz(c, anios, modelos):
    pv = ev.matriz(ERR, modelos, c, anios)
    return pv, list(pv.index), np.array([a for a, _ in pv.index]), np.array([D[(c, a)] for a, _ in pv.index])


# ----------------------------------------------------------------------------- metricas
filas, filas_p = [], []
for c in CULT:
    for pool, anios in POOLS.items():
        modelos = TODOS + CHRX
        pv, claves, estr, dv = matriz(c, anios, modelos)
        AE = pv.to_numpy().T
        rng = np.random.default_rng(ev.SEMILLA_BOOT)
        idx_i = ev.indices_iid(estr, np.ones(len(estr), bool), rng)
        est_i = AE[:, idx_i].mean(axis=2)
        idx_b = ev.indices_bloques(estr, np.random.default_rng(ev.SEMILLA_BOOT))
        est_b = ev.remuestrear(AE, np.ones(len(estr)), idx_b)
        for j, m in enumerate(modelos):
            ae = AE[j]
            base = {"cultivo": c, "pool": pool, "modelo": m, "MAE": ae.mean(), "IC_iid_lo": np.percentile(est_i[j], 2.5),
                    "IC_iid_hi": np.percentile(est_i[j], 97.5), "IC_bloques_lo": np.nanpercentile(est_b[j], 2.5),
                    "IC_bloques_hi": np.nanpercentile(est_b[j], 97.5), "RMSE": ev.rmse_semillas(ES, m, c, anios), "MASE": float(np.mean(ae / dv))}
            for tipo, et in TIPOS.items():
                for p in PCTS:
                    sh = ev.vector_shock(claves, M, c, tipo, p)
                    sn = AE[modelos.index("Seasonal Naive")][sh].mean()
                    d = {"n_shock": int(sh.sum()), "MAE_normal": ae[~sh].mean(), "MAE_shock": ae[sh].mean(),
                         "t_de_mas": ae[sh].mean() - ae[~sh].mean(), "MASE_shock": float(np.mean(ae[sh] / dv[sh])),
                         "MAE_shock_rel_SNaive": ae[sh].mean() / sn}
                    if p == 75:
                        base.update({f"{k}_{et}": v for k, v in d.items()})
                    filas_p.append({"cultivo": c, "pool": pool, "modelo": m, "definicion": et, "percentil": p, **d})
            filas.append(base)
guardar(pd.DataFrame(filas), "T1_metricas_P75_MoM_YoY.csv")
guardar(pd.DataFrame(filas_p), "T2_metricas_shock_todos_percentiles.csv")

# ----------------------------------------------------------------------------- ranking y primero o empatado
filas = []
for grupo, modelos in (("todos", TODOS), ("todos_mas_chronos_small_base", TODOS + CHRX)):
    for c in CULT:
        for pool, anios in POOLS.items():
            pv, claves, estr, _ = matriz(c, anios, modelos)
            AE = pv.to_numpy().T
            casos = [("global", "-", 0, np.ones(len(claves), bool))]
            casos += [("shock", et, p, ev.vector_shock(claves, M, c, tipo, p)) for tipo, et in TIPOS.items() for p in PCTS]
            for crit, et, p, sub in casos:
                r = ev.ranking(AE, modelos, estr, sub, "iid")
                r.insert(0, "percentil", p)
                r.insert(0, "definicion", et)
                r.insert(0, "criterio", crit)
                r.insert(0, "pool", pool)
                r.insert(0, "cultivo", c)
                r.insert(0, "grupo", grupo)
                filas.append(r)
RK = pd.concat(filas, ignore_index=True)
guardar(RK, "T3_ranking_primero_empatado.csv")
sh = RK[RK.criterio == "shock"]
rob = sh.groupby(["grupo", "cultivo", "pool", "definicion", "modelo"]).primero.sum().rename("n_primero_de_4").reset_index()
rob["robusto_3de4"] = rob.n_primero_de_4 >= 3
guardar(rob, "T4_robustez.csv")

# ----------------------------------------------------------------------------- DM-HLN contra el mejor univariado
filas = []
for c in CULT:
    for pool, anios in POOLS.items():
        pv, claves, estr, _ = matriz(c, anios, TODOS + CHRX)
        ref = pv[REF[c]].to_numpy()
        for m in NUEVOS + CHRX + [x for x in ORIG10 if x != REF[c]]:
            for alc, sub in (("global", np.ones(len(claves), bool)), ("shock_MoM_P75", ev.vector_shock(claves, M, c, "mensual", 75)),
                             ("shock_YoY_P75", ev.vector_shock(claves, M, c, "interanual", 75))):
                r = ev.dm_hln(pv[m].to_numpy()[sub], ref[sub])
                filas.append({"cultivo": c, "pool": pool, "modelo": m, "referencia": REF[c], "alcance": alc, "nuevo": m in NUEVOS + CHRX, **r})
guardar(pd.DataFrame(filas), "T5_DM_HLN_vs_mejor_univariado.csv")

# ----------------------------------------------------------------------------- comparaciones clave con IC pareado
PARES = [("GC3-Y1", "GC3"), ("GE-Y1", "GE"), ("LSTM-U", "GC3"), ("GC3-R", "GC3"), ("GC3-R", "SARIMA-sel"), ("GC3-R", "Chronos"),
         ("LSTM-U-Y1", "GC3-Y1"), ("GC3-R-Y1", "GC3-Y1"), ("GC3-R-Y1", "SARIMA-sel"), ("GC3-R-Y1", "Chronos"), ("LSTM-U", "SARIMA-sel"),
         ("LSTM-U", "Chronos"), ("XGB-37-Y1", "XGB-37"), ("Ridge-Y1", "Ridge"), ("ElasticNet-Y1", "ElasticNet"), ("SARIMA-Y1", "SARIMA"),
         ("SARIMA-sel-Y1", "SARIMA-sel"), ("Chronos-small", "Chronos"), ("Chronos-base", "Chronos")]
CON_SEM = {"XGB-37", "GC3", "GE"} | {m for m in NUEVOS if G.MODELOS[m][1]}
filas = []
for c in CULT:
    for pool, anios in POOLS.items():
        pv, claves, estr, _ = matriz(c, anios, TODOS + CHRX)
        for a, b in PARES:
            for alc, sub in (("global", np.ones(len(claves), bool)), ("shock_MoM_P75", ev.vector_shock(claves, M, c, "mensual", 75)),
                             ("shock_YoY_P75", ev.vector_shock(claves, M, c, "interanual", 75))):
                d = (pv[a] - pv[b]).to_numpy()
                idx = ev.indices_iid(estr, sub, np.random.default_rng(ev.SEMILLA_BOOT))
                bs = d[idx].mean(axis=1)
                fila = {"cultivo": c, "pool": pool, "A": a, "B": b, "alcance": alc, "n_meses": int(sub.sum()), "MAE_A": pv[a].to_numpy()[sub].mean(),
                        "MAE_B": pv[b].to_numpy()[sub].mean(), "dif_A_menos_B": d[sub].mean(), "IC95_lo": np.percentile(bs, 2.5),
                        "IC95_hi": np.percentile(bs, 97.5)}
                if a in CON_SEM and b in CON_SEM:
                    meses = set(f for (_, f), s in zip(claves, sub) if s)
                    ea = ES[(ES.modelo == a) & (ES.cultivar == c) & ES.anio_test.isin(anios) & ES.fecha.isin(meses)].groupby("semilla").ae.mean()
                    eb = ES[(ES.modelo == b) & (ES.cultivar == c) & ES.anio_test.isin(anios) & ES.fecha.isin(meses)].groupby("semilla").ae.mean()
                    dd = (ea - eb).dropna()
                    fila.update({"semillas_A_mejor_de_10": int((dd < 0).sum()), "DE_dif_entre_semillas": float(dd.std(ddof=1))})
                filas.append(fila)
guardar(pd.DataFrame(filas), "T6_comparaciones_clave.csv")

# ----------------------------------------------------------------------------- dispersion entre semillas y razon val/train
filas = []
for m in sorted(CON_SEM):
    for c in CULT:
        for pool, anios in POOLS.items():
            x = ES[(ES.modelo == m) & (ES.cultivar == c) & ES.anio_test.isin(anios)].groupby("semilla").ae.mean()
            filas.append({"modelo": m, "cultivo": c, "pool": pool, "n_semillas": len(x), "MAE_media": x.mean(), "DE": x.std(ddof=1),
                          "min": x.min(), "max": x.max(), "CV_pct": x.std(ddof=1) / x.mean() * 100})
guardar(pd.DataFrame(filas), "T7_dispersion_semillas.csv")
filas = []
for m in ("LSTM-U", "GC3-R"):
    q = nuevos[nuevos.modelo == m].assign(ae=lambda d: (d.y_true - d.y_pred).abs())
    g = q.groupby(["cultivar", "anio_test", "semilla", "particion"]).ae.mean().unstack()
    g["razon_val_train"] = g["val"] / g["train"]
    g = g.reset_index()
    for c in CULT:
        x = g[g.cultivar == c]
        filas.append({"modelo": m, "cultivo": c, "n_unidades": len(x), "n_razon_gt_2": int((x.razon_val_train > 2).sum()),
                      "razon_mediana": x.razon_val_train.median(), "razon_max": x.razon_val_train.max()})
guardar(pd.DataFrame(filas), "T8_razon_val_train.csv")

# ----------------------------------------------------------------------------- Chronos small/base 2018-2025 por ventana
ch = ERR[ERR.modelo.isin(["Chronos"] + CHRX)].groupby(["modelo", "cultivar", "anio_test"]).ae.mean().unstack("modelo").reset_index()
guardar(ch, "T9_chronos_por_ventana.csv")
# epocas y parametros
filas = []
for ruta in glob.glob(str(G.UNI / "*" / "*" / "*" / "seed_*" / "info.json")):
    i = json.loads(Path(ruta).read_text(encoding="utf-8"))
    if G.MODELOS[i["modelo"]][0] == "lstm":
        filas.append({"modelo": i["modelo"], "cultivar": i["cultivar"], "anio": i["anio_test"], "semilla": i["semilla"], "n_params": i["n_params"],
                      "mejor_epoca": i.get("mejor_epoca"), "epocas_corridas": i.get("epocas_corridas"), "epocas_fijas": i.get("epocas_fijas"),
                      "fit_seconds": i["fit_seconds"], "segundos_unidad": i["segundos_unidad"]})
guardar(pd.DataFrame(filas), "T10_lstm_epocas_parametros.csv")
