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

Operadores úteis:
união | union - Une
intersecção & intersection - Itens presentes em ambos
diferença - Itens presentes apenas no set da esquerda
diferença simétrica ^ Itens que não estão em ambos
"""

# Sets parecem dicionários porém não tem chave, apenas valor.
# Apesar de ser iteráveis os valores podem não ser mantidos na ordem
# que foram enviados, como no caso da string abaixo
# s1 = set('Matheus')

# É possível criar o set com {} porém é necessário passar todos os valores
# na linha onde o set é criado.
s1 = {'Matheus', 2, 3, 4}
# s1 = {'Matheus'}
print(s1)

# Formas de utilizar o set para remover duplicatas em uma lista
# type convergion
l1 = [1, 1, 1, 2, 2, 2, 4, 7]
# convertendo a lista para set as duplicatas são removidas
s1 = set(l1)
# ao transformá-la novamente em lista, não haverá duplicatas
l2 = list(s1)
# o maior problema desse método é que o set não mantém a ordem
# e como não há indexes em sets, não é possível acessar um valor
# específico como por exemplo s1[0]. Porém eles são iteráveis com
# for, in ou not in como no exemplo abaixo
# for numero in s1:
#     print(numero)
print(l2)
