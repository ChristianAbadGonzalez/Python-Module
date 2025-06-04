# Crea una función recursiva llamada suma_lista que calcule la suma de todos 
# los elementos de una lista de enteros. Puedes asumir que la lista no está 
# vacía.

# Definimos la funcion suma_lista que toma una lista de enteros como argumento
# y devuelve la suma de sus elementos utilizando el metodo de recursividad.
def suma_lista(lista):
    # Como primer caso, comprobamos si la lista tiene algún elemento.
    if len(lista) == 1:
        return lista[0]
    else:
        # En el caso de que la lista tenga más de un elemento,
        # devolvemos la suma del primer elemento y la suma del resto de la lista.
        return lista[0] + suma_lista(lista[1:])

# Ejemplo de uso:
lista = [1, 2, 3, 4, 5]
print(suma_lista(lista))

"""
1 + suma_lista([2, 3, 4, 5])
1 + 2 + suma_lista([3, 4, 5])
1 + 2 + 3 + suma_lista([4, 5])
# 1 + 2 + 3 + 4 + suma_lista([5])
# 1 + 2 + 3 + 4 + 5 + suma_lista([])
"""