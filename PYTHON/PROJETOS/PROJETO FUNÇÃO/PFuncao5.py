'''Crie um gerador de senhas que permita ao usuário especificar o 
comprimento da senha e quais caracteres devem ser usados (letras 
maiúsculas, minúsculas, números, caracteres especiais, etc.). Implemente 
a geração de senhas em uma função.'''

import random

def Gerar_Senha(Comprimento, Caracteres):
    Senha = ''
    for _ in range(Comprimento):
        Senha += random.choice(Caracteres)
    return Senha

Comprimento_Senha = int(input("Digite o comprimento da senha: "))
Caracteres_Senha = input("Digite os caracteres a serem usados: ")

Senha_Gerada = Gerar_Senha(Comprimento_Senha, Caracteres_Senha)
print("Senha gerada:", Senha_Gerada)