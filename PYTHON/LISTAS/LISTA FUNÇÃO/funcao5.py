'''Escreva uma função chamada `inverter_string` que recebe
uma string como argumento e retorna a mesma string, mas invertida (ou
seja, o último caractere se torna o primeiro, o penúltimo se torna o
segundo, e assim por diante).'''

def Inverter_String(Frase):
  return Frase[::-1]

Frase = input("Digite uma frase: ")
print("Frase invertida:", Inverter_String(Frase))