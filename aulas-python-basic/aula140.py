"""
Evitando uso de condicionais + Guard Clause

É recomendado reduzir a quantidade de condicionais como o if
no código sempre que possível para manter o código mais legível.
Pegamos abaixo o exercício da aula anterior para utilizar de exemplo
de como poderia substituí-los.
"""

import os

lista_tarefas = []
lista_desfazer = []
repeat = True


def listar_tarefas(lista):
    print('Tarefas:')
    for item in lista:
        print(item)
    print('--------------------------------------------------------')


def desfazer_tarefa():
    if not lista_tarefas:
        print('Nenhuma ação para desfazer.')
        print('--------------------------------------------------------')
        return
    ultimo_item = lista_tarefas.pop()
    lista_desfazer.append(ultimo_item)
    print('Última ação desfeita.')
    print('--------------------------------------------------------')


def refazer_tarefa():
    if not lista_desfazer:
        print('Nenhuma ação para refazer.')
        print('--------------------------------------------------------')
        return
    ultimo_item = lista_desfazer.pop()
    lista_tarefas.append(ultimo_item)
    print('Ação refeita.')
    print('--------------------------------------------------------')


def adicionar_tarefa(tarefa):
    lista_tarefas.append(tarefa)
    print(f'Tarefa {tarefa} adicionada à lista.')


while True:
    print('Lista de Tarefas')
    print('--------------------------------------------------------')
    print('Comandos aceitos:')
    print(' - Listar')
    print(' - Desfazer')
    print(' - Refazer')
    print(' - Limpar')
    print(' - Sair')
    print('--------------------------------------------------------')
    print('Insira seu comando ou tarefa:')
    resposta_usuario = input().strip().lower()
    if not resposta_usuario:
        print('Digite alguma coisa antes de pressionar ENTER.')
        print()
        continue
    if resposta_usuario == 'sair':
        break
    print()
    print('--------------------------------------------------------')
    comandos = {
        'listar': lambda: listar_tarefas(lista_tarefas),
        'desfazer': lambda: desfazer_tarefa(),
        'refazer': lambda: refazer_tarefa(),
        'limpar': lambda: os.system('cls' if os.name == 'nt' else 'clear'),
        'adicionar': lambda: adicionar_tarefa(resposta_usuario.capitalize()),
    }
    comando = comandos.get(resposta_usuario, comandos['adicionar'])
    comando()


print('Programa finalizado. Até a próxima!')
