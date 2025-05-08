# Imagina que eres el gerente de recursos humanos de una empresa y necesitas gestionar la información de los empleados. 
# Cada empleado tiene un nombre, salario y departamento al que pertenece. 
# Implementa un programa en Python que permita agregar nuevos empleados, actualizar el salario de un empleado existente, 
# mostrar la lista completa de empleados y calcular el promedio salarial por departamento.

# Diccionario para almacenar los nombres de los empleados
empleados = {}

# Inicializamos la variable continuar a True para entrar al bucle directamente y permitir al usuario ingresar las ventas de los productos y continuar hasta que el usuario decida salir.
continuar = True

# Iniciamos bucle while para que el usuario pueda elegir entre las opciones del menu
while continuar:
    # Imprimimos por pantalla las opciones disponibles para que el usuario elija
    print("Menu de opciones:")
    print("1. Agregar empleado")
    print("2. Actualizar salario de empleados")
    print("3. Mostrar lista de empleados")
    print("4. Calcular promedio salarial por departamente")
    print("5. Salir")
    opcion = input("Seleccione una opcion: ")

    # Agregar empleado
    if opcion == "1":
        nombre = input("Ingrese nombre del empleado: ")
        salario = float(input("Ingrese salario del empleado: "))
        departamento = input("Ingrese departamento del empleado: ")

        empleados[nombre] = {
            "salario": salario,
            "departamento": departamento
        }

        print("Empleado agregado exitosamente")

    # Actualizar salario empleados
    elif opcion == "2":
        nombre = input("Ingrese el nombre del empleado: ")
        # Comprobamos si el nombre de la persona introducida exsite en nuestro diccionario/base de datos
        if nombre in empleados:
            # Proponemos nuevo salario
            nuevo_salario = float(input("Ingrese el nuevo salario del empleado: "))
            # Actualizamos salario del empleado
            empleados[nombre]["salario"] = nuevo_salario
            print("Salario actualizado exitosamente")
        # Si el empleado no existe en el diccionario/base de datos lo indicamos
        else:
            print("Empleado no encontrado")

    # Mostrar lista de empleados
    elif opcion == "3":
        print("Lista de empleados: ")
        # Recorremos pares clave-valor =  nombre-datos
        for nombre, datos_empleado in empleados.items():
            salario = datos_empleado["salario"] # Extraemos valor del salario
            departamento = datos_empleado["departamento"] # Extraemos departamento
            # Imprimimos informacion
            print(f"Nombre: {nombre}, Salario: {salario}, Departamento: {departamento}")

    # Calcular promedio salarial por departamento
    elif opcion == "4":
        departamento = input("Ingrese el departamento: ")

        # Inicializamos variables
        total_salarios = 0
        contador = 0
        # Recorremos datos de los empleados guardados en los valores del dict
        for datos_empleado in empleados.values():
            # Si el departamento coincide sumamos el salario
            if datos_empleado["departamento"] == departamento:
                total_salarios = total_salarios + datos_empleado["salario"]
                contador = contador + 1

        # Si hay empleados en el departamento calculamos el promedio
        if contador > 0:
            promedio_salario = total_salarios / contador
            print(f"Promedio salarial del departamento {departamento}: {promedio_salario}")
        # Si no hay empleados en el departamento lo indicamos
        else:
            print(f"No hay empleados en el departamento {departamento}")

    elif opcion == "5":
        print("Cerrando programa")
        continuar = False

    else: 
        print("Opcion invalida. Por favor, seleccione una opcion valida.")

# Fin del programa

