Area = float(input("Digite o tamanho da área a ser pintada (m²): "))

Litros_Tinta = Area / 3
Latas_Tinta = int(Litros_Tinta / 18)
Total_Preco = Latas_Tinta * 80

print(f"Quantidade de latas de tinta a serem compradas: {Latas_Tinta}")
print(f"Preço total: R${Total_Preco:.2f}")