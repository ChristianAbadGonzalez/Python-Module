# ATRIBUTOS PRIVADOS
class Ejemplo:
    # Método constructor
    def __init__(self):
        # Atributo PRIVADO (dos guiones bajos "__")
        # Solo puede ser accedido dentro de la propia clase
        self.__atributo_privado = 10

    # Método público (getter) que accede al atributo privado
    def get_atributo(self):
        # Imprime el doble del valor del atributo privado
        print(f"{self.__atributo_privado * 2}")

# EJEMPLO DE USO
# Creamos una instancia de la clase
valor = Ejemplo()
# Llamamos al método PÚBLICO, que SÍ tiene acceso al atributo privado.
valor.get_atributo()
# Intentamos acceder al atributo privado directamente (no es correcto)
valor.__atributo_privado = 20


# ATRIBUTOS PROTEGIDOS
class Ejemplo:
    # Método constructor
    def __init__(self):
        # Atributo PROTEGIDO (un guion bajo "_")
        # Por convención: se puede acceder desde fuera o desde subclases,
        # pero NO se recomienda modificarlo directamente.
        self._atributo_protegido = 20

    # Método público (getter) recomendado para acceder al atributo protegido
    def get_atributo(self):
        print(self._atributo_protegido)

# EJEMPLO DE USO
# Creamos una instancia de la clase
valor = Ejemplo()
# Intentamos acceder al atributo protegido directamente (no es correcto pero posible)
print(valor._atributo_protegido)
# Llamamos al método PÚBLICO, que SÍ tiene acceso al atributo protegido.
valor.get_atributo()