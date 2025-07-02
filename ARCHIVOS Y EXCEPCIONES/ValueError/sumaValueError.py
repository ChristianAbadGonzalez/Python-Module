# Un problema común al solicitar una entrada numérica ocurre cuando las
# personas ingresan texto en lugar de números. Cuando intentas convertir la
# entrada a un entero (int), obtendrás un ValueError. 
# Escribe un programa que solicite dos números. Suma los números y muestra el resultado. 
# Captura el ValueError si alguno de los valores de entrada no es un número e imprime un
# mensaje de error amigable. Prueba tu programa ingresando dos números y
# luego ingresando texto en lugar de un número. Envuelve tu código del en un
# bucle while para que el usuario pueda continuar ingresando números incluso
# si comete un error ingresando texto en lugar de un número.
while True:
    try:
        # Solicitamos al usuario que ingrese dos números
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        resultado = num1 + num2
        print(f"El resultado de sumar los numeros {num1} y {num2} es: {resultado}")
        break # El bucle deja de ejecutarse si la suma es exitosa
    except ValueError: # Capturamos el ValueError si la excepción ocurre
        print("Error, por favor ingresa solamente numeros enteros.")

