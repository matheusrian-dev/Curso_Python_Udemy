'''
Operadores in e not in
Strings são iteráveis
 0  1  2  3  4  5  6
 M  a  t  h  e  u  s
-7 -6 -5 -4 -3 -2 -1
'''

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')
# print(nome[1])
# print(nome[-6])
# print('M' in nome)
# print('v' in nome)
# print('Mat' in nome)
# print('amt' not in nome)
if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
