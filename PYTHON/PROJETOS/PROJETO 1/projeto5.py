Carrinho_Compras = []

while True:
    print("*"*30)
    print("Bem-vindo à Simulação de Carrinho de Compras!")
    print("Opções:")
    print("1 - Adicionar produto ao carrinho")
    print("2 - Ver carrinho")
    print("3 - Calcular total")
    print("4 - Sair")
    print("*"*30)

    Opcao = input("Escolha uma opção: ")

    if Opcao == "1":
        Produto = input("Digite o nome do produto: ")
        Preco_Produto = float(input("Digite o preço do produto: "))
        Carrinho_Compras.append({"produto": Produto, "preco": Preco_Produto})
        print(f"{Produto} foi adicionado ao carrinho.")

    elif Opcao == "2":
        if not Carrinho_Compras:
            print("Seu carrinho está vazio.")
        else:
            print("Produtos no carrinho:")
            for Item_Carrinho in Carrinho_Compras:
                print(f"{Item_Carrinho['produto']} - R${Item_Carrinho['preco']}")

    elif Opcao == "3":
        Total_Carrinho = sum(Item_Carrinho['preco'] for Item_Carrinho in Carrinho_Compras)
        print(f"Total do carrinho: R${Total_Carrinho:.2f}")

    elif Opcao == "4":
        print("Obrigado por usar a Simulação de Carrinho de Compras!")
        break

    else:
        print("Opção inválida. Tente novamente.")