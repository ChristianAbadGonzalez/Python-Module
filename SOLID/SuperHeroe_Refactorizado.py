# IMPORTACIÓN DE MÓDULOS NECESARIOS
from abc import ABC, abstractmethod


# Clase base abstracta para representar un superhéroe
class Superhero(ABC):
    """Clase abstracta que define la interfaz común para todos los superhéroes."""
    
    def __init__(self, name, health):
        self.name = name      # Nombre del superhéroe
        self.health = health  # Puntos de vida del superhéroe
    
    @abstractmethod
    def attack(self):
        """Método abstracto que cada superhéroe debe implementar con su ataque específico."""
        pass


# CLASES CONCRETAS: Tipos de Superhéroes

class PunchSuperhero(Superhero):
    """Superhéroe que ataca con puñetazos."""
    
    def attack(self):
        return f"{self.name} attacks with a powerful punch!"


class LaserSuperhero(Superhero):
    """Superhéroe que ataca con rayos láser."""
    
    def attack(self):
        return f"{self.name} attacks with a laser beam!"


class RegularSuperhero(Superhero):
    """Superhéroe con ataque regular."""
    
    def attack(self):
        return f"{self.name} attacks with a regular attack!"


class FireSuperhero(Superhero):
    """Superhéroe que ataca con fuego."""
    
    def attack(self):
        return f"{self.name} attacks with a blazing fireball!"
    
# CLASE JUEGO
class Game:
    """Clase que representa el juego y gestiona los superhéroes."""
    
    def __init__(self):
        self.superheroes = []  # Lista de superhéroes en el juego

    def add_superhero(self, superhero: Superhero):
        """Añade un superhéroe al juego."""
        self.superheroes.append(superhero)

    def superhero_actions(self):
        """Ejecuta las acciones de ataque de todos los superhéroes."""
        for superhero in self.superheroes:
            print(superhero.attack())

# EJEMPLO DE USO
# Creamos una instancia del juego
game = Game()

# Creamos superhéroes de diferentes tipos (cada uno es una clase específica)
superhero1 = PunchSuperhero("Superman", 100)
superhero2 = LaserSuperhero("Cyclops", 80)
superhero3 = FireSuperhero("Human Torch", 90)

# Añadimos los superhéroes al juego
game.add_superhero(superhero1)
game.add_superhero(superhero2)
game.add_superhero(superhero3)

# Ejecutamos las acciones de todos los superhéroes
game.superhero_actions()