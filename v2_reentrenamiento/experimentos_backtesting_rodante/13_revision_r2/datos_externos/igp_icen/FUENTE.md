# Índice Costero El Niño (ICEN) y lista de eventos — IGP / ENFEN

Descargados el **2026-11-13T21:39:26Z** (UTC; ver `fecha_descarga_utc.txt`), desde la página de índices climáticos del
IGP, http://met.igp.gob.pe/variabclim/indices.html. Los archivos no se modificaron después de la descarga.

| Archivo | URL | SHA-256 |
|---|---|---|
| `ICEN.txt` | http://met.igp.gob.pe/datos/ICEN.txt (ICEN oficial, ENFEN 2024) | `14b3469df9397cb30359945f90a81768ae7fe86924ff66dbccc97d4e06af01a5` |
| `ICEN_91_20.txt` | http://met.igp.gob.pe/datos/ICEN_91_20.txt (ICEN tradicional, climatología 1991–2020; "no es el ICEN oficial") | `1015dd4d61bbb96998d9dc8ee01978c6ec27abca5e407b3ed85e0e3c0bbe762e` |
| `ICENr.txt` | http://met.igp.gob.pe/datos/ICENr.txt | `ec45b0d2cb59e295c7c64998369def6308e7fbd087823da13da321d43b58fe36` |
| `lista_eventos_ICEN.html` | http://met.igp.gob.pe/datos/lista_eventos_ICEN.html (eventos El Niño y La Niña costeros, criterio ENFEN 2024) | `08f00f183f3e02f4f7000a7445166c1676273d5ec8c736fc29897024aa1723e5` |

Uso: solo `lista_eventos_ICEN.html`, en `scripts/t8_ex_ante.py` (definición C de T8: meses dentro de un evento El Niño
Costero). Referencia: ENFEN (2024). *Definición operacional de los eventos El Niño Costero y La Niña Costera en el
Perú*. Nota Técnica.

Advertencia de la propia página: desde 2015, el sistema de alerta del ENFEN puede declarar eventos sin que se cumplan
las condiciones del ICEN, y esa declaración operativa tiene prelación. Los comunicados de alerta no se descargaron: la
definición C usa solo la lista basada en el ICEN.
