'''Escreva uma função chamada `verificar_par` que recebe
um número como argumento e retorna `True` se o número for par e `False`
se for ímpar.
'''

def Verificar_Par(Num):
    if Num % 2 == 0:
        return True
    else:
        return False
    
Numero = int(input("Digite um número: ")) 
Resultado = Verificar_Par(Numero)

if Resultado:
    print(f"{Numero} é um número par")
else:
    print(f"{Numero} é um número ímpar")
 

