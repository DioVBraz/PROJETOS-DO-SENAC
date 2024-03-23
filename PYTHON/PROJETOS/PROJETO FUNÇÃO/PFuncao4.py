'''Desenvolva um jogo de adivinhação onde o computador escolhe um 
número aleatório e o jogador tenta adivinhá-lo. Use funções para 
gerenciar o processo de adivinhação e a lógica do jogo.'''

import random

def Jogo_Adivinhacao():
    Numero_Secreto = random.randint(1, 100)
    Tentativas = 0

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")

    while True:
        try:
            Numero = int(input("Digite um número: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        Tentativas += 1

        if Numero < Numero_Secreto:
            print("Tente um número maior.")
        elif Numero > Numero_Secreto:
            print("Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou o número secreto {Numero_Secreto} em {Tentativas} Tentativas.")
            break

if __name__ == "__main__":
    Jogo_Adivinhacao()