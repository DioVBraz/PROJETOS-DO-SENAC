import tkinter as tk

taxa_dolar_para_euro = 0.85
taxa_real_para_dolar = 0.18

def converter_dolar_para_euro():
    quantia = float(entrada_quantia.get())
    resultado = quantia * taxa_dolar_para_euro
    label_resultado.config(text=f"{quantia} dólares = {resultado:.2f} euros")

def converter_real_para_dolar():
    quantia = float(entrada_quantia.get())
    resultado = quantia * taxa_real_para_dolar
    label_resultado.config(text=f"{quantia} reais = {resultado:.2f} dólares")

root = tk.Tk()
root.title("Conversor de Moedas")

frame = tk.Frame(root)
frame.pack(pady=10)

label_instrucao = tk.Label(frame, text="Digite a quantia a ser convertida:")
label_instrucao.pack()

entrada_quantia = tk.Entry(frame, width=30)
entrada_quantia.pack()

botao_dolar_para_euro = tk.Button(frame, text="Converter Dólar para Euro", command=converter_dolar_para_euro)
botao_dolar_para_euro.pack()

botao_real_para_dolar = tk.Button(frame, text="Converter Real para Dólar", command=converter_real_para_dolar)
botao_real_para_dolar.pack()

label_resultado = tk.Label(frame, text="", fg="black")
label_resultado.pack()

root.mainloop()