"""Revision G7 - Fase 1: regenerates the CSV tables of this folder and compares them, cell by cell, with the
published ones.

The original script of Fase 1 (INFORME_FASE1.md) was lost; this is a reconstruction. It only reads frozen files
and never writes over the published CSV: the regenerated tables go to --salida (a temporary folder by default).

    python g7_fase1.py [--salida DIR] [--json REPORT.json] [--estricto]

Inputs (read only):
  05_predicciones/errores_test_promediados_semillas.csv   monthly AE averaged over seeds (column ae)
  05_predicciones/predicciones_consolidadas.csv           per-seed predictions (tables F and I)
  03_ventanas/umbrales_y_mascaras.csv                      P50/P60/P75/P90 MoM and YoY shock masks per window
  03_ventanas/denominador_mase_por_ventana.csv             MASE denominator D_w per window
  06_metricas/agregadas/T06_agregadas_IC.csv               MAE, RMSE, MASE and bootstrap intervals (table E1)
  06_metricas/agregadas/T17_descriptivo_2018_2020_{c}.csv  windows 2018-2020 (table E3)
  06_metricas/por_semilla/T15_diagnostico_ajuste.csv       validation/train ratio (table E2)
  01_configuracion/hiperparametros_congelados.json         number of LSTM parameters (table F)
  v2_reentrenamiento/data/interim/limon_{c}_nacional_mensual.csv, limon_{c}_provincia.csv   (tables B and G)

Comparison: each regenerated CSV is compared with the published one as text, cell by cell (same header, same
number of rows, same string in every cell). Cells whose text differs are also compared numerically; the report
gives the number of different cells and the maximum absolute and relative difference. Exit code 0, or 1 with
--estricto when any cell differs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
import tempfile
from pathlib import Path

import numpy as np
import pandas as pd

AQUI = Path(__file__).resolve().parent
BR = AQUI.parents[2]
RAIZ = BR.parents[1]
INT = RAIZ / "v2_reentrenamiento" / "data" / "interim"

MODELOS = ["Naive", "Seasonal Naive", "Chronos", "SARIMA", "SARIMA-sel", "Ridge", "ElasticNet", "XGB-37", "GC3", "GE"]
LIMPIOS = ["Naive", "Seasonal Naive", "Chronos", "SARIMA-sel", "Ridge", "ElasticNet"]
CULT = ["sutil", "dulce"]
POOLS = {"principal_2021_2025": [2021, 2022, 2023, 2024, 2025], "sensibilidad_2023_2025": [2023, 2024, 2025]}
PCTS = [50, 60, 75, 90]
DEFS = {"MoM": ("mensual", 1), "YoY": ("interanual", 12)}
B, SEMILLA = 10_000, 42
ARCHIVOS = ["B1_calendario_shocks_P75.csv", "B2_shocks_por_mes_calendario.csv", "B3_MAE_inicio_vs_continuacion.csv",
            "B4_caso_2023.csv", "C_metricas_escaladas_shock.csv", "D_ranking_modelos_limpios.csv",
            "E1_suplementaria_2021_2025.csv", "E2_razon_val_train_gt2.csv", "E3_ventanas_2018_2020.csv",
            "F_parametros_por_observacion.csv", "G0_provincias_meses_registro_dulce.csv",
            "G0_provincias_meses_registro_sutil.csv", "G1_provincias_por_mes_2021_2025.csv",
            "G2_shocks_entradas_salidas.csv", "I_ensamble_semillas.csv"]


# ----------------------------------------------------------------------------------------------- inputs
def serie_nacional(c: str) -> pd.Series:
    d = pd.read_csv(INT / f"limon_{c}_nacional_mensual.csv", encoding="utf-8-sig", dtype={"mes": str})
    idx = d.iloc[:, 0].astype(str) + "-" + d["mes"].str.zfill(2)
    return pd.Series(d["produccion_t_nacional"].astype(float).to_numpy(), index=idx.to_numpy()).sort_index()


def provincias(c: str) -> pd.DataFrame:
    d = pd.read_csv(INT / f"limon_{c}_provincia.csv", encoding="utf-8-sig", dtype={"mes": str})
    d["fecha"] = d.iloc[:, 0].astype(str) + "-" + d["mes"].str.zfill(2)
    d["provincia_id"] = d["departamento"] + "|" + d["provincia"]
    return d


S = {c: serie_nacional(c) for c in CULT}
E = pd.read_csv(BR / "05_predicciones/errores_test_promediados_semillas.csv")
MK = pd.read_csv(BR / "03_ventanas/umbrales_y_mascaras.csv")
DEN = pd.read_csv(BR / "03_ventanas/denominador_mase_por_ventana.csv")


def mascara(c: str, defi: str, anio: int, p: int) -> tuple[float, list[str]]:
    r = MK[(MK.cultivar == c) & (MK.tipo == DEFS[defi][0]) & (MK.anio_test == anio) & (MK.percentil == p)].iloc[0]
    return float(r.umbral), [x for x in str(r.meses_shock).split(";") if x and x != "nan"]


def shocks_pool(c: str, defi: str, p: int, anios) -> list[str]:
    return [m for a in anios for m in mascara(c, defi, a, p)[1]]


def ae_mat(c: str, anios, modelos) -> pd.DataFrame:
    d = E[(E.cultivar == c) & E.anio_test.isin(anios) & E.modelo.isin(modelos)]
    return d.pivot(index="fecha", columns="modelo", values="ae")[modelos].sort_index()


def ref(fecha: str, k: int) -> str:
    return str(pd.Period(fecha, "M") - k)


# ----------------------------------------------------------------------------------------------- tables
def tabla_b() -> dict[str, pd.DataFrame]:
    filas = []
    for c in CULT:
        s = S[c]
        A = ae_mat(c, POOLS["principal_2021_2025"], MODELOS)
        for defi, (_, k) in DEFS.items():
            todos = {m for a in range(2020, 2026) for m in mascara(c, defi, a, 75)[1]}
            for a in POOLS["principal_2021_2025"]:
                u, sh = mascara(c, defi, a, 75)
                for f in sh:
                    fr = ref(f, k)
                    filas.append({"cultivo": c, "definicion": f"P75 {defi}", "fecha": f, "anio_ventana": a,
                                  "mes_calendario": int(f[5:]), "y_t": s[f], "y_ref": s[fr], "fecha_ref": fr,
                                  "y_t_menos_1": s[ref(f, 1)], "cambio_pct": (s[f] - s[fr]) / s[fr] * 100,
                                  "umbral_ventana_pct": u * 100,
                                  "episodio": "continuacion" if ref(f, 1) in todos else "inicio",
                                  **{f"AE_{m}": A.loc[f, m] for m in MODELOS}})
    b1 = pd.DataFrame(filas)
    b2 = (b1.groupby(["cultivo", "definicion"]).mes_calendario.value_counts().unstack(fill_value=0)
          .reindex(columns=range(1, 13), fill_value=0).reset_index())
    b2.columns = [str(x) for x in b2.columns]
    b3 = []
    for (c, defi, ep), g in b1.groupby(["cultivo", "definicion", "episodio"]):
        b3.append({"cultivo": c, "definicion": defi, "episodio": ep, "n": len(g), **{m: g[f"AE_{m}"].mean() for m in MODELOS}})
    b4 = b1[b1.fecha.str.startswith("2023")].reset_index(drop=True)
    return {"B1_calendario_shocks_P75.csv": b1, "B2_shocks_por_mes_calendario.csv": b2,
            "B3_MAE_inicio_vs_continuacion.csv": pd.DataFrame(b3), "B4_caso_2023.csv": b4}


def tabla_c() -> pd.DataFrame:
    filas = []
    for c in CULT:
        Dm = DEN[DEN.cultivar == c].set_index("anio_test").D_mase
        for pool, anios in POOLS.items():
            A = ae_mat(c, anios, MODELOS)
            dvec = np.array([Dm[int(f[:4])] for f in A.index])
            for defi in DEFS:
                for p in PCTS:
                    es = A.index.isin(shocks_pool(c, defi, p, anios))
                    bloque = []
                    for m in MODELOS:
                        ae = A[m].to_numpy()
                        esc = ae / dvec
                        bloque.append({"conjunto": pool, "cultivo": c, "definicion": f"P{p} {defi}", "modelo": m,
                                       "n_shock": int(es.sum()), "n_normal": int((~es).sum()), "MAE": ae.mean(),
                                       "MAE_normal": ae[~es].mean(), "MAE_shock": ae[es].mean(),
                                       "exceso_t": ae[es].mean() - ae[~es].mean(), "razon_shock_normal": ae[es].mean() / ae[~es].mean(),
                                       "MASE": esc.mean(), "MASE_shock": esc[es].mean(), "MASE_normal": esc[~es].mean()})
                    g = pd.DataFrame(bloque)
                    g["MAE_shock_rel_SNaive"] = g.MAE_shock / float(g.loc[g.modelo == "Seasonal Naive", "MAE_shock"].iloc[0])
                    g["rank_MASE_shock"] = g.MASE_shock.rank(method="min").astype(int)
                    g["rank_MAE_shock_rel"] = g.MAE_shock_rel_SNaive.rank(method="min").astype(int)
                    filas.append(g)
    return pd.concat(filas, ignore_index=True)


def bootstrap_pareado(M: np.ndarray, estratos: np.ndarray) -> np.ndarray:
    """Paired iid bootstrap of months stratified by window, with the resampling of 02_scripts/lib/metricas.py:31-42
    (default_rng(42), rng.choice per window). M: months x models; returns B x models of resampled MAE.
    The mean is taken over axis 0 of the months x models matrix (sequential summation), as in the original run."""
    rng = np.random.default_rng(SEMILLA)
    grupos = [np.flatnonzero(estratos == g) for g in pd.unique(estratos)]
    out = np.empty((B, M.shape[1]))
    for b in range(B):
        idx = np.concatenate([rng.choice(g, size=len(g), replace=True) for g in grupos])
        out[b] = M[idx].mean(axis=0)
    return out


def tabla_d() -> pd.DataFrame:
    filas = []
    for pool, anios in POOLS.items():
        for c in sorted(CULT):
            A = ae_mat(c, anios, LIMPIOS)
            sh = shocks_pool(c, "MoM", 75, anios)
            for alcance, sub in (("global", np.ones(len(A), bool)), ("shock_P75_MoM", A.index.isin(sh))):
                X = A[sub]
                estr = np.array([int(f[:4]) for f in X.index])
                M = X.to_numpy()
                mae = dict(zip(LIMPIOS, M.mean(axis=0)))
                orden = sorted(LIMPIOS, key=lambda m: mae[m])
                lider = orden[0]
                bs = dict(zip(LIMPIOS, bootstrap_pareado(M, estr).T))
                for i, m in enumerate(orden, 1):
                    if m == lider:
                        lo = hi = np.nan
                        emp = True
                    else:
                        d = bs[m] - bs[lider]
                        lo, hi = np.percentile(d, 2.5), np.percentile(d, 97.5)
                        emp = bool(lo <= 0 <= hi)
                    filas.append({"conjunto": pool, "cultivo": c, "alcance": alcance, "n_meses": int(sub.sum()), "modelo": m,
                                  "MAE": mae[m], "posicion": i, "lider": lider, "dif_vs_lider": mae[m] - mae[lider],
                                  "IC95_dif_lo": lo, "IC95_dif_hi": hi, "empatado_con_lider": emp})
    return pd.DataFrame(filas)


def tabla_e() -> dict[str, pd.DataFrame]:
    t15 = pd.read_csv(BR / "06_metricas/por_semilla/T15_diagnostico_ajuste.csv")
    t15 = t15[~t15.exploratorio.astype(bool) & t15.anio_test.between(2021, 2025)]
    e2 = (t15.groupby(["cultivar", "modelo"]).agg(n_unidades=("razon_val_train", "size"),
                                                   n_razon_gt_2=("sobreajuste_razon_gt_2", "sum")).reset_index())
    t06 = pd.read_csv(BR / "06_metricas/agregadas/T06_agregadas_IC.csv")
    t06 = t06[t06.modelo.isin(MODELOS)]

    def sel(conj, tipo, c):
        return t06[(t06.conjunto == conj) & (t06.tipo == tipo) & (t06.percentil == 75) & (t06.cultivar == c)].set_index("modelo").loc[MODELOS]

    filas = []
    for c in CULT:
        pm, sm, py = sel("principal_2021_2025", "mensual", c), sel("sensibilidad_2023_2025", "mensual", c), sel("principal_2021_2025", "interanual", c)
        cols = ["MAE", "iid_global_lo", "iid_global_hi", "bloq_global_lo", "bloq_global_hi", "RMSE", "MASE", "MAE_shock",
                "iid_shock_lo", "iid_shock_hi", "bloq_shock_lo", "bloq_shock_hi", "n_shock"]
        d = pm[cols].copy()
        d["rank_MAE_2023_2025"] = sm.MAE.rank(method="min").astype(int)
        d["rank_MAE_shock_2023_2025"] = sm.MAE_shock.rank(method="min").astype(int)
        d["rank_MAE_2021_2025"] = pm.MAE.rank(method="min").astype(int)
        d["MAE_shock_YoY_P75"] = py.MAE_shock
        d["n_shock_YoY_P75"] = py.n_shock
        d["rank_MAE_shock_YoY_P75"] = py.MAE_shock.rank(method="min").astype(int)
        d["rank_MAE_shock_MoM_P75"] = pm.MAE_shock.rank(method="min").astype(int)
        d = d.reset_index().rename(columns={"index": "modelo"})
        d.insert(0, "cultivar", c)
        d = d.merge(e2[e2.cultivar == c].drop(columns="cultivar"), on="modelo", how="left")
        filas.append(d)
    e1 = pd.concat(filas, ignore_index=True)
    e3 = pd.concat([pd.read_csv(BR / f"06_metricas/agregadas/T17_descriptivo_2018_2020_{c}.csv")
                    .query("modelo in ['Naive', 'Seasonal Naive', 'Chronos']").assign(cultivar=c) for c in CULT], ignore_index=True)
    return {"E1_suplementaria_2021_2025.csv": e1, "E2_razon_val_train_gt2.csv": e2, "E3_ventanas_2018_2020.csv": e3}


P = pd.read_csv(BR / "05_predicciones/predicciones_consolidadas.csv")


def tabla_f() -> pd.DataFrame:
    npar = json.loads((BR / "01_configuracion/hiperparametros_congelados.json").read_text(encoding="utf-8"))
    npar = next(v["parametros_esperados"] for v in npar.values() if isinstance(v, dict) and "parametros_esperados" in v)
    d = P[P.modelo.isin(["GC3", "GE"]) & P.anio_test.between(2021, 2025)]
    n = d.groupby(["modelo", "cultivar", "anio_test", "semilla", "particion"]).size().unstack("particion")
    g = n.groupby(["modelo", "cultivar", "anio_test"]).agg(n_train=("train", "max"), n_train_min=("train", "min"), n_val=("val", "max")).reset_index()
    g["parametros"] = g.modelo.map(npar)
    g["param_por_obs_train"] = g.parametros / g.n_train
    g["param_por_obs_train_mas_val"] = g.parametros / (g.n_train + g.n_val)
    return g


def tabla_g() -> dict[str, pd.DataFrame]:
    out, g1, g2 = {}, [], []
    for c in CULT:
        pr = provincias(c)
        pr = pr[pr.fecha.between("2016-01", "2025-12")]
        w = pr.pivot_table(index="fecha", columns="provincia_id", values="produccion_t", aggfunc="sum").fillna(0.0)
        cnt = (w > 0).sum()
        g0 = pd.DataFrame({"provincia": cnt.index, "meses_con_produccion_de_120": cnt.to_numpy(),
                           "intermitente": (cnt < 120).to_numpy(), "t_2016_2025": w.sum().to_numpy()})
        g0 = g0.sort_values("meses_con_produccion_de_120").reset_index(drop=True)
        out[f"G0_provincias_meses_registro_{c}.csv"] = g0
        inter = list(cnt.index[cnt < 120])
        nrep = pd.read_csv(INT / f"limon_{c}_nacional_mensual.csv", encoding="utf-8-sig", dtype={"mes": str})
        nrep.index = nrep.iloc[:, 0].astype(str) + "-" + nrep["mes"].str.zfill(2)
        shm = set(shocks_pool(c, "MoM", 75, POOLS["principal_2021_2025"]))
        shy = set(shocks_pool(c, "YoY", 75, POOLS["principal_2021_2025"]))
        for f in [m for m in w.index if m >= "2021-01"]:
            fila = w.loc[f]
            g1.append({"cultivo": c, "fecha": f, "n_provincias_reportan": int((fila > 0).sum()),
                       "n_provincias_reporte_nacional": int(nrep.loc[f, "n_provincias_reportando"]),
                       "pct_prod_intermitentes": fila[inter].sum() / fila.sum() * 100,
                       "shock_P75_MoM": f in shm, "shock_P75_YoY": f in shy})
        for defi, (_, k) in DEFS.items():
            for f in shocks_pool(c, defi, 75, POOLS["principal_2021_2025"]):
                fr = ref(f, k)
                a, b = w.loc[f], w.loc[fr]
                ent = sorted(a.index[(a > 0) & (b <= 0)])
                sal = sorted(a.index[(a <= 0) & (b > 0)])
                te, ts = float(a[ent].sum()), float(b[sal].sum())
                dy = S[c][f] - S[c][fr]
                g2.append({"cultivo": c, "definicion": f"P75 {defi}", "fecha": f, "fecha_ref": fr, "delta_y_t": dy,
                           "n_entran": len(ent), "n_salen": len(sal), "t_entran": te, "t_salen": ts,
                           "neto_entradas_salidas_t": te - ts, "pct_delta_explicado": (te - ts) / dy * 100,
                           "entran": "; ".join(f"{p} ({a[p]:.1f} t)" for p in ent),
                           "salen": "; ".join(f"{p} ({b[p]:.1f} t)" for p in sal)})
    out["G1_provincias_por_mes_2021_2025.csv"] = pd.DataFrame(g1)
    out["G2_shocks_entradas_salidas.csv"] = pd.DataFrame(g2)
    return out


def tabla_i() -> pd.DataFrame:
    filas = []
    for m in ["XGB-37", "GC3", "GE", "XGB-43"]:
        for c in CULT:
            d = P[(P.modelo == m) & (P.cultivar == c) & (P.particion == "test") & P.anio_test.between(2021, 2025)].copy()
            por_mes = d.groupby("fecha").agg(y_true=("y_true", "first"), y_pred=("y_pred", "mean")).sort_index()
            ens = (por_mes.y_true - por_mes.y_pred).abs()
            es = por_mes.index.isin(shocks_pool(c, "MoM", 75, POOLS["principal_2021_2025"]))
            ae = ae_mat(c, POOLS["principal_2021_2025"], [m])[m].reindex(por_mes.index).to_numpy()
            filas.append({"modelo": m, "cultivo": c, "n_semillas": int(d.semilla.nunique()),
                          "MAE_media_errores_semilla": ae.mean(), "MAE_ensamble": ens.mean(),
                          "MAE_shock_media_errores_semilla": ae[es].mean(), "MAE_shock_ensamble": ens[es].mean(),
                          "n_shock": int(es.sum()), "exploratorio": m == "XGB-43"})
    return pd.DataFrame(filas)


# ----------------------------------------------------------------------------------------------- comparison
def sha_lf(p: Path) -> str:
    return hashlib.sha256(p.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def comparar(nuevo: Path, publicado: Path) -> dict:
    a = pd.read_csv(nuevo, dtype=str, keep_default_na=False, encoding="utf-8")
    b = pd.read_csv(publicado, dtype=str, keep_default_na=False, encoding="utf-8")
    r = {"identical_bytes": sha_lf(nuevo) == sha_lf(publicado)}
    if list(a.columns) != list(b.columns) or a.shape != b.shape:
        r.update(status="DIFFERENT_SHAPE", new_shape=list(a.shape), published_shape=list(b.shape),
                 new_columns=list(a.columns), published_columns=list(b.columns))
        return r
    dif = a.to_numpy() != b.to_numpy()
    r.update(cells=int(dif.size), cells_different=int(dif.sum()), max_abs=0.0, max_rel=0.0, non_numeric_different=0)
    for i, j in zip(*np.nonzero(dif)):
        x, y = pd.to_numeric(a.iat[i, j], errors="coerce"), pd.to_numeric(b.iat[i, j], errors="coerce")
        if pd.notna(x) and pd.notna(y):
            r["max_abs"] = max(r["max_abs"], abs(x - y))
            if y != 0:
                r["max_rel"] = max(r["max_rel"], abs(x - y) / abs(y))
        else:
            r["non_numeric_different"] += 1
    if r["cells_different"]:
        cols = sorted({a.columns[j] for j in np.nonzero(dif)[1]})
        r["columns_with_differences"] = cols
    r["status"] = "IDENTICAL" if r["cells_different"] == 0 else "DIFFERENT_CELLS"
    return r


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--salida", type=Path, help="folder for the regenerated CSV (default: a temporary folder, removed at the end)")
    ap.add_argument("--json", type=Path, help="write the comparison report to this JSON file")
    ap.add_argument("--estricto", action="store_true", help="exit with code 1 if any cell differs")
    args = ap.parse_args()
    salida = args.salida or Path(tempfile.mkdtemp(prefix="g7_fase1_"))
    if salida.resolve() == AQUI:
        raise SystemExit("--salida must not be the folder of the published CSV.")
    salida.mkdir(parents=True, exist_ok=True)

    tablas: dict[str, pd.DataFrame] = {}
    tablas.update(tabla_b())
    tablas["C_metricas_escaladas_shock.csv"] = tabla_c()
    tablas["D_ranking_modelos_limpios.csv"] = tabla_d()
    tablas.update(tabla_e())
    tablas["F_parametros_por_observacion.csv"] = tabla_f()
    tablas.update(tabla_g())
    tablas["I_ensamble_semillas.csv"] = tabla_i()

    informe = {}
    for nombre in ARCHIVOS:
        tablas[nombre].to_csv(salida / nombre, index=False, encoding="utf-8", lineterminator="\n")
        informe[nombre] = comparar(salida / nombre, AQUI / nombre)
        r = informe[nombre]
        extra = (f"{r['cells_different']} of {r['cells']} cells differ, max |diff| = {r['max_abs']:.3g}, "
                 f"max rel = {r['max_rel']:.3g}") if r["status"] == "DIFFERENT_CELLS" else ""
        print(f"[{r['status']}{', same bytes' if r['identical_bytes'] else ''}] {nombre} {extra}", flush=True)
    n_ok = sum(r["status"] == "IDENTICAL" for r in informe.values())
    print(f"{n_ok} of {len(ARCHIVOS)} tables identical cell by cell.")
    if args.json:
        args.json.write_text(json.dumps({"identical_tables": n_ok, "tables": len(ARCHIVOS), "files": informe}, indent=1), encoding="utf-8")
    if args.salida is None:
        shutil.rmtree(salida, ignore_errors=True)
    raise SystemExit(1 if args.estricto and n_ok != len(ARCHIVOS) else 0)


if __name__ == "__main__":
    main()
