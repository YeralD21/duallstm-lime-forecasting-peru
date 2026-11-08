"""ETL 03 — Coordenadas de las 109 provincias (data/interim/coordenadas_provincias_completo.csv).

Reconstrucción (revisión G7, observación 12). Origen de cada coordenada, verificado en el repositorio:

* provincia_exacta (99): lat/lon de la provincia en el dataset climático de v1
  data/interim/nasa/clima_dataset_final.csv (columnas departamento, provincia, lat, lon; 102 provincias),
  copiadas como texto. El origen primario de esas coordenadas en v1 NO está documentado ni hay código que
  las genere (valores con aspecto de conversión manual desde grados-minutos-segundos, p. ej. -5.63888888888889).
* departamento_fallback (10): provincias que no están en el dataset de v1. Se les asigna la coordenada del
  diccionario COORDS_DEPTO de v1 (notebooks/fase2/_build_act02_time.py, commit 7dbd515), que el código
  llama "centroide aproximado" pero que son las coordenadas de la CAPITAL del departamento (Lima ciudad,
  Iquitos, Huaraz, Trujillo...). DECISIONES_METODOLOGICAS.md dice "centroide del departamento": impreciso.

Universo: unión de provincias de limon_sutil_provincia.csv y limon_dulce_provincia.csv (107 + 28 -> 109),
ordenado por departamento, provincia.

Validación (--validar, por defecto activada) contra una fuente documentada: geoBoundaries gbOpen PER ADM2
(límites provinciales; fuente IGN Perú vía OCHA ROLAC/HDX; licencia CC BY 3.0 IGO; boundaryID
PER-ADM2-86281439; 196 provincias), versión fijada en el commit 90a1d52 del repositorio wmgeolab/geoBoundaries
(el mismo commit del ADM1 de 11_geometria_externa). Prueba punto-en-polígono: la coordenada de cada provincia
debe caer dentro del polígono de esa provincia. Para las 10 de fallback se informa en qué provincia cae
(se espera la provincia capital del departamento). El GeoJSON se descarga a la carpeta de salida si no se da
--adm2, y se verifica su SHA-256.

Uso:
    python etl/03_coordenadas.py [--salida CARPETA] [--adm2 GEOJSON] [--sin-validar]
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import re
import sys
import unicodedata
import urllib.request
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comun import INTERIM, RAIZ, carpeta_salida, comparar, escribir_csv, informe  # noqa: E402

V1_CLIMA = RAIZ / "data" / "interim" / "nasa" / "clima_dataset_final.csv"
V1_DICT = RAIZ / "notebooks" / "fase2" / "_build_act02_time.py"
ADM2_URL = ("https://github.com/wmgeolab/geoBoundaries/raw/90a1d52/releaseData/gbOpen/PER/ADM2/"
            "geoBoundaries-PER-ADM2_simplified.geojson")
ADM2_SHA256 = "4986d514b9898f7c415febd47d2ae302f79f5a0d23434cc81fb2bdbfaec623a3"


def coords_depto_v1() -> dict[str, tuple[float, float]]:
    """Lee el diccionario COORDS_DEPTO del archivo de v1 sin ejecutarlo (ast.literal_eval)."""
    txt = V1_DICT.read_text(encoding="utf-8")
    m = re.search(r"COORDS_DEPTO = (\{.*?\n\})", txt, flags=re.S)
    if not m:
        raise SystemExit(f"No se encontró COORDS_DEPTO en {V1_DICT}")
    return ast.literal_eval(m.group(1))


def universo() -> pd.DataFrame:
    u = pd.concat([pd.read_csv(INTERIM / f"limon_{c}_provincia.csv", usecols=["departamento", "provincia"])
                   for c in ("sutil", "dulce")]).drop_duplicates()
    return u.sort_values(["departamento", "provincia"]).reset_index(drop=True)


def construir() -> pd.DataFrame:
    v1 = pd.read_csv(V1_CLIMA, dtype=str, usecols=["departamento", "provincia", "lat", "lon"]).drop_duplicates()
    if v1.duplicated(["departamento", "provincia"]).any():
        raise SystemExit("clima_dataset_final.csv tiene provincias con más de una coordenada")
    dep = coords_depto_v1()
    t = universo().merge(v1, on=["departamento", "provincia"], how="left")
    exacta = t.lat.notna()
    t["fuente"] = exacta.map({True: "provincia_exacta", False: "departamento_fallback"})
    for i in t.index[~exacta]:
        la, lo = dep[t.at[i, "departamento"]]
        t.at[i, "lat"], t.at[i, "lon"] = repr(float(la)), repr(float(lo))
    return t[["departamento", "provincia", "lat", "lon", "fuente"]]


def norm(s: str) -> str:
    """Mayúsculas sin tildes, conservando la Ñ; repara nombres con mojibake UTF-8/latin-1 del GeoJSON."""
    try:
        s = s.encode("latin-1").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        pass
    s = unicodedata.normalize("NFC", s).upper().replace("Ñ", "\0")
    s = "".join(ch for ch in unicodedata.normalize("NFD", s) if unicodedata.category(ch) != "Mn")
    return s.replace("\0", "Ñ").strip()


def validar(t: pd.DataFrame, adm2: Path) -> pd.DataFrame:
    import geopandas as gpd

    a = gpd.read_file(adm2)
    a["prov_geo"] = a.shapeName.map(norm)
    if a.prov_geo.duplicated().any():
        raise SystemExit("Nombres de provincia repetidos en ADM2: el emparejamiento por nombre no es único")
    pts = gpd.GeoDataFrame(t.copy(), geometry=gpd.points_from_xy(t.lon.astype(float), t.lat.astype(float)), crs="EPSG:4326")
    j = gpd.sjoin(pts, a[["prov_geo", "geometry"]], how="left", predicate="within")
    j = j[~j.index.duplicated()]
    v = t.copy()
    v["provincia_norm"] = v.provincia.map(norm)
    v["en_adm2"] = v.provincia_norm.isin(set(a.prov_geo))
    v["provincia_que_contiene_el_punto"] = j.prov_geo.reindex(v.index)
    v["dentro_de_su_provincia"] = v.provincia_norm == v.provincia_que_contiene_el_punto
    # distancia (km) del punto al polígono de su provincia, si está fuera
    pm = a.set_index("prov_geo").to_crs(32718).geometry
    pp = gpd.GeoSeries(pts.geometry.values, crs="EPSG:4326").to_crs(32718)
    v["km_al_poligono_propio"] = [
        round(float(pp.iloc[i].distance(pm.loc[n])) / 1000, 2) if n in pm.index else None
        for i, n in enumerate(v.provincia_norm)]
    return v.drop(columns=["provincia_norm"])


def obtener_adm2(ruta: str | None, sal: Path) -> Path:
    p = Path(ruta) if ruta else sal / "geoBoundaries-PER-ADM2_simplified.geojson"
    if not p.exists():
        print(f"Descargando {ADM2_URL}")
        urllib.request.urlretrieve(ADM2_URL, p)
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    if h != ADM2_SHA256:
        raise SystemExit(f"SHA-256 de {p} = {h}; se esperaba {ADM2_SHA256}")
    return p


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--salida", default=None)
    ap.add_argument("--adm2", default=None, help="GeoJSON geoBoundaries PER ADM2 ya descargado")
    ap.add_argument("--sin-validar", action="store_true")
    a = ap.parse_args()
    sal = carpeta_salida(a.salida)
    t = construir()
    print(t.fuente.value_counts().to_dict())
    f = escribir_csv(t, sal / "coordenadas_provincias_completo.csv")
    res = comparar(f, INTERIM / f.name, f"v2_reentrenamiento/data/interim/{f.name}")
    if not a.sin_validar:
        v = validar(t, obtener_adm2(a.adm2, sal))
        escribir_csv(v, sal / "validacion_coordenadas_adm2.csv")
        res["validacion_adm2"] = {
            fu: {"n": int((v.fuente == fu).sum()), "dentro_de_su_provincia": int(v[v.fuente == fu].dentro_de_su_provincia.sum())}
            for fu in ("provincia_exacta", "departamento_fallback")}
        res["validacion_adm2"]["fuera"] = v[~v.dentro_de_su_provincia][
            ["departamento", "provincia", "fuente", "provincia_que_contiene_el_punto", "km_al_poligono_propio"]].to_dict("records")
        print(res["validacion_adm2"])
    informe([res], sal / "comparacion_03_coordenadas.json")


if __name__ == "__main__":
    main()
