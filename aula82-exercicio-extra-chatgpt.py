"""
Crie uma função chamada executar_operacao que recebe uma
função lambda como primeiro parâmetro, e um número variável
de argumentos (*args) como segundo.

A função deve executar o lambda passando os args
recebidos e retornar o resultado.
"""


def executar_operacao(funcao, *args):
    return funcao(*args)


resultado = executar_operacao(lambda x, y: x + y, 3, 5)

print(resultado)

resultado = executar_operacao(lambda *args: sum(args), 1, 2, 3, 4)
print(resultado)
