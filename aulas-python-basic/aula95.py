# Introdução às Generator functions em Python
# generator = (n for n in range(10000))


# def generator(n=0):
#     # yield pausa a execução da função
#     # e quando é chamado o next() ele
#     # retorna o valor passado
#     yield 1  # Pausa
#     print('Continuando pós pausa...')
#     yield 2  # Pausa
#     print('Continuando pós pausa...')
#     yield 3  # Pausa
#     print('Finalizado.')


def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator(n=0)
# print(next(gen))
# # retorna StopIteration se não houver outras implementações de
# # yield dentro da função.
# print(next(gen))

# forma correta padrão
for n in gen:
    print(n)
