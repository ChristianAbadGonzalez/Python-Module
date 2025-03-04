# --- Definimos la operacion ---
operacion = ((3+2)/(2*5))**2
# --- operacion es la combinación de una suma y una multiplicación todo ello elevado al cuadrado ---

# --- Definimos la operacion2 ---
operacion2 = ((3+2) /2 /5) **2
# --- operacion2 es la combinación de una suma y una primera división dividido entre 2 y luego otra división entre 5. Además de estar todo ello elevado al cuadrado ---

# --- Imprimimos el resultado de la operacion ---
print(operacion)

# --- Imprimimos el resultado de la operacion ---
print(operacion2)

# --- Pedimos un numero n por pantalla ---
n = float(input("Introduce un número: "))

# --- Definimos la operacion3 ---
operacion3 = n * (n+1) / 2
# --- operacion3 es la multiplicación de n por n+1 y todo ello dividido entre 2 ---

# --- Imprimimos el resultado de la operacion3 ---
print(operacion3)

# Pedimos al usuario dos números enteros
num1 = int(input("Ingresa un número entero: "))
num2 = int(input("Ingresa un número entero: "))
# --- num1 y num2 son dos números enteros que el usuario introduce por pantalla ---

# Calculamos el cociente y el resto
cociente = num1 // num2
# --- Para calcular el cociente de la división entera de num1 entre num2 debemos de poner el simbolo // ---

resto = num1 % num2
# --- Para calcular el resto de la división entera de num1 entre num2 debemos de poner el simbolo % ---

# Mostramos por pantalla los números de entrada, el cociente y el resto# Mostrar por pantalla numeros de entrada, cociente y resto
print("Los números de entrada son ", num1, " y ", num2)
print("El cociente es ", cociente)
print("El resto es ", resto)