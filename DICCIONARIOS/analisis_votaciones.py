# Supongamos que tienes los resultados de una elección con los nombres de los candidatos y la cantidad de votos obtenidos por cada uno.
# Implementa un programa en Python que permita registrar los votos, mostrar la lista completa de candidatos y sus votos, 
# encontrar al candidato ganador (con más votos) y calcular el porcentaje de votos que obtuvo cada candidato.

# Diccionario para almacenar los votos de los candidatos
resultados = {}

# Inicializamos la variable continuar a True para entrar al bucle directamente y permitir al usuario ingresar las ventas de los productos y continuar hasta que el usuario decida salir.
continuar = True

# Iniciamos bucle while para que el usuario pueda elegir entre las opciones del menu
while continuar:
    # Imprimimos por pantalla las opciones disponibles para que el usuario elija
    print("Menu de opciones:")
    print("1. Registrar voto")
    print("2. Mostrar lista de candidatos y votos")
    print("3. Encontrar candidato ganador")
    print("4. Calcular porcentaje de votos")
    print("5. Salir")
    opcion = input("Seleccione un opción: ")

    # Resgistrar voto
    if opcion == "1":
        # Pedimos al usuario que introduzca el nombre del candidato
        candidato = input("Ingrese nombre del candidato: ")
        # Comprobamos si el candidato esta en la base de datos
        if candidato in resultados:
            # Si el candidato se encuentra en la base de datos le sumamos un voto
            resultados[candidato] = resultados[candidato] + 1
        # Si no esta en la base de datos añadimos par clave valor
        else:
            # añadimos voto
            resultados[candidato] = 1

        print("Voto registrado satisfactoriamente")
    
    # Mostrar lista de candidatos y votos
    elif opcion == "2":
        print("Lista de candidatos y votos: ")
        # Recorremos la base de datos obteniendo pares clave-valor
        for candidato, votos in resultados.items():
            # Imprimimos pares clave-valor candidatos-votos
            print(f"Candidato: {candidato}, Votos: {votos}")

    # Encontrar candidato ganador
    elif opcion == "3":
        # Comprobamos si hay candidatos registrados
        if len(resultados) == 0:
            print("No hay candidatos registrados.")

        # Si hay votaciones registadas, procedemos a encontrar al candidato con mayor numero de votos
        else:
            # Extraemos la clave asociada al numero de votos mas alto
            ganador = max(resultados, key = resultados.get) # key = resultados.get indica que queremos el valor maximo de la clave
            # Imprimimos el nombre del candidato ganador
            print(f"El candidato ganador es: {ganador}")

    # Calcular el porcentaje de votos
    elif opcion == "4":
        total_votos = sum(resultados.values())
        print("Porcentaje de votos por candidato")
        for candidato, votos in resultados.items():
            porcentaje = (votos/total_votos) * 100
            print(f"Candidato: {candidato}, Porcentaje de votos {porcentaje:.2f}%")

    # Cerrar script
    elif opcion == "5":
        print("Cerrando votaciones")
        continuar = False

    # Indicar que la opcion no es valida
    else:
        print("Opcion invalida. Por favor, seleccione una opcion valida.")

# Fin del script