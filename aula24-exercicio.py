"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome tem
um tamanho médio"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu nome: ')
nome_curto = len(nome) >= 1 and len(nome) < 5
nome_medio = len(nome) > 4 and len(nome) < 7
sem_entrada = len(nome) < 1

if nome_curto:
    print('Seu nome é curto')
elif nome_medio:
    print('Seu nome tem um tamanho médio')
elif sem_entrada:
    print('Nada foi digitado')
else:
    print('seu nome é muito grande')