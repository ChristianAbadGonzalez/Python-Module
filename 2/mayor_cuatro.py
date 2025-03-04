# --- Crea un script que pida al usuario 4 números diferentes y imprima el mayor de los cuatro por pantalla.

# --- Pedir al usuario 4 números diferentes
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))
num4 = int(input("Introduce el cuarto número: "))


# --- Calcular el mayor de los cuatro números
if num1 > num2 and num1 > num3 and num1 > num4:
    print("El mayor número es: ", num1)
elif num2 > num1 and num2 > num3 and num2 > num4:
    print("El mayor número es: ", num2)
elif num3 > num1 and num3 > num2 and num3 > num4:
    print("El mayor número es: ", num3)
else:
    print("El mayor número es: ", num4)

# --- Imprimir el mayor de los cuatro números por pantalla
