# Supongamos que trabajas en una empresa que fabrica dispositivos electrónicos y quieres analizar los datos de calidad 
# de los componentes utilizados en la producción de dichos dispositivos. Tienes un conjunto de datos que contiene información 
# sobre la fecha de producción, el tipo de componente, el lote al que pertenece el componente y la puntuación de calidad del componente (un número entre 0 y 100). 
# Quieres analizar estos datos para determinar cuál es el tipo de componente con la puntuación de calidad más alta, cuántos componentes se produjeron en cada mes 
# y cuál es la puntuación de calidad promedio de cada tipo de componente.

# Importación de módulos
import numpy as np

# Datos de entrada
datos = np.array([['2022-01-01', 'Componente 1', 'Lote A', 80],
                  ['2022-01-15', 'Componente 1', 'Lote B', 90],
                  ['2022-02-01', 'Componente 2', 'Lote C', 85],
                  ['2022-02-15', 'Componente 2', 'Lote D', 95],
                  ['2022-03-01', 'Componente 1', 'Lote E', 75],
                  ['2022-03-15', 'Componente 2', 'Lote F', 90]])

# Identificar el componente con la puntuación de calidad más alto
tipo_componente = np.unique(datos[:, 1])

puntuacion_calidad = datos[:,3].astype(float)

promedios = np.zeros(len(tipo_componente))
i = 0

for tipo in tipo_componente:
    print(tipo)
    print(puntuacion_calidad[tipo_componente == tipo])
    promedios[i] = np.mean(puntuacion_calidad[tipo_componente == tipo])
    i += 1

indice_maximo = np.argmax(promedios)
componente_mejor_calidad = tipo_componente[indice_maximo]

print("El componente con la puntuación de calidad más alta es: ", componente_mejor_calidad)

# Contar cuántos componentes se produjeron en cada mes
fechas = datos[:, 0]
meses, counts = np.unique([fecha[0:7] for fecha in fechas], return_counts = True)
for i in range(len(meses)):
    print("Mes: ", meses[i], "Cantidad de componentes: ", counts[i])

# Calcular la puntuación de calidad promedio de cada tipo de componente que tenemos almacenado en nuestro array de datos 
promedio_componente = np.zeros(len(tipo_componente))
for i in range(len(tipo_componente)):
    promedio_componente[i] = np.mean(puntuacion_calidad[tipo_componente == tipo_componente[i]])
    print("Tipo de componente: ", tipo_componente[i], "Puntuación de calidad promedio: ", promedio_componente[i])

# Resultado
# El componente con la puntuación de calidad más alta es: Componente 2

