# ============================================================== SISTEMA DE GESTION DE BIBLIOTECA ==============================================================
# ==============================================================================================================================================================

# Crea un sistema de gestión de una biblioteca utilizando clases en Python. Debes implementar las siguientes clases:

# 1. “Libro”: Representa un libro con atributos como título, autor y número de ejemplares disponibles.
# 2. “Usuario”: Representa a un usuario de la biblioteca con atributos como nombre, número de identificación y lista de libros prestados.
# 3. “Biblioteca”: Representa la biblioteca en sí, con métodos para agregar libros, prestar libros a usuarios, devolver libros y mostrar el inventario.

class Libro:
    def __init__(self, titulo, autor, ejemplares_disponibles):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares_disponibles = ejemplares_disponibles

    def __str__(self):
        return f"'{self.titulo}' de {self.autor} (Disponible: {self.ejemplares_disponibles})"

class Usuario:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
        self.libros_prestados = []

    def __str__(self):
        return f"{self.nombre} (ID: {self.identificacion})"

class Biblioteca:
    def __init__(self):
        self.libros = []  # lista de instancias Libro

    def agregar_libro(self, libro):
        # Si ya existe un libro con el mismo título y autor, suma ejemplares
        for l in self.libros:
            if l.titulo == libro.titulo and l.autor == libro.autor:
                l.ejemplares_disponibles += libro.ejemplares_disponibles
                print(f"Se agregaron {libro.ejemplares_disponibles} ejemplares a {l.titulo}. Total: {l.ejemplares_disponibles}")
                return
        self.libros.append(libro)
        print(f"Libro agregado: {libro}")

    def mostrar_inventario(self):
        print("\n=== Inventario de la Biblioteca ===")
        if not self.libros:
            print("No hay libros en el inventario.")
            return
        for i, libro in enumerate(self.libros, start=1):
            print(f"{i}. {libro}")

    def prestar_libro(self, usuario, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                if libro.ejemplares_disponibles > 0:
                    libro.ejemplares_disponibles -= 1
                    usuario.libros_prestados.append(libro)
                    print(f"El libro '{titulo}' ha sido prestado a {usuario.nombre}. Quedan {libro.ejemplares_disponibles} ejemplares.")
                    return True
                else:
                    print(f"No hay ejemplares disponibles de '{titulo}'.")
                    return False
        print(f"El libro '{titulo}' no se encuentra en la biblioteca.")
        return False

    def devolver_libro(self, usuario, titulo):
        # Busca en los libros prestados del usuario
        for idx, libro in enumerate(usuario.libros_prestados):
            if libro.titulo == titulo:
                usuario.libros_prestados.pop(idx)
                # Incrementa el conteo en el inventario (coincide por referencia)
                libro.ejemplares_disponibles += 1
                print(f"{usuario.nombre} ha devuelto '{titulo}'. Disponibles ahora: {libro.ejemplares_disponibles}")
                return True
        print(f"{usuario.nombre} no tiene prestado el libro '{titulo}'.")
        return False

    def mostrar_prestamos_usuario(self, usuario):
        print(f"\nLibros prestados a {usuario.nombre}:")
        if not usuario.libros_prestados:
            print("Ninguno.")
            return
        for i, libro in enumerate(usuario.libros_prestados, start=1):
            print(f"{i}. {libro.titulo} - {libro.autor}")

# Ejemplos de uso
# Crear biblioteca, libros y usuarios
biblio = Biblioteca()
biblio.agregar_libro(Libro("Cien años de soledad", "Gabriel García Márquez", 3))
biblio.agregar_libro(Libro("El Quijote", "Miguel de Cervantes", 2))
biblio.agregar_libro(Libro("Cien años de soledad", "Gabriel García Márquez", 1))  # suma ejemplares

biblio.mostrar_inventario()

usuario1 = Usuario("Ana", "U001")
usuario2 = Usuario("Luis", "U002")

# Préstamos
biblio.prestar_libro(usuario1, "Cien años de soledad")
biblio.prestar_libro(usuario2, "Cien años de soledad")
biblio.prestar_libro(usuario2, "El Quijote")

biblio.mostrar_inventario()
biblio.mostrar_prestamos_usuario(usuario1)
biblio.mostrar_prestamos_usuario(usuario2)

# Devolución
biblio.devolver_libro(usuario2, "Cien años de soledad")
biblio.mostrar_inventario()
biblio.mostrar_prestamos_usuario(usuario2)