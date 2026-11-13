# Deterioration under Large Production Changes: Evaluating a Dual-Branch LSTM against Statistical and Pretrained Benchmarks for Small-Data Agricultural Forecasting in Peru

**Authors:** Fabrizio Yerald Alfonso Sanchez Saravia, Alex Coila Jarita and Esteban Tocto-Cano
(Professional School of Systems Engineering, Faculty of Engineering and Architecture, Universidad Peruana Unión, Juliaca, Peru).

Code, frozen input tables and results of the article submitted to *Forecasting* (MDPI). The study forecasts the
monthly national production of sour lime (*limón sutil*) and sweet lime (*limón dulce*) in Peru with a rolling-origin
backtesting (test years 2018–2025) and compares ten models: Naive, Seasonal Naive, Chronos-Bolt-tiny (zero-shot),
SARIMA, SARIMA-sel, Ridge, ElasticNet, XGBoost and two dual-branch LSTM networks with Bahdanau attention (GC3 without
news features, GE with news sentiment). It also contains the diagnostic experiments added during peer review.

## Contents

```
reproduce.py                    single driver: reproduces every table and figure data file and compares them
download_chronos_weights.py     Chronos-Bolt weights at the exact Hugging Face revisions
expected_outputs_sha256.json    SHA-256 of the 2,231 published CSV outputs (reference for the comparison)
requirements.txt                exact package versions (Python 3.11.9)
LICENSE                         MIT license of the code (see "License" for the data tables and vendored code)
v2_reentrenamiento/
  src/                          model, feature and training code (28 files; SHA-256 frozen)
  etl/                          raw sources -> frozen input tables (MIDAGRI-SISAGRI, INDECI, province coordinates)
  data/interim/                 frozen input tables: national and provincial lime series, INDECI monthly panel,
                                province coordinates, monthly news sentiment (aggregates only)
  data/raw/nasa_power/          NASA POWER monthly climate by province, 2016-2025
  data/processed/               master datasets of the original 2025 evaluation (reference for equivalence tests)
  resultados_v2_final/          scalers, geographic weights and the original 2025 test evaluation (reference)
  DECISIONES_METODOLOGICAS.md   methodological decision log (Spanish)
  experimentos_backtesting_rodante/
    00_plan/  01_configuracion/ protocol, frozen hyperparameters, windows, thresholds, hashes, environment manifest
    02_scripts/                 pipeline: run_all.py (phases B, C, D1, D2), models, metrics, statistics, figures
    03_ventanas/                windows, shock thresholds and masks, MASE denominators, geographic weights
    04_modelos/                 per-unit predictions, chosen hyperparameters and training histories
                                (model binaries are not included)
    05_predicciones/            consolidated predictions (frozen before the evaluation phase)
    06_metricas/ 07_barrido_umbral/   metrics, bootstrap intervals, Diebold-Mariano tests, threshold sweep
    08_graficos/                figures (PNG, PDF) with the CSV data and a TXT description of each figure
    09_reportes/                phase reports and protocol deviations (DESVIACIONES.md), in Spanish;
                                revision_g7/fase1/ holds the first-round review tables and g7_fase1.py
    11_geometria_externa/       public-domain boundaries used only for the study-area map
    12_revision_g7/             diagnostic experiments (scripts, per-unit predictions, tables T1-T10)
v3_robustez_metodologica/, v4_benchmark_moderno/   two reference files and the vendored Chronos package
data/interim/nasa/, notebooks/fase2/               two files of an earlier project version used by etl/03
```

Folder and file names are in Spanish because the paths are part of the frozen SHA-256 registry
(`01_configuracion/hashes_congelados.json`); renaming them would break the integrity checks.

## Installation

Python **3.11** is required (tested with 3.11.9 on Windows 11, CPU only; TensorFlow 2.21 does not support Python 3.13+).

```bash
python -m venv venv
venv\Scripts\activate            # Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
python download_chronos_weights.py          # Chronos-Bolt-tiny (~35 MB); add --all for small and base (~1 GB)
```

## Reproducing the results (one command)

```bash
python reproduce.py
```

From the frozen predictions, the driver (1) verifies the SHA-256 of the official code, the frozen input tables and the
Chronos weights; (2) runs the leakage tests; (3) recomputes all metrics, bootstrap intervals, Diebold-Mariano tests and
the threshold sweep; (4) evaluates the diagnostic experiments and regenerates the 15 first-round review tables of
`09_reportes/revision_g7/fase1/`; (5) redraws the figures; and (6) compares the 2,231 CSV outputs with
`expected_outputs_sha256.json`. The result is written to `reproduction_report.json`. On the authors'
machine both modes reproduce every file byte for byte, except the wall-clock run times stored in
`12_revision_g7/resultados/T10_lstm_epocas_parametros.csv` after `--retrain`. Bit-identical results on other
hardware or operating systems are not guaranteed for the neural networks.

To refit every model from the frozen input tables (rolling-origin backtesting and diagnostic experiments; 1 h 52 min
on a 16-thread AMD CPU under Windows 11; needs `download_chronos_weights.py --all`), run on a fresh clone:

```bash
python reproduce.py --retrain
```

All runs fix `PYTHONHASHSEED=42`, `TF_ENABLE_ONEDNN_OPTS=0`, `TF_DETERMINISTIC_OPS=1` and run offline
(`HF_HUB_OFFLINE=1`). Seeded models use seeds 0–9.

### First-round review tables (`09_reportes/revision_g7/fase1/`)

The script that originally produced these 15 CSV files was lost. `09_reportes/revision_g7/fase1/g7_fase1.py` is a
reconstruction that recomputes them from the frozen predictions (`05_predicciones/`), the shock masks and MASE
denominators (`03_ventanas/`), the metric tables T06, T15 and T17 (`06_metricas/`) and the national and provincial
lime series (`data/interim/`). It writes to a temporary folder (never over the published files) and compares every
cell with the published tables; `reproduce.py` runs it and stores the result under `g7_fase1_tables` in
`reproduction_report.json`. On the authors' machine all 15 tables are reproduced byte for byte. To run it alone:

```bash
python v2_reentrenamiento/experimentos_backtesting_rodante/09_reportes/revision_g7/fase1/g7_fase1.py --estricto
```

## Regenerating the frozen input tables from the raw data

The raw files are not redistributed. Download them, place them in the paths below (or pass the paths as arguments)
and run the three ETL scripts. Each script writes to a temporary folder (never over `data/interim/`) and compares its
output, cell by cell and by SHA-256, with the frozen table.

[`data_sources.json`](data_sources.json) lists every data source (MIDAGRI–SISAGRI, INDECI, NASA POWER, geoBoundaries,
Agraria.pe) with its link, access date (or "not recorded"), expected file, path, size in bytes and SHA-256. The ETL
scripts read it: if a raw file is missing they print the link and the expected path; if its SHA-256 differs they warn
that it is not the file used in the article and continue (add `--estricto` to stop instead).

| Source | Raw file | Where to get it | Script |
|---|---|---|---|
| MIDAGRI, SISAGRI (crop statistics) | `v2_reentrenamiento/data/raw/midagri/sisagri_2015_2026.xlsx` (229,208,492 bytes; SHA-256 `b7dec236a0d65c7aada297118cab584104863e6f21430fe60e279cf5293e3283`) | [MIDAGRI Regional Productive Profile dashboard (SISAGRI)](https://app.powerbi.com/view?r=eyJrIjoiN2U3NTdkYTktOTk5Ny00NjQ5LTg0ZjEtMmIzYzlmZWIwMDhlIiwidCI6IjdmMDg0NjI3LTdmNDAtNDg3OS04OTE3LTk0Yjg2ZmQzNWYzZiJ9), district-level export of all crops, 2015–2026 (5 sheets) | `python v2_reentrenamiento/etl/01_sisagri_a_series.py [--excel PATH]` (~10 min) |
| INDECI (emergency records) | `v2_reentrenamiento/data/raw/indeci/oficial_2016_2018/BD_2003-2025_EMERGENCIAS.csv` (27,040,446 bytes; SHA-256 `a1fe63f0a7c836b8ff7dd1c87271d3bd3144f8444e41f93b7db205c85fef2687`) | Peruvian open-data portal (datosabiertos.gob.pe), consolidated INDECI emergencies dataset 2003–2025 | `python v2_reentrenamiento/etl/02_indeci_a_panel.py [--crudo PATH]` |
| Province coordinates | included (`data/interim/nasa/clima_dataset_final.csv`, `notebooks/fase2/_build_act02_time.py`) | validated against [geoBoundaries](https://www.geoboundaries.org) gbOpen PER ADM2 (downloaded by the script, commit `90a1d52`) | `python v2_reentrenamiento/etl/03_coordenadas.py` |
| NASA POWER (climate) | included (`data/raw/nasa_power/por_provincia/clima_nasa_power_2016_2025.csv`) | [NASA POWER](https://power.larc.nasa.gov) monthly point API (endpoint `https://power.larc.nasa.gov/api/temporal/monthly/point`) | `v2_reentrenamiento/src/data_collection/nasa_power_downloader_v2.py` |

Download dates: the manuscript cites the MIDAGRI dashboard as accessed on 25 June 2026; the workbook used here has a
file date of 29 August 2026. The INDECI dataset was described as updated on 26 August 2026. The exact download URLs
and dates of the two raw files were not recorded; the SHA-256 above identifies the exact files used. Rules and
limitations of each ETL step are documented in `v2_reentrenamiento/etl/README.md` (Spanish).

## News data

The texts of the [Agraria.pe](https://agraria.pe) news items (headlines, bodies or excerpts) are **not redistributed**. The repository
contains only the monthly aggregates used by the models,
`v2_reentrenamiento/data/interim/noticias/sentimiento_mensual_2016_2025.csv`: mean sentiment score
(`avg_sentiment`, RoBERTuito via pysentimiento 0.7.3, rounded to 4 decimals) and number of news items (`n_noticias`)
per month, 2016–2025 (2,883 items from agraria.pe, *agronegocios* section). The scraper used to collect the corpus is
`v2_reentrenamiento/src/data_collection/agraria_scraper_v2.py`.

## License

- **Code**: MIT License (see `LICENSE`), © 2026 Fabrizio Yerald Alfonso Sanchez Saravia, Alex Coila Jarita and
  Esteban Tocto-Cano.
- **Derived data tables** (frozen input tables, predictions, metrics, figure data and the other CSV files produced
  by this project): [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
  Please cite the article (see "How to cite") when you reuse them. The source data (MIDAGRI–SISAGRI, INDECI,
  NASA POWER) remain subject to the terms of their providers; the CC BY 4.0 licence applies to the derived tables
  in this repository.
- **Third-party code**: `v4_benchmark_moderno/vendor/` contains vendored copies of Chronos (`chronos-forecasting`
  2.3.2, Apache-2.0) and einops (0.8.2, MIT). They keep their original licenses (included in the `*.dist-info/licenses/`
  folders) and are not covered by the project's MIT license.

## How to cite

Sanchez Saravia, F.Y.A.; Coila Jarita, A.; Tocto-Cano, E. Deterioration under Large Production Changes: Evaluating a
Dual-Branch LSTM against Statistical and Pretrained Benchmarks for Small-Data Agricultural Forecasting in Peru.
*Forecasting* (submitted, 2026).

Volume, pages and DOI will be added on publication.

Contact: estocan@upeu.edu.pe
