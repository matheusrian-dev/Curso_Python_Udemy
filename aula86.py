# Dictionary Comprehension e Set Comprehension
produto = {'nome': 'Caneta Azul', 'preco': 2.5, 'categoria': 'Escritório'}

# for chave, valor in produto.items:
#     print(chave, valor)

# Dictionary Comprehension
dc = {
    chave: valor.upper() if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    # Inclui apenas a chave mencionada
    if chave == 'categoria'
    # Exclui a chave mencionada
    if chave != 'categoria'
}

lista = [('a', 'valor a')('b', 'valor b')('c', 'valor c')]

# dc = {chave: valor for chave, valor in lista}
# consegue converter uma lista com valores que parecem dicionários
print(dict(lista))

# Set comprehension
# s1 = {i for i in range(10)}
print(set(range(10)))
