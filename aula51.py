#Desempacotamento em chamadas de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

# p, b, *_, ap, u = lista
# print(p, b, u, ap)

# for nome in lista:
#     print(nome, end = ' ', sep=', ') # o parametro end define o que é exibido no final da linha, sendo por padrão a quebra de linha '/n'
#                                      # exemplo: caso insira uma virgula, por exemplo, será inserida uma virgula no final do print
                                       # mas a quebra de linha será removida, se não for referenciada junto.
print(*lista) # itera todos os itens da lista, tupla ou string.
print(*lista, end=', ')
print(*lista, sep=', ') #já o parametro sep insere o que foi passado entre os valores dentro da string, tupla ou lista.