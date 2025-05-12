"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop del, clear, extend, +
CRUD - Create Read Update Delete
"""

#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
lista = [
    123,
    True,
    'Matheus',
    1.2,
    [],
]
# além de mutável, a lista pode receber vários
# tipos de valores diferentes ao mesmo tempo
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))
# é possível criar com type conversion tbm
# mas não é recomendado ex: list(string)
# print(bool([])) #falsy
# print(lista, type(lista))
numero = lista[0]
print(numero)
