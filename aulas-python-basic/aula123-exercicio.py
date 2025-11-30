"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

from itertools import zip_longest

list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [1, 2, 3, 4]


# Solução crua
# def sum_lists(list1, list2):
#     minor_list_range = min(len(list1), len(list2))
#     return [list1[i] + list2[i] for i in range(minor_list_range)]


# print(sum_lists(list_a, list_b))

# Solução mais limpa
sum_list = [x + y for x, y in zip(list_a, list_b)]
print(f'Lista com zip(): {sum_list}')

# Também é possível utilizar o zip_longest pra incluir os valores
# que não tem um valor direto para serem somados:
sum_list = [x + y for x, y in zip_longest(list_a, list_b, fillvalue=0)]
print(f'Lista com zip_longest(): {sum_list}')
