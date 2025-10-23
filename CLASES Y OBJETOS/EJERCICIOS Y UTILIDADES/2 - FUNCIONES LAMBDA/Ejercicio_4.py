# ================================================================ F. LAMBDA - DATOS EMPRESARIALES ================================================================
# =================================================================================================================================================================

# Imagina que trabajas en una empresa internacional con equipos distribuidos en diferentes países. 
# Cada equipo tiene una lista de empleados, representados como diccionarios, con información sobre el nombre, la edad y el rendimiento en proyectos recientes.

# Tu tarea es organizar una lista consolidada de todos los empleados de la empresa. La organización debe seguir ciertas reglas:

#   1. Los empleados se deben ordenar por el rendimiento en proyectos recientes de forma descendente. 
#   2. Para aquellos con el mismo rendimiento, se deben ordenar por edad de forma ascendente. Además, deseas agrupar a los empleados por país para un análisis más efectivo. Utiliza funciones lambda.

# A continuacion un ejemplo de una posible entrada y salida de la solucion:
from itertools import groupby

def ordenar_empleados(empleados):
    empleados_ordenados = sorted(empleados, key = lambda emp: (emp['rendimiento'], -emp['edad']), reverse = True)
    return empleados_ordenados

def agrupar_empleados_por_pais(empleados_ordenados):
    # Agrupamos empleados por pais
    empleados_agrupados = {pais: list(grupo_empleados) for pais, grupo_empleados in groupby(empleados_ordenados, key = lambda emp:emp['pais'])}
    return empleados_agrupados

def mostrar_empleados_agrupados(empleados_agrupados):
    for pais, grupo_empleados in empleados_agrupados.item():
        print(f"\nPais: {pais}")

        for empleados in grupo_empleados:
            print(empleados)

# Ejemplos de uso
empleados = [
    {"nombre": "Juan Pérez", "edad": 30, "pais": "España", "rendimiento": 90},
    {"nombre": "María García", "edad": 28, "pais": "España", "rendimiento": 85},
    {"nombre": "Pedro Rodríguez", "edad": 26, "pais": "Argentina", "rendimiento": 95},
    {"nombre": "Ana Rodríguez", "edad": 32, "pais": "Argentina", "rendimiento": 105},
    {"nombre": "Sofía Gómez", "edad": 29, "pais": "Argentina", "rendimiento": 95},
    {"nombre": "José López", "edad": 32, "pais": "Bolivia", "rendimiento": 80},
    {"nombre": "Ana Sánchez", "edad": 35, "pais": "Bolivia", "rendimiento": 85},

]
empleados_ordenados = ordenar_empleados(empleados)
empleados_agrupados = agrupar_empleados_por_pais(empleados_ordenados)
mostrar_empleados_agrupados(empleados_agrupados)