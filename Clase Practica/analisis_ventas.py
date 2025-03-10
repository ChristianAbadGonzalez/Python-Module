# --- ANALISIS DE VENTAS: ---
# --- Supongamos que eres el propietario de una tienda en línea y tienes una lista de ventas de los últimos 30 días. ---
# --- Quieres analizar las ventas por día de la semana para identificar los días de mayor venta. ---

# --- Creamos una lista de ventas en la cual vamos almacenar los días de la semana y otra lista con las ventas generados en el mes ---
# --- A partir del valor asociado a cada día de la semana obtendremos la suma total de ventas generadas en un mes, en referencia a los días de la semana. ---
ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110, 140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250] 

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# --- Creamos una lista almacenada con valores nulos para que cuando el bucle acceda al día en cuestión pueda almacenar el valor introducido. ---
ventas_totales = [0, 0, 0, 0, 0, 0, 0] 

# --- Accedemos al bucle de ventas para poder. ---
# --- Inicializamos el día de venta con valor 0 para poder ingresarle posteriormente un valor. ---
dia_venta = 0

for venta in ventas:
    ## sumar para cada dia de la semana las ventas realizadas
    ventas_totales[dia_venta] = ventas_totales[dia_venta] + venta
    
    # --- Aumentamos el valor de día de venta en +1 ---
    dia_venta = dia_venta + 1

    # --- Si el bucle asociado al valor día llega al máximo, este valor se inicializa nuevamente a 0 para poder seguir rellenandolo ---
    if dia_venta == 7:
        dia_venta = 0

# --- Imprimir las ventas realizadas para cada dia de la semana a lo a largo de ese mes
for i in range(len(dias_semana)):
    print(dias_semana[i]+ ":", ventas_totales[i])