# Crea una función recursiva llamada numero_triangular que calcule el n-ésimo
# número triangular. Un número triangular se obtiene al sumar todos los 
# números naturales desde 1 hasta n.

# Definimos la función numero_tiangular que toma un número entero n como argumento
# y devuelve el n-ésimo número triangular utilizando el método de recursividad.

def numero_triangular(n):
    # Comprobamos si n es igual a 1, en cuyo caso el número triangular es 1.
    if n == 1:
        return 1
    else: 
        # En el caso de que n sea mayor que 1, devolvemos n más el número triangular
        # del número anterior (n - 1).
        return n + numero_triangular(n - 1)
    
# Ejemplo de uso:
resultado = numero_triangular(5)
print(resultado)
# 5 + numero_triangular(4)
# 5 + 4 + numero_triangular(3)
# 5 + 4 + 3 + numero_triangular(2)
# 5 + 4 + 3 + 2 + numero_triangular(1)  
