'''Crie um programa que combine dicionários com informações de alunos, 
incluindo nome, idade e notas. Os dados estão armazenados em listas 
separadas.'''

import os

alunos = []

while True:
    nome = input("Informe o nome do aluno (ou Enter para sair): ")
    if nome.lower() == '':
        break  

    idade = int(input("Informe a idade do aluno: "))
    nota = float(input("Informe a nota do aluno: "))

    os.system("cls")
    
    aluno = {
        "Nome": nome,
        "Idade": idade,
        "Nota": nota
    }
    alunos.append(aluno)

print("Informações dos alunos:")
for aluno in alunos:
    print(f"Nome: {aluno['Nome']} | Idade: {aluno['Idade']} | Nota: {aluno['Nota']}")
