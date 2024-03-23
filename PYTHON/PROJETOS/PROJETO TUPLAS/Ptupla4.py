Lista_Livros = []

while True:
    print("*" *30)
    print("Menu:")
    print("1. Adicionar livro")
    print("2. Remover livro")
    print("3. Atualizar informações de um livro")
    print("4. Listar livros disponíveis")
    print("5. Sair")
    print("*" *30)
    
    Opcao = input("Digite o número da opção desejada: ")
    
    if Opcao == "1":
        Titulo = input("Digite o título do livro: ")
        Autor = input("Digite o autor do livro: ")
        Preco = float(input("Digite o preço do livro: "))
        Quantidade = int(input("Digite a quantidade em estoque: "))
        Livros = (Titulo, Autor, Preco, Quantidade)

        Lista_Livros.append(Livros)
        print("Livro adicionado com sucesso!")

    elif Opcao == "2":
        Titulo = input("Digite o título do livro que deseja remover: ")
        for Livros in Lista_Livros:
            if Livros[0] == Titulo:
                Lista_Livros.remove(Livros)
                print("Livro removido com sucesso!")
                break
        else:
            print("Livro não encontrado!")

    elif Opcao == "3":
        Titulo = input("Digite o título do livro que deseja atualizar: ")
        for Atualizar, Livros in enumerate(Lista_Livros):
            if Livros[0] == Titulo:
                Novo_Titulo = input("Digite o novo título (ou deixe em branco para manter o mesmo): ")
                Novo_Autor = input("Digite o novo autor (ou deixe em branco para manter o mesmo): ")
                Novo_Preco = input("Digite o novo preço (ou deixe em branco para manter o mesmo): ")
                Novo_Estoque = input("Digite a nova quantidade em estoque (ou deixe em branco para manter o mesmo): ")
                
                Novo_Titulo = Novo_Titulo if Novo_Titulo else Livros[0]
                Novo_Autor = Novo_Autor if Novo_Autor else Livros[1]
                Novo_Preco = float(Novo_Preco) if Novo_Preco else Livros[2]
                Novo_Estoque = int(Novo_Estoque) if Novo_Estoque else Livros[3]
                
                Lista_Livros[Atualizar] = (Novo_Titulo, Novo_Autor, Novo_Preco, Novo_Estoque)
                
                print("Informações do livro atualizadas com sucesso!")
                break
        else:
            print("Livro não encontrado!")

    elif Opcao == "4":
        print("Lista de livros disponíveis:")
        for i, Livros in enumerate(Lista_Livros, 1):
            Titulo, Autor, Preco, Quantidade = Livros
            print(f"{i}. Título: {Titulo}, Autor: {Autor}, Preço: R$ {Preco:.2f}, Estoque: {Quantidade}")

    elif Opcao == "5":
        break
    else:
        print("Não é possível sair do programa.")