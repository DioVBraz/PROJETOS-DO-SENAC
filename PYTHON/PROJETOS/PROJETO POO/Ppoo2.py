'''# Projeto 2: Simulador de Jogo RPG'''

import random

class Personagem:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.vida = 100
        self.experiencia = 0
        self.level = 1

    def atacar(self, alvo):
        dano = random.randint(5, 15)
        alvo.levar_dano(dano)
        print(f"{self.nome} ataca {alvo.nome} e causa {dano} de dano.")

    def levar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            print(f"{self.nome} foi derrotado.")
        else:
            print(f"{self.nome} tem {self.vida} pontos de vida restantes.")

    def usar_item(self, item):
        pass

    def ganhar_experiencia(self, quantidade):
        self.experiencia += quantidade
        if self.experiencia >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.vida = 100
        self.experiencia = 0
        print(f"{self.nome} subiu para o nível {self.level}!")

class Monstro:
    def __init__(self, nome, vida, dano):
        self.nome = nome
        self.vida = vida
        self.dano = dano

    def atacar(self, alvo):
        dano = random.randint(3, self.dano)
        alvo.levar_dano(dano)
        print(f"{self.nome} ataca {alvo.nome} e causa {dano} de dano.")

    def levar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            print(f"{self.nome} foi derrotado.")
        else:
            print(f"{self.nome} tem {self.vida} pontos de vida restantes.")

    def is_vivo(self):
        return self.vida > 0

class Batalha:
    def __init__(self, personagem, monstro):
        self.personagem = personagem
        self.monstro = monstro

    def iniciar_batalha(self):
        while self.personagem.vida > 0 and self.monstro.is_vivo():
            self.personagem.atacar(self.monstro)
            if not self.monstro.is_vivo():
                self.personagem.ganhar_experiencia(self.monstro.dano)
                break
            self.monstro.atacar(self.personagem)
        if self.personagem.vida <= 0:
            print(f"{self.personagem.nome} foi derrotado.")
        else:
            print(f"{self.monstro.nome} foi derrotado e {self.personagem.nome} ganhou {self.monstro.dano} de experiência!")

personagem = Personagem("Herói", "Guerreiro")
monstro = Monstro("Dragão", 50, 10)

batalha = Batalha(personagem, monstro)
batalha.iniciar_batalha()