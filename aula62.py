"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-se de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

# def soma(x, y)
#   return x + y

def soma(*args): # quando for utilizar argumentos não nomeados sempre utilize *args
    print(args, type(args))
    for num in args:
        print(num)
    
soma(1, 2, 3, 4, 5, 6)