# CLASE SUPERHÉROE 
class Superhero:
    """Clase que representa un superhéroe con nombre, salud y tipo de ataque."""
    
    # DEFINICIÓN DEL MÉTODO CONSTRUCTOR
    def __init__(self, name, health, attack_type):
        self.name = name            # Nombre del superhéroe
        self.health = health        # Puntos de vida del superhéroe
        self.attack_type = attack_type  # Tipo de ataque (cadena de texto)

    # Método que determina el ataque según el tipo. -- Problema: usa condicionales para decidir el comportamiento
    def attack(self):
        # Verifica si el ataque es de tipo "punch"
        if self.attack_type == "punch":
            return f"{self.name} attacks with a powerful punch!"
        
        # Verifica si el ataque es de tipo "laser"
        elif self.attack_type == "laser":
            return f"{self.name} attacks with a laser beam!"
        
        # Ataque genérico si no coincide con ninguno
        else:
            return f"{self.name} attacks with a regular attack!"

# CLASE JUEGO
class Game:
    """Clase que representa el juego y gestiona los superhéroes."""
    
    def __init__(self):
        # Lista para almacenar los superhéroes del juego
        self.superheroes = []

    # Método para añadir un superhéroe al juego
    def add_superhero(self, superhero):
        self.superheroes.append(superhero)

    # Método que ejecuta las acciones de todos los superhéroes
    def superhero_actions(self):
        # Itera sobre todos los superhéroes y ejecuta su ataque
        for superhero in self.superheroes:
            print(superhero.attack())

# EJEMPLO DE USO
# Creamos una instancia del juego
game = Game()

# Creamos dos superhéroes con diferentes tipos de ataque
superhero1 = Superhero("Superman", 100, "punch")
superhero2 = Superhero("Cyclops", 80, "laser")

# Añadimos los superhéroes al juego
game.add_superhero(superhero1)
game.add_superhero(superhero2)

# Ejecutamos las acciones de todos los superhéroes
game.superhero_actions()