Candidato_1 = 0
Candidato_2 = 0
Candidato_3 = 0
Candidato_4 = 0
Votos_Nulos = 0
Votos_Branco = 0
Votos_Total = 0

while True:
    Votos = int(input("Digite o código do candidato (1, 2, 3, 4, 5 para nulo, 6 para em branco, 0 para encerrar): "))
    
    if Votos == 0:
        break
    
    Votos_Total += 1

    if Votos == 1:
        Candidato_1 += 1

    elif Votos == 2:
        Candidato_2 += 1

    elif Votos == 3:
        Candidato_3 += 1

    elif Votos == 4:
        Candidato_4 += 1

    elif Votos == 5:
        Votos_Nulos += 1

    elif Votos == 6:
        Votos_Branco += 1

Percentual_Nulos = (Votos_Nulos / Votos_Total) * 100
Percentual_Branco = (Votos_Branco / Votos_Total) * 100

print(f"Total de votos para o Candidato 1: {Candidato_1}")
print(f"Total de votos para o Candidato 2: {Candidato_2}")
print(f"Total de votos para o Candidato 3: {Candidato_3}")
print(f"Total de votos para o Candidato 4: {Candidato_4}")
print(f"Total de votos nulos: {Votos_Nulos}")
print(f"Total de votos em branco: {Votos_Branco}")
print(f"Percentagem de votos nulos sobre o total de votos: {Percentual_Nulos} %")
print(f"Percentagem de votos em branco sobre o total de votos: {Percentual_Branco} %")