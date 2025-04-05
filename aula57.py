"""
Argumentos nomeados e não nomeados em funções Python
Argumentos nomeados tem nome com sinal de igual
Argumentos não nomeados(posicionais) recebem apenas o argumento(valor)
"""

def soma (x, y):
    print(f'{x=} y={y}', '|', 'x + y = ', x + y)
    # return x + Y

soma(1,5) # executa a função 
print(soma) # não executa a função e só referencia o nome e o local na memória onde ela é armazenada
print(soma(1,2)) # executa a função e exibe o retorno, como essa função acima não retorna nada é exibido None
soma(y = 3, x = 6) # é possível nomear a variável para trocar a ordem que o argumento é utilizado dentro dos 
                   # observação: apartir do momento que você nomeia um argumento, todos os que vierem depois dele são obrigados a serem nomeados