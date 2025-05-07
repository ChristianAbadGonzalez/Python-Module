# Implementa un programa en Python que permita registrar y mantener un seguimiento de los puntajes de un juego. 
# El programa debe permitir a los jugadores ingresar sus nombres y puntajes, almacenarlos en un diccionario y proporcionar funcionalidades 
# para mostrar el puntaje más alto, el promedio de puntajes y la cantidad total de jugadores. 

# Base de datos con las puntuaciones de los jugadores
registro_puntuacion = {}

# Inicializamos la variable continuar a True para entrar al bucle y permitir que el usuario ingrese los puntajes de los jugadores y continuar hasta que el usuario decida salir.
continuar = True

# Seguimiento de los puntajes de cada jugador
while continuar:
    # Solicitar el nombre del jugador
    nombre_jugador = input("Ingrese el nombre del jugador: ")
    if nombre_jugador.lower() == "salir":
        continuar = False
    else:
        puntuacion = int(input("Ingrese la puntuación del jugador: "))
        registro_puntuacion[nombre_jugador] = puntuacion
        print("Puntuación registrada para el jugador:", nombre_jugador, "es: ", puntuacion)

    # Obtener el puntaje más alto
    jugador_max_alto = max(registro_puntuacion, key = registro_puntuacion.get) # Devuelve el jugador con la puntuación más alta
    puntuacion_max_alto = registro_puntuacion[jugador_max_alto] # Devuelve la puntuación más alta

    print("El jugador con la puntuación más alta es:", jugador_max_alto, "con una puntuación de:", puntuacion_max_alto)

    # Obtener el promedio de puntajes
    total_puntuaciones = sum(registro_puntuacion.values())
    cantidad_jugadores = len(registro_puntuacion)
    promedio_puntuaciones = total_puntuaciones/cantidad_jugadores
    print("El promedio de puntuaciones es: ", promedio_puntuaciones)

    print("La cantidad total de jugadores es: ", cantidad_jugadores)
    