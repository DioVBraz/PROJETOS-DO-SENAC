maior = 0
contador = 0
while contador < 5:
    numero = int(input("Digite um número: "))
    if numero > maior:
        maior = numero
    contador += 1
print("O maior número é", maior)


