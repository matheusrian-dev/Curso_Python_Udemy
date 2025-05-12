"""
Exercício - Iterando strings com while
"""

nome = input('Digite seu nome: ')

string_length = len(nome)
contador = 0
new_name = ''
while contador < string_length:
    letra = nome[contador]
    print(letra)
    contador += 1
    new_name += letra

print(f'Sua iteração foi finalizada, {new_name}.')
