# --- Crea un script que dado un usuario le de la bienvenida personalizada si es administrador y una bienvenida genérica si es otra persona ---

# - Pedimos al usuario que introduzca su nombre --
nombre = input("Por favor, introduce tu nombre: ")

administrador = "christian"

# --- Comprobamos si el nombre introducido es administrador ---
if nombre == administrador: # --- case insensitive ---
    print("Hola " + nombre.title() + " Bienvenido al sistema!")
else:
    print("Bienvenido al sistema! " + nombre.title())

