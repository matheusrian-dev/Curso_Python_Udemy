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
lista_comandos = ['listar', 'desfazer', 'refazer', 'limpar']


def listar_tarefas(lista):
    print('Tarefas:')
    for item in lista:
        print(item)


def desfazer_tarefa():
    if lista_tarefas is None:
        print('Nenhuma ação para desfazer.')
    else:
        ultimo_item = lista_tarefas.pop()
        lista_desfazer.append(ultimo_item)
        print('Última ação desfeita.')


def refazer_tarefa():
    if lista_desfazer is None:
        print('Nenhuma ação para refazer.')
    else:
        ultimo_item = lista_desfazer.pop()
        lista_tarefas.append(ultimo_item)
        print('Ação refeita.')


print('Lista de Tarefas')
print('--------------------------------------------------------')
print('Comandos aceitos:')
print(' - Listar')
print(' - Desfazer')
print(' - Refazer')
print(' - Limpar')
print('--------------------------------------------------------')
print('Insira seu comando ou tarefa:')
resposta_usuario = input()
print()
print('--------------------------------------------------------')

if resposta_usuario.lower() in lista_comandos:
    resposta_usuario = resposta_usuario.lower()
    if resposta_usuario == 'listar':
        listar_tarefas(lista_tarefas)

    elif resposta_usuario == 'desfazer':
        desfazer_tarefa()

    elif resposta_usuario == 'refazer':
        refazer_tarefa()

    else:
        os.system('cls' if os.name == 'nt' else 'clear')

else:
    lista_tarefas.append(resposta_usuario)
