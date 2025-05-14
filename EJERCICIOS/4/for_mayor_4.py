# --- Pida al usuario 4 numeros y devuelve los numeros introducidos en orden ascendente ---
# --- Para ello puedes usar listas y bucles for ---

# --- Inicializar la lista de números ---
lista_numeros = []

# --- Crear un bucle para ir almacenandolos y añadiendolos a la lista ---
# --- output: lista de cuatro numeros --> [num1, num2, num3, num4] ---
for i in range(4):
    numero = int(input("Introduce un número: "))
    lista_numeros.append(numero)

# --- Ordenar la lista de números de menor a mayor ---
lista_numeros.sort()

# --- Imprimir la lista de números ordenada ---
print("Los números introducidos ordenados de menor a mayor son: ", lista_numeros)

# --- Imprimir el mayor número de la lista ---
print("El mayor número de la lista es: ", max(lista_numeros))