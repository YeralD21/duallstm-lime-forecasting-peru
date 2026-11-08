"""
AgrariaScraperV2 — Scraper corregido de Agraria.pe (tema cat7, 2026).

Reemplaza a historical_scraper.py (Selenium, selectores obsoletos) para la
ventana 2016-2025 del reentrenamiento v2. Diferencias clave vs v1:

  - Basado en requests (no Selenium): ~0.8-1.0 s/pagina vs 4 s/pagina medidos.
  - Selectores nuevos (dominio actual, tema "cat7"): el listado ya expone la
    fecha en .cat7-meta / .cat7-news-meta, y el cuerpo en div.cuerpo.
  - Categorias actualizadas del menu de agraria.pe (negocios -> agronegocios,
    tecnologia -> ciencia-e-innovacion) + auto-deteccion de la ultima pagina.
  - Sin limite duro de paginacion (v1 tenia end_page=200).
  - Mantiene el esquema de salida identico al corpus v1/v2:
    fecha, titular, cuerpo_completo, fuente, url
  - robots.txt respetado (Agraria.pe permite todo) + delays humanos (2-4 s).

Salida: agro_news_{anio}.csv por año + checkpoint json por categoria/pagina.
"""

import argparse
import json
import logging
import os
import random
import re
import socket
import sys
import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FutureTimeoutError
from datetime import datetime
from pathlib import Path
from urllib import robotparser

import pandas as pd
import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format='%(message)s')
LOGGER = logging.getLogger('agraria_v2')

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MESES_ES = {
    'enero': '01', 'febrero': '02', 'marzo': '03', 'abril': '04',
    'mayo': '05', 'junio': '06', 'julio': '07', 'agosto': '08',
    'septiembre': '09', 'setiembre': '09',
    'octubre': '10', 'noviembre': '11', 'diciembre': '12'
}

CATEGORIAS = [
    'agronegocios', 'produccion', 'alimentacion', 'ciencia-e-innovacion',
    'clima-y-medio-ambiente', 'eventos', 'opinion', 'politica',
    'proyectos', 'publirreportajes', 'salud-y-sanidad', 'agraria-tv'
]

KEYWORDS_NIVEL1 = [
    'limón', 'limon', 'piura', 'sullana', 'tumbes', 'niño', 'senamhi',
    'midagri', 'lluvias', 'sequía', 'sequia', 'helada'
]

KEYWORDS_NIVEL2 = [
    'agroexportación', 'agroexportaciones', 'cosecha', 'campaña agrícola',
    'campaña agricola', 'producción agrícola', 'produccion agricola',
    'sector agrario', 'clima', 'cambio climático', 'cambio climatico',
    'fenómeno climático', 'fenomeno climatico', 'irrigación', 'irrigacion',
    'inundación', 'inundacion'
]

CONTEXTO_AGRO = [
    'limón', 'limon', 'cítricos', 'citricos', 'naranja', 'mandarina',
    'fruta', 'frutas', 'uva', 'uvas', 'palta', 'paltas', 'espárrago',
    'esparrago', 'café', 'cafe', 'mango', 'arándano', 'arandano',
    'piura', 'sullana', 'tumbes', 'lambayeque', 'perú', 'peru', 'región',
    'region', 'agro'
]


def matches_filtro(texto: str) -> bool:
    """Filtro 2 niveles: Nivel 1 match directo; Nivel 2 solo con contexto agro."""
    t = texto.lower()
    if any(kw in t for kw in KEYWORDS_NIVEL1):
        return True
    if any(kw in t for kw in KEYWORDS_NIVEL2):
        return any(c in t for c in CONTEXTO_AGRO)
    return False


def parse_fecha_es(raw: str) -> str:
    """'28 agosto 2026 |09:22 am', '31 enero de 2026' -> '2026-08-28'."""
    try:
        clean = str(raw).split('|')[0].strip().lower()
        clean = re.sub(r'[^\w\sáéíóúñ]', ' ', clean)
        clean = re.sub(r'\s+', ' ', clean).strip()
        parts = [p for p in clean.split() if p != 'de']
        if len(parts) >= 3:
            day = parts[0].zfill(2)
            month = MESES_ES.get(parts[1], '')
            year = parts[2]
            if month and year.isdigit() and len(year) == 4 and day.isdigit():
                return f'{year}-{month}-{day}'
    except Exception:
        pass
    return ''


def _ultima_pagina(soup: BeautifulSoup) -> int:
    last = None
    for a in soup.find_all('a', href=True):
        m = re.search(r'page=(\d+)$', a['href'])
        if m and 'categoria' in a['href']:
            pg = int(m.group(1))
            last = pg if last is None else max(last, pg)
    return last or 1


class AgrariaScraperV2:
    """Scraper requests-based de Agraria.pe con selectores cat7 verificados."""

    SCHEMA = ['fecha', 'titular', 'cuerpo_completo', 'fuente', 'url']

    def __init__(self, delay_min: float = 2.0, delay_max: float = 4.0,
                 min_year: int = 2016, max_year: int = 2025,
                 output_dir: str = None, checkpoint_file: str = None,
                 user_agent: str = None):
        self.delay_min = delay_min
        self.delay_max = delay_max
        self.min_year = min_year
        self.max_year = max_year

        self.base_url = 'https://agraria.pe'
        self.output_dir = Path(output_dir or (
            PROJECT_ROOT / 'v2_reentrenamiento' / 'data' / 'raw' / 'noticias' / 'agraria_pe'))
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.checkpoint_file = Path(checkpoint_file or (self.output_dir / 'checkpoint_v2.json'))

        self.headers = {
            'User-Agent': (user_agent or
                           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                           'AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/120.0.0.0 Safari/537.36'),
            'Accept-Language': 'es-PE,es;q=0.9,en;q=0.5',
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

        self.rp = robotparser.RobotFileParser()
        self.rp.set_url(f'{self.base_url}/robots.txt')
        try:
            self.rp.read()
            LOGGER.info('robots.txt de agraria.pe leido OK')
        except Exception as e:
            LOGGER.warning(f'No se pudo leer robots.txt: {e}')
            self.rp = None

        self.seen_urls = set()
        self._load_seen_urls()

    # ------------------------------------------------------------------
    # HTTP (GET con guarda anti-DNS-hang + reintentos con backoff exponencial)
    # ------------------------------------------------------------------
    # Errores "transitorios" de red: se reintentan. Cualquier otro error
    # (HTTP real de la app, parseo, etc.) NO se captura aqui para no
    # ocultar bugs de otra indole.
    RETRYABLE_EXCEPTIONS = (
        requests.exceptions.ConnectionError,
        requests.exceptions.Timeout,
        socket.gaierror,
    )
    MAX_RETRIES = 5
    BACKOFF_SECONDS = [2, 4, 8, 16, 32]

    def _get(self, url: str, timeout: int = 30) -> requests.Response:
        if self.rp is not None and not self.rp.can_fetch(self.headers['User-Agent'], url):
            LOGGER.warning(f'robots.txt prohibe: {url}')
            return None
        for attempt in range(1, self.MAX_RETRIES + 1):
            try:
                executor = ThreadPoolExecutor(max_workers=1)
                future = executor.submit(requests.get, url, headers=self.headers, timeout=timeout)
                try:
                    resp = future.result(timeout=timeout + 10)
                except FutureTimeoutError:
                    raise requests.exceptions.Timeout(f'Request colgada: {url}')
                finally:
                    executor.shutdown(wait=False)
                try:
                    resp.raise_for_status()
                except requests.exceptions.HTTPError as e:
                    LOGGER.error(f'HTTP {resp.status_code} en {url}: {e}')
                    return None
                return resp
            except self.RETRYABLE_EXCEPTIONS as e:
                if attempt >= self.MAX_RETRIES:
                    LOGGER.error(
                        f'[FALLO PERMANENTE] {type(e).__name__} en {url} tras '
                        f'{self.MAX_RETRIES} intentos: {e}')
                    raise
                wait_s = self.BACKOFF_SECONDS[attempt - 1]
                LOGGER.warning(
                    f'[{type(e).__name__}] {url} | reintentando en {wait_s}s... '
                    f'intento {attempt + 1}/{self.MAX_RETRIES}')
                time.sleep(wait_s)
        return None

    def _delay(self):
        time.sleep(random.uniform(self.delay_min, self.delay_max))

    # ------------------------------------------------------------------
    # Persistencia / dedupe
    # ------------------------------------------------------------------
    def _load_seen_urls(self):
        for f in self.output_dir.glob('agro_news_*.csv'):
            try:
                df = pd.read_csv(f, usecols=['url'])
                self.seen_urls.update(u.rstrip('/') for u in df['url'].dropna().astype(str))
            except Exception as e:
                LOGGER.warning(f'No se pudo leer cache de {f.name}: {e}')
        if self.seen_urls:
            LOGGER.info(f'Cache de URLs cargado: {len(self.seen_urls)}')

    def _append_row(self, row: dict):
        if not row or not row.get('url'):
            return
        anio = int(row['fecha'][:4])
        filepath = self.output_dir / f'agro_news_{anio}.csv'
        df = pd.DataFrame([row], columns=self.SCHEMA)
        if not filepath.exists():
            df.to_csv(filepath, index=False, encoding='utf-8')
        else:
            df.to_csv(filepath, mode='a', header=False, index=False, encoding='utf-8')
        self.seen_urls.add(row['url'].rstrip('/'))

    def _save_checkpoint(self, categoria: str, page: int):
        state = {}
        if self.checkpoint_file.exists():
            try:
                with open(self.checkpoint_file, 'r', encoding='utf-8') as f:
                    state = json.load(f)
            except Exception:
                pass
        state[categoria] = {'last_page': page, 'updated_at': datetime.now().isoformat()}
        with open(self.checkpoint_file, 'w', encoding='utf-8') as f:
            json.dump(state, f, indent=2, ensure_ascii=False)

    def _load_checkpoint(self, categoria: str) -> int:
        if self.checkpoint_file.exists():
            try:
                with open(self.checkpoint_file, 'r', encoding='utf-8') as f:
                    state = json.load(f)
                if categoria in state:
                    return int(state[categoria]['last_page'])
            except Exception:
                pass
        return None

    # ------------------------------------------------------------------
    # Parsing del listado (tema cat7 verificado)
    # ------------------------------------------------------------------
    def _parse_articulos(self, soup: BeautifulSoup, categoria: str) -> list:
        container = soup.find('div', class_='cat7-container')
        if not container:
            return []
        arts = container.find_all('article', class_='cat7-featured')
        arts += container.find_all('article', class_='cat7-news')

        resultado = []
        for art in arts:
            h2 = art.find('h2')
            if not h2:
                continue
            link = h2.find('a', href=True)
            if not link:
                continue
            url = link['href'].rstrip('/')
            if '/noticias/' not in url or url in self.seen_urls:
                continue
            titular = link.get_text(strip=True)

            # fecha: el listado expone '28 agosto 2026' en .cat7-meta/.cat7-news-meta
            fecha_iso = ''
            for sel in ['.cat7-meta', '.cat7-news-meta']:
                meta = art.select_one(sel)
                if meta:
                    txt = meta.get_text(' ', strip=True)
                    fecha_iso = parse_fecha_es(txt)
                    if fecha_iso:
                        break

            # resumen para filtro de keywords
            resumen_sel = art.select_one('.cat7-featured-summary') or art.select_one('.cat7-news-summary')
            resumen = resumen_sel.get_text(' ', strip=True) if resumen_sel else ''
            texto = f'{titular} {resumen}'

            resultado.append({
                'url': url, 'titular': titular,
                'fecha_iso': fecha_iso, 'texto': texto,
                'fuente': f'agraria.pe/{categoria}',
            })
        return resultado

    # ------------------------------------------------------------------
    # Cuerpo del articulo
    # ------------------------------------------------------------------
    def _fetch_cuerpo(self, url: str) -> str:
        resp = self._get(url)
        if resp is None:
            return ''
        soup = BeautifulSoup(resp.content, 'html.parser')
        content = (soup.find('div', class_='cuerpo') or
                   soup.select_one('div.text-justify') or
                   soup.find('div', class_='card-body'))
        if not content:
            return ''
        parrafos = [p.get_text(' ', strip=True) for p in content.find_all('p')
                    if p.get_text(' ', strip=True)]
        if not parrafos:
            # tema antiguo (pre ~2017): cuerpo usa divs directos en vez de <p>
            for ch in content.find_all(recursive=False):
                if getattr(ch, 'name', None) in ('div', 'p'):
                    t = ch.get_text(' ', strip=True)
                    if t:
                        parrafos.append(t)
        texto = ' '.join(parrafos)
        texto = re.sub(r'\s+', ' ', texto)
        return re.sub(r'\(Agraria\.pe\)', '', texto, flags=re.IGNORECASE)

    # ------------------------------------------------------------------
    # Motor principal por categoria
    # ------------------------------------------------------------------
    def scrape_categoria(self, categoria: str, end_page: int = None, resume: bool = True):
        base = f'{self.base_url}/noticias/categoria/{categoria}'
        start = self._load_checkpoint(categoria) if resume else None
        if start is not None:
            start += 1  # retomar DESPUES de la pagina ya completada
            LOGGER.info(f'Checkpoint encontrado: retomando en pagina {start}')

        # pagina 1 para detectar ultima pagina (si no se especifica)
        primero = 1 if start is None or resume is False else min(start, 1)
        if end_page is None:
            resp = self._get(f'{base}?page=1')
            if resp is None:
                LOGGER.error(f'No se pudo leer pagina 1 de {categoria}. Abortando.')
                return
            soup = BeautifulSoup(resp.content, 'html.parser')
            end_page = _ultima_pagina(soup)
            LOGGER.info(f'{categoria}: ultima pagina detectada = {end_page}')

        start = start if start is not None else 1
        if start > end_page:
            LOGGER.info(f'{categoria}: ya completada (checkpoint en {start}).')
            return

        LOGGER.info(f'{categoria}: paginas {start}..{end_page} | ventana {self.min_year}-{self.max_year}')
        n_guardadas = 0

        for page in range(start, end_page + 1):
            url = f'{base}?page={page}'
            resp = self._get(url)
            if resp is None:
                LOGGER.warning(f'  ! pagina {page} fallo. Siguiente.')
                self._save_checkpoint(categoria, page)
                continue
            soup = BeautifulSoup(resp.content, 'html.parser')

            candidatos = self._parse_articulos(soup, categoria)
            filtrados = []
            for c in candidatos:
                if not c['fecha_iso']:
                    continue
                anio = int(c['fecha_iso'][:4])
                if not (self.min_year <= anio <= self.max_year):
                    continue
                if not matches_filtro(c['texto']):
                    continue
                filtrados.append(c)

            self._delay()

            for c in filtrados:
                cuerpo = self._fetch_cuerpo(c['url'])
                if cuerpo:
                    self._append_row({
                        'fecha': c['fecha_iso'],
                        'titular': c['titular'],
                        'cuerpo_completo': cuerpo,
                        'fuente': c['fuente'],
                        'url': c['url'],
                    })
                    n_guardadas += 1
                self._delay()

            self._save_checkpoint(categoria, page)
            if page % 20 == 0 or page == end_page:
                LOGGER.info(f'  {categoria} pag {page}/{end_page} | guardadas={n_guardadas}')

        LOGGER.info(f'{categoria}: FIN. guardadas={n_guardadas}')

    def scraper_categorias(self, categorias=None, end_page=None, resume=True):
        for c in (categorias or CATEGORIAS):
            LOGGER.info(f'--- INICIO {c} ---')
            self.scrape_categoria(c, end_page=end_page, resume=resume)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Agraria.se V2 scraper')
    parser.add_argument('--categoria', default='produccion')
    parser.add_argument('--end-page', type=int, default=None)
    parser.add_argument('--start-page', type=int, default=1, help='ignorar: entra por checkpoint')
    parser.add_argument('--min-year', type=int, default=2016)
    parser.add_argument('--max-year', type=int, default=2025)
    parser.add_argument('--delay-min', type=float, default=2.0)
    parser.add_argument('--delay-max', type=float, default=4.0)
    parser.add_argument('--resume', action='store_true', default=False)
    parser.add_argument('--no-resume', dest='resume', action='store_false')
    parser.set_defaults(resume=True)
    args = parser.parse_args()

    scraper = AgrariaScraperV2(
        delay_min=args.delay_min, delay_max=args.delay_max,
        min_year=args.min_year, max_year=args.max_year)
    scraper.scrape_categoria(args.categoria, end_page=args.end_page, resume=args.resume)
    print('[OK] Scraping finalizado. Archivos en', scraper.output_dir)