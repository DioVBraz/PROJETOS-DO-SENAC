'''Desenvolva um programa de lista de tarefas onde o usuário pode 
adicionar, visualizar e marcar tarefas como concluídas. Cada operação 
deve ser gerenciada por funções.'''

Tarefa = []

while True:
    print("*"*30)
    print("---- Lista de Tarefas ----")
    print("1. Adicionar Tarefa")
    print("2. Visualizar Tarefa")
    print("3. Marcar Tarefas")
    print("4. Sair")
    print("*"*30)

    def Adicionar_Tarefa(Tarefa):
        Adicionar = input("Digite a tarefa a ser adicionada: ")
        Tarefa.append(Adicionar)
        print(f"Tarefa '{Adicionar}' adicionada com sucesso!")

    def Visualizar_Tarefa(Tarefa):
        print("Tarefas adicionadas:")
        for i, Adicionar in enumerate(Tarefa):
                print(f"{i + 1}. {Adicionar}")

    def Marcar_Tarefa(Tarefa):
            Numero_Tarefa = int(input("Digite o número da tarefa a ser removida: ")) - 1
            if 0 <= Numero_Tarefa < len(Tarefa):
                Tarefa_Concluida = Tarefa.pop(Numero_Tarefa)
                print(f"Tarefa '{Tarefa_Concluida}' concluída com sucesso!")
            else:
                print("Número de tarefa inválido. Tente novamente.")

    Escolha = Escolha = input("Escolha uma opção: ")

    if Escolha.lower() == '1':
        Adicionar_Tarefa(Tarefa)

    elif Escolha.lower() == '2':
        Visualizar_Tarefa(Tarefa)

    elif Escolha.lower() == '3':
        Marcar_Tarefa(Tarefa)

    elif Escolha.lower() == '4':
        break