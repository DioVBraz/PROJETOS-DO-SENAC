'''Crie um jogo de quiz com várias perguntas e opções de resposta. Use um dicionário 
para armazenar as perguntas, opções de resposta e a resposta correta. O programa 
deve permitir que os jogadores escolham uma pergunta, forneçam uma resposta e 
mostrar se a resposta está correta ou não.'''

import os

dicio_quiz = {
    "1": {
        "pergunta": "Qual país venceu a Copa do Mundo de 2018 ?",
        "opcoes": ["a) Brasil", "b) Alemanha", "c) Argentina", "d) França", "e) Espanha"],
        "resposta_correta": "d"
    },

    "2": {
        "pergunta": "Quem é considerado o maior artilheiro da história da Copa do Mundo ?",
        "opcoes": ["a) Pelé", "b) Cristiano Ronaldo", "c) Miroslav Klose", "d) Lionel Messi", "e) Diego Maradona"],
        "resposta_correta": "c"
    },

    "3": {
        "pergunta": "Qual jogador é conhecido como Rei ?",
        "opcoes": ["a) Neymar", "b) Cristiano Ronaldo", "c) Lionel Messi", "d) Zinedine Zidane", "e) Pelé"],
        "resposta_correta": "e"
    },

    "4": {
        "pergunta": "Em que ano o Brasil sediou a Copa do Mundo pela última vez antes de 2014 ?",
        "opcoes": ["a) 2002", "b) 1998", "c) 1986", "d) 1970", "e) 1950"],
        "resposta_correta": "e"
    },

    "5": {
        "pergunta": "Qual é o nome da taça concedida ao vencedor da Copa Libertadores da América ?",
        "opcoes": ["a) Taça da Libertação", "b) Taça da Conquista", "c) Taça da América", "d) Taça dos Campeões", "e) Taça Libertadores"],
        "resposta_correta": "e"
    },
}

def jogar_quiz():
    pontuacao = 0
    for numero_pergunta in dicio_quiz:
        pergunta = dicio_quiz[numero_pergunta]["pergunta"]
        opcoes = dicio_quiz[numero_pergunta]["opcoes"]
        resposta_correta = dicio_quiz[numero_pergunta]["resposta_correta"]

        print(pergunta)
        for opcao in opcoes:
            print(opcao)

        resposta = input("Digite a letra da sua resposta: ").lower()
        os.system("cls")

        if resposta == resposta_correta:
            print("Resposta correta!")
            pontuacao += 1
        else:
            print(f"Resposta incorreta. A resposta correta é '{resposta_correta}'.")

    print(f"Sua pontuação final é: {pontuacao}/{len(dicio_quiz)}")

print("--- QUIZ DE FUTEBOL ---")
jogar_quiz()
