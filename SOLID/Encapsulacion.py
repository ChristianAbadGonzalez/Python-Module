# ATRIBUTOS PRIVADOS
class Ejemplo:
    def __init__(self):
        self.__atributo_privado = 10

    def get_atributo(self):
        print(f"{ self.__atributo_privado*2}")

# EJEMPLO DE USO
# Creamos una instancia de la clase
valor = Ejemplo()
# Llamamos al método PÚBLICO, que SÍ tiene acceso al atributo privado.
valor.get_atributo()
# Intentamos acceder al atributo privado directamente (no es correcto)
valor.__atributo_privado = 20


# ATRIBUTOS PROTEGIDOS
class Ejemplo:
    def __init__(self):
        self._atributo_protegido = 20

    def get_atributo(self):
        print(self._atributo_protegido)


# EJEMPLO DE USO
# Creamos una instancia de la clase
valor = Ejemplo()
# Intentamos acceder al atributo protegido directamente (no es correcto pero posible)
print(valor._atributo_protegido)
# Llamamos al método PÚBLICO, que SÍ tiene acceso al atributo protegido.
valor.get_atributo()