import os
import json
from functools import wraps

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "personal_habits.json")


def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Função {func.__name__} iniciada.')
        result = func(*args, **kwargs)
        print('Função finalizada.')
        pause()
        return result

    return wrapper


def require_habit_name(check_duplicate=False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if 'habit_name' in kwargs:
                habit_name = kwargs['habit_name']
            else:
                if len(args) >= 1:
                    habit_name = args[0]

                elif 'habit_name' in kwargs:
                    habit_name = kwargs['habit_name']
                else:
                    while True:
                        habit_name = input('Insira o nome do hábito: ')
                        if len(habit_name) == 0:
                            print('O campo não pode estar em branco.')
                            continue
                        if check_duplicate and check_duplicated_habit_name(
                            habit_name
                        ):
                            print('Hábito já cadastrado.')
                            continue
                        break
                    kwargs['habit_name'] = habit_name

            return func(*args, **kwargs)

        return wrapper

    return decorator


def require_description(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'description' in kwargs:
            description = kwargs['description']
        else:
            while True:
                description = input('Insira a descrição do hábito: ')
                if len(description) == 0:
                    print('O campo não pode estar em branco.')
                    continue
                break
            kwargs['description'] = description

        return func(*args, **kwargs)

    return wrapper


@log_action
@require_habit_name(check_duplicate=True)
@require_description
def add_habit(habit_name, description):
    personal_habits = load_personal_habits()
    new_habit = {
        'habit_name': habit_name,
        'description': description,
        'days_completed': 0,
        'active': True,
    }
    personal_habits.append(new_habit)
    save_personal_habits(personal_habits)
    print('Hábito registrado com sucesso!')


@log_action
@require_habit_name(check_duplicate=False)
def check_habit_completed(habit_name):
    personal_habits = load_personal_habits()
    found = False
    for habit in personal_habits:
        if habit['habit_name'] == habit_name:
            habit['days_completed'] += 1
            found = True
    if not found:
        print('Hábito não encontrado.')
    save_personal_habits(personal_habits)
    print("Contador de dias concluídos atualizado com sucesso!")


@log_action
def list_active_habits():
    personal_habits = load_personal_habits()
    for habit in personal_habits:
        if habit['active']:
            print(f'Nome do hábito: {habit["habit_name"]}')
            print(f'Descrição do hábito: {habit["description"]}')
            print(f'Dias concluídos: {habit["days_completed"]}')
            print('=======================================================')


@log_action
def list_inactive_habits():
    personal_habits = load_personal_habits()
    for habit in personal_habits:
        if not habit['active']:
            print(f'Nome do hábito: {habit["habit_name"]}')
            print(f'Descrição do hábito: {habit["description"]}')
            print(f'Dias concluídos: {habit["days_completed"]}')
            print('=======================================================')


@log_action
@require_habit_name(check_duplicate=False)
def disable_habit(habit_name):
    personal_habits = load_personal_habits()
    found = False
    for habit in personal_habits:
        if habit['habit_name'] == habit_name:
            if habit['active']:
                habit['active'] = False
                found = True
                print('Hábito desativado com sucesso!')
            else:
                print('Hábito já está inativo.')
    if not found:
        print('Hábito não encontrado.')
    else:
        save_personal_habits(personal_habits)


def check_duplicated_habit_name(habit_name):
    personal_habits = load_personal_habits()
    for habit in personal_habits:
        if habit['habit_name'] == habit_name:
            return True
    return False


def save_personal_habits(personal_habits):
    with open(JSON_PATH, 'w', encoding='utf-8') as archive:
        json.dump(personal_habits, archive, indent=4)


def load_personal_habits():
    try:
        with open(JSON_PATH, 'r', encoding='utf-8') as archive:
            personal_habits = json.load(archive)
    except FileNotFoundError:
        print('Arquivo não encontrado.')
        personal_habits = []
    except json.JSONDecodeError:
        print('Erro ao ler o arquivo.')
        personal_habits = []
    return personal_habits


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    input('Pressione qualquer tecla para continuar...')
    clear_terminal()
