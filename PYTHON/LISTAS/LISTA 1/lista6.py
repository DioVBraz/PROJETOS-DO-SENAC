Num1 = float(input("Digite o primeiro número: "))
Num2 = float(input("Digite o segundo número: "))

Operacao = input("Escolha a operação (+, -, *, /): ")

if Operacao == '+':
    Resultado = Num1 + Num2

elif Operacao == '-':
    Resultado = Num1 - Num2

elif Operacao == '*':
    Resultado = Num1 * Num2

elif Operacao == '/':
    Resultado = Num1 / Num2

Par_Impar = "par" if Resultado % 2 == 0 else "ímpar"

Positivo_Negativo = "positivo" if Resultado >= 0 else "negativo"

Inteiro_Decimal = "inteiro" if Resultado.is_integer() else "decimal"

print(f"Resultado da operação: {Resultado}")
print(f"O número é {Par_Impar}, {Positivo_Negativo} e {Inteiro_Decimal}.")