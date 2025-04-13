"""
Exercícios com funções

Crie uma função que multiplica todos os argumentos não nomeados recebidos
retorne o total para uma variável e mostre o valor da variável.

Crie uma função que fala se um número é par ou ímpar
"""


def multiplicacao(*args):
    produto = 1
    for numero in args:
        produto *= numero
    return produto


def par_ou_impar(numero):
    if numero % 2 == 0:
        return "O número {numero} é par"
    return "O número {numero} é ímpar"


numeros = 3, 3, 3, 3
numero = 6

print(multiplicacao(*numeros))
print(par_ou_impar(numero))
