import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time

def iniciar_contagem():
    tempo = int(entrada_tempo.get())
    for i in range(tempo, 0, -1):
        label_contagem.config(text=f"Tempo restante: {i} segundos")
        root.update()
        time.sleep(1)
    messagebox.showinfo("Contagem Regressiva", "Tempo esgotado!")

root = tk.Tk()
root.title("Contagem Regressiva")

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

label_tempo = ttk.Label(frame, text="Informe o tempo (em segundos):")
label_tempo.grid(row=0, column=0, padx=5, pady=5)

entrada_tempo = ttk.Entry(frame)
entrada_tempo.grid(row=0, column=1, padx=5, pady=5)

botao_iniciar = ttk.Button(frame, text="Iniciar Contagem", command=iniciar_contagem)
botao_iniciar.grid(row=1, columnspan=2, padx=5, pady=10)

label_contagem = ttk.Label(frame, text="")
label_contagem.grid(row=2, columnspan=2, padx=5, pady=5)

root.mainloop()