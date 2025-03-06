# --- Análisis de precio de productos ---

# --- Escribe un programa en Python que analice una lista de precios de productos y determine el precio más alto, 
# --- el precio más bajo y el precio promedio de todos los productos. 

# --- Para ello, soluciona el ejercicio sin usar las funciones de min() y max() de Python.

# --- Inicializar la lista de precios de productos ---
lista_precios = []

# --- Inicilizar la variable de control precio_total ---
precio_total = 0

# --- Inicilizar la variable de control precio_mayor ---
precio_mayor = 0.0

# --- Inicilizar la variable de control precio_menor ---
precio_menor = 0.0

# --- Crear un bucle para ir almacenandolos y añadiendolos a la lista ---
# --- output: lista de precios de productos --> [precio1, precio2, precio3, precio4] ---

for i in range(4):
    precio = float(input("Introduce el precio de un producto: "))
    lista_precios.append(precio)

    # --- Calcular el precio total ---
    precio_total += precio

    # --- Calcular el precio mayor ---
    if precio > precio_mayor:
        precio_mayor = precio
    else:
        precio_menor = precio

# --- Calcular el precio promedio ---
precio_promedio = precio_total / len(lista_precios)

# --- Imprimir el precio promedio de la lista ---
print("El precio promedio de la lista es: ", precio_promedio)

# --- Imprimir el precio mayor de la lista ---
print("El precio mayor de la lista es: ", precio_mayor)

# --- Imprimir el precio menor de la lista ---
print("El precio menor de la lista es: ", precio_menor)

# --- FIN SCRIPT ---