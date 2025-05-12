"""
Exercício
Exiba os índices da lista
0 - Karen
1 - Geovana
2 - Marina
"""

# Minha solução
lista = ['Karen', 'Geovana', 'Marina']
indice = 0
for nome in lista:
    print(f'{indice} - {nome}')
    indice += 1
# Solução do Instrutor
# lista = ['Karen', 'Geovana', 'Marina']
# indices = range(len(lista)) # retorna o tamanho da lista

# retorna o índice, o valor incluido naquele indice e o tipo do valor
# for indice in indices:
#     print(indice, lista[indice], type(lista[indice]))
