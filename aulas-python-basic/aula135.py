"""
encoding

Ao gerar o arquivo, especialmente em sistemas Windows,
é provável que a codificação de texto utilizada seja a
padrão do Windows(Windows 1252, por exemplo),
o que acaba interferindo na escrita de caracteres especiais
como ~, ç, entre outros.

Para resolver isso é necessário inserir a codificação desejada
como parâmetro ao criar o arquivo, conforme demonstrado abaixo.
"""

caminho_arquivo = '.\\aulas-python-basic\\aula133\\aula133.txt'

with open(caminho_arquivo, 'w+', encoding='utf-8') as arquivo:
    print(type(arquivo))
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(('Linha 3\n', 'Atenção\n'))
