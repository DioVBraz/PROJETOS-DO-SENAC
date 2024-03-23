Ano_1 = 1995
Salario_Inicial = float(input("Digite o salário inicial do funcionário: R$ "))
Ano_Atual = 2023

Anos = Ano_Atual - Ano_1

Aumento = 1.5

for _ in range(Anos):
    Salario_Inicial += (Aumento / 100) * Salario_Inicial
    Aumento *= 2

print(f"O salário atual do funcionário em {Ano_Atual} é: R$ {Salario_Inicial:.2f}")
