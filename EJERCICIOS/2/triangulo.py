# --- En una obra es necesario construir para el tejado de una casa una estructura triangular con tres piezas. 
# El ingeniero se pregunta si dadas la largura de las piezas que ha recibido podrá construir este estructura. 
# Crea un script que dados tres longitudes indique si podría construirse un triangulo con esas piezas.

# --- NOTA: La suma de dos piezas tiene que ser mayor que el lado restante. ---

# --- Pedir al usuario las longitudes de las tres piezas ---
L1 = float(input("Introduce la longitud de la primera pieza: "))
L2 = float(input("Introduce la longitud de la segunda pieza: "))
L3 = float(input("Introduce la longitud de la tercera pieza: "))


# --- Comprobar si la suma de dos piezas es mayor que la longitud de la tercera pieza ---
if L1 + L2 > L3 and L1 + L3 > L2 and L2 + L3 > L1:
    print("Se puede construir un triángulo con las piezas dadas")
else:
    print("No se puede construir un triángulo con las piezas")

# --- Imprimir si se puede construir un triángulo con las piezas dadas por pantalla ---

# --- Fin del script ---