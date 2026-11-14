"""R2-T13 (obs. 7): desde que mes existen, en las tablas de entrada congeladas, la produccion por cultivo, el clima,
INDECI y las noticias. POSTERIOR AL PROTOCOLO; solo lee data/interim/ y data/raw/nasa_power/.

Para cada fuente: primer y ultimo mes, numero de meses distintos, primer mes con valor > 0 y meses sin dato o en 0.
Ademas comprueba que los archivos leidos tienen el SHA-256 registrado en 01_configuracion/hashes_congelados.json
(si figuran alli). El Excel crudo de MIDAGRI (sisagri_2015_2026.xlsx) no se redistribuye: su cobertura no se puede
comprobar aqui.
Salida: resultados/T13_cobertura_datos.csv
Uso: python 13_revision_r2/scripts/t13_cobertura_datos.py
"""
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import r2lib as R  # noqa: E402
from lib.entorno import preparar_entorno  # noqa: E402

preparar_entorno()

import pandas as pd  # noqa: E402

DATA = R.RAIZ / "v2_reentrenamiento" / "data"
HASHES = json.loads((R.BR / "01_configuracion" / "hashes_congelados.json").read_text(encoding="utf-8"))


def sha_lf(p: Path) -> str:
    return hashlib.sha256(p.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def registrado(p: Path) -> str:
    rel = p.relative_to(R.RAIZ).as_posix()
    encontrado = next((g[rel] for g in HASHES.values() if isinstance(g, dict) and rel in g), None)
    if encontrado is None:
        return "no registrado"
    if encontrado != sha_lf(p):
        raise SystemExit(f"{rel}: SHA-256 distinto del registrado en hashes_congelados.json")
    return "coincide"


def fila(fuente, p: Path, meses: pd.Series, valor: pd.Series | None, nota: str) -> dict:
    m = pd.Series(sorted(meses.unique()))
    completos = pd.period_range(m.iloc[0], m.iloc[-1], freq="M").strftime("%Y-%m")
    faltan = sorted(set(completos) - set(m))
    pos = None
    cero = []
    if valor is not None:
        agg = valor.groupby(meses).sum()
        pos = agg[agg > 0].index.min()
        cero = list(agg[agg <= 0].index)
    return {"fuente": fuente, "archivo": p.relative_to(R.RAIZ).as_posix(), "sha256_vs_hashes_congelados": registrado(p),
            "primer_mes": m.iloc[0], "ultimo_mes": m.iloc[-1], "n_meses": len(m), "meses_faltantes": ";".join(faltan),
            "primer_mes_con_valor_positivo": pos, "meses_con_valor_0": ";".join(cero), "nota": nota}


filas = []
for c in R.CULTIVARES:
    p = DATA / "interim" / f"limon_{c}_nacional_mensual.csv"
    d = pd.read_csv(p, dtype={"año": str, "mes": str})
    filas.append(fila(f"produccion nacional {c} (MIDAGRI-SISAGRI)", p, d["año"] + "-" + d["mes"].str.zfill(2), d.produccion_t_nacional,
                      "valor = produccion_t_nacional (t)"))
    p = DATA / "interim" / f"limon_{c}_distrito_crudo.csv"
    d = pd.read_csv(p, dtype={"AÑO": str, "MES": str}, usecols=["AÑO", "MES", "PRODUCCION"])
    filas.append(fila(f"produccion distrital {c} (MIDAGRI-SISAGRI, filtrada por el ETL)", p, d["AÑO"] + "-" + d["MES"].str.zfill(2),
                      d.PRODUCCION, "valor = suma de PRODUCCION de los distritos (t)"))
p = DATA / "raw" / "nasa_power" / "por_provincia" / "clima_nasa_power_2016_2025.csv"
d = pd.read_csv(p, encoding="utf-8-sig", usecols=["provincia", "DATE", "T2M"])
filas.append(fila("clima NASA POWER (109 provincias)", p, d.DATE.str[:7], None,
                  f"{d.provincia.nunique()} provincias; cada provincia tiene {int(d.groupby('provincia').size().min())} a "
                  f"{int(d.groupby('provincia').size().max())} meses"))
p = DATA / "interim" / "indeci_limpio_2016_2025.csv"
d = pd.read_csv(p)
filas.append(fila("emergencias INDECI/SINPAD (panel provincia x mes)", p, d.anio.astype(str) + "-" + d.mes.astype(str).str.zfill(2),
                  d.num_emergencias, "valor = num_emergencias sumado sobre provincias"))
p = DATA / "interim" / "noticias" / "sentimiento_mensual_2016_2025.csv"
d = pd.read_csv(p, encoding="utf-8-sig")
d.columns = ["anio", "mes", "avg_sentiment", "n_noticias"]
filas.append(fila("noticias Agraria.pe (sentimiento mensual)", p, d.anio.astype(str) + "-" + d.mes.astype(str).str.zfill(2),
                  d.n_noticias, "valor = n_noticias; el corpus de textos no se redistribuye"))

T = pd.DataFrame(filas)
T.to_csv(R.RES / "T13_cobertura_datos.csv", index=False, lineterminator="\n")
with pd.option_context("display.width", 250, "display.max_columns", 20, "display.max_colwidth", 60):
    print(T.drop(columns=["archivo", "nota"]))
