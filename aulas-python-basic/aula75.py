"""
Sets - Métodos e Operações Úteis

Métodos úteis:
add, update, clear, discard

Operadores úteis:
união | union - Une
intersecção & intersection - Itens presentes em ambos
diferença - Itens presentes apenas no set da esquerda
diferença simétrica ^ Itens que não estão em ambos
"""

s1 = set()
s1.add('Matheus')
s1.add(2)
s1.update(('Olá mundo', 1, 2, 3, 4))
# s1.clear()
s1.discard('Olá mundo')
s1.discard(1)
print(s1)
s1 = {1, 2, 3}
s2 = {1, 5, 4}
# union
s3 = s1 | s2
# intersection
s3 = s1 & s2
# diferença
# lembrando que mostram itens apenas no set da esquerda
s3 = s1 - s2
# diferença simétrica
s3 = s1 ^ s2
print(s3)
