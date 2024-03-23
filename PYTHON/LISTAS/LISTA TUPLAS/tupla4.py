def Troca(Val_1, Val_2):
    Val_1, Val_2 = Val_2, Val_1
    
    return (Val_1, Val_2)

Valor_1 = input("Digite o valor 1: ")
Valor_2 = input("Digite o valor 2: ")

Novo_1, Novo_2 = Troca(Valor_1, Valor_2)

print("Novo Valor 1:", Novo_1)
print("Novo Valor 2:", Novo_2)