from functions import (
    register_student,
    list_students,
    remove_student,
    class_average,
    clear_terminal,
)

options = ['1', '2', '3', '4', '5']

try:
    repeat = True
    while repeat:
        print('===== Gerenciamento de Classe =====')
        print('')
        print('1. Cadastrar aluno e nota.')
        print('2. Listar alunos cadastrados.')
        print('3. Mostrar a média geral da turma.')
        print('4. Remover um aluno específico.')
        print('5. Encerrar o programa.')
        print('')
        print('===================================')
        answer = input('Informe a opção desejada: ')
        if answer not in options:
            clear_terminal()
            print('Opção inválida, tente novamente.')
            continue
        if answer == '1':
            clear_terminal()
            register_student()
        if answer == '2':
            clear_terminal()
            list_students()
        if answer == '3':
            clear_terminal()
            class_average()
        if answer == '4':
            clear_terminal()
            remove_student()
        if answer == '5':
            clear_terminal()
            print('Deseja realmente encerrar a aplicação?')
            leave = (
                input(
                    'Digite Sim para sair e qualquer'
                    ' outro valor para voltar ao menu: '
                )
                .strip()
                .lower()
            )
            if leave == 'sim':
                repeat = False
                print('Acesso encerrado, até a próxima!')

except Exception as ex:
    print(f'Ocorreu um erro inesperado: {ex}')
