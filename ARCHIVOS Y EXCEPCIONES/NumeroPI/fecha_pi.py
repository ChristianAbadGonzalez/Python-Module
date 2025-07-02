# Busca si tu fecha de nacimiento esta en los primeros 10000 digitos de pi 
# (y en que posición. Puedes usar find()). Puedes usar el archivo pi_10000.txt

def buscar_fecha_en_pi(filename, string_fecha):
    # Busca la fecha de nacimiento en los primeros 10000 digitos de pi

    try:
        # Abrimos el archivo de texto en modo lectura
        with open(filename, "r") as file:
            # Leemos el contenido del archivo
            contenido = file.read()

            # Buscamos la fecha en el contenido del archivo
            posicion = contenido.find(string_fecha)

            # Si la fecha se encuentra, devolvemos la posición
            if posicion != -1:
                print(f"La fecha {string_fecha} se encuentra en la posición {posicion} de los primeros 10000 dígitos de pi.")
                # Retornamos la posición encontrada
                return posicion
            else:
                print(f"La fecha {string_fecha} no se encuentra en los primeros 10000 dígitos de pi.")
                return None

    except FileNotFoundError:
        # Si el archivo no se encuentra, mostramos un mensaje de error
        print(f"El archivo {filename} no se encontró. Por favor, verifica la ubicación del archivo.")
        return None
    

# Definimos el nombre del archivo y la fecha a buscar
filename = "pi_10000.txt"
string_fecha = "17041998"

buscar_fecha_en_pi(filename, string_fecha)