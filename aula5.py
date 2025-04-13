# Formatação de strings com método format

a = 'A'
b = 'B'
c = 1.1
d = 'D'
e = 123
f = "1x"
# é possível utilizar sem os índices mantendo os colchetes sem número,
string = 'a = {0} b = {1} c = {2:.2f}'
formato = string.format(
    a, b, c
)  # porém será utilizada na ordem da lista de parâmetros.

# se um parametro for nomeado, todos os parametros que vierem depois dele
# também devem ser.
string1 = 'd = {param1} e = {param2} f = {param}'
formato_Nomeado = string1.format(param=d, param1=e, param2=f)

print(formato)
print(formato_Nomeado)
