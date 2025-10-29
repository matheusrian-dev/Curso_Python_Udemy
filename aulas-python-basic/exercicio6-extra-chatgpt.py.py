"""
2. Validador de Palíndromos
Crie uma função chamada eh_palindromo(palavra)
que retorne True se a palavra for um palíndromo
(lida igual de trás para frente) e False caso
contrário. Ignore espaços e acentuação simples.
"""

import re
import unicodedata


def remover_acentos_e_espacos(texto):
    # Remove acentos
    texto_sem_acentos = ''.join(
        c
        for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    # Remove espaços em branco (inclusive tabulações)
    texto_sem_espacos = re.sub(r'\s+', '', texto_sem_acentos)
    return texto_sem_espacos


# Minha solução
# def eh_palindromo(palavra):
#     palavra_formatada = remover_acentos_e_espacos(palavra)
#     palavra_formatada = palavra_formatada.lower()
#     tamanho_palavra = len(palavra_formatada)
#     meio_palavra = tamanho_palavra // 2
#     primeira_parte = ''
#     segunda_parte = ''
#     for letra in palavra_formatada[:meio_palavra]:
#         primeira_parte += letra
#     for letra in palavra_formatada[-1 : meio_palavra - 1 : -1]:
#         segunda_parte += letra
#     indice = 0
#     for letra in primeira_parte:
#         if letra != segunda_parte[indice]:
#             return False
#         indice += 1
#     return True


# Solução simples do ChatGPT
def eh_palindromo(palavra):
    palavra_formatada = remover_acentos_e_espacos(palavra.lower())
    return palavra_formatada == palavra_formatada[::-1]


palavra = 'saas'

resposta = eh_palindromo(palavra)

if resposta is True:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
