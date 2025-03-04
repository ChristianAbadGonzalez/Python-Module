# --- En uno de los cursos se ha dividido a una clase en dos grupos A y B. 
# --- Para mezclar a los alumnos de la forma más equitativa posible se ha asignado a todas las chicas con nombres empezando por la letra E hasta la M en el grupo A y el resto en el B. ---
# --- A los chicos con nombres empezando por la letra A hasta la H y R hasta la Z se les ha asignado al grupo A también, el resto están en el B. ---
# --- Crea un script que pregunte al usuario si es chica o chico y el nombre. El script debe mostrar por ---
# --- pantalla el grupo que le corresponde a ese alumno. ---


# --- Pedir al usuario si es chico o chica y su nombre ---
sexo = input("¿Eres chico o chica? (chico/chica): ")
nombre = input("Introduce tu nombre: ")

# --- Letras para el grupo A ---
chicos_A = "ABCDEFGHRSTUVWXYZ"
chicas_A = "EFGHIJKLM"

# --- Letras para el grupo B ---
chicos_B = "IJKLMNOPQ"
chicas_B = "ABCDNRSTUVWXYZ"

# --- Comprobar si el sexo es chica ---
if sexo.lower() == "chica":
    if nombre[0].upper() in chicas_A:
        print("Perteneces al grupo A")
    else:
        print("Perteneces al grupo B")

# --- Comprobar si el sexo es chico ---
elif sexo.lower() == "chico":
    if nombre[0].upper() in chicos_A:
        print("Perteneces al grupo A")
    else:
        print("Perteneces al grupo B")

# --- Si el sexo no es ni chico ni chica ---    
else:
    print("Sexo no válido")

# --- Fin del script ---
print("Fin del script")
