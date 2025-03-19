# --- Supongamos que tienes un conjunto de datos de ventas de una tienda durante un año. ---
# --- Cada fila representa una venta y tiene tres columnas: la fecha de la venta, el monto de la venta 
# --- y la categoría de producto vendido (por ejemplo, electrónicos, ropa, alimentos, etc.). ---
# --- Quieres analizar estos datos para determinar cuánto fue el monto total de ventas en cada mes. ---
# --- Para ello, puedes usar NumPy para cargar los datos en un array de 3 columnas y n filas, donde n es el número de ventas. ---
# --- Luego, puedes usar operaciones de NumPy para filtrar los datos por mes y sumar los montos de venta correspondientes. ---

import numpy as np

# Lista para almacenar los datos de las ventas
ventas = []

# Número de registros que el usuario quiere ingresar
numero_ventas = int(input("Ingrese el número de ventas que desea registrar: "))

for i in range(numero_ventas):
    print(f"\nRegistro de la venta {i + 1}:")

    fecha = input("Ingrese la fecha de la venta (YYYY-MM-DD): ")
    cantidad = int(input("Ingrese la cantidad de productos vendidos: "))
    precio_unitario = float(input("Ingrese el precio unitario del producto (€): "))
    categoria = input("Ingrese la categoría del producto (Alimentos, Electrónicos, Ropa, etc.): ")

    # Calcular el monto total de la venta
    monto_total = cantidad * precio_unitario

    # Almacenar la venta
    ventas.append([fecha, monto_total, categoria])

# Convertir la lista en un array de NumPy
ventas = np.array(ventas)

# Extraer los meses de las fechas
meses = np.array([int(fecha[5:7]) for fecha in ventas[:, 0]])

# Convertir la columna de montos a float
montos = ventas[:, 1].astype(float)

# Crear un array para almacenar las sumas de ventas por mes
montos_mes = np.zeros(12)

# Sumar los montos por cada mes
for mes in range(1, 13):
    montos_mes[mes - 1] = montos[meses == mes].sum()

# Mostrar resultados
print("\nVentas por mes:")
for mes in range(12):
    print(f"Mes {mes + 1}: {montos_mes[mes]:.2f}€")
