"""
Função lambda em Python
A função lambda é uma função como qualquer
outra em Python. Porém, são funções anônimas
que contém apenas uma linha. Ou seja, tudo
deve ser contido dentro de uma única expressão.
"""

lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# lista = [4, 32, 1, 3, 5, 123, 55]
# Ordena a lista
# lista.Sort()
# Ordena a lista de forma contrária ao padrão
# lista.Sort(reverse=True)
# Gera uma cópia rasa e ordenada da lista
# sorted(lista)

lista.sort(key=lambda item: item['nome'])

lista_ordenada_nome = sorted(lista, key=lambda item: item['nome'])
lista_ordenada_sobrenome = sorted(lista, key=lambda item: item['sobrenome'])


def exibir(lista):
    for item in lista:
        print(item)
    print()


exibir(lista_ordenada_nome)
exibir(lista_ordenada_sobrenome)
