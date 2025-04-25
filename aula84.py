"""
List comprehension em Python
É uma forma rápida para criar listas a partir de iteráveis.
"""

import pprint


def formatacao_pprint(v):
    pprint.pprint(novos_produtos, sort_dicts=False, width=40)


# print(list(range(10)))
lista = []

# Método básico para incluir de forma rápida de incluir os valores
# for numero in range(10):
#     lista.append(numero)

# print(lista)

# Método com List Comprehension
# lista = [numero for numero in range(10)]
# Insere o mesmo número em todas as iterações do range
# lista = [1 for numero in range(10)]
# É possível fazer operações também
# lista = [numero * numero for numero in range(10)]
# print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {
        'nome': 'p1',
        'preco': 20,
    },
    {
        'nome': 'p2',
        'preco': 10,
    },
    {
        'nome': 'p3',
        'preco': 30,
    },
]

# novos_produtos = [produto['nome'] for produto in produtos]
# novos_produtos = [
#     {'nome': produto['nome'], 'preco': produto['preco']}
#     for produto in produtos
# ]
# Desempacotando os dados e inserindo um aumento de 5% no preço do produto
novos_produtos = [
    (
        {**produto, 'preco': produto['preco'] * 1.05}
        # é possível usar um if também para mapear dados entre a alimentação
        # do dicionário e o for, nesse caso foi acrescentado o aumento
        # somente nos produtos com preço acima de 20
        if produto['preco'] > 20
        else {**produto}
    )
    for produto in produtos
    if produto['preco'] >= 20 and produto['preco'] > 10
]
# print(*novos_produtos, sep='\n')

# Pprint é um módulo do Python para formatação dos prints podendo mexer com a
# configuração das linhas e ordenação dos dados
# formatacao_pprint(novos_produtos)

# Lembre-se!!! o if antes do for é mapeamento e o if depois do for é filtro!!!
lista = [n for n in range(10) if n < 5]
print(lista)
