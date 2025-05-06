# Eres un gerente de proyectos y necesitas un programa para administrar las tareas y responsabilidades de tu equipo. 
# Cada tarea tiene un nombre, una descripción y un responsable asignado. 
# Implementa un programa en Python que utilice un diccionario para almacenar la información de las tareas. 
# El programa debe permitir agregar nuevas tareas, asignar responsables a las tareas existentes, 
# actualizar las descripciones de las tareas y mostrar la lista completa de tareas y responsables. 

# Diccionario para almacenar las tareas
tareas = {}

# Agregar nuevas tareas
tareas["Tarea1"] = {"descripcion": "Desarrollar la interfaz de usuario", "respondable": "Juan"}
tareas["Tarea2"] = {"descripcion": "Implementar la lógica de negocio", "respondable": "Maria"}
tareas["Tarea3"] = {"descripcion": "Realizar pruebas de integración", "respondable": "Pedro"}
tareas["Tarea4"] = {"descripcion": "Desplegar la aplicación en producción", "respondable": "Ana"}

print("Tareas diarias: " + tareas)

# Asignar un nuevo responsable a las tareas existentes
tareas["Tarea1"]["responsable"] = "Elena"
tareas["Tarea3"]["responsable"] = "Maria"

# Actualizar las descripciones de las tareas
tareas["Tarea2"]["descripcion"] = "Realizar test de hiperparametros"

# Mostrar la lista de tareas y responsables
print("Lista de Tareas y Responsables:")
for tarea, detalles in tareas.items():
    print("Tarea", tarea)
    print("Descripcion:", detalles["descripcion"])
    print("Responsable:", detalles["responsable"])
    print()

# Fin del programa