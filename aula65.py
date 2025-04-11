"""
Higher Order Functions - Funções que podem receber e/ou retornar outras funções
Funções de primeira classe - Funções que são tratadas como outros tipos de dados comuns (stirngs, inteiros, etc...)
"""
def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)

v = executa(saudacao, 'Bom dia', 'Matheus')
print(v)
