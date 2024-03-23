'''# Projeto 1: Sistema de Gestão de Funcionários'''

import os

class Funcionario:
    def __init__(self, nome, ID, salario):
        self.nome = nome
        self.ID = ID
        self.salario = salario

    def calcular_salario(self):
        return self.salario

    def __str__(self):
        return f"Nome: {self.nome}, ID: {self.ID}, Salário: R$ {self.salario}"

class Gerente(Funcionario):
    def __init__(self, nome, ID, salario, departamento):
        super().__init__(nome, ID, salario)
        self.departamento = departamento

    def calcular_salario(self):
        return self.salario * 1.2

    def __str__(self):
        return f"Nome: {self.nome}, ID: {self.ID}, Salário: {self.salario}, Departamento: {self.departamento}"

class Gestao_Funcionarios:
    def __init__(self):
        self.funcionarios = []

    def contratar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def demitir_funcionario(self, ID):
        for funcionario in self.funcionarios:
            if funcionario.ID == ID:
                self.funcionarios.remove(funcionario)
                return f"Funcionário com ID {ID} demitido com sucesso."
        return f"Funcionário com ID {ID} não encontrado."

    def promover_funcionario(self, ID, novo_salario):
        for funcionario in self.funcionarios:
            if funcionario.ID == ID:
                funcionario.salario = novo_salario
                return f"Funcionário com ID {ID} promovido com sucesso."
        return f"Funcionário com ID {ID} não encontrado."

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(funcionario)

def main():
    sistema = Gestao_Funcionarios()
    
    while True:
        print()
        print("--- Sistema de Gestão de Funcionários ---")
        print("1) Contratar funcionário")
        print("2) Demitir funcionário")
        print("3) Promover funcionário")
        print("4) Listar funcionários")
        print("5) Sair")
        
        opcao = input("Escolha uma opção: ")
        os.system('cls')
        
        if opcao == "1":
            nome = input("Nome do funcionário: ")
            ID = int(input("ID do funcionário: "))
            salario = float(input("Salário do funcionário: R$ "))
            funcionario = Funcionario(nome, ID, salario)
            sistema.contratar_funcionario(funcionario)
            print(f"{nome} contratado com sucesso!")

        elif opcao == "2":
            ID = int(input("ID do funcionário a ser demitido: "))
            print(sistema.demitir_funcionario(ID))

        elif opcao == "3":
            ID = int(input("ID do funcionário a ser promovido: "))
            novo_salario = float(input("Novo salário: "))
            print(sistema.promover_funcionario(ID, novo_salario))

        elif opcao == "4":
            print("Lista de funcionários:")
            sistema.listar_funcionarios()

        elif opcao == "5":
            break

if __name__ == "__main__":
    main()