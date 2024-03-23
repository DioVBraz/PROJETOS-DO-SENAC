import tkinter as tk
import random

def iniciar_jogo():
    global numero_secreto
    numero_secreto = random.randint(1, 100)
    tentativas_label.config(text="Tentativas: 0")
    resultado_label.config(text="")
    tentativa_entry.delete(0, tk.END)

def verificar_adivinhacao():
    tentativa = int(tentativa_entry.get())
    tentativa_entry.delete(0, tk.END)

    if tentativa == numero_secreto:
        resultado_label.config(text="Parabéns! Você acertou o número.")
    elif tentativa < numero_secreto:
        resultado_label.config(text="Tente um número maior.")
    else:
        resultado_label.config(text="Tente um número menor.")

    atualizar_tentativas()

def atualizar_tentativas():
    tentativas = int(tentativas_label.cget("text").split(": ")[1])
    tentativas += 1
    tentativas_label.config(text=f"Tentativas: {tentativas}")

root = tk.Tk()
root.title("Jogo de Adivinhação")

frame = tk.Frame(root)
frame.pack(pady=10)

iniciar_botao = tk.Button(frame, text="Iniciar Novo Jogo", command=iniciar_jogo)
iniciar_botao.grid(row=0, column=0)

tentativa_label = tk.Label(frame, text="Tentativa:")
tentativa_label.grid(row=0, column=1)

tentativa_entry = tk.Entry(frame, width=5)
tentativa_entry.grid(row=0, column=2)

verificar_botao = tk.Button(frame, text="Verificar", command=verificar_adivinhacao)
verificar_botao.grid(row=0, column=3)

tentativas_label = tk.Label(frame, text="Tentativas: 0")
tentativas_label.grid(row=1, column=0)

resultado_label = tk.Label(frame, text="")
resultado_label.grid(row=2, columnspan=4)

iniciar_jogo()

root.mainloop()