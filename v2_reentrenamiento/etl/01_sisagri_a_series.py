"""ETL 01 — SISAGRI (Excel MIDAGRI) -> distrito_crudo -> distrito_dedup -> provincia -> nacional mensual, por cultivo.

Reconstrucción (revisión G7, observación 12) de la cadena que generó los CSV congelados de data/interim/.
El código original no existe en el repositorio ni en su historial (D21); las reglas salen de
DECISIONES_METODOLOGICAS.md ("Deduplicación Ayacucho", "Agregación distrito->provincia") y se fijaron
comparando con los CSV congelados. Ver README.md.

Uso:
    python etl/01_sisagri_a_series.py [--excel RUTA] [--salida CARPETA] [--cache-limon CSV]

Escribe en --salida (por defecto <TEMP>/etl_v2_salida; nunca en data/interim) y compara con los congelados.
"""
from __future__ import annotations

import argparse
import csv
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comun import INTERIM, RAW, carpeta_salida, comparar, escribir_csv, informe  # noqa: E402

COLUMNAS = ["AÑO", "MES", "COD_UBIGEO", "DEPARTAMENTO", "PROVINCIA", "DISTRITO", "COD_PRODUCTO", "PRODUCTO",
            "SIEMBRA", "COSECHA", "PRODUCCION", "VERDE_ACTUAL", "PRECIO_CHACRA"]
NUM = ["SIEMBRA", "COSECHA", "PRODUCCION", "VERDE_ACTUAL", "PRECIO_CHACRA"]
CLAVE = ["AÑO", "MES", "COD_UBIGEO", "COD_PRODUCTO"]
CULTIVOS = {"sutil": "LIMON SUTIL", "dulce": "LIMON DULCE"}  # COD_PRODUCTO 13010170102 y 13010480000
ANIO_INI, ANIO_FIN = 2016, 2025


# ---------------------------------------------------------------- 1. Excel -> filas de limón
def leer_excel_limon(excel: Path) -> pd.DataFrame:
    """Lee todas las hojas del Excel (5 hojas: 2015-2018, 2018-2020, 2020-2023, 2023-2025, 2025-2026).

    El Excel declara dimensiones falsas (A1:A1) en 4 de las 5 hojas: sin reset_dimensions() openpyxl
    en modo read_only solo ve 1 fila. Se guardan solo filas de LIMON SUTIL y LIMON DULCE.
    """
    import openpyxl

    warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")
    wb = openpyxl.load_workbook(excel, read_only=True)
    filas = []
    for ws in wb.worksheets:
        ws.reset_dimensions()
        for row in ws.iter_rows(values_only=True):
            if not row or len(row) < 13 or row[7] not in CULTIVOS.values():
                continue
            filas.append([("" if v is None else v) for v in row[:13]])
    wb.close()
    return pd.DataFrame(filas, columns=COLUMNAS)


def guardar_cache(df: pd.DataFrame, ruta: Path) -> None:
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(COLUMNAS)
        w.writerows(df.itertuples(index=False))


def leer_cache(ruta: Path) -> pd.DataFrame:
    return pd.read_csv(ruta, dtype=str, keep_default_na=False)


# ---------------------------------------------------------------- 2. distrito_crudo
def distrito_crudo(limon: pd.DataFrame, producto: str) -> pd.DataFrame:
    """Filtra el cultivo y 2016-2025; orden estable por AÑO, MES, COD_UBIGEO (orden de hojas dentro de la clave).

    Las celdas vacías del Excel quedan vacías (NaN); los numéricos se escriben como float de Python (p. ej. 17.0).
    """
    d = limon[limon.PRODUCTO.astype(str) == producto].copy()
    for c in ["AÑO", "MES", "COD_UBIGEO", "COD_PRODUCTO"]:
        d[c] = d[c].astype(str)
    d = d[d["AÑO"].astype(int).between(ANIO_INI, ANIO_FIN)]
    for c in NUM:
        d[c] = pd.to_numeric(d[c].replace("", np.nan), errors="raise").astype(float)
    return d.sort_values(["AÑO", "MES", "COD_UBIGEO"], kind="stable").reset_index(drop=True)[COLUMNAS]


# ---------------------------------------------------------------- 3. distrito_dedup
def distrito_dedup(crudo: pd.DataFrame) -> pd.DataFrame:
    """Claves AÑO+MES+COD_UBIGEO+COD_PRODUCTO duplicadas (solo Ayacucho, sutil) -> MEDIA de cada numérico.

    Regla de DECISIONES_METODOLOGICAS.md ("Deduplicación Ayacucho"). Metadatos de la primera fila; la fila
    agregada ocupa la posición de la primera aparición de la clave. Formato de las filas agregadas, fijado
    al comparar con el congelado: valores con 2 decimales (f"{x:.2f}", redondeo de Python), salvo SIEMBRA y
    COSECHA cuando todo el grupo es 0, que se escriben "0.0". Las claves no duplicadas no cambian.
    """
    meta = [c for c in COLUMNAS if c not in NUM]
    g = crudo.groupby(CLAVE, sort=False, dropna=False)
    out = pd.concat([g[meta].first().drop(columns=CLAVE), g[NUM].mean()], axis=1).reset_index()[COLUMNAS]
    n = g.size().reset_index(drop=True)
    dup = (n > 1).to_numpy()
    out = out.astype({c: object for c in NUM})
    for c in NUM:
        fmt = out.loc[dup, c].map(lambda x: "" if pd.isna(x) else f"{x:.2f}")
        if c in ("SIEMBRA", "COSECHA"):
            fmt = fmt.where(out.loc[dup, c].astype(float) != 0, "0.0")
        out.loc[dup, c] = fmt
    return out


# ---------------------------------------------------------------- 4. provincia
def provincia(dedup_csv: Path) -> pd.DataFrame:
    """Distrito -> provincia (se lee el CSV dedup tal como se escribió, con sus redondeos).

    produccion_t y verde_actual_ha: SUMA. precio_chacra_kg: media ponderada por producción
    (DECISIONES: "PRECIO_CHACRA — media ponderada por producción"); si la producción provincial es 0,
    precio = 0 y precio_es_fallback = 1. PRODUCCION/PRECIO vacíos cuentan como 0 en la ponderación.
    Formato: 3 decimales (producción, superficie) y 6 (precio).
    """
    d = pd.read_csv(dedup_csv, dtype={"MES": str, "COD_UBIGEO": str, "COD_PRODUCTO": str})
    filas = []
    for (a, m, dep, prov), g in d.groupby(["AÑO", "MES", "DEPARTAMENTO", "PROVINCIA"], sort=True):
        q = g.PRODUCCION.fillna(0).to_numpy()
        p = g.PRECIO_CHACRA.fillna(0).to_numpy()
        tot = q.sum()
        precio = float((p * q).sum() / tot) if tot > 0 else 0.0
        filas.append((a, m, dep, prov, tot, g.VERDE_ACTUAL.sum(), precio, int(not tot > 0)))
    out = pd.DataFrame(filas, columns=["año", "mes", "departamento", "provincia", "produccion_t", "verde_actual_ha",
                                       "precio_chacra_kg", "precio_es_fallback"])
    out["produccion_t"] = out.produccion_t.map("{:.3f}".format)
    out["verde_actual_ha"] = out.verde_actual_ha.map("{:.3f}".format)
    out["precio_chacra_kg"] = out.precio_chacra_kg.map("{:.6f}".format)
    return out


# ---------------------------------------------------------------- 5. nacional mensual
def nacional(provincia_csv: Path) -> pd.DataFrame:
    """Provincia -> nacional (se lee el CSV provincial ya redondeado).

    produccion_t_nacional: SUMA; precio_chacra_kg_nacional: media ponderada por produccion_t;
    n_provincias_reportando: provincias con produccion_t > 0 en el mes.
    """
    p = pd.read_csv(provincia_csv, dtype={"mes": str})
    p["pp"] = p.precio_chacra_kg * p.produccion_t
    n = p.groupby(["año", "mes"], sort=True).agg(
        produccion_t_nacional=("produccion_t", "sum"), pp=("pp", "sum"),
        n_provincias_reportando=("produccion_t", lambda s: int((s > 0).sum()))).reset_index()
    n["precio_chacra_kg_nacional"] = n.pp / n.produccion_t_nacional
    n = n[["año", "mes", "produccion_t_nacional", "precio_chacra_kg_nacional", "n_provincias_reportando"]]
    n["produccion_t_nacional"] = n.produccion_t_nacional.map("{:.3f}".format)
    n["precio_chacra_kg_nacional"] = n.precio_chacra_kg_nacional.map("{:.6f}".format)
    return n


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--excel", default=str(RAW / "midagri" / "sisagri_2015_2026.xlsx"))
    ap.add_argument("--salida", default=None, help="carpeta de salida (por defecto <TEMP>/etl_v2_salida)")
    ap.add_argument("--cache-limon", default=None,
                    help="CSV intermedio con las filas de limón del Excel; si existe se usa en lugar de leer el Excel (~9 min)")
    a = ap.parse_args()
    sal = carpeta_salida(a.salida)

    cache = Path(a.cache_limon) if a.cache_limon else sal / "_sisagri_limon_filas.csv"
    if cache.exists():
        print(f"Leyendo filas de limón de la caché {cache}")
        limon = leer_cache(cache)
    else:
        excel = Path(a.excel)
        if not excel.exists():
            raise SystemExit(f"Falta el Excel crudo de MIDAGRI-SISAGRI: {excel}")
        print(f"Leyendo {excel} (todas las hojas)...")
        limon = leer_excel_limon(excel)
        guardar_cache(limon, cache)
        limon = leer_cache(cache)
    print(f"Filas de limón leídas: {len(limon)} ({limon.PRODUCTO.value_counts().to_dict()})")

    res = []
    for c, producto in CULTIVOS.items():
        f_crudo = escribir_csv(distrito_crudo(limon, producto), sal / f"limon_{c}_distrito_crudo.csv")
        crudo = pd.read_csv(f_crudo, dtype={"MES": str, "COD_UBIGEO": str, "COD_PRODUCTO": str})
        dd = distrito_dedup(crudo)
        print(f"{c}: crudo {len(crudo)} filas; claves duplicadas {int(crudo.duplicated(CLAVE).sum())} "
              f"en {sorted(crudo[crudo.duplicated(CLAVE, keep=False)].DEPARTAMENTO.unique())}; dedup {len(dd)} filas")
        f_dedup = escribir_csv(dd, sal / f"limon_{c}_distrito_dedup.csv")
        f_prov = escribir_csv(provincia(f_dedup), sal / f"limon_{c}_provincia.csv")
        f_nac = escribir_csv(nacional(f_prov), sal / f"limon_{c}_nacional_mensual.csv")
        for f in (f_crudo, f_dedup, f_prov, f_nac):
            res.append(comparar(f, INTERIM / f.name, f"v2_reentrenamiento/data/interim/{f.name}"))
    informe(res, sal / "comparacion_01_sisagri.json")


if __name__ == "__main__":
    main()
