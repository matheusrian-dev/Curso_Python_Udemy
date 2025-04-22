"""
Exemplo de uso dos sets
"""

# poupa espaço por não permitir duplicadas
letras = set()
while True:
    letra = input('Digite uma letra: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('Parabéns! Encontrou a letra secreta!')
        break
    print(letras)
