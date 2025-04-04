"""
Introdução ao desempacotamento + tuples(tuplas)
Tipo tupla - Uma lista imutável
"""
nomes = ['Karen', 'Geovana', 'Marina']
# nome1, nome2, nome3 = nomes # o desempacotamento atribui cada valor a uma variável na ordem que foi especificada.
                            # Inicialmente e de forma direta é obrigatório que tenha o mesmo tanto de variáveis e de valores na lista.
                            # Ex.: 1º variável -> indice 0
_, nome, *_ = nomes # Caso precide puxar menos valores do que tem na lista, utilize uma variável antecedida por * para empacotar o resto
                  # dos valores. Essa variável de resto que não for utilizada, geralmente é referenciada com um underline (_) para
                  # que outros programadores entendam que ela é só uma variável descartada com o resto dos valores não utilizados.
print(nome)

# Exemplo de tupla
items = 'Matheus', 'João', 'Raquel' # ao inserir uma lista em uma variável sem o [] a mesma se torna uma tupla, ou seja, imutável
                                    # pode ser feita com parênteses () também ou com conversão (items = tuple('a', 'b', 'c'))
                                    # é possível converter tuplas em listas e vice e versa.
#items[1] = 'Bruno' # Isso gerará um erro informando que o tipo tupla não suporta modificações em seus itens.
print(items[0], items[-1])