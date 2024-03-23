Entrada_Letras = input("Digite uma string: ")

Contador_Vogais = 0
Contador_Consoantes = 0

vogais = "aeiouAEIOU"

for Letra in Entrada_Letras:
    if Letra in vogais:
        Contador_Vogais += 1
    elif Letra.isalpha():
        Contador_Consoantes += 1

Resultado = (Contador_Vogais, Contador_Consoantes)

print(f"Número de vogais na string: {Resultado[0]}")
print(f"Número de consoantes na string: {Resultado[1]}")