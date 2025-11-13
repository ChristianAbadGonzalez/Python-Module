from typing import Protocol

# Protocols pequeños por capacidad (ISP)
class IDepositar(Protocol):
    def depositar(self, monto: float) -> None: pass

class IRetirar(Protocol):
    def retirar(self, monto: float) -> None: pass

class ITransferir(Protocol):
    def transferir(self, monto: float, a_cuenta: str) -> None: pass

# Implementaciones concretas de cuentas bancarias
class CuentaAhorros(IDepositar, IRetirar):
    def depositar(self, monto: float) -> None:
        print(f"Depositando {monto} en cuenta de ahorros")

    def retirar(self, monto: float) -> None:
        print(f"Retirando {monto} de cuenta de ahorros")

# Implementación completa de CuentaCorriente
class CuentaCorriente(IDepositar, IRetirar, ITransferir):
    def depositar(self, monto: float) -> None:
        print(f"Depositando {monto} en cuenta corriente")

    def retirar(self, monto: float) -> None:
        print(f"Retirando {monto} de cuenta corriente")

    def transferir(self, monto: float, a_cuenta: str) -> None:
        print(f"Transfiriendo {monto} de cuenta corriente a cuenta {a_cuenta}")


# Funciones utilitarias polimórficas por capacidad
def hacer_deposito(cuenta: IDepositar, monto: float) -> None:
    cuenta.depositar(monto)

def hacer_retiro(cuenta: IRetirar, monto: float) -> None:
    cuenta.retirar(monto)

def realizar_pago(cuenta: ITransferir, monto: float, a_cuenta: str) -> None:
    cuenta.transferir(monto, a_cuenta)


# Ejemplo de uso
ahorros = CuentaAhorros()
corriente = CuentaCorriente()

hacer_deposito(ahorros, 100)
hacer_retiro(ahorros, 50)

hacer_deposito(corriente, 100)
hacer_retiro(corriente, 50)
realizar_pago(corriente, 20, "ABCSK189148")

# La cuenta de ahorros no implementa ITransferir, evitando errores de tiempo de ejecución