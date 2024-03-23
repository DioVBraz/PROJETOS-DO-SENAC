'''Crie um sistema de reservas de voo em Python. Crie classes para representar voos,
passageiros e reservas. Implemente métodos para verificar a disponibilidade de voos, fazer
reservas, cancelar reservas e emitir bilhetes de embarque. O sistema deve permitir que os
passageiros façam reservas e consultem suas informações de voo.'''

import os

class Voo:
    def __init__(self, numero_voo, capacidade):
        self.numero_voo = numero_voo
        self.capacidade = capacidade
        self.reservas = []

    def verificar_disponibilidade(self):
        return len(self.reservas) < self.capacidade

    def fazer_reserva(self, passageiro):
        if self.verificar_disponibilidade():
            self.reservas.append(passageiro)
            return f"Reserva feita com sucesso para o voo {self.numero_voo}."
        else:
            return f"Desculpe, não há vagas disponíveis no voo {self.numero_voo}."

    def cancelar_reserva(self, nome_passageiro):
        for passageiro in self.reservas:
            if passageiro.nome == nome_passageiro:
                self.reservas.remove(passageiro)
                return f"Reserva no voo {self.numero_voo} cancelada com sucesso para {nome_passageiro}."
        return f"{nome_passageiro} não possui uma reserva no voo {self.numero_voo}."

    def listar_reservas(self):
        if self.reservas:
            return f"Reservas do voo {self.numero_voo}:\n" + "\n".join([f"{reserva.nome}" for reserva in self.reservas])
        else:
            return f"Não há reservas no voo {self.numero_voo}."

class Passageiro:
    def __init__(self, nome, ID):
        self.nome = nome
        self.ID = ID

def menu():
    print("\n--- Sistema de Reservas de Voos ---")
    print("1) Fazer reserva")
    print("2) Cancelar reserva")
    print("3) Consultar reservas")
    print("4) Sair")

def main():
    numero_voo = input("Digite o número do voo: ")
    capacidade_voo = int(input("Digite a capacidade do voo: "))
    voo = Voo(numero_voo, capacidade_voo)

    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        os.system('cls')

        if opcao == "1":
            nome = input("Digite o nome do passageiro: ")
            passageiro = Passageiro(nome, 1)  
            print(voo.fazer_reserva(passageiro))
        elif opcao == "2":
            nome = input("Digite o nome do passageiro: ")
            print(voo.cancelar_reserva(nome))
        elif opcao == "3":
            print(voo.listar_reservas())
        elif opcao == "4":
            print("Obrigado por usar o Sistema de Reservas de Voos. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
