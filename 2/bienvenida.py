# --- Crea un script que pida el nombre de usuario y le de una bienvenida personalizada. ---
# --- Crea un script de tal manera que si el usuario no es ninguno de los tres se le dé un saludo genérico. ---


# - Pedimos al usuario que introduzca su nombre --
nombre = input("Por favor, introduce tu nombre: ")

# --- Introducción de error en el nombre del usuario ---
nombre = nombre.replace(".", "")
nombre = nombre.replace("#", "")
nombre = nombre.replace("!", "")
nombre = nombre.replace("?", "")
nombre = nombre.replace(";", "")
nombre = nombre.replace(",", "")
nombre = nombre.replace(":", "")

# --- Almacenamos los nombres de los administradores mediante usuario predefinidos ---
usuario_1 = "christian"
usuario_2 = "naomi"
usuario_3 = "sergio"

if nombre == usuario_1 or nombre == usuario_2 or nombre == usuario_3:
    print("Hola " + nombre.title() + ". Bienvenido al sistema!")

else:
    print("Bienvenido al sistema! " + nombre.title() + ", eres un usuario invitado.")