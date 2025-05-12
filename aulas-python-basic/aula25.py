"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = 'matheus Rian'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
# tipos imutáveis não podem ter seus valores substituídos de forma direta
# string[3] = 'ABC'
print(string)
print(string.capitalize())
print(outra_variavel)
