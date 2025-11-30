def separador_exercicio():
    print()
    print('-----------------------------------------------')
    print()


# Exercício 1 — Unir produtos e preços
produtos = ['Arroz', 'Feijão', 'Macarrão', 'Azeite']
precos = [25.90, 7.99, 5.49]

relacao_produto_preco = list(zip(produtos, precos))
print('Relação produto - preço')
print(relacao_produto_preco)
separador_exercicio()

# Exercício 2 — Criar um dicionário com zip
print('Dicionário com zip()')
nomes = ['Ana', 'Bruno', 'Carlos']
idades = [22, 35, 19]
dicionario_pessoa = dict(zip(nomes, idades))
print(dicionario_pessoa)
separador_exercicio()

# Exercício 3 — Somas paralelas
print('Soma das listas:')
lista_a = [10, 20, 30, 40]
lista_b = [1, 2, 3, 4]

lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)
