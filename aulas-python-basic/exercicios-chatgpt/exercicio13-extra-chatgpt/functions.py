import os

student_list = []


def register_student():
    name = input('Informe o nome do aluno: ')
    while True:
        try:
            grade = float(input('Informe a nota do aluno: '))
            break
        except ValueError:
            print('A nota deve ser um número válido.')
    student = {'nome': name, 'nota': grade}
    student_list.append(student)


def list_students():
    for student in student_list:
        print(f"nome: {student['nome']} ")
        print(f"nota: {student['nota']} ")


def class_average():
    count = 0
    total = 0
    for student in student_list:
        total += student['nota']
        count += 1
    if count == 0:
        raise ZeroDivisionError(
            'Informe ao menos um aluno antes de calcular a média da turma.'
        )
    result = total / count
    print(f'A média da turma é {result}!')


def remove_student():
    found = False
    repeat = True
    while not found and repeat:
        name = input('Informe o nome do aluno que deseja remover: ')
        for student in student_list:
            if student['nome'] == name:
                print(
                    "Tem certeza que deseja remover o"
                    f" aluno {student['nome']}?"
                )
                answer_remove = (
                    input(
                        "Digite Sim para remover e qualquer"
                        " outro valor para Não: "
                    )
                    .strip()
                    .lower()
                )
                if answer_remove == 'sim':
                    student_list.remove(student)
                    repeat = False
                    print('Aluno removido da turma com sucesso!')
                else:
                    print('Deseja buscar por outro aluno?')
                    answer_leave = (
                        input(
                            "Digite Sim para retornar à busca ou qualquer"
                            " outro valor para Não: "
                        )
                        .strip()
                        .lower()
                    )
                    if answer_leave == 'sim':
                        repeat = False


def clear_terminal():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
