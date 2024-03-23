Combustivel = input("Digite o tipo de combustível (A - Álcool, G - Gasolina): ")
Lit_vendidos = float(input("Digite o número de litros vendidos: "))

Preco_alcool = 1.90
Preco_gasolina = 2.50

if Combustivel.lower() == 'a':
    if Lit_vendidos <= 20:
        Desconto = Lit_vendidos * 0.03
    else:
        Desconto = Lit_vendidos * 0.05
    Total_Preco = Lit_vendidos * Preco_alcool
else:
    if Lit_vendidos <= 20:
        Desconto = Lit_vendidos * 0.04
    else:
        Desconto = Lit_vendidos * 0.06
    Total_Preco = Lit_vendidos * Preco_gasolina

Total_Preco -= Desconto

print(f"Valor a ser pago: R${Total_Preco:.2f}")