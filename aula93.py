# dir, hasattr, getattr

# dir - ao digitar dir(objeto) no terminal retorna todos os atributos
# definidos dentro do objetivo nos parênteses

string = 'Matheus'
print(string)
metodo = 'upper1'
# hasattr - checa se o objeto tem um certo atributo
if hasattr(string, metodo):
    print('Existe upper')
    # invoca um método de dentro de um objeto
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)
