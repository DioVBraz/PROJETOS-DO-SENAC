def Soma_Numeros(Num):
   Soma = sum(Num)
   return Soma

def Multiplicacao_Numeros(Num):
   Multiplicacao = 1
   for Numeros in Num:
       Multiplicacao *= Numeros
   return Multiplicacao

Lista_Numeros = []
for i in range(5):
   Numeros = int(input('Digite um número: '))
   Lista_Numeros.append(Numeros)

Soma = Soma_Numeros(Lista_Numeros) 
Multiplicacao = Multiplicacao_Numeros(Lista_Numeros)

print(f'Soma dos números no vetor: {Soma}')
print(f'Multiplicação dos números no vetor: {Multiplicacao}')
print(f'Números no vetor {Lista_Numeros}')
