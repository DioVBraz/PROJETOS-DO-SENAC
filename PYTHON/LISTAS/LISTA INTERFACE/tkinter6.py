import tkinter as tk
import random
import string

def gerar_senha():
    comprimento = int(caixa_comprimento.get())
    incluir_maiusculas = var_maiusculas.get()
    incluir_minusculas = var_minusculas.get()
    incluir_numeros = var_numeros.get()
    incluir_caracteres_especiais = var_caracteres_especiais.get()

    caracteres = ""
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_caracteres_especiais:
        caracteres += string.punctuation

    if not caracteres:
        resultado_label.config(text="Selecione pelo menos um tipo de caractere.")
        return

    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    senha_label.config(text="Senha gerada: " + senha)

janela = tk.Tk()
janela.title("Gerador de Senhas")

comprimento_label = tk.Label(janela, text="Comprimento da Senha:")
comprimento_label.pack()
caixa_comprimento = tk.Entry(janela)
caixa_comprimento.pack()

var_maiusculas = tk.BooleanVar()
var_maiusculas.set(True)
caixa_maiusculas = tk.Checkbutton(janela, text="Letras Maiúsculas", variable=var_maiusculas)
caixa_maiusculas.pack()

var_minusculas = tk.BooleanVar()
var_minusculas.set(True)
caixa_minusculas = tk.Checkbutton(janela, text="Letras Minúsculas", variable=var_minusculas)
caixa_minusculas.pack()

var_numeros = tk.BooleanVar()
var_numeros.set(True)
caixa_numeros = tk.Checkbutton(janela, text="Números", variable=var_numeros)
caixa_numeros.pack()

var_caracteres_especiais = tk.BooleanVar()
var_caracteres_especiais.set(True)
caixa_caracteres_especiais = tk.Checkbutton(janela, text="Caracteres Especiais", variable=var_caracteres_especiais)
caixa_caracteres_especiais.pack()

botao_gerar = tk.Button(janela, text="Gerar Senha", command=gerar_senha)
botao_gerar.pack()

senha_label = tk.Label(janela, text="")
senha_label.pack()

resultado_label = tk.Label(janela, text="")
resultado_label.pack()

janela.mainloop()