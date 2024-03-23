import tkinter as tk
from tkinter import messagebox
import random

def verificar_resultado(jogador_escolha):
    opcoes = ["Pedra", "Papel", "Tesoura"]
    computador_escolha = random.choice(opcoes)

    if jogador_escolha == computador_escolha:
        resultado = "Empate!"
    elif (
        (jogador_escolha == "Pedra" and computador_escolha == "Tesoura")
        or (jogador_escolha == "Papel" and computador_escolha == "Pedra")
        or (jogador_escolha == "Tesoura" and computador_escolha == "Papel")
    ):
        resultado = "Você ganhou!"
    else:
        resultado = "Você perdeu!"

    messagebox.showinfo("Resultado", f"Você escolheu {jogador_escolha}\nComputador escolheu {computador_escolha}\n{resultado}")

def escolher_pedra():
    verificar_resultado("Pedra")

def escolher_papel():
    verificar_resultado("Papel")

def escolher_tesoura():
    verificar_resultado("Tesoura")

janela = tk.Tk()
janela.title("Pedra, Papel e Tesoura")

btn_pedra = tk.Button(janela, text="Pedra", command=escolher_pedra)
btn_papel = tk.Button(janela, text="Papel", command=escolher_papel)
btn_tesoura = tk.Button(janela, text="Tesoura", command=escolher_tesoura)

btn_pedra.pack(padx=10, pady=10)
btn_papel.pack(padx=10, pady=10)
btn_tesoura.pack(padx=10, pady=10)

janela.mainloop()