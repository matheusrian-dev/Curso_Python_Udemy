import os

"""
os.remove, os.unlink e os.rename

# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
"""

caminho_arquivo = '.\\aulas-python-basic\\aula133\\aula133.txt'

with open(caminho_arquivo, 'w+', encoding='utf-8') as arquivo:
    print(type(arquivo))
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(('Linha 3\n', 'Atenção\n'))

# os.remove(caminho_arquivo)
# os.unlink(caminho_arquivo)
os.rename(caminho_arquivo, '.\\aulas-python-basic\\aula133\\aula136.txt')
