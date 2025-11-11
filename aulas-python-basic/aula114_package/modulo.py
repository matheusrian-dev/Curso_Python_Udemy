"""
Ao especificar o '__all__',
dizemos ao python para importar somente as variáveis e
metodos listados dentro dele quando se importar o módulo completamente.
Logo, utilizando o exemplo abaixo, ao importar o módulo atual com um
comando 'from aula114_package.modulo import *', apenas a variavel
especificada será importada.
"""

__all__ = [
    'variavel',
]

variavel = 'Qualquer coisa'


def soma_do_modulo(x, y):
    return x + y
