"""
Métodos úteis:
    append - Adiciona um item ao final da lista
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - Apaga um índice
    clear - limpa a lista
    + - concatena listas
Create Read Update   Delete
Criar, Ler, Alterar, Apagar lista[i] (CRUD)
"""

# lista = [10, 20, 30 ,40]
# lista.append('Matheus')
# nome = lista.pop() # Removeu o último elemento e o referenciou na variável
# lista.append(1233)
# del lista[-1]
#lista.clear()
# lista.insert(0, 5) # O insert requer dois argumentos, o primeiro é o índice e o segundo o valor que vai ser inserido.
# lista.insert(12315, 50) # Caso insira um índice que esteja fora do range atual da lista, o python irá inserir o valor no final da lista.
# print(lista)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b) # Métodos que não retornam nada, geralmente modificam o objeto que estão referenciando.
# lista_d = lista_a.extend(lista_b) # Por isso, ao tentar inserir o valor dessa ação em uma variável, ela retornará None
print(lista_a)