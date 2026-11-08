
import nbformat as nbf
import os

def create_notebook():
    nb = nbf.v4.new_notebook()
    nb.metadata['kernelspec'] = {
        'display_name': 'Python 3',
        'language': 'python',
        'name': 'python3'
    }

    cells = []

    # Markdown - Title
    cells.append(nbf.v4.new_markdown_cell("# 🕒 Actividad 02: Codificación Cíclica del Tiempo y Coordenadas NASA\n---\n**Módulo 2: Feature Engineering para LSTM**\n\nEste notebook implementa la transformación de variables temporales en representaciones cíclicas (seno/coseno) y la integración de coordenadas geográficas. Estos pasos son críticos para que el modelo **LSTM-Attention** capture correctamente la estacionalidad agrícola y la proximidad espacial de las provincias."))

    # Markdown - Preamble
    cells.append(nbf.v4.new_markdown_cell("## 🎯 Objetivos\n1. **Codificación Cíclica**: Transformar meses y trimestres para eliminar saltos artificiales entre diciembre (12) y enero (1).\n2. **Coordenadas NASA**: Asegurar que cada registro tenga su latitud y longitud para que el modelo aprenda patrones climáticos regionales.\n3. **Validación Visual**: Confirmar que la transformación circular se realizó correctamente."))

    # Code - Setup
    cells.append(nbf.v4.new_code_cell("""import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Configuración estética
sns.set_theme(style='whitegrid', palette='viridis')
%matplotlib inline

# Rutas
INPUT_FILE = '../../data/processed/master_dataset_fase1.csv'
OUTPUT_FILE = '../../data/processed/master_dataset_fase2_multivariado.csv'

if not os.path.exists(INPUT_FILE):
    # Intentamos con v2 si existe
    INPUT_FILE = '../../data/processed/master_dataset_fase1_v2.csv'

print(f"Cargando dataset desde: {INPUT_FILE}")"""))

    # Markdown - Step 1
    cells.append(nbf.v4.new_markdown_cell("## 1. Carga de Datos\nLeemos el dataset generado en la Fase 1 que integra MIDAGRI, INDECI y NASA."))

    # Code - Load
    cells.append(nbf.v4.new_code_cell("""df = pd.read_csv(INPUT_FILE)
print(f"Dataset cargado: {df.shape[0]} filas, {df.shape[1]} columnas")
df.head(2)"""))

    # Markdown - Step 2
    cells.append(nbf.v4.new_markdown_cell("## 2. Integración de Coordenadas NASA\n\n### ¿Para qué sirve este paso?\nEl modelo LSTM analiza secuencias temporales, pero no sabe qué provincias están cerca de otras. Al incluir `lat` y `lon`, le damos al modelo una **dimensión espacial**. Por ejemplo, Piura y Lambayeque comparten climas similares por su ubicación; las coordenadas permiten al modelo aprender esa relación."))

    # Code - Coords Mapping
    cells.append(nbf.v4.new_code_cell("""# Diccionario de coordenadas por departamento (Centroide aproximado)
# Nota: Si se dispone de coordenadas provinciales exactas de NASA POWER, se pueden incluir aquí.
COORDS_DEPTO = {
    'AMAZONAS': (-6.2294, -77.8728),
    'ANCASH': (-9.5261, -77.5289),
    'APURIMAC': (-13.6339, -72.8814),
    'AREQUIPA': (-16.4090, -71.5375),
    'AYACUCHO': (-13.1588, -74.2239),
    'CAJAMARCA': (-7.1638, -78.5003),
    'CALLAO': (-12.0566, -77.1491),
    'CUSCO': (-13.5320, -71.9675),
    'HUANCAVELICA': (-12.7826, -74.9727),
    'HUANUCO': (-9.9306, -76.2422),
    'ICA': (-14.0678, -75.7286),
    'JUNIN': (-11.1582, -74.9962),
    'LA LIBERTAD': (-8.1091, -79.0285),
    'LAMBAYEQUE': (-6.7711, -79.8441),
    'LIMA': (-12.0464, -77.0428),
    'LORETO': (-3.7491, -73.2538),
    'MADRE DE DIOS': (-12.5933, -69.1891),
    'MOQUEGUA': (-17.1983, -70.9357),
    'PASCO': (-10.6865, -76.2625),
    'PIURA': (-5.1945, -80.6328),
    'PUNO': (-15.8422, -70.0199),
    'SAN MARTIN': (-6.5200, -76.3656),
    'TACNA': (-18.0146, -70.2536),
    'TUMBES': (-3.5669, -80.4515),
    'UCAYALI': (-8.3791, -74.5339)
}

# Rellenar coordenadas faltantes basándose en el departamento
def fill_coords(row):
    if pd.isna(row['lat']) or pd.isna(row['lon']):
        return COORDS_DEPTO.get(row['departamento'], (np.nan, np.nan))
    return row['lat'], row['lon']

# Aplicamos la función si las columnas existen, si no, las creamos
if 'lat' not in df.columns: df['lat'] = np.nan
if 'lon' not in df.columns: df['lon'] = np.nan

new_coords = df.apply(fill_coords, axis=1)
df['lat'] = [c[0] for c in new_coords]
df['lon'] = [c[1] for c in new_coords]

print(f"Coordenadas integradas. NaNs restantes: {df['lat'].isna().sum()}")"""))

    # Markdown - Step 3
    cells.append(nbf.v4.new_markdown_cell("## 3. Codificación Cíclica (Mes y Trimestre)\n\n### ¿Por qué es necesaria?\nSi usamos el mes como número (1, 2, ..., 12), el modelo cree que la distancia entre Diciembre (12) y Enero (1) es 11. Pero en la realidad, ¡están pegados! \n\nUsando la transformación **Seno y Coseno**, convertimos el tiempo en un círculo donde el 12 y el 1 quedan matemáticamente contiguos.\n\n*   `month_sin = sin(2π * mes / 12)`\n*   `month_cos = cos(2π * mes / 12)`\n*   `quarter_sin = sin(2π * trimestre / 4)`\n*   `quarter_cos = cos(2π * trimestre / 4)`"))

    # Code - Cyclic Encoding
    cells.append(nbf.v4.new_code_cell("""# 1. Asegurar formato fecha
df['fecha_evento'] = pd.to_datetime(df['fecha_evento'])

# 2. Extraer componentes
df['mes_num'] = df['fecha_evento'].dt.month
df['trimestre_num'] = df['fecha_evento'].dt.quarter

# 3. Transformación Cíclica del Mes
df['month_sin'] = np.sin(2 * np.pi * df['mes_num'] / 12)
df['month_cos'] = np.cos(2 * np.pi * df['mes_num'] / 12)

# 4. Transformación Cíclica del Trimestre
df['trimestre_sin'] = np.sin(2 * np.pi * df['trimestre_num'] / 4)
df['trimestre_cos'] = np.cos(2 * np.pi * df['trimestre_num'] / 4)

print("Codificación cíclica completada para Mes y Trimestre.")
df[['fecha_evento', 'month_sin', 'month_cos', 'trimestre_sin', 'trimestre_cos']].head()"""))

    # Markdown - Step 4
    cells.append(nbf.v4.new_markdown_cell("## 4. Visualización de los Resultados\n\n### El \"Reloj\" del Tiempo\nSi graficamos el Seno vs el Coseno, deberíamos ver un círculo perfecto. Esto confirma que el modelo ahora entiende que el tiempo es cíclico."))

    # Code - Visualizations
    cells.append(nbf.v4.new_code_cell("""plt.figure(figsize=(15, 6))

# Subplot 1: Círculo de Meses
plt.subplot(1, 2, 1)
plt.scatter(df['month_sin'], df['month_cos'], c=df['mes_num'], cmap='hsv', alpha=0.5)
plt.title('Codificación Cíclica: Meses (1-12)', fontsize=12)
plt.xlabel('Seno')
plt.ylabel('Coseno')
plt.axis('equal')
plt.colorbar(label='Mes')

# Subplot 2: Círculo de Trimestres
plt.subplot(1, 2, 2)
plt.scatter(df['trimestre_sin'], df['trimestre_cos'], c=df['trimestre_num'], cmap='coolwarm', s=100)
plt.title('Codificación Cíclica: Trimestres (1-4)', fontsize=12)
plt.xlabel('Seno')
plt.ylabel('Coseno')
plt.axis('equal')
plt.colorbar(label='Trimestre')

plt.tight_layout()
plt.savefig('../../data/processed/visualizacion_ciclica.png')
plt.show()"""))

    # Markdown - Step 5
    cells.append(nbf.v4.new_markdown_cell("## 5. Exportar Dataset Preparado para LSTM\nGuardamos el dataset final de la Fase 2, que ahora incluye sentimiento NLP, coordenadas y tiempo cíclico."))

    # Code - Export
    cells.append(nbf.v4.new_code_cell("""# Eliminar columnas auxiliares si se desea (opcional)
# df = df.drop(columns=['mes_num', 'trimestre_num'])

# Guardar
df.to_csv(OUTPUT_FILE, index=False)
print(f"Dataset exportado exitosamente a: {OUTPUT_FILE}")
print(f"Columnas finales: {df.columns.tolist()}")"""))

    nb.cells = cells

    output_path = 'notebooks/fase2/actividad_02_cyclic_time_encoding.ipynb'
    with open(output_path, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)

if __name__ == "__main__":
    create_notebook()
