'''Modifique o exercício anterior para criar um dicionário de dicionários, 
onde cada aluno é representado por um dicionário contendo idade e 
nota.'''

import os

alunos = {}

while True:
    nome = input("Informe o nome do aluno (ou Enter para sair): ")
    if nome.lower() == '':
        break 

    idade = int(input("Informe a idade do aluno: "))
    nota = float(input("Informe a nota do aluno: "))

    os.system("cls")

    aluno = {
        "Idade": idade,
        "Nota": nota
    }
    
    alunos[nome] = aluno

print("\nInformações dos alunos:")
for nome, info in alunos.items():
    print(f"Nome: {nome}, Idade: {info['Idade']}, Nota: {info['Nota']}")
