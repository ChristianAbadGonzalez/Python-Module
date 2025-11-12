# Clase Padre Animal
class Animal:
    # Definición del método constructor de la clase padre (animal)
    def __init__(self, nombre):
        self.nombre = nombre

    # Definición del método "hacer_sonidos" que será sobrescrito por las clases hijas
    def hacer_sonidos(self):
        pass

# Clase Hija que hereda de la Clase Padre Animal
class Conejo(Animal):
    def hacer_sonidos(self):
        return "Hola soy un conejo"
    

# Creamos una instancia de la clase Conejo con la asignación a la variable mi_conejo
mi_conejo = Conejo("Zanahoria") 
# Ejemplo de uso al cual se le pasa el parámetro zanahoria y se imprime el nombre registrado o asociado a la etiqueta nombre. En este caso nombre = (Zanahoria).

# print(mi_conejo.nombre)
# TERMINAL --> Zanahoria 

# print(mi_conejo.hacer_sonidos())
# TERMINAL --> Hola soy un conejo


# Ejemplo 2 - herencia multiple
# Definición de la clase padre Vehículo
class Vehiculo:
    # Definición del método constructor de la clase padre (vehículo)
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    # Definición del método conducir
    def conducir(self):
        return "Rum rum!!"

# Definición de la clase Persona que hereda de las clases Vehículo y Animal
class Persona:
    # Definición del método constructor de la clase Persona que recibe parámetros heredados de las clases Vehículo y Animal
    def __init__(self, nombre, vehiculo, animal):
        self.nombre = nombre
        self.vehiculo = vehiculo
        self.animal = animal

    # Definición del método presentarse
    def presentarse(self):
        return f"Soy { self.nombre}, conduzco un {self.vehiculo.marca} {self.vehiculo.modelo} y mi mascota es: { self.animal.nombre}"
    

# EJEMPLO DE USO
vehiculo1 = Vehiculo("Toyota", "Corolla")
animal1 = Animal("Du")
persona2 = Persona("Raquel", vehiculo1, animal1)
print(persona2.presentarse())
print(persona2.vehiculo.conducir())