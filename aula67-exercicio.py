"""
Exercícios
Crie Funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro.
"""
# Minha solução
def duplicar(numero):
    return numero * 2

    
def triplicar(numero):
    return numero * 3
    
def quadruplicar(numero):
    return numero * 4

try:
    numero = input('Informe um número inteiro: ')
    numero = int(numero)
    
    print(f'O dobro do número passado é {duplicar(numero)}')
    print(f'O triplo do número passado é {triplicar(numero)}')
    print(f'O quádruplo do número passado é {quadruplicar(numero)}')
    
except ValueError:
    print('O valor informado não é um número inteiro.')
    
# Solução do instrutor com closure
def criar_multiplicacao(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicacao(2)
triplicar = criar_multiplicacao(3)
quadruplicar = criar_multiplicacao(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
