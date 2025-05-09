# Yield from


def gen1():
    print('Início Gen1')
    yield 1
    yield 2
    yield 3
    print('Fim Gen1')


def gen3():
    print('Início Gen3')
    yield 10
    yield 20
    yield 30
    print('Fim Gen3')


# 'yield from' permite que uma função generator "repasse" os valores
# de outro generator ou iterable, como se fossem seus.
def gen2(gen=None):
    print('Início Gen2')
    if gen is not None:
        yield from gen()
    yield 4
    yield 5
    yield 6
    print('Fim Gen2')


g1 = gen2(gen1)
g2 = gen2(gen3)
g3 = gen2()
for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)
print()
