"""
Exercícios - copy, sorted, lista.sort
- Aumente os preços dos produtos a seguir em 10%
- Gere novos_produtos por deep copy (cópia profunda)

- Ordene os produtos por nome decrescente ( do maior para menor)
- Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

- Ordene os produtos por preço crescente (do menor para maior)
- Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
"""

import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
print('Lista original')
for produto in produtos:
    print(f"Produto: {produto['nome']} | Preço: R${produto['preco']:.2f}")
print('================================================')
# Aumenta o preço
for produto in produtos:
    novo_preco = produto['preco']
    novo_preco += novo_preco * 0.1
    produto['preco'] = novo_preco
novos_produtos = copy.deepcopy(produtos)
print('Produtos com aumento de 10%')
for produto in novos_produtos:
    print(f"Produto: {produto['nome']} | Preço: R${produto['preco']:.2f}")
print('================================================')

# Ordena por nome decrescente
produtos.sort(reverse=True, key=lambda produto: produto['nome'])
produtos_ordenados_por_nome = copy.deepcopy(produtos)
print('Produtos ordenados por nome')
for produto in produtos_ordenados_por_nome:
    print(f"Produto: {produto['nome']} | Preço: R${produto['preco']:.2f}")
print('================================================')

# ordena por preço crescente
produtos.sort(key=lambda produto: produto['preco'])
produtos_ordenados_por_preco = copy.deepcopy(produtos)
print('Produtos ordenados por preço')
for produto in produtos_ordenados_por_preco:
    print(f"Produto: {produto['nome']} | Preço: R${produto['preco']:.2f}")
print('================================================')
