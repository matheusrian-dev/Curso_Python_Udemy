# Problema dos parâmetros mutáveis em funções Python
"""
Se você chamar um método que requer um parâmetro mutável
sem definir o mesmo. O Python irá armazenar a primeira
criação do mesmo e o utilizará em todas as próximas chamadas
mesmo se armazenadas em variáveis distintas.
"""

# def adiciona_clientes(nome, lista=[]):
#     lista.append(nome)
#     return lista

# O método mais simples de se resolver isso é gerando a lista previamente
# lista_1 = []

# cliente_1 = adiciona_clientes('Luiz')
# adiciona_clientes('Joana', cliente_1)
# print(cliente_1)

# # Não irá gerar uma segunda lista, apenas adicionar os valores
# # na lista utilizada em cliente_1.
# cliente_2 = adiciona_clientes('Rafael')
# adiciona_clientes('Miranda', cliente_2)
# print(cliente_2)


# -------------------------------------------------------------------------
# Mas a forma ideal é não passar valores mutáveis como parâmetros nesse
# caso!


def adiciona_clientes(nome, lista=None):
    # Usando None como parâmetro aqui, você garante que, se caso não for
    # inserida uma lista nos parâmetros, uma nova será criada.
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


novos_clientes = adiciona_clientes('Natália')
adiciona_clientes('Marcos', novos_clientes)
print(novos_clientes)

velhos_clientes = adiciona_clientes('Raquel')
adiciona_clientes('Marina', velhos_clientes)
print(velhos_clientes)
