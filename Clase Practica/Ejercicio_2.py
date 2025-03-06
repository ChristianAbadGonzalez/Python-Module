# --- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, ---
# --- pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta. ---

# --- Pedir al usuario que introduzca su nombre ---
nombre = input("Introduce tu nombre: ")

# --- Informamos al usuario de que para acceder a la aplicación debe introducir la contraseña correcta ---
print(f"Hola {nombre}, para acceder a la aplicación debes introducir la contraseña correcta.")

# --- Inicializar la variable de control de acceso ---
contraseña = "@Cmillan179"

passwd = ""

# --- Inicializamos un bucle while para preguntar al usuari por la contraseña ---
# --- Dicho bucle se va a repetir hasta que el usuario introduzca la contraseña correcta ---
while passwd != contraseña:
    passwd = input("Introduce la contraseña correcta: ")
    if passwd != contraseña:
        print(f"{nombre} La contraseña introducida es incorrecta. Por favor, inténtalo de nuevo.")
    else:
        print(f"{nombre} La contraseña introducida es correcta. Bienvenido al sistema.")
        break
# --- FIN SCRIPT ---