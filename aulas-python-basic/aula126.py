# groupby- agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]


def ordena(aluno):
    return aluno['nota']


alunos_agrupados = sorted(alunos, key=ordena)
# groupby agrupa elementos consecutivos de um iterável que possuem
# o mesmo valor de chave.
grupos = groupby(alunos_agrupados, key=ordena)

print('Alunos agrupados por nota:')
for chave, grupo in grupos:
    print(f'Nota: {chave}')
    for aluno in grupo:
        print(aluno['nome'])
    print()

# Importante! A ordem importa, pois o groupby só agrupa elementos
# em sequência! Ou seja, é preciso ordenar a lista de dicionários
# previamente.

# Curiosidade: se não passar a key para ordenar a lista, o groupby
# utiliza a própria variável do iterável como chave (no caso acima
# o próprio dicionário).
# Ou seja: groupby(alunos) = groupby(alunos, key=lambda x:x)
