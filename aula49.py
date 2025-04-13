"""
Lista de listas e seus índices
"""

salas = [
    [
        'Maria',
        'Helena',
    ],
    [
        'Elaine',
    ],
    [
        'Luiz',
        'João',
        'Eduarda',
    ],
]

# print(salas[0][1])

for sala in salas:  # primeiro for puxa a primeira lista
    print(f'A sala é {sala}')
    for aluno in sala:  # segundo for puxa os itens de cada lista separado
        print(aluno)
