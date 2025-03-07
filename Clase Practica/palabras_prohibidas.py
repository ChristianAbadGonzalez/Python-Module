# --- Define una lista de 5 palabras aleatorias y una lista de letras prohibidas que contenga tres letras. ---
# --- Filtra las palabras en tu lista original crea una nueva lista de palabras filtradas que solo contenga aquellas palabras que no tienen ninguna letra prohibida. ---

# --- Creamos una lista de palabras aleatorias y otra lista de letras prohibidas ---
palabras_aleatorias = ["Casa", "Perro", "Gato", "Libro", "Ratón"]
letras_prohibidas = ["a", "u"]

# --- Creamos una lista de palabras filtradas ---
palabras_filtradas = []

# --- Creamos un bucle que recorra la lista de palabras aleatorias añadiendo el filtro de letras prohibidas ---
# --- y aquellas palabras aleatorias que no contengan las letras prohibidas, las añadimos a palabras filtradas ---
for palabra in palabras_aleatorias:
    incluir = True
    for letra_prohibida in letras_prohibidas:
        if letra_prohibida in palabra:
            incluir = False
    if incluir:
        palabras_filtradas.append(palabra)

print(f"La lista de palabras aletorias es {palabras_aleatorias}. Si la palabra en cuestion tiene las letras prohibidas {letras_prohibidas}, serán eliminadas de la lista")

# --- Imprimimos la lista de palabras filtradas -- 
print(f"La lista de palabras filtradas obtenida es: {palabras_filtradas}")