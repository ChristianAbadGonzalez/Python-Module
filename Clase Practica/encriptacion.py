# --- ENCRIPTACIÓN ROT13 ---

# --- Desarrolla un script que recibiendo de entrada una cadena de caracteres devuelva el texto codificado según el cifrado ROT13 ---
alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabeto_mayusculas = alfabeto.upper

# --- Según la encriptación ROT13, la siguiente palabra codificada, no debe de dar de resultado [HOLA --> UBYN]
mensaje = input("Hola! Por favor, introduce un mensaje para encriptar: ")

mensaje_extra = mensaje = input("Hola! Por favor, introduce un mensaje para comparar: ")

mensaje_cifrado = ""
for char in mensaje:
    # -- Compruebo si se encuentra en el alfabeto en minusculas --- 
    if char in alfabeto:
    # -- Bucle que recorre el alfabeto definido
        for i in range(len(alfabeto)):
            # -- Cuando la letra analizada sea del mensaje en el alfabeto, este cogera un nuevo indice actualizado 13 posiciones añadidas --
            if char == alfabeto[i]:
                char_indice = i
                print("Indice inicial: ", char_indice)
                if char_indice + 13 >= 26:
                    char_indice = char_indice - 26

                nuevo_indice = char_indice + 13
                letra_cifrada = alfabeto[nuevo_indice]
        
        mensaje_cifrado = mensaje_cifrado + letra_cifrada
    
    elif char in alfabeto_mayusculas:
        for i in range(len(alfabeto_mayusculas)):
            # -- Cuando la letra analizada sea del mensaje en el alfabeto, este cogera un nuevo indice actualizado 13 posiciones añadidas --
            if char == alfabeto_mayusculas[i]:
                char_indice = i
                print("Indice inicial: ", char_indice)
                if char_indice + 13 >= 26:
                    char_indice = char_indice - 26

                nuevo_indice = char_indice + 13
                letra_cifrada = alfabeto_mayusculas[nuevo_indice]
        
        mensaje_cifrado = mensaje_cifrado + letra_cifrada
    else:
        mensaje_cifrado = mensaje_cifrado + char

print(f"El mensaje cifrado analizado {mensaje} es {mensaje_cifrado}")

# --- Desarrolla ahora un script que compare dos cadenas de caracteres y nos diga si una de ellas esta codificación ROT13 de la otra. ---
if mensaje_cifrado == mensaje_extra:
    print(f"Los mensajes expuestos {mensaje_cifrado} y {mensaje_extra} tienen la misma encriptación")
else:
    print(f"Los mensajes expuestos {mensaje_cifrado} y {mensaje_extra} no tienen la misma encriptación")



