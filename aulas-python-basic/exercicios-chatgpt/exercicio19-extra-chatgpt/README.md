Exercícios para Fixação - zip() & zip_longest()
🟢 PARTE 1 — Exercícios com zip()
Exercício 1 — Unir produtos e preços

Dadas as listas:

produtos = ['Arroz', 'Feijão', 'Macarrão', 'Azeite']
precos = [25.90, 7.99, 5.49]


Crie uma lista de tuplas unindo produto e preço usando zip().

Dica: O último produto deve ser ignorado, porque zip usa a menor lista.

Exercício 2 — Criar um dicionário com zip

Com os dados:

nomes = ['Ana', 'Bruno', 'Carlos']
idades = [22, 35, 19]


Use zip() para criar um dicionário assim:

{'Ana': 22, 'Bruno': 35, 'Carlos': 19}

Exercício 3 — Somas paralelas

Dadas:

a = [10, 20, 30, 40]
b = [1, 2, 3, 4]


Use zip() para gerar uma lista com as somas de cada par:

[11, 22, 33, 44]

=======================================================================

🟡 PARTE 2 — Exercícios com zip_longest()

Você importa assim:

from itertools import zip_longest

Exercício 4 — Unir listas de tamanhos diferentes

Dados:

nomes = ['Matheus', 'Beatriz', 'João', 'Alice']
notas = [9.5, 8.7]


Use:

zip_longest(nomes, notas, fillvalue='Sem nota')


Resultado esperado:

[('Matheus', 9.5),
 ('Beatriz', 8.7),
 ('João', 'Sem nota'),
 ('Alice', 'Sem nota')]

Exercício 5 — Criar pares com valor padrão

Dados:

chaves = ['nome', 'idade', 'email', 'telefone']
valores = ['Matheus', 23]


Use zip_longest() para criar um dicionário assim:

{
    'nome': 'Matheus',
    'idade': 23,
    'email': None,
    'telefone': None
}


com fillvalue=None.

Exercício 6 — Intercalar strings

Dadas:

frase1 = "Python"
frase2 = "ABC"


Use zip_longest() para intercalar caractere por caractere, com fillvalue=''.

Resultado esperado:

['PA', 'yB', 'tC', 'h', 'o', 'n']

=======================================================================

🔴 PARTE 3 — DESAFIO FINAL
Exercício 7 — Criar uma função “zipper invertida”

Crie uma função zipper_full(a, b) que:

retorna uma lista de pares

usa zip() se as listas tiverem o mesmo tamanho

usa zip_longest() se tiverem tamanhos diferentes

e o usuário pode escolher o fillvalue (padrão: None)

Exemplo:

zipper_full([1, 2, 3], ['a'], fillvalue='vazio')


Resultado:

[(1, 'a'), (2, 'vazio'), (3, 'vazio')]