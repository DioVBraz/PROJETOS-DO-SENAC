import sqlite3
import os 

def exibir_dados():
    cursor.execute("SELECT * FROM minha_tabela")
    dados = cursor.fetchall()
    for linha in dados:
        print(linha)

conn = sqlite3.connect('banco_de_dados.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS minha_tabela (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER,
        cidade TEXT,
        email TEXT
    )
''')

conn.commit()

while True:
    print("Opções:")
    print("1. Inserir dados")
    print("2. Alterar dados")
    print("3. Exibir dados")
    print("4. Excluir dados")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    os.system("cls")
    
    if opcao == "1":
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        cidade = input("Digite a cidade: ")
        email = input("Digite o email: ")
        os.system("cls")


        cursor.execute("INSERT INTO minha_tabela (nome, idade, cidade, email) VALUES (?, ?, ?, ?)", (nome, idade, cidade, email))

        conn.commit()
        print("Dados inseridos com sucesso!")
    
    elif opcao == "2":
        exibir_dados()
        id_registro = int(input("Digite o ID do registro que deseja alterar: "))
   
        novo_nome = input("Digite o novo nome: ")
        nova_idade = int(input("Digite a nova idade: "))
        nova_cidade = input("Digite a nova cidade: ")
        novo_email = input("Digite o novo email: ")
        os.system("cls")

        cursor.execute("UPDATE minha_tabela SET nome = ?, idade = ?, cidade = ?, email = ? WHERE id = ?", (novo_nome, nova_idade, nova_cidade, novo_email, id_registro))

        conn.commit()
        print("Dados atualizados com sucesso!")
    
    elif opcao == "3":
        exibir_dados()
    
    elif opcao == "4":
        exibir_dados()
        id_registro = int(input("Digite o ID do registro que deseja excluir: "))
        os.system("cls")

        cursor.execute("DELETE FROM minha_tabela WHERE id = ?", (id_registro,))

        conn.commit()
        print("Registro excluído com sucesso!")
    
    elif opcao == "5":
        break

cursor.close()
conn.close()