# --- INICIO SCRIPT ---
# --- Importamos la librería getpass para ocultar la contraseña en pantalla ---
import getpass

# Contraseña de autentificación y acceso al sistema es la siguiente --- 
password = "@Cmillan179"

# --- Pedimos al usuario que introduzca su nombre ---
nombre = input("Por favor, introduce tu nombre: ")


# Mostramos por pantalla el nombre del usuario y la solicitud de contraseña
print(f"Hola {nombre.title()}. Por favor, introduce tu contraseña de administrador.")

# Mostramos los requisitos de la contraseña
print("""
La contraseña tiene los siguientes requisitos:
1. La contraseña debe contener entre 10 y 12 caracteres.
2. La contraseña debe contener al menos una letra mayúscula.
3. La contraseña debe contener al menos una letra minúscula.
4. La contraseña debe contener al menos un número.
5. La contraseña debe contener al menos un carácter especial.
""")

# Función para validar la contraseña según los requisitos
def validar_contraseña(contraseña):
    requisitos = []
    
    # Verificación de los requisitos
    # --- Verificación de la longitud de la contraseña ---
    if len(contraseña) < 10 or len(contraseña) > 12:
        requisitos.append("La contraseña debe contener entre 10 y 12 caracteres.")
    
    # --- Verificación de los caracteres de tipo Mayusculas de la contraseña ---
    if not any(c.isupper() for c in contraseña):
        requisitos.append("La contraseña debe tener al menos una letra mayúscula.")
    
    # --- Verificación de los caracteres de tipo Minusculas de la contraseña ---
    if not any(c.islower() for c in contraseña):
        requisitos.append("La contraseña debe tener al menos una letra minúscula.")
    
    # --- Verificación de los caracteres de tipo Numeros de la contraseña ---
    if not any(c.isdigit() for c in contraseña):
        requisitos.append("La contraseña debe tener al menos un número.")
    
    # --- Verificación de los caracteres de tipo Especiales de la contraseña ---
    if not any(c in "!@#$%^&*()-+" for c in contraseña):
        requisitos.append("La contraseña debe tener al menos un carácter especial.")
    

    # Si la contraseña no cumple los requisitos, devolvemos los errores
    if requisitos:
        print("La contraseña no cumple con los requisitos:\n" + "\n".join(requisitos))
        return False
    else:
        return True

# Intentos para ingresar la contraseña correcta
for intento in range(2):
    # Usamos getpass para que la contraseña no se muestre en pantalla
    passwd = getpass.getpass("Por favor, introduce tu contraseña: ")

    # Validamos si la contraseña cumple con los requisitos
    if validar_contraseña(passwd):
        # Si la contraseña es válida, verificamos si coincide con la contraseña correcta
        if passwd == password:
            print(f"✅ Bienvenido! {nombre.title()}. Acceso concedido.")
            break  # Salimos del bucle si la contraseña es correcta
        else:
            print(f"❌ Contraseña incorrecta. {nombre.title()}. Intentalo de nuevo.")
    else:
        print(f"❌ Contraseña no cumple con los requisitos. {nombre.title()}. Inténtalo nuevamente.")
    
else:
    print(f"🚫 {nombre.title()}. Has superado el número de intentos. Acceso denegado.")

# --- FIN SCRIPT ---