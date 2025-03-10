# --- VALIDAR ACCESO A UN SITIO WEB: ---
# --- Supongamos que eres un administrador de sistemas y necesitas validar el acceso de los usuarios a un sitio web. ---
# --- Crea un script que verifique si el nombre de usuario y la contraseña ingresados son correctos y permita el acceso solo si ambos son correctos. ---

# --- Creamos una lista con los nombre de usuarios ---
nombres_usuario = ["Cmillan179", "Mataperros32", "Deso17"]

# --- Creamos una lista con los nombre de usuarios ---
passwords = ["Cag17041998", "mTp3298", "Okp2025"]

#--- Pedimos al usuario que introduzcan el nombre de usuario ---
usuario = input("Ingrese su nombre de usuario: ")

#--- Pedimos al usuario que introduzcan la contraseña ---
password = input("Ingrese su contaseña: ")

# --- Creamos un boolenano que valide si el usuario y la contraseña son correctos y coinciden con los almacenados ---
credenciales = False

# --- Iterador incializado a 0 para recorrer las listas
i = 0

# --- Usamos un bucle while para recorrer lista de usuarios y contraseñas
while i < len(nombres_usuario):

    # --- Comprobamos si el nombre de usuario y la contraseña introducida por el usuario son correctas ---
    if nombres_usuario[i] == usuario and passwords[i] == password:
        # --- Si son correctos, el booleano inicializado a False lo ponemos como True
        credenciales = True

    # --- Aumentamos en uno el valor del iterador
    i = i + 1

# --- Si el usuario y contaseña son validos damos la bienvenida
if credenciales == True:
    print(f"Acceso autorizado {usuario}. Bienvenido al sistema")
    
# --- Si el usuario y la contrraseña no son valido arrojamos error
else:
    print("Acceso denegado")

