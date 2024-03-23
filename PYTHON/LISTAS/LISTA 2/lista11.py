Total_Geral = 0

while True:
    Codigo = int(input("Digite o código do item (ou 0 para encerrar o pedido): "))
    
    if Codigo == 0:
        break
    
    Quantidade = int(input("Digite a quantidade desejada: "))
    
    if Codigo == 100:
        Preco = 1.20
        Item = "Cachorro Quente"

    elif Codigo == 101:
        Preco = 1.30
        Item = "Bauru Simples"

    elif Codigo == 102:
        Preco = 1.50
        Item = "Bauru com ovo"

    elif Codigo == 103:
        Preco = 1.20
        Item = "Hambúrguer"

    elif Codigo == 104:
        Preco = 1.30
        Item = "Cheeseburguer"

    elif Codigo == 105:
        Preco = 1.00
        Item = "Refrigerante"
    else:
        print("Código de item inválido. Tente novamente")
        continue
    
    Item_Valor = Preco * Quantidade
    print(f"Item: {Item}")
    print(f"Quantidade: {Quantidade}")
    print(f"Preço: R$ {Preco:.2f}")
    print(f"Valor a ser pago pelo item: R$ {Item_Valor:.2f}")
    
    Total_Geral += Item_Valor

print(f"Total geral do pedido: R$ {Total_Geral:.2f}")