''''Desenvolva um programa de agenda de contatos. Os usuários podem adicionar, 
visualizar, editar e excluir contatos. Use um dicionário onde as chaves são os nomes 
dos contatos e os valores são os detalhes de contato (número de telefone, email, 
etc.).'''

import os

dicio_contatos = {}

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone: ")
    email = input("Digite o endereço de e-mail: ")
    
    contato = {"Telefone": telefone, "Email": email}
    dicio_contatos[nome] = contato
    print(f"Contato {nome} adicionado com sucesso!")

def visualizar_contato():
    nome = input("Digite o nome do contato que deseja visualizar: ")
    os.system("cls")
    if nome in dicio_contatos:
        contato = dicio_contatos[nome]
        print(f"Detalhes do Contato {nome}:")
        print(f"Telefone: {contato['Telefone']}")
        print(f"Email: {contato['Email']}")
    else:
        print(f"Contato {nome} não encontrado na agenda.")

def editar_contato():
    nome = input("Digite o nome do contato que deseja editar: ")
    os.system("cls")
    if nome in dicio_contatos:
        contato = dicio_contatos[nome]
        print(f"Editando o Contato {nome}:")
        novo_telefone = input(f"Digite o novo número de telefone (atual: {contato['Telefone']}): ")
        novo_email = input(f"Digite o novo endereço de e-mail (atual: {contato['Email']}): ")
        
        contato['Telefone'] = novo_telefone
        contato['Email'] = novo_email
        print(f"Contato {nome} editado com sucesso!")
    else:
        print(f"Contato {nome} não encontrado na agenda.")

def excluir_contato():
    nome = input("Digite o nome do contato que deseja excluir: ")
    os.system("cls")
    if nome in dicio_contatos:
        del dicio_contatos[nome]
        print(f"Contato {nome} excluído com sucesso!")
    else:
        print(f"Contato {nome} não encontrado na agenda.")

while True:
    print("*" * 30)
    print("Opções:")
    print("1 - Adicionar Contato")
    print("2 - Visualizar Contato")
    print("3 - Editar Contato")
    print("4 - Excluir Contato")
    print("5 - Sair")
    print("*" * 30)
    
    opcao = input("Escolha uma opção: ")
    os.system("cls")
    
    if opcao == '1':
        adicionar_contato()

    elif opcao == '2':
        visualizar_contato()

    elif opcao == '3':
        editar_contato()

    elif opcao == '4':
        excluir_contato()

    elif opcao == '5':
        break