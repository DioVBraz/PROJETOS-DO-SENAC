Itens = {
    'Jogo': 220,
    'Fone': 130,
    'Computador': 2000,
    'Mouse': 110,
    'Pen drive': 30,
    'Cabo USB': 10,
    'Placa de vídeo': 1230,
    'Celular': 800,
    'Carregador': 25,
    'Capa de celular': 20
}

Preco_Total = 0

while True:
    Pedidos = input("Digite o nome do item desejado (Digite 'sair' para sair): ")

    if Pedidos == 'sair':
        print("Fim")
        break

    Valor_Itens = Itens.get(Pedidos)

    if Valor_Itens is None:
        print("Nome de item inválido. Tente novamente")
        continue

    Quantidade = input(f"Digite a quantidade desejada do {Pedidos}: ")

    if not Quantidade.isdigit():
        print("Quantidade inválida. Tente novamente")
        continue

    Quantidade = int(Quantidade)

    Preco_Total += Valor_Itens * Quantidade

    print(f"Valor a ser pago pelo {Pedidos}: R$ {Valor_Itens * Quantidade:.2f}")

print(f"Preço total do pedido: R${Preco_Total:.2f}")