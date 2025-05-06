
# Tienes una tienda y deseas realizar un seguimiento de las ventas diarias de tus productos. 
# Cada producto tiene un nombre y una cantidad vendida. 
# Implementa un programa en Python que utilice un diccionario para almacenar la información de las ventas. 
# El programa debe permitir registrar las ventas de productos, actualizar la cantidad vendida de un producto existente y calcular el total de ventas diarias.

# Diccionario para almacenar las ventas
ventas = {}

# Registro de ventas produccidas
ventas["Producto1"] = 10
ventas["Producto2"] = 5
ventas["Producto3"] = 8
ventas["Producto4"] = 12

# Actualizar la cantidad vendida de un producto existente
ventas["Producto1"] += 5
ventas["Producto2"] += 2
ventas["Producto3"] += 3
ventas["Producto4"] += 4

# Calcular el total de ventas ejecutadas
total_ventas = sum(ventas.values())

# Imprimir el total de ventas
print("El total de ventas realizadas en el día de hoy es: ", total_ventas)

for producto, cantidad in ventas.items():
    print(producto + ": " + str(cantidad))