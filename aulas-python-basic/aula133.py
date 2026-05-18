# Criação de Arquivos com Python e Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
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

# Observação: Sempre que precisar inserir o caminho absoluto de um arquivo
# em um sistema operacional Windows, que utiliza barra invertida, insira
# uma barra extra para evitar erros!
# caminho_arquivo = (
#     'C:\\Users\\m1563301\\Documents\\curso_python_1\\aulas-python-basic'
# )
caminho_arquivo = 'aula133.txt'

# arquivo = open(caminho, 'w')
# #
# arquivo.close()

# Lembre-se de sempre fechar qualquer arquivo que seja aberto para
# realizar funções específicas! Seja com try/except ou with open
# como mostrado abaixo, onde o mesmo fecha o arquivo após executar
# a ação solicitada.
with open(caminho_arquivo, 'w') as arquivo:
    print('Olá mundo')
    print('Arquivo vai ser fechado')
