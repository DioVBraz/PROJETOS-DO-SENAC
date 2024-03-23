import tkinter as tk

def calcular():
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())
        operacao = operacoes.get()
        
        if operacao == "Soma":
            resultado.set(num1 + num2)
        elif operacao == "Subtração":
            resultado.set(num1 - num2)
        elif operacao == "Multiplicação":
            resultado.set(num1 * num2)
        elif operacao == "Divisão":
            resultado.set(num1 / num2)
    except ValueError:
        resultado.set("Erro")

janela = tk.Tk()
janela.title("Calculadora")

tk.Label(janela, text="Número 1").grid(row=0, column=0)
entrada_num1 = tk.Entry(janela)
entrada_num1.grid(row=0, column=1)

tk.Label(janela, text="Número 2").grid(row=1, column=0)
entrada_num2 = tk.Entry(janela)
entrada_num2.grid(row=1, column=1)

operacoes = tk.StringVar()
operacoes.set("Soma")
tk.Label(janela, text="Operação").grid(row=2, column=0)
menu_operacoes = tk.OptionMenu(janela, operacoes, "Soma", "Subtração", "Multiplicação", "Divisão")
menu_operacoes.grid(row=2, column=1)

botao_calcular = tk.Button(janela, text="Calcular", command=calcular)
botao_calcular.grid(row=3, columnspan=2)

resultado = tk.StringVar()
resultado.set("Resultado")
tk.Label(janela, textvariable=resultado).grid(row=4, columnspan=2)

janela.mainloop()