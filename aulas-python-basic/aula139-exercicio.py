"""
Exercício - Lista de tarefas com opções de desfazer e refazer
Crie uma lista com um input para o usuário digitar comandos ou tarefas
Comandos exigidos:
    - Listar
    - Desfazer
    - Refazer
Comando opcional:
    - Limpar
Caso o input do usuário não esteja entre os comandos, será salvo na lista
de tarefas.
"""

import os

lista_tarefas = []
lista_desfazer = []
lista_comandos = ['listar', 'desfazer', 'refazer', 'limpar', 'sair']
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
    else:
        ultimo_item = lista_tarefas.pop()
        lista_desfazer.append(ultimo_item)
        print('Última ação desfeita.')
        print('--------------------------------------------------------')


def refazer_tarefa():
    if not lista_desfazer:
        print('Nenhuma ação para refazer.')
        print('--------------------------------------------------------')
    else:
        ultimo_item = lista_desfazer.pop()
        lista_tarefas.append(ultimo_item)
        print('Ação refeita.')
        print('--------------------------------------------------------')


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
    print()
    print('--------------------------------------------------------')

    if resposta_usuario in lista_comandos:
        resposta_usuario = resposta_usuario
        if resposta_usuario == 'listar':
            listar_tarefas(lista_tarefas)

        elif resposta_usuario == 'desfazer':
            desfazer_tarefa()

        elif resposta_usuario == 'refazer':
            refazer_tarefa()

        elif resposta_usuario == 'sair':
            break

        else:
            os.system('cls' if os.name == 'nt' else 'clear')

    else:
        lista_tarefas.append(resposta_usuario.capitalize())
print('Programa finalizado. Até a próxima!')
