"""
Criando arquivos com Python + Context Manager with
with open (context manager) e métodos úteis do TextIOWrapper
Usamos a função open para abrir um arquivo em Python
(ele pode existir ou não existir)
Modos:
# r ( leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo text), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis:
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
arquivo - open(caminho_arquivo, 'w')
#
arquivo.close()
"""

caminho_arquivo = '.\\aulas-python-basic\\aula133\\aula133.txt'

with open(caminho_arquivo, 'w+') as arquivo:
    print(type(arquivo))
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(('Linha 3\n', 'Linha 4\n'))

    arquivo.seek(0, 0)
    print(arquivo.read())
    print('Lendo')
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())

    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())

print('#' * 10)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())

"""
w(escrita) vs a(escrita ao final):
Ambos podem ser utilizados também para criar o arquivo,
porém contam com uma diferença importante:
O w abre o arquivo, apaga todo o conteúdo já existente
e escreve o que foi solicitado. O a apenas adiciona
o novo conteúdo no final do existente.
"""
