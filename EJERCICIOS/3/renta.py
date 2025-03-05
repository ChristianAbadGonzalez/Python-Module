# --- Pedir datos del usuario: Edad, Ingresos ---
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
ingresos = float(input("Introduce tus ingresos mensuales: "))

# --- Calcular la renta anual ---
renta_anual = ingresos * 12

# --- Comprobar si el usuario en cuestion tiene que tributar ---
if edad >= 18 and ingresos >= 1000:
    print(nombre.title(), "eres suceptible de tener que tributar por tus ingresos anuales de", renta_anual, "euros")

    if 12000 <= renta_anual <= 15000:
        print("Tributarás un 5% de tus ingresos")
    elif 15000 < renta_anual <= 25000:
        print("Tributarás un 15% de tus ingresos")
    elif 25000 < renta_anual <= 35000:
        print("Tributarás un 20% de tus ingresos")
    elif 35000 < renta_anual <= 60000:
        print("Tributarás un 30% de tus ingresos")
    else:
        print("Tributarás un 40% de tus ingresos")
else:
    print(nombre.title(), "no tienes que tributar por tus ingresos anuales de", renta_anual, "euros")
    