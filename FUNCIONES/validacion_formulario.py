# VALIDACIÓN DE FORMULARIO
# Crea un programa que valide un formulario de registro. 
# Crea una función llamada validar_formulario que reciba diferentes campos de un formulario (nombre, correo electrónico y número de teléfono) 
# y verifique si los valores ingresados cumplen con los requisitos especificados, siendo estos:

# 1. Que el nombre tenga una longitud minima de 3 caracteres 
# 2. Que el teléfono este conformado por dígitos y tenga una longitud de 9 caracteres
# 3. Que el email contenga un “@“ y un “.”

# Definicion de la funcion validad_formulario
def validar_formulario(nombre, email, telefono):
    # Validar nombre
    if len(nombre) < 3:
        print("El nombre introducido no es valido")
        return False
    
    # Validar email
    if "@" not in email or "." not in email:
        print("El email introducido no es valido")
        return False

    # Validar teléfono
    if len(telefono) != 9 or not telefono.isdigit():
        print("El telefono introducido no es valido")
        return False
    
    # Si todas y cada una de las validaciones son correctas, esta función devuelve True
    return True

# Datos de entrada:
nombre = input("Introduzca su nombre: ")
email = input("Introduzca su email: ")
telefono = input("Introduzca su telefono: ")

usuario_valido = validar_formulario(nombre, email, telefono)

# Validar usuario
if usuario_valido:
    print("Usuario valido")
else:
    print("Usuario no valido")