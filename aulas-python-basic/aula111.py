# Módulos padrão do Python (import, from, as e *)
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
# import sys

# platform = 'A MINHA'
# print(sys.platform)
# print(platform)

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
# from sys import exit, platform

# Lembre-se que caso importe dessa forma,
# ao gerar um objeto com o mesmo nome, ele irá
# sobrescrever o método importado.
# platform = 'minha variável'

# print(platform)

# alias 1 - import nome_modulo as apelido
# Evite mudar o nome dos módulos do python! Por questão de
# familiaridade, é preferível utilizar objetos com nomes diferentes
# do que utilizar apelidos para os módulos padrões.
# import sys as s

# sys = 'alguma coisa'
# print(s.platform)
# print(sys)


# alias 2 - from nome_modulo import objeto as apelido
# from sys import exit as ex
# from sys import platform as pf

# print(pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo
# from sys import exit, platform

# print(platform)
# exit()
