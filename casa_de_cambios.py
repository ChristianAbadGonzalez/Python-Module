# --- Pedir al usuario que ingrese la cantidad en euros ---
euros = input("Ingresa la cantidad de euros que deseas convertir: ") # tipo string

# --- Convertimos la cantidad ingresada a un float ---
euros = float(euros) # Convertir a float

# --- Convertir la cantidad de euros a dolares ---
dolares = euros * 1.2 # Convertir a dolares de tipo float

# --- Imprimir el resultado de la conversión ---
print(euros, "euros son", dolares, "dólares") # Imprimir el resultado

# --- Calculamos la cantidad que se queda la casa de cambios ---
tasas_gestion = dolares * 0.1 # tipo float

# --- Calculamos la cantidad de dolares que recibe el usuario ---
dolares_recibidos = dolares - tasas_gestion # tipo float

# --- Imprimimos el desglose de la operación ---
print("Monto ingresado: ", euros, " euros") 
print("Cambio en dólares: ", dolares, " dólares")
print("Tasa de gestión: ", tasas_gestion, " dólares")
print("Monto recibido: ", dolares_recibidos, " dólares")