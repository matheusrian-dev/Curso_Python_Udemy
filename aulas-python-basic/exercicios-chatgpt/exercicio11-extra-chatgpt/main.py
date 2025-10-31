from functions import (
    add_task,
    list_task,
    complete_task,
    remove_task,
    clear_terminal,
)

stay_on = True
options_list = [
    '1',
    '2',
    '3',
    '4',
    '5',
]

while stay_on:
    try:
        print('===== Bem Vindo ao Sistema de Gerenciamento de Tarefas =====')
        print('1. Adicionar Tarefa')
        print('2. Listar Tarefas')
        print('3. Concluir Tarefa')
        print('4. Remover Tarefa')
        print('5. Encerrar Sessão')
        print('=============================================================')
        answer = input('Digite o número da ação desejada: ')
        if answer in options_list:
            if answer == '1':
                add_task()
            elif answer == '2':
                list_task()
            elif answer == '3':
                complete_task()
            elif answer == '4':
                remove_task()
            elif answer == '5':
                clear_terminal()
                print('Sessão encerrada, até a próxima!')
                stay_on = False
        else:
            clear_terminal()
            print('Você inseriu uma opção inválida, tente novamente.')

    except Exception as ex:
        print('Ocorreu um erro inesperado:')
        print(ex)
