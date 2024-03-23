'''Crie um programa que permita aos professores registrarem notas de alunos e calcular 
médias de notas. Use um dicionário onde as chaves são os nomes dos alunos e os 
valores são listas de notas.'''

import os 

def calcular_media(notas):
    if len(notas) == 0:
        return 0
    else:
        return sum(notas) / len(notas)

notas_alunos = {}

while True:
    print("*" * 30)
    print("Menu:")
    print("1. Adicionar notas de um aluno")
    print("2. Calcular média de um aluno")
    print("3. Sair")
    print("*" * 30)

    escolha = input("Escolha uma opção: ")

    os.system("cls")

    if escolha == "1":
        nome_aluno = input("Digite o nome do aluno: ")
        notas_str = input("Digite as notas do aluno separadas por espaço: ")
        notas = [float(nota) for nota in notas_str.split()]
        
        if nome_aluno in notas_alunos:
            notas_alunos[nome_aluno].extend(notas)
        else:
            notas_alunos[nome_aluno] = notas
        
        print("Notas adicionadas com sucesso!")

    elif escolha == "2":
        nome_aluno = input("Digite o nome do aluno para calcular a média: ")
        if nome_aluno in notas_alunos:
            media = calcular_media(notas_alunos[nome_aluno])
            print(f"A média de {nome_aluno} é: {media:.2f}")
        else:
            print(f"O aluno {nome_aluno} não foi encontrado.")

    elif escolha == "3":
        break