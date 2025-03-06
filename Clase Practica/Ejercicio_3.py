# --- Crea un script que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última. ---

# --- Pedir al usuario que introduzca su nombre ---
nombre = input("Introduce tu nombre: ")

# --- Pedir al usuario que introduzca una palabra ---
palabra = input("Introduce una palabra: ")  

# --- Calculamos la longitud de la palabra introducida por el usuario ---
longitud = len(palabra)

# --- Crear un bucle para imprimir las letras de la palabra introducida recorriendo cada letra de la palabra introducida de forma invertida ---
for i in range(longitud - 1, -1, -1):
    print(palabra[i])

# --- FIN SCRIPT ---