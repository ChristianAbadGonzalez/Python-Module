# Definición de la clase padre 
class Vehiculo():
    # Definición del método constructor o inicial de la clase padre.
    def __init__(self, marca, modelo, color):
    # Atributos (variables) comunes a todos los vehículos.
        self.marca = marca
        self.modelo = modelo
        self.color = color

        # Definimos un estado inicial. Todo vehículo empieza apagado.
        self.encendido = False

        # Definimos un estado inicial. Todo vehículo empieza parado
        self.velocidad = 0

    # Definición de métodos concretos con utilidades o funciones a realizar.
    # Mostrar información del vehículo
    def mostrar_vehiculo(self):
        print(f"Este es un {self.marca}  {self.modelo}")


    def encender(self):
        # Cambia el estado del atributo 'encendido' a True.
        self.encendido = True
        print("El vehículo está encendido.")


    def apagar(self):
        # Cambia el estado del atributo 'encendido' a False.
        self.encendido = False
        print("El vehículo está apagado.")


    # Métodos para acelerar y frenar el vehículo
    def acelerar(self, incremento):
        # Comprueba que el vehículo esté encendido antes de acelerar
        if self.encendido:
            self.velocidad += incremento
            print(f"Vehiculo acelerado: {self.velocidad} km/h")
        else:
            print(f"No se puede acelerar, encienda el vehiculo")


    def frenar(self, decremento):
        if self.encendido:
            if self.velocidad - decremento >= 0:
                self.velocidad -= decremento
                print(f"El vehiculo desacelero a: {self.velocidad} km/h")
            else:
                self.velocidad = 0
                print(f"El vehiculo se detuvo")
        else:
            print(f"No se puede frenar, encienda el vehiculo")


# EJEMPLOS DE USO
vehiculo = Vehiculo("Toyota", "Corolla")
vehiculo.mostrar_vehiculo()
vehiculo.encender()
vehiculo.acelerar(10)
vehiculo.frenar(10)
vehiculo.apagar()
