# --- BASE DE DATOS DE UN COLEGIO: ---
# --- Trabajas en colegio y estas encargado de mantener un seguimiento de las notas de los estudiantes de un clase. ---
# --- En tu base de datos tienes una lista con los nombres de los estudiantes y para cada estudiante debes guardar sus notas provenientes de deberes, exámenes y proyectos. ---
# --- También necesitas calcular a nota media de cada estudiante y la nota media de la clase al completo. ---

# --- Pista: Para resolver este problema puedes usar una lista anidada donde guardes las notas para cada estudiante. ---
# --- Entonces puedes usar un bucle para recorrer la lista de listas y calcular la nota media de cada estudiante. ---
# --- También puedes usar otro bucle para calcular la nota media de toda la clase. ---

# --- Creamos una lista asociada a los estudiantes con sus respectivas notas almacenadas en una lista vacia para pedirselo al usuario ---
estudiantes = ["Juan", "Maria", "Pedro"]


database = []

# --- Recorremos la base de datos en cuestion que hemos creado ---
# --- Calculamos la nota media de cada alumno asociado a cada estudiante ---
# --- Calculamos la nota media de la clase ---

for estudiante in estudiantes:
    # --- Creamos una lista vacia para almacenar los datos que vamos a pedir al usuario --- 
    notas = []
    print(f"Ingrese las notas de {estudiante}")
    
    # --- PUNTOS POR DEBERES ---
    deberes = float(input("Notas de deberes: "))
    notas.append(deberes)

    # --- PUNTOS POR EXAMENES ---
    examenes = float(input("Notas de examenes: "))
    notas.append(examenes)

    # --- PUNTOS POR PROYECTOS ---
    proyectos = float(input("Notas de proyectos: "))
    notas.append(proyectos)
    
    # añadir a la database el nombre y la lista de notas del alumno
    database.append([estudiante, notas])

# --- database = [["Juan", [6.4,7.0,9.1]], ["María", [8.2, 9.8, 6.5]], ["Pedro", [7.1, 8.4, 5.2]]] 
    
print("  ")
print("  ")
print("Calculando medias individuales y totales...")
print("  ")
print("  ")

# --- Calculamos la nota media de cada estudiante ---
sum_media = 0

for data in database:
    # --- Nombre del estudiante ---
    nombre = data[0]

    # --- Notas del estudiante ---
    notas = data[1]

    # --- Calculamos la suma de las notas del estudiante ---
    suma_notas = 0
    for nota in notas:
        suma_notas = suma_notas + nota
    
    # --- Calculamos la media del estudiante ---
    media = suma_notas / len(notas)
    
    # --- Imprimimos por pantalla la media de cada estudiante aproximandola a 2 decimales ---
    print(f"La media de {nombre} es {media :.2f}")

    # --- Calculamos la suma de todas las medias ---
    sum_media = sum_media + media

# --- Divividmos la suma de todas las medias por el numero de alumnos para obtener la media de toda la clase ---
media_clase = sum_media / len(database)

# --- Imprimimos por pantalla la media de la clase ---
print("La media de la clase es {:.2f}".format(media_clase))
