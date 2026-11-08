"""Construccion del maestro y de las features por ventana sin tocar v2_reentrenamiento/src.

Replica la cadena oficial (00_pesos_geograficos -> 02_fusion_dataset_maestro -> 03_features_temporales)
cambiando solo el fin de la ventana de pesos geograficos (DA3). Cada etapa pasa por una ida y vuelta
CSV en memoria para reproducir bit a bit los archivos oficiales cuando la ventana es Y=2025.
"""
from __future__ import annotations

import io
import json
from functools import lru_cache

import pandas as pd

from lib.entorno import CONFIG, RAIZ_REPO
from v2_reentrenamiento.src.features.agregacion_espacial import AgregadorEspacial
from v2_reentrenamiento.src.features.features_temporales import FeaturesTemporales
from v2_reentrenamiento.src.features.pesos_geograficos import PesosGeograficos, VentanaTrain

VARS_CLIMA = ["T2M", "T2M_MAX", "WS2M", "PRECTOTCORR", "RH2M"]
VARS_INDECI = ["num_emergencias", "personas_afectadas", "personas_damnificadas",
               "total_afectados", "hectareas_cultivo_perdidas", "hectareas_cultivo_afectadas"]
VARS_NLP = ["avg_sentiment", "n_noticias"]
EXOGENAS = VARS_CLIMA + VARS_INDECI + VARS_NLP
CULTIVARES = ("sutil", "dulce")

_RUTAS = json.loads((CONFIG / "rutas_datos.json").read_text(encoding="utf-8"))


def ruta(clave: str, cultivar: str | None = None, oficial: bool = False):
    plantilla = _RUTAS["referencias_oficiales"][clave] if oficial else _RUTAS[clave]
    return RAIZ_REPO / plantilla.format(c=cultivar or "")


def ida_y_vuelta_csv(df: pd.DataFrame) -> pd.DataFrame:
    buf = io.StringIO()
    df.to_csv(buf, index=False)
    buf.seek(0)
    return pd.read_csv(buf)


def con_fecha(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["fecha"] = pd.to_datetime({"year": df["año"].astype(int), "month": df["mes"].astype(int), "day": 1})
    return df.sort_values("fecha").reset_index(drop=True)


class ConstructorDatosVentana:
    """Pesos, maestro y features de un cultivar para un fin de train dado (ano)."""

    def __init__(self) -> None:
        nasa = pd.read_csv(ruta("nasa_provincial"), encoding="utf-8-sig")
        nasa["DATE"] = pd.to_datetime(nasa["DATE"])
        nasa["año"] = nasa["DATE"].dt.year
        nasa["mes"] = nasa["DATE"].dt.month
        self.nasa = nasa
        self.indeci = pd.read_csv(ruta("indeci_provincial"), encoding="utf-8-sig").rename(columns={"anio": "año"})
        self.sent = pd.read_csv(ruta("sentimiento_mensual"), encoding="utf-8-sig")
        self.provincial = {c: pd.read_csv(ruta("produccion_provincial", c), encoding="utf-8-sig") for c in CULTIVARES}
        self.nacional = {c: pd.read_csv(ruta("produccion_nacional", c), encoding="utf-8-sig") for c in CULTIVARES}

    @lru_cache(maxsize=None)
    def pesos(self, cultivar: str, anio_fin_train: int) -> PesosGeograficos:
        ventana = VentanaTrain(2016, 1, anio_fin_train, 12)
        return PesosGeograficos(cultivar=cultivar, ventana=ventana).ajustar(self.provincial[cultivar])

    @lru_cache(maxsize=None)
    def maestro(self, cultivar: str, anio_fin_train: int) -> pd.DataFrame:
        """Equivale a master_dataset_{c}_v2.csv (02_fusion celdas 6 y 8) con pesos de la ventana."""
        # 02_fusion celda 6 lee los pesos desde CSV: se replica la ida y vuelta
        t = ida_y_vuelta_csv(self.pesos(cultivar, anio_fin_train).tabla)
        w = pd.Series(t["peso"].to_numpy(), index=(t["departamento"] + "|" + t["provincia"]).to_numpy())
        clima = AgregadorEspacial(pesos=w, nombre=f"NASA-{cultivar}").agregar(self.nasa, VARS_CLIMA)
        indeci = AgregadorEspacial(pesos=w, nombre=f"INDECI-{cultivar}").agregar(self.indeci, VARS_INDECI)
        nacm = self.nacional[cultivar]
        df = nacm[["año", "mes", "produccion_t_nacional"]].rename(columns={"produccion_t_nacional": f"produccion_t_{cultivar}"})
        df = (df.merge(clima, on=["año", "mes"], how="left")
                .merge(indeci, on=["año", "mes"], how="left")
                .merge(self.sent[["año", "mes"] + VARS_NLP], on=["año", "mes"], how="left"))
        df[VARS_CLIMA + VARS_INDECI] = df[VARS_CLIMA + VARS_INDECI].round(4)
        df = df.sort_values(["año", "mes"]).reset_index(drop=True)
        if len(df) != 120 or int(df.isna().sum().sum()) != 0:
            raise ValueError(f"Maestro {cultivar}/{anio_fin_train} inesperado: {df.shape}, NaN={int(df.isna().sum().sum())}")
        return ida_y_vuelta_csv(df)

    @lru_cache(maxsize=None)
    def features(self, cultivar: str, anio_fin_train: int) -> pd.DataFrame:
        """Equivale a master_dataset_{c}_v2_features.csv (03_features_temporales celda 4)."""
        ft = FeaturesTemporales(target=f"produccion_t_{cultivar}", exogenas=EXOGENAS, lags=(1, 3, 6))
        feats = ft.construir(self.maestro(cultivar, anio_fin_train))
        return ida_y_vuelta_csv(feats)

    def serie(self, cultivar: str) -> pd.Series:
        """Produccion nacional en toneladas indexada por 'YYYY-MM' (2016-01..2025-12)."""
        nacm = self.nacional[cultivar]
        idx = nacm["año"].astype(int).astype(str) + "-" + nacm["mes"].astype(int).map("{:02d}".format)
        return pd.Series(nacm["produccion_t_nacional"].astype(float).to_numpy(), index=idx.to_numpy(), name=cultivar)
