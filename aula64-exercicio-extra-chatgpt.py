"""
Criar um script que gere senhas seguras e personalizáveis com base nas
escolhas do usuário.

Requisitos:
    O usuário define o tamanho da senha (mínimo de 4 caracteres).

    O usuário escolhe se quer:

    Letras maiúsculas

    Letras minúsculas

    Números

    Caracteres especiais (!@#$% etc.)

O script gera uma senha aleatória com base nas escolhas.
"""

# Minha solução
import random
import string

repeat = True
tem_maiuscula = False
tem_minuscula = False
tem_numero = False
tem_caractere_especial = False
perguntar = True


def valida_numero(numero):  # valida se o valor passado é um numero
    try:
        numero = int(numero)
    except ValueError:
        print(
            "Gentileza inserir uma quantidade válida de caracteres "
            + "(apenas números)."
        )
        return False
    return True


def repetir_programa():  # verifica se vai continuar o loop do programa
    resposta_enviada = input(
        "Gostaria de finalizar o programa? Digite sim para sair e digite "
        + "qualquer outra coisa para reiniciar: "
    )
    return resposta_enviada.lower() != "sim"  # True = continua, False = sai


def perguntas_sim_ou_nao(
    resposta,
):  # gera o valor booleano nas perguntas para fazer o checkin das
    # especificações da senha do usuário
    if resposta == "sim":
        return True
    return False


def valida_resposta(resposta):  # verifica se o usuário enviou uma resposta
    # válida.
    if resposta not in ["sim", "não", "nao"]:
        print("Resposta inválida, tente novamente.")
        return False
    return True


def gerador_senha(
    tamanho, maiuscula, minuscula, numero, caractere_especial
):  # gera a senha conforme as preferencias do usuário
    caracteres = ""

    if maiuscula:
        # insere letras maiúsculas no range
        caracteres += string.ascii_uppercase
    if minuscula:
        # insere letras minúsculas no range
        caracteres += string.ascii_lowercase
    if numero:
        # insere números no range
        caracteres += string.digits
    if caractere_especial:
        # insere caracteres especiais no range
        caracteres += string.punctuation

    if not caracteres:
        # caso o usuário não informe nenhum tipo de caractere
        return "Nenhum tipo de caractere selecionado!"

    senha = "".join(
        random.choice(caracteres) for _ in range(int(tamanho))
    )  # gera a string com base nos dados acima
    return senha


while repeat:
    print("Gerador de Senhas Personalizáveis")
    tamanho_senha = input(
        "Insira a quantidade de caracteres deseja em sua " + "senha: "
    )
    if valida_numero(tamanho_senha) is not True:
        repetir_programa()
    else:
        while perguntar:
            resposta_maiuscula = input(
                "Gostaria de inserir letras maiúsculas na senha? Digite sim "
                + "para inserir e não caso contrário: "
            ).lower()
            if valida_resposta(resposta_maiuscula):
                perguntar = False
            else:
                continue
            if perguntas_sim_ou_nao(resposta_maiuscula):
                tem_maiuscula = True

        perguntar = True
        while perguntar:
            resposta_minuscula = input(
                "Gostaria de inserir letras minúsculas na senha? Digite sim "
                + "para inserir e não caso contrário: "
            ).lower()
            if valida_resposta(resposta_minuscula):
                perguntar = False
            else:
                continue
            if perguntas_sim_ou_nao(resposta_minuscula):
                tem_minuscula = True

        perguntar = True
        while perguntar:
            resposta_numero = input(
                "Gostaria de inserir números na senha? Digite"
                + " sim para inserir e não caso contrário: "
            ).lower()
            if valida_resposta(resposta_numero):
                perguntar = False
            else:
                continue
            if perguntas_sim_ou_nao(resposta_numero):
                tem_numero = True

        perguntar = True
        while perguntar:
            resposta_caractere_especial = input(
                "Gostaria de inserir caracteres especiais na senha? Digite sim"
                + " para inserir e não caso contrário: "
            ).lower()
            if valida_resposta(resposta_caractere_especial):
                perguntar = False
            else:
                continue
            if perguntas_sim_ou_nao(resposta_caractere_especial):
                tem_caractere_especial = True

        senha = gerador_senha(
            tamanho_senha,
            tem_maiuscula,
            tem_minuscula,
            tem_numero,
            tem_caractere_especial,
        )
        print(f"Sua senha foi gerada: {senha}")
        tem_maiuscula = tem_minuscula = tem_numero = False
        tem_caractere_especial = False
        repeat = repetir_programa()

# Solução ChatGPT - Mais enxuta
# import random
# import string

# def valida_numero(numero):
#     try:
#         return int(numero)
#     except ValueError:
#         print('Gentileza inserir uma quantidade válida de caracteres'
#         + '(apenas números).')
#         return None

# def perguntar(texto):
#     while True:
#         resposta = input(texto + " (sim/não): ").strip().lower()
#         if resposta in ['sim', 'não', 'nao']:
#             return resposta == 'sim'
#         print('Resposta inválida, tente novamente.')

# def gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_numeros,
#                   usar_especiais):
#     caracteres = ''
#     if usar_maiusculas:
#         caracteres += string.ascii_uppercase
#     if usar_minusculas:
#         caracteres += string.ascii_lowercase
#     if usar_numeros:
#         caracteres += string.digits
#     if usar_especiais:
#         caracteres += string.punctuation

#     if not caracteres:
#         return 'Nenhum tipo de caractere selecionado!'

#     return ''.join(random.choice(caracteres) for _ in range(tamanho))

# def main():
#     while True:
#         print('\n=== Gerador de Senhas Personalizáveis ===')
#         tamanho_input = input('Insira a quantidade de caracteres desejada: ')
#         tamanho = valida_numero(tamanho_input)
#         if tamanho is None:
#             continue

#         usar_maiusculas = perguntar('Incluir letras maiúsculas?')
#         usar_minusculas = perguntar('Incluir letras minúsculas?')
#         usar_numeros = perguntar('Incluir números?')
#         usar_especiais = perguntar('Incluir caracteres especiais?')

#         senha = gerar_senha(tamanho, usar_maiusculas, usar_minusculas,
#                               usar_numeros, usar_especiais)
#         print(f'\nSua senha gerada é: {senha}')

#         if not perguntar('Deseja gerar outra senha?'):
#             print('Programa finalizado.')
#             break

# if __name__ == '__main__':
#     main()
