import random

Dado = (1, 2, 3, 4, 5, 6)

input("Para jogar o dado, pressione Enter")

Dado_Aleatorio = random.choice(Dado)

Dado_Escolhido = int(input("Escolha um número de 1 a 6: "))

if Dado_Escolhido in Dado:
    if Dado_Escolhido == Dado_Aleatorio:
        print(f"Você escolheu {Dado_Escolhido} e o dado mostrou {Dado_Aleatorio}. Parabéns, você venceu!")
    else:
        print(f"Você escolheu {Dado_Escolhido} e o dado mostrou {Dado_Aleatorio}. Você perdeu.")
else:
    print("Número inválido. Escolha um número de 1 a 6.")