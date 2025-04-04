frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. ' \
        'Python foi criado por Guido van Rossum.'
i = 0
apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ' '
while i < len(frase):
    letra_atual = frase[i]
    qnt_vezes_atual = frase.count(letra_atual)
    
    if letra_atual == ' ':
        i += 1
        continue
    
    if apareceu_mais_vezes < qnt_vezes_atual:
        apareceu_mais_vezes = qnt_vezes_atual
        letra_que_apareceu_mais_vezes = letra_atual
    
    print(letra_atual)
    i += 1