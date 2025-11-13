# Clase base (padre) que define la interfaz común para figuras
class Figura:
    # Método que deberán implementar las subclases
    def obtener_area(self):
        pass


# Subclase Rectangulo que hereda de Figura
class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho  # Base del rectángulo
        self.alto = alto    # Altura del rectángulo

    # Implementación concreta del cálculo de área
    def obtener_area(self):
        return self.ancho * self.alto

    # Setters para modificar dimensiones
    def set_ancho(self, ancho):
        self.ancho = ancho

    def set_alto(self, alto):
        self.alto = alto


# Subclase Cuadrado que hereda de Figura
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado  # Longitud de un lado

    # Setter para modificar el lado
    def set_lado(self, lado):
        self.lado = lado

    # Implementación concreta del cálculo de área
    def obtener_area(self):
        return self.lado * self.lado


# Función polimórfica: acepta cualquier objeto que implemente obtener_area()
def imprimir_area(figura: Figura):
    print(f"Area:{figura.obtener_area()}")


# EJEMPLOS DE USO

rectangulo = Rectangulo(4, 5)
cuadrado = Cuadrado(4)

imprimir_area(rectangulo)  # 4 * 5 = 20
imprimir_area(cuadrado)    # 4 * 4 = 16

# Modificamos dimensiones del rectángulo y recalculamos
rectangulo.set_alto(6)     # alto = 6
rectangulo.set_ancho(7)    # ancho = 7
imprimir_area(rectangulo)  # 7 * 6 = 42

# Modificamos el lado del cuadrado y recalculamos
cuadrado.set_lado(2)       # lado = 2
imprimir_area(cuadrado)    # 2 * 2 = 4