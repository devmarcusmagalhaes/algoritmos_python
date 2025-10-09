def calcularNotas():
    alunos = {}

    # Coleta nome e nota de 3 alunos
    for i in range(3):
        nome = input(f"Digite o nome do {i+1}º aluno: ")
        nota = float(input(f"Digite a nota de {nome}: "))
        alunos[nome] = nota  # adiciona ao dicionário

    # Calcula a média das notas
    soma = sum(alunos.values())
    media = soma / len(alunos)

    # Exibe as notas e a média
    print("\nNotas dos alunos:")
    for nome, nota in alunos.items():
        print(f"{nome}: {nota}")

    print(f"\nMédia da turma: {media:.2f}")


# Chamada da função
calcularNotas()
