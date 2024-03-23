import tkinter as tk

def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)

def marcar_concluida():
    selecao = lista_tarefas.curselection()
    if selecao:
        index = selecao[0]
        lista_tarefas.itemconfig(index, {'bg': 'light green'})
        lista_tarefas.selection_clear(0, tk.END)

def remover_tarefa():
    selecao = lista_tarefas.curselection()
    if selecao:
        index = selecao[0]
        lista_tarefas.delete(index)

root = tk.Tk()
root.title("Lista de Tarefas")

frame = tk.Frame(root)
frame.pack(pady=10)

entrada_tarefa = tk.Entry(frame, width=30)
entrada_tarefa.grid(row=0, column=0)

adicionar_botao = tk.Button(frame, text="Adicionar", command=adicionar_tarefa)
adicionar_botao.grid(row=0, column=1)

marcar_botao = tk.Button(frame, text="Marcar Concluída", command=marcar_concluida)
marcar_botao.grid(row=1, column=0)

remover_botao = tk.Button(frame, text="Remover", command=remover_tarefa)
remover_botao.grid(row=1, column=1)

lista_tarefas = tk.Listbox(root, width=50)
lista_tarefas.pack(padx=10, pady=10)

root.mainloop()