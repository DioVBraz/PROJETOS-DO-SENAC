'''Crie um programa que permita aos usuários gerenciarem uma lista de tarefas. Os 
usuários devem poder adicionar, listar e marcar tarefas como concluídas. Use um 
dicionário onde as chaves são as tarefas e os valores indicam se a tarefa foi concluída 
ou não.'''

import os

dicio_tarefas = {}

while True:
    print("*" * 30)
    print("--- Gerenciador de Tarefas ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Sair")
    print("*" * 30)

    escolha = input("Escolha uma opção: ")
    os.system("cls")

    if escolha == '1':
        tarefa = input("Digite a tarefa que deseja adicionar: ")
        dicio_tarefas[tarefa] = False 

    elif escolha == '2':
        print("--- Lista de dicio_tarefas ---")
        for tarefa, concluida in dicio_tarefas.items():
            status = "Concluída" if concluida else "Não Concluída"
            print(f"{tarefa}: {status}")

    elif escolha == '3':
        tarefa_concluir = input("Digite a tarefa que deseja marcar como concluída: ")
        if tarefa_concluir in dicio_tarefas:
            dicio_tarefas[tarefa_concluir] = True
            print(f"A tarefa '{tarefa_concluir}' foi marcada como concluída.")
        else:
            print(f"A tarefa '{tarefa_concluir}' não foi encontrada na lista.")

    elif escolha == '4':
        break