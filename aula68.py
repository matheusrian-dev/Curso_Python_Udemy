"""
Dicionários em python (tipo dict)
Dicionários são estruturas de dados do tipo par de "chave" e "valor".
Chaves podem ser consideradas como o "índice" que vimos na lista e podem ser
de tipos imutáveis como: str, int, float, bool, tuple etc.
O valor pode ser de qualquer tipo, incluindo outro dicinoário.
Usamos as chaves - {} - ou a classe dict para criar dicionários.
Imutáveis: str, int, float , bool, tuple
Mutável: dict, list
pessoa = {
    'nome': 'Luiz' Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços':[
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
        ]
    ]
}
"""

pessoa = {
    "nome": "Matheus Rian",
    "sobrenome": "Souza",
    "idade": 26,
    "altura": 1.73,
    "endereços": [
        {"rua": "tal tal", "número": 123},
        {"rua": "outra rua", "número": 321},
    ],
}
# pessoa = dict(nome='Matheus Rian', sobrenome='Souza', idade=26) # É possível
# alimentar o dicionário na mesma linha porém esse método não é tão utilizado.
# print(pessoa, type(pessoa))
# print(pessoa['nome'], pessoa['sobrenome'])

# o dicionário em si não é iterável, mas ao fazer um for e pedindo pra exibir
# cada item dele, o python retorna cada chave(a chave! não o valor que foi
# inserido nela!).
# for chave in pessoa:
#     print(chave)
# caso queira retornar os valores, o for deve ser formatado da seguinte
# maneira:
for chave in pessoa:
    print(f"{chave}: {pessoa[chave]}")
