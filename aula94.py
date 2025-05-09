import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__()

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# # Se chamar Iterator além do tamanho do Iterável,
# # será retornado um StopIteration por não haver mais valores
# # para buscar.
# print(next(iterator))

# Utilizando um for in esse problema não acontece já que o
# próprio método identifica onde o iterável acaba.
for item in iterable:
    print(next(iterator))

# Generator é um tipo especial de iterator que gera valores
# sob demanda, economizando memória.
# Generator vs Iterator:
# Iterator guarda tudo na memória, diferente do Generator, que
# 'pausa' e 'continua' a execução da função a cada next()

# Importante! Todo Generator é um Iterator, mas o contrário não é verdade.
# Com o generator a utilização da memória se torna gradual então a memória é
# poupada até que seja solicitada.
lista = [n for n in range(1000)]
generator = (n for n in range(1000))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

# Características de cada um:

# - Iterator:
# 1. Maior flexibilidade e robustez: pode se implementar lógicas mais complexas
# de erro como fallback, logs detalhados e etc;
# 2. Integração com bibliotecas que exigem interface formal: certas API's
# esperam uma implementação __iter__ e __next__ . Isso demanda um
# iterator tradicional;
# 3. Maior gama de métodos personalizados: é possível criar métodos auxiliares
# além da iteração como reset, reverse, peek, entre outros.

# - Generator:
# 1. Economia de memória;
# 2. Lógica de iteração simples e linear;
