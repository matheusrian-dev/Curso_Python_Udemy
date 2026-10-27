"""
# __dict__ e vars para atributos de instância
# __dict__ é um dicionário que contém os atributos de instância de um objeto.
# vars() é uma função que retorna o __dict__ de um objeto.

# Importante! O __dict__ é editável, ou seja, podemos adicionar, modificar e
# remover atributos de instância através dele, logo é preciso ter cautela ao
# utilizar.

"""


class Pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {'nome': 'Leah', 'idade': 18}

p1 = Pessoa(**dados)
# p1.nome = 'Nova'
# print(p1.idade)
# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'Nova'
# del p1.__dict__['nome']
# print(p1.__dict__)
# print(vars(p1))
# print(p1.outra)
# print(p1.nome)
print(vars(p1))
print(p1.nome)
