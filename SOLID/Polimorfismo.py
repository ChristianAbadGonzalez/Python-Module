# CLASE BASE (PADRE): FIGURA
class Figura:
    # Método genérico para calcular el área (interfaz común)
    # Usamos 'pass' porque las subclases deben implementar
    # este método de acuerdo con su forma geométrica.
    def area(self):
        pass

# CLASE HIJA: CIRCULO
class Circulo(Figura):
    # Constructor que recibe el radio del círculo
    def __init__(self, radio):
        self.radio = radio  # Atributo que almacena el radio

    # Implementación concreta del método 'area'
    # Fórmula del área del círculo = π * radio²
    def area(self):
        return 3.14 * self.radio**2
    

# CLASE HIJA: CUADRADO
class Cuadrado(Figura):
    # Constructor que recibe el tamaño del lado
    def __init__(self, lado):
        self.lado = lado  # Atributo que almacena la longitud del lado

    # Implementación concreta del método 'area'
    # Fórmula del área del cuadrado = lado²
    def area(self):
        return self.lado**2

# FUNCIÓN GENÉRICA PARA CALCULAR EL ÁREA
# Esta función recibe cualquier objeto que implemente
# el método 'area' (puede ser un Circulo, Cuadrado, etc.)
# No necesita saber de qué tipo exacto de figura se trata.
def calcular_area(figura):
    return figura.area()


# EJEMPLO DE USO
# Creamos una instancia de Circulo con radio 5
circulo = Circulo(5)

# Creamos una instancia de Cuadrado con lado 10
cuadrado = Cuadrado(10)

# Llamamos a la misma función 'calcular_area' con diferentes objetos
# gracias al polimorfismo: ambas clases tienen su propio 'area()'
print(f"Área del círculo: {calcular_area(circulo)}")   # 3.14 * 5² = 78.5
print(f"Área del cuadrado: {calcular_area(cuadrado)}") # 10² = 100
