from functools import partial, reduce
from types import GeneratorType


def separar_exercicio():
    print()
    print('=======================================')
    print()


# Exercício 1 — MAP
# produtos = [
#     {'produto': 'Produto 1', 'preco': 10.00},
#     {'produto': 'Produto 2', 'preco': 127.10},
#     {'produto': 'Produto 3', 'preco': 25.90},
#     {'produto': 'Produto 4', 'preco': 47.50},
#     {'produto': 'Produto 5', 'preco': 34.20},
# ]


# def aplicar_desconto(produto):
#     return {**produto, 'preco': produto['preco'] * 0.9}


# produtos_com_desconto = list(map(aplicar_desconto, produtos))

# for produto in produtos_com_desconto:
#     print(f'Produto: {produto["produto"]}')
#     print(f'Novo Preço: {produto["preco"]:.2f}')
#     print('=========================================')

# separar_exercicio()

# Exercício 2 — FILTER
# pessoas = [
#     {'nome': 'Matheus', 'idade': 27},
#     {'nome': 'Mariah Anna', 'idade': 24},
#     {'nome': 'Marcus', 'idade': 15},
#     {'nome': 'Arthur', 'idade': 13},
#     {'nome': 'Jade', 'idade': 38},
# ]


# def apenas_maiores_de_idade(pessoa):
#     return pessoa['idade'] > 17


# maiores_de_idade = list(filter(apenas_maiores_de_idade, pessoas))

# print('As pessoas abaixos são maiores de idade:')
# for pessoa in maiores_de_idade:
#     print(f'Nome: {pessoa["nome"]}')

# separar_exercicio()

# Exercício 3 - reduce
# lista_palavras = ["Marih", "Umbra", "Filhos", "SoJ", "SP"]

# total_caracteres = reduce(lambda tc, p: tc + len(p), lista_palavras, 0)

# print(total_caracteres)

# separar_exercicio()

# Exercício 4 - recursividade

# lista_numerica = [1, 2, 3]


# def soma_recursiva(lista):
#     if not lista:
#         return 0
#     return lista[0] + soma_recursiva(lista[1:])


# resultado = soma_recursiva(lista_numerica)
# print(resultado)
"""
Lembrete importante sobre a recursividade caso esqueça!
A recursividade se resolve da base para fora! Pegando o exemplo
acima, começando da primeira chamada da função, seria assim:
return 1 + soma_recursiva([2, 3])
        └── depende de:
            return 2 + soma_recursiva([3])
                    └── depende de:
                        return 3 + soma_recursiva([])
                                └── depende de:
                                    return 0
quando a função retornar o 0, ela vai repassar esse valor para a execução
anterior que irá finalizar a execução e repassar para a anterior e assim
por diante até que todas sejam finalizadas. Algo como:
1 + ?
2 + ?
3 + ?
quando retorna o zero ele faz o caminho inverso:
3 + 0 -> 3
         |
         V
     2 + 3 - > 5
               |
               V
           1 + 5 -> 6
"""
# separar_exercicio()


# Exercício 5 - partial
# numeros = [1, 2, 3]


# def multiplicar(a, b):
#     return a * b


# multiplicar_por_dois = partial(multiplicar, b=2)
# multiplicar_por_tres = partial(multiplicar, b=3)

# numeros_vezes_dois = list(map(multiplicar_por_dois, numeros))
# numeros_vezes_tres = list(map(multiplicar_por_tres, numeros))

# print('Lista de números múltiplicadas por dois(2):')
# for numero in numeros_vezes_dois:
#     print(numero)
# separar_exercicio()
# print('Lista de números múltiplicadas por três(3):')
# for numero in numeros_vezes_tres:
#     print(numero)
# separar_exercicio()

# Exercício 6 - map + filter
# nomes = ["Ana", "Paulo", "Beatriz", "João", "Amanda"]


# def checar_inicias_com_a(nome):
#     # return nome[0] == 'A'
#     # evita exceção caso tenha string vazia
#     return nome.startswith('A')


# def transformar_em_letra_minuscula(nome):
#     return nome.lower()


# nomes_com_inicial_a = filter(checar_inicias_com_a, nomes)
# nomes_com_inicial_a = list(
#     map(transformar_em_letra_minuscula, nomes_com_inicial_a)
# )

# for nome in nomes_com_inicial_a:
#     print(nome)
# separar_exercicio()


# Exercício 7 - Generator
# def gerador_de_passos():
#     contador = 1
#     while contador <= 5:
#         yield contador
#         contador += 1


# for passo in gerador_de_passos():
#     print(passo)
# separar_exercicio()

# Exercício 8 - reduce + partial
# numeros = [1, 2, 3]


# def multiplicar(a, b):
#     return a * b


# # multiplicar_por_dois = partial(multiplicar, b=2) # desnecessário

# numeros_multiplicados_por_dois = reduce(multiplicar, numeros, 2)

# print(numeros_multiplicados_por_dois)
# separar_exercicio()
"""
O exercício 8 era um teste pra ver se conseguiria identificar a
falta de necessidade do partial no código ao analisar o enunciado.
Basicamente para forçar a questionar o uso do partial.
"""

# # Exercício 9 - recursividade
# palavra = "Marih Anna"


# def contar_letra_na_palavra(palavra, letra):
#     if not palavra:
#         return  # return vazio no generator finaliza a recursão
#     if palavra[0] == letra:
#         # gera um valor caso a letra bater
#         yield 1
#     else:
#         # caso contrário não gera nada
#         yield 0
#     # com esse yield from ele reinicia a recursão até que não sobre
#     # letras na palavra
#     yield from contar_letra_na_palavra(palavra[1:], letra)


# # soma cada valor gerado e retorna o total
# resultado = sum(contar_letra_na_palavra(palavra.lower(), 'a'))
# print(resultado)
# separar_exercicio()

# Exercício 10 - filter + generator
numeros_inteiros = [-1, 10, 22, 7, -13, -8]


def remover_negativos(numero):
    return numero >= 0


apenas_positivos = list(filter(remover_negativos, numeros_inteiros))


def gerar_numeros_pares(numeros):
    if not numeros:
        return
    if numeros[0] % 2 == 0:
        yield numeros[0]
    yield from gerar_numeros_pares(numeros[1:])


numeros_pares = list(gerar_numeros_pares(apenas_positivos))

for numero in numeros_pares:
    print(numero)


"""
Recursão vs Generator vs filter/map (regra prática)

Guarda isso como regra mental:

filter/map → transformar ou filtrar coleções simples

generator → fluxo sob demanda, grandes volumes, pipelines

recursão → estrutura naturalmente recursiva (árvore, divisão de problema)

lambda → detalhe pequeno, local, descartável
"""
