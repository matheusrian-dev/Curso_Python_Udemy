# Manipulando chaves e valores em dicionários
pessoa = {}

##
##
# é possível definir o nome da chave dinamicamente dessa forma.
chave = "nome_completo"  #

pessoa[chave] = "Matheus Rian"
pessoa["sobrenome"] = "Souza"
lista = []

print(pessoa[chave])
# Retorna KeyError pois a chave nome1 não foi criada.
# print(pessoa['nome1'])

pessoa[chave] = "Raquel"
del pessoa["sobrenome"]
print(pessoa)

# Por padrão o .get retorna None não é necessário inserir esse parametro no
# final do método. Ex.: pessoa.get("sobrenome", None)
if pessoa.get("sobrenome") is None:
    print("Não existe")
else:
    print(pessoa["sobrenome"])
