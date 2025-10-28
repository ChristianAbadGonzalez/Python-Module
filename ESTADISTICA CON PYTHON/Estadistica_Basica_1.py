# Importación y uso de librerias
import pandas as pd
import numpy as np

# Definición de función
def calulo(vector):

    # Cálculo del proceso de la media
    suma = 0
    n = 0

    for elemento in vector:

        suma += elemento
        n += 1

    media = ((1/n) * suma)
    
    print('El valor de la media hallado es: ', media)

    # Otras alternativas de calculo
    suma_alternativa = sum(vector)
    n_alternativo = len(vector)

    media_alternativa = ((1/n_alternativo) * suma_alternativa)
    
    print('El valor de la media hallado es: ', media_alternativa)


    # Cálculo del proceso de la moda
    moda = 0
    repeticiones = 0

    diccionario = {}

    for elemento in vector:

        if not diccionario.get(elemento):
            diccionario[elemento] = 1

        else:
            diccionario[elemento] += 1

        if diccionario[elemento] > repeticiones:
            repeticiones = diccionario[elemento]  
            moda=elemento

    print('El valor de la moda hallado es: ', moda)


    # Cálculo del proceso de la mediana
    vector.sort(reverse = False) # Ordenamos el vector de menor a mayor

    punto_medio = int(len(vector)/2)

    if len(vector) % 2 ==0:

        mediana = (vector[punto_medio] + vector[punto_medio+1])/2

    else:
        mediana = vector[punto_medio]

    print('El valor de la mediana hallado es: ',mediana)


# Ejemplo de uso
Vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 6, 5, 7, 5]

# calulo(Vector)

df = pd.read_csv('Salary_data.csv', sep=";")

# print(df.head())

print(df.age.mean())
print(df.age.mode())

V = np.array(Vector)
print(V.mean())