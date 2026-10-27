"""
# Exercício - Salve sua classe em JSON
Salve os dados da sua classe em JSON e depois
crie  novamente as instâncias da classe com os dados salvos.
Faça em arquivos separados.
"""

import json


class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade


p1 = Pessoa('Leah', 'Neves', 26)

with open('aula150_file.json', 'w', encoding='utf-8') as arquivo:
    json.dump(p1.__dict__, arquivo, ensure_ascii=False)
