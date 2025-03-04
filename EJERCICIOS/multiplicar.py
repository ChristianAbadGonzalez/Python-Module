# -- Pide un numero por pantalla e indica si el numero es un múltiplo de 3 o no --

# --- Pedimos al usuario que introduzca un número ---
numero = int(input("Por favor, introduce un número: "))

# --- Comprobamos si el número es múltiplo de 3 ---
if numero % 3 == 0:
    print("El número " + str(numero) + " es múltiplo de 3.")
else:
    print("El número " + str(numero) + " no es múltiplo de 3!")
