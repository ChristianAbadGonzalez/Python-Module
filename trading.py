# --- Un bot de trading está programado para realizar ciertas acciones con respecto a un producto financiero. ---
# --- Crea un script de manera que dado un precio introducido por el usuario, si el precio del producto está por debajo de 100 dólares, ---
# --- el bot imprima por pantalla la orden de comprar. Si está entre 100 y 150 dolores (ambos incluidos) el bot deberá imprimir la orden de hold. ---
# --- Si el precio está estrictamente por encima de 150 el bot deberá imprimir la orden de vender. ---

precio = float(input("Introduce el precio actual del producto financiero en dólares: "))

# Lógica de decisión del bot de trading
if precio < 100:
    print("📉 Orden: COMPRAR 💰 (El precio está por debajo de $100).")
elif 100 <= precio <= 150:
    print("⏸️ Orden: HOLD 🔄 (El precio está entre $100 y $150).")
else:
    print("📈 Orden: VENDER 🚀 (El precio está por encima de $150).")