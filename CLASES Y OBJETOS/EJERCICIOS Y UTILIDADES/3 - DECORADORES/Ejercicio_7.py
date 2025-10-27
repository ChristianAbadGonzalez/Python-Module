# ================================================================ DECORADORES - LOGGER CON TIEMPO DE EJECUCION ================================================================
# ==============================================================================================================================================================================

# Imagina que estás desarrollando un sistema complejo que incluye múltiples funciones críticas. 
# Para asegurarte de que todo funcione correctamente y para realizar un seguimiento del tiempo de ejecución de estas funciones, decides implementar un decorador de registro (logger) con tiempo de ejecución.

# El decorador debería realizar las siguientes acciones: 
#   1. Antes de llamar a la función original (puedes incluir cualquier función), debe imprimir un mensaje indicando que la función está a punto de ejecutarse. 
#   2. Después de que la función se haya ejecutado, debe imprimir un mensaje que incluya el tiempo que tardó la función en ejecutarse. 
#   3. Si la función original arroja una excepción, el decorador debe manejarla e imprimir un mensaje adecuado, indicando que se ha producido una excepción.

# A continuacion un ejemplo de una posible entrada y salida de la solucion:

import time

def logger_tiempo(funcion):
    def wrapper():
        # Imprimir tiempo de ejecución
        inicio = time.time()
        print(f"Invocando a la función '{funcion.__name__}' ...")

        try:
            resultado = funcion()
        
        except Exception as e:
            print(f"Se produjo un error en la funcion '{funcion.__name__}': {e}")
            raise

        # Llamada al evento del tiempo de ejecución
        fin = time.time()
        print(f"La función '{funcion.__name__} ha tardado {fin - inicio} segundos en ejecutarse'")

        return resultado
    
    return wrapper()

@logger_tiempo

# Funcion principal que calcula la serie de fibonacci
def mi_funcion():
    fib_serie = [0,1]
    for i in range(2,20):
        fib_serie.append(fib_serie[i-1] + fib_serie[i-2])
    return fib_serie
print(mi_funcion)