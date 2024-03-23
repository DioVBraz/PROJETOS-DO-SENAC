import tkinter as tk

def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

def adicionar_nota():
    aluno = nome_entry.get()
    nota = float(nota_entry.get())
    if aluno in notas_alunos:
        notas_alunos[aluno].append(nota)
    else:
        notas_alunos[aluno] = [nota]
    atualizar_tela()

def atualizar_tela():
    lista_notas.delete(0, tk.END)
    for aluno, notas in notas_alunos.items():
        media = calcular_media(notas)
        lista_notas.insert(tk.END, f"{aluno}: {notas} (Média: {media:.2f})")

root = tk.Tk()
root.title("Sistema de Notas Escolares",)

notas_alunos = {}

nome_label = tk.Label(root, text="Nome do Aluno: ")
nome_label.pack()
nome_entry = tk.Entry(root)
nome_entry.pack()

nota_label = tk.Label(root, text="Nota: ")
nota_label.pack()
nota_entry = tk.Entry(root)
nota_entry.pack()

adicionar_button = tk.Button(root, text="Adicionar Nota", command=adicionar_nota)
adicionar_button.pack()

lista_notas = tk.Listbox(root, width=40)
lista_notas.pack()

root.mainloop()