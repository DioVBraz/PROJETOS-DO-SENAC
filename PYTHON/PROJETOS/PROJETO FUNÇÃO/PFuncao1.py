'''Crie uma calculadora que permite ao usuário realizar operações de adição, 
subtração, multiplicação e divisão. Cada operação deve ser implementada 
em uma função separada.'''

print("--CALCULADORA SIMPLES--")
Num1 = int(input("Digite o primeiro número: "))
Num2 = int(input("Digite o segundo número: "))

def Adicao(Num1, Num2):
    return (Num1 + Num2)

def Sub(Num1, Num2):
    return Num1 - Num2
    
def Multi(Num1, Num2):
    return Num1 * Num2
    
def Divisao(Num1, Num2):
    return Num1 / Num2

Escolha = input("Escolha uma operação matemática (soma, subtração, multiplicação, divisão): ")

if Escolha.lower() == "soma":
    print("O resultado da soma é:", Adicao(Num1, Num2))

elif Escolha.lower() == "subtração":
    print("O resultado da subtração é:", Sub(Num1, Num2))

elif Escolha.lower() == "multiplicação":
    print("O resultado da multiplicação é:", Multi(Num1, Num2))

elif Escolha.lower() == "divisão":
    print("O resultado da divisão é:", Divisao(Num1, Num2))        
    

     


    