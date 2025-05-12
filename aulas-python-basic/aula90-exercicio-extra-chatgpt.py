"""
4. Sistema simples de login
Crie um sistema com um dicionário de usuários (usuario: senha).
Solicite o login do usuário por input e informe se o
acesso foi permitido ou negado.
"""

# Minha Solução
usuarios = {
    'matheus': {'senha': '1998'},
    'ana': {'senha': '1234'},
}


def valida_usuario(usuario, senha):
    for perfil in usuarios:
        if usuario == perfil:
            if senha == usuarios[usuario].get('senha'):
                return True
    return False


print('Acesso ao Sistema')
print('\n')
usuario_recebido = input('Digite o usuário: ')
senha_recebida = input('Digite sua senha: ')

if valida_usuario(usuario_recebido, senha_recebida):
    print('Usuário validado, seja bem vindo!')
else:
    print('Usuário incorreto.')
