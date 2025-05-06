lista = []
# Método normal com for in
# for x in range(3):
#     for y in range(3):
#         lista.append((x, y))
# List Comprehension
# lista = [(x, y) for x in range(3) for y in range(3)]
lista = [[(letra) for letra in 'Matheus'] for x in range(3)]
print(lista)
