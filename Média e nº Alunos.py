num_alunos = int(input("Digite o número de alunos: "))
medias = []

for i in range(num_alunos):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    notas = []
    for n in range(3):
        while True: 
            try:
                nota = float(input(f"Digite a nota {n + 1} de {nome}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("A nota deve estar entre 0 e 10. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")

    media = sum(notas) / len(notas)
    medias.append(media)

    if media >= 7.0:
        status = "Aprovado"
    else:
        status = "Reprovado"

    print(f"Aluno: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {status}")

media_geral = sum(medias) / num_alunos
print(f"Média geral da turma: {media_geral:.2f}")