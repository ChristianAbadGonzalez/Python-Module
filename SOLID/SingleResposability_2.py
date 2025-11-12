# Definición de la clase Order que representa un pedido con sus artículos y estado
class Order:
    # Constructor que inicializa las listas de artículos y el estado del pedido
    def __init__(self):
        self.items = []        # Lista para almacenar los nombres de los artículos
        self.quantities = []    # Lista para almacenar las cantidades de cada artículo
        self.prices = []       # Lista para almacenar los precios unitarios de cada artículo
        self.status = "open"   # Estado inicial del pedido (abierto)

    # Método para agregar un artículo al pedido con su cantidad y precio
    def add_item(self, name: str, quantity: int, price: float) -> None:
        self.items.append(name)        # Añade el nombre del artículo a la lista
        self.quantities.append(quantity) # Añade la cantidad a la lista
        self.prices.append(price)       # Añade el precio unitario a la lista


# Definición de la clase PaymentProcesor que se encarga de procesar los pagos
class PaymentProcesor:
    # Método que procesa el pago según el tipo de pago especificado
    def pay(self, order: Order, security_code: str, payment_type: str):
        
        # Verifica si el tipo de pago es débito
        if payment_type == "debit":
            print("Processing debit payment type")           # Indica que se está procesando un pago con débito
            print(f"Verifying security code: {security_code}") # Muestra el código de seguridad que se está verificando
            order.status = "paid"                            # Cambia el estado del pedido a "pagado"
        
        # Verifica si el tipo de pago es crédito
        elif payment_type == "credit":
            print("Processing credit payment type")          # Indica que se está procesando un pago con crédito
            print(f"Verifying security code: {security_code}") # Muestra el código de seguridad que se está verificando
            order.status = "paid"                            # Cambia el estado del pedido a "pagado"
        # Si el tipo de pago no es reconocido, lanza una excepción
        else:
            raise Exception(f"Unknown payment type: {payment_type}")


# Definición de la clase CalculateProcesor que se encarga de calcular el precio total del pedido
class CalculateProcesor:
    # Método que calcula el precio total del pedido multiplicando cantidades por precios
    def total_price(self, order: Order):
        total = 0  # Inicializa el total en 0
        # Itera sobre las cantidades y precios simultáneamente usando zip
        for quantity, price in zip(order.quantities, order.prices):
            total += quantity * price  # Suma al total el producto de cantidad por precio
        return total  # Retorna el precio total calculado


# Creación de una instancia de Order (pedido)
order = Order()

# Imprime el estado inicial del pedido (debería mostrar "open")
print(order.status)

# Añade un artículo al pedido: 3 Laptops a 150 cada una
order.add_item("Laptop", 3, 150)

# Artículos comentados que podrían añadirse al pedido
# order.add_item("SSD", 2, 20)
# order.add_item("USB cable", 1, 5)

# Creación de una instancia del procesador de pagos
processor = PaymentProcesor()

# Procesa el pago del pedido usando tarjeta de débito con código de seguridad "12345"
processor.pay(order, "12345", "debit")

# Imprime el estado del pedido después del pago (debería mostrar "paid")
print(order.status)

# Creación de una instancia del calculador de precios
total = CalculateProcesor()

# Calcula e imprime el precio total del pedido (3 * 150 = 450)
print(total.total_price(order))