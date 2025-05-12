"""
Retorno de valores das funções (return)
"""

# Ele vai executar a ação dentro da função,
# porém o retorno (return) da função print() é nulo (None)
# variavel = print('Luiz')

# Logo o valor da variável continuará sendo nulo (None)
# print(variavel)

# Validação comprovando o comentário acima
# print(variavel is None)


# Agora ao inserir um retorno na função,
# o valor retornado é passado para a variável abaixo
def soma(x, y):
    if x > 10:
        return 10
    return x + y


variavel = soma(1, 2)
# Logo, a variável já passa a ter um valor.
print(variavel)
