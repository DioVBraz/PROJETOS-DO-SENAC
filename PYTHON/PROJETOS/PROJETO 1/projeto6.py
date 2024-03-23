import os 
os.system('cls')

def Calculo_Digito1(CPF):
    Soma = 0
    Peso = 10
    for Digito in CPF[:9]:
        Soma += int(Digito) * Peso
        Peso -= 1
    Resto = Soma % 11
    if Resto < 2:
        Digito1 = 0
    else:
        Digito1 = 11 - Resto
    return Digito1

def Calculo_Digito2(CPF):
    Soma = 0
    Peso = 11
    for Digito in CPF[:10]:
        Soma += int(Digito) * Peso
        Peso -= 1
    Resto = Soma % 11
    if Resto < 2:
        Digito2 = 0
    else:
        Digito2 = 11 - Resto
    return Digito2

def Validacao_CPF(CPF):
    if len(CPF) != 11 or not CPF.isdigit():
        return False  

    Digito1 = Calculo_Digito1(CPF)
    Digito2 = Calculo_Digito2(CPF)

    if int(CPF[9]) == Digito1 and int(CPF[10]) == Digito2 and len(set(CPF)) > 1:
        return True  
    else:
        return False
CPF = input("Digite o número do CPF: ")

print()

if Validacao_CPF(CPF):
    print("CPF válido.")
else:
    print("CPF inválido.")