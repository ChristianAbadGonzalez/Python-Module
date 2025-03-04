# --- Definir el precio de cada alimento con Variables de tipo Entero---
precio_ensalada_mixta = 12 
precio_sopa_pescado = 10 
precio_dorada_horno = 18 
precio_arroz_curry = 14
precio_lasagna_carne = 15
precio_brownie_chocolate = 8
precio_helado = 6
precio_refresco = 5.5
precio_cafe = 3.5

# --- Pedir al usuario que introduzca la cantidad de cada alimento que ha consumido ---
# --- Variables de almacenamiento de tipo Entero con interacción del usuario al introducir el valor por la pantalla ---
cantidad_ensalada_mixta = int(input("¿Cuántos pedidos de ensaladas mixtas se han consumido? ")) 
cantidad_sopa_pescado = int(input("¿Cuántos pedidos de sopas de pescado se han consumido? "))
cantidad_dorada_horno = int(input("¿Cuántos pedidos de doradas al horno se han consumido? "))
cantidad_arroz_curry = int(input("¿Cuántos pedidos de arroces al curry se han consumido? "))
cantidad_lasagna_carne = int(input("¿Cuántos pedidos de lasañas de carne se han consumido? "))
cantidad_brownie_chocolate = int(input("¿Cuántos pedidos de brownies de chocolate se han consumido? "))
cantidad_helado = int(input("¿Cuántos pedidos de helados se han consumido? "))
cantidad_refresco = int(input("¿Cuántos pedidos de refrescos se han consumido? "))
cantidad_cafe = int(input("¿Cuántos pedidos de cafés se han consumido? "))

# --- Calculamos el total de la cuenta ---
total = cantidad_ensalada_mixta * precio_ensalada_mixta + \
    cantidad_sopa_pescado * precio_sopa_pescado + \
    cantidad_dorada_horno * precio_dorada_horno + \
    cantidad_arroz_curry * precio_arroz_curry + \
    cantidad_lasagna_carne * precio_lasagna_carne + \
    cantidad_brownie_chocolate * precio_brownie_chocolate + \
    cantidad_helado *  precio_helado + \
    cantidad_refresco * precio_refresco + \
    cantidad_cafe * precio_cafe 

# --- Imprimimos la cuenta ---
print("La cuenta suma un total de ", total," euros.") # -- Imprime un mensaje en pantalla con el valor de la variable total --
# --- Definir el precio de cada alimento con Variables de tipo Flotante --- 