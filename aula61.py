"""
Retorno de valores das funções (return)
"""
# variavel = print('Luiz') # Ele vai executar a ação dentro da função, porém o retorno (return) da função print() é nulo (None)
# print(variavel) # Logo o valor da variável continuará sendo nulo (None)
# print(variavel is None) # Validação comprovando o comentário acima

def soma(x, y): # Agora ao inserir um retorno na função, o valor retornado é passado para a variável abaixo
    if x > 10:
        return 10
    return x + y

variavel = soma(1, 2)
print(variavel) # Logo, a variável já passa a ter um valor.