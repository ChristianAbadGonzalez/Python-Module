from abc import ABC, abstractmethod
from typing import Dict


# ABSTRACCIÓN: Servicio de almacenamiento de productos
class AlmacenamientoProductos(ABC):
    @abstractmethod
    def agregar_producto(self, nombre: str, cantidad: int) -> None: pass    # Agrega o actualiza el stock de un producto

    @abstractmethod
    def obtener_stock(self, nombre: str) -> int: pass   # Devuelve la cantidad disponible de un producto

    @abstractmethod
    def retirar_producto(self, nombre: str, cantidad: int) -> None: pass    # Retira una cantidad del stock de un producto


# IMPLEMENTACIÓN DE BAJO NIVEL: almacenamiento en memoria 
class MemoriaAlmacenamientoProductos(AlmacenamientoProductos):  # Implementa la abstracción
    def __init__(self):
        # Diccionario interno: nombre -> cantidad disponible
        self.inventario: dict[str, int] = {}


    def agregar_producto(self, nombre: str, cantidad: int) -> None:
        # Suma cantidades si ya existe; si no, crea la entrada
        # Suma al stock actual o inicializa si no existe
        self._inventario[nombre] = self._inventario.get(nombre, 0) + cantidad


    def obtener_stock(self, nombre: str) -> int:
        # Devuelve 0 si el producto no existe aún
        return self.inventario.get(nombre, 0)
    

    def retirar_producto(self, nombre: str, cantidad: int) -> None:     
        # Verifica que haya suficiente stock antes de retirar
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva")

        stock_actual = self._inventario.get(nombre, 0)
        
        if cantidad > stock_actual:
            raise ValueError("Stock insuficiente")

        # Actualiza el inventario
        self._inventario[nombre] = stock_actual - cantidad


#   MÓDULO DE ALTO NIVEL: lógica de negocio de productos
#   Depende de la abstracción, no de una implementación concreta (DIP)
class GestorProductos:
    def __init__(self, almacenamiento: AlmacenamientoProductos) -> None:
        # Inyección de dependencias por constructor. Permite cambiar la implementación sin tocar esta clase.
        self._almacenamiento = almacenamiento

    
    def agregar(self, nombre: str, cantidad: int) -> None:
        # Caso de uso: agregar stock de un producto. Incluye validación simple de entrada.
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser positiva")
        
        self._almacenamiento.agregar_producto(nombre, cantidad)
        
        # En una app real, preferir logging en lugar de print.
        print(f"Producto '{nombre}' agregado (+{cantidad})")

    
    def stock(self, nombre: str) -> int:
        # Caso de uso: consultar stock de un producto.
        cantidad = self._almacenamiento.obtener_stock(nombre)
        print(f"Stock de '{nombre}': {cantidad}")
        return cantidad


    def retirar(self, nombre: str, cantidad: int) -> None:
        # Caso de uso: retirar stock (por venta, merma, etc.).
        self._almacenamiento.retirar_producto(nombre, cantidad)
        print(f"Producto '{nombre}' retirado (-{cantidad})")


# EJEMPLO DE USO
if __name__ == "__main__":
    # Implementación concreta seleccionada (memoria).
    almacenamiento = MemoriaAlmacenamientoProductos()

    # Inyectamos la dependencia en el gestor (alto nivel).
    gestor = GestorProductos(almacenamiento)

    # Flujo de ejemplo
    gestor.agregar("Camisa", 3)
    gestor.agregar("Pantalón", 10)

    gestor.stock("Camisa")     # → 3
    gestor.stock("Pantalón")   # → 10

    gestor.retirar("Camisa", 1)
    gestor.stock("Camisa")     # → 2