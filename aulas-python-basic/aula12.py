"""
Operadores lógicos
and (e), or(ou), not(não)

or - Qualquer condiçaõ verdadeira avalia toda a expressão como verdadeira.

Truthy & Falsy

Um valor Falsy é algo que foi avaliado como false, no processo de coerção
(conversão de tipos) são considerados falsys: 0, 0.0 e ''
Também há o tipo None que é usado para representar um 'não valor'

Ao contrário do Falsy, um valor Truthy é algo que foi avaliado como true, no
processo de coerção (conversão de tipos). É considerado Truthy todo valor
não listado como Falsy como exemplo acima.
"""

# entrada = input('[E]ntrar [S]air:')
# senha_digita = input('Senha: ')

# senha_permitida = '123456'
# if (entrada == 'E' or entrada == 'e') and senha_digita == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuíto
senha = input('Senha: ') or 'Sem senha'
print(senha)
