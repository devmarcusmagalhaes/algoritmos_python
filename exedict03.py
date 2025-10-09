
"""
produtos = {'shampoo': 10, 'condicionador': 25,
            'sabonete': 30, 'pasta de dente': 5}

produto = input("Digite um produto: ")

if produto in produtos:
    print(
        f"Nome do produto: {produto} -- Quantidade em estoque: {produtos[produto]}")
else:
    print("Produto não cadastrado")
"""
tradutor = {'Azul': 'Blue', 'Vermelho': 'Red',
            'Verde': 'Green', 'Amarelo': 'Yellow'}

palavra = input("Digite uma cor(em portugûes) para traduzir para inglês: ")

if palavra in tradutor:
    print(f"Tradução: {palavra} (Português) -- {tradutor[palavra]} (Inglês)")
else:
    print("Cor inválida.")
