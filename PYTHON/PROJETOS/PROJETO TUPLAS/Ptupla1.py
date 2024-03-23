Lista_Produtos = []

while True:
    print("*" *30)
    print("Escolha uma opção:")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Atualizar produto")
    print("4. Remover produto")
    print("5. Sair")
    print("*" *30)
    
    Opcao = input("Digite o número da opção desejada: ")
    
    if Opcao == '1':
        Produto_Nome = input("Digite o nome do produto: ")
        Produto_Preco = float(input("Digite o preço do produto: "))
        Produto_Quantidade = int(input("Digite a quantidade do produto: "))
        Produto = (Produto_Nome, Produto_Preco, Produto_Quantidade)
        Lista_Produtos.append(Produto)
        print("Produto cadastrado")
    
    elif Opcao == '2':
        print("*" *30)
        print("Lista de produtos:")
        for i, Produto in enumerate(Lista_Produtos, start=1):
            Nome, Preco, Quantidade = Produto
            print(f"{i}. Nome: {Nome} | Preço: R${Preco:.2f} | Quantidade do produto: {Quantidade}")
            print("*" *30)
    
    elif Opcao == '3':
        print("*" *30)
        print("Lista de produtos:")
        for i, Produto in enumerate(Lista_Produtos, start=1):
            Nome, Preco, Quantidade = Produto
            print(f"{i}. Nome: {Nome}, Preço: R${Preco:.2f}, Quantidade do produto: {Quantidade}")
            print("*" *30)
        
        Atualizar = int(input("Digite o número do produto que deseja atualizar: "))
        if 1 <= Atualizar <= len(Lista_Produtos):
            Novo_Nome = input("Digite o novo nome do produto: ")
            Novo_Preco = float(input("Digite o novo preço do produto: "))
            Nova_Quantidade = int(input("Digite a nova quantidade do produto: "))
            Lista_Produtos[Atualizar - 1] = (Novo_Nome, Novo_Preco, Nova_Quantidade)
            print("Produto atualizado")
        else:
            print("Não é possível atualizar esse produto")
    
    elif Opcao == '4':
        print("Lista de produtos:")
        for i, Produto in enumerate(Lista_Produtos, start=1):
            Nome, Preco, Quantidade = Produto
            print(f"{i}. Nome: {Nome} | Preço: R${Preco:.2f} | Quantidade do produto: {Quantidade}")
        
        Remover = int(input("Digite o número do produto que deseja remover: "))
        if 1 <= Remover <= len(Lista_Produtos):
            del Lista_Produtos[Remover - 1]
            print("Produto removido")
        else:
            print("Não é possível remover esse produto")
    
    elif Opcao == '5':
        break
    
    else:
        print("Não é possível sair do programa.")