"""Prueba: con Y=2025 el envoltorio reproduce exactamente los artefactos oficiales v2.

Compara pesos, maestro, features, scaler v2c, dataset escalado, secuencias GC3/GE (build_sequences oficial)
y pares tabulares XGB (build_gc2_tabular_bundle oficial). Escribe 10_logs/verificaciones/equivalencia_2025.json.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lib.entorno import BR, preparar_entorno, semillas_globales  # noqa: E402

preparar_entorno()
semillas_globales(42)

import json  # noqa: E402

import joblib  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from lib.datos import ConstructorDatosVentana, ida_y_vuelta_csv, ruta  # noqa: E402
from lib.preparacion import EscaladorVentana, pares_tabulares, secuencias  # noqa: E402
from lib.ventanas import Ventana  # noqa: E402
from v2_reentrenamiento.src.models.features_gc2_xgboost import build_gc2_feature_spec  # noqa: E402
from v2_reentrenamiento.src.models.features_gc3_ge import build_feature_spec  # noqa: E402
from v2_reentrenamiento.src.training.sequences_gc3_ge import build_sequences, load_feature_dataframe  # noqa: E402
from v2_reentrenamiento.src.training.tabular_gc2_xgboost import build_gc2_tabular_bundle, load_train_val_dataframe  # noqa: E402

SALIDA = BR / "10_logs" / "verificaciones" / "equivalencia_2025.json"


def max_dif(a: pd.DataFrame, b: pd.DataFrame) -> dict:
    cols_a, cols_b = list(a.columns), list(b.columns)
    if cols_a != cols_b:
        return {"columnas_iguales": False, "solo_nuevo": sorted(set(cols_a) - set(cols_b)), "solo_oficial": sorted(set(cols_b) - set(cols_a))}
    if len(a) != len(b):
        return {"columnas_iguales": True, "filas_iguales": False, "filas": [len(a), len(b)]}
    d = np.abs(a.to_numpy(dtype=float) - b.to_numpy(dtype=float))
    return {"columnas_iguales": True, "filas_iguales": True, "max_abs_dif": float(d.max()), "identico_bit_a_bit": bool((d == 0).all())}


def main() -> None:
    v = Ventana(2025)
    datos = ConstructorDatosVentana()
    rep: dict = {"ventana": v.como_dict(), "cultivares": {}}
    ok = True
    pesos_of = pd.read_csv(ruta("pesos", oficial=True), encoding="utf-8-sig")
    for c in ("sutil", "dulce"):
        r: dict = {}
        # 1. pesos
        # La cadena oficial usa los pesos leidos del CSV (02_fusion celda 6): se compara esa representacion.
        t_mem = datos.pesos(c, v.anio_fin_train).tabla
        t = ida_y_vuelta_csv(t_mem)
        of = pesos_of[pesos_of["cultivar"] == c].reset_index(drop=True)
        m = t.merge(of, on=["departamento", "provincia"], suffixes=("", "_of"))
        m_mem = t_mem.merge(of, on=["departamento", "provincia"], suffixes=("", "_of"))
        r["pesos"] = {"n_nuevo": len(t), "n_oficial": len(of), "n_emparejadas": len(m),
                      "max_abs_dif": float((m["peso"] - m["peso_of"]).abs().max()),
                      "max_abs_dif_en_memoria_antes_de_csv": float((m_mem["peso"] - m_mem["peso_of"]).abs().max()),
                      "identico_bit_a_bit": bool(len(m) == len(of) == len(t) and (m["peso"] == m["peso_of"]).all())}
        # 2. maestro y 3. features
        r["maestro"] = max_dif(datos.maestro(c, v.anio_fin_train), pd.read_csv(ruta("maestro", c, oficial=True), encoding="utf-8-sig"))
        feats = datos.features(c, v.anio_fin_train)
        r["features"] = max_dif(feats, pd.read_csv(ruta("features", c, oficial=True), encoding="utf-8-sig"))
        # 4. scaler y escalado
        esc = EscaladorVentana(v)
        escalado = esc.ajustar_transformar(feats)
        sc_of = joblib.load(ruta("scaler_v2c", c, oficial=True))
        r["scaler_v2c"] = {
            "columnas_iguales": list(esc.scaler.feature_names_in_) == list(sc_of.feature_names_in_),
            "n_samples_seen": [int(esc.scaler.n_samples_seen_), int(sc_of.n_samples_seen_)],
            "fechas_ajuste": esc.fechas_ajuste,
            "max_abs_dif_mean": float(np.abs(esc.scaler.mean_ - sc_of.mean_).max()),
            "max_abs_dif_scale": float(np.abs(esc.scaler.scale_ - sc_of.scale_).max()),
            "identico_bit_a_bit": bool(np.array_equal(esc.scaler.mean_, sc_of.mean_) and np.array_equal(esc.scaler.scale_, sc_of.scale_)),
        }
        r["escalado"] = max_dif(escalado, pd.read_csv(ruta("escalado", c, oficial=True), encoding="utf-8-sig"))
        # 5. secuencias
        oficial_df = load_feature_dataframe(ruta("escalado", c, oficial=True))
        for modelo in ("GC3", "GE"):
            spec = build_feature_spec(c, modelo)
            ob = build_sequences(oficial_df, spec)
            nb = secuencias(escalado, spec.rama_a, spec.rama_b, spec.target, v)
            res = {}
            for nombre, of_split in (("train", ob.train), ("val", ob.validation), ("test", ob.test)):
                n = nb[nombre]
                res[nombre] = {"n": [len(n.y), len(of_split.y)],
                               "X_a_identico": bool(np.array_equal(n.X_a, of_split.X_a)),
                               "X_b_identico": bool(np.array_equal(n.X_b, of_split.X_b)),
                               "y_identico": bool(np.array_equal(n.y, of_split.y)),
                               "fechas_identicas": bool(n.fechas_objetivo.equals(of_split.target_dates.reset_index(drop=True).rename("fecha")))}
            r[f"secuencias_{modelo}"] = res
        # 6. pares tabulares XGB-37
        spec = build_gc2_feature_spec(c)
        ob = build_gc2_tabular_bundle(load_train_val_dataframe(ruta("escalado", c, oficial=True)), spec)
        nb = pares_tabulares(escalado, spec.predictors, spec.target, v)
        r["tabular_XGB37"] = {nombre: {"n": [len(nb[nombre].y), len(of_split.y)],
                                       "X_identico": bool(np.array_equal(nb[nombre].X, of_split.X)),
                                       "y_identico": bool(np.array_equal(nb[nombre].y, of_split.y))}
                              for nombre, of_split in (("train", ob.train), ("val", ob.validation))}
        rep["cultivares"][c] = r

        def todo_identico(x) -> bool:
            if isinstance(x, dict):
                return all(todo_identico(val) for key, val in x.items() if key not in ("n", "n_nuevo", "n_oficial", "n_emparejadas",
                           "n_samples_seen", "fechas_ajuste", "max_abs_dif", "max_abs_dif_en_memoria_antes_de_csv", "max_abs_dif_mean", "max_abs_dif_scale", "filas", "solo_nuevo", "solo_oficial"))
            return bool(x) if isinstance(x, bool) else True
        r["OK"] = todo_identico(r) and r["scaler_v2c"]["n_samples_seen"] == [90, 90]
        ok &= r["OK"]
    rep["OK"] = ok
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(json.dumps(rep, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    print(json.dumps(rep, indent=1, ensure_ascii=False, default=str))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
