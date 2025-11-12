# CLASE CON ENCAPSULACIÓN
class Ejemplo:
    # Método constructor
    def __init__(self):
        # Atributo privado: solo accesible dentro de la clase
        # Python aplica "name mangling" → internamente se llama _Ejemplo__atributo_privado
        self.__atributo_privado = 30

    # Getter: método para OBTENER el valor del atributo privado
    def getter(self):
        return self.__atributo_privado

    # Setter: método para MODIFICAR (asignar) el valor del atributo privado
    def setter(self, valor):
        # Se añade una validación antes de modificar el atributo
        if valor > 0:
            self.__atributo_privado = valor
        else:
            print("El valor debe ser positivo")


# EJEMPLO DE USO

# Creamos una instancia de la clase Ejemplo
ejemplo = Ejemplo()


# Accedemos al valor inicial mediante el método getter
print(ejemplo.getter())    # → 30


# Usamos el setter para cambiar el valor con validación
ejemplo.setter(2)
print(ejemplo.getter())    # → 2 (el cambio fue aceptado)


# El getter sigue devolviendo el valor del atributo REAL interno
# porque el original (oculto) sigue existiendo con su nombre interno _Ejemplo__atributo_privado
print(ejemplo.getter())    # → 2
