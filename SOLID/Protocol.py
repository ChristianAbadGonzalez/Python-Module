from typing import Protocol

# Protocols que modelan capacidades específicas (ISP)
class IDepositar(Protocol):
    def depositar(self, monto: float) -> None: pass

class IRetirar(Protocol):
    def retirar(self, monto: float) -> None: pass

class ITransferir(Protocol):
    def transferir(self, monto: float, a_cuenta: str) -> None: pass

# Implementaciones concretas de cuentas bancarias
class CuentaAhorros:
    def depositar(self, monto: float) -> None:
        print(f"Depositando {monto} en cuenta de ahorros")

    def retirar(self, monto: float) -> None:
        print(f"Retirando {monto} de cuenta de ahorros")

# Implementación incompleta de transferencia para ilustrar ISP
class CuentaCorriente:
    def depositar(self, monto: float) -> None:
        print(f"Depositando {monto} en cuenta corriente")

    def retirar(self, monto: float) -> None:
        print(f"Retirando {monto} de cuenta corriente")

    def transferir(self, monto: float, a_cuenta: str) -> None:
        print(f"Transfiriendo {monto} de cuenta corriente a cuenta {a_cuenta}")


# Funciones polimórficas por capacidad
def hacer_deposito(cuenta: IDepositar, monto: float) -> None:
    cuenta.depositar(monto)

def hacer_retiro(cuenta: IRetirar, monto: float) -> None:
    cuenta.retirar(monto)

def realizar_pago(cuenta: ITransferir, monto: float, a_cuenta: str) -> None:
    cuenta.transferir(monto, a_cuenta)


# Ejemplo de uso
cuenta_corriente = CuentaCorriente()
cuenta_ahorros = CuentaAhorros()

hacer_deposito(cuenta_corriente, 100)
hacer_retiro(cuenta_corriente, 50)
realizar_pago(cuenta_corriente, 20, "ABCSK189148")

hacer_deposito(cuenta_ahorros, 200)
hacer_retiro(cuenta_ahorros, 80)

# La cuenta de ahorros no implementa ITransferir, evitando errores de tiempo de ejecución