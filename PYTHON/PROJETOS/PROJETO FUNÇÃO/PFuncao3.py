'''Crie um conversor de moedas que permita ao usuário converter uma 
quantia de uma moeda para outra (por exemplo, de dólares para Euros). 
Implemente cada conversão em uma função separada.'''

def Dolar_Euro(Valor_Dolar):
    Taxa_Conversao = 0.85
    Valor_Euro = Valor_Dolar * Taxa_Conversao
    return Valor_Euro

def Euro_Dolar(Valor_Euro):
    Taxa_Conversao = 1.18
    Valor_Dolar = Valor_Euro * Taxa_Conversao
    return Valor_Dolar

Quantidade_Dolar = float(input("Digite o valor em dólares: "))
Quantidade_Euro = Dolar_Euro(Quantidade_Dolar)
print(f"{Quantidade_Dolar} dólares equivalem a {Quantidade_Euro:.2f} euros.")

Quantidade_Euro = float(input("Digite o valor em euros: "))
Quantidade_Dolar = Euro_Dolar(Quantidade_Euro)
print(f"{Quantidade_Euro} euros equivalem a {Quantidade_Dolar:.2f} dólares.")

