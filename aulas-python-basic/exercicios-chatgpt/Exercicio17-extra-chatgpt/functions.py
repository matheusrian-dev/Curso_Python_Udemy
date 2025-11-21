import json
import os


def add_task():
    print('Registro de Tarefa')
    title = input('Informe o título da tarefa: ').strip()
    description = input('Informe a descrição da tarefa').strip()
    priority_level = ''
    while not verify_priority_level(priority_level):
        priority_level = (
            input('Informe o nível de prioridade(baixo, médio ou alto): ')
            .strip()
            .lower()
        )

    task = {
        'titulo': title,
        'descricao': description,
        'nivel_prioridade': priority_level,
        'status': 'pendente',
    }
    tasks = load_tasks()

    tasks.append(task)

    save_tasks(tasks)
    print(f'Tarefa {title} adicionada com sucesso!')
    pause()


def list_tasks():
    tasks = load_tasks()
    print('Lista de Tarefas: ')
    for task in tasks:
        print(f'Título: {task['titulo']}')
        print(f'Descrição: {task['descricao']}')
        print(f'Prioridade: {task['nivel_prioridade']}')
        print(f'Status: {task['status']}')
        print('---------------------------------------------------')
    pause()


def update_task():
    task = search_by_title()
    tasks = load_tasks()
    task_options = ['1', '2', '3', '4']
    print('----------------------')
    while True:
        print('1. Título')
        print('2. Descrição')
        print('3. Prioridade')
        print('4. Status')
        option = print('Digite o número da opção que gostaria de alterar: ')
        if option in task_options:
            if option == '1':
                clear_terminal()
                update_title(task, tasks)
            if option == '2':
                clear_terminal()
                update_description(task, tasks)
            if option == '3':
                clear_terminal()
                update_priority(task, tasks)
            if option == '4':
                clear_terminal()
                update_status(task, tasks)
        else:
            print('Digite uma opção válida.')
            pause()
        print('Gostaria de voltar ao menu principal?')
        leave = (
            input(
                'Digite Sim para voltar e qualquer outro valor para '
                'atualizar outra informação da tarefa: '
            )
            .strip()
            .lower()
        )
        if leave == 'sim':
            print('Voltando ao menu principal.')
            pause()
            break


def remove_task():
    while True:
        task = search_by_title()
        tasks = load_tasks()
        answer = (
            input(
                'Quer mesmo apagar essa tarefa? Digite Sim para apagar e '
                'qualquer outro valor pra não: '
            )
            .strip()
            .lower()
        )
        if answer == 'sim':
            tasks.remove(task)
            save_tasks(tasks)
            print('Tarefa apagada com sucesso!')
            pause()
        leave = (
            input(
                'Gostaria de procurar outra tarefa? Digite Sim para apagar e '
                'qualquer outro valor pra não: '
            )
            .strip()
            .lower()
        )
        if leave == 'sim':
            print('Voltando ao menu principal.')
            pause()
            break


def update_title(task, tasks):
    while True:
        new_title = input('Informe o novo título da tarefa: ').strip()
        if verify_title(new_title):
            print(
                'Já existe uma tarefa com esse título. '
                'Gentileza inserir um novo.'
            )
        else:
            task['titulo'] = new_title
            save_tasks(tasks)
            print('Título da tarefa atualizado com sucesso!')
            break


def update_description(task, tasks):
    new_description = input('Informe a nova descrição da tarefa: ').strip()
    task['descricao'] = new_description
    save_tasks(tasks)
    print('Descrição da tarefa atualizado com sucesso!')


def update_priority(task, tasks):
    while True:
        new_priority = input(
            'Informe o novo nível de prioridade da '
            'tarefa(baixo, médio, alto): '
        ).strip()
        if verify_priority_level(new_priority):
            task['nivel_prioridade'] = new_priority
            save_tasks(tasks)
            print('Nível de prioridade da tarefa atualizado com sucesso!')
            break
        else:
            print('Nível de prioridade inválido, tente novamente.')


def update_status(task, tasks):
    if task['status'] == 'pendente':
        task['status'] = 'concluída'
        save_tasks(tasks)
        print('Tarefa marcada como concluída!')
    else:
        task['status'] = 'pendente'
        save_tasks(tasks)
        print('Tarefa marcada como pendente!')


def search_by_title():
    tasks = load_tasks()
    found = False
    while not found:
        title = input('Informe o título da tarefa desejada: ').strip()
        for task in tasks:
            if task['titulo'] == title:
                print(f'Título: {task['titulo']}')
                print(f'Descrição: {task['descricao']}')
                print(f'Prioridade: {task['nivel_prioridade']}')
                print(f'Status: {task['status']}')
                print(
                    '---------------------------------------------------------'
                )
                found = True
                return task
    if not found:
        print('Nenhuma tarefa encontrada com esse título.')


def verify_title(title):
    tasks = load_tasks()
    for task in tasks:
        if task['titulo'] == title:
            return True
    return False


def verify_priority_level(priority_level):
    priorities = ['baixo', 'medio', 'médio', 'alto']
    if priority_level in priorities:
        return True
    else:
        print('Informe um nível de prioridade válido.')
        return False


def load_tasks():
    try:
        with open('tasks.json', 'r', encoding='utf-8') as archive:
            tasks = json.load(archive)
    except FileNotFoundError:
        print('Arquivo de contatos não encontrado.')
        tasks = []
    except json.JSONDecodeError:
        print('Erro ao ler o arquivo de contatos.')
        tasks = []
    return tasks


def save_tasks(tasks):
    with open('tasks.json', 'w', encoding='utf-8') as archive:
        json.dump(tasks, archive, indent=4)


def clear_terminal():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')


def pause():
    input('Pressione qualquer tecla para continuar...')
    clear_terminal()
