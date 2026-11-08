"""Modelos univariados: Naive, Seasonal Naive, SARIMA rolling con orden congelado y SARIMA-sel (D-BR10).

SARIMA replica auditorias/evaluar_test_sarima_rolling.py:107-155 con fechas de la ventana:
ajuste unico en train (2016-07..fin_train), append(refit=False) de la validacion como estado,
y en test forecast(steps=1) seguido de append del valor real. Los parametros nunca se reestiman.
Con con_validacion=True tambien se guarda el pronostico a 1 paso de cada mes de validacion; forecast()
no modifica el estado, asi que las predicciones de test son identicas a las de con_validacion=False.
"""
from __future__ import annotations

import itertools
import json
import warnings

import numpy as np
import pandas as pd

from lib.entorno import CONFIG
from lib.ventanas import Ventana

_HP = json.loads((CONFIG / "hiperparametros_congelados.json").read_text(encoding="utf-8"))


def naive(serie: pd.Series, ventana: Ventana) -> pd.DataFrame:
    s = serie.sort_index()
    filas = [{"fecha": m, "y_true": float(s[m]), "y_pred": float(s[s.index < m].iloc[-1])} for m in ventana.meses_test]
    return pd.DataFrame(filas)


def seasonal_naive(serie: pd.Series, ventana: Ventana) -> pd.DataFrame:
    s = serie.sort_index()
    filas = []
    for m in ventana.meses_test:
        t = pd.Timestamp(f"{m}-01") - pd.DateOffset(months=12)
        filas.append({"fecha": m, "y_true": float(s[m]), "y_pred": float(s[f"{t:%Y-%m}"])})
    return pd.DataFrame(filas)


def ingenuos_todas_particiones(serie: pd.Series, ventana: Ventana, rezago: int) -> pd.DataFrame:
    """Naive (rezago 1) o Seasonal Naive (rezago 12) en todos los meses con y_(t-rezago), hasta el test de la ventana.

    particion: train (<= dic Y-2), val (Y-1), test (Y). Los meses de train sirven de referencia para D-BR8;
    la Fase D recorta el train de cada modelo a sus propios meses objetivo.
    """
    s = serie.sort_index().astype(float)
    previo = s.shift(rezago)
    filas = []
    for m in s.index:
        if m > ventana.test[1] or np.isnan(previo[m]):
            continue
        anio = int(m[:4])
        parte = "test" if anio == ventana.anio else ("val" if anio == ventana.anio - 1 else "train")
        filas.append({"particion": parte, "fecha": m, "y_true": float(s[m]), "y_pred": float(previo[m])})
    return pd.DataFrame(filas)


def _particiones(serie: pd.Series, ventana: Ventana):
    s = serie.sort_index().astype(float)
    train = s[(s.index >= "2016-07") & (s.index <= ventana.fin_train)]
    val = s[(s.index >= ventana.val[0]) & (s.index <= ventana.val[1])]
    return s, train, val


def _ajustar(y: np.ndarray, order, seasonal_order, opciones: dict):
    from statsmodels.tsa.statespace.sarimax import SARIMAX

    op = dict(opciones)
    maxiter = op.pop("maxiter")
    with warnings.catch_warnings(record=True) as avisos:
        warnings.simplefilter("always")
        fit = SARIMAX(y, order=tuple(order), seasonal_order=tuple(seasonal_order), **op).fit(disp=False, maxiter=maxiter)
    return fit, sorted({str(a.category.__name__) for a in avisos})


def _convergio(fit) -> bool | None:
    return bool(fit.mle_retvals.get("converged", False)) if isinstance(fit.mle_retvals, dict) else None


def _a_un_paso(estado, fechas, valores) -> tuple[list[dict], object]:
    filas = []
    for m, y in zip(fechas, valores):
        filas.append({"fecha": m, "y_true": float(y), "y_pred": float(np.asarray(estado.forecast(steps=1), dtype=float)[0])})
        estado = estado.append([float(y)], refit=False)
    return filas, estado


def sarima_rolling(serie: pd.Series, ventana: Ventana, order, seasonal_order, opciones: dict | None = None,
                   con_validacion: bool = False, ajuste=None) -> tuple[pd.DataFrame, dict]:
    """ajuste: un resultado ya ajustado en train con estos ordenes (SARIMA-sel lo reutiliza); si es None se ajusta aqui."""
    op = dict(_HP["sarima_congelado"]["opciones"]) if opciones is None else dict(opciones)
    s, train, val = _particiones(serie, ventana)
    if ajuste is None:
        fit, avisos = _ajustar(train.to_numpy(), order, seasonal_order, op)
    else:
        fit, avisos = ajuste
    params0 = np.asarray(fit.params, dtype=float).copy()
    filas_val, actual = _a_un_paso(fit, list(val.index), val.to_numpy())
    filas_test, actual = _a_un_paso(actual, ventana.meses_test, [s[m] for m in ventana.meses_test])
    if con_validacion:
        pred = pd.DataFrame([{"particion": "val", **f} for f in filas_val] + [{"particion": "test", **f} for f in filas_test])
    else:
        pred = pd.DataFrame(filas_test)
    info = {"n_train": int(len(train)), "train_inicio": str(train.index.min()), "train_fin": str(train.index.max()),
            "convergio": _convergio(fit), "aic_train": float(fit.aic),
            "parametros_invariantes": bool(np.allclose(np.asarray(actual.params, dtype=float), params0, rtol=0, atol=1e-10)),
            "avisos": avisos}
    return pred, info


def rejilla_sarima_sel() -> list[tuple[tuple[int, int, int], tuple[int, int, int, int]]]:
    """576 ordenes en el orden de la rejilla (p, d, q, P, D, Q), que es el criterio de desempate por AIC."""
    g = _HP["sarima_seleccion_por_ventana_DA9"]["rejilla"]
    return [((p, d, q), (P, D, Q, g["m"])) for p, d, q, P, D, Q in itertools.product(g["p"], g["d"], g["q"], g["P"], g["D"], g["Q"])]


def sarima_sel(serie: pd.Series, ventana: Ventana) -> tuple[pd.DataFrame, dict, pd.DataFrame, pd.DataFrame]:
    """D-BR10. Devuelve (predicciones val+test del elegido, info, tabla de la rejilla, tabla de los 5 candidatos)."""
    hp = _HP["sarima_seleccion_por_ventana_DA9"]
    base = dict(hp["opciones_ajuste"])
    s, train, val = _particiones(serie, ventana)
    y = train.to_numpy()
    # Pasos 1-2: los 576 ordenes en train con maxiter 200; los que lanzan excepcion se descartan y se cuentan
    filas = []
    for i, (o, so) in enumerate(rejilla_sarima_sel()):
        fila = {"indice_rejilla": i, "order": str(o), "seasonal_order": str(so), "aic": np.nan, "convergio": None, "error": ""}
        try:
            fit, _ = _ajustar(y, o, so, {**base, "maxiter": hp["maxiter_rejilla"]})
            fila.update(aic=float(fit.aic), convergio=_convergio(fit))
        except Exception as exc:  # noqa: BLE001 - D-BR10 paso 2
            fila["error"] = f"{type(exc).__name__}: {exc}"[:300]
        filas.append(fila)
    rejilla = pd.DataFrame(filas)
    fallidos = int((rejilla["error"] != "").sum())
    validos = rejilla[(rejilla["error"] == "") & np.isfinite(rejilla["aic"])]
    aic_no_finito = int(((rejilla["error"] == "") & ~np.isfinite(rejilla["aic"])).sum())
    # Paso 3: top-5 por AIC (empate: orden de la rejilla)
    top = validos.sort_values(["aic", "indice_rejilla"], kind="mergesort").head(int(hp["n_candidatos_por_aic"]))
    # Paso 4: reajuste con maxiter 500 y MAE de validacion a 1 paso
    candidatos, ajustes = [], {}
    for pos, fila in enumerate(top.itertuples(), start=1):
        o, so = rejilla_sarima_sel()[fila.indice_rejilla]
        fit, avisos = _ajustar(y, o, so, {**base, "maxiter": hp["maxiter_candidatos_y_final"]})
        filas_val, _ = _a_un_paso(fit, list(val.index), val.to_numpy())
        mae_val = float(np.mean([abs(f["y_true"] - f["y_pred"]) for f in filas_val]))
        ajustes[pos] = (fit, avisos, o, so)
        candidatos.append({"posicion_aic": pos, "indice_rejilla": int(fila.indice_rejilla), "order": str(o), "seasonal_order": str(so),
                           "aic_rejilla_maxiter200": float(fila.aic), "aic_maxiter500": float(fit.aic), "MAE_val": mae_val,
                           "convergio_maxiter500": _convergio(fit)})
    cand = pd.DataFrame(candidatos)
    # Paso 5: menor MAE de validacion (empate: menor AIC, el de la rejilla, que es el que ordeno el top-5)
    elegido = cand.sort_values(["MAE_val", "aic_rejilla_maxiter200", "indice_rejilla"], kind="mergesort").iloc[0]
    fit, avisos, o, so = ajustes[int(elegido.posicion_aic)]
    # Paso 6: el mismo ajuste sigue con val como estado y test a 1 paso, igual que el SARIMA congelado
    pred, info = sarima_rolling(serie, ventana, o, so, con_validacion=True, ajuste=(fit, avisos))
    info.update({"order": list(o), "seasonal_order": list(so), "posicion_aic_elegido": int(elegido.posicion_aic),
                 "aic_elegido": float(elegido.aic_rejilla_maxiter200), "MAE_val_elegido": float(elegido.MAE_val),
                 "n_ordenes": len(rejilla), "n_fallidos": fallidos, "n_aic_no_finito": aic_no_finito,
                 "n_no_convergidos_rejilla": int((validos["convergio"] == False).sum())})  # noqa: E712
    return pred, info, rejilla, cand
