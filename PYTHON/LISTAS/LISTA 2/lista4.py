Numero = int(input('Digite um número: '))  
Contador = 1

while(Contador <= 10):  
  print('{1} X {0} = {2}'.format(Contador, Numero, (Contador * Numero)))  
  Contador = Contador + 1 