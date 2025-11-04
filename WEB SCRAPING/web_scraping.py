# Importación de bibliotecas necesarias
import requests
from bs4 import BeautifulSoup as BS
import numpy as np
import pandas as pd


# Ejemplo 1: Captura de una noticia de un sitio web de noticias y parse de HTML

# Define la URL de la noticia que quieres "raspar"
url = "https://elpais.com/ciencia/2024-11-29/la-ingeniosa-tecnica-de-moctezuma-y-su-banda-de-orcas-para-cazar-tiburones-ballena-en-mexico.html"

try:
    # Intenta descargar la página. page contendrá la respuesta del servidor.
    page = requests.get(url)
except:
    # Si hay un error (ej. no hay internet, la URL es mala), imprime un error.
    print("Error al abrir la URL")

# "Parsea" (interpreta) el contenido HTML de la página
soup = BS(page.text, 'html.parser')

# Busca la primera etiqueta <div> que tenga el atributo "data-dtm-region"
# con el valor "articulo_cuerpo". Aquí es donde está el texto principal.
contenido_noticia = soup.find('div', {"data-dtm-region": "articulo_cuerpo"})

articulo = [] # Crea una lista vacía para guardar los párrafos

# Busca todas las etiquetas <p> (párrafos) DENTRO del <div> anterior
for i in contenido_noticia.find_all('p'):
    articulo.append(i.text) # Añade solo el texto de cada párrafo a la lista

print('\n'.join(articulo)) # Imprime la lista, uniendo cada párrafo con un salto de línea

# Buscamos los parrafos dentro de la etiqueta <div> con el cuerpo de la noticia que contenga un elemento de tipo enlace <a>
links = contenido_noticia.find_all('a')

for link in links:
    print(f"Texto del enlace: {link.text}, Href: {link['href']}")

# -----------------------------------------------------------------------------------------------------------------------------

# Ejemplo 2: Datos de la Wikipedia - Provincias de España
url_wikipedia = requests.get("https://es.wikipedia.org/wiki/Provincia_(Espa%C3%B1a)")

soup_wikipedia = BS(url_wikipedia.text, 'html.parser')

# Busca la etiqueta <table> que tenga la clase "wikitable sortable"
tabla = soup_wikipedia.find('table', {"class": "wikitable sortable"})

# Busca todas las etiquetas <tr> (filas de la tabla) dentro de esa tabla
provincias = tabla.find_all('tr')

# Imprime la primera celda <td> de la segunda fila <tr> (índice [1])
# .prettify() la formatea de manera legible. Es para inspección/debug.
print(provincias[1].td.prettify())

# Esta sección busca enlaces dentro de la primera celda de la segunda fila
enlaces = provincias[1].td.find_all('a')


# Crea una lista vacía para guardar los datos
datos_provincias = []


# Itera sobre CADA fila en la lista de provincias, OMITIENDO la primera
for provincia in provincias[1:]:
    # Dentro de cada fila, busca todas las celdas <td>
    celdas = provincia.find_all('td')
    
    # Asegúrate de que la fila tiene suficientes celdas
    if len(celdas) > 4: 
        
        # El nombre está en la celda [1] (esto estaba bien)
        nombre = celdas[1].text.strip()

        # CORRECCIÓN 1: La población está en la celda [4]
        # CORRECCIÓN 2: Los números usan espacios, no puntos
        poblacion_texto = celdas[4].text.strip().replace(' ', '')
        
        # Comprobamos que el texto sea solo dígitos antes de convertir
        if poblacion_texto.isdigit():
            poblacion = int(poblacion_texto)
            
            # Añade la tupla (nombre, poblacion) a la lista
            datos_provincias.append((nombre, poblacion))
            print(f"Provincia: {nombre}, Población: {poblacion}")
        else:
            print(f"Omitiendo {nombre}: dato de población no numérico ('{poblacion_texto}')")

# Convierte la lista de tuplas (ej. [('Álava', 334045), ...]) 
# en una tabla de datos (DataFrame) con columnas etiquetadas.
df_provincias = pd.DataFrame(datos_provincias, columns=['Provincia', 'Población'])

print("--- DataFrame Creado ---")
print(df_provincias)

# Guarda esta tabla de memoria en un archivo físico en tu disco.
# index=False evita que pandas guarde el índice (0, 1, 2...) como una columna.
df_provincias.to_csv('provincias_espana.csv', index=False)

# Vuelve a leer el archivo que acabas de guardar para verificar
# (es una buena forma de comprobar que el guardado funcionó).
print("\n--- Leyendo CSV Guardado ---")
df_leido = pd.read_csv('provincias_espana.csv')
print(df_leido)

# Utiliza las funciones matemáticas de pandas para analizar la columna 'Población'.
print("\n--- Estadísticas de Población ---")
# .describe() da un resumen estadístico completo (media, min, max, cuartiles...)
print(df_provincias['Población'].describe())

# Aquí calculas y muestras algunas de esas estadísticas manualmente:
print(f"Población total: {df_provincias['Población'].sum()}")
print(f"Población media: {df_provincias['Población'].mean()}")
print(f"Población máxima: {df_provincias['Población'].max()}")
print(f"Población mínima: {df_provincias['Población'].min()}")

