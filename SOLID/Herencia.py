class Vehiculo:
    # Constructor que inicializa atributos comunes a todos los vehículos
    def __init__(self, marca, modelo):
        self.marca = marca   # Marca del vehículo (por ejemplo, Toyota)
        self.modelo = modelo # Modelo del vehículo (por ejemplo, Corolla)

    # Método que devuelve una descripción general del vehículo
    def describir(self):
        return f"Este vehículo es un {self.marca} {self.modelo}"


class Automovil(Vehiculo):
    # Constructor que amplía el del padre añadiendo parámetro "puertas"
    def __init__(self, marca, modelo, puertas):
        # Llama al constructor de la clase padre con super()
        super().__init__(marca, modelo)
        self.puertas = puertas  # Nuevo atributo específico de Automovil

    # Sobrescritura (override) del método describir()
    # Este método reemplaza el que tiene la clase padre.
    def describir(self):
        return f"Este automóvil es un {self.marca} {self.modelo} con {self.puertas} puertas"


class Camion(Automovil):
    # Constructor que añade el atributo "carga" (además de los heredados)
    def __init__(self, marca, modelo, puertas, carga):
        # Llama al constructor de Automovil (que a su vez llama a Vehiculo)
        super().__init__(marca, modelo, puertas)
        self.carga = carga  # Nuevo atributo exclusivo del camión

    # Sobrescritura del método describir()
    def describir(self):
        return f"Este camión es un {self.marca} {self.modelo} con {self.puertas} puertas y una capacidad de carga de {self.carga} kg"
    

# EJEMPLO DE USO
vehiculo1 = Automovil("Toyota", "Corolla", 4)
vehiculo2 = Camion("Toyota", "FSHD", 2, 1000)
print(vehiculo1.describir())
print(vehiculo2.describir())
