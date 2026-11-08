"""Prueba automatica de ausencia de fuga (plan A2, puntos a-f) en todas las ventanas y cultivares.

Incluye controles negativos: se introduce una fuga a proposito y la prueba debe detectarla.
Escribe 10_logs/verificaciones/fuga.json; sale con codigo 1 si algo falla.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lib.entorno import BR, CONFIG, preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import json  # noqa: E402
from dataclasses import asdict  # noqa: E402

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from lib.datos import CULTIVARES, ConstructorDatosVentana  # noqa: E402
from lib.integridad import Integridad  # noqa: E402
from lib.preparacion import EscaladorVentana, pares_tabulares, secuencias  # noqa: E402
from lib.shocks import cambios, mascara  # noqa: E402
from lib.ventanas import todas  # noqa: E402
from v2_reentrenamiento.src.models.features_gc2_xgboost import build_gc2_feature_spec  # noqa: E402
from v2_reentrenamiento.src.models.features_gc3_ge import build_feature_spec  # noqa: E402
from v2_reentrenamiento.src.training.config_gc2_xgboost import OFFICIAL_GC2_XGB_CONFIG  # noqa: E402
from v2_reentrenamiento.src.training.config_gc3_ge import OFFICIAL_TRAINING_CONFIG  # noqa: E402

SALIDA = BR / "10_logs" / "verificaciones" / "fuga.json"
MES = pd.DateOffset(months=1)


def chequear_escalador(esc: EscaladorVentana, feats: pd.DataFrame, ventana) -> list[str]:
    fallos = []
    if esc.fechas_ajuste[1] > ventana.fin_train:
        fallos.append(f"(a) scaler ajustado hasta {esc.fechas_ajuste[1]} > fin_train {ventana.fin_train}")
    k = feats["año"].astype(str) + "-" + feats["mes"].astype(str).str.zfill(2)
    train = feats[(k >= "2016-07") & (k <= ventana.fin_train)]
    if int(esc.scaler.n_samples_seen_) != len(train):
        fallos.append(f"(a) n_samples_seen {esc.scaler.n_samples_seen_} != filas de train {len(train)}")
    if not np.allclose(esc.scaler.mean_, train[esc.columnas].mean().to_numpy(), rtol=0, atol=1e-9):
        fallos.append("(a) media del scaler distinta de la media del train")
    return fallos


def chequear_particiones(parts: dict, ventana, nombre: str) -> list[str]:
    fallos = []
    tr, va, te = (parts[s].fechas_objetivo for s in ("train", "val", "test"))
    if len(tr) and tr.max() > pd.Timestamp(f"{ventana.fin_train}-01"):
        fallos.append(f"(c) {nombre}: objetivo de train {tr.max():%Y-%m} > fin_train")
    if len(va) != 12 or va.dt.year.ne(ventana.anio - 1).any():
        fallos.append(f"(c) {nombre}: validacion no es el ano {ventana.anio - 1}")
    if len(te) != 12 or te.dt.year.ne(ventana.anio).any():
        fallos.append(f"(c) {nombre}: test no es el ano {ventana.anio}")
    if set(va) & set(te) or set(tr) & set(te) or set(tr) & set(va):
        fallos.append(f"(c) {nombre}: particiones solapadas")
    # (e) un paso adelante: la ultima fecha de entrada es exactamente t-1
    for s in ("train", "val", "test"):
        p = parts[s]
        if len(p.y) and not (p.fechas_contexto_max + MES == p.fechas_objetivo).all():
            fallos.append(f"(e) {nombre}/{s}: la ultima entrada no es t-1")
    return fallos


def chequear_lags_reales(parts: dict, esc: EscaladorVentana, serie: pd.Series, objetivo: str, nombre: str, idx_prod: int, es_secuencia: bool) -> list[str]:
    """(e) La produccion de entrada en test (fila t-1) desescalada es la produccion real observada en t-1."""
    p = parts["test"]
    escalados = p.X_a[:, -1, idx_prod] if es_secuencia else p.X[:, idx_prod]
    reales = esc.invertir(objetivo, escalados)
    esperados = serie.reindex(p.fechas_contexto_max.dt.strftime("%Y-%m")).to_numpy(dtype=float)
    if not np.allclose(reales, esperados, rtol=0, atol=1e-6):
        return [f"(e) {nombre}: la entrada de produccion en test no coincide con la serie real en t-1"]
    return []


def chequear_umbral(serie: pd.Series, ventana) -> list[str]:
    fallos = []
    for tipo in ("mensual", "interanual"):
        mk = mascara(serie, ventana, tipo, 75)
        if mk.historia_fin != ventana.origen:
            fallos.append(f"(b) {tipo}: historia del umbral termina en {mk.historia_fin} != origen")
        r = cambios(serie, tipo)
        esperado = float(np.percentile(r[r.index <= ventana.origen], 75, method="linear"))
        if mk.umbral != esperado:
            fallos.append(f"(b) {tipo}: umbral no reproducible solo con historia hasta el origen")
    return fallos


def chequear_hiperparametros() -> list[str]:
    hp = json.loads((CONFIG / "hiperparametros_congelados.json").read_text(encoding="utf-8"))
    tc, g = asdict(OFFICIAL_TRAINING_CONFIG), hp["gc3_ge"]
    fallos = [f"(d) GC3/GE {k}: {tc[k2]} != {g[k]}" for k, k2 in
              (("lookback", "lookback"), ("batch_size", "batch_size"), ("max_epochs", "max_epochs"), ("learning_rate", "learning_rate"),
               ("shuffle", "shuffle"), ("early_stopping_patience", "early_stopping_patience"), ("reduce_lr_patience", "reduce_lr_patience"))
              if tc[k2] != g[k]]
    xc, x = asdict(OFFICIAL_GC2_XGB_CONFIG), hp["xgb37"]
    fallos += [f"(d) XGB {k}: {xc[k]} != {x[k]}" for k in x if k != "fuente" and xc.get(k) != x[k]]
    return fallos


def control_negativo(datos, serie, ventana, c) -> dict:
    """Introduce fugas a proposito; la prueba debe detectarlas (si no, la prueba es inutil)."""
    feats = datos.features(c, ventana.anio_fin_train)
    esc_malo = EscaladorVentana(ventana)
    esc_malo.ventana = type(ventana)(ventana.anio + 1) if ventana.anio < 2025 else ventana  # scaler ajustado un ano de mas
    esc_malo.ajustar_transformar(feats)
    detecta_scaler = bool(chequear_escalador(esc_malo, feats, ventana)) if ventana.anio < 2025 else None
    # Umbral con fuga: historia que llega al final del test. Se detecta por fecha (la comparacion por
    # valor sola no basta: el P75 puede coincidir numericamente, p. ej. Dulce 2021 = 2022 = 2023).
    r = cambios(serie, "mensual")
    hist_malo = r[r.index <= ventana.test[1]]
    umbral_con_test = float(np.percentile(hist_malo, 75, method="linear"))
    detecta_por_fecha = str(hist_malo.index.max()) != ventana.origen
    coincide_valor = umbral_con_test == mascara(serie, ventana, "mensual", 75).umbral
    return {"scaler_con_un_ano_extra_detectado": detecta_scaler, "umbral_con_test_detectado": bool(detecta_por_fecha),
            "info_umbral_con_test_coincide_en_valor": bool(coincide_valor)}


def main() -> None:
    Integridad().verificar()
    datos = ConstructorDatosVentana()
    rep = {"ventanas": {}, "hiperparametros": chequear_hiperparametros(), "controles_negativos": {}}
    fallos_totales = list(rep["hiperparametros"])
    for v in todas():
        for c in CULTIVARES:
            serie = datos.serie(c)
            feats = datos.features(c, v.anio_fin_train)
            fallos = []
            pw = datos.pesos(c, v.anio_fin_train).tabla
            if (pw["periodo_fin"] != v.fin_train).any():
                fallos.append(f"(f) pesos con periodo_fin distinto de {v.fin_train}")
            esc = EscaladorVentana(v)
            escalado = esc.ajustar_transformar(feats)
            fallos += chequear_escalador(esc, feats, v)
            fallos += chequear_umbral(serie, v)
            for modelo in ("GC3", "GE"):
                spec = build_feature_spec(c, modelo)
                parts = secuencias(escalado, spec.rama_a, spec.rama_b, spec.target, v)
                fallos += chequear_particiones(parts, v, modelo)
                fallos += chequear_lags_reales(parts, esc, serie, spec.target, modelo, list(spec.rama_a).index(spec.target), True)
            spec = build_gc2_feature_spec(c)
            parts = pares_tabulares(escalado, spec.predictors, spec.target, v)
            fallos += chequear_particiones(parts, v, "tabular")
            fallos += chequear_lags_reales(parts, esc, serie, spec.target, "tabular", list(spec.predictors).index(spec.target), False)
            rep["ventanas"][f"{v.anio}/{c}"] = fallos or "OK"
            fallos_totales += fallos
            if v.anio in (2021, 2023):
                rep["controles_negativos"][f"{v.anio}/{c}"] = control_negativo(datos, serie, v, c)
    negativos_ok = all(all(x in (True, None) for k, x in d.items() if not k.startswith("info_"))
                       for d in rep["controles_negativos"].values())
    rep["OK"] = not fallos_totales and negativos_ok
    rep["n_ventana_cultivar"] = len(rep["ventanas"])
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(json.dumps(rep, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(rep, indent=1, ensure_ascii=False))
    sys.exit(0 if rep["OK"] else 1)


if __name__ == "__main__":
    main()
