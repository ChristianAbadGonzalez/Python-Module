# 1. Crea una lista llamada “numeros“ que contenga los siguientes numeros enteros: [1,2,3,4,5,6,7,8,9,10]. ---
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 4. INTENTA REHACER LOS PASOS 2 Y 3 CON EL MENOR NUMERO DE LÍNEAS PSOIBLESntenta rehacer los pasos 2 y 3 con el menor número de lineas posible (método de compresión). 
# 2. Crea una nueva lista con los números pares de la lista anterior en orden inverso ---
numeros_pares = [numero for numero in numeros if numero % 2 == 0][::-1]
# --- Crea una lista de numeros pares, ligado a la variable "numero" a cada elemento de la lista "numeros". ---
# --- Si el modulo de "numero" entre 2 es igual a 0 lo añada a la lista "numeros_pares". ---
# --- Invierte el orden de la lista "numeros_pares". ---
print(numeros_pares)

# 3. Escribe un bucle que recorra la lista “numeros“ e imprima el cuadrado de cada numero por consola.
numeros_cuadrados = [(numero**2) for numero in numeros] # --- Para numero en la lista "numeros" imprime el cuadrado de cada numero. ---
print(numeros_cuadrados)


# 5. Usa un método que te devuelva el número más pequeño de la lista e imprímelo por pantalla
numero_menor = min(numeros)
print(numero_menor)

# 6. Haz lo mismo con el número más alto
numero_mayor = max(numeros)
print(numero_mayor)

# 7. Suma todos los elementos de la lista con y sin un bucle.
suma_numeros = sum(numeros)
print(suma_numeros)

# 8. Encuentra el índice correspondiente al número 8 en la lista original y en la lista resultante tras el punto 2.
index_numero8 = numeros.index(8)
print(index_numero8)

index_numero8_inv = numeros_pares.index(8)
print(index_numero8_inv)
