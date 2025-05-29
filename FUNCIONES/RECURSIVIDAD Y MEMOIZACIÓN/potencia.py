# Implementa una función recursiva llamada potencia que calcule el resultado de elevar un número a una potencia dada. 
# Puedes asumir que tanto el número como la potencia son enteros no negativos.

def potencia(base, exponente):
    # Caso base: cualquier número elevado a la potencia 0 es 1.
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Solicitamos al usuario que introduzca la base y el exponente.
base = int(input("Introduce la base (número entero no negativo): "))
exponente = int(input("Introduce el exponente (número entero no negativo): "))

# Llamamos a la función potencia y mostramos el resultado.
resultado = potencia(base, exponente)
print(f"El numero base {base} elevado al valor del exponente {exponente} da como resultado: {resultado}")

