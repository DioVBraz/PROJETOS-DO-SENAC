Morangos = float(input("Digite a quantidade de morangos (em Kg): "))
Macas = float(input("Digite a quantidade de maçãs (em Kg): "))

Preco_morangos = Morangos * (2.50 if Morangos <= 5 else 2.20)
Preco_macas = Macas * (1.80 if Macas <= 5 else 1.50)

Total_kg = Morangos + Macas
if Total_kg > 8 or (Preco_morangos + Preco_macas) > 25:
    Desconto = (Preco_morangos + Preco_macas) * 0.10
else:
    Desconto = 0

Total_Preco = (Preco_morangos + Preco_macas) - Desconto

print(f"Valor a ser pago: R${Total_Preco:.2f}")