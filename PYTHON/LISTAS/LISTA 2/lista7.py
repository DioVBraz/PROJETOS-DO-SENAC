Soma = 0
Contador = 0
Maior = float('-inf')  
Menor = float('inf')   

while True:
    Temperatura = input("Digite uma temperatura (Digite 'sair' para sair): ")
    
    if Temperatura.lower() == 'sair':  
        print("Fim")
        break

    Temperatura = float(Temperatura)

    if Temperatura > Maior:
        Maior = Temperatura
    if Temperatura < Menor:
        Menor = Temperatura

    Soma += Temperatura
    Contador += 1

if Contador > 0:
    Media = Soma / Contador
    print("Maior temperatura digitada:", Maior, "°C")
    print("Menor temperatura digitada:", Menor, "°C")
    print("Média das temperaturas digitadas:", Media, "°C")
else:
    print("Nenhuma temperatura foi informada.")
