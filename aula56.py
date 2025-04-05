"""
Introdução às funções (def) em python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

# def Print():
#     print('Linha1')
#     print('Linha2')
#     print('Linha3')
#     print('Linha4')

def imprimir(a, b, c): # parâmetros são as variáveis que são passados no parentese da função que serão utilizados no código dentro dela
    print(a, b, c)

imprimir(1, 2, 3) # argumentos são os valores que alimentam os parâmetros da função
imprimir(3, 4, 5)

def saudacao(nome):
    print(f'Olá {nome}')
    
saudacao('Luna')