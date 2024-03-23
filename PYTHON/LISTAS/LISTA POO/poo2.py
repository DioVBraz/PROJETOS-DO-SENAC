'''# Exercício 2: Gerenciador de Estudantes'''

import os

class Estudante:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = 0

    def adicionar_notas(self, adicionar):
        if adicionar > 0:
            self.notas += adicionar

    def calcular_media(self):
        return self.notas / 5
            
    def informacoes_aluno(self):
        print("Nome do aluno:", self.nome)
        print("Matrícula do aluno:", self.matricula)
        print("Notas:", self.notas)
        print("Média das notas:", self.calcular_media())

estudante1 = Estudante(input("Digite o nome do estudante: "), input("Digite o número da matrícula do estudante: "))
estudante1.adicionar_notas(int(input("Digite a nota de português: ")))
estudante1.adicionar_notas(int(input("Digite a nota de matemática: ")))
estudante1.adicionar_notas(int(input("Digite a nota de física: ")))
estudante1.adicionar_notas(int(input("Digite a nota de química: ")))
estudante1.adicionar_notas(int(input("Digite a nota de inglês: ")))
os.system('cls')



estudante2 = Estudante(input("Digite o nome do segundo estudante: "), input("Digite o número da matrícula do estudante: "))
estudante2.adicionar_notas(int(input("Digite a nota de português: ")))
estudante2.adicionar_notas(int(input("Digite a nota de matemática: ")))
estudante2.adicionar_notas(int(input("Digite a nota de física: ")))
estudante2.adicionar_notas(int(input("Digite a nota de química: ")))
estudante2.adicionar_notas(int(input("Digite a nota de inglês: ")))
os.system('cls')

print("--- Informações do primeiro estudante ---")
estudante1.informacoes_aluno()

print()

print("--- Informações do estudante ---")
estudante2.informacoes_aluno()
    