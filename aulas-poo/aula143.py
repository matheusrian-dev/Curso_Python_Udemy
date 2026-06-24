"""
class - Classes são moldes para criar novos objetos
As classes geram novos objetos (instâncias) que
podem ter seus próprios atributos e métodos.

Os objetos gerados pela classe podem usar seus dados
internos para realizar várias ações.
Por convenção, usamos PascalCase para nomes de
classes.

string = 'Matheus'  # str
print(string.upper())
print(isinstance(string, str))

O método __init__ é utilizado para inicializar a
classe.
"""


class Pessoa:
    # Qualquer método que for tratar da instância da
    # classe precisa receber como primeiro argumento o self.
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Matheus', 'Rian')
# p1.nome = 'Matheus'
# p1.sobrenome = 'Rian'

p2 = Pessoa('Beatriz', 'Neves')
# p2.nome = 'Beatriz'
# p2.sobrenome = 'Neves'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)
