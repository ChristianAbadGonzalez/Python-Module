# --- Pedir nombre al usuario ---
nombre = input("Ingresa tu nombre: ")

# --- Saludar al usuario ---
print("¡Hola,", nombre, "!")

# --- Guardamos ingresos y horas trabajadas ---
ingresos_hora = float(input("Ingresa tus ingresos por hora: "))
# --- La variable ingresos_hora pide al usuario que ingrese sus ingresos por hora y los trasforma a un número decimal "float" ---

horas_trabajadas = int(input("Ingresa las horas trabajadas: "))
# --- La variable horas_trabajadas pide al usuario que ingrese las horas trabajadas y las trasforma a un número entero "int" ---

# --- Calculamos la ganancia semanal ---
salario_semanal = ingresos_hora * horas_trabajadas
# --- salario_semanal es igual a la multiplicación de ingresos_hora por horas_trabajadas ---

# --- Calculamos la ganancia anual ---
ganancia_anual = salario_semanal * 52
# --- ganancia_anual es igual a la multiplicación de salario_semanal por 52 semanas que trabajas al año ---

# --- Imprime ganancia anual por pantalla ---
print(nombre.title(), "tienes unas ganacias anuales de", ganancia_anual, "euros")
# --- Imprime el nombre del usuario en mayúsculas y el resultado de la ganancia anual ---

# --- Pedimos los gastos semanales al usuario ---
gastos_semanales = float(input("Ingresa tus gastos semanales: "))
# --- La variable gastos_semanales pide al usuario que ingrese sus gastos semanales y los trasforma a un número decimal "float" ---

# --- Calculamos el gasto anual ---
gasto_anual = gastos_semanales * 52

# --- Calculamos los ahorros ---
ahorro_anual = ganancia_anual - gasto_anual

# --- Imprime el ahorro anual por pantalla ---
print("Tu ahorro anual será de", ahorro_anual, "euros")