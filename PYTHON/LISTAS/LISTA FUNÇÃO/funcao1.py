'''Crie uma função chamada `calcular_media` que recebe
uma lista de números como argumento e retorna a média dos números na
lista.'''

def Calcular_Media(Lista_Numeros):
    if not Lista_Numeros:
        return 0
    
    Soma_Numeros = sum(Lista_Numeros)
    Quantidade_Numeros = len(Lista_Numeros)
    Media_Numeros = Soma_Numeros / Quantidade_Numeros
    return Media_Numeros

Lista_Numeros = []

for i in range(10):
    Numeros = int(input("Digite um número: "))
    Lista_Numeros.append(Numeros)

Media_Numeros = Calcular_Media(Lista_Numeros)
print(f'A média dos números na lista é: {Media_Numeros}')