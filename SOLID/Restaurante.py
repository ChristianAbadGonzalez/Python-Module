# CLASE RESTAURANTE
class Restaurante:

    # Constructor que inicializa el nombre del restaurante
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del restaurante

    # Método que maneja TODOS los tipos de pedidos -- Problema: este método tiene demasiadas responsabilidades
    def realizar_pedido(self, tipo_pedido, detalles):

        # Verifica si el pedido es para llevar
        if tipo_pedido == "para_llevar": 
            # Lógica para manejar pedidos para llevar
            print(f"Procesando pedido para llevar: {detalles}")
        
        # Verifica si el pedido es para comer en el local
        elif tipo_pedido == "comer_en_local":
            # Lógica para manejar pedidos para comer en el local
            print(f"Procesando pedido para comer en el local: {detalles}")
        
        # Verifica si el pedido es de entrega a domicilio
        elif tipo_pedido == "entrega_a_domicilio":
            # Lógica para manejar pedidos de entrega a domicilio
            print(f"Procesando pedido de entrega a domicilio: {detalles}")
        
        # Si el tipo de pedido no es reconocido
        else:
            print("Tipo de pedido no válido")


# EJEMPLO DE USO

# Creamos una instancia del restaurante
restaurante = Restaurante("La Buena Mesa")

# Realizamos diferentes tipos de pedidos
restaurante.realizar_pedido("para_llevar", "2 pizzas")
restaurante.realizar_pedido("comer_en_local", "1 menú del día")
restaurante.realizar_pedido("entrega_a_domicilio", "3 hamburguesas")
restaurante.realizar_pedido("delivery", "Ensalada")  # ERROR: Tipo no válido