"""
while/else
"""

string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        # ao inserir o break, o else do while não será executado
        break

    print(letra)
    i += 1
else:
    print('Não foi encontrado espaços na string.')
print('Fora do while.')
