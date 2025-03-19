# --- Supongamos que tienes un conjunto de calificaciones de un grupo de estudiantes en un curso. ---
# --- Cada estudiante tiene cuatro calificaciones: dos exámenes, un trabajo final y una participación en clase. ---
# --- Quieres calcular la nota final de cada estudiante, donde los exámenes valen un 30% cada uno, ---
# --- el trabajo final vale un 30% y la participación en clase vale un 10%. ---
# --- Para ello, puedes usar NumPy para crear un array de 4 columnas y n filas, donde n es el número de estudiantes. ---
# --- Cada columna representa una de las calificaciones y cada fila representa un estudiante. ---
# --- Luego, puedes usar operaciones de NumPy para calcular la nota final de cada estudiante y almacenarla en un nuevo array de una sola columna. ---

# --- Importación de módulos --- 
import numpy as np

# --- Solicitar al usuario que introduzca el numero de alumnos que tiene en la clase == tamaño del array a formar ---
alumnos = int(input("Por favor. Introduzca el número de alumnos que tiene en clase: "))

# calificaciones = np.array([[nota_examen_1(30%), nota_examen_2(30%), trabajo_final(30%), actitud(10%)]])

calificaciones = []

for alumno in range(alumnos):
    print(f"Ingrese las calificaciones para el estudiante {alumno + 1}")
    
    nota_examen_1 = float(input(f"Nota del examen 1 (30%): "))
    nota_examen_1 = (nota_examen_1 * 0.3)
    
    nota_examen_2 = float(input(f"Nota del examen 2 (30%): "))
    nota_examen_2 = (nota_examen_2 * 0.3)

    trabajo_final = float(input(f"Trabajo Final (30%): "))
    trabajo_final = (trabajo_final * 0.3)

    participacion = float(input(f"Participación en clase (10%): "))
    participacion = (participacion * 0.1)

    nota_final = nota_examen_1 + nota_examen_2 + trabajo_final + participacion

    # --- Agregamos las calificaciones de los estudiante al array ---
    calificaciones.append([nota_examen_1, nota_examen_2, trabajo_final, participacion, nota_final])

# --- Conformamos el array mediante el modulo de NumPy
calificaciones = np.array(calificaciones)

# Obtener las calificaciones por cada categoría
nota_examen_1 = calificaciones[:, 0]
nota_examen_2 = calificaciones[:, 1]
trabajo_final = calificaciones[:, 2]
participacion = calificaciones[:, 3]
nota_final = calificaciones[:, 4]

# Mostrar las notas finales
print("Notas finales de los estudiantes: ")

for i in range(alumnos):
    print(f"Estudiante {i + 1}: {nota_final[i]:.2f}")
