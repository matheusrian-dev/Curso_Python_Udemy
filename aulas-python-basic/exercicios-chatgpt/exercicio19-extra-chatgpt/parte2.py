from itertools import zip_longest
from parte1 import separador_exercicio

# Exercício 4 — Unir listas de tamanhos diferentes
nomes = ['Matheus', 'Beatriz', 'João', 'Alice']
notas = [9.5, 8.7]

alunos = list(zip_longest(nomes, notas, fillvalue='Sem nota'))
for aluno in alunos:
    print(aluno)
separador_exercicio()

# Exercício 5 — Criar pares com valor padrão
chaves = ['nome', 'idade', 'email', 'telefone']
valores = ['Matheus', 23]
pessoa = dict(zip_longest(chaves, valores, fillvalue=None))
print(pessoa)
separador_exercicio()

# Exercício 6 — Intercalar strings
frase1 = "Python"
frase2 = "ABC"

frase_unida = [x + y for x, y in zip_longest(frase1, frase2, fillvalue='')]
print(frase_unida)
separador_exercicio()
