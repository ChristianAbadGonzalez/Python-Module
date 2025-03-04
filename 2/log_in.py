# --- Crea un script que pida una contraseña al usuario (el script sabe cual es la contraseña correcta). ---
# --- Si la contraseña es correcta el script debe darle la bienvenida al usuario. De lo contrario debe ---
# --- indicarle que la contraseña es incorrecta y darle una segunda oportunidad de introducir la contraseña. ---
# --- Al segundo fallo debe mostrar un mensaje de error y terminar de ejecutarse. Cambia el script para que no distinga entre mayúsculas y minúsculas. ---

passwd = "miContraseña123"

# - Pedimos al usuario que introduzca una contraseña --
contraseña = input("Por favor, introduce tu contraseña: ")

# --- Comprobamos si la contraseña introducida por el usuario es correcta ---
if contraseña == passwd:
    print("Bienvenido al sistema!")
else:
    print("Contraseña incorrecta. Inténtalo de nuevo.")
    # - Pedimos al usuario que introduzca una contraseña --
    contraseña = input("Por favor, introduce tu contraseña: ")
    if contraseña == passwd:
        print("Bienvenido al sistema!")
    else:
        print("Contraseña incorrecta. Has fallado dos veces. Vuelve a intentarlo más tarde.")