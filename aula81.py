# Empacotamento e desempacotamento de dicionários

# a, b = 1, 2
# a, b = b, a
# print(a, b)


# Ao iterar dentro de um dicionário, normalmente é
# retornado primeiro as chaves.
# a, b = pessoa
# Lembre-se de inserir o .values() para assinalar
# para o Python que precisa dos valores.
# a, b = pessoa.values()
# print(a, b)
# Exemplo de desempacotamento interno
# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(f'{chave}: {valor}')

# Métodos para unificar dois dicionários
pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 26,
    'altura': 1.64,
}

# 1º método: unir ambos em um terceiro dicionário novo
# utilize o ** para sinalizar de que irá puxar todos os dados
# do dicionário.
perfil_pessoa = {**pessoa, **dados_pessoa, 'signo': 'Leão'}

print(perfil_pessoa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados:', args)

    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')


# Lembrando que ao passar argumentos não nomeados eles aparecerão
# separados dos kwargs
# mostro_argumentos_nomeados(1, 2, nome='Joana', qualquer=123)
mostro_argumentos_nomeados(**perfil_pessoa)
