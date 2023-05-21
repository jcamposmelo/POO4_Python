class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")


# Exemplo de uso
conta = ContaBancaria("Jorge", 100)  # Criar uma nova conta com saldo inicial de R$ 100

conta.depositar(250)  # Depositar R$ 50
conta.consultar_saldo()  # Saldo atual: R$ 150.00

conta.sacar(30)  # Sacar R$ 30
conta.consultar_saldo()  # Saldo atual: R$ 120.00

conta.sacar(200)  # Tentar sacar R$ 200 (saldo insuficiente)
conta.consultar_saldo()  # Saldo atual: R$ 120.00
