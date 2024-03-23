import tkinter as tk
from tkinter import messagebox

palavras = [
    "PYTHON", "INTERFACE", "GRAFICA", "FORCA", "COMPUTADOR",
    "TELEFONE", "INTERNET", "DESENVOLVIMENTO", "PROGRAMADOR", "CARRO", "CASA",
    "ESCOLA", "FACULDADE", "CADERNO", "CANETA", "BICICLETA", "ELEFANTE", "GIRASSOL",
    "MONTANHA", "SOL", "LUA", "ASTRONOMIA", "PLANEJAMENTO", "CAVALO", "BOLA",
    "VIAGEM", "AVIAO", "DINHEIRO", "ESPORTE", "MUSICA", "ARTISTA", "FOTOGRAFIA",
    "CELULAR", "TELEVISAO", "RELATORIO", "ALMOFADA", "PREGUICA", "CROCODILO",
    "PIZZA", "HAMBURGUER", "PRAIA", "MONTANHA-RUSSA", "TRABALHO", "RELAXAMENTO",
    "PROGRAMACAO", "ESCALADA", "ARVORE", "PANTUFA", "INTELIGENCIA"
]

def escolher_palavra():
    import random
    return random.choice(palavras)

def verificar_letra():
    letra = letra_entry.get()
    if letra in palavra_atual:
        for i in range(len(palavra_atual)):
            if palavra_atual[i] == letra:
                palavra_display[i] = letra
        letra_entry.delete(0, tk.END)
        atualizar_display()
        if "_" not in palavra_display:
            messagebox.showinfo("Parabéns!", "Você venceu!")
            reiniciar_jogo()
    else:
        letras_erradas.append(letra)
        atualizar_display()
        if len(letras_erradas) == 6:
            messagebox.showinfo("Fim de jogo", f"A palavra era '{palavra_atual}'. Você perdeu!")
            reiniciar_jogo()

def reiniciar_jogo():
    global palavra_atual, palavra_display, letras_erradas
    palavra_atual = escolher_palavra()
    palavra_display = ["_" for _ in palavra_atual]
    letras_erradas = []
    atualizar_display()

def atualizar_display():
    palavra_label.config(text=" ".join(palavra_display))
    letras_erradas_label.config(text="Letras erradas: " + " ".join(letras_erradas))

janela = tk.Tk()
janela.title("Jogo da Forca")

palavra_atual = escolher_palavra()
palavra_display = ["_" for _ in palavra_atual]
letras_erradas = []

palavra_label = tk.Label(janela, text=" ".join(palavra_display), font=("Arial", 24))
palavra_label.pack(pady=20)
letra_label = tk.Label(janela, text="Digite uma letra:", font=("Arial", 16))
letra_label.pack()
letra_entry = tk.Entry(janela, font=("Arial", 16))
letra_entry.pack()
verificar_button = tk.Button(janela, text="Verificar", command=verificar_letra, font=("Arial", 16))
verificar_button.pack()
letras_erradas_label = tk.Label(janela, text="Letras erradas:", font=("Arial", 16))
letras_erradas_label.pack()

atualizar_display()

janela.mainloop()