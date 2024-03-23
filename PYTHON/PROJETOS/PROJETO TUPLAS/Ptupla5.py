import random

Tupla_Palavras = ("python", "java", "javascript", "ruby", "php", "html", "css", "maçã", "felicidade",
            "computador", "amizade", "guitarra", "montanha", "fotografia", "chocolate", "viagem", "cinema", "oceano",
            "universidade", "astronomia", "dinossauro", "música", "floresta", "livro", "café", "esporte", "cachorro",
            "arquitetura", "arte", "comida", "estrela", "telefone", "relógio", "história", "fotografia", "pintura",
            "política", "espaço", "férias", "aventura", "saúde", "internet", "trabalho", "amor", "carro", "dinheiro",
            "inovação", "natureza", "aventura", "religião", "ciência", "inverno", "verão", "primavera", "outono",
            "arco-íris", "amarelo", "verde", "azul", "vermelho", "gato", "fotografia", "sonho", "felicidade", "tempo",
            "escola", "energia", "comédia", "drama", "futebol", "basquete", "natação", "agricultura", "família",
            "amuleto", "história", "guerra", "paz", "herança", "aniversario", "guitarra", "tecnologia")

Palavra_Escolhida = random.choice(Tupla_Palavras)

Letras_Corretas = []
Letras_Erradas = []
Maximo_Tentativas = 6

while True:
    Estado_Palavra = ""
    for letra in Palavra_Escolhida:
        if letra in Letras_Corretas:
            Estado_Palavra += letra
        else:
            Estado_Palavra += "_ "
    print("Palavra: " + Estado_Palavra)

    if Letras_Erradas:
        print("Letras erradas: " + ", ".join(Letras_Erradas))

    letra = input("Digite uma letra: ").lower()

    if letra in Letras_Corretas or letra in Letras_Erradas:
        print("Você já escolheu essa letra antes. Tente novamente.")
        continue

    if letra in Palavra_Escolhida:
        Letras_Corretas.append(letra)
    else:
        Letras_Erradas.append(letra)

    if set(Letras_Corretas) == set(Palavra_Escolhida):
        print("Parabéns! Você venceu. A palavra é: " + Palavra_Escolhida)
        break

    if len(Letras_Erradas) >= Maximo_Tentativas:
        print("Você perdeu! A palavra era: " + Palavra_Escolhida)
        break