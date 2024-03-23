'''Construa um programa para gerenciar um catálogo de produtos em uma loja. Os 
usuários podem adicionar produtos com informações como nome, preço e quantidade 
em estoque. Use um dicionário onde as chaves são os nomes dos produtos e os valores 
são outros dicionários com informações sobre cada produto.'''

import os

dicio_produtos = {}

while True:
    print("--- Catálogo de produtos ---")
    nome_produtos = input("Informe o nome do produto (ou Enter para sair): ")
    os.system("cls")
    if nome_produtos.lower() == '':
        break 
    preco_produto = float(input("Informe o preço do produto: R$ "))
    quantidade_produto = int(input("Informe a quantidade do produto: "))

    os.system("cls")

    produto = {
        "Preço": preco_produto,
        "Quantidade": quantidade_produto
    }
    
    dicio_produtos[nome_produtos] = produto

print("--- Lista de produtos ---")
for nome_produtos, info in dicio_produtos.items():
    print(f"Nome: {nome_produtos} | Preço: R$ {info['Preço']} | Quantidade: {info['Quantidade']}")