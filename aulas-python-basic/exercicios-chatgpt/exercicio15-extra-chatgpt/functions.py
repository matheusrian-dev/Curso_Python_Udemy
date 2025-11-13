import json
import os
import re


def add_contact():
    name = input('Informe o nome referente ao contato: ')
    while True:
        phone_number = input(
            'Informe o número para contato (apenas dígitos, ex: 99123456789): '
        ).strip()
        if valid_phone_number(phone_number):
            break
    phone_number = format_phone_number(phone_number)
    while True:
        email = input('Informe o e-mail referente ao contato: ').strip()
        if valid_email(email):
            break
    contact = {'nome': name, 'numero': phone_number, 'email': email}

    contacts = load_contacts()

    contacts.append(contact)

    save_contacts(contacts)
    print(f'Contato {name} adicionado com sucesso!')
    pause()


def list_contacts():
    try:
        with open('contacts.json', 'r', encoding='utf-8') as archive:
            contacts = json.load(archive)
            if not contacts:
                print('Nenhum contato cadastrado.')
            pause()
    except FileNotFoundError:
        print('Arquivo de contatos não encontrado.')
        return
    except json.JSONDecodeError:
        print('Erro ao ler o arquivo de contatos.')
        return

    print('Lista de Contatos:')
    for contact in contacts:
        print(
            f"Nome: {contact['nome']} | "
            f"Número: {contact['numero']} | "
            f"E-mail: {contact['email']}"
        )
        pause()


def search_contact():
    contacts = load_contacts()
    found = False
    while not found:
        name = input('Informe o nome do contato que deseja verificar: ')
        for contact in contacts:
            if contact['nome'] == name:
                print(
                    f"Nome: {contact['nome']} | "
                    f"Número: {contact['numero']} | "
                    f"E-mail: {contact['email']}"
                )
                found = True
                pause()
    if not found:
        print('Nenhum contato encontrado com esse nome.')


def update_contact():
    found = False
    contacts = load_contacts()
    while not found:
        name = input('Informe o nome do contato que deseja atualizar: ')
        for contact in contacts:
            if contact['nome'] == name:
                found = True
                valid_option = False
                while not valid_option:
                    print('1. Alterar telefone')
                    print('2. Alterar e-mail')
                    print('3. Alterar telefone e e-mail')
                    print('4. Voltar ao menu')
                    option = input('Digite o número da opção desejada: ')
                    if option == '1':
                        while True:
                            phone_number = input(
                                'Informe o novo número (apenas dígitos): '
                            ).strip()
                            if valid_phone_number(phone_number):
                                break
                        phone_number = format_phone_number(phone_number)
                        contact['numero'] = phone_number
                        print(
                            f'O número do contato {name} foi '
                            'alterado com sucesso!'
                        )
                        pause()
                        valid_option = True
                    if option == '2':
                        while True:
                            email = input('Informe o novo e-mail: ').strip()
                            if valid_email(email):
                                break
                        contact['email'] = email
                        print(
                            f'O e-mail do contato {name} foi '
                            'alterado com sucesso!'
                        )
                        pause()
                        valid_option = True
                    if option == '3':
                        while True:
                            phone_number = input(
                                'Informe o novo número (apenas dígitos): '
                            ).strip()
                            if valid_phone_number(phone_number):
                                break
                        phone_number = format_phone_number(phone_number)
                        contact['numero'] = phone_number
                        while True:
                            email = input('Informe o novo e-mail: ').strip()
                            if valid_email(email):
                                break
                        contact['email'] = email
                        print(
                            f'Número e e-mail do contato {name} '
                            'alterados com sucesso!'
                        )
                        pause()
                        valid_option = True
                    if option == '4':
                        print('Voltando ao menu principal...')
                        valid_option = True
                        pause()
                save_contacts(contacts)
                return
    if not found:
        print('Nenhum contato encontrado com esse nome.')


def delete_contact():
    found = False
    contacts = load_contacts()
    while not found:
        name = input('Informe o nome do contato que deseja apagar: ')
        for contact in contacts:
            if contact['nome'] == name:
                found = True
                print(f'Deseja realmente apagar o contato {name}?')
                answer = (
                    input(
                        'Digite Sim para apagar e qualquer '
                        'outro valor para Não: '
                    )
                    .strip()
                    .lower()
                )
                if answer == 'sim':
                    contacts.remove(contact)
                    save_contacts(contacts)
                    print(f'Contato {name} apagado com sucesso!')
                    pause()
                else:
                    print(f'Contato {name} mantido.')
                    print('Voltando ao menu principal...')
                    pause()
    if not found:
        print('Nenhum contato encontrado com esse nome.')


def pause():
    input('Pressione qualquer tecla para continuar...')
    clear_terminal()


def valid_phone_number(phone):
    if len(phone) != 11:
        print('O número de telefone inserido é inválido. Tente novamente.')
        pause()
        return False
    elif not phone.isdigit():
        print(
            'Você inseriu valores não numéricos, '
            'insira um número de telefone válido.'
        )
        pause()
        return False
    else:
        return True


def valid_email(email):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

    if re.match(regex, email):
        return True
    else:
        print('Informe um e-mail válido.')
        pause()
        return False


def format_phone_number(phone):
    return f'({phone:2}) {phone[2]} {phone[3:]}'


def load_contacts():
    try:
        with open('contacts.json', 'r', encoding='utf-8') as archive:
            contacts = json.load(archive)
    except FileNotFoundError:
        print('Arquivo de contatos não encontrado.')
        contacts = []
    except json.JSONDecodeError:
        print('Erro ao ler o arquivo de contatos.')
        contacts = []
    return contacts


def save_contacts(contacts):
    with open('contacts.json', 'w', encoding='utf-8') as archive:
        json.dump(contacts, archive, indent=4)


def clear_terminal():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
