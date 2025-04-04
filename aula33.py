"""
for/in
Observação: é preferível utilizar o laço while quando não sabemos quantas repetições terá o laço. Já o for/in é utilizado quando é
possível saber exatamente quando o laço irá terminar.
"""
texto = 'Python'

novo_text = ''
for letra in texto:
    novo_text += f'*{letra}'
    print(letra)
print(novo_text + '*')
