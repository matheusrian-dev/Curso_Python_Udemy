# reduce - faz a redução de um iterável em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

# def funcao_do_reduce(acumulador, produto):
#     print('acumulador', acumulador)
#     print('produto', produto)
#     print()
#     return acumulador + produto['preco']

# De forma mais resumida: reduce aplica uma função acumuladora a uma lista,
# combinando os elementos um por um, até restar apenas um valor.
# Obs: É recomendado sempre passar um valor inicial (0 nesse caso), mas
# é possível utilizar sem isso.
total = reduce(lambda ac, p: ac + p['preco'], produtos, 0)

# pode ser feito com outros operadores também:
# total = reduce(lambda ac, p: ac * p['preco'], produtos, 0)

print('Total é ', total)

# total = 0
# for p in produtos:
#     total += p['preco']

# print(total)

# print(sum([p['preco'] for p in produtos]))
