import os

users = []


def log_action(func):
    def wrapper(*args, **kwargs):
        print(f'Função: {func.__name__}')
        result = func(*args, **kwargs)
        print('Execução finalizada')
        pause()
        return result

    return wrapper


def validate_string(param_name):
    def decorator(func):
        def wrapper(*args, **kwargs):

            if param_name in kwargs:
                value = kwargs[param_name]
            else:
                func_params = func.__code__.co_varnames
                index = func_params.index(param_name)
                value = args[index]
            if not isinstance(value, str):
                raise TypeError('Valor passado não é um texto válido.')

            return func(*args, **kwargs)

        return wrapper

    return decorator


@validate_string("name")
@log_action
def add_user(name):
    if not check_duplicates(name):
        user = {'nome': name}
        users.append(user)
        print(f'Usuário {name} cadastrado com sucesso!')
    else:
        print('Usuário já cadastrado no sistema.')


@log_action
def list_users():
    if not check_empty_list():
        for user in users:
            print(f"Usuário: {user['nome']}")
        print('----------------------------------------')
    else:
        print('Não há usuários cadastrados.')


@validate_string("name")
@log_action
def search_user(name):
    found = False
    for user in users:
        if user['nome'] == name:
            print(f'Usuário {name} está cadastrado no sistema.')
            found = True

    if not found:
        print(f'Usuário {name} não está cadastrado no sistema.')


@validate_string("name")
@log_action
def remove_user(name):
    found = False
    for user in users:
        if user['nome'] == name:
            found = True
            answer = (
                input(
                    'Tem certeza que quer remover esse usuário? '
                    'Digite Sim para remover: '
                )
                .strip()
                .lower()
            )
            if answer == 'sim':
                users.remove(user)
                print(f'Usuário {name} removido com sucesso!')

            else:
                print('Digitou um valor diferente de Sim, usuário mantido.')

    if not found:
        print(f'Usuário {name} não está cadastrado no sistema.')


def set_name():
    while True:
        name = input('Insira o nome do usuário: ').strip().lower()
        if len(name) >= 1:
            return name
        else:
            print('Insira ao menos um caractere.')
            pause()


def check_duplicates(name):
    for user in users:
        if user['nome'] == name:
            return True
    return False


def check_empty_list():
    if not users:
        return True
    return False


def clear_terminal():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')


def pause():
    input('Pressione qualquer tecla para continuar...')
    clear_terminal()
