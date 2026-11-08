"""Ejecucion reanudable de la Fase C (diseno aprobado: opcion a).

Unidad = (modelo, cultivo, ventana, semilla); los modelos sin semilla (SARIMA, SARIMA-sel, lineales, Naive,
Seasonal Naive, Chronos) usan una unidad por modelo, cultivo y ventana.

Cada unidad escribe todo en una carpeta temporal `<destino>.tmp`. Al terminar, escribe ahi `completado.json`
(hash de la configuracion, hash del codigo y SHA-256 de cada archivo) y renombra la carpeta a `<destino>`.
Una unidad cuenta como hecha solo si `<destino>/completado.json` existe y sus hashes coinciden.
Al reanudar: las unidades hechas se saltan; una carpeta `.tmp` sobrante se borra y la unidad se repite.
Si una unidad hecha tiene otro hash de configuracion o de codigo, o le falta un archivo, la corrida se detiene
(no se mezclan resultados de dos versiones).

Log: `<raiz>/10_logs/ejecucion/faseC_<etapa>.log`, en modo anadir, con [INICIO], [OK], [VENTANA] y [FALLO].
El log no muestra metricas de test (solo progreso y lo elegido con la validacion): el test se resume en la Fase D.
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import sys
import time
import traceback
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from lib.entorno import BR, CONFIG
from lib.integridad import sha256_normalizado

CARPETAS = {
    "Naive": "naive", "Seasonal Naive": "seasonal_naive", "Chronos": "chronos_bolt_tiny",
    "SARIMA": "sarima_rolling", "SARIMA-sel": "sarima_sel", "Ridge": "ridge", "ElasticNet": "elasticnet",
    "XGB-37": "xgb37", "XGB-43": "exploratorios/xgb43", "GC3": "gc3_lstm_sin_nlp", "GE": "ge_lstm_con_nlp",
}
ARCHIVOS_CONFIG = ("hiperparametros_congelados.json", "ventanas.json", "rutas_datos.json", "hashes_congelados.json")
LIB = Path(__file__).resolve().parent


def _hash_conjunto(rutas: list[Path], base: Path) -> tuple[str, dict[str, str]]:
    tabla = {r.relative_to(base).as_posix(): sha256_normalizado(r) for r in rutas}
    total = hashlib.sha256(json.dumps(tabla, sort_keys=True).encode("utf-8")).hexdigest()
    return total, tabla


def hash_configuracion() -> tuple[str, dict[str, str]]:
    """Configuracion congelada; hashes_congelados.json cubre a su vez src oficial, datos y Chronos."""
    return _hash_conjunto([CONFIG / n for n in ARCHIVOS_CONFIG], CONFIG)


def hash_codigo(script: Path) -> tuple[str, dict[str, str]]:
    """Todo 02_scripts/lib/*.py mas el script de la etapa."""
    rutas = sorted(LIB.glob("*.py")) + [Path(script).resolve()]
    return _hash_conjunto(rutas, LIB.parent)


def ahora() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


class Registro:
    """Log de la etapa: cada linea va a stdout y al archivo (con flush y fsync, sobrevive a una interrupcion)."""

    def __init__(self, raiz: Path, etapa: str) -> None:
        self.ruta = raiz / "10_logs" / "ejecucion" / f"faseC_{etapa}.log"
        self.ruta.parent.mkdir(parents=True, exist_ok=True)

    def __call__(self, etiqueta: str, texto: str) -> None:
        linea = f"{ahora()} [{etiqueta}] {texto}"
        print(linea, flush=True)
        with open(self.ruta, "a", encoding="utf-8") as f:
            f.write(linea + "\n")
            f.flush()
            os.fsync(f.fileno())


@dataclass(frozen=True)
class Unidad:
    modelo: str
    cultivar: str
    anio: int
    semilla: int | None = None

    def carpeta(self, raiz: Path) -> Path:
        c = raiz / "04_modelos" / CARPETAS[self.modelo] / self.cultivar / str(self.anio)
        return c / f"seed_{self.semilla:02d}" if self.semilla is not None else c

    @property
    def nombre(self) -> str:
        s = f" seed {self.semilla:02d}" if self.semilla is not None else ""
        return f"{self.modelo} {self.cultivar} {self.anio}{s}"


def escribir_csv(df: pd.DataFrame, ruta: Path) -> None:
    df.to_csv(ruta, index=False, float_format="%.17g")


def escribir_json(obj: dict, ruta: Path) -> None:
    ruta.write_text(json.dumps(obj, indent=2, ensure_ascii=False, default=str), encoding="utf-8")


def _reemplazar(origen: Path, destino: Path, intentos: int = 10) -> None:
    """os.replace con reintentos: en Windows el antivirus o el indexador pueden bloquear un instante."""
    for i in range(intentos):
        try:
            os.replace(origen, destino)
            return
        except PermissionError:
            if i == intentos - 1:
                raise
            time.sleep(0.5)


class Reanudador:
    """Ejecuta unidades de forma idempotente y lleva el log de la etapa."""

    def __init__(self, etapa: str, script: str, raiz: Path | None = None, interrumpir_en: int | None = None) -> None:
        self.etapa = etapa
        self.raiz = Path(raiz) if raiz else BR
        self.log = Registro(self.raiz, etapa)
        self.hash_config, self.tabla_config = hash_configuracion()
        self.hash_codigo, self.tabla_codigo = hash_codigo(Path(script))
        self.interrumpir_en = interrumpir_en  # solo pruebas: corta el proceso en la unidad nueva n (1, 2, ...)
        self.nuevas = 0
        self.por_ventana: dict[int, dict[str, int]] = {}

    def anunciar(self, texto: str) -> None:
        import subprocess

        head = subprocess.run(["git", "rev-parse", "--short=12", "HEAD"], cwd=BR, capture_output=True, text=True).stdout.strip()
        self.log("INICIO", f"etapa {self.etapa}: {texto} | HEAD {head or '?'} | hash_config {self.hash_config[:12]} "
                           f"| hash_codigo {self.hash_codigo[:12]} | pid {os.getpid()}")

    def hecha(self, u: Unidad) -> bool:
        """True si la unidad ya esta completa y es valida; error si existe pero no corresponde a esta version."""
        final = u.carpeta(self.raiz)
        marca = final / "completado.json"
        if not final.exists():
            return False
        if not marca.exists():
            raise RuntimeError(f"{u.nombre}: existe {final} sin completado.json (no la creo este flujo); revisar a mano.")
        c = json.loads(marca.read_text(encoding="utf-8"))
        if c.get("hash_config") != self.hash_config or c.get("hash_codigo") != self.hash_codigo:
            raise RuntimeError(f"{u.nombre}: completado.json con otro hash de configuracion o de codigo. "
                               "No se mezclan versiones: se detiene la corrida.")
        for nombre, h in c["archivos"].items():
            r = final / nombre
            if not r.exists() or sha256_normalizado(r) != h:
                raise RuntimeError(f"{u.nombre}: el archivo {nombre} falta o cambio desde que se completo.")
        return True

    def ejecutar(self, u: Unidad, trabajo) -> dict | None:
        """trabajo(carpeta_tmp) escribe sus archivos en la carpeta y devuelve un resumen (dict)."""
        cuenta = self.por_ventana.setdefault(u.anio, {"nuevas": 0, "reanudadas": 0})
        if self.hecha(u):
            cuenta["reanudadas"] += 1
            self.log("OK", f"{u.nombre} | ya completada (completado.json valido): se salta")
            return None
        final = u.carpeta(self.raiz)
        tmp = final.with_name(final.name + ".tmp")
        nota = ""
        if tmp.exists():
            shutil.rmtree(tmp)
            nota = " | se borro una carpeta .tmp de una corrida interrumpida"
        tmp.mkdir(parents=True)
        self.log("INICIO", f"{u.nombre}{nota}")
        t0 = time.perf_counter()
        try:
            resumen = trabajo(tmp) or {}
        except Exception:
            self.log("FALLO", f"{u.nombre} | {traceback.format_exc(limit=3).strip().splitlines()[-1]}")
            raise
        self.nuevas += 1
        if self.interrumpir_en is not None and self.nuevas == self.interrumpir_en:
            self.log("FALLO", f"{u.nombre} | interrupcion simulada (--interrumpir-en {self.interrumpir_en}): "
                              "archivos escritos en .tmp, sin completado.json ni renombrado")
            os._exit(3)
        seg = time.perf_counter() - t0
        archivos = {p.name: sha256_normalizado(p) for p in sorted(tmp.iterdir()) if p.is_file()}
        marca = {"unidad": u.__dict__, "etapa": self.etapa, "hash_config": self.hash_config, "hash_codigo": self.hash_codigo,
                 "archivos": archivos, "segundos": seg, "fin": ahora(), "resumen": resumen}
        escribir_json(marca, tmp / "completado.json.tmp")
        _reemplazar(tmp / "completado.json.tmp", tmp / "completado.json")
        _reemplazar(tmp, final)
        cuenta["nuevas"] += 1
        extra = " | " + " ".join(f"{k}={v}" for k, v in resumen.items() if k in ("elegido", "MAE_val", "mejor_epoca", "convergio")) if resumen else ""
        self.log("OK", f"{u.nombre} | {seg:.1f} s{extra}")
        return resumen

    def cerrar_ventana(self, anio: int) -> None:
        c = self.por_ventana.get(anio, {"nuevas": 0, "reanudadas": 0})
        self.log("VENTANA", f"{anio} completa en {self.etapa}: {c['nuevas'] + c['reanudadas']} unidades "
                            f"({c['nuevas']} nuevas, {c['reanudadas']} ya hechas)")

    def consolidar(self, modelos: list[str]) -> Path:
        """05_predicciones/<etapa>.csv a partir de las unidades completas (regenerable; escritura atomica)."""
        partes = []
        for m in modelos:
            base = self.raiz / "04_modelos" / CARPETAS[m]
            for marca in sorted(base.rglob("completado.json")):
                if ".tmp" in marca.parent.name:
                    continue
                u = json.loads(marca.read_text(encoding="utf-8"))["unidad"]
                p = pd.read_csv(marca.parent / "predicciones.csv")
                partes.append(p.assign(modelo=u["modelo"], cultivar=u["cultivar"], anio_test=u["anio"], semilla=u["semilla"]))
        destino = self.raiz / "05_predicciones" / f"{self.etapa}.csv"
        destino.parent.mkdir(parents=True, exist_ok=True)
        if partes:
            df = pd.concat(partes, ignore_index=True)
            cols = ["modelo", "cultivar", "anio_test", "semilla", "particion", "fecha", "y_true", "y_pred"]
            df = df[cols + [c for c in df.columns if c not in cols]]
            escribir_csv(df, destino.with_suffix(".csv.tmp"))
            _reemplazar(destino.with_suffix(".csv.tmp"), destino)
        return destino


def argumentos_comunes(ap) -> None:
    ap.add_argument("--anios", type=int, nargs="+", help="subconjunto de ventanas (por defecto todas las viables)")
    ap.add_argument("--cultivares", nargs="+", choices=("sutil", "dulce"), default=["sutil", "dulce"])
    ap.add_argument("--modelos", nargs="+")
    ap.add_argument("--semillas", type=int, nargs="+", default=list(range(10)))
    ap.add_argument("--salida", help="raiz alternativa (pruebas); por defecto la carpeta del experimento")
    ap.add_argument("--interrumpir-en", type=int, help="SOLO PRUEBAS: corta el proceso en la unidad nueva n")


def ventanas_de(args, modelo: str):
    from lib.ventanas import todas

    return [v for v in todas() if v.viable(modelo) and (not args.anios or v.anio in args.anios)]


def salir_con_error(log: Registro | None, exc: BaseException) -> None:
    if log is not None:
        log("FALLO", f"se detiene la corrida (no se cambia el protocolo): {type(exc).__name__}: {exc}")
    sys.exit(1)


def correr_etapa(etapa: str, script: str, args, modelos_validos: tuple[str, ...], con_semilla: tuple[str, ...], trabajo_de) -> None:
    """Bucle comun: ventana -> cultivo -> modelo -> semilla. trabajo_de(unidad, ventana, carpeta_tmp) -> resumen.

    Verifica la integridad al empezar; ante cualquier error registra [FALLO] y termina con codigo 1.
    """
    from lib.integridad import Integridad
    from lib.ventanas import Ventana

    modelos = tuple(args.modelos or modelos_validos)
    desconocidos = set(modelos) - set(modelos_validos)
    if desconocidos:
        raise SystemExit(f"Modelos no validos para {etapa}: {sorted(desconocidos)}")
    r = Reanudador(etapa, script, args.salida, args.interrumpir_en)
    try:
        r.anunciar(f"modelos {list(modelos)} | cultivos {args.cultivares} | anios {args.anios or 'todos los viables'}"
                   + (f" | semillas {args.semillas}" if set(modelos) & set(con_semilla) else ""))
        r.log("INICIO", f"integridad: {Integridad().verificar()}")
        viables = {m: [v.anio for v in ventanas_de(args, m)] for m in modelos}
        for anio in sorted({a for lista in viables.values() for a in lista}):
            for c in args.cultivares:
                for m in modelos:
                    if anio not in viables[m]:
                        continue
                    for s in (args.semillas if m in con_semilla else [None]):
                        u = Unidad(m, c, anio, s)
                        r.ejecutar(u, lambda tmp, u=u: trabajo_de(u, Ventana(u.anio), tmp))
            r.cerrar_ventana(anio)
        destino = r.consolidar(list(modelos))
        r.log("OK", f"etapa {etapa} completa | consolidado {destino.relative_to(r.raiz).as_posix()}")
    except Exception as exc:  # noqa: BLE001
        salir_con_error(r.log, exc)
