Nome = input("Nome de usuário: ")
Senha = input("Digite a senha: ")

while Senha == Nome:
    print("A senha não pode ser igual ao nome de usuário")
    Senha = input("Digite a senha novamente: ")

print("Usuário:", Nome, "| Senha:", Senha)