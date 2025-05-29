# Implementa una función recursiva llamada factorial que calcule el factorial de un número entero positivo. 
# El factorial de un número n se define como el producto de todos los números enteros positivos desde 1 hasta n. 
# (El factorial de 0 y de 1 es igual a 1)

# Definimos la función factorial que calcula el número factorial de manera recursiva.
# Calcula el factorial de un número entero positivo n de manera recursiva.

# Solicitamos al usuario que introduzca un valor númerico entero positivo.
n = int(input("Introduce un valor númerico entero positivo: "))

def factorial(n):
    # Planteamos el caso base: si n es 0 o 1. El factorial de dicho valor es 1.
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
# Llamamos a la función factorial con un 
numero_factorial = factorial(n)

# Imprimimos el resultado del numero factorial.
print(f"El numero factorial es: {numero_factorial}")

