Area = float(input("Digite o tamanho da área a ser pintada (m²): "))

Litros_Tinta = Area / 6

Latas_Tinta = int(Litros_Tinta / 18)
Preco_Latas = Latas_Tinta * 80

Galao_Tinta = int(Litros_Tinta / 3.6)
Preco_Galao = Galao_Tinta * 25

Latas_Mix = int((Litros_Tinta * 1.1) / 18)
Galao_Mix = int(((Litros_Tinta * 1.1) % 18) / 3.6)
Preco_mix = (Latas_Mix * 80) + (Galao_Mix * 25)

print(f"Opção 1: Comprar apenas latas de tinta - Quantidade: {Latas_Tinta}, Preço: R${Preco_Latas:.2f}")
print(f"Opção 2: Comprar apenas galões de tinta - Quantidade: {Galao_Tinta}, Preço: R${Preco_Galao:.2f}")
print(f"Opção 3: Misturar latas e galões - Quantidade de latas: {Latas_Mix}, Quantidade de galões: {Galao_Mix}, Preço: R${Preco_mix:.2f}")