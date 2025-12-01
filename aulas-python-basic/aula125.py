"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa - Iterável + tamanho do grupo
Permutação - Ordem importa
Produto - Ordem importa e repete valores únicos
"""

from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = ['João', 'Joana', 'Leah', 'Mariana']

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster'],
]

# O combinations gera combinações de tamanho N retiradas do iterável
# sem repetir elementos e nem considerar ordem (AB seria igual a BA).
print_iter(combinations(pessoas, 2))
# Já o permutations gera todas as combinações possíveis levando
# em consideração também a ordem (AB e BA constam como valores distintos).
print_iter(permutations(pessoas, 2))
# O product gera o produto cartesiano entre iteráveis, ou seja, pega
# todas as combinações possíveis pegando um elemento de cada iterável.
print_iter(product(*camisetas))
