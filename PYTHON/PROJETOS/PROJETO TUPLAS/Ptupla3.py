Lista_Voos = [
    (105, "Uberlândia", "São Paulo", "19-09-2023", 200.00),
    (106, "Rio de Janeiro", "Manaus", "26-09-2023", 180.00),
    (107, "Porto Alegre", "Belo Horizonte", "06-10-2023", 220.00),
    (108, "Uberaba", "Caldas Novas", "22-10-2023", 280.00),
    (109, "Brasília", "São Paulo", "29-10-2023", 320.00),
    (110, "Brasília", "Buenos Aires", "04-11-2023", 330.00),
    (111, "Rio de Janeiro", "Santiago", "18-11-2023", 270.00),
    (112, "São Paulo", "Las Vegas", "26-11-2023", 350.00),
    (113, "Uberlândia", "Teresina", "30-11-2023", 420.00),
    (114, "Goiânia", "Salvador", "02-12-2023", 150.00),
    (115, "Manaus", "Montevidéu", "14-12-2023", 330.00),
    (116, "Cuíaba", "Curitiba", "25-12-2023", 270.00),
    (117, "São Paulo", "Madrid", "01-01-2024", 350.00),
    (118, "Rio de Janeiro", "Montreal", "07-01-2024", 380.00),
    (119, "Curitiba", "Bogotá", "19-01-2024", 350.00),
    (120, "Rio Branco", "Fortaleza", "10-02-2024", 150.00),
    (121, "Recife", "São Paulo", "21-02-2024", 180.00),
    (122, "Porto Velho", "Goiânia", "05-03-2024", 220.00),
    (123, "Porto Alegre", "Uberaba", "13-03-2024", 280.00),
    (124, "Salvador", "João Pessoa", "26-03-2024", 320.00),
]

Reservas = {}

while True:
    print("Opções:")
    print("1 - Listar voos disponíveis")
    print("2 - Reservar passagem")
    print("3 - Cancelar reserva")
    print("4 - Listar voos reservados")
    print("5 - Sair")

    Escolha = input("Escolha uma opção: ")

    if Escolha == "1":
        print("Voos Disponíveis:")
        for Numero, Origem, Destino, Data, Preco in Lista_Voos:
            print(f"Voo {Numero}: De {Origem} para {Destino}, Data: {Data}, Preço: R${Preco:.2f}")

    elif Escolha == "2":
        Numero_Voo = int(input("Digite o número do voo desejado: "))
        Nome_Passageiro = input("Digite o nome do passageiro: ")
        Voo = False
        for Numero, _, _, _, _ in Lista_Voos:
            if Numero_Voo == Numero:
                Voo = True
                if Numero_Voo not in Reservas:
                    Reservas[Numero_Voo] = [(Nome_Passageiro,)]
                else:
                    Reservas[Numero_Voo].append((Nome_Passageiro,))
                print(f"Passagem reservada no Voo {Numero_Voo} para {Nome_Passageiro}.")
                break
        if not Voo:
            print(f"Voo com número {Numero_Voo} não encontrado.")

    elif Escolha == "3":
        Numero_Voo = int(input("Digite o número do voo desejado: "))
        Nome_Passageiro = input("Digite o nome do Passageiro: ")
        if Numero_Voo in Reservas:
            for i, (Passageiro,) in enumerate(Reservas[Numero_Voo]):
                if Nome_Passageiro == Passageiro:
                    del Reservas[Numero_Voo][i]
                    print(f"Reserva cancelada no Voo {Numero_Voo} para {Nome_Passageiro}.")
                    break
            else:
                print("Reserva não encontrada.")
        else:
            print("Reserva não encontrada.")

    elif Escolha == "4":
        print("Voos Reservados:")
        for Numero_Voo, Reserva_Passageiro in Reservas.items():
            for (Passageiro,) in Reserva_Passageiro:
                print(f"Número do Voo: {Numero_Voo} | Passageiro: {Passageiro}")

    elif Escolha == "5":
        break
    else:
        print("Não é possível sair do programa.")