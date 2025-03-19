# --- Supongamos que tienes un conjunto de datos de clima que contiene información sobre la temperatura, la humedad y la presión atmosférica en una ciudad durante un año. ---
# --- Quieres analizar estos datos para determinar cuál fue la temperatura promedio de cada mes, cuál fue la humedad promedio y la presión atmosférica promedio durante todo el año. --- 
# --- Para ello, puedes usar NumPy para cargar los datos en un array de 3 columnas y n filas, donde n es el número de mediciones. ---
# --- Luego, puedes usar operaciones de NumPy para filtrar los datos por mes y calcular las medias de temperatura, humedad y presión atmosférica correspondientes. ---

# importar módulos
import numpy as np

# Datos de clima
# clima = np.array([temperatura, humedad, presion, mes])
clima = np.array([
    [20, 70, 1009, 1],
    [18, 75, 1012, 2],
    [16, 72, 1011, 2],
    [19, 73, 1011, 2],
    [22, 65, 1008, 3],
    [25, 60, 1010, 4],
    [22, 60, 1013, 4],
    [24, 59, 1010, 4],
    [25, 61, 1011, 4],
    [28, 50, 1007, 5],
    [30, 45, 1005, 6],
    [10, 45, 1005, 6],
    [32, 40, 1002, 7],
    [30, 35, 1003, 8],
    [33, 35, 1001, 8],
    [32, 35, 1004, 8],
    [31, 45, 1003, 9],
    [28, 50, 1006, 10],
    [27, 48, 1008, 10],
    [25, 60, 1010, 11],
    [22, 70, 1011, 12]
])

# Guardamos datos en arrays independientes
meses = clima[:, 3].astype(int)  # Convertimos a enteros para evitar errores de comparación
temperaturas = clima[:, 0]
humedad = clima[:, 1]
presion = clima[:, 2]

# Inicializamos arrays de valores promedio por mes
temp_mes = np.zeros(12)
humedad_mes = np.zeros(12)
presion_mes = np.zeros(12)

# Recorrer los valores para cada mes
for i in range(12):
    # Filtrar los datos del mes correspondiente
    mask = meses == (i + 1)

    # Verificar si hay datos para evitar warnings de NumPy
    if np.any(mask):
        temp_mes[i] = np.mean(temperaturas[mask])
        humedad_mes[i] = np.mean(humedad[mask])
        presion_mes[i] = np.mean(presion[mask])

        # Imprimimos resultados para cada mes
        print(f"Mes {i+1}:")
        print(f"Temperatura promedio: {temp_mes[i]:.2f}°C")
        print(f"Humedad promedio: {humedad_mes[i]:.2f}%")
        print(f"Presión promedio: {presion_mes[i]:.2f} hPa\n")
    else:
        print(f"No hay datos para el mes {i+1}\n")