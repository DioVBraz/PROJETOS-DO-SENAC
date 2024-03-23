import random

Palavras = ['diogo', 'lucas', 'wesley', 'marco', 'davi', 'pedro', 'maria', 'kaua', 'icaro', 'maruzam']

Palavra_Escolhida = random.choice(Palavras)

Letras_Corretas = []

Maximo_Tentativas = 6

while Maximo_Tentativas > 0:

    Palavra_Parcial = ''
    for Letra in Palavra_Escolhida:
        if Letra in Letras_Corretas:
            Palavra_Parcial += Letra
        else:
            Palavra_Parcial += '_'   
    print(f'Palavra: {Palavra_Parcial}')
    
    Tentativa = input('Digite uma letra: ').lower()
    
    if Tentativa in Letras_Corretas:
        print('Você já tentou essa letra!')
        continue
    
    if Tentativa in Palavra_Escolhida:
        Letras_Corretas.append(Tentativa)
    else:
        Maximo_Tentativas -= 1
        print(f'Letra "{Tentativa}" não está na palavra. Tentativas restantes: {Maximo_Tentativas}')
    
    if set(Letras_Corretas) == set(Palavra_Escolhida):
        print(f'Parabéns, você venceu! A palavra é: {Palavra_Escolhida}')
        break

if Maximo_Tentativas == 0:
    print(f'Você perdeu! A palavra era: {Palavra_Escolhida}')