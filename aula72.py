"""
Métodos úteis dos dicionários em Python:
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
"""

pessoa = {
    "nome": "Matheus Rian",
    "sobrenome": "Souza",
    "idade": 26,
    "altura": 1.73,
}

# get
# print(pessoa['nome'])
# retorna o item da chave,
# o segundo parâmetro é o retorno caso ela não exista
# print(pessoa.get('nome', 'Não existe'))

# pop
# retorna o item da chave passada e depois o apaga
# nome = pessoa.pop('nome')
# print(pessoa)
# print(nome)

# popitem
# retorna o item da última chave e depois o apaga
ultima_chave = pessoa.popitem()
print(ultima_chave)
print(pessoa)

# update
# atualiza o dicionário conforme instruções dentro
# do método
pessoa.update({'nome': 'Nico', 'idade': 23})
# é possível fazer utilizando tuplas e listas também, conforme a linha abaixo:
# tupla = (('nome', 'novo valor'), ('idade', 30))
# lista = [['nome', 'novo valor'], ['idade', 30]]
# pessoa.update(tupla)
# pessoa.update(lista)
print(pessoa)
