# Exercício - Sistema de Perguntas e Respostas
import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5x5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

# Minha solução
acertos = 0
print('Questionário - Matemática Fundamental 01')
input('\nPressione Enter para começar')
# código para limpar a tela
os.system('cls' if os.name == 'nt' else 'clear')
contador_perguntas = 1
contador_opcoes = 1

for pergunta in perguntas:
    resposta = ''
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Questão {contador_perguntas}: ')
    print(pergunta['Pergunta'])

    for opcao in pergunta['Opções']:
        print(f'Opção {contador_opcoes}: {opcao}')
        contador_opcoes += 1

    while resposta not in pergunta['Opções']:
        print('Digite sua resposta: ')
        resposta = input('')

        if resposta not in pergunta['Opções']:
            print('Sua resposta não está entre as opções passadas.')
            continue

        if resposta == pergunta['Resposta']:
            print('Resposta correta!')
            input('')
            acertos += 1
        else:
            print('Sua resposta está incorreta.')
        input('\nPressione Enter para continuar...')
        break

    contador_opcoes = 1
    contador_perguntas += 1

os.system('cls' if os.name == 'nt' else 'clear')
print('Teste finalizado!')
if acertos >= 2:
    print('Você foi aprovado!')
else:
    print('Você foi reprovado.')
print(f'Número de acertos: {acertos}')
