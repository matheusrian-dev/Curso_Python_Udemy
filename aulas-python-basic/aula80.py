"""
Exemplos - Funções Lambda
"""


def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador

    return multiplica


# Má prática.
# funcao = lambda parametro: parametro

# exemplo de como executar a função soma com lambda
# print(executa(lambda x, y: x + y, 2, 3))
# é a mesma coisa de executar o código abaixo
# print(soma(2, 3))

duplica = cria_multiplicador(2)
# é possível fazer a função multiplica da forma abaixo
# IMPORTANTE: caso a legibilidade esteja sendo muito
# afetada, crie uma função nomeada para facilitar o
# entendimento.
duplica = executa(lambda m: lambda n: n * m, 2)

print(executa(lambda *args: sum(args), 1, 2, 3, 4, 5, 6, 7))
