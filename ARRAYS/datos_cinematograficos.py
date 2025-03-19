# Supongamos que tienes un conjunto de datos de películas que contiene información sobre su título, género, duración, año de lanzamiento y calificación. 
# Quieres analizar estos datos para determinar cuál es el género de película más popular, cuántas películas se lanzaron en cada década y cuál es la duración promedio de cada género de película.

# np.unique --> Devuelve los valores únicos de un array, eliminando duplicados.
# np.argsort --> Devuelve los índices que ordenarían un array en orden ascendente.
# np.count_nonzero --> Cuenta la cantidad de elementos distintos de cero en un array.

# Importación de módulos
import numpy as np

# Array con datos de peliculas
peliculas = np.array([    
    ['Peli 1', 'Comedia', 120, 1990, 8.5],
    ['Peli 2', 'Acción', 110, 2005, 7.8],
    ['Peli 3', 'Drama', 95, 2010, 6.9],
    ['Peli 4', 'Comedia', 100, 1985, 7.5],
    ['Peli 5', 'Acción', 130, 2015, 8.1],
    ['Peli 6', 'Drama', 115, 2000, 6.7],
    ['Peli 7', 'Comedia', 90, 1995, 8.2],
    ['Peli 8', 'Acción', 105, 2010, 7.4],
    ['Peli 9', 'Drama', 125, 1980, 6.8],
    ['Peli 10', 'Comedia', 95, 2000, 8.0]
])


# Obtener generos populares y apariciones de la base de datos almacenada de peliculas
generos, conteos = np.unique(peliculas[:, 1], return_counts = True)

# Ordenamos el número de apariciones que tiene el array de peliculas de mayor a menor
conteos_desc = np.argsort(conteos)[:, :, -1]

# Obtener el genero más popular
genero_popular = generos[conteos_desc[0]]

print("El genero más popular es: ", genero_popular)

# Agrupamos las peliculas de la BBDD por decada redondeando y aproximando a la decada
decadas = np.unique(peliculas[:,3].astype(int) // 10 * 10)

# contamos las peliculas en cada decada
conteos_decadas = []
for decada in decadas:
    conteo = np.count_nonzero((peliculas[:,3].astype(int) >= decada) & (peliculas[:,3].astype(int) < decada + 10))
    conteos_decadas.append(conteo)

    print("En al decada de", decada, "se crearon", conteo, "peliculas")

# Duracion promedio por genero
todos_generos = peliculas[:,1]
duraciones = peliculas[:,2]
duracion_media = np.zeros(len(generos))

# Calculamos la duracion media segun
for i in range(len(generos)):
    duracion_media[i] = np.mean(duraciones[todos_generos == generos[i]].astype(float))
    print("Duracion media de las peliculas de tipo:", generos[i], "es de", duracion_media[i], "minutos")
