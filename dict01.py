dicio = {'chave': 'valor'}
print(type(dicio))

dicio02 = {'primeiro': 1, 'segundo': 2, 'terceiro': 3}

dicio03 = dict(primeiro=1, ssegundo=2, terceiro=3)

dicio04 = dict(zip(['primeiro', 'segundo', 'terceiro'], [1, 2, 3]))

dicio05 = dict([('primeiro', 1), ('segundo', 2), ('terceiro', 3)])

pessoa = {'nome': 'Pythonico', 'altura': 1.65, 'idade': 21}

print(pessoa['nome'])
print(pessoa.get('nome'))
print(pessoa.get('peso', 'Chave não encontrada'))

dict.keys()
dict.values()
dict.items()
dict.update()

