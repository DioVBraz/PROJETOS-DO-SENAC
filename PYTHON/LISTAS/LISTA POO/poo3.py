'''# Exercício 3: Modelando uma Biblioteca'''

import os 

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado.")
        else:
            print(f"O livro '{self.titulo}' não está disponível para empréstimo.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro '{self.titulo}' foi devolvido.")
        else:
            print(f"O livro '{self.titulo}' já está disponível na biblioteca.")
    
    def informacoes_livro(self):
        print("Título do livro:", self.titulo)
        print("Autor do livro:", self.autor)
        print("Ano de publicação do livro:", self.ano_publicacao)

livro1 = Livro(input("Digite o título do primeiro livro: "), input("Digite o nome do autor do primeiro livro: "), input("Digite o ano de publicação do primeiro livro: "))
os.system('cls')

livro2 = Livro(input("Digite o título do segundo livro: "), input("Digite o nome do autor do segundo livro: "), input("Digite o ano de publicação do segundo livro: "))
os.system('cls')

livro3 = Livro(input("Digite o título do terceiro livro: "), input("Digite o nome do autor do terceiro livro: "), input("Digite o ano de publicação do terceiro livro: "))
os.system('cls')

print()

print("--- Informações do primeiro livro ---")
livro1.informacoes_livro()

print()

print("--- Informações do segundo livro ---")
livro2.informacoes_livro()

print()

print("--- Informações do terceiro livro ---")
livro3.informacoes_livro()

print()

livro1.emprestar()
livro2.emprestar()
livro3.emprestar()
livro1.devolver()
livro2.devolver()
livro3.devolver()