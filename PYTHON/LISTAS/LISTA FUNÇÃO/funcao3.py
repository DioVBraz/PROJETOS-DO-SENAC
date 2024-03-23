'''Crie uma função chamada `contar_vogais` que recebe
uma string como argumento e retorna o número de vogais na string
(considere tanto maiúsculas quanto minúsculas).
'''

Frase = input("Digite uma frase: ").lower()

def Contar_Vogais(Frase):
    Vogais = 0
    for Letra in Frase:
        if Letra in "aeiou":
            Vogais += 1
    return Vogais
    
print("Total de vogais lidas:", Contar_Vogais(Frase))