"""
Exercício - Unir listas
Crie uma função zipper (como o zipper de roupas)
O trabalho dessa função será unir duas
listas na ordem.
Use todos os valores da menor lista.
Ex.:
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']
Resultado
[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
"""

from itertools import zip_longest

list1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list2 = ['BA', 'SP', 'MG', 'RJ']


# Solução crua
# def zipper(list1, list2):
#     # Min busca o menor valor entre os itens passados
#     intervalo = min(len(list1), len(list2))
#     return [(list1[i], list2[i]) for i in range(intervalo)]


# zipper(list1, list2)

# Solução com zip()
# zip() une as listas se limitando ao tamanho da menor
print('Com zip()')
resultado = list(zip(list1, list2))

for item in resultado:
    print(item)
print('------------------------------------')
# Utilizando zip_longest()
# utilizando o zip_longest() da biblioteca itertools é possível
# fazer o inverso do zip, unindo as listas pela maior

print('Com zip_longest()')
# O parâmetro fillvalue é utilizado para substituir o None onde não
# há valor na lista menor.
resultado = list(zip_longest(list1, list2, fillvalue='Sem cidade'))

for item in resultado:
    print(item)
