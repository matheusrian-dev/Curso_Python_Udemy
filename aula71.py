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

import copy

# copy
d1 = {'c1': 1, 'c2': 2, 'l1': [0, 1, 2]}

# O método copy é útil para criar cópias rasas
# que podem ser alteradas futuramente. Isso é especialmente útil
# em casos com listas mutáveis para impedir comportamentos não
# intencionais como o abaixo, ao alterar uma chave no d2,
# d1 é afetado também, pois ao atribuir diretamente um objeto mutável
# a outro, os dois passam a apontar pro mesmo lugar na memória,
# fazendo com que qualquer alteração no valor impacte ambos.
# d2 = d1
# d2['c1'] = 100
# print(d1)

# Ponto importante sobre cópias rasas: valores mutáveis dentro das chaves
# como listas, não são copiadas, o método apenas aponta para o mesmo local
# na memória. Provavelmente para poupar memória em códigos extensos
# d2 = d1.copy()
# d2 = copy.copy(d1)
# d2['c1'] = 100
# d2['l1'][1] = 999
# print(d1)
# print(d2)

# Caso necessite de uma cópia completa, utilize o método copy.deepcopy()
d2 = copy.deepcopy(d1)
d2['c1'] = 100
d2['l1'][1] = 999
print(d1)
print(d2)
