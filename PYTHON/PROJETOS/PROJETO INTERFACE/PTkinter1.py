import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")

        self.jogador_atual = "X"
        self.tabuleiro = [""] * 9

        self.botoes = []
        for i in range(9):
            linha = i // 3
            coluna = i % 3
            botao = tk.Button(root, text="", width=10, height=3, command=lambda i=i: self.fazer_jogada(i))
            botao.grid(row=linha, column=coluna)
            self.botoes.append(botao)

    def fazer_jogada(self, indice):
        if self.tabuleiro[indice] == "":
            self.tabuleiro[indice] = self.jogador_atual
            self.botoes[indice].config(text=self.jogador_atual)
            if self.verificar_vencedor(self.jogador_atual):
                messagebox.showinfo("Fim do Jogo", f"O jogador {self.jogador_atual} venceu!")
                self.reiniciar_jogo()
            elif "" not in self.tabuleiro:
                messagebox.showinfo("Fim do Jogo", "Empate!")
                self.reiniciar_jogo()
            else:
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

    def verificar_vencedor(self, jogador):
        combinacoes_vitoria = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]

        for combinacao in combinacoes_vitoria:
            if all(self.tabuleiro[i] == jogador for i in combinacao):
                return True
        return False

    def reiniciar_jogo(self):
        for i in range(9):
            self.tabuleiro[i] = ""
            self.botoes[i].config(text="")
        self.jogador_atual = "X"

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDaVelha(root)
    root.mainloop()