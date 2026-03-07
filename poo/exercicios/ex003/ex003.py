#Classe
class ContaBancaria:
    """
    Cria uma conta bancaria que permite fazer saques e depósitos.
    """
    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso. Titular: {self.titular}. Saldo atual: R${self.saldo}')

    def __str__(self):
        return f'Conta: {self.id}  //  Títular: {self.titular}  //  Saldo: R${self.saldo}'

    def deposito(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor} autorizado')

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor} autorizado')
        else:
            print(f'Saque de R${valor} não autorizado, saldo insuficiente')



#Declaração de objeto
conta1 = ContaBancaria(1002, 'João Vitor', 35000)
conta1.deposito(5000)
print(conta1)
conta1.saque(2000)
print(conta1)