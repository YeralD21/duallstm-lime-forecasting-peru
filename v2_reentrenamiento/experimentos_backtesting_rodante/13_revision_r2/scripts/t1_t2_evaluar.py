"""R2-T1 y R2-T2: metricas, IC bootstrap, DM-HLN y ranking con 12 modelos (10 del articulo + ETS + Theta).

POSTERIOR AL PROTOCOLO: ETS y Theta se reportan como robustez; el ranking principal (10 modelos) no cambia.
Metodologia identica a 02_scripts/08_metricas.py (T06, T08) y 12_revision_g7/scripts/evaluar.py (T1, T5), con
lib/evaluacion.py: error absoluto promediado entre semillas; bootstrap iid pareado estratificado por ventana,
B = 10 000, semilla 42 (un generador nuevo por cada remuestreo, como en 08_metricas.py); empate con el primero =
IC 95 % de la diferencia con el mejor contiene 0; "consistently top-ranked" = primero o empatado en >= 3 de
P50, P60, P75 y P90. Control: para los 10 modelos originales se exige igualdad con T06/T08 publicados.

Salidas en 13_revision_r2/resultados/: T1_*.csv, T2_*.csv y fragmentos .md para el informe.
Uso: python 13_revision_r2/scripts/t1_t2_evaluar.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import r2lib as R  # noqa: E402
from lib.entorno import preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import glob  # noqa: E402
import json  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from lib import evaluacion as ev  # noqa: E402

ORIG10 = list(ev.MODELOS_RANKING)
MOD12 = ORIG10 + list(R.NUEVOS)
CULT = list(R.CULTIVARES)
POOL = list(R.VENTANAS)
PCTS = [50, 60, 75, 90]
TIPOS = {"mensual": "MoM", "interanual": "YoY"}
REF_G7 = {"sutil": "Chronos", "dulce": "SARIMA-sel"}  # referencia de 12_revision_g7 (T5)
DEC = {"sutil": 0, "dulce": 1}
OUT = R.RES


def guardar(df: pd.DataFrame, nombre: str) -> None:
    R.escribir(df, OUT / nombre)
    print("escrito", nombre, df.shape)


def md(df: pd.DataFrame) -> str:
    cab = [str(c) for c in df.columns]
    return "\n".join(["| " + " | ".join(cab) + " |", "|" + "|".join("---" for _ in cab) + "|"]
                     + ["| " + " | ".join(str(v) for v in r) + " |" for r in df.itertuples(index=False)])


def num(x, d):
    return "—" if x is None or not np.isfinite(x) else f"{x:,.{d}f}"


def etiqueta(m: str) -> str:
    return f"{m} †" if m in R.NUEVOS else m


# ----------------------------------------------------------------------------- errores
S = ev.series()
orig = pd.read_csv(ev.BR / "05_predicciones" / "predicciones_consolidadas.csv", dtype={"fecha": str})
orig["semilla"] = orig["semilla"].astype("Int64")
nuevos = []
for ruta in sorted(glob.glob(str(R.UNI / "*" / "*" / "*" / "predicciones.csv"))):
    info = json.loads((Path(ruta).parent / "info.json").read_text(encoding="utf-8"))
    p = pd.read_csv(ruta, dtype={"fecha": str})
    p["modelo"], p["cultivar"], p["anio_test"], p["semilla"] = info["modelo"], info["cultivar"], int(info["anio_test"]), pd.NA
    nuevos.append(p[["modelo", "cultivar", "anio_test", "semilla", "particion", "fecha", "y_true", "y_pred"]])
nuevos = pd.concat(nuevos, ignore_index=True)
nuevos["semilla"] = nuevos["semilla"].astype("Int64")
if sorted(nuevos.modelo.unique()) != sorted(R.NUEVOS) or len(nuevos[nuevos.particion == "test"]) != 2 * 2 * 5 * 12:
    raise SystemExit("Faltan unidades de ETS/Theta: ejecute antes t1_ets_theta.py")
ES = ev.errores_por_semilla(pd.concat([orig, nuevos], ignore_index=True), S, "test")
ERR = ev.promediar_semillas(ES)
D = ev.denominadores_mase().set_index(["cultivar", "anio_test"]).D_mase
M = ev.mascaras(S, POOL, PCTS)


def matriz(c, anios, modelos):
    pv = ev.matriz(ERR, modelos, c, anios)
    claves = list(pv.index)
    return pv, claves, np.array([a for a, _ in claves]), np.array([D[(c, a)] for a, _ in claves])


def rng():
    return np.random.default_rng(ev.SEMILLA_BOOT)


# ----------------------------------------------------------------------------- T1: metricas (pool 2021-2025)
filas = []
for c in CULT:
    pv, claves, est, Dv = matriz(c, POOL, MOD12)
    AE = pv.to_numpy().T
    g = AE[:, ev.indices_iid(est, np.ones(len(est), bool), rng())].mean(axis=2)
    for tipo, et in TIPOS.items():
        sh = ev.vector_shock(claves, M, c, tipo, 75)
        bs = AE[:, ev.indices_iid(est, sh, rng())].mean(axis=2)
        bn = AE[:, ev.indices_iid(est, ~sh, rng())].mean(axis=2)
        for i, m in enumerate(MOD12):
            k = ev.metricas(AE[i], sh, Dv, ev.rmse_semillas(ES, m, c, POOL))
            filas.append({"cultivo": c, "modelo": m, "anadido_posterior": m in R.NUEVOS, "definicion_shock": et, "percentil": 75, **k,
                          "MASE_shock": float(np.mean(AE[i][sh] / Dv[sh])),
                          "IC_MAE_lo": ev.ic(g[i])[0], "IC_MAE_hi": ev.ic(g[i])[1],
                          "IC_shock_lo": ev.ic(bs[i])[0], "IC_shock_hi": ev.ic(bs[i])[1],
                          "IC_normal_lo": ev.ic(bn[i])[0], "IC_normal_hi": ev.ic(bn[i])[1]})
T1 = pd.DataFrame(filas)
guardar(T1, "T1_metricas_12_modelos_2021_2025.csv")

# control frente a T06 publicado (10 modelos originales)
t06 = pd.read_csv(ev.BR / "06_metricas" / "agregadas" / "T06_agregadas_IC.csv")
t06 = t06[(t06.conjunto == "principal_2021_2025") & (t06.percentil == 75)]
pares = {"MAE": "MAE", "MAE_shock": "MAE_shock", "MAE_normal": "MAE_normal", "Delta_s": "Delta_s", "MASE": "MASE",
         "IC_MAE_lo": "iid_global_lo", "IC_MAE_hi": "iid_global_hi", "IC_shock_lo": "iid_shock_lo", "IC_shock_hi": "iid_shock_hi",
         "IC_normal_lo": "iid_normal_lo", "IC_normal_hi": "iid_normal_hi"}
control = []
for r in T1[~T1.anadido_posterior].itertuples():
    tipo = {v: k for k, v in TIPOS.items()}[r.definicion_shock]
    ref = t06[(t06.cultivar == r.cultivo) & (t06.tipo == tipo) & (t06.modelo == r.modelo)].iloc[0]
    for a, b in pares.items():
        control.append(abs(getattr(r, a) - ref[b]) <= 1e-9 * max(1.0, abs(ref[b])))
if not all(control):
    raise AssertionError(f"T1 no reproduce T06 publicado en {control.count(False)} celdas")
print(f"control T06: {len(control)} celdas de los 10 modelos originales identicas a las publicadas")

# Tabla tipo Tabla 3 (MAE y MAE_shock MoM P75 con IC; Delta_s) + YoY y MASE_shock
vista = []
for c in CULT:
    d = DEC[c]
    a = T1[(T1.cultivo == c) & (T1.definicion_shock == "MoM")].set_index("modelo")
    b = T1[(T1.cultivo == c) & (T1.definicion_shock == "YoY")].set_index("modelo")
    for m in MOD12:
        x, y = a.loc[m], b.loc[m]
        vista.append({"cultivo": c, "modelo": etiqueta(m),
                      "MAE todos (IC95)": f"{num(x.MAE, d)} ({num(x.IC_MAE_lo, d)}–{num(x.IC_MAE_hi, d)})",
                      "MAE normal MoM (IC95)": f"{num(x.MAE_normal, d)} ({num(x.IC_normal_lo, d)}–{num(x.IC_normal_hi, d)})",
                      "MAE shock MoM P75 (IC95)": f"{num(x.MAE_shock, d)} ({num(x.IC_shock_lo, d)}–{num(x.IC_shock_hi, d)})",
                      "Δs MoM %": num(x.Delta_s, 1), "MASE_shock MoM": num(x.MASE_shock, 2),
                      "MAE shock YoY P75 (IC95)": f"{num(y.MAE_shock, d)} ({num(y.IC_shock_lo, d)}–{num(y.IC_shock_hi, d)})",
                      "MAE normal YoY": num(y.MAE_normal, d), "MASE_shock YoY": num(y.MASE_shock, 2)})
V1 = pd.DataFrame(vista)
n_sh = {(c, et): int(T1[(T1.cultivo == c) & (T1.definicion_shock == et)].n_shock.iloc[0]) for c in CULT for et in TIPOS.values()}

# ----------------------------------------------------------------------------- T1: DM-HLN frente al mejor
mejor10 = {c: T1[(T1.cultivo == c) & (T1.definicion_shock == "MoM") & ~T1.anadido_posterior].set_index("modelo").MAE.idxmin() for c in CULT}
filas = []
for c in CULT:
    pv, claves, est, _ = matriz(c, POOL, MOD12)
    for ref_tipo, ref in (("referencia_G7", REF_G7[c]), ("menor_MAE_10_modelos", mejor10[c])):
        for m in R.NUEVOS:
            for alc, sub in (("todos", np.ones(len(claves), bool)), ("shock_MoM_P75", ev.vector_shock(claves, M, c, "mensual", 75)),
                             ("shock_YoY_P75", ev.vector_shock(claves, M, c, "interanual", 75))):
                k = ev.dm_hln(pv[m].to_numpy()[sub], pv[ref].to_numpy()[sub])
                filas.append({"cultivo": c, "modelo": m, "referencia": ref, "tipo_referencia": ref_tipo, "alcance": alc, **k})
DM = pd.DataFrame(filas).drop_duplicates(["cultivo", "modelo", "referencia", "alcance"])
guardar(DM, "T1_DM_HLN_vs_mejor.csv")

# ----------------------------------------------------------------------------- T1: ranking con 12 modelos
filas = []
for c in CULT:
    pv, claves, est, _ = matriz(c, POOL, MOD12)
    AE = pv.to_numpy().T
    for tipo, et in TIPOS.items():
        for p in PCTS:
            sh = ev.vector_shock(claves, M, c, tipo, p)
            for grupo, mods in (("12_modelos", MOD12), ("10_modelos", ORIG10)):
                r = ev.ranking(AE[[MOD12.index(m) for m in mods]], mods, est, sh, "iid")
                r.insert(0, "percentil", p)
                r.insert(0, "definicion", et)
                r.insert(0, "cultivo", c)
                r.insert(0, "grupo", grupo)
                filas.append(r)
RK = pd.concat(filas, ignore_index=True)
guardar(RK, "T1_ranking_shock_P50_P90.csv")
# control frente a T08 publicado (10 modelos, iid, shock, principal)
t08 = pd.read_csv(ev.BR / "06_metricas" / "agregadas" / "T08_ranking_empates.csv")
t08 = t08[(t08.conjunto == "principal_2021_2025") & (t08.criterio == "shock") & (t08.bootstrap == "iid")]
a = RK[RK.grupo == "10_modelos"].assign(tipo=lambda d: d.definicion.map({v: k for k, v in TIPOS.items()}))
mm = a.merge(t08, left_on=["cultivo", "tipo", "percentil", "modelo"], right_on=["cultivar", "tipo", "percentil", "modelo"], suffixes=("", "_pub"))
if len(mm) != len(a) or not ((mm.posicion == mm.posicion_pub).all() and (mm.primero == mm.primero_pub).all()):
    raise AssertionError("El ranking de 10 modelos no reproduce T08 publicado")
print(f"control T08: {len(mm)} filas (posicion y primero/empate) identicas a las publicadas")

rob = RK.groupby(["grupo", "cultivo", "definicion", "modelo"]).primero.sum().rename("n_primero_de_4").reset_index()
rob["consistently_top_ranked"] = rob.n_primero_de_4 >= 3
guardar(rob, "T1_robustez_3de4.csv")
vista = []
for c in CULT:
    r12 = RK[(RK.grupo == "12_modelos") & (RK.cultivo == c)]
    for m in MOD12:
        fila = {"cultivo": c, "modelo": etiqueta(m)}
        for p in PCTS:
            x = r12[(r12.definicion == "MoM") & (r12.percentil == p) & (r12.modelo == m)].iloc[0]
            fila[f"MoM P{p}"] = f"{int(x.posicion)}{'*' if x.primero else ''}"
        for et in TIPOS.values():
            n12 = int(rob[(rob.grupo == "12_modelos") & (rob.cultivo == c) & (rob.definicion == et) & (rob.modelo == m)].n_primero_de_4.iloc[0])
            fila[f"1º/empate {et} (de 4)"] = n12
            fila[f"Robusto {et}"] = "Sí" if n12 >= 3 else "No"
            if m in ORIG10:
                n10 = int(rob[(rob.grupo == "10_modelos") & (rob.cultivo == c) & (rob.definicion == et) & (rob.modelo == m)].n_primero_de_4.iloc[0])
                fila[f"Robusto {et} (10 modelos, publicado)"] = "Sí" if n10 >= 3 else "No"
            else:
                fila[f"Robusto {et} (10 modelos, publicado)"] = "—"
        vista.append(fila)
V2 = pd.DataFrame(vista)

# ----------------------------------------------------------------------------- T2: solo 2025
filas, pool_first = [], {}
for c in CULT:
    pvp, clp, estp, _ = matriz(c, POOL, MOD12)
    pv, claves, est, _ = matriz(c, [2025], MOD12)
    AE, AEp = pv.to_numpy().T, pvp.to_numpy().T
    for crit, tipo in (("todos", None), ("shock_MoM_P75", "mensual"), ("shock_YoY_P75", "interanual")):
        sub = np.ones(len(claves), bool) if tipo is None else ev.vector_shock(claves, M, c, tipo, 75)
        subp = np.ones(len(clp), bool) if tipo is None else ev.vector_shock(clp, M, c, tipo, 75)
        r = ev.ranking(AE, MOD12, est, sub, "iid")
        rp = ev.ranking(AEp, MOD12, estp, subp, "iid")
        b = AE[:, ev.indices_iid(est, sub, rng())].mean(axis=2) if sub.any() else None
        for i, m in enumerate(MOD12):
            x, xp = r.iloc[i], rp.iloc[i]
            lo, hi = ev.ic(b[i]) if b is not None else (np.nan, np.nan)
            filas.append({"cultivo": c, "criterio": crit, "modelo": m, "anadido_posterior": m in R.NUEVOS, "n_meses": int(sub.sum()),
                          "MAE_2025": x.MAE, "IC_lo": lo, "IC_hi": hi, "posicion_2025": None if pd.isna(x.posicion) else int(x.posicion), "primero_o_empate_2025": bool(x.primero),
                          "MAE_pool_2021_2025": xp.MAE, "posicion_pool": None if pd.isna(xp.posicion) else int(xp.posicion), "primero_o_empate_pool": bool(xp.primero)})
T2 = pd.DataFrame(filas)
guardar(T2, "T2_ranking_2025.csv")
def primero(d, col):
    return "— (sin meses)" if d[col].isna().all() else d.loc[d[col].idxmin(), "modelo"]


resp = []
for c in CULT:
    for crit in ("todos", "shock_MoM_P75", "shock_YoY_P75"):
        d = T2[(T2.cultivo == c) & (T2.criterio == crit)]
        d10 = d[~d.anadido_posterior]
        p25, pp = primero(d, "MAE_2025"), primero(d, "MAE_pool_2021_2025")
        resp.append({"cultivo": c, "criterio": crit, "n_meses_2025": int(d.n_meses.iloc[0]),
                     "1º 2025 (12 mod.)": p25, "1º pool (12 mod.)": pp,
                     "1º 2025 (10 mod.)": primero(d10, "MAE_2025"), "1º pool (10 mod.)": primero(d10, "MAE_pool_2021_2025"),
                     "mismo 1º (12)": "—" if p25.startswith("—") else ("Sí" if p25 == pp else "No"),
                     "mismo 1º (10)": "—" if p25.startswith("—") else ("Sí" if primero(d10, "MAE_2025") == primero(d10, "MAE_pool_2021_2025") else "No"),
                     "empatados con el 1º en 2025": ", ".join(d[d.primero_o_empate_2025].sort_values("MAE_2025").modelo) or "—"})
T2R = pd.DataFrame(resp)
guardar(T2R, "T2_primer_lugar_2025_vs_pool.csv")
vista = []
for c in CULT:
    dd = DEC[c]
    for m in MOD12:
        fila = {"cultivo": c, "modelo": etiqueta(m)}
        for crit, et in (("todos", "todos"), ("shock_MoM_P75", "shock MoM P75"), ("shock_YoY_P75", "shock YoY P75")):
            x = T2[(T2.cultivo == c) & (T2.criterio == crit) & (T2.modelo == m)].iloc[0]
            fila[f"MAE {et} (IC95)"] = f"{num(x.MAE_2025, dd)} ({num(x.IC_lo, dd)}–{num(x.IC_hi, dd)})"
            fila[f"pos. {et}"] = "—" if pd.isna(x.posicion_2025) else f"{int(x.posicion_2025)}{'*' if x.primero_o_empate_2025 else ''}"
        vista.append(fila)
V3 = pd.DataFrame(vista)

# ----------------------------------------------------------------------------- fragmentos markdown
nota = ("† = añadido posterior al protocolo (revisión R2); no altera el ranking principal. "
        "* = primero o empatado con el primero (IC 95 % bootstrap pareado de la diferencia con el mejor contiene 0).")
txt = [f"<!-- generado por t1_t2_evaluar.py; no editar a mano -->\n",
       "## T1.a Precisión agregada 2021–2025 (formato Tabla 3, 12 modelos)\n",
       "MAE en toneladas con IC 95 % bootstrap pareado (meses remuestreados dentro de cada ventana, B = 10 000, semilla 42). "
       "Δs = (MAE_shock − MAE)/MAE × 100. MASE_shock con los denominadores por ventana del artículo "
       "(03_ventanas/denominador_mase_por_ventana.csv). " + nota + "\n"]
for c in CULT:
    txt.append(f"\n### {c} ({60} meses; shock MoM P75: {n_sh[(c, 'MoM')]}; shock YoY P75: {n_sh[(c, 'YoY')]})\n")
    txt.append(md(V1[V1.cultivo == c].drop(columns="cultivo")))
txt.append("\n\n## T1.b Diebold–Mariano HLN (pérdida absoluta, h = 1) de ETS y Theta frente al mejor\n")
dm = DM.copy()
for col in ("d_media", "HLN", "p"):
    dm[col] = dm[col].map(lambda v: num(v, 3))
txt.append(md(dm[["cultivo", "modelo", "referencia", "tipo_referencia", "alcance", "n", "d_media", "HLN", "p"]]))
txt.append("\n\n## T1.c Ranking por MAE en meses de shock, 12 modelos (formato Tabla 4)\n\n" + nota + "\n")
for c in CULT:
    txt.append(f"\n### {c}\n")
    txt.append(md(V2[V2.cultivo == c].drop(columns="cultivo")))
txt.append("\n\n## T2 Ranking solo en 2025 (12 modelos)\n\n" + nota + " IC con remuestreo de los meses de 2025 (un estrato).\n")
for c in CULT:
    txt.append(f"\n### {c}\n")
    txt.append(md(V3[V3.cultivo == c].drop(columns="cultivo")))
txt.append("\n\n### Primer lugar: 2025 frente al pool 2021–2025\n")
txt.append(md(T2R))
(OUT / "tablas_T1_T2.md").write_text("\n".join(txt) + "\n", encoding="utf-8", newline="\n")
print("escrito tablas_T1_T2.md")
