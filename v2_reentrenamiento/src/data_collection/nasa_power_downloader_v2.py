import logging
import time

import numpy as np
import pandas as pd
import requests


class NasaPowerV2Downloader:
    """
    Descarga mensual de NASA POWER (community=AG) para el dataset v2 de
    reentrenamiento, usando las coordenadas de
    data/interim/coordenadas_provincias_completo.csv (109 provincias).

    Variables (5): T2M, T2M_MAX, WS2M, PRECTOTCORR, RH2M
    (T2M_MAX es nueva vs v1; WS2M fue la variable dominante en SHAP v1).

    Salida LONG: departamento, provincia, DATE, <vars>, month_sin,
    month_cos, lat, lon.
    """

    API_URL = 'https://power.larc.nasa.gov/api/temporal/monthly/point'

    PARAMETROS = [
        'T2M',
        'T2M_MAX',
        'WS2M',
        'PRECTOTCORR',
        'RH2M',
    ]

    def __init__(self, coords_path: str, delay: float = 0.7,
                 retries: int = 3, backoff: float = 2.0, log_every: int = 20):
        self.coords_path = coords_path
        self.delay = delay
        self.retries = retries
        self.backoff = backoff
        self.log_every = log_every
        self.logger = logging.getLogger(__name__)

    def _leer_coordenadas(self) -> pd.DataFrame:
        df = pd.read_csv(self.coords_path, encoding='utf-8')
        cols = ['departamento', 'provincia', 'lat', 'lon', 'fuente']
        return df[cols].drop_duplicates().reset_index(drop=True)

    def _fetch_punto(self, lat: float, lon: float,
                     anho_inicio: int, anho_fin: int) -> dict:
        params = {
            'parameters': ','.join(self.PARAMETROS),
            'community': 'AG',
            'longitude': lon,
            'latitude': lat,
            'start': anho_inicio,
            'end': anho_fin,
            'format': 'JSON',
        }
        last_err = None
        for intento in range(1, self.retries + 1):
            try:
                resp = requests.get(self.API_URL, params=params, timeout=90)
                resp.raise_for_status()
                return resp.json()
            except Exception as e:  # noqa: BLE001
                last_err = e
                if intento < self.retries:
                    time.sleep(self.backoff * intento)
        raise last_err

    def _parse_punto(self, data: dict, departamento: str, provincia: str,
                     lat: float, lon: float) -> pd.DataFrame:
        param_data = data['properties']['parameter']
        muestra = next(iter(param_data.values()))
        fechas = sorted(k for k in muestra.keys() if not k.endswith('13'))

        rows = []
        for fecha in fechas:
            anho, mes = int(fecha[:4]), int(fecha[4:6])
            row = {
                'departamento': departamento,
                'provincia': provincia,
                'DATE': f'{anho}-{mes:02d}-01',
            }
            for p in self.PARAMETROS:
                row[p] = param_data[p].get(fecha)
            row['month_sin'] = np.sin(2 * np.pi * mes / 12)
            row['month_cos'] = np.cos(2 * np.pi * mes / 12)
            row['lat'] = lat
            row['lon'] = lon
            rows.append(row)

        return pd.DataFrame(rows)

    def download(self, anho_inicio: int, anho_fin: int):
        """Descarga todas las provincias. Devuelve (df_final, errores)."""
        coords = self._leer_coordenadas()
        n = len(coords)
        self.logger.info(
            f'Descargando NASA POWER {anho_inicio}-{anho_fin} '
            f'para {n} provincias...')

        dfs, errores = [], []
        for i, row in coords.iterrows():
            dept, prov = row['departamento'], row['provincia']
            try:
                data = self._fetch_punto(
                    row['lat'], row['lon'], anho_inicio, anho_fin)
                dfs.append(self._parse_punto(
                    data, dept, prov, row['lat'], row['lon']))
            except Exception as e:  # noqa: BLE001
                errores.append((dept, prov, float(row['lat']),
                                float(row['lon']), str(e)))
                self.logger.warning(f'  [{i+1}/{n}] ERROR {dept}-{prov}: {e}')

            if (i + 1) % self.log_every == 0 or (i + 1) == n:
                self.logger.info(
                    f'{i+1}/{n} provincias descargadas, '
                    f'{len(errores)} errores')
            time.sleep(self.delay)

        cols = (['departamento', 'provincia', 'DATE'] + self.PARAMETROS +
                ['month_sin', 'month_cos', 'lat', 'lon'])
        df_final = (pd.concat(dfs, ignore_index=True) if dfs
                    else pd.DataFrame(columns=cols))
        return df_final[cols], errores


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    COORDS = (r'C:\Machine-learming\Machine-Learning-Multimodal--Agro-NLP-Clima-'
              r'\v2_reentrenamiento\data\interim\coordenadas_provincias_completo.csv')
    OUT_DIR = (r'C:\Machine-learming\Machine-Learning-Multimodal--Agro-NLP-Clima-'
               r'\v2_reentrenamiento\data\raw\nasa_power\por_provincia')
    OUT = OUT_DIR + r'\clima_nasa_power_2016_2025.csv'
    LOG = OUT_DIR + r'\errores_descarga.log'

    downloader = NasaPowerV2Downloader(COORDS, delay=0.7, log_every=20)
    df, errores = downloader.download(2016, 2025)

    print()
    print('Shape final:', df.shape)
    df.to_csv(OUT, index=False, encoding='utf-8-sig')
    print(f'[OK] Guardado en {OUT}')

    if errores:
        with open(LOG, 'w', encoding='utf-8') as f:
            f.write('# provincias fallidas en descarga NASA POWER 2016-2025\n')
            for e in errores:
                f.write('%s\t%s\t%r\t%r\t%s\n' % e)
        print(f'[ALERTA] {len(errores)} provincias con error ')
        print(f'  log en {LOG}')
    else:
        print('[OK] 0 provincias con error.')