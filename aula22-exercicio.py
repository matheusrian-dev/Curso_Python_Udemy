"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número 
inteiro, informe que não é um número inteiro
"""
numero_str = input('Digite um número: ')
try:
    numero_int = int(numero_str) #tenta converter o valor para inteiro
    par = numero_int % 2 == 0
    if par:
        print(f'O número {numero_int} é par.')
    else:
        print(f'O número {numero_int} é ímpar.')
except:
    print('O valor digitado não é um número inteiro.') # retorna que o valor não é inteiro caso a conversão não funcione