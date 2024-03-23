class Cliente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome 
        self.cpf = cpf
        self.idade = idade

class ContaBancaria:
    def __init__(self, numero_conta, cliente):
        self.numero_conta = numero_conta
        self.cliente = cliente
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor

    def consultar_saldo(self):
        return self.saldo
    
    def informacoes_conta(self):
        print("Número da conta:", self.numero_conta)
        print("Nome do titular:", self.cliente.nome)
        print("CPF do titular:", self.cliente.cpf)
        print("Idade do titular:", self.cliente.idade)
        print("Saldo da conta:", self.saldo)

cliente1 = Cliente("Alice", "123.456.789-00", 30)
cliente2 = Cliente("Bob", "987.654.321-00", 25)

conta1 = ContaBancaria("001", cliente1)
conta2 = ContaBancaria("002", cliente2)

conta1.depositar(1000)
conta2.depositar(500)
conta1.sacar(300)
conta2.sacar(700)

print("Informações da conta 1:")
conta1.informacoes_conta()

print()

print("Informações da conta 2:")
conta2.informacoes_conta()