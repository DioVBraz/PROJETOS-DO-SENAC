Pais_A = 80000
Crescimento_A = 3
Pais_B = 200000
Crescimento_B = 1.5
Anos = 0

while Pais_A < Pais_B:
    Pais_A = Pais_A * (1 + Crescimento_A / 100)
    Pais_B = Pais_B * (1 + Crescimento_B / 100)
    Anos += 1

print(f"O país A irá ultrapassar ou igualar o país B em {Anos} anos.")


