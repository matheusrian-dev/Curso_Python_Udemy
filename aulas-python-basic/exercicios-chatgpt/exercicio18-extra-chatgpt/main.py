from functions import (
    add_user,
    remove_user,
    list_users,
    search_user,
    clear_terminal,
    pause,
    set_name,
)

try:
    while True:
        print('===== Sistema para Cadastro de Contatos =====')
        print('')
        print('1. Adicionar usuário')
        print('2. Listar usuários')
        print('3. Buscar usuário por nome')
        print('4. Remover usuário')
        print('5. Encerrar o Programa')
        print('')
        print('==============================================')
        answer = input('Digite o número da opção desejada: ')
        requires_name = ['1', '3', '4']
        name = ''
        if answer in requires_name:
            name = set_name()
        if answer == '1':
            clear_terminal()
            add_user(name)
        elif answer == '2':
            clear_terminal()
            list_users()
        elif answer == '3':
            clear_terminal()
            try:
                search_user(name)
            except ValueError as e_value:
                print(e_value)
            except IndexError as e_index:
                print(e_index)
        elif answer == '4':
            clear_terminal()
            name = set_name()
            remove_user(name)
        elif answer == '5':
            clear_terminal()
            print('Programa encerrado, até a próxima!')
            break
        else:
            print('Opção inválida, tente novamente.')
            pause()
            continue
except Exception as ex:
    print(f'Ocorreu um erro inesperado: {ex}')
