# --- STRING A LISTA: ---
# --- Desarrolla un script en Python que dado una cadena de caracteres con la siguiente información: ---    
#   --- Nombre ---
#   --- Apellido ---
#   --- DNI ---
#   --- Código_asignatura --
#   --- Convocatoria ---
#   --- Nota1, Nota2, Nota3. ---

# ---El script debe crear una lista con esos datos, introducirlo en una lista de listas donde se encuentra la información de todos los alumnos --- 
# --- e imprimir la nota media de los alumnos junto con el DNI. ---

# --- Definir la cadena de caracteres con la información del alumno ---
cadena = [
    "David Fernandez 12311267A 43527 2 9.1 7.6 2.4", 
    "Maria Garcia 12316487A 43527 2 7.1 8.6 5.4",
    "Juan Perez 647829236A 43527 2 8.1 8.5 8.4"
]

# --- Inicializamos una lista vacia con el fin de obtener una base de datos con los datos de los alumnos ---
base_datos = []

# --- Procesar cada línea de datos ---
for alumno in cadena:
    datos_alumno = alumno.split()  # --- Separar la línea en partes por espacio ---
    nombre = datos_alumno[0]
    apellido = datos_alumno[1]
    dni = datos_alumno[2]
    codigo_asignatura = datos_alumno[3]
    convocatoria = datos_alumno[4]

    # Convertir las notas en una lista de floats
    notas = list(map(float, datos_alumno[5:]))

    # Agregar a la base de datos
    base_datos.append([nombre, apellido, dni, codigo_asignatura, convocatoria, notas])
    
# Calcular e imprimir la nota media junto con el DNI
for alumno in base_datos:
    dni = alumno[2]
    notas = alumno[5]
    nota_media = sum(notas) / len(notas)
    print(f"DNI: {dni} - Nota Media: {nota_media:.2f}")
