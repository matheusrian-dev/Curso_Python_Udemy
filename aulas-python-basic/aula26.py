"""
Repetições
While (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Cuidado com o loop infinito!
"""

# ------------------------
# Exemplo de loop infinito
# condicao = True

# while condicao:
#     print(1)
#     print(2)
#     print(3)
# ------------------------

# condicao = True

# while condicao:
#     nome = input('Qual o seu nome: ')
#     print(f'Seu nome é {nome}')

# Esse print nunca será executado nessa sequencia,
# já que o while acima está em um loop infinito
# print(123)

# condicao = True

# while condicao:
#     entrada = input('Deseja entrar no sistema?')
#     entrar = entrada == 'sim' or entrada == 'Sim'
#     sair = entrada == 'não' or entrada == 'Não' or
#       entrada == 'nao' or entrada == 'nao'

#     if entrar:
#         print('Você entrou no sistema.')
#         break
#     elif sair:
#         print('Você saiu do sistema.')
#         break
#     else:
#         print('Resposta inválida, tente novamente.')

# condicao1 = True

# while condicao1:
#     entrada1 = input('Quer que o loop continue? S/N')
#     sim = entrada1 == 'S' or entrada1 == 's'
#     nao = entrada1 == 'N' or entrada1 == 'n'
#     if sim:
#         print('O loop irá continuar')
#     elif nao:
#         print('O loop será encerrado.')
#         condicao1 = False
#     else:
#         print('Resposta inválida, tente novamente.')

contador = 0

while contador < 10:
    contador = contador + 1

    if contador == 4:
        print('Pularemos o 4.')
        # pula todo o restante dessa repetição do loop e inicia a próxima
        continue

    print(contador)

print('Fim da contagem.')
