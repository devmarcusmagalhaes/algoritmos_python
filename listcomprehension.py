"""
# [expressão for item in sequência if condição]
numeros = [x for x in range(10)]
print(numeros)

quadrados = [x**2 for x in range(10)]
print(quadrados)

pares = [x for x in range(10) if x % 2 == 0]
print(pares)

numeros = [numero for numero in range(10)]
print(numeros)

quadrados = [numero**2 for numero in range(10)]
print(quadrados)

pares = [numero for numero in range(21) if numero % 2 == 0]
print(pares)

nomes = ["ana","bia","carlos","daniel"]
maiusculas = [nome.upper() for nome in nomes]
print(maiusculas)

numeros = [1,4,9,16,25,36,49]
maiores = [numero for numero in numeros if numero > 10]
print(maiores)

palavras = ["python", "java", "c", "sql", "html"]
longas = [palavra for palavra in palavras if len(palavra) > 3]
print(longas)

multiplicados = [numero*3 for numero in range(10)]
print(multiplicados)
"""
temperaturas = [30, 22, 25, 28, 35]


fahrenheit = [ grau*1.8 + 32 for grau in temperaturas]
print(fahrenheit)

