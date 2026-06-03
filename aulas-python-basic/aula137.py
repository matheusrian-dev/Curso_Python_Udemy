"""
Salvando dados Python em JSON

O que é JSON (.json)?
JSON é uma estrutura para transporte e
armazenamento de dados.
"""

import json

pessoa = {
    'nome': 'Beatriz',
    'sobrenome': 'Neves',
    'enderecos': [
        {'rua': 'Rua A', 'numero': 11},
        {'rua': 'Rua B', 'numero': 22},
    ],
    'altura': 1.70,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': False,
    'nada': None,
}

with open('aula137.json', 'w', encoding='utf8') as arquivo:
    # A função dump insere um objeto no arquivo
    # Insira ensure_ascii caso queira garantir acentuação concisa.
    json.dump(pessoa, arquivo, ensure_ascii=False)

# with open('aula117.json', 'r', encoding='utf8') as arquivo:
#     # A função load carrega os dados de um arquivo json para
#     # um objeto.
#     pessoa = json.load(arquivo)
#     # print(pessoa)
#     # print(type(pessoa))
#     print(pessoa['nome'])
