Lista_Disciplinas = []

while True:
    Disciplina = input("Digite o nome da disciplina (ou digite 'sair' para encerrar): ")
    if Disciplina.lower() == 'sair':
        break
    Lista_Disciplinas.append(Disciplina)

Lista_Alunos = []

while True:
    Nome_Aluno = input("Digite o nome do aluno (ou digite 'sair' para encerrar): ")
    if Nome_Aluno.lower() == 'sair':
        break

    Lista_Notas = []
    for Disciplina in Lista_Disciplinas:
        Nota_Aluno = float(input(f"Digite a nota de {Disciplina} para {Nome_Aluno}: "))
        Lista_Notas.append(Nota_Aluno)

    Lista_Alunos.append((Nome_Aluno, Lista_Notas))

if not Lista_Alunos:
    print("Nenhum aluno registrado.")
else:
    Media_Alunos = []
    for Aluno in Lista_Alunos:
        Nome, Notas = Aluno
        Media = sum(Notas) / len(Notas)
        Media_Alunos.append((Nome, Media))

    Media_alta = sorted(Media_Alunos, reverse=True)
    Media_Baixa = sorted(Media_Alunos)

    print("\nMédias dos alunos:")
    for Nome, Media in Media_Alunos:
        print(f"{Nome}: {Media:.2f}")

    print("\nAlunos com as médias mais altas:")
    for Nome, Media in Media_alta:
        print(f"{Nome}: {Media:.2f}")

    print("\nAlunos com as médias mais baixas:")
    for Nome, Media in Media_Baixa:
        print(f"{Nome}: {Media:.2f}")