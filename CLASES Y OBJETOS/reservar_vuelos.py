# ================================================================ SISTEMA DE RESERVAS DE VUELOS ================================================================
# ===============================================================================================================================================================

# Imagina que estás desarrollando un sistema de reservas de vuelos para una aerolínea. 
# Crea un sistema de clases que permita a los usuarios realizar reservas de vuelos. 
# Aquí tienes una posible estructura: 
#  - Clase base: `Vuelo`.
#  - Atributos: número de vuelo, origen, destino, capacidad máxima, lista de pasajeros.
#  - Métodos: agregar pasajero, verificar disponibilidad de asientos

#  - Clase derivada: `VueloEspecial` (hereda de `Vuelo`) 
#  - Atributos adicionales: motivo del vuelo especial (por ejemplo, vacaciones, trabajo) 

# Resuelve el problema creando instancias de estas clases y realizando reservas para diferentes vuelos y tipos de vuelos especiales.

class Vuelo:
    def __init__(self, numero, origen, destino, capacidad):
        self.numero = numero
        self.origen = origen
        self.destino = destino
        self.capacidad = capacidad
        self.pasajeros = []  # Inicializamos la lista de pasajeros

    def agregar_pasajero(self, pasajero):
        if self.verificar_disponibilidad() > 0:
            self.pasajeros.append(pasajero)
            print(f"El pasajero '{pasajero}' ha sido añadido correctamente al vuelo {self.numero}.")
            return True
        else:
            print(f"No hay asientos disponibles para el vuelo {self.numero}.")
            return False

    def verificar_disponibilidad(self):
        return self.capacidad - len(self.pasajeros)

    def __str__(self):
        return f"Vuelo {self.numero}: {self.origen} -> {self.destino} | Capacidad: {self.capacidad} | Ocupados: {len(self.pasajeros)}"


class VueloEspecial(Vuelo):
    def __init__(self, numero, origen, destino, capacidad, motivo):
        super().__init__(numero, origen, destino, capacidad)
        self.motivo = motivo  # p.ej., "Vacaciones" o "Trabajo"

    def __str__(self):
        base = super().__str__()
        return f"{base} | Tipo: Especial ({self.motivo})"
    


# Ejemplo de uso
vuelo_regular = Vuelo("UA30", "NL", "MAD", 150)
vuelo_regular.agregar_pasajero("CHRISTIAN")

print("Asientos disponibles: ", vuelo_regular.verificar_disponibilidad())

vuelo_especial = VueloEspecial("IB770", "LN", "BAR", 350, "Vacaciones")
vuelo_especial.agregar_pasajero("CHRISTIAN")

print("Asientos disponibles: ", vuelo_especial.verificar_disponibilidad())


