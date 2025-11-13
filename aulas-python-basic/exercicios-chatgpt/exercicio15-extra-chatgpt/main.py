from functions import (
    add_contact,
    list_contacts,
    update_contact,
    delete_contact,
    pause,
    search_contact,
    clear_terminal,
)

try:
    while True:
        print('===== Sistema para Cadastro de Contatos =====')
        print('')
        print('1. Cadastrar Contato')
        print('2. Listar Contatos')
        print('3. Atualizar Contato')
        print('4. Remover Contato')
        print('5. Buscar Contato por Nome')
        print('6. Encerrar o Programa')
        print('')
        print('==============================================')
        answer = input('Digite o número da opção desejada: ')
        if answer == '1':
            add_contact()
        elif answer == '2':
            list_contacts()
        elif answer == '3':
            update_contact()
        elif answer == '4':
            delete_contact()
        elif answer == '5':
            search_contact()
        elif answer == '6':
            clear_terminal()
            print('Programa encerrado, até a próxima!')
            break
        else:
            print('Opção inválida, tente novamente.')
            pause()
            continue

except Exception as ex:
    print('Ocorreu um erro inesperado.')
    print(f'Mensagem: {ex}')
