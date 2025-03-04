# Importamos el módulo getpass para cifrar la contraseña del usuario
import getpass

# --- Pedimos al usuario que introduzca una contraseña segura con la caracterización requerida por el sistema ---
# --- Requisitos de seguridad: ---
# --- 1. La contraseña debe tener al menos 8 caracteres ---
# --- 2. La contraseña debe tener al menos una letra mayúscula ---
# --- 3. La contraseña debe tener al menos una letra minúscula ---
# --- 4. La contraseña debe tener al menos un número ---
# --- 5. La contraseña debe tener al menos un carácter especial ---
print("La contraseña debe de cumplir los siguientes requisitos: " + "\n"
      "1. La contraseña debe tener al menos 8 caracteres \n"
      "2. La contraseña debe tener al menos una letra mayúscula \n"
      "3. La contraseña debe tener al menos una letra minúscula \n"
      "4. La contraseña debe tener al menos un número \n"
      "5. La contraseña debe tener al menos un carácter especial \n")

def validar_contraseña(contraseña):
    requisitos = []
    
    if len(contraseña) < 8:
        requisitos.append("La contraseña debe tener al menos 8 caracteres.")
    
    if not any(c.isupper() for c in contraseña):
        requisitos.append("La contraseña debe tener al menos una letra mayúscula.")
    
    if not any(c.islower() for c in contraseña):
        requisitos.append("La contraseña debe tener al menos una letra minúscula.")
    
    if not any(c.isdigit() for c in contraseña):
        requisitos.append("La contraseña debe tener al menos un número.")
    
    if not any(c in "!@#$%^&*()-+" for c in contraseña):
        requisitos.append("La contraseña debe tener al menos un carácter especial.")
    
    if requisitos:
        print("La contraseña debe cumplir los siguientes requisitos:\n" + "\n".join(requisitos))
    else:
        print("La contraseña es válida.")

passwd = getpass.getpass("Por favor, introduce tu contraseña: ")

validar_contraseña(passwd)
# --- Fin del script ---

