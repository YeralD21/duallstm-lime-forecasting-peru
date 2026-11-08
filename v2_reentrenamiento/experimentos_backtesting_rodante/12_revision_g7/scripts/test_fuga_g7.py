"""Prueba anti-fuga de la Fase 3 (G7), adaptada de 02_scripts/tests/test_fuga.py.

Para cada ventana 2021-2025, cultivo y experimento verifica que fechas usa cada paso:
  (a) pesos geograficos y scaler ajustados hasta fin_train del protocolo (Y-2 original; Y-1 en -Y1), y n de filas;
  (b) objetivos de train <= fin_train; test = 12 meses de Y; (orig) validacion = Y-1;
  (c) un paso adelante: ultima entrada = t-1 y produccion de entrada = serie real en t-1;
  (d) GC3-R: media/sd del residuo solo con meses 2017-01..fin_train; y_(t-12) < t;
  (e) PERTURBACION: se multiplica por 10 la serie nacional desde el mes t en adelante y se reconstruye todo; las
      entradas del mes t (tabular, secuencias, residuo) y el pronostico de SARIMA-Y1/SARIMA-sel-Y1 deben ser identicos;
  (f) controles negativos: scaler con un ano de mas, entrada contemporanea (y_t) y train que incluye el test;
      la prueba debe detectarlos;
  (g) artefactos de las unidades ya corridas (info.json, predicciones.csv): fechas registradas por unidad,
      contexto de Chronos = t-1, x_fecha = t-1, epocas -Y1 = mejor epoca de la base.
Escribe 12_revision_g7/logs/fuga_g7.json; sale con 1 si algo falla.
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
from lib.datos import CULTIVARES, ConstructorDatosVentana  # noqa: E402
from lib.integridad import Integridad  # noqa: E402
from lib.modelos_series import _a_un_paso, _ajustar  # noqa: E402
from lib.preparacion import EscaladorVentana, pares_tabulares, secuencias  # noqa: E402
from lib.ventanas import Ventana  # noqa: E402
from v2_reentrenamiento.src.models.features_gc2_xgboost import build_gc2_feature_spec  # noqa: E402
from v2_reentrenamiento.src.models.features_gc3_ge import build_feature_spec  # noqa: E402

MES = pd.DateOffset(months=1)
SALIDA = G.G7 / "logs" / "fuga_g7.json"


def clave(df):
    return df["año"].astype(int).astype(str) + "-" + df["mes"].astype(int).map("{:02d}".format)


def datos_perturbados(c, desde: str | None):
    d = ConstructorDatosVentana()
    if desde is not None:
        n = d.nacional[c].copy()
        k = n.iloc[:, 0].astype(int).astype(str) + "-" + n.iloc[:, 1].astype(int).map("{:02d}".format)
        n.loc[k >= desde, "produccion_t_nacional"] = n.loc[k >= desde, "produccion_t_nacional"] * 10.0
        d.nacional[c] = n
    return d


def preparar(d, c, w, raiz):
    """Reproduce exactamente la preparacion de g7lib para un experimento (sin entrenar)."""
    feats = d.features(c, w.anio_fin_train)
    esc = EscaladorVentana(w)
    df = esc.ajustar_transformar(feats)
    s = d.serie(c)
    out = {"feats": feats, "esc": esc, "df": df, "serie": s}
    if raiz == "tabular":
        spec = build_gc2_feature_spec(c)
        out["parts"] = pares_tabulares(df, spec.predictors, spec.target, w)
        out["parts_crudo"] = pares_tabulares(feats, spec.predictors, spec.target, w)  # Ridge/EN usan X sin escalar
        out["idx_prod"] = list(spec.predictors).index(spec.target)
        return out
    spec = build_feature_spec(c, "GC3")
    rama_a = tuple(spec.rama_a) + (G.LSTM_U_EXTRA if raiz == "LSTM-U" else ())
    rama_b = rama_a if raiz == "LSTM-U" else spec.rama_b
    objetivo = spec.target
    if raiz == "GC3-R":
        k = clave(df)
        y12 = k.map(lambda f: s.get(str(pd.Period(f, "M") - 12), np.nan))
        r = k.map(s) - y12
        en = (k >= "2017-01") & (k <= w.fin_train)
        out["r_meses"] = (str(k[en].min()), str(k[en].max()))
        out["r_stats"] = (float(r[en].mean()), float(r[en].std(ddof=0)))
        df = df.copy()
        df["r12_esc"] = (r - out["r_stats"][0]) / out["r_stats"][1]
        objetivo = "r12_esc"
    out["parts"] = secuencias(df, rama_a, rama_b, objetivo, w)
    out["idx_prod"] = list(rama_a).index(spec.target)
    return out


def chequeos_fechas(o, d, c, w, protocolo, nombre) -> list[str]:
    f = []
    pw = d.pesos(c, w.anio_fin_train).tabla
    if (pw["periodo_fin"] != w.fin_train).any():
        f.append(f"(a) {nombre}: pesos con periodo_fin != {w.fin_train}")
    esc, feats = o["esc"], o["feats"]
    k = clave(feats)
    n_tr = int(((k >= "2016-07") & (k <= w.fin_train)).sum())
    if esc.fechas_ajuste[1] != w.fin_train or int(esc.scaler.n_samples_seen_) != n_tr:
        f.append(f"(a) {nombre}: scaler {esc.fechas_ajuste} / n={esc.scaler.n_samples_seen_} (esperado fin {w.fin_train}, n={n_tr})")
    tr, va, te = (o["parts"][x].fechas_objetivo for x in ("train", "val", "test"))
    if tr.max() > pd.Timestamp(f"{w.fin_train}-01"):
        f.append(f"(b) {nombre}: objetivo de train {tr.max():%Y-%m} > {w.fin_train}")
    if len(te) != 12 or te.dt.year.ne(w.anio).any():
        f.append(f"(b) {nombre}: test no es {w.anio}")
    if protocolo == "orig" and (len(va) != 12 or va.dt.year.ne(w.anio - 1).any() or set(tr) & set(va)):
        f.append(f"(b) {nombre}: validacion no es Y-1 o solapa con train")
    if set(tr) & set(te):
        f.append(f"(b) {nombre}: train y test solapan")
    p = o["parts"]["test"]
    if not (p.fechas_contexto_max + MES == p.fechas_objetivo).all():
        f.append(f"(c) {nombre}: la ultima entrada de test no es t-1")
    esc_v = p.X[:, o["idx_prod"]] if p.X is not None else p.X_a[:, -1, o["idx_prod"]]
    target = f"produccion_t_{c}"
    reales = esc.invertir(target, esc_v)
    esperados = o["serie"].reindex(p.fechas_contexto_max.dt.strftime("%Y-%m")).to_numpy(float)
    if not np.allclose(reales, esperados, rtol=0, atol=1e-6):
        f.append(f"(c) {nombre}: produccion de entrada en test != serie real en t-1")
    if "r_meses" in o and (o["r_meses"][0] < "2017-01" or o["r_meses"][1] > w.fin_train):
        f.append(f"(d) {nombre}: estadisticas del residuo con meses {o['r_meses']}")
    return f


def entradas_mes(o, t: str):
    p = o["parts"]["test"]
    i = int(np.flatnonzero(p.fechas_objetivo.dt.strftime("%Y-%m").to_numpy() == t)[0])
    if p.X is not None:
        xs = [p.X[i], o["parts_crudo"]["test"].X[i]]
    else:
        xs = [p.X_a[i], p.X_b[i]]
    return xs + ([np.array(o["r_stats"])] if "r_stats" in o else [])


def perturbacion(c, w, raiz, meses_t) -> list[str]:
    f = []
    base = preparar(datos_perturbados(c, None), c, w, raiz)
    for t in meses_t:
        pert = preparar(datos_perturbados(c, t), c, w, raiz)
        for a, b in zip(entradas_mes(base, t), entradas_mes(pert, t)):
            if not np.array_equal(np.asarray(a), np.asarray(b)):
                f.append(f"(e) {raiz}/{w.anio}/{c}: las entradas del mes {t} cambian al perturbar y_(>= {t})")
                break
    return f


def sarima_pred(s, w, o, so, op, t):
    train = s[(s.index >= "2016-07") & (s.index <= w.fin_train)]
    fit, _ = _ajustar(train.to_numpy(), o, so, op)
    meses = [m for m in w.meses_test if m <= t]
    filas, _ = _a_un_paso(fit, meses, [s[m] for m in meses])
    return filas[-1]["y_pred"]


def perturbacion_sarima(c, anio, t) -> list[str]:
    f = []
    w = G.VentanaY1(anio)
    s0 = ConstructorDatosVentana().serie(c).sort_index().astype(float)
    s1 = s0.copy()
    s1[s1.index >= t] *= 10.0
    cfg = G.HP["sarima_congelado"]
    hp = G.HP["sarima_seleccion_por_ventana_DA9"]
    sel = json.loads((G.ORIG / "sarima_sel" / c / str(anio) / "info.json").read_text(encoding="utf-8"))
    casos = {"SARIMA-Y1": (cfg[c]["order"], cfg[c]["seasonal_order"], dict(cfg["opciones"])),
             "SARIMA-sel-Y1": (sel["order"], sel["seasonal_order"], {**hp["opciones_ajuste"], "maxiter": hp["maxiter_candidatos_y_final"]})}
    for nombre, (o, so, op) in casos.items():
        a, b = sarima_pred(s0, w, o, so, op, t), sarima_pred(s1, w, o, so, op, t)
        if a != b:
            f.append(f"(e) {nombre}/{anio}/{c}: pronostico de {t} cambia al perturbar y_(>= {t}) ({a} vs {b})")
    return f


def controles_negativos(c) -> dict:
    out = {}
    w = G.VentanaY1(2023)
    d = ConstructorDatosVentana()
    o = preparar(d, c, w, "tabular")
    malo = EscaladorVentana(G.VentanaY1(2024))  # scaler ajustado con un ano de mas
    malo.ajustar_transformar(o["feats"])
    o2 = dict(o, esc=malo)
    out["scaler_un_ano_extra_detectado"] = any("(a)" in x for x in chequeos_fechas(o2, d, c, w, "Y1", "neg"))
    # entrada contemporanea: secuencia que incluye y_t (desplazada un mes) -> la perturbacion debe detectarlo
    def contemporanea(dd):
        oo = preparar(dd, c, w, "GC3")
        p = oo["parts"]["test"]
        k = p.fechas_objetivo.dt.strftime("%Y-%m")
        return np.array([dd.serie(c)[m] for m in k])
    t = "2023-06"
    a, b = contemporanea(datos_perturbados(c, None)), contemporanea(datos_perturbados(c, t))
    out["entrada_contemporanea_detectada"] = bool(not np.array_equal(a, b))
    # train que incluye el test: objetivos hasta dic Y
    class VentanaMala(G.VentanaY1):
        @property
        def fin_train(self):
            return f"{self.anio}-12"

        @property
        def anio_fin_train(self):
            return self.anio

    om = preparar(d, c, VentanaMala(2023), "GC3")
    om["parts"]["train"] = om["parts"]["train"]
    tr = om["parts"]["train"].fechas_objetivo
    out["train_con_test_detectado"] = bool(tr.max() > pd.Timestamp(f"{w.fin_train}-01"))
    return out


def artefactos() -> tuple[list[str], int]:
    f, n = [], 0
    for ruta in glob.glob(str(G.UNI / "*" / "*" / "*" / "**" / "info.json"), recursive=True):
        ruta = Path(ruta)
        i = json.loads(ruta.read_text(encoding="utf-8"))
        m, y = i["modelo"], int(i["anio_test"])
        fam, _, prot, base = G.MODELOS[m]
        pred = pd.read_csv(ruta.parent / "predicciones.csv")
        te = pred[pred.particion == "test"]
        n += 1
        fin = f"{y - 1}-12" if prot == "Y1" else f"{y - 2}-12"
        if sorted(te.fecha) != [f"{y}-{k:02d}" for k in range(1, 13)]:
            f.append(f"(g) {ruta}: test no es {y}")
        prev = (pd.PeriodIndex(te.fecha, freq="M") - 1).astype(str)
        if fam == "chronos":
            if (te.contexto_fin.astype(str).values != prev.values).any():
                f.append(f"(g) {ruta}: contexto de Chronos no termina en t-1")
            continue
        if "x_fecha" in te and (te.x_fecha.astype(str).values != prev.values).any():
            f.append(f"(g) {ruta}: x_fecha != t-1")
        if fam == "sarima":
            if i["train_fin"] != fin:
                f.append(f"(g) {ruta}: SARIMA train_fin {i['train_fin']} != {fin}")
            continue
        if i.get("pesos_geograficos_fin") != fin or i["train_objetivos"][1] != fin:
            f.append(f"(g) {ruta}: pesos/train hasta {i.get('pesos_geograficos_fin')}/{i['train_objetivos'][1]} != {fin}")
        if "scaler_fechas_ajuste" in i and i["scaler_fechas_ajuste"][1] != fin:
            f.append(f"(g) {ruta}: scaler hasta {i['scaler_fechas_ajuste'][1]} != {fin}")
        if prot == "orig" and i.get("val_objetivos") != [f"{y - 1}-01", f"{y - 1}-12"]:
            f.append(f"(g) {ruta}: validacion {i.get('val_objetivos')}")
        if fam == "lstm" and prot == "Y1":
            e, _, _ = G.mejor_epoca_y_lr(base, i["cultivar"], y, int(i["semilla"]))
            h = pd.read_csv(ruta.parent / "history.csv")
            if int(i["epocas_fijas"]) != e or len(h) != e:
                f.append(f"(g) {ruta}: epocas {i['epocas_fijas']}/{len(h)} != mejor epoca base {e}")
        if "r_estadisticas_meses" in i and i["r_estadisticas_meses"][1] != fin:
            f.append(f"(g) {ruta}: residuo con meses hasta {i['r_estadisticas_meses'][1]}")
    return f, n


def main() -> None:
    Integridad().verificar()
    rep = {"ventanas": {}, "perturbacion_sarima": {}, "controles_negativos": {}}
    fallos = []
    for anio in G.VENTANAS_ENTRENADOS:
        for c in CULTIVARES:
            ff = []
            d = ConstructorDatosVentana()
            for prot, raices in (("Y1", ("tabular", "GC3", "LSTM-U", "GC3-R")), ("orig", ("LSTM-U", "GC3-R"))):
                w = G.ventana(anio, prot)
                for raiz in raices:
                    o = preparar(d, c, w, raiz)
                    ff += chequeos_fechas(o, d, c, w, prot, f"{raiz}/{prot}")
                    ff += perturbacion(c, w, raiz, [f"{anio}-01", f"{anio}-06", f"{anio}-12"])
            rep["ventanas"][f"{anio}/{c}"] = ff or "OK"
            fallos += ff
            ps = perturbacion_sarima(c, anio, f"{anio}-06")
            rep["perturbacion_sarima"][f"{anio}/{c}"] = ps or "OK"
            fallos += ps
    for c in CULTIVARES:
        rep["controles_negativos"][c] = controles_negativos(c)
    neg_ok = all(all(v.values()) for v in rep["controles_negativos"].values())
    fa, n = artefactos()
    rep["artefactos"] = {"unidades_revisadas": n, "fallos": fa or "OK"}
    fallos += fa
    rep["OK"] = not fallos and neg_ok
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(json.dumps(rep, indent=1, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"OK": rep["OK"], "n_fallos": len(fallos), "controles_negativos": rep["controles_negativos"],
                      "unidades_revisadas": n, "primeros_fallos": fallos[:10]}, indent=1, ensure_ascii=False))
    sys.exit(0 if rep["OK"] else 1)


if __name__ == "__main__":
    main()
