# Crea dos archivos, cats.txt y dogs.txt. 
# Almacena al menos tres nombres de gatos en el primer archivo y tres nombres de perros en el segundo archivo. 
# Escribe un programa que intente leer estos archivos e imprima el contenido de cada archivo en la pantalla. 
# Envuelve tu código en un bloque try-except para capturar el error de FileNotFoundError, 
# e imprime un mensaje amigable si falta algún archivo. 
# Mueve uno de los archivos a una ubicación diferente en tu sistema y asegúrate de que el código en el bloque except se ejecute correctamente. 
# Modifica tu bloque except para que falle en silencio si falta alguno de los archivos.

# Manejo de archivos
fileName = ["gatos.txt", "perros.txt"]

for filename in fileName:
    try:
        with open(filename, "r") as file:
            print(f"Contenido de {filename}:")
            contenido = file.read()
            print(contenido)
    except FileNotFoundError:
        pass
        print(f"El archivo {filename} no se encontró. Por favor, verifica la ubicación del archivo.")
        