# Exercícios de fixação - combinations, permutations e product
from itertools import combinations, permutations, product


def separador_exercicio():
    print()
    print('-----------------------------------------------')
    print()


"""
1. Exercício de combinations()

Dada a lista:

pessoas = ["Ana", "Bia", "Luiz", "João"]


Pergunta:
Use combinations() para gerar todos os times possíveis de 2 pessoas.
Depois conte quantos times existem no total.
"""
print('Exercício 1 - combinations()')


def gerador_times():
    pessoas = ["Ana", "Bia", "Luiz", "João"]

    times_possiveis = list(combinations(pessoas, 2))
    quantidade_times_possiveis = len(times_possiveis)

    for times in times_possiveis:
        print(times)
    print()
    print(f'Quantidade total de times possíveis: {quantidade_times_possiveis}')


gerador_times()
separador_exercicio()

"""
2. Exercício de permutations()

Dada a string:

palavra = "CAT"


Use permutations() para gerar todas as palavras possíveis
com as letras dessa palavra.

Dica: junte as tuplas em strings:

"".join(tupla)
"""
print('Exercício 2 - permutations()')


def calcular_combinacao_letras():
    palavra = "CAT"
    lista_caracteres = list(palavra)
    combinacoes_letras = permutations(lista_caracteres, 3)
    for combinacao in combinacoes_letras:
        print(combinacao)


calcular_combinacao_letras()
separador_exercicio()

"""
3. Exercício de product()

Considere:

cores = ["Vermelho", "Azul"]
tamanhos = ["P", "M", "G"]


Use product() para gerar todas as combinações
possíveis de cor + tamanho de uma camiseta.
"""
print('Exercício 3 - product()')


def especificar_camisetas():
    cores = ["Vermelho", "Azul"]
    tamanhos = ["P", "M", "G"]
    camisetas = [cores, tamanhos]
    camisetas_especificas = product(*camisetas)
    for camiseta in camisetas_especificas:
        print(camiseta)


especificar_camisetas()
