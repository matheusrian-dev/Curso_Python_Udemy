"""
enumerate - enumera iteráveis (índices)
"""
lista = ['Karen', 'Geovana', 'Marina']

lista_enumerada = enumerate(lista)
# print(lista_enumerada) # tentar exibir um enumerate de forma direta irá retornar o objeto em si e não os valores referenciados

#print(list(lista_enumerada)) # É possível exibir ao converter o enumerate para lista ou tupla

for indice, item in lista_enumerada:
     print(indice, item) # Outro método de exibir os itens do enumerate

# for item in lista_enumerada:
#     print(item) # Por algum motivo, o python continua os 'for's subsequentes da onde o outro parou, sendo assim ele não exibirá mais nada.