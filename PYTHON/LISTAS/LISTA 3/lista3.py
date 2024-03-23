def Vetor_Intercalado(Vetor_1, Vetor_2):
    Vetor_Intercalado = []
    for Numero_1, Numero_2 in zip(Vetor_1, Vetor_2):
        Vetor_Intercalado.extend([Numero_1, Numero_2])
    return Vetor_Intercalado

def Vetores():
    Vetor = []
    for i in range(10):
        Numeros = int(input(f"Digite o {i + 1}° número do vetor: "))
        Vetor.append(Numeros)
    return Vetor

print("Digite os números do primeiro vetor:")
Vetor_1 = Vetores()

print("Digite os números do segundo vetor:")
Vetor_2 = Vetores()

Vetor_3 = Vetor_Intercalado(Vetor_1, Vetor_2)

print("Vetor intercalado:")
print(Vetor_3)