"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-se de desempacotamento
x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma(x, y)
#   return x + y

def soma(*args): # quando for utilizar argumentos não nomeados sempre utilize *args
    total = 0
    # print(args, type(args))
    for num in args: # caso não for desempacotado, vai retornar um erro alegando que o tipo tuple não suporta a operação abaixo (+=)
        total += num
    # print(total)
    return total

numeros = 1, 2, 3, 4, 5, 6
print(soma(*numeros)) # quando for passar uma tupla como argumento, lembre-se de desempacotá-la (*) para que não haja problemas na função, veja na linha 15

print(sum(numeros)) 