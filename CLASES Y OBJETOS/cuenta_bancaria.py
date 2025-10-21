# ========================== CUENTA BANCARIA ==========================
# =====================================================================
# Crea una clase "CuentaBancaria" con atributos como número de cuenta y saldo. 
# Implementa métodos para depositar y retirar dinero, y muestra el saldo actual.

class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo = 0):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
        print(f"Se depositaron {monto} €. Saldo actual: {self.saldo} €")

    def retirar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print(f"Se ha retirado {monto} €. Saldo actual: {self.saldo} €")
        else:
            print("Saldo insuficiente")
    
    def mostrar_saldo(self):
        print(f"El saldo actual: {self.saldo} €")

# Ejemplo de uso
cuenta = CuentaBancaria("1500") # El valor que se introduce como parametro asociado a la variable cuenta se trata del numero de cuenta
cuenta.depositar(100)
cuenta.retirar(50)
cuenta.mostrar_saldo()
