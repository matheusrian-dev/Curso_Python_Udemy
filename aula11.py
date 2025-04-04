"""
Operadores lógicos
and (e), or(ou), not(não)

and - todas as condições precisam ser verdadeiras. Se qualquer valor for considerado falso,
a expressão inteira será avaliada naquele valor.

Truthy & Falsy

Um valor Falsy é algo que foi avaliado como false, no processo de coerção (conversão de tipos)
São considerados falsys: 0, 0.0 e ''
Também há o tipo None que é usado para representar um 'não valor'

Ao contrário do Falsy, um valor Truthy é algo que foi avaliado como true, no processo de coerção (conversão de tipos).
É considerado Truthy todo valor não listado como Falsy como exemplo acima.
"""
entrada = input('[E]ntrar [S]air:')
senha_digita = input('Senha: ')

senha_permitida = '123456'
if entrada == 'E' and senha_digita == senha_permitida:
    print('Entrar')
else:
    print('Sair')
    
#avaliação de curto circuíto
print(True and 0 and True)