# --- RESTAURANTE ONLINE ---

# --- Solicitamos al usuario que elija una de las opciones disponibles de la carta ---
entrante = input("¿Désea un entrante? (si/no): ")
hamburguesa = input("¿Qué tipo de hamburguesa quieres? (Clasica/Smash/Vegana): ")
patatas = input("¿Désea añadir patatas? (si/no): ")
bebida = input("¿Désea añadir una bebida? (si/no): ")
postre = input("¿Désea añadir un postre? (si/no): ")

# --- ENTRANTE ---
if entrante == "si":
    print("Los entrantes disponibles en carta son: Alitas/Nachos/Tequeños")
    entrante = input("¿Qué entrante desea pedir? (Alitas/Nachos/Tequeños): ")
    print("Entrante seleccionado: " + entrante)
else:
    entrante = "sin entrante"

# --- HAMBURGUESA SELECCIONADA CON ENTRANTES---
if hamburguesa.lower() == "clasica" or hamburguesa.lower() == "smash":
    print("Los ingredientes extras disponibles son: Queso Cheddar/Bacon/Huevo")
    extra = input("¿Quieres añadir algún extra? (si/no): ")
    if extra == "si":
        extra = input("¿Qué extra quieres? (cheddar/bacon/huevo): ")
        print("Extra seleccionado: " + extra)
    else:
        extra = "sin extras"
elif hamburguesa.lower() == "vegana":
    print("Los ingredientes extras disponibles son: Queso Vegano/Bacon Vegano/Huevo Vegano")
    extra = input("¿Quieres añadir algún extra? (si/no): ")
    if extra == "si":
        extra = input("¿Qué extra quieres? (queso vegano/bacon vegano/huevo vegano): ")
        print("Extra seleccionado: " + extra)
    else:
        extra = "sin extras"

# --- PATATAS, BEBIDA Y POSTRE ---
if patatas == "si":
    print("Las patatas disponibles en carta son: Fritas/Gajo")
    patatas = input("¿Qué tipo de patatas quieres? (Fritas/Gajo): ")
    print("Patatas seleccionadas: " + patatas)
else:
    patatas = "sin patatas"

if bebida == "si":
    print("Las bebidas disponibles en carta son: Refresco/Cerveza/Agua")
    bebida = input("¿Qué bebida quieres? (Refresco/Cerveza/Agua): ")
    print("Bebida seleccionada: " + bebida)
else:
    bebida = "sin bebida"

if postre == "si":
    print("Los postres disponibles en carta son: Tarta de Queso/Brownie/Helado")
    postre = input("¿Qué postre quieres? (Tarta de Queso/Brownie/Helado): ")
    print("Postre seleccionado: " + postre)
else:
    postre = "sin postre"

# --- IMPRIMIMOS EL PEDIDO REALIZADO ---
print(f"Usted ha elegido el siguiente pedido:\n"
      f"Entrante: {entrante}\n"
      f"Hamburguesa: {hamburguesa}\n"
      f"Extra: {extra}\n"
      f"Patatas: {patatas}\n"
      f"Bebida: {bebida}\n"
      f"Postre: {postre}\n"
      "¡Gracias por su pedido!")
