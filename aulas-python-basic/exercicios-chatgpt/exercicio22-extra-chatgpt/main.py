from functions import (
    add_habit,
    check_habit_completed,
    list_active_habits,
    list_inactive_habits,
    disable_habit,
    pause,
    clear_terminal,
)

try:
    while True:
        print('===== Sistema de Gerenciamento de Biblioteca =====')
        print('')
        print('1. Registrar hábito')
        print('2. Marcar conclusão diária do hábito')
        print('3. Listar hábitos ativos')
        print('4. Arquivar hábito')
        print('5. Listar hábitos inativos')
        print('6. Encerrar o programa')
        print('')
        print('==============================================')
        answer = input('Digite o número da opção desejada: ')
        if answer == '1':
            clear_terminal()
            # acusa erro mas o parâmetro está sendo passado pelo decorator
            add_habit()  # type: ignore
        elif answer == '2':
            clear_terminal()
            check_habit_completed()  # type: ignore
        elif answer == '3':
            clear_terminal()
            list_active_habits()
        elif answer == '4':
            clear_terminal()
            disable_habit()  # type: ignore
        elif answer == '5':
            clear_terminal()
            list_inactive_habits()
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
