'''Defina uma função chamada
encontrar_menor_elemento` que recebe uma lista de números como
argumento e retorna o menor número na lista.'''

def encontrar_menor_elemento(lista):
    if len(lista) == 0:
        return None
     
    menor = lista[0] 
    for num in lista:
        if num < menor:
            menor = num  
    return menor

lista_numeros = []

while True:
    entrada = input("Digite um número (ou pressione Enter para encerrar o programa): ")
    if entrada == '':
        break
    numero = int(entrada)
    lista_numeros.append(numero)

menor_numero = encontrar_menor_elemento(lista_numeros)
print("O menor número na lista é:", menor_numero)
