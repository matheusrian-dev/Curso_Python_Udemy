import os

task_list = []
task = {}
next_id = 1


def add_task():
    try:
        global next_id
        title = input('Informe o título da tarefa: ').strip()
        task = {'id': next_id, 'title': title, 'done': False}
        task_list.append(task)
        next_id += 1
    except Exception as ex:
        print('Ocorreu um erro inesperado.')
        print(ex)


def list_task():
    try:
        for task in task_list:
            done_value = 'V' if task['done'] else 'X'
            print(
                f"id: {task['id']} | "
                f"título: {task['title']} | concluído: {done_value}"
            )
    except Exception as ex:
        print('Ocorreu um erro inesperado.')
        print(ex)


def complete_task():
    try:
        id = int(input('Informe o ID da tarefa: ').strip())
    except ValueError:
        print('Valor inserido não é um ID válido.')
        return

    for task in task_list:
        if task['id'] == id:
            task['done'] = True


def remove_task():
    repeat = True
    while repeat:
        list_task()
        print('=====================================================')
        try:
            id = int(input('Informe o ID da tarefa que deseja excluir: '))
        except ValueError:
            print('Valor inserido não é um ID válido.')
            return
        found = False
        for task in task_list:
            if task['id'] == id:
                print('Tem certeza que gostaria de remover essa tarefa?')
                answer = input(
                    'Digite Sim para remover ou qualquer outro valor para Não.'
                )
                if answer.lower().strip() == 'sim':
                    for task in task_list:
                        if task['id'] == id:
                            task_list.remove(task)
                            print(
                                f'Tarefa {task['title']} removida com sucesso.'
                            )
                            break
                    found = True
                    repeat = False
            if not found:
                print('Nenhuma tarefa foi encontrada com esse ID.')


def clear_terminal():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
