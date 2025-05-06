"""
1. Manipulação de Dicionário
Crie uma função que recebe uma lista de dicionários com nomes
e idades de pessoas, e retorna um novo dicionário com os nomes
como chave e a idade como valor, mas apenas das pessoas com 18
anos ou mais.

entrada = [
    {'nome': 'João', 'idade': 17},
    {'nome': 'Maria', 'idade': 22},
    {'nome': 'José', 'idade': 18},
]

saida = {
    'Maria': 22,
    'José': 18
}
"""

entrada = [
    {'nome': 'João', 'idade': 17},
    {'nome': 'Maria', 'idade': 22},
    {'nome': 'José', 'idade': 18},
]

novo_dicionario = {}


def adiciona_ao_dicionario(lista):
    # novo_dicionario = {
    #     chave: 'nome' for chave, valor in dict.items() if dict['idade'] >= 18
    # }
    for dicionario in lista:
        if dicionario['idade'] >= 18:
            chave = dicionario['nome']
            valor = dicionario['idade']
            novo_dicionario[chave] = valor
    return novo_dicionario


adiciona_ao_dicionario(entrada)

print(novo_dicionario)

# Resolução ChatGPT
# entrada = [
#     {'nome': 'João', 'idade': 17},
#     {'nome': 'Maria', 'idade': 22},
#     {'nome': 'José', 'idade': 18},
# ]

# maiores_de_idade = {
#     pessoa['nome']: pessoa['idade']
#     for pessoa in entrada
#     if pessoa['idade'] >= 18
# }

# print(maiores_de_idade)
