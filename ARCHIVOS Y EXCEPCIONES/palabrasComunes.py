# Encuentra o crea algunos textos que te gustaría analizar 
# (puedes visitar Project Gutenberg (http://gutenberg.org/) 
# o crear textos usando ChatGPT). Copia el texto sin formato 
# desde tu navegador en un archivo de texto en tu computadora 
# (o descarga los archivos). # Averigua cuántas veces aparece 
# una palabra o frase en el texto (puedes usar el método count()).

def contar_palabras_comunes(filename, palabra):
    # Contar cuantas veces aparece una palabra en un texto
    
    # Abrimos el archivo de texto en modo lectura
    with open(filename, "r") as file:
        # Leemos el contenido del archivo
        contenido = file.read()

        # Contamos el número de veces que se repite la palabra clave
        count = contenido.count(palabra)

        # Devolvemos el resultado del analisis del texto
        return count
    
# Definimos el nombre del archivo y la palabra clave a buscar
filename = "texto.txt"
palabra = "dia"
# OTRAS PALABRAS CLAVES -- "sol", "luz", "noche", "tiempo", y "claridad"

# Llamamos a la función y moestramos el resultado obtenido
repeticiones = contar_palabras_comunes(filename, palabra)
print(f"La palabra {palabra} aparece en el texto un total de {repeticiones} veces.")