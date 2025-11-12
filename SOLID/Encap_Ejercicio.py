# Definición de la clase CuentaBancaria
class CuentaBancaria:
    # Método constructor que inicializa los atributos principales de la cuenta
    def __init__(self, numero_cuenta, saldo):
        # Atributo protegido (por convención, un solo guión bajo)
        # Indica que este valor puede ser accedido por subclases,
        # pero se recomienda no modificarlo directamente fuera de la clase.
        self._numero_cuenta = numero_cuenta

        # Atributo privado (doble guión bajo)
        # Solo puede ser accedido dentro de la propia clase.
        # Python le aplica "name mangling" => el atributo pasa a llamarse internamente _CuentaBancaria__saldo
        self.__saldo = saldo

    # Método getter para obtener el saldo (forma correcta)
    def get_saldo(self):
        return self.__saldo

    # Método público para realizar depósitos en la cuenta
    def depositar(self, monto):
        # Suma el monto depositado al saldo actual
        self.__saldo += monto

    # Método público para retirar dinero de la cuenta
    def retirar(self, monto):
        # Verifica si el saldo es suficiente antes de retirar
        if self.__saldo >= monto:
            self.__saldo -= monto
        else:
            print("Saldo insuficiente")


# ====================
#     MODO DE USO
# ====================

# Se crea una instancia o "objeto" de la clase CuentaBancaria con número y saldo inicial
cuenta = CuentaBancaria("12345", 1000)

# Acceso al atributo protegido (no recomendado, pero posible)
print(cuenta._numero_cuenta)

# ❌ NO recomendado:
# Acceder directamente al atributo privado fuera de la clase.
# print(cuenta._CuentaBancaria__saldo)
# Aunque es posible (por el mecanismo de name mangling), rompería la encapsulación.

# ✅ Forma CORRECTA de acceder al saldo:
valor = cuenta.get_saldo()
print(f"Saldo actual (usando getter): {valor} €")

# Uso correcto de los métodos públicos (interfaz segura de la clase)
cuenta.depositar(500)   # Aumenta el saldo en 500
cuenta.retirar(200)     # Resta 200 del saldo

# Verificamos el nuevo saldo usando el método getter
print(f"Saldo final (usando getter): {cuenta.get_saldo()} €")