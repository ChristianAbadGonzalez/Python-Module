# --- Supongamos una lista de de caracteres llamada “palabras“ que representa una mano de Scrabble. ---
# --- Cada string contiene dos caracteres: el primer carácter es la letra de una ficha y el segundo el numero que representa los puntos de la ficha. ---
# --- Por ejemplo, el string "A5" representa la ficha con la letra A y un valor de 5 puntos. ---
# --- Crea un script que calcule el valor total de los puntos en una mano de scrabble. El valor total será la suma de los puntos de todas las fichas de la mano. ---

# --- Creamos una lista de fichas de scrabble ---
fichas_scrabble = ["A5", "B3", "C4", "H8", "D1"]

# --- Creamos un bucle para recorrer los valores asociados a la mano de scrabble y sumamos los puntos en cuestion ---
puntos = 0
for ficha in fichas_scrabble:
    puntos = puntos + int(ficha[1])

# --- Imprimimos el valor resultante obtenido en el bucle --- 
print("Los valores de la suma asociados a la mano de scrabble es: ", puntos)