def Calculo_Abono(salario):
    Abono_Percentual = 0.20
    Minimo_Abono = 100.00
    
    Abono = max(salario * Abono_Percentual, Minimo_Abono)
    
    return Abono

Total_Funcionario = 0
Total_Abono = 0
Total_Minimo = 0
Maior_Abono = 0

print("Projeção de Gastos com Abono")
print("=============================")

while True:
    Salario = float(input("Salário: "))
    
    if Salario == 0:
        break
    
    Abono = Calculo_Abono(Salario)
    
    Total_Funcionario += 1
    Total_Abono += Abono
    
    if Abono == 100:
       Total_Minimo += 1
    
    if Abono > Maior_Abono:
        Maior_Abono = Abono
    
    print(f"Salário: R$ {Salario:.2f} | Abono: R$ {Abono:.2f}")

print("Foram processados", Total_Funcionario, "colaboradores")
print("Total gasto com abonos: R$", Total_Abono)
print("Valor mínimo pago a", Total_Minimo, "colaboradores")
print("Maior valor de abono pago: R$", Maior_Abono)