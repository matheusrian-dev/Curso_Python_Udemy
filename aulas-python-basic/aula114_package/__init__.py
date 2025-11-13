"""
O arquivo de inicialização (__init__) é
inicializado sempre que o package é importado.
Veja o exemplo no arquivo aula114.py
"""

# é possível utilizar variáveis e métodos importados no __init__
# como se fosse dele ao importar o package
# from aula114_package.modulo import soma_do_modulo

print('Você importou ', __name__)


def dobra(x):
    return x * 2
