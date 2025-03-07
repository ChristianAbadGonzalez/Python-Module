# --- Dado una lista de números enteros, escribe un script en Python que devuelva una nueva lista con los números primos de la lista original. ---
# --- Además, el script debe devolver el número total de números primos encontrados y la suma de los números primos encontrados. ---

# --- Creamos una lista de numeros enteros, una lista asociada a los numeros primos, una varible que contenga el numero total de numeros primo. ---
# --- Y por ultimo, una variable que contenga la suma total de los numero primos. ---

# --- Lista de números aletorios --
numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10]

primos = []

total_primos = 0

suma_primos = 0

for numero in numeros:
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False

    if primo == True:
        primos.append(numero)
        total_primos = total_primos + 1
        suma_primos = suma_primos + numero

# --- Imprimimos los resultados obtenios ---
print("Los números primos son: ", primos)
print("El numero total de primos obtenidos es: ", total_primos)
print("La suma total de los numeros primos es: ", sum(primos))