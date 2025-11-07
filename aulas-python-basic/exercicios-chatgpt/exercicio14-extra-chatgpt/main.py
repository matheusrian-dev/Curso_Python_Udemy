from functions import (
    add_product,
    list_products,
    delete_product,
    update_product,
    clear_terminal,
    show_stock_total_value,
    pause,
)

try:
    while True:
        print('===== Sistema de Controle de Estoque =====')
        print('')
        print('1. Cadastrar Produto')
        print('2. Listar Produtos')
        print('3. Atualizar Produto')
        print('4. Remover Produto')
        print('5. Mostrar Valor Total do Estoque')
        print('6. Encerrar o Programa')
        print('')
        print('==========================================')
        answer = input('Digite o número da opção desejada: ')
        if answer == '1':
            add_product()
        elif answer == '2':
            list_products()
        elif answer == '3':
            update_product()
        elif answer == '4':
            delete_product()
        elif answer == '5':
            show_stock_total_value()
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
