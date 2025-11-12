# Importación de modulos
# ABC (Abstract Base Class) -- y abstractmethod del módulo 'abc' para poder crear clases abstractas.
from abc import ABC, abstractmethod

# Definición de la clase padre abstracta
class Vehiculo(ABC):
    # Definición del método constructor o inicial de la clase padre abstracta.
    def __init__(self, marca, modelo, color):
        # Atributos comunes a todo tipo de vehículo
        self.marca = marca     # Marca del vehículo (ej: Toyota)
        self.modelo = modelo   # Modelo del vehículo (ej: Corolla)
        self.color = color     # Color del vehículo

        # Estado inicial: el vehículo comienza apagado
        self.encendido = False


    # Definición de métodos concretos con utilidades o funciones a realizar.
    def encender(self):
        """Enciende el vehículo y cambia su estado."""
        self.encendido = True
        print("El vehículo está encendido.")

    def apagar(self):
        """Apaga el vehículo y cambia su estado."""
        self.encendido = False
        print("El vehículo está apagado.")


    # Definición de método abstracto que debe ser implementado en las clases hijas.
    @abstractmethod
    def conducir(self):
        """
        Método abstracto que obliga a las clases hijas a implementar su propio
        comportamiento de conducción.
        """
        pass


# Definición de clases derivadas (Hijas) que heredan de la clase (Padre) Vehiculo.
class Automovil(Vehiculo):
    """Clase concreta que representa un automóvil."""

    def __init__(self, marca, modelo, color, tipo_combustible):
        # Llamada al constructor de la clase padre para heredar sus atributos
        super().__init__(marca, modelo, color)

        # Atributo propio del automóvil
        self.tipo_combustible = tipo_combustible  # Ejemplo: Gasolina, Diésel, Eléctrico

    # Implementación concreta del método abstracto 'conducir'
    def conducir(self):
        if self.encendido:
            print(f"Conduciendo el {self.marca} {self.modelo} ({self.color}) - {self.tipo_combustible}.")
        else:
            print("No se puede conducir, el vehículo está apagado.")


# Definición de clases derivadas (Hijas) que heredan de la clase (Padre) Vehiculo.
class Camion(Vehiculo):
    """Clase concreta que representa un camión."""

    def __init__(self, marca, modelo, color, capacidad_carga):
        # Llamada al constructor del padre
        super().__init__(marca, modelo, color)

        # Atributo propio del camión
        self.capacidad_carga = capacidad_carga  # Ejemplo: '2 toneladas', '5000 kg'

    # Implementación concreta del método abstracto 'conducir'
    def conducir(self):
        if self.encendido:
            print(f"Conduciendo el {self.marca} {self.modelo} ({self.color}) - Capacidad de carga: {self.capacidad_carga}.")
        else:
            print("No se puede conducir, el vehículo está apagado.")


# EJEMPLOS DE USO
print("--- Ejemplo con Automóvil ---")

# Creamos una instancia del automóvil (clase concreta)
automovil1 = Automovil("Toyota", "Corolla", "Rojo", "Gasolina")

# Creamos una instancia de camión (otra clase concreta)
camion1 = Camion("Ford", "F-150", "Azul", "2 toneladas")

# Uso de métodos concretos y abstractos implementados
automovil1.encender()  # Heredado de Vehiculo
automovil1.conducir()  # Implementado en Automovil
automovil1.apagar()    # Heredado de Vehiculo

# Si llamáramos a conducir() ahora, sin estar encendido:
# automovil1.conducir()  -> "No se puede conducir, el vehículo está apagado."

print("\n--- Ejemplo con Camión ---")
camion1.encender()
camion1.conducir()
