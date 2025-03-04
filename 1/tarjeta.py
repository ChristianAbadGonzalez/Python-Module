# --- Pedir al usuario que ingrese el número de trajeta
num_tarjeta = input("Ingresa tu número de tarjeta ") # -- Solicita al usuario que introduzca el número de tarjeta por pantalla --

# --- Determinar la longitud del numero de la tarjeta de credito
longitud = len(num_tarjeta) # -- Determina la longitud del número de tarjeta introducida por el usuario --

# -- Imprime por pantalla el número de tarjeta ocultando los primeros dígitos y mostrando los últimos 4 dígitos --
# -- El número de dígitos a ocultar es igual a la longitud del número de tarjeta menos 4 --
# -- Se imprimen tantos asteriscos como dígitos se ocultan y se concatenan los últimos 4 dígitos --
print("*" * (longitud-4) + num_tarjeta[longitud-4:longitud]) 