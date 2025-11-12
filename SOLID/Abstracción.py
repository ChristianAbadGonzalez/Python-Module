# Definición de la clase padre llamada Vehiculo
class Vehiculo():
    # Definición del método constructor o inicializador de la clase padre.
    # Se ejecuta automáticamente al crear una nueva instancia de Vehiculo.
    def __init__(self, marca, modelo, color):
        # Atributos (variables) comunes a todos los vehículos.
        self.marca = marca      # Marca del vehículo (por ejemplo, Toyota)
        self.modelo = modelo    # Modelo del vehículo (por ejemplo, Corolla)
        self.color = color      # Color del vehículo (por ejemplo, rojo)

        # Definimos un estado inicial: todo vehículo empieza apagado.
        self.encendido = False

        # Estado inicial de la velocidad: el vehículo empieza detenido.
        self.velocidad = 0

    # Definición de método para mostrar la información del vehículo
    def mostrar_vehiculo(self):
        # Imprime por pantalla marca y modelo del vehículo
        print(f"Este es un {self.marca} {self.modelo} de color {self.color}")

    # Método para encender el vehículo
    def encender(self):
        # Cambia el estado del atributo 'encendido' a True
        self.encendido = True
        print("El vehículo está encendido.")

    # Método para apagar el vehículo
    def apagar(self):
        # Cambia el estado del atributo 'encendido' a False
        self.encendido = False
        print("El vehículo está apagado.")

    # Método para acelerar el vehículo
    def acelerar(self, incremento):
        # Comprueba que el vehículo esté encendido antes de acelerar
        if self.encendido:
            self.velocidad += incremento  # Aumenta la velocidad
            print(f"Vehículo acelerado: {self.velocidad} km/h")
        else:
            # No permite acelerar si el vehículo está apagado
            print("No se puede acelerar, encienda el vehículo primero.")

    # Método para frenar el vehículo
    def frenar(self, decremento):
        # Solo se puede frenar si el vehículo está encendido
        if self.encendido:
            # Comprueba que la velocidad no sea negativa
            if self.velocidad - decremento >= 0:
                self.velocidad -= decremento
                print(f"El vehículo desaceleró a: {self.velocidad} km/h")
            else:
                # Si el decremento excede la velocidad actual, el vehículo se detiene
                self.velocidad = 0
                print("El vehículo se detuvo.")
        else:
            # Si el vehículo está apagado, no puede frenar
            print("No se puede frenar, encienda el vehículo primero.")


# ===============================
# EJEMPLO DE USO DE LA CLASE
# ===============================

# Creación de una instancia de la clase Vehiculo.
# ⚠️ Se añadió el argumento 'color' porque el constructor lo requiere.
vehiculo = Vehiculo("Toyota", "Corolla", "Blanco")

# Llamada a los distintos métodos definidos en la clase.
vehiculo.mostrar_vehiculo()  # Muestra la información del vehículo
vehiculo.encender()          # Enciende el vehículo
vehiculo.acelerar(10)        # Acelera 10 km/h
vehiculo.frenar(10)          # Frena 10 km/h
vehiculo.apagar()            # Apaga el vehículo