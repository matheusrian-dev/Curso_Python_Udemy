from functions import (
    register_book,
    update_book,
    list_books,
    search_by_title,
    change_book_status,
    remove_book,
    clear_terminal,
    pause,
)

try:
    while True:
        print('===== Sistema de Gerenciamento de Biblioteca =====')
        print('')
        print('1. Registrar livro')
        print('2. Listar livros')
        print('3. Buscar livro por título')
        print('4. Alterar informações de um livro')
        print('5. Emprestar / Devolver livro')
        print('6. Remover livro')
        print('7. Encerrar o programa')
        print('')
        print('==============================================')
        answer = input('Digite o número da opção desejada: ')
        if answer == '1':
            clear_terminal()
            # acusa erro mas o parâmetro está sendo passado pelo decorator
            register_book()  # type: ignore
        elif answer == '2':
            clear_terminal()
            list_books()
        elif answer == '3':
            clear_terminal()
            search_by_title()  # type: ignore
        elif answer == '4':
            clear_terminal()
            update_book()  # type: ignore
        elif answer == '5':
            clear_terminal()
            change_book_status()  # type: ignore
        elif answer == '6':
            clear_terminal()
            remove_book()  # type: ignore
        elif answer == '7':
            clear_terminal()
            print('Programa encerrado, até a próxima!')
            break
        else:
            print('Opção inválida, tente novamente.')
            pause()
            continue
except Exception as ex:
    print(f'Ocorreu um erro inesperado: {ex}')
