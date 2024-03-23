Carne_Tipo = input("Digite o tipo de carne (F - Filé Duplo, A - Alcatra, P - Picanha): ")
Carne_Quantidade = float(input("Digite a quantidade de carne em Kg: "))
Cartao_Tabajara = input("Pagamento com Cartão Tabajara? (S - Sim, N - Não): ")

Preco_File_Duplo = 4.90
Preco_Alcatra = 5.90
Preco_Picanha = 6.90

if Carne_Tipo.lower() == 'f':
    Total_Preco = Carne_Quantidade * Preco_File_Duplo
elif Carne_Tipo.lower() == 'a':
    Total_Preco = Carne_Quantidade * Preco_Alcatra
elif Carne_Tipo.lower() == 'p':
    Total_Preco = Carne_Quantidade * Preco_Picanha

if Cartao_Tabajara.lower() == 's':
    Desconto = Total_Preco * 0.05
else:
    Desconto = 0

print("Cupom Fiscal")
print(f"Tipo de Carne: {Carne_Tipo}")
print(f"Quantidade de Carne: {Carne_Quantidade} Kg")
print(f"Preço Total: R${Total_Preco:.2f}")
print(f"Tipo de Pagamento: {'Cartão Tabajara' if Cartao_Tabajara.lower() == 's' else 'Dinheiro'}")
print(f"Valor do Desconto: R${Desconto:.2f}")
print(f"Valor a Pagar: R${Total_Preco - Desconto:.2f}")