# Importación de módulos necesarios
import numpy as np
import pandas as pd

# Muestreo Aleatorio - Generamos una población de ejemplo
poblacion = np.arange(1, 101)  # Población del 1 al 100 como arreglo NumPy (IDs 1..100)

tamaño_muestra = 10  # Tamaño de la muestra que queremos extraer

# Seleccionamos la muestra usando un muestreo aleatorio simple (sin reemplazo)
# - np.random.choice elige 'tamaño_muestra' elementos de 'poblacion'
# - replace=False asegura que no se repitan individuos
muestra_aleatoria_simple = np.random.choice(poblacion, tamaño_muestra, replace=False)
print('Muestra aleatoria simple:', muestra_aleatoria_simple)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# Muestreo Estratificado
# Construimos un DataFrame con:
# - 'individuos': IDs del 1 al 100
# - 'estratos': 4 estratos etiquetados A, B, C, D con 25 individuos cada uno (repetimos 25 veces cada etiqueta)
data = {
    'individuos': np.arange(1, 101),
    'estratos': np.repeat(['A', 'B', 'C', 'D'], 25)
}

poblacion = pd.DataFrame(data)

# print(poblacion.head())  # (opcional) ver las primeras filas

tamaño_muestra = 12  # Tamaño total que deseamos extraer de forma estratificada

# Muestreo Estratificado:
# - groupby('estratos'): separa la población por cada estrato A, B, C, D
# - para cada grupo (x), toma una muestra al azar de tamaño proporcional:
#     tamaño_estrato_aprox = tamaño_muestra * len(x) / len(poblacion)
#   y se redondea al entero más cercano con np.rint.
# - Nota: la suma de redondeos por estrato puede no ser exactamente 'tamaño_muestra'
#   (por temas de redondeo), pero la idea general es respetar la proporción.
muestra_estratificada = poblacion.groupby('estratos', group_keys=False).apply(
    lambda x: x.sample(int(np.rint(tamaño_muestra * len(x) / len(poblacion))))
)

print("Muestra Estratificada \n", muestra_estratificada)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------

# Muestreo por Conglomerados - Población de ejemplo con conglomerados
# Creamos un DataFrame con:
# - 'individuos': IDs del 1 al 50
# - 'conglomerados': 10 conglomerados (1..10), cada uno con 5 individuos (se repite cada ID de conglomerado 5 veces)
data = {
    'individuos': np.arange(1, 51),
    'conglomerados': np.repeat(np.arange(1, 11), 5)  # 10 conglomerados con 5 individuos cada uno
}

poblacion = pd.DataFrame(data)

print(poblacion)  # Mostramos la estructura completa de la población con sus conglomerados

# Elegimos aleatoriamente 2 conglomerados distintos (sin reemplazo)
# - unique() obtiene los valores únicos de la columna 'conglomerados'
# - np.random.choice selecciona 2 IDs de conglomerado al azar
conglomerados_seleccionados = np.random.choice(poblacion['conglomerados'].unique(), size=2, replace=False)

# La muestra por conglomerados incluye TODOS los individuos cuyos 'conglomerados' pertenecen
# al conjunto seleccionado (muestreo de conglomerados de una etapa)
muestra_por_conglomerados = poblacion[poblacion['conglomerados'].isin(conglomerados_seleccionados)]

print("Muestra por conglomerados \n", muestra_por_conglomerados)