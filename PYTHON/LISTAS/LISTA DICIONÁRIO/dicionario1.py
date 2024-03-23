'''Dado um dicionário de informações de alunos, escreva um programa que 
filtre os alunos que têm uma nota superior a 85 e crie um novo dicionário 
com esses alunos.'''

alunos = {}

while True:
    nome = input("Digite o nome do aluno(a) (ou pressione Enter para parar): ")
    if nome.lower() == '':
        break
    nota = float(input("Digite a nota do aluno(a): "))
    alunos[nome] = nota

alunos_aprovados = {}

for nome, nota in alunos.items():
    if nota > 85:
        alunos_aprovados[nome] = nota

print("Alunos com nota acima de 85:")
for nome, nota in alunos_aprovados.items():
    print(f"Aluno: {nome}, nota: {nota}")

