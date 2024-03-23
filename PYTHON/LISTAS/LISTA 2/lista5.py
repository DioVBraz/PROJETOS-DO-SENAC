n = int(input("Digite um número inteiro: "))
resultado = 1
i = 1

while i <= n:
  resultado *= i
  i += 1
print(n,"! =", end=" ")

for i in range(1, n + 1):
  print(i, end=".")
print("=", resultado)
