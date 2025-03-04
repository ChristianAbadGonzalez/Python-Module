# --- Preguntar al usuario cuantos coches ha vendido de cada tipo ---
rbm_serie1_vendidos = int(input("¿Cuántos RBM serie 1 has vendido? ")) # -- Variable de tipo entero que espera un valor numérico -- 
rbm_plus_vendidos = int(input("¿Cuántps RBM plus has vendido? ")) # -- Variable de tipo entero que espera un valor numérico -- 
rbm_todoterreno_vendidos = int(input("¿Cuántos RBM todoterreno has vendido?")) # -- Variable de tipo entero que espera un valor numérico --

# --- Guardamos los datos en variables ---
precio_rbm_serie1 = 20000 # -- Variable de tipo entero que almacena un valor numérico --
precio_rbm_plus = 35000 # -- Variable de tipo entero que almacena un valor numérico --
precio_rbm_todoterreno = 60000 # -- Variable de tipo entero que almacena un valor numérico --

# -- Comisiones resultantes por venta de cada tipo de coche --
comision_rbm_serie1 = 0.03 # -- Variable de tipo flotante que almacena un valor numérico --
comision_rbm_plus = 0.05 # -- Variable de tipo flotante que almacena un valor numérico --
comision_rbm_todoterreno = 0.07 # -- Variable de tipo flotante que almacena un valor numérico --

# --- Calculamos la cantidad de euros a comisionar ese mes ---
ganancia_rbm_serie_1 = rbm_serie1_vendidos * precio_rbm_serie1 * comision_rbm_serie1 # -- Variable de tipo flotante que almacena un valor numérico --
ganancia_rbm_plus = rbm_plus_vendidos * precio_rbm_plus * comision_rbm_plus # -- Variable de tipo flotante que almacena un valor numérico --
ganancia_rbm_todoterreno = rbm_todoterreno_vendidos * precio_rbm_todoterreno * comision_rbm_todoterreno # -- Variable de tipo flotante que almacena un valor numérico --

ganancia_total = ganancia_rbm_serie_1 + ganancia_rbm_plus + ganancia_rbm_todoterreno # -- Variable de tipo flotante que almacena un valor numérico --

# --- Imprimimos la ganancia total ---
print("La cantidad total de euros a comisionar este més es de ", ganancia_total, "euros") # -- Imprime un mensaje en pantalla con el valor de la variable ganancia_total --