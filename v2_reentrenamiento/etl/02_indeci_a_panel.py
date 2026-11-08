"""ETL 02 — INDECI/SINPAD (registros crudos de emergencias) -> panel mensual provincia x mes 2016-2025.

Reconstrucción (revisión G7, observación 12) de data/interim/indeci_limpio_2016_2025.csv. El código original
no está en el repositorio; las reglas salen de DECISIONES_METODOLOGICAS.md ("Fuente INDECI — reemplazo por
dataset consolidado oficial") y se fijaron comparando con el CSV congelado. Ver README.md.

Fuente: data/raw/indeci/oficial_2016_2018/BD_2003-2025_EMERGENCIAS.csv (datosabiertos.gob.pe, consolidado
2003-2025; latin-1, separador ';'). Pese al nombre de la carpeta, el archivo cubre 2003-2025.

Reglas:
 1. Años 2016-2025 (columna AÑO) y mes por nombre (columna MES: ENERO..DICIEMBRE).
 2. Solo los 10 peligros climáticos: LLUVIA INTENSA, VIENTOS FUERTES, BAJAS TEMPERATURAS, INUNDACION,
    DESLIZAMIENTO, HUAYCO, SEQUIA, EROSION, TORMENTA ELECTRICA, MAREJADA.
 3. LIMA: departamentos LIMA METROPOLITANA y LIMA PROVINCIAS -> LIMA; provincia LIMA METROPOLITANA -> LIMA.
 4. Agregación por año, mes, departamento, provincia: num_emergencias = número de registros;
    personas_afectadas = suma AFECTADOS; personas_damnificadas = suma DAMNIFICADOS;
    total_afectados = afectadas + damnificadas; hectareas_cultivo_perdidas = suma HAS CULTIVO DESTRUIDO;
    hectareas_cultivo_afectadas = suma HAS CULTIVO AFECTADO (hectáreas redondeadas a 2 decimales).
 5. Universo: provincias de limon_sutil_provincia.csv (107). Rejilla completa 107 x 120 meses; un mes sin
    ningún registro climático en la provincia se codifica como 0 en todas las variables (no como faltante).
    CARHUAZ y YUNGAY (Ancash), solo de limón dulce, no están en el panel congelado.
 6. Orden: departamento, provincia, anio, mes.

Uso:
    python etl/02_indeci_a_panel.py [--crudo CSV] [--provincias CSV] [--salida CARPETA]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comun import INTERIM, RAW, carpeta_salida, comparar, escribir_csv, informe  # noqa: E402

PELIGROS_CLIMATICOS = ["LLUVIA INTENSA", "VIENTOS FUERTES", "BAJAS TEMPERATURAS", "INUNDACION", "DESLIZAMIENTO",
                       "HUAYCO", "SEQUIA", "EROSION", "TORMENTA ELECTRICA", "MAREJADA"]
MESES = {m: i + 1 for i, m in enumerate(["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO",
                                         "SETIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"])}
ANIO_INI, ANIO_FIN = 2016, 2025
VARS = {"AFECTADOS": "personas_afectadas", "DAMNIFICADOS": "personas_damnificadas",
        "HAS CULTIVO DESTRUIDO": "hectareas_cultivo_perdidas", "HAS CULTIVO AFECTADO": "hectareas_cultivo_afectadas"}
SALIDA = ["anio", "mes", "departamento", "provincia", "num_emergencias", "personas_afectadas", "personas_damnificadas",
          "total_afectados", "hectareas_cultivo_perdidas", "hectareas_cultivo_afectadas"]


def leer_crudo(ruta: Path) -> pd.DataFrame:
    r = pd.read_csv(ruta, sep=";", encoding="latin-1", dtype=str)
    r.columns = [c.strip() for c in r.columns]
    r = r.rename(columns={r.columns[2]: "ANIO"})  # 'AÑO' en latin-1
    for c in ("ANIO", "MES", "DPTO.", "PROV.", "PELIGRO"):
        r[c] = r[c].str.strip()
    return r


def panel(r: pd.DataFrame, universo: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    r = r.copy()
    r["anio"] = r.ANIO.astype(int)
    r["mes"] = r.MES.map(MESES)
    if r.mes.isna().any():
        raise ValueError(f"Meses no reconocidos: {sorted(r.loc[r.mes.isna(), 'MES'].unique())}")
    r = r[r.anio.between(ANIO_INI, ANIO_FIN) & r.PELIGRO.isin(PELIGROS_CLIMATICOS)].copy()
    r["departamento"] = r["DPTO."].replace({"LIMA METROPOLITANA": "LIMA", "LIMA PROVINCIAS": "LIMA"})
    r["provincia"] = r["PROV."].replace({"LIMA METROPOLITANA": "LIMA"})
    for c in VARS:
        r[c] = pd.to_numeric(r[c].str.replace(",", ".", regex=False), errors="coerce").fillna(0)
    g = r.groupby(["anio", "mes", "departamento", "provincia"]).agg(
        num_emergencias=("PELIGRO", "size"), **{v: (k, "sum") for k, v in VARS.items()}).reset_index()

    rejilla = (universo.assign(_k=1)
               .merge(pd.DataFrame([(a, m) for a in range(ANIO_INI, ANIO_FIN + 1) for m in range(1, 13)],
                                   columns=["anio", "mes"]).assign(_k=1), on="_k").drop(columns="_k"))
    p = rejilla.merge(g, on=["anio", "mes", "departamento", "provincia"], how="left")
    sin_registro = int(p.num_emergencias.isna().sum())
    p = p.fillna({c: 0 for c in ["num_emergencias", *VARS.values()]})  # mes sin registro -> 0
    for c in ["num_emergencias", "personas_afectadas", "personas_damnificadas"]:
        p[c] = p[c].astype(int)
    p["total_afectados"] = p.personas_afectadas + p.personas_damnificadas
    for c in ["hectareas_cultivo_perdidas", "hectareas_cultivo_afectadas"]:
        p[c] = p[c].astype(float).round(2)
    p = p.sort_values(["departamento", "provincia", "anio", "mes"]).reset_index(drop=True)[SALIDA]
    fuera = sorted(set(map(tuple, g[["departamento", "provincia"]].drop_duplicates().values))
                   - set(map(tuple, universo.values)))
    info = {"registros_climaticos_2016_2025": int(len(r)), "provincias_universo": len(universo),
            "celdas_panel": len(p), "celdas_sin_registro_codificadas_0": sin_registro,
            "provincias_con_registros_fuera_del_universo": len(fuera)}
    return p, info


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--crudo", default=str(RAW / "indeci" / "oficial_2016_2018" / "BD_2003-2025_EMERGENCIAS.csv"))
    ap.add_argument("--provincias", default=str(INTERIM / "limon_sutil_provincia.csv"),
                    help="CSV con columnas departamento, provincia que define el universo (solo lectura)")
    ap.add_argument("--salida", default=None)
    a = ap.parse_args()
    sal = carpeta_salida(a.salida)
    crudo = Path(a.crudo)
    if not crudo.exists():
        raise SystemExit(f"Falta el archivo crudo de INDECI: {crudo}")
    universo = (pd.read_csv(a.provincias, usecols=["departamento", "provincia"])
                .drop_duplicates().sort_values(["departamento", "provincia"]).reset_index(drop=True))
    p, info = panel(leer_crudo(crudo), universo)
    print(info)
    f = escribir_csv(p, sal / "indeci_limpio_2016_2025.csv")
    informe([comparar(f, INTERIM / f.name, f"v2_reentrenamiento/data/interim/{f.name}") | {"info": info}],
            sal / "comparacion_02_indeci.json")


if __name__ == "__main__":
    main()
