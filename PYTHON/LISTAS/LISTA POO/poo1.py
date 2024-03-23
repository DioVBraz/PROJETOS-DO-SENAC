'''# Exercício 1: Modelando um Carro'''

import os

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano 
        self.velocidade = 0

    def acelerar(self, acelerar):
        if acelerar > 0:
            self.velocidade += acelerar

    def frear(self, frear):
        if frear > 0 <= self.velocidade:
            self.velocidade -= frear

    def informacoes_carro(self):
        print("Marca do carro:", self.marca)
        print("Modelo do carro:", self.modelo)
        print("Ano do carro:", self.ano)
        print("Velocidade atual do carro:", self.velocidade, "km")

carro1 = Carro(input("Digite a marca do primeiro carro: "), input("Digite o modelo do primeiro carro: "), input("Digite o ano do primeiro carro: "))
carro1.acelerar(int(input("Digite a velocidade de aceleração do primeiro carro: ")))
carro1.frear(int(input("Digite a velocidade de frenagem do primeiro carro: ")))
os.system("cls")

carro2 = Carro(input("Digite a marca do segundo carro: "), input("Digite o modelo do segundo carro: "), input("Digite o ano do segundo carro: "))
carro2.acelerar((int(input("Digite a velocidade de aceleração do segundo carro: "))))
carro2.frear((int(input("Digite a velocidade de frenagem do segundo carro: "))))
os.system("cls")


carro3 = Carro(input("Digite a marca do terceiro carro: "), input("Digite o modelo do terceiro carro: "), input("Digite o ano do terceiro carro: "))
carro3.acelerar((int(input("Digite a velocidade de aceleração do terceiro carro: "))))
carro3.frear((int(input("Digite a velocidade de frenagem do terceiro carro: "))))
os.system("cls")

carro4 = Carro(input("Digite a marca do quarto carro: "), input("Digite o modelo do quarto carro: "), input("Digite o ano do quarto carro: "))
carro4.acelerar((int(input("Digite a velocidade de aceleração do quarto carro: "))))
carro4.frear((int(input("Digite a velocidade de frenagem do quarto carro: "))))
os.system("cls")

print("--- Informações do primeiro carro ---")
carro1.informacoes_carro()

print()

print("--- Informações do segundo carro ---")
carro2.informacoes_carro()

print()

print("--- Informações do terceiro carro ---")
carro3.informacoes_carro()

print()

print("--- Informações do quarto carro ---")
carro4.informacoes_carro()

print()