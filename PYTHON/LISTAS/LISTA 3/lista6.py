Votos_Sistema = {
    "Windows Server": 0,
    "Unix": 0,
    "Linux": 0,
    "Netware": 0,
    "Mac OS": 0,
    "Outro": 0
}

while True:
    Voto = int(input("Digite o voto (1 a 6, 0 para encerrar): "))

    if Voto < 0 or Voto > 6:
        print("Voto inválido. Por favor, digite um valor de 1 a 6.")
        continue

    if Voto == 0:
        break

    if Voto == 1:
        Votos_Sistema["Windows Server"] += 1
    elif Voto == 2:
        Votos_Sistema["Unix"] += 1
    elif Voto == 3:
        Votos_Sistema["Linux"] += 1
    elif Voto == 4:
        Votos_Sistema["Netware"] += 1
    elif Voto == 5:
        Votos_Sistema["Mac OS"] += 1
    elif Voto == 6:
        Votos_Sistema["Outro"] += 1

Votos_Total = sum(Votos_Sistema.values())

Sistema_Vencedor = max(Votos_Sistema, key=Votos_Sistema.get)
Votos_Vencedor = Votos_Sistema[Sistema_Vencedor]
Percentual_Vencedor = (Votos_Vencedor / Votos_Total) * 100

print("Sistema Operacional    Votos   %")
print("-------------------    -----   ---")
for Sistema, Voto in Votos_Sistema.items():
    Percentual = (Voto / Votos_Total) * 100
    print(f"{Sistema:21} {Voto}   {Percentual:.0f}%")
print("-------------------    -----   ---")
print(f"Total                  {Votos_Total}")
print(f"O Sistema Operacional mais votado foi o {Sistema_Vencedor}, com {Votos_Vencedor} votos, correspondendo a {Percentual_Vencedor:.0f}% dos votos.")