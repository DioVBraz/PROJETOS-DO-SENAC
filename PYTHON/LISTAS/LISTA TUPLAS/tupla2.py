Lista_Disciplinas = ["Matemática", "Português", "Ciências", "História", "Geografia"]
Lista_Notas = []

for Disciplina in Lista_Disciplinas:
    Nota = float(input(f"Digite a nota do aluno em {Disciplina}: "))
    Lista_Notas.append(Nota)

Notas_Aluno = tuple(Lista_Notas)

Soma_Notas = sum(Notas_Aluno)
Quantidade_Disciplinas = len(Notas_Aluno)
Media = Soma_Notas / Quantidade_Disciplinas

print(f"A média das notas do aluno é: {Media:.2f}")