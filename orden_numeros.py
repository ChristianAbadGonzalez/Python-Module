# --- Pedimos al usuario que introduzca un número
numero = input("Por favor, introduce un número de cuatro cifras ") #string

# --- Mostrar el número componente a componente por pantalla
print(numero[0] + "\n" + numero[1] + "\n" + numero[2] + "\n" + numero[3]) 
# -- Imprime en pantalla los caracteres de la variable numero con salto de línea separando número por número --

# --- Pedimos un numero al usuario ---
numero2 = input("Por favor, introduce un número de cuatro cifras ") #string

# --- Imprimir el numero2 recorriendo el string al revés -- 
print(numero2[::-1]) # --- Imprime el string almacedado en la variable numero2 recorriendo los caracteres desde el inicio hasta el final de forma inversa --

# --- Creamos el strig inverso ---
numero_inverso = numero2[3] + numero2[2] + numero2[1] + numero2[0]

# --- Imprimos el resultado por pantalla
print(numero_inverso)