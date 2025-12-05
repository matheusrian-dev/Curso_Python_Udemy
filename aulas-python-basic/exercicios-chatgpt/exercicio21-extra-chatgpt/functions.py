import os
import json
from functools import wraps

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE_DIR, "library.json")


def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Função: {func.__name__}')
        result = func(*args, **kwargs)
        print('Função executada')
        pause()
        return result

    return wrapper


def require_title_input(check_duplicate=False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # já recebeu title por kwargs?
            if 'title' in kwargs:
                title = kwargs['title']
            else:
                # recebeu por args (posicional)?
                if len(args) >= 1:
                    title = args[0]
                else:
                    # não recebeu -> pedir
                    while True:
                        title = input('Insira o título do livro: ').strip()
                        if len(title) == 0:
                            print('O campo não pode estar em branco.')
                            continue
                        if check_duplicate and check_book_registered(title):
                            print(
                                'Já tem um livro cadastrado com esse título.'
                            )
                            continue
                        break
                    # injetar no kwargs para os próximos wrappers
                    kwargs['title'] = title

            return func(*args, **kwargs)

        return wrapper

    return decorator


def require_author_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'author' in kwargs:
            author = kwargs['author']
        else:
            # se title foi passado posicionalmente, author seria args[1]
            if len(args) >= 2:
                author = args[1]
            else:
                while True:
                    author = input('Insira o autor do livro: ').strip()
                    if len(author) == 0:
                        print('O campo não pode estar em branco.')
                        continue
                    break
                kwargs['author'] = author

        return func(*args, **kwargs)

    return wrapper


def require_year_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'year' in kwargs:
            year = kwargs['year']
        else:
            # se title e author passaram por args: args[2] seria year
            if len(args) >= 3:
                year = args[2]
            else:
                while True:
                    try:
                        year_input = input(
                            'Insira o ano de publicação '
                            '(digite apenas números): '
                        ).strip()
                        year = int(year_input)
                    except ValueError:
                        print('Digite apenas números.')
                        continue
                    break
                kwargs['year'] = year

        return func(*args, **kwargs)

    return wrapper


@log_action
@require_title_input(check_duplicate=True)
@require_author_input
@require_year_input
def register_book(title, author, year):
    book = {
        'titulo': title,
        'autor': author,
        'ano': year,
        'status': 'disponivel',
    }
    library = load_library()
    library.append(book)
    save_library(library)


@log_action
@require_title_input()
def update_book(title):
    if check_book_registered(title):
        answer = update_options()
        if answer == '1':
            update_title(title)
        if answer == '2':
            update_author(title)
        if answer == '3':
            update_year(title)


@log_action
def update_title(title):
    library = load_library()
    repeat = True
    while repeat:
        new_title = input('Insira o novo título: ').strip()
        if len(new_title) > 0 and not check_book_registered(new_title):
            for book in library:
                if book['titulo'] == title:
                    book['titulo'] = new_title
                    save_library(library)
                    print(
                        f'Titulo do livro {title} alterado para {new_title} '
                        'com sucesso.'
                    )
                    repeat = False
                    break
        else:
            print('O título informado não é válido ou já está cadastrado.')
            continue


@log_action
def update_author(title):
    library = load_library()
    repeat = True
    while repeat:
        new_author = input('Insira o nome do novo autor: ').strip()
        if len(new_author) > 0:
            for book in library:
                if book['titulo'] == title:
                    book['autor'] = new_author
                    save_library(library)
                    print(f'Autor do livro {title} alterado com sucesso!')
                    repeat = False
                    break
        else:
            print('Não é possível inserir um valor vazio.')
            continue


@log_action
def update_year(title):
    library = load_library()
    repeat = True
    while repeat:
        new_year = input('Insira o novo ano de publicação: ').strip()
        if len(new_year) > 0:
            for book in library:
                if book['titulo'] == title:
                    book['ano'] = new_year
                    save_library(library)
                    print(
                        f'O ano de publicação do livro {title} '
                        'alterado com sucesso!'
                    )
                    repeat = False
                    break
        else:
            print('Não é possível inserir um valor vazio.')
            continue


def update_options():
    update_options = ['1', '2', '3']
    while True:
        print('1. Título')
        print('2. Autor')
        print('3. Ano')
        answer = input('Digite o número da informação que deseja alterar: ')
        if answer in update_options:
            if answer == '1':
                return '1'
            if answer == '2':
                return '2'
            if answer == '3':
                return '3'
        print('Insira uma opção válida.')


@log_action
def list_books():
    library = load_library()
    print('Lista de libros registrados na biblioteca: ')
    print('--------------------------------------------------------')
    for book in library:
        print(f'Título do livro: {book['titulo']}')
        print(f'Autor do livro: {book['autor']}')
        print(f'Ano de Publicação do livro: {book['ano']}')
        print(f'Status: {book['status']}')
        print('--------------------------------------------------------')


@log_action
@require_title_input()
def search_by_title(title):
    library = load_library()
    if check_book_registered(title):
        for book in library:
            if book['titulo'] == title:
                print(f'Título do livro: {book['titulo']}')
                print(f'Autor do livro: {book['autor']}')
                print(f'Ano de Publicação do livro: {book['ano']}')
                print(f'Status: {book['status']}')
                print(
                    '--------------------------------------------------------'
                )
    else:
        print('Não foi encontrado nenhum livro com esse título.')


@log_action
@require_title_input()
def change_book_status(title):
    library = load_library()
    if check_book_registered(title):
        for book in library:
            if book['titulo'] == title:
                if confirm_action():
                    if book['status'] == 'disponivel':
                        book['status'] = 'emprestado'
                        save_library(library)
                        print('Livro reservado com sucesso!')
                    else:
                        book['status'] = 'disponivel'
                        save_library(library)
                        print('Livro devolvido com sucesso!')
                else:
                    print('Alteração cancelada, retornando ao menu.')


@log_action
@require_title_input()
def remove_book(title):
    library = load_library()
    if check_book_registered(title):
        for book in library:
            if book['titulo'] == title:
                if confirm_action():
                    library.remove(book)
                    save_library(library)
                    print(f'Livro {title} removido com sucesso!')
                else:
                    print('Remoção cancelada, retornando ao menu.')


def confirm_action():
    print('Tem certeza que gostaria de realizar essa ação?')
    answer = input('Digite Sim para confirmar: ').strip().lower()
    if answer in {'sim', 's', 'yes', 'y'}:
        return True
    return False


def check_book_registered(book_title):
    library = load_library()
    for book in library:
        if book['titulo'] == book_title:
            return True
    return False


def save_library(library):
    with open(JSON_PATH, 'w', encoding='utf-8') as archive:
        json.dump(library, archive, indent=4)


def load_library():
    try:
        with open(JSON_PATH, 'r', encoding='utf-8') as archive:
            library = json.load(archive)
    except FileNotFoundError:
        print('Biblioteca não encontrada.')
        library = []
    except json.JSONDecodeError:
        print('Erro ao ler a biblioteca.')
        library = []
    return library


def clear_terminal():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')


def pause():
    input('Pressione qualquer tecla para continuar...')
    clear_terminal()
