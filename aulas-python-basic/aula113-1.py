"""
Os módulos do python são singleton por padrão.
Isso significa que ao importar um módulo, ele será
carregado apenas uma vez e após isso será salvo na
memória e consultado sempre que necessário.

Caso precise recarregar o módulo por algum motivo,
utilize importlib e o método reload para isso.
"""

import importlib
import aula113

print(aula113.variavel)

for i in range(5):
    importlib.reload(aula113)
    print(i)

print('Fim.')
