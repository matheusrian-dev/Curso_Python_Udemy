"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

text = 'Luiz'  # Iterável
iterator = iter(text)  # Iterador

while True:
    try:
        letra = next(iterator)
        print(letra)
    except StopIteration:
        # Esse erro é comum e é retornado quando tenta buscar um valor acima
        # do tamanho da string.
        break
