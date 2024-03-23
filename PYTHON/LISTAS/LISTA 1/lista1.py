Peso = int(input("Qual o peso de peixes pescado hoje? "))
if Peso > 50:
    Excesso = Peso - 50
    Multa = Excesso * 4
    print(f'O limite de quilos pescado foi ultrapassado em: {Excesso} quilos, sua multa será de: R$ {Multa}')
else:
    print('O limite de quilos pescado é adequado')