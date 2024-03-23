import tkinter as tk

perguntas = {
    "Pergunta 1": {
        "pergunta": "Quem é mais forte entre os filhos de Krypton?",
        "opcoes": ["Mulher Maravilha", "Caçador de Marte", "Superman", "Supergirl"],
        "resposta_correta": "Supergirl"
    },
    "Pergunta 2": {
        "pergunta": "Qual foi considerado pior filme da DC?",
        "opcoes": ["The Flash (2023)", "Liga da justiça (2017)", "Lanterna Verde (2011)", "Aço (1997)"],
        "resposta_correta": "Aço (1997)"
    },
    "Pergunta 3": {
        "pergunta": "Qual vilão mais poderoso da DC?",
        "opcoes": ["Darkseid", "Amazo", "Nekron", "Lex Luthor"],
        "resposta_correta": "Nekron"
    },
    "Pergunta 4": {
        "pergunta": "Qual o ponto fraco do Batman?",
        "opcoes": ["Veneno", "Força física", "Ataques mentais", "Kryptonita"],
        "resposta_correta": "Ataques mentais"
    },
    "Pergunta 5": {
        "pergunta": "Quem dirigiu o filme 'Aquaman' de 2018?",
        "opcoes": ["Zack Snyder", "Patty Jenkins", "James Wan", "David Ayer"],
        "resposta_correta": "James Wan"
    }
}

def mostrar_pergunta():
    selecionada = lista_perguntas.curselection()
    if selecionada:
        indice = selecionada[0]
        pergunta_selecionada = lista_perguntas.get(indice)
        pergunta = perguntas[pergunta_selecionada]["pergunta"]
        opcoes = perguntas[pergunta_selecionada]["opcoes"]
        resposta_correta = perguntas[pergunta_selecionada]["resposta_correta"]
        
        label_pergunta.config(text=pergunta)
        
        for i, opcao in enumerate(opcoes):
            radio_buttons[i].config(text=opcao, variable=selecao_var, value=opcao)
            radio_buttons[i].pack()
        
        verificar_resposta.config(command=lambda: verificar(resposta_correta))

def verificar(resposta_correta):
    resposta = selecao_var.get()
    if resposta == resposta_correta:
        resultado.config(text="Resposta correta!", fg="green")
    else:
        resultado.config(text="Resposta incorreta. Tente novamente.", fg="red")

root = tk.Tk()
root.title("Jogo de Quiz")

frame = tk.Frame(root)
frame.pack(pady=10)

label_instrucao = tk.Label(frame, text="Escolha uma pergunta:")
label_instrucao.pack()

lista_perguntas = tk.Listbox(frame, width=40)
for pergunta in perguntas:
    lista_perguntas.insert(tk.END, pergunta)
lista_perguntas.pack()

botao_mostrar_pergunta = tk.Button(frame, text="Mostrar Pergunta", command=mostrar_pergunta)
botao_mostrar_pergunta.pack()

label_pergunta = tk.Label(frame, text="")
label_pergunta.pack()

radio_buttons = [tk.Radiobutton(frame) for _ in range(4)]
selecao_var = tk.StringVar()
resultado = tk.Label(frame, text="", fg="black")

verificar_resposta = tk.Button(frame, text="Verificar Resposta", command=lambda: verificar(None))
verificar_resposta.pack()

resultado.pack()

root.mainloop()