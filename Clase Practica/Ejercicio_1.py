# --- Escribe un programa que pida al usuario un número entero y muestre por pantalla una estructura como la de más abajo, ---
# --- donde el valor de entrada es el número de estrellas en el centro de la estructura. ---
"""
*
**
***
****
*****
****
***
**
*
"""
# --- Pedir al usuario un número entero ---
num = int(input("Introduce un número entero: "))

# --- Crear un bucle para imprimir la estructura ---
# --- Bucle ascenmente para imprimir las estrellas ---
for i in range(1, num + 1):
    print("*" * i + " " * (num - i))

# --- Bucle descendentemente para imprimir las estrellas ---
for i in range(num - 1, 0, -1):
    print("*" * i + " " * (num - i))
# --- FIN SCRIPT ---