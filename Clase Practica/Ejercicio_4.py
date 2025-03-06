# --- Crea un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase. ---

# --- Pedir al usuario que introduzca una frase ---
frase = input("Introduce una frase: ")

# --- Pedir al usuario que introduzca una letra ---
letra = input("Introduce una letra: ")

contador  = 0

# --- Crear un bucle para contar el número de veces que aparece la letra en la frase ---
for caracter in frase:
    if caracter == letra:
        contador += 1   # --- contrador = contador + 1

print(f"La letra '{letra}' aparece {contador} veces en la frase '{frase}'")
# --- FIN SCRIPT ---