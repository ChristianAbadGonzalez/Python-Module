# Definición de la clase Engine que se encarga únicamente de la lógica relacionada con el motor.
class Engine:
    # Método que retorna las revoluciones por minuto (RPM) del motor
    def getRPM(self):
        return 3000

# Definición de la clase Vehiculo que se encarga únicamente de la lógica relacionada con el vehículo.
class Vehiculo:
    # Definición del método constructor de la clase 
    def __init__(self, name, speed, engine):
        # Asignación o inicialización de variables con instancias privadas
        self._name = name      # Nombre del vehículo
        self._speed = speed    # Velocidad máxima del vehículo
        self._engine = engine  # Instancia del motor asociado al vehículo

    # Método getter que retorna el nombre del vehículo
    def getName(self):
        return self._name # Retorna el nombre del vehículo con la instancia privada

    # Método que obtiene las RPM del motor delegando la llamada a la clase Engine
    def getEngineRPM(self):
        return self._engine.getRPM()

    # Método getter que retorna la velocidad máxima del vehículo
    def getMaxSpeed(self):
        return self._speed
    
# Definición de la clase VehiclePrinter que se encarga únicamente de la impresión de información del vehículo.
class VehiculoImpreso:
    # Constructor que recibe una instancia de Vehiculo
    def __init__(self, vehicle):
        self._vehicle = vehicle  # Almacena la referencia al vehículo a imprimir

    # Método que imprime la información completa del vehículo en formato legible
    def printInfo(self):
        print(
            "Vehicle: {}, Max Speed: {}, RPM: {}".format(
                self._vehicle.getName(),        # Obtiene el nombre del vehículo
                self._vehicle.getMaxSpeed(),    # Obtiene la velocidad máxima
                self._vehicle.getEngineRPM(),   # Obtiene las RPM del motor (nota: hay un typo aquí - debería ser getEngineRPM)
            )
        )


# Definición de la clase VehiculoPersistencia que se encarga de la persistencia de datos del vehículo
class VehiculoPersistencia:
    # Constructor que recibe una instancia de Vehiculo y el tipo de base de datos
    def __init__(self, vehicle, db):
        self._vehicle = vehicle      # Almacena la referencia al vehículo
        self._persistance = db       # Almacena el tipo de base de datos a utilizar
        # Imprime un mensaje indicando dónde se están almacenando los datos
        print("Hey, storing data! in", self._persistance)


# Punto de entrada principal del programa
if __name__ == "__main__":
    # Creación de una instancia del motor
    engine = Engine()
    
    # Creación de una instancia de vehículo con nombre "Car", el motor creado y velocidad máxima de 200
    vehicle = Vehiculo(name = "Car", engine = engine, speed = 200)
    
    # Creación de una instancia de persistencia para almacenar el vehículo en una base de datos SQL
    persistance = VehiculoPersistencia(vehicle = vehicle, db = "SQL")
    
    # Creación de una instancia del impresor de vehículos
    printer = VehiculoImpreso(vehicle = vehicle)
    
    # Llamada al método para imprimir la información del vehículo
    printer.printInfo()