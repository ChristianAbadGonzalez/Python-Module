
# - Pedimos al usuario que introduzca su nombre --
nombre = input("¿Cual es tu nombre? ")

# - Reformatear nombre encaso de error al introducir un caracter por error --
nombre = nombre.replace(".", "")

# - Creamos un mensaje de bienvenida con el nombre del usuario --
mensaje = "Hola " + nombre.title() + " Bienvenido al mundo de Python!"

# - Imprimimos el mensaje --
print(mensaje)