"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f - casas decimais desejadas
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0 > -100, .1f
Conversion flags - !r !s !a
"""
variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: >10}') #Insere um padding com o tamanho solicitado
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.') #No caso do centro ele tenta sempre ajustar ao centro da linha
print(f'{1000.4836464412315:+,.1f}') # O sinal de positivo faz com que o python mostre na tela o + quando o número for positivo
                                     # da mesma forma que acontece quando é mostrado um número negativo
print(f'O hexadecimal de 1500 é {1500:08X}')