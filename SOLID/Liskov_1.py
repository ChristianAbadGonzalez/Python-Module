# CLASES BASES - METODO DE PAGO
class MetodoPagoBase:
    """
    Clase base que define la interfaz común para todos los métodos de pago.
    Actúa como contrato que todas las subclases deben cumplir.
    """
    
    def procesar_pago(self):
        """Método base que será sobrescrito por las clases hijas."""
        pass


# CLASES INTERMEDIAS - CATEGORIAS DE METODOS DE PAGO
class MetodoPagoAutomatico(MetodoPagoBase):
    """
    Clase intermedia que representa métodos de pago automáticos.
    Hereda de MetodoPagoBase y sirve como categoría para pagos electrónicos.
    """
    
    def procesar_pago(self, cantidad):
        """Método que será implementado por cada tipo de pago automático."""
        pass


class MetodoPagoManual(MetodoPagoBase):
    """
    Clase intermedia que representa métodos de pago manuales.
    Hereda de MetodoPagoBase y sirve como categoría para pagos físicos.
    """
    
    def procesar_pago(self, cantidad):
        """Método que será implementado por cada tipo de pago manual."""
        pass


# CLASES CONCRETAS - METODOS DE PAGO AUTOMATICOS
class PagoTarjeta(MetodoPagoAutomatico):
    """Clase que procesa pagos con tarjeta de crédito/débito."""
    
    def __init__(self, numero_tarjeta):
        self.numero_tarjeta = numero_tarjeta  # Número de la tarjeta

    def procesar_pago(self, cantidad):
        """Implementación específica para pagos con tarjeta."""
        print(f"Procesando pago automático de {cantidad}€ usando tarjeta {self.numero_tarjeta}")


class PagoPayPal(MetodoPagoAutomatico):
    """Clase que procesa pagos mediante PayPal."""
    
    def __init__(self, cuenta_paypal):
        self.cuenta_paypal = cuenta_paypal  # Correo de la cuenta PayPal

    def procesar_pago(self, cantidad):
        """Implementación específica para pagos con PayPal."""
        print(f"Procesando pago automático de {cantidad}€ usando PayPal cuenta {self.cuenta_paypal}")


class PagoBitcoin(MetodoPagoAutomatico):
    """Clase que procesa pagos con criptomoneda Bitcoin."""
    
    def __init__(self, direccion_bitcoin):
        self.direccion_bitcoin = direccion_bitcoin  # Dirección de wallet Bitcoin

    def procesar_pago(self, cantidad):
        """Implementación específica para pagos con Bitcoin."""
        print(f"Procesando pago automático de {cantidad}€ usando Bitcoin {self.direccion_bitcoin}")


# CLASES CONCRETAS - METODOS DE PAGO MANUALES
class PagoCheque(MetodoPagoManual):
    """Clase que procesa pagos mediante cheque físico."""
    
    def __init__(self, numero_cheque):
        self.numero_cheque = numero_cheque  # Número del cheque

    def procesar_pago(self, cantidad):
        """Implementación específica para pagos con cheque."""
        print(f"Procesando pago manual de {cantidad}€ usando cheque {self.numero_cheque}")


# FUNCIONES DE PROCESAMIENTO DE PAGO
def realizar_pago_automatico(metodo_pago: MetodoPagoAutomatico, cantidad):
    """
    Función que procesa pagos automáticos.
    Acepta cualquier objeto que herede de MetodoPagoAutomatico.
    Utiliza polimorfismo: no necesita saber el tipo exacto de pago.
    """
    metodo_pago.procesar_pago(cantidad)


def realizar_pago_manual(metodo_pago: MetodoPagoManual, cantidad):
    """
    Función que procesa pagos manuales.
    Acepta cualquier objeto que herede de MetodoPagoManual.
    Utiliza polimorfismo para delegar el procesamiento.
    """
    metodo_pago.procesar_pago(cantidad)


# EJEMPLOS DE USO
# Instanciamos diferentes métodos de pago con sus datos específicos
pago_tarjeta = PagoTarjeta("123 456 789 123")
pago_paypal = PagoPayPal("mi_cuenta@pago.com")
pago_bitcoin = PagoBitcoin("892173912udfhie938")
pago_cheque = PagoCheque("123456768")

# Procesamos pagos automáticos usando polimorfismo
# Cada objeto usa su propia implementación de procesar_pago()
realizar_pago_automatico(pago_tarjeta, 1000)
realizar_pago_automatico(pago_paypal, 400)
realizar_pago_automatico(pago_bitcoin, 6000)

# Procesamos pago manual
realizar_pago_manual(pago_cheque, 3000)