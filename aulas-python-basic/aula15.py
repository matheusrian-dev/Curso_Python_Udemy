"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
Observação: se você colocar 0 seguido de um número, ele vai completar o número
hexadecimal com 0 até a quantidade digitada.
Exemplo: print('O preço é %08X', % 1500) vai retornar 000005DC
"""

nome = 'Matheus'
preco = 1000.95897643
variavel = '%s, o preço total é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %x' % (15, 15))
