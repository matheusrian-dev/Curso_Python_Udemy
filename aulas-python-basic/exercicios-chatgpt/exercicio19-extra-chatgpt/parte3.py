from itertools import zip_longest


# Exercício 7 — Criar uma função “zipper invertida”
def zipper_full(lista_a, lista_b):
    if len(lista_a) == len(lista_b):
        return list(zip(lista_a, lista_b))
    filler = preencher_filler()
    return list(zip_longest(lista_a, lista_b, fillvalue=filler))


def preencher_filler():
    print('Gostaria de inserir um valor customizado para campos vazios?')
    resposta = input('Digite Sim para inserir: ').strip().lower()
    if resposta in {'sim', 's', 'yes', 'y'}:
        filler = input(
            'Informe qual o valor que gostaria que '
            'fosse utilizado para preencher campos vazios: '
        )
        return filler
    return None


lista_1 = [10, 20, 30, 40]
lista_2 = [1, 2, 3, 4]
lista_3 = ['Matheus', 'Beatriz', 'Mariana']
lista_4 = ['Rian', 'Silva']

resultado1 = zipper_full(lista_1, lista_2)
print(resultado1)
print()

resultado2 = zipper_full(lista_3, lista_4)
print(resultado2)
