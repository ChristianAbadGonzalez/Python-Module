# Una biblioteca tiene una lista de libros y sus autores. Crea un programa que tome la lista de libros y sus autores como una lista de tuplas, 
# donde cada tupla contiene el título del libro y el nombre del autor, y devuelva una nueva lista de tuplas que contenga el título del libro y el apellido del autor.

# Pista: Tus datos de entrada podrían ser así —> lista_libros = [(‘El aleph', ‘Jorge LuisBorges'), ('Cien años de soledad', ‘Garbriel Garcia Márquez'), 
# ('La ciudad y los perros', ‘Mario Vargas Llosa')]

lista_libros = [
    ("El aleph", "Jorge Luis Borges"), 
    ("Cien años de soledad", "Garbriel Garcia Márquez"), 
    ("La ciudad y los perros", "Mario Vargas Llosa")
]

lista_libros_con_apellido = []

for titulo, autor in lista_libros:
    # Dividir el nombre completo del autor en palabras haciendo uso del metodo split()
    nombre = autor.split()
    
    # Obtenemos el apellido del autor posicionando el puntero en la ultima posición de la lista
    apellido = nombre[-1]
    
    # Agregamos a la lista de los libros y el apellido del autor del libro
    lista_libros_con_apellido.append((titulo, apellido))


print("La lista de libros con el apellido del autor es: ", lista_libros_con_apellido)