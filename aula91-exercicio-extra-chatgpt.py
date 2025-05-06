"""
5. Formatação
Escreva uma função que recebe uma string com nomes separados por vírgula e
retorne uma lista com os nomes formatados (sem espaços antes/depois,
com primeira letra maiúscula).

entrada = "  joão, maria ,jose  "
saida = ["João", "Maria", "Jose"]
"""

# import re


# Minha solução - incompleta por que remove espaços
# de nomes compostos
# def remover_espacos(texto):
#     # Remove espaços em branco (inclusive tabulações)
#     texto_sem_espacos = re.sub(r'\s+', '', texto)
#     return texto_sem_espacos


entrada = "  joão, maria ,Ana Paula  "

# entrada = remover_espacos(entrada)

# lista_nomes = entrada.split(',')

# print(lista_nomes)

# Solução eficiente - ChatGPT
lista_nomes = [nome.strip() for nome in entrada.split(',')]
print(lista_nomes)
