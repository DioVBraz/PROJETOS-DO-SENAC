Respostas_Positivas = 0

Pergunta_1 = input("Telefonou para a vítima? (Sim ou Não): ")
Pergunta_2 = input("Esteve no local do crime? (Sim ou Não): ")
Pergunta_3 = input("Mora perto da vítima? (Sim ou Não): ")
Pergunta_4 = input("Devia para a vítima? (Sim ou Não): ")
Pergunta_5 = input("Já trabalhou com a vítima? (Sim ou Não): ")

if Pergunta_1.lower() == "sim":
    Respostas_Positivas += 1

if Pergunta_2.lower() == "sim":
    Respostas_Positivas += 1

if Pergunta_3.lower() == "sim":
    Respostas_Positivas += 1

if Pergunta_4.lower() == "sim":
    Respostas_Positivas += 1

if Pergunta_5.lower() == "sim":
    Respostas_Positivas += 1


if Respostas_Positivas == 2:
    Resultado = "Suspeita"

elif 3 <= Respostas_Positivas <= 4:
    Resultado = "Cúmplice"

elif Respostas_Positivas == 5:
    Resultado = "Assassino"

else:
    Resultado = "Inocente"

print(f"Classificação: {Resultado}")