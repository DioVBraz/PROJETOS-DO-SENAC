def Consoante(Caractere):
    Consoantes_Total = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return Caractere in Consoantes_Total

Lista_Caracteres = []

for i in range(10):
    Letras = input("Digite um caractere: ")
    Lista_Caracteres.append(Letras)

Contagem_Consoantes = 0

Consoantes = []

for Caractere in Lista_Caracteres:
    if Consoante(Caractere):
        Contagem_Consoantes += 1
        Consoantes.append(Caractere)

print(f"Total de consoantes lidas: {Contagem_Consoantes}")
if Contagem_Consoantes > 0:
    print("Consoantes lidas:", ", ".join(Consoantes))
else:
    print("Nenhuma consoante foi lida")