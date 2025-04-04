"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

# v1 = 'a'
# v2 = 'a' # Caso haja duas variáveis com exatamente o mesmo valor, o python irá atribuir o mesmo id para ambas
# print(id(v1))
# print(id(v2))

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True # É um péssimo hábito criar variáveis dentro de ifs, já que caso tente retorná-la fora dele
    print('Faça algo')  # pode haver situações onde a condição não foi atendida, gerando uma exceção
else:
    print('Não faça algo')
    
if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')