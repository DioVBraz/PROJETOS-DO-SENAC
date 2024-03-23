Lista_Notas = []
Valor = 0
Quantidade_Notas = 0
Soma_Notas = 0

while Valor != -1:
    Valor = float(input("Digite uma nota (-1 para encerrar): "))
    if Valor != -1:
        Lista_Notas.append(Valor)
        Soma_Notas += Valor
        Quantidade_Notas += 1

print(f"Quantidade de notas lidas: {Quantidade_Notas}")

print("Notas informadas:")
for Nota in Lista_Notas:
    print(Nota, end=" ")

print("Notas na ordem inversa:")
for Nota in reversed(Lista_Notas):
    print(Nota)

print(f"Soma das notas: {Soma_Notas:.2f}")

if Quantidade_Notas > 0:
    Media_Notas = Soma_Notas / Quantidade_Notas
else:
    Media_Notas = 0
print(f"Média das notas: {Media_Notas:.2f}")

Acima_Media = len([Nota for Nota in Lista_Notas if Nota > Media_Notas])
print(f"Quantidade de notas acima da média: {Acima_Media}")

Abaixo_Sete = len([Nota for Nota in Lista_Notas if Nota < 7])
print(f"Quantidade de notas abaixo de sete: {Abaixo_Sete}")

print("Programa encerrado.")