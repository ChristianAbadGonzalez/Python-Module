# --- Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error. ---

# - Pedimos al usuario que introduzca dos números --
numero_1 = float(input("Por favor, introduce un número: "))
numero_2 = float(input("Por favor, introduce otro número: "))

# --- Comprobar si el divisor es cero ---
if numero_2 == 0:
    # - Si el divisor es cero, mostrar un mensaje de error --
    print("Error. El divisor no puede ser cero.")
else:
    # - Almacenamos el resultado de la división en una variable --
    division = numero_1 / numero_2
    # - Si el divisor no es cero, mostrar el resultado de la división --
    print("La división de " + str(numero_1) + " entre " + str(numero_2) + " es igual a: " + str(division))



