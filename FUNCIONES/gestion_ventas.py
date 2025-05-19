# GESTIÓN DE VENTAS
# Crea un programa que permita gestionar las ventas de una tienda. 
# Utiliza una estructura de datos adecuada para almacenar la información de las ventas (por ejemplo, una lista de diccionarios). 
# Implementa dos funciones, una para agregar el producto vendido con su precio y otro para mostrar las ventas de productos con sus respectivos precios.
# (La base de datos puede tener la forma [{“Producto”: producto1, “Precio”: precio1}, {“Producto”: producto2, “Precio”: precio2}…])

# Definimos la estructura de los datos que vamos a utilizar para almacenar las ventas
ventas = []

# Definición de la función para agregar una venta
def agregar_venta(producto, precio):
    venta = {
        "Producto": producto, 
        "Precio": precio,
    }

    # Añadimos el producto a la lista de ventas
    ventas.append(venta)
    print(f"Venta agregada: {venta} con éxito")

    # Definición de la función para mostras las ventas generadas
    def mostrar_ventas():
        # Compromabamos que la lista de ventas no esté vacía
        if ventas == []:
            print("No hay ventas registradas")
            return False
        # En el caso de que la lista de ventas no esté vacia, mostramos las ventas
        else:
            print("Ventas registradas:")
            for venta in ventas:
                print(f"Producto: {venta["Producto"]}, Precio: {venta["Precio"]}")
            return True
        
# Ejemplos de uso
agregar_venta("Cafe molido 250 grs", "4,50€")
agregar_venta("ColaCao 1Kg", "6€")
agregar_venta("Galletas Maria", "2,50€")