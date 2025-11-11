# Importación de modulos
# ABC (Abstract Base Class) -- y abstractmethod del módulo 'abc' para poder crear clases abstractas.
from abc import ABC, abstractmethod

# Definición de la clase padre abstracta
class Vehiculo(ABC):
    # Definición del método constructor o inicial de la clase padre abstracta.
    def __init__(self, marca, modelo, color):
    # Atributos (variables) comunes a todos los vehículos.
        self.marca = marca
        self.modelo = modelo
        self.color = color

        # Definimos un estado inicial. Todo vehículo empieza apagado.
        self.encendido = False


    # Definición de métodos concretos con utilidades o funciones a realizar.
    def encender(self):
        # Cambia el estado del atributo 'encendido' a True.
        self.encendido = True
        print("El vehículo está encendido.")


    def apagar(self):
        # Cambia el estado del atributo 'encendido' a False.
        self.encendido = False
        print("El vehículo está apagado.")


    # Definición de método abstracto que debe ser implementado en las clases hijas.
    @abstractmethod
    def conducir(self):
        pass


# Definición de clases derivadas (Hijas) que heredan de la clase (Padre) Vehiculo.
class Automovil(Vehiculo):
    # Definición del método constructor o inicial de la clase hija
    def __init__(self, marca, modelo, color, tipo_combustible):
        # Llamada del metodo constructor de la clase (PADRE) haciendo uso de super() 
        # haciendo uso de la herecia de los atributos comunes (marca, modelo, color, encendido). 
        super().__init__(marca, modelo, color)

        # Añadimos el atributo que es específico solo de Automovil
        self.tipo_combustible = tipo_combustible


    # Definición del método abstracto heredado de la clase Padre Vehiculo
    def conducir(self):
        if self.encendido:
            print(f"Conduciendo el {self.marca} {self.modelo} - {self.tipo_combustible}.")
        else:
            print("No se puede conducir, el vehículo está apagado.")


# Definición de clases derivadas (Hijas) que heredan de la clase (Padre) Vehiculo.
class Camion(Vehiculo):
    # Definición del método constructor o inicial de la clase hija
    def __init__(self, marca, modelo, color, capacidad_carga):
        # Llamada del metodo constructor de la clase (PADRE) haciendo uso de super() 
        # haciendo uso de la herecia de los atributos comunes (marca, modelo, color, encendido).
        super().__init__(marca, modelo, color)

        # Añadimos el atributo que es específico solo de Automovil
        self.capacidad_carga = capacidad_carga

    # Definición del método abstracto heredado de la clase Padre Vehiculo
    def conducir(self):
        if self.encendido:
            print(f"Conduciendo el {self.marca} {self.modelo} - Capacidad de carga: {self.capacidad_carga}.")
        else:
            print("No se puede conducir, el vehículo está apagado.")


# EJEMPLOS DE USO
print("--- Ejemplo con Automóvil ---")
# Creamos una 'instancia' (un objeto real) de la clase Automovil
automovil1 = Automovil("Toyota", "Corolla", "Rojo", "Gasolina")
# Creamos una instancia de Camion
camion1 = Camion("Ford", "F-150", "Azul", "2 toneladas")

# Usamos los métodos del objeto 'automovil1'
automovil1.encender() # Llama al método heredado de Vehiculo
automovil1.conducir() # Llama al método propio de Automovil
automovil1.apagar()   # Llama al método heredado de Vehiculo

# (Opcional) Si intentáramos conducir ahora, fallaría:
# automovil1.conducir() # Imprimiría "No se puede conducir..."

print("\n--- Ejemplo con Camión ---")
camion1.encender()
camion1.conducir()
