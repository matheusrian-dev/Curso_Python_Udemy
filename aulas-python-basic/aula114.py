# Introdução aos Packages em Python

# Duas formas de importar o módulo, a segunda é mais legível
# e geralmente é a recomendada.

# import aula114_package.modulo
# from aula114_package.modulo import soma_do_modulo

# # print(aula114_package.modulo.soma_do_modulo(5, 2))
# print(soma_do_modulo(1, 3))

# Há também uma terceira forma de importar um módulo, porém
# ela é considerada uma má prática, já que corre o risco de
# misturar suas variáveis e métodos com os do módulo que está
# importando.
# from aula114_package.modulo import *
# print(soma_do_modulo(1,8))

import aula114_package

print(aula114_package.dobra(2))
# é possível utilizar variáveis e métodos importados no __init__
# como se fosse dele ao importar o package
# print(aula114_package.soma_do_modulo(2, 3))
