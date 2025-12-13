"""
Funções recursivas e recursividade
- funções que podem se chamar de volta
- úteis para dividir problemas grande sem partes menores
Toda função recursiva de ve ter:
- Um problema que possa ser dividido em partes menores
- Um caso recursivo que resolve o pequeno problema
- Um caso base que para a recursão
- fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 - 120
https://brasilescola.uol.com.br/matematica/fatorial.htm
"""

import sys

# O python tem por padrão um limite de 1000 stacks
# por segurança, mas em casos específicos é possível
# aumentar esse limite com o setrecursionlimit
sys.setrecursionlimit(1004)


# Lembre-se que em funções recursivas, a cada invocação
# da mesma, todo o escopo é salvo em uma stack, então
# se o código for muito robusto pode causar um problema
# de desempenho. Tente deixá-la o mais objetiva possível.
def recursiva(contador=0, fim=4):
    print(contador, fim)

    # Caso base
    if contador >= fim:
        return fim

    # Caso recursivo
    # Contar até chegar ao final
    contador += 1
    # no fim da execução, se o caso base
    # não tiver sido resolvido, a função
    # recursiva retorna ela mesma até que
    # seja solucionado.
    return recursiva(contador, fim)


print(recursiva())


def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))
print(factorial(10))
print(factorial(100))
