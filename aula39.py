"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop del, clear, extend, +
CRUD - Create Read Update Delete 
"""
lista = [10, 20, 30, 40]
print('Antes do comando del')
print(lista)
#del lista[2] # deleta o valor no indice indicado
              # adendo importante!: ao deletar um item ele move o restante para a direita, reorganizando a lista. Em listas
              # extensas essa movimentação pode deixar o processo do código um pouco pesado e lento.
#print('Depois do comando del')
#print(lista)
lista.append(50) # adiciona o valor no final da lista
lista.pop() # remove o último valor da lista
lista.append(60) 
lista.append(70)
ultimo_valor = lista.pop() 
print(lista, 'Removido, ', ultimo_valor)
