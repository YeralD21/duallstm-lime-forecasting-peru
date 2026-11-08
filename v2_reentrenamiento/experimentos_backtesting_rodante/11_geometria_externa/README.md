# Geometría externa (Fase D3, fig29)

Descargada el 2026-10-30T00:32:44Z (UTC) solo para dibujar el mapa de la zona de estudio. **No está en git** (carpeta sin versionar; no se cambió `.gitignore`). No se modificó ningún archivo tras la descarga.

| Archivo | URL | Tamaño (bytes) | SHA-256 |
|---|---|---:|---|
| `geoboundaries_PER_ADM1/geoBoundaries-PER-ADM1_simplified.geojson` | https://github.com/wmgeolab/geoBoundaries/raw/90a1d52/releaseData/gbOpen/PER/ADM1/geoBoundaries-PER-ADM1_simplified.geojson | 326,575 | `df5bbc9e4eabae9dcf9fe163180be85c1ef297bb1633e250b6f0c5bab5deebdf` |
| `natural_earth_10m_admin0/ne_10m_admin_0_countries.zip` | https://naciscdn.org/naturalearth/10m/cultural/ne_10m_admin_0_countries.zip | 4,930,492 | `ce1ac7036499a0edd641fbc093cd209a98f96a49d2eca8480aaacad35138a7f6` |

Total: 5,257,067 bytes (≈ 5.0 MB).

## Licencias

- **geoBoundaries gbOpen, PER ADM1** (metadato leído en https://www.geoboundaries.org/api/current/gbOpen/PER/ADM1/ antes de descargar):
  boundaryID `PER-ADM1-1875124`; boundaryLicense **Public Domain**; boundarySource Wikimedia Commons
  (licenseSource commons.wikimedia.org/wiki/File); boundaryYearRepresented **2008**; admUnitCount 26; buildDate 21 feb 2024.
  Cita: Runfola, D. et al. (2020). geoBoundaries: A global database of political administrative boundaries. *PLoS ONE* 15(4): e0231866.
- **Natural Earth**, 1:10m Cultural Vectors, Admin 0 – Countries: dominio público (naturalearthdata.com). Solo se usan los países vecinos (ECU, COL, BRA, BOL, CHL).

## Emparejamiento con los departamentos de MIDAGRI

El ADM1 tiene 26 unidades: 24 departamentos, **El Callao** y Lima partida en **Lima** (región) y **Municipalidad Metropolitana de Lima**.
MIDAGRI usa un solo departamento LIMA (incluye la provincia LIMA), así que en `02_scripts/11_figuras_d3.py` las dos piezas de Lima se unen
(`dissolve`) en LIMA; El Callao queda como CALLAO, que no aparece en los datos de producción. Resultado: 25 polígonos departamentales.
Los nombres se emparejan en mayúsculas y sin tildes (la Ñ se conserva).

Límites de 2008 de origen no oficial (Wikimedia, no INEI): adecuados para un mapa de ubicación a escala nacional, no como límite catastral.
