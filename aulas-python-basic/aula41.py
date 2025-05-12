"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

# nome = 'Matheus'
# nome[1] = 'D' # retorna erro por ser imutável
# outro_nome = nome
# nome = 'João'
# print(nome)
# print(outro_nome)
lista_a = ['Luiz', 'Maria']
lista_b = lista_a

lista_a[0] = 'Karen'
# Como a lista é um objeto mutável, mesmo que a alteração seja feita
# após atribuir a lista A para a B, o valor da B
# exibido também é alterado, já que ela aponta para o mesmo lugar na memória
# em ambas as listas. A lista não está
# gravando o valor e sim o 'endereço' do valor, logo se o endereço se mantém o
# mesmo mas o valor muda, será exibido o novo valor.

# Caso queira criar duas listas inicialmente iguais mas que
# serão tratas de forma diferente, utilize o método list.copy()
lista_b = lista_a.copy()
lista_a.append('Gustavo')
print(lista_b)
