Num = []

Quantidade = int(input("Quantos números você deseja inserir? "))

for i in range(Quantidade):
    Numero = float(input(f"Digite o {i+1}º número: "))
    Num.append(Numero)

Media = sum(Num) / Quantidade

print(f"A média dos números é: {Media:.2f}")