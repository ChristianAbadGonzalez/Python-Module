# Generamos un validador de contaseñas
def validar_contrasena(contrasena):
    # Esta función valida la contraseña dada como argumento siguiendo 
    # las reglas de seguridad
    
    # Longitud mínima de 8 caracteres
    longitud_minima = 8
    # Longitud máxima de 16 caracteres
    longitud_maxima = 16
    # Al menos una letra mayúscula
    mayuscula = False
    # Al menos una letra minúscula
    minuscula = False
    # Al menos un número
    numero = False
    # Al menos un carácter especial
    caracter_especial = False

    if len(contrasena) < longitud_minima or len(contrasena) > longitud_maxima:
        return False
    
    # Reorremos la contraseña para comprobar si cumple con los requisitos
    for caracter in contrasena:
        if caracter.isupper():
            mayuscula = True
        elif caracter.islower():
            minuscula = True
        elif caracter.isdigit():
            numero = True
        elif caracter in "!@#$%^&*()-_=+[]{}|;:,.<>?/":
            caracter_especial = True
    
    # Comprobamos si cumple con todos los requisitos
    if mayuscula and minuscula and numero and caracter_especial:
        return True
    else:
        return False
    
