🔹 EXERCÍCIO 1 — MAP

Crie uma função que receba uma lista de preços (floats) e retorne uma nova lista com 10% de desconto usando map.

Regras:

A função aplicadora deve estar separada (nada de lambda)

Tem que converter o resultado pra list no final

🔹 EXERCÍCIO 2 — FILTER

Dada uma lista de idades, filtre apenas as idades que representam maiores de 18 anos usando filter.

Extras opcionais:

evitar lambda e criar a função separada

🔹 EXERCÍCIO 3 — REDUCE

Use reduce para somar o tamanho total das palavras de uma lista.

Exemplo de entrada:

["python", "curso", "estudo"]


Saída esperada:

17

🔹 EXERCÍCIO 4 — RECURSIVIDADE

Implemente uma função recursiva chamada soma_recursiva(lista) que soma todos os números de uma lista sem usar loops.

Regras:

Não pode usar sum()

Não pode usar while ou for

A função deve ser apenas 3–6 linhas

🔹 EXERCÍCIO 5 — PARTIAL

Crie uma função multiplicar(a, b) que retorna a * b.
Usando partial, crie:

uma função que sempre dobra números

uma função que sempre triplica números

Depois aplique ambas em uma lista com map.

🔹 EXERCÍCIO 6 — MAP + FILTER

Dada a lista:

nomes = ["Ana", "Paulo", "Beatriz", "João", "Amanda"]


Use filter para pegar apenas nomes que começam com “A”.

Use map para transformar todos em letras minúsculas.

🔹 EXERCÍCIO 7 — GENERATOR

Crie um generator chamado gerador_de_passos() que:

começa em 1

vai até 5

gera um valor por vez usando yield

E então, no programa principal:

itere sobre ele

imprima cada valor

ao final, imprima o tipo do objeto retornado

🔹 EXERCÍCIO 8 — REDUCE + PARTIAL

Usando apenas reduce + partial:

Crie uma função que multiplique todos os valores de uma lista

Sem escrever lambdas diretamente dentro do reduce

A operação de multiplicação deve vir de uma função “especializada” criada com partial

🔹 EXERCÍCIO 9 — RECURSIVIDADE (nível um pouquinho maior)

Crie uma função recursiva que conte quantas vezes uma letra aparece em uma string.

Exemplo:

contar_letra("banana", "a")  # 3


Sem loops.

🔹 EXERCÍCIO 10 — FILTER + GENERATOR

Crie um generator que receba uma lista e gere apenas os números pares.

Depois:

aplique filter para garantir que nenhum número negativo seja gerado