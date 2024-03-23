Entrada_Numeros = input("Digite os números (separados por espaço): ")

Lista_Numeros = [float(Numero) for Numero in Entrada_Numeros.split()]

Opcao = input("Deseja ordenar em ordem crescente (C) ou decrescente (D)? ").upper()

if Opcao == 'C':
    Lista_Numeros.sort()

elif Opcao == 'D':
    Lista_Numeros.sort(reverse=True)
else:
    print("Opção inválida. Por favor, escolha 'C' para crescente ou 'D' para decrescente.")
    exit(1)

print("Lista ordenada:", Lista_Numeros)