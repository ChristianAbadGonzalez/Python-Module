# Escribe un programa que solicite al usuario su número favorito. 
# Utiliza json.dump() para almacenar este número en un archivo. 
# Escribe un programa separado que lea este valor e imprima el mensaje: 
# “Sé cuál es tu número favorito… Es .....” 
# Combina ambos programas en un solo archivo (puedes crear tantas funciones como necesites). 
# Si el número ya está almacenado, muestra el número favorito al usuario. 
# Si no lo está, solicita al usuario su número favorito y guárdalo en un archivo. 
# Ejecuta el programa al menos dos veces para asegurarte de que funciona correctamente.

# Importamos el modulo json para manejar archivos JSON
import json


def comprobar_num_fav():
    # Comprueba si el archivo numero_fav.json existe y contiene un número favorito
    try:
        with open("numero_fav.json", "r") as file:
            num_fav = json.load(file)
            return(num_fav)
            
    except FileNotFoundError:
        print("No se encontró el archivo numero_fav.json. Por favor, introduce tu número favorito.")
        return None
    
def guardar_num_fav(numero_favorito):
    # Guarda el número favorito introducido por el usuario en un archivo JSON
    with open("numero_fav.json", "w") as file:
        # Convertimos el número favorito a un diccionario y lo guardamos en el archivo
        json.dump({"numero_favorito": numero_favorito}, file)
        print(f"Tu número favorito {numero_favorito} ha sido guardado correctamente.")

def preguntar_num_fav():
    num_fav = int(input("¿Cuál es tu número favorito? "))
    guardar_num_fav(num_fav)
    return num_fav

def imprimir_num_fav(numero_favorito):
    # Imprime el número favorito del usuario
    print(f"¡Sé cuál es tu número favorito! Es {numero_favorito}.")


# PROGRAMA PRINCIPAL
numero_favorito = comprobar_num_fav()

if numero_favorito:
    print(numero_favorito)
else:
    # Si no hay número favorito guardado, solicitamos al usuario que lo introduzca
    numero_favorito = preguntar_num_fav()
    imprimir_num_fav(numero_favorito)
