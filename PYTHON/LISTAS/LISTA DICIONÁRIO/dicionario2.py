''''Dado um texto, conte quantas vezes cada caractere aparece (incluindo 
espaços e caracteres especiais) e armazene os resultados em um 
dicionário.'''

texto = input("Digite um texto: ")

contagens = {}

for caractere in texto:
    if caractere in contagens:
        contagens[caractere] += 1
    else:
        contagens[caractere] = 1

for caractere, contagem in contagens.items():
    if contagem == 1:
        print(f"'{caractere}': {contagem} vez")
    
    else:
        print(f"'{caractere}': {contagem} vezes")