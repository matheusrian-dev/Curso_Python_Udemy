"""
Sets - Conjuntos em Python (tipo set)
Conjuntos são ensinados na matemática
https://brasilescola.uol.com.br/matematica/conjunto.html
Representados graficamente pelo diagrama de Venn
Sets em Python são mutáveis, porém aceitam apenas
tipos imutáveis como valor interno.

Criando um set
set(iterável) ou {1, 2, 3}

Sets são eficientes para remover valores duplicados
de iteráveis.
- eles não tem indexes;
- eles não garantem ordem;
- eles são iteráveis (for, in, not in)

Métodos úteis:
add, update, clear, discard
"""

# Sets parecem dicionários porém não tem chave, apenas valor.
# Apesar de ser iteráveis os valores podem não ser mantidos na ordem
# que foram enviados, como no caso da string abaixo
# s1 = set('Matheus')

# É possível criar o set com {} porém é necessário passar todos os valores
# na linha onde o set é criado.
# s1 = {'Matheus', 2, 3, 4}
s1 = {'Matheus'}
print(s1)
