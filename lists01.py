""" 
nome = "Ana"
idade = 25
cidade = "São Paulo"

print(f"Olá! Meu nome é {nome}. Eu tenho {idade} anos e moro em {cidade}.")

numeros = [10,20,30,40,50]
soma = 0
for numero in numeros:
    soma += numero
media = soma / len(numeros)
print(media)

gastos_joao = [300, 500, 200, 800]
gastos_pedro = [200, 300, 500, 700]

total_gastos_joao = sum(gastos_joao)
total_gastos_pedro = sum(gastos_pedro)

if total_gastos_joao > total_gastos_pedro:
    print("João gastou mais dinheiro este mês.")
elif total_gastos_pedro > total_gastos_joao:
    print("Pedro gastou mais dinheiro este mês.")
else:
    print("João e Pedro gastaram a mesma quantia este mês.")

    
palavras = ["python","asimov","código","web","programação"]

maior_palavra = palavras[0]
menor_palavra = palavras[0]

for palavra in palavras:
    if len(palavra) > len(maior_palavra):
        maior_palavra  = palavra
    if len(palavra) < len(menor_palavra):
        menor_palavra  = palavra

print("A maior palavra é: ", maior_palavra)
print("A menor palavra é: ", menor_palavra)
"""  
numeros = [32, 10, 58, 30, 55, 12, 28, 51]

maior_valor = 0
segundo_maior_valor = 0

for numero in numeros:
    if numero > maior_valor:
        segundo_maior_valor = maior_valor  # o antigo maior vira o segundo
        maior_valor = numero
    elif numero > segundo_maior_valor:
        segundo_maior_valor = numero

print("Maior valor:", maior_valor)
print("Segundo maior valor:", segundo_maior_valor)









    

