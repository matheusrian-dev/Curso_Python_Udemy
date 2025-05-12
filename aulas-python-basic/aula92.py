# isinstance - para saber se objeto é de determinado tipo
lista = [
    'a',
    1,
    1.1,
    True,
    [0, 1, 2],
    (1, 2),
    {0, 1},
    {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set):
        print('Set')
        item.add(5)
        print(item, isinstance(item, set))
    elif isinstance(item, str):
        print('STRING')
        print(item.upper())
    elif isinstance(item, int, float):
        print('numbers')
        print(item, item * 2)
    else:
        print('Outros')
