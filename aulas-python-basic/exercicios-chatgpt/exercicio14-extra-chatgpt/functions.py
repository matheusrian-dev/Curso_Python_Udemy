import os

products = []
next_id = 0


def add_product():
    clear_terminal()
    name = input('Informe o nome do produto: ')
    while True:
        try:
            quantity = int(input('Informe a quantidade do produto: '))
            unit_price = float(input('Informe o preço da unidade: '))
            break
        except ValueError:
            print(
                'Você inseriu um valor inválido no campo "quantidade" ou '
                '"preço da unidade", gentileza tentar novamente.'
            )
            pause()
    global next_id
    product = {
        'id': next_id,
        'nome': name,
        'quantidade': quantity,
        'preco_unidade': unit_price,
    }
    products.append(product)
    next_id += 1
    print(f'Produto {name} cadastrado com sucesso!')
    pause()


def list_products():
    clear_terminal()
    if not products:
        print('Insira ao menos um produto antes de listar.')
        pause()
    else:
        for product in products:
            total = calculate_product_total_value(
                product['quantidade'], product['preco_unidade']
            )
            print(
                f'ID: {product['id']} | '
                f'Nome: {product['nome']} | '
                f'Quantidade: {product['quantidade']} | '
                f'Preço Unitário: R${product['preco_unidade']:.2f} | '
                f'Valor Total: {total}'
            )


def update_product():
    clear_terminal()
    list_products()
    found = False
    if products:
        try:
            id = int(input('Informe o ID do produto que deseja atualizar: '))
        except ValueError:
            print('Informe um número válido.')
            pause()
            return
        for product in products:
            if product['id'] == id:
                found = True
                while True:
                    choice = input(
                        'Digite 1 para atualizar a quantidade '
                        'ou 2 para atualizar o preço unitário do produto: '
                    )
                    try:
                        if choice == '1':
                            new_quantity = int(
                                input(
                                    'Informe a nova quantidade ' 'do produto: '
                                )
                            )
                            product['quantidade'] = new_quantity
                            print(
                                'Quantidade do produto '
                                'atualizada com sucesso!'
                            )
                            print('Voltando ao menu principal...')
                            pause()
                            break
                        elif choice == '2':
                            unit_price = float(
                                input(
                                    'Informe o novo preço da unidade do '
                                    'produto: '
                                )
                            )
                            product['preco_unidade'] = unit_price
                            print(
                                'Preço da unidade do produto '
                                'atualizado com '
                                'sucesso!'
                            )
                            print('Voltando ao menu principal...')
                            pause()
                            break
                        else:
                            print('Opção inválida, tente novamente.')
                            pause()
                    except TypeError:
                        print(
                            'Você inseriu um valor inválido para o campo '
                            'desejado, tente novamente.'
                        )
                        pause()
    if not found:
        print('Produto não encontrado.')
        pause()


def delete_product():
    list_products()
    found = False
    if products:
        try:
            id = int(input('Informe o ID do produto que deseja excluir: '))
        except ValueError:
            print('Informe um número válido.')
            pause()
            return
        for product in products:
            if product['id'] == id:
                found = True
                print(
                    'Deseja realmente excluir o ' f'produto {product['nome']}?'
                )
                answer = (
                    input(
                        'Digite sim para excluir ou '
                        'qualquer outro valor para '
                        'voltar ao menu: '
                    )
                    .strip()
                    .lower()
                )
                if answer == 'sim':
                    products.remove(product)
                    print(f'produto {product['nome']} excluído com sucesso! ')
                    print('Voltando ao menu principal...')
                    pause()
                else:
                    print('Exclusão não realizada.')
                    pause()
    if not found:
        print('Produto não encontrado.')
        pause()


def show_stock_total_value():
    list_products()
    if products:
        stock_total_value = 0
        for product in products:
            product_total_value = calculate_product_total_value(
                product['quantidade'], product['preco_unidade']
            )
            stock_total_value += product_total_value
        print(f'O valor total do estoque atual é R${stock_total_value:.2f}')
        pause()


def calculate_product_total_value(quantity, unit_price):
    return quantity * unit_price


def pause():
    input('Pressione qualquer tecla para continuar...')
    clear_terminal()


def clear_terminal():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
