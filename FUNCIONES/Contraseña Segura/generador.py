# Importación de módulos
import random
import string

# Generamos un generador de contraseñas
def generar_contrasena(longitud, mayusculas = True, 
                       minusculas = True, 
                       numeros = True, 
                       caracteres_especiales = True):
    
    # Generar una contrasena dada una logitud
    # longitud: numero de caracteres de la contraseña
    # mayusculas: True si la contraseña contiene al menos una mayuscula
    # minusculas: True si la contraseña contiene al menos una minuscula
    # numeros: True si la contraseña contiene al menos un numero
    # caracteres_especiales: True si la contraseña contiene al menos un caracter especial

    caracteres = ""
    if mayusculas:
        # Añadimos las letras mayúsculas
        caracteres += string.ascii_uppercase
        # cacteres += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if minusculas:
        # Añadimos las letras minúsculas
        caracteres += string.ascii_lowercase
        # caracteres += "abcdefghijklmnopqrstuvwxyz"
    
    if numeros:
        # Añadimos los numeros
        caracteres += string.digits
        # caracteres += "0123456789"
    
    if caracteres_especiales:
        # Añadimos los caracteres especiales
        cartacteres += string.punctuation
        # caracteres += "!@#$%^&*()-_=+[]{}|;:,.<>?/`~"
    
    contrasena = "".join(random.choice(caracteres) for i in range(longitud))
    return contrasena