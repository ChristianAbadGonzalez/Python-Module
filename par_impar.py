# --- Crea un script que dado un número y una potencia compruebe si ese numero elevado a esa potencia es par o impar. ---

# - Pedimos al usuario que introduzca un número --
numero = int(input("Por favor, introduce un número: "))

if numero % 2 == 0:
    
    print("El número " + str(numero) + " es par.")
else:
    print("El número " + str(numero) + " es impar.")

