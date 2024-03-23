GanhoHora = int(input("Quanto você ganha por hora? "))

Horas = int(input("Quantas horas trabalhadas no mês? "))

SalarioBruto = GanhoHora * Horas 
print(f'O seu salário bruto é igual à =', SalarioBruto)

Ir = SalarioBruto * 0.11
print(f'O desconto do imposto de renda é igual à =', Ir)

Inss = SalarioBruto * 0.08
print(f'O desconto do INSS é igual à =', Inss)

Sindicato = SalarioBruto * 0.05
print(f'O desconto do sindicato é igual à =', Sindicato)

Descontos =  Ir + Inss + Sindicato

SalarioLiquido = SalarioBruto - Descontos

print(f'O seu salário líquido é igual à =', SalarioLiquido)