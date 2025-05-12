"""
Métodos úteis dos dicionários em Python:
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
"""

# Observação: chaves com nomes iguais contam como apenas uma e
# seu valor é sobreposto.
pessoa = {
    "nome": "Matheus Rian",
    "sobrenome": "Souza",
    "idade": 26,
    "altura": 1.73,
}

# setdefault serve para atribuir um valor padrão para uma chave
# isso auxilia nos casos em que não há chave ou valor nenhum no
# dicionário com o nome passado ou se quiser alterar o
# valor padrão (None).
pessoa.setdefault('idade', 0)
print(pessoa["idade"])

# len
# Utilizada para retornar a quantidade de chaves, porém não é
# recomendado pela nomenclatura contraintuitiva.
# print(pessoa.__len__())
# Método mais legível.
print(len(pessoa))

# keys
# Dessa forma retorna 'dict keys' que parece com uma lista com as
# chaves do dicionário (ainda sim não é uma lista!).
# print(pessoa.keys())
# pode ser convertido em listas e tuplas
print(list(pessoa.keys()))

# values
# O mesmo acontece com values e com items.
# print(pessoa.values())
print(list(pessoa.values()))

# items
# print(pessoal.items())
print(list(pessoa.items()))

for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')
