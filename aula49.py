"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ], # 0
    # 0
    ['Elaine', ],  # 1
    #0        1       2
    ['Luiz', 'João', 'Eduarda', ], #2
]

# print(salas[0][1])

for sala in salas: #primeiro for puxa a primeira lista
    print(f'A sala é {sala}')
    for aluno in sala: #segundo for puxa os itens de cada lista separado
        print(aluno)