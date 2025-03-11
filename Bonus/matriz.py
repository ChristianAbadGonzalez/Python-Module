# --- Crea un script que dada una lista de listas M (numérica), identifique si se trata de una matriz y en ese caso imprima dos listas correspondientes a: --- 
# --- 1. La fila cuyos elementos suman el máximo
# --- 2. La columna cuyos elementos suman el máximo

# --- Definimos una matriz de "m" filas y "n" columnas de tamaño cuadrado --> 1x1 2x2 3x3 ...
M = [[2,5,3],
     [6,1,8],
     [7,5,4]]

# --- Definimos y comprobamos el tamaño de la matriz definida ---
filas = len(M)
columnas = len(M[0])  # Tomamos la longitud de la primera fila

# --- Comprobamos si la matriz es cuadrada obteniendo una respuesta booleana ---
matriz_cuadrada = all(len(fila) == columnas for fila in M)


if matriz_cuadrada:

    # --- Inicializamos la variable de suma maxima ---
    sum_max_fila = 0
    num_fila = -1

    # --- Recorremos las filas de la matriz con el objetivo de obtener el número maximo del valor de las componentes de cada fila ---
    for i in range(filas):
        suma_fila = sum(M[i])
        # --- Si la suma de la fila tiene el valor máximo, lo almacenamos dicho valor para posteriormente imprimirlo por la pantalla ---
        if suma_fila > sum_max_fila:
            sum_max_fila = suma_fila
            num_fila = i
    print("La fila cuyos elementos obtienen el máximo valor es: ", M[i], "cuyo valor es: ", sum_max_fila)

    # --- Encontrar la columna con la suma máxima ---
    sum_max_col = 0
    num_columna = -1
    columna_max = []

    for j in range(0,columnas):
        # --- Inicializamos nuestra lista donde guardamos los valores de cada una de las columnas en cada iteracion extrayendo el valor
        columna = [M[i][j] for i in range(filas)]

        # --- Inicializamos la variable que contiene la suma de la columna
        suma_columna = sum(columna)

        if suma_columna > sum_max_col:
            sum_max_col = suma_columna
            num_columna = j
            columna_max = columna  # Guardar la mejor columna
    
    print("La columna cuyos elementos suman el máximo es:", columna_max, "con suma:", sum_max_col)
            



