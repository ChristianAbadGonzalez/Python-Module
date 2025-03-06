# --- Crea un programa que imprima todos los números primos entre el 2 y el 100. 
# --- Un numero primo es un numero positivo y entero mayor que uno que no tiene un divisor positivo y entero que no sea 1 o sí mismo.

# --- Crear un bucle que recorra los números del 2 al 100 ---
for numero in range(2, 101):
    primo = True
    # --- Crear un bucle que recorra los números del 2 al número anterior al número actual ---
    for i in range(2, numero):
        # --- Comprobar si el número actual es divisible por otro número ---
        if numero % i == 0:
            primo = False
            break
    # --- Imprimir el número actual si es primo ---
    if primo:
        print(numero)
