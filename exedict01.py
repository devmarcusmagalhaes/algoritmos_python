"""
def contaVogais(texto):
    # Dicionário com todas as vogais iniciando com 0
    vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    # Percorre cada caractere do texto
    for letra in texto.lower():  # transforma tudo em minúsculo
        if letra in vogais:      # verifica se é vogal
            vogais[letra] += 1   # soma 1 no contador da vogal

    return vogais


# Programa principal
texto = input("Digite um texto: ")
resultado = contaVogais(texto)

# Exibe o resultado
print("\nQuantidade de cada vogal:")
for vogal, quantidade in resultado.items():
    print(f"{vogal}: {quantidade}")
"""


def contaLetras(palavra):
    letras = {}
    for letra in palavra.lower():
        if letra in letras:
            letras[letra] += 1
        else:
            letras[letra] = 1

    return letras


palavra = input("Digite uma palavra:")
resultado = contaLetras(palavra)

print(f"Número de letras na palavra: {resultado.items()}")
