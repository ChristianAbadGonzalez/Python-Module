# =========================== TIENDA ONLINE ===========================
# =======================================================================
# Crea una clase "Producto" con atributos como nombre, precio y cantidad en stock. 
# Luego, crea una clase "Tienda" que contenga una lista de productos disponibles y 
# métodos para agregar productos, mostrar el inventario y realizar una compra.

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - {self.precio} € (Stock: {self.cantidad})"


class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado con éxito.")

    def mostrar_inventario(self):
        print("\n=== INVENTARIO DISPONIBLE ===")
        if not self.productos:
            print("No hay productos disponibles.")
        else:
            for indice, producto in enumerate(self.productos, start=1):
                print(f"{indice}. {producto}")

    def realizar_compra(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre.lower() == nombre_producto.lower():
                if producto.cantidad >= cantidad:
                    total = producto.precio * cantidad
                    producto.cantidad -= cantidad
                    print(f"Compra realizada: {cantidad} x {producto.nombre} = {total} €")
                    print(f"Stock restante: {producto.cantidad}")
                    return
                else:
                    print("No hay suficiente stock disponible.")
                    return
        print("Producto no encontrado en la tienda.")


# ====== Ejemplo de uso ======
tienda = Tienda()

# Agregar productos
p1 = Producto("Portátil", 800, 5)
p2 = Producto("Auriculares", 50, 10)
p3 = Producto("Ratón inalámbrico", 25, 8)

tienda.agregar_producto(p1)
tienda.agregar_producto(p2)
tienda.agregar_producto(p3)

# Mostrar inventario
tienda.mostrar_inventario()

# Realizar compras
tienda.realizar_compra("Portátil", 2)
tienda.realizar_compra("Auriculares", 15)  # no hay suficiente stock
tienda.realizar_compra("Tablet", 1)        # producto no existe

# Mostrar inventario actualizado
tienda.mostrar_inventario()