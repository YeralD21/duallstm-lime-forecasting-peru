"""Revision G7 - Fase 2 (solo lectura). Definiciones alternativas de shock, evento 2023 y efecto del registro.

Lee solo archivos existentes y escribe CSV en esta carpeta. No reentrena ni modifica nada.
Uso (desde cualquier carpeta):  <venv>/python.exe -I g7_fase2.py <raiz_repo>

Definiciones de shock (para cada ventana Y, umbral = percentil lineal de la historia hasta el origen dic Y-1;
shock si r_t > umbral, comparacion estricta, igual que lib/shocks.py):
  MoM  r_t = |y_t - y_(t-1)| / y_(t-1)                     historia: 2016-02..origen
  YoY  r_t = |y_t - y_(t-12)| / y_(t-12)                   historia: 2017-01..origen
  3M   r_t = |y_t - y_(t-3)| / y_(t-3)                     historia: 2016-04..origen
  STL  STL robusta (period=12, seasonal=13, resto por defecto de statsmodels) ajustada en y[2016-01..origen];
       a_t = y_t - S_t (historia: S_t estacional in-sample); en el test a_t = y_t - S_origen(mes), con S_origen(m)
       = componente estacional del mes m en el ultimo ano de la historia (Y-1); r_t = |a_t - a_(t-1)| / a_(t-1).
       historia: 2016-02..origen.
Bootstrap "primero o empatado": replica exacta de lib/evaluacion.py ranking()+indices_iid() (iid pareado,
estratificado por ventana, dentro de los meses de shock, B=10000, default_rng(42) por llamada).
"""
import re
import sys
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd
from statsmodels.tsa.seasonal import STL

RAIZ = Path(sys.argv[1])
BR = RAIZ / "v2_reentrenamiento" / "experimentos_backtesting_rodante"
INT = RAIZ / "v2_reentrenamiento" / "data" / "interim"
XLSX = RAIZ / "v2_reentrenamiento" / "data" / "raw" / "midagri" / "sisagri_2015_2026.xlsx"
OUT = Path(__file__).resolve().parent

MODELOS = ["Naive", "Seasonal Naive", "Chronos", "SARIMA", "SARIMA-sel", "Ridge", "ElasticNet", "XGB-37", "GC3", "GE"]
MULTI = ["Ridge", "ElasticNet", "XGB-37", "GC3", "GE", "XGB-43"]
UNI = ["Naive", "Seasonal Naive", "Chronos", "SARIMA", "SARIMA-sel"]
CULT = ["sutil", "dulce"]
POOLS = {"principal_2021_2025": [2021, 2022, 2023, 2024, 2025], "sensibilidad_2023_2025": [2023, 2024, 2025]}
PCTS = [50, 60, 75, 90]
DEFS = ["MoM", "YoY", "STL", "3M"]
B, SEMILLA = 10_000, 42
STL_PAR = {"period": 12, "seasonal": 13, "robust": True}


def guardar(df: pd.DataFrame, nombre: str) -> None:
    df.to_csv(OUT / nombre, index=False, encoding="utf-8")
    print("escrito", nombre, df.shape)


def serie_desde(df: pd.DataFrame, col: str) -> pd.Series:
    idx = df.iloc[:, 0].astype(int).astype(str) + "-" + df.iloc[:, 1].astype(int).map("{:02d}".format)
    return pd.Series(df[col].astype(float).to_numpy(), index=idx.to_numpy()).sort_index()


S = {c: serie_desde(pd.read_csv(INT / f"limon_{c}_nacional_mensual.csv", encoding="utf-8-sig"), "produccion_t_nacional") for c in CULT}
E = pd.read_csv(BR / "05_predicciones/errores_test_promediados_semillas.csv")
DEN = pd.read_csv(BR / "03_ventanas/denominador_mase_por_ventana.csv")
MK = pd.read_csv(BR / "03_ventanas/umbrales_y_mascaras.csv")


def meses(anio: int) -> list[str]:
    return [f"{anio}-{m:02d}" for m in range(1, 13)]


# ----------------------------------------------------------------------------- cambios por definicion
def cambios(s: pd.Series, defi: str, anio: int) -> tuple[pd.Series, pd.Series, dict]:
    """(historia hasta el origen, cambios de los 12 meses de test, info). Solo usa y hasta el origen para umbral/STL."""
    origen = f"{anio - 1}-12"
    s = s.sort_index()
    if defi in ("MoM", "YoY", "3M"):
        k = {"MoM": 1, "YoY": 12, "3M": 3}[defi]
        r = ((s - s.shift(k)).abs() / s.shift(k)).dropna()
        return r[r.index <= origen], r.reindex(meses(anio)), {}
    h = s[s.index <= origen]
    fit = STL(h.to_numpy(), **STL_PAR).fit()
    est = pd.Series(fit.seasonal, index=h.index)
    a_h = h - est
    r_h = ((a_h - a_h.shift(1)).abs() / a_h.shift(1)).dropna()
    s_origen = {int(m[5:]): est[m] for m in meses(anio - 1)}
    a_t = pd.Series([s[m] - s_origen[int(m[5:])] for m in meses(anio)], index=meses(anio))
    a_full = pd.concat([a_h.iloc[[-1]], a_t])
    r_t = ((a_full - a_full.shift(1)).abs() / a_full.shift(1)).dropna()
    info = {"min_a_hist": float(a_h.min()), "min_a_test": float(a_t.min()), "n_hist_stl": len(h)}
    return r_h, r_t, info


def mascara(s: pd.Series, defi: str, anio: int, p: int):
    r_h, r_t, info = cambios(s, defi, anio)
    u = float(np.percentile(r_h.to_numpy(), p, method="linear"))
    return u, [m for m in meses(anio) if r_t[m] > u], r_t, info


MASC, INFO = {}, []
for c in CULT:
    for defi in DEFS:
        for anio in range(2020, 2026):
            for p in PCTS:
                u, sh, r_t, info = mascara(S[c], defi, anio, p)
                MASC[(c, defi, anio, p)] = (u, sh, r_t)
                if p == 75:
                    INFO.append({"cultivo": c, "definicion": defi, "anio": anio, "umbral_P75": u, **info})
guardar(pd.DataFrame(INFO), "00_umbrales_P75_y_control_STL.csv")

# control: MoM e YoY reproducen las mascaras del pipeline
dif = 0
for c in CULT:
    for defi, tipo in (("MoM", "mensual"), ("YoY", "interanual")):
        for anio in range(2021, 2026):
            for p in PCTS:
                r = MK[(MK.cultivar == c) & (MK.tipo == tipo) & (MK.anio_test == anio) & (MK.percentil == p)].iloc[0]
                ref = [x for x in str(r.meses_shock).split(";") if x and x != "nan"]
                dif += int(sorted(ref) != sorted(MASC[(c, defi, anio, p)][1])) + int(abs(r.umbral - MASC[(c, defi, anio, p)][0]) > 1e-12)
print("CONTROL mascaras MoM/YoY distintas del pipeline:", dif)


def shocks_pool(c, defi, p, anios):
    return [m for a in anios for m in MASC[(c, defi, a, p)][1]]


def ae_mat(c, anios, modelos):
    d = E[(E.cultivar == c) & E.anio_test.isin(anios) & E.modelo.isin(modelos)]
    return d.pivot(index="fecha", columns="modelo", values="ae")[modelos].sort_index()


def indices_iid(estratos, sub, rng, b=B):  # copia de lib/evaluacion.py:151-158
    cols = []
    for g in pd.unique(estratos):
        pos = np.flatnonzero((estratos == g) & sub)
        if len(pos):
            cols.append(pos[rng.integers(0, len(pos), size=(b, len(pos)))])
    return np.concatenate(cols, axis=1)


def ranking(AE, nombres, estratos, sub):  # copia de lib/evaluacion.py:112-134 (tipo iid)
    rng = np.random.default_rng(SEMILLA)
    est = AE[:, indices_iid(estratos, sub, rng)].mean(axis=2)
    mae = AE[:, sub].mean(axis=1)
    mejor = int(np.argmin(mae))
    out = []
    for i, m in enumerate(nombres):
        d = est[i] - est[mejor]
        lo, hi = np.percentile(d, 2.5), np.percentile(d, 97.5)
        out.append({"modelo": m, "primero_o_empatado": bool(i == mejor or (lo <= 0 <= hi)), "dif_vs_mejor_lo": lo, "dif_vs_mejor_hi": hi})
    return pd.DataFrame(out)


# ----------------------------------------------------------------------------- 1. definiciones alternativas
filas, dist, cap = [], [], []
for c in CULT:
    for pool, anios in POOLS.items():
        A = ae_mat(c, anios, MODELOS)
        AE = A.to_numpy().T
        estr = np.array([int(f[:4]) for f in A.index])
        Dm = DEN[DEN.cultivar == c].set_index("anio_test").D_mase
        dvec = np.array([Dm[int(f[:4])] for f in A.index])
        for defi in DEFS:
            for p in PCTS:
                sh = shocks_pool(c, defi, p, anios)
                es = A.index.isin(sh)
                if es.sum() == 0:
                    continue
                rk = ranking(AE, MODELOS, estr, es).set_index("modelo")
                mae_s = A[es].mean()
                sn = mae_s["Seasonal Naive"]
                for m in MODELOS:
                    ae = A[m].to_numpy()
                    filas.append({"cultivo": c, "pool": pool, "definicion": defi, "percentil": p, "modelo": m, "n_shock": int(es.sum()),
                                  "MAE_normal": ae[~es].mean(), "MAE_shock": ae[es].mean(), "t_de_mas": ae[es].mean() - ae[~es].mean(),
                                  "MASE_shock": np.mean(ae[es] / dvec[es]), "MAE_shock_rel_SNaive": ae[es].mean() / sn,
                                  "rango_MAE_shock": int(mae_s.rank(method="min")[m]),
                                  "primero_o_empatado": rk.loc[m, "primero_o_empatado"],
                                  "IC95_dif_vs_mejor_lo": rk.loc[m, "dif_vs_mejor_lo"], "IC95_dif_vs_mejor_hi": rk.loc[m, "dif_vs_mejor_hi"]})
                if pool == "principal_2021_2025":
                    cnt = pd.Series([int(x[5:]) for x in sh]).value_counts().reindex(range(1, 13), fill_value=0)
                    dist.append({"cultivo": c, "definicion": defi, "percentil": p, "n_shock": len(sh), **{f"m{k:02d}": int(v) for k, v in cnt.items()}})
                    if c == "sutil":
                        w = [m for m in sh if "2023-03" <= m <= "2023-12"]
                        cap.append({"definicion": defi, "percentil": p, "n_capturados_mar_dic_2023": len(w), "meses": "; ".join(w),
                                    "umbral_2023": MASC[(c, defi, 2023, p)][0]})
R = pd.DataFrame(filas)
guardar(R, "01_definiciones_alternativas_metricas.csv")
guardar(pd.DataFrame(dist), "01b_distribucion_mes_calendario.csv")
guardar(pd.DataFrame(cap), "01c_sutil_2023_capturados.csv")
rob = (R.groupby(["cultivo", "pool", "definicion", "modelo"]).agg(n_umbrales=("percentil", "nunique"), n_primero=("primero_o_empatado", "sum"))
       .reset_index())
rob["robusto_3de4"] = rob.n_primero >= 3
guardar(rob, "01d_robustez_primero_o_empatado.csv")

# control contra T08 (MoM P75 principal, iid, shock)
t08 = pd.read_csv(BR / "06_metricas/agregadas/T08_ranking_empates.csv")
t08 = t08[(t08.conjunto == "principal_2021_2025") & (t08.tipo == "mensual") & (t08.criterio == "shock") & (t08.bootstrap == "iid") & t08.percentil.isin(PCTS)]
mine = R[(R.pool == "principal_2021_2025") & (R.definicion == "MoM")]
m = mine.merge(t08, left_on=["cultivo", "percentil", "modelo"], right_on=["cultivar", "percentil", "modelo"])
print("CONTROL T08 primero distinto:", int((m.primero_o_empatado != m.primero).sum()), "de", len(m),
      "| max dif IC:", float((m.IC95_dif_vs_mejor_lo - m.dif_vs_mejor_lo).abs().max()))

# calendario de shocks STL y 3M (P75, 2021-2025) con inicio/continuacion
cal = []
for c in CULT:
    A = ae_mat(c, POOLS["principal_2021_2025"], MODELOS)
    for defi in DEFS:
        todos = set(m for a in range(2020, 2026) for m in MASC[(c, defi, a, 75)][1])
        for a in range(2021, 2026):
            u, sh, r_t = MASC[(c, defi, a, 75)]
            for f in sh:
                prev = str(pd.Period(f, "M") - 1)
                cal.append({"cultivo": c, "definicion": defi, "fecha": f, "mes": int(f[5:]), "r_t_pct": r_t[f] * 100, "umbral_pct": u * 100,
                            "y_t": S[c][f], "episodio": "continuacion" if prev in todos else "inicio",
                            **{f"AE_{m}": A.loc[f, m] for m in MODELOS}})
CAL = pd.DataFrame(cal)
guardar(CAL, "01e_calendario_P75_todas_definiciones.csv")
ic = []
for (c, defi, ep), g in CAL.groupby(["cultivo", "definicion", "episodio"]):
    ic.append({"cultivo": c, "definicion": defi, "episodio": ep, "n": len(g), **{m: g[f"AE_{m}"].mean() for m in MODELOS}})
guardar(pd.DataFrame(ic), "04_inicio_vs_continuacion.csv")

# ----------------------------------------------------------------------------- 2. evento 2023
filas = []
for c in CULT:
    A = ae_mat(c, [2022, 2023, 2024], MODELOS + ["XGB-43"])
    for m in MODELOS + ["XGB-43"]:
        fila = {"cultivo": c, "modelo": m, "grupo": "univariado" if m in UNI else "con exogenas"}
        fila.update({f"AE_{f}": A.loc[f, m] for f in [f"2023-{k:02d}" for k in range(3, 13)]})
        for a in (2022, 2023, 2024):
            fila[f"MAE_mar_dic_{a}"] = A.loc[[f"{a}-{k:02d}" for k in range(3, 13)], m].mean()
            fila[f"MAE_mar_may_{a}"] = A.loc[[f"{a}-{k:02d}" for k in range(3, 6)], m].mean()
        filas.append(fila)
ev = pd.DataFrame(filas)
guardar(ev, "02_evento_2023.csv")

# ----------------------------------------------------------------------------- 3. registro (Excel, solo lectura)
COD = {"13010480000": "dulce", "13010170102": "sutil"}
COLS = "ABCDEFGHIJKLM"
NOMBRES = ["anio", "mes", "ubigeo", "departamento", "provincia", "distrito", "cod", "producto", "siembra", "cosecha", "produccion", "verde_actual", "precio"]


def leer_excel_limon(ruta: Path) -> pd.DataFrame:
    z = zipfile.ZipFile(ruta)
    ROW = re.compile(rb"<row [^>]*>(.*?)</row>", re.S)
    CELL = re.compile(rb'<c r="([A-M])\d+"([^>]*?)(?:/>|>(.*?)</c>)', re.S)
    filas, ss_need = [], set()
    hojas = sorted(n for n in z.namelist() if re.match(r"xl/worksheets/sheet\d+\.xml$", n))
    for h in hojas:
        buf = b""
        with z.open(h) as fh:
            while True:
                ch = fh.read(1 << 24)
                if not ch:
                    break
                buf += ch
                last = 0
                for mm in ROW.finditer(buf):
                    last = mm.end()
                    r = mm.group(1)
                    if b"13010480000" not in r and b"13010170102" not in r:
                        continue
                    d = {}
                    for col, attrs, body in CELL.findall(r):
                        v = re.search(rb"<v>(.*?)</v>", body or b"") or re.search(rb"<t[^>]*>(.*?)</t>", body or b"")
                        val = v.group(1).decode() if v else ""
                        if b't="s"' in attrs:
                            ss_need.add(int(val))
                            val = ("SS", int(val))
                        d[col.decode()] = val
                    if d.get("G") in COD:
                        filas.append(d)
                buf = buf[last:]
    ss = {}
    SI = re.compile(rb"<si>(.*?)</si>", re.S)
    i, buf = 0, b""
    with z.open("xl/sharedStrings.xml") as fh:
        while True:
            ch = fh.read(1 << 24)
            if not ch:
                break
            buf += ch
            last = 0
            for mm in SI.finditer(buf):
                if i in ss_need:
                    ss[i] = "".join(x.decode("utf-8", errors="replace") for x in re.findall(rb"<t[^>]*>(.*?)</t>", mm.group(1), re.S))
                i += 1
                last = mm.end()
            buf = buf[last:]
    res = pd.DataFrame([{n: (ss[d[k][1]] if isinstance(d.get(k), tuple) else d.get(k, "")) for k, n in zip(COLS, NOMBRES)} for d in filas])
    for k in ("siembra", "cosecha", "produccion", "verde_actual", "precio"):
        res[k] = pd.to_numeric(res[k], errors="coerce")
    res["cultivo"] = res.cod.map(COD)
    res["fecha"] = res.anio.astype(str).str[:4] + "-" + res.mes.astype(str).str.zfill(2)
    return res


X = leer_excel_limon(XLSX)
print("Excel filas limon:", X.groupby("cultivo").size().to_dict())
crudo = {c: pd.read_csv(INT / f"limon_{c}_distrito_crudo.csv", encoding="utf-8-sig", dtype=str) for c in CULT}
for c in CULT:
    x = X[(X.cultivo == c) & (X.fecha >= "2016-01") & (X.fecha <= "2025-12")]
    print(f"CONTROL Excel vs crudo {c}: filas {len(x)} vs {len(crudo[c])}; t {x.produccion.sum():.3f} vs {crudo[c].PRODUCCION.astype(float).sum():.3f}")

CINCO = [("JUNIN", "SATIPO"), ("LORETO", "MAYNAS"), ("CAJAMARCA", "CHOTA"), ("CAJAMARCA", "JAEN"), ("LORETO", "ALTO AMAZONAS")]
x = X[(X.cultivo == "dulce") & (X.fecha >= "2016-01") & (X.fecha <= "2025-12")].copy()
x["clave"] = x.departamento.str.strip() + "|" + x.provincia.str.strip()
g = (x.groupby(["clave", "fecha"]).agg(n_filas=("produccion", "size"), n_filas_prod_pos=("produccion", lambda v: int((v > 0).sum())),
                                        produccion_t=("produccion", "sum"), cosecha_ha=("cosecha", "sum"), verde_actual_ha=("verde_actual", "sum"),
                                        siembra_ha=("siembra", "sum")).reset_index())
claves5 = [f"{d}|{p}" for d, p in CINCO]
g5 = g[g.clave.isin(claves5)].copy()
todas_f = [f"{a}-{m:02d}" for a in range(2016, 2026) for m in range(1, 13)]
g5 = (g5.set_index(["clave", "fecha"]).reindex(pd.MultiIndex.from_product([claves5, todas_f], names=["clave", "fecha"])).reset_index())
g5["sin_filas"] = g5.n_filas.isna()
guardar(g5, "03a_cinco_provincias_dulce_mensual_excel.csv")
g5["mes"] = g5.fecha.str[5:].astype(int)
res = (g5.groupby(["clave", "mes"]).agg(meses_sin_filas=("sin_filas", "sum"), meses_con_prod_pos=("produccion_t", lambda v: int((v > 0).sum())),
                                         prod_media_t=("produccion_t", "mean"), cosecha_media_ha=("cosecha_ha", "mean"),
                                         verde_media_ha=("verde_actual_ha", "mean")).reset_index())
guardar(res, "03a_cinco_provincias_por_mes_calendario.csv")

# 3b/3c paneles balanceados (tablas interinas versionadas)
pan, calb = [], []
for c in CULT:
    pv = pd.read_csv(INT / f"limon_{c}_provincia.csv", encoding="utf-8-sig")
    pv["fecha"] = pv.iloc[:, 0].astype(int).astype(str) + "-" + pv.iloc[:, 1].astype(int).map("{:02d}".format)
    pv["clave"] = pv.departamento + "|" + pv.provincia
    W = pv.pivot_table(index="fecha", columns="clave", values="produccion_t", aggfunc="sum").sort_index()
    filas_presentes = W.notna().sum()
    prod_pos = (W.fillna(0) > 0).sum()
    for nombre, cols in (("prod_pos_120", prod_pos[prod_pos == 120].index), ("filas_120", filas_presentes[filas_presentes == 120].index)):
        s = W[cols].fillna(0).sum(axis=1)
        pan.append({"cultivo": c, "panel": nombre, "n_provincias": len(cols), "pct_t_2016_2025": s.sum() / S[c].sum() * 100})
        for a in range(2021, 2026):
            r = ((s - s.shift(1)).abs() / s.shift(1)).dropna()
            h = r[r.index <= f"{a - 1}-12"]
            u = float(np.percentile(h.to_numpy(), 75, method="linear"))
            orig = MASC[(c, "MoM", a, 75)][1]
            for f in meses(a):
                if r[f] > u or f in orig:
                    calb.append({"cultivo": c, "panel": nombre, "fecha": f, "mes": int(f[5:]), "shock_panel": bool(r[f] > u),
                                 "shock_serie_nacional": f in orig, "r_panel_pct": r[f] * 100, "umbral_panel_pct": u * 100})
guardar(pd.DataFrame(pan), "03b_paneles_balanceados.csv")
guardar(pd.DataFrame(calb), "03b_calendario_MoM_P75_paneles.csv")
