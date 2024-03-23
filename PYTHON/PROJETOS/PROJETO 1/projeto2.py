Lista_Tarefas = []

while True:
    print("*"*30)
    print("---- Aplicativo de Lista de Tarefas ----")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Listar Tarefas Pendentes")
    print("4. Sair")
    print("*"*30)

    Escolha = input("Escolha uma opção: ")

    if Escolha == "1":
        Tarefa = input("Digite a tarefa a ser adicionada: ")
        Lista_Tarefas.append(Tarefa)
        print(f"Tarefa '{Tarefa}' adicionada com sucesso!")

    elif Escolha == "2":
        if len(Lista_Tarefas) == 0:
            print("Não há tarefas para remover.")
        else:
            print("Tarefas Pendentes:")
            for i, Tarefa in enumerate(Lista_Tarefas):
                print(f"{i + 1}. {Tarefa}")

            Numero_Tarefa = int(input("Digite o número da tarefa a ser removida: ")) - 1

            if 0 <= Numero_Tarefa < len(Lista_Tarefas):
                Tarefa_Removida = Lista_Tarefas.pop(Numero_Tarefa)
                print(f"Tarefa '{Tarefa_Removida}' removida com sucesso!")
            else:
                print("Número de tarefa inválido. Tente novamente.")

    elif Escolha == "3":
        if len(Lista_Tarefas) == 0:
            print("Não há tarefas pendentes.")
        else:
            print("Tarefas Pendentes:")
            for i, Tarefa in enumerate(Lista_Tarefas):
                print(f"{i + 1}. {Tarefa}")

    elif Escolha == "4":
        print("Saindo do aplicativo. Até a próxima!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")