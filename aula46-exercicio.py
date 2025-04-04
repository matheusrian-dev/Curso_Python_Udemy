"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir,
apagar e listar valores da sua lista.
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""
lista = []
repeat = True
try:
    while repeat: # Mantém o programa rodando até o usuário Digitar n ou N
        print('Selecione uma opção')
        acao = input('[i]nserir [a]pagar [l]istar: ')
        acao = acao.lower() # transforma a letra retornada em minúscula para que o usuário possa escrever em maiúsculo também sem retornar
        if acao == 'i':     # valor inválido.
            valor = input('Digite o item que gostaria de inserir na lista: ')
            lista.append(valor) # insere o valor na lista
            print(f'{valor} inserido na lista de compras.')
        elif acao == 'a':
            indice = input('Digite o índice que gostaria de apagar: ')
            try:
                indice_int = int(indice) # tenta converter o índice para int
            except ValueError: 
                print('O índice informado não é válido.')
            except IndexError: #Solução do instrutor
                print('O índice não existe na lista.')
            except:
                print('Erro desconhecido, contate o administrador.') # caso o valor passado não seja um número inteiro retornará valor inválido
            #Minha solução
            """if indice_int < len(lista) and indice_int > -len(lista): # caso o índice esteja fora do alcance da lista, retorna inválido
                del lista[indice_int] # deleta o valor no índice passado
                print(f'Índice {indice} removido da lista de compras.')
            else:
                print('O índice informado não é válido.')"""
        elif acao == 'l':
            lista_enumerada = enumerate(lista) # enumera a lista
            for indice, item in lista_enumerada: # para cada item na lista, retorna o índice e o valor
                print(indice, item)
        else:
            print('Opção inválida')
        finalizar = input('Deseja finalizar o programa? [S]im ou [N]ão: ')
        finalizar.lower() # transforma a letra retornada em minúscula para que o usuário possa escrever em maiúsculo também.
        if finalizar == 's': 
            repeat = False
    print('Programa finalizado, segue abaixo a lista de compra atual: ')
    lista_enumerada = enumerate(lista)
    for indice, item in lista_enumerada: # Após finalizar o programa, enumera e retorna o índice e o valor de cada item na lista.
                print(indice, item)
except:
    print('Erro inesperado.')