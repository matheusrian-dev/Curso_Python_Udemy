"""
Sistema de Controle de Estoque Simplificado

Contexto:
Você foi contratado para ajudar uma pequena loja que
ainda usa planilhas manuais.
O dono quer um script simples em Python puro
(sem banco de dados nem bibliotecas externas)
para cadastrar, consultar e atualizar produtos no estoque.

🎯 Objetivos

Implementar um sistema que:

Permita cadastrar produtos com nome, quantidade e preço.

Permita consultar produtos cadastrados.

Permita atualizar a quantidade de um produto existente.

Permita remover um produto do estoque.

Armazene as informações em um dicionário, onde a chave é o nome do produto.
"""

product = {}
stay_on = True


def register_product():
    try:
        name = input('Informe o nome do produto: ').lower().strip()
        quantity = int(
            input('Informe a quantidade atual do produto: ').strip()
        )
        price = float(input('Informe o preço do produto: ').strip())
        product[name] = {'quantidade': quantity, 'preço': price}

        print(f'O produto {name} foi cadastrado com sucesso!')
    except ValueError as ex_value:
        print('Um dos valores inseridos são inválidos.')
        print(ex_value)
    except Exception as ex:
        print('Ocorreu um erro inesperado:')
        print(ex)


def consult_product():
    try:
        name = (
            input('Informe o nome do produto que deseja consultar: ')
            .lower()
            .strip()
        )
        print(product[name])
    except KeyError:
        print('Nome do produto inexistente.')
    except Exception as ex:
        print('Ocorreu um erro inesperado:')
        print(ex)


def update_product():
    try:
        name = (
            input(
                'Informe o nome do produto que deseja atualizar a quantidade: '
            )
            .lower()
            .strip()
        )
        quantity = int(
            input('Informe a quantidade atual do produto: ').strip()
        )
        product[name] = {'quantidade': quantity}
        print(f'A quantidade do produto {name} foi atualizada com sucesso!')
    except KeyError:
        print('Produto inexistente no sistema.')
    except ValueError as ex_value:
        print('Um dos valores inseridos são inválidos.')
        print(ex_value)
    except Exception as ex:
        print('Ocorreu um erro inesperado:')
        print(ex)


def delete_product():
    try:
        name = (
            input('Informe o nome do produto que deseja excluir: ')
            .lower()
            .strip()
        )
        del product[name]
        print(f'O produto {name} foi removido com sucesso!')
    except KeyError:
        print('Produto inexistente no sistema.')
    except Exception as ex:
        print('Ocorreu um erro inesperado:')
        print(ex)


def leave_program():
    try:
        answer = input(
            'Deseja finalizar o programa? Digite Sim para finalizar '
            + 'ou qualquer outro valor para continuar: '
        )
        if answer.lower().strip() == 'sim':
            return False
        return True
    except Exception as ex:
        print('Ocorreu um erro inesperado:')
        print(ex)


def select_option(answer):
    try:
        options = ['1', '2', '3', '4', '5']
        if answer in options:
            return answer
        else:
            return 0
    except Exception as ex:
        print('Ocorreu um erro inesperado:')
        print(ex)


def main_menu():
    try:
        answer = 0
        print('----- Bem Vindo ao Sistema de Gerenciamento de Produtos -----')
        print('1. Cadastrar Produto')
        print('2. Consultar Produto')
        print('3. Atualizar Quantidade do Produto')
        print('4. Excluir Produto')
        print('5. Encerrar Sessão')
        print('-------------------------------------------------------------')
        answer = input('Digite o número da ação desejada: ')
        select_option(answer.strip())
        return answer
    except Exception as ex:
        print('Ocorreu um erro inesperado:')
        print(ex)


while stay_on:
    try:
        answer = main_menu()
        if answer == '1':
            register_product()
        elif answer == '2':
            consult_product()
        elif answer == '3':
            update_product()
        elif answer == '4':
            delete_product()
        elif answer == '5':
            stay_on = leave_program()
        else:
            print('Insira uma ação válida.')
    except Exception as ex:
        print('Ocorreu um erro inesperado:')
        print(ex)

print('Programa finalizado, até a próxima!')
