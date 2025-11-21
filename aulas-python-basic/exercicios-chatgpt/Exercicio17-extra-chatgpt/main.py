from functions import (
    add_task,
    list_tasks,
    update_task,
    remove_task,
    search_by_title,
    clear_terminal,
    pause,
)

try:
    while True:
        print('===== Sistema para Cadastro de Contatos =====')
        print('')
        print('1. Adicionar Tarefa')
        print('2. Listar Tarefa')
        print('3. Atualizar Tarefa')
        print('4. Remover Tarefa')
        print('5. Buscar Tarefa por Título')
        print('6. Encerrar o Programa')
        print('')
        print('==============================================')
        answer = input('Digite o número da opção desejada: ')
        if answer == '1':
            clear_terminal()
            add_task()
        elif answer == '2':
            clear_terminal()
            list_tasks()
        elif answer == '3':
            clear_terminal()
            update_task()
        elif answer == '4':
            clear_terminal()
            remove_task()
        elif answer == '5':
            clear_terminal()
            search_by_title()
        elif answer == '6':
            clear_terminal()
            print('Programa encerrado, até a próxima!')
            break
        else:
            print('Opção inválida, tente novamente.')
            pause()
            continue
except Exception as ex:
    print(f'Ocorreu um erro inesperado: {ex}')
