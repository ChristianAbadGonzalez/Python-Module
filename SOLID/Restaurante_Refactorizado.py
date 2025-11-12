# Importamos ABC (Abstract Base Class) y abstractmethod para crear clases abstractas
from abc import ABC, abstractmethod

# CLASE ABSTRACTA (MAESTRA): ManejadorPedidos
class ManejadorPedidos(ABC):
    # Clase abstracta que define la interfaz común para todos los tipos de pedidos.
    # Obliga a las clases hijas a implementar el método 'procesar_pedido'.
        
    @abstractmethod
    def procesar_pedido(self, detalles): # Método abstracto que debe ser implementado por cada tipo de pedido.
        pass

# CLASES CONCRETAS HIJAS
class PedidoParaLlevar(ManejadorPedidos):
    """Clase que maneja pedidos para llevar."""
    
    def procesar_pedido(self, detalles):
        # Implementación específica para pedidos para llevar
        print(f"Procesando pedido para llevar: {detalles}")


class PedidoLocal(ManejadorPedidos):
    """Clase que maneja pedidos para comer en el local."""
    
    def procesar_pedido(self, detalles):
        # Implementación específica para pedidos en el local
        print(f"Procesando pedido para comer en el local: {detalles}")


class PedidoEntregaADomicilio(ManejadorPedidos):
    """Clase que maneja pedidos de entrega a domicilio."""
    
    def procesar_pedido(self, detalles):
        # Implementación específica para entregas a domicilio
        print(f"Procesando pedido para entrega a domicilio: {detalles}")


class PedidoEspecial(ManejadorPedidos):
    """Clase que maneja pedidos especiales (eventos, catering, etc.)."""
    
    def procesar_pedido(self, detalles):
        # Implementación específica para pedidos especiales
        print(f"Procesando pedido para evento especial: {detalles}")


# CLASE RESTAURANTE
class Restaurante:
    """
    Clase que representa un restaurante y gestiona los pedidos.
    Utiliza composición y polimorfismo para delegar el procesamiento
    de pedidos a las clases especializadas.
    """
    
    def __init__(self, nombre) -> None:
        self.nombre = nombre  # Nombre del restaurante
        # Lista para almacenar los tipos de pedidos registrados (manejadores)
        self.manejadores_pedido = []

    def registrar_pedidos(self, tipo_pedido):
        """
        Registra un tipo de pedido (manejador) en el restaurante.
        Esto permite tener un catálogo de tipos de pedidos disponibles.
        """
        self.manejadores_pedido.append(tipo_pedido)

    def realizar_pedido(self, tipo_pedido, detalles):
        """
        Procesa un pedido delegando la responsabilidad al manejador correspondiente.
        Utiliza polimorfismo: no necesita saber qué tipo específico de pedido es,
        solo llama al método 'procesar_pedido' que cada clase implementa.
        """
        tipo_pedido.procesar_pedido(detalles)


# EJEMPLO DE USO

# Creamos una instancia del restaurante
restaurante = Restaurante("Mi restaurante de pastas")

# Registramos los tipos de pedidos disponibles en el restaurante
restaurante.registrar_pedidos(PedidoParaLlevar())
restaurante.registrar_pedidos(PedidoEspecial())

# Realizamos pedidos específicos usando polimorfismo
# Cada tipo de pedido procesa la solicitud de forma diferente
restaurante.realizar_pedido(PedidoParaLlevar(), "Plato de pasta grande")
restaurante.realizar_pedido(PedidoEspecial(), "Plato especial de mariscos")