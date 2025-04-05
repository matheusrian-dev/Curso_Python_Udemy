"""
Exercício
Gerando CPF's com o algoritmo das aulas anteriores (aulas 54 e 53)
"""
# Minha solução
import re
import sys

print('Gerador de CPF válido a partir de 9 dígitos')
cpf_enviado = input('Insira 9 números válido:')
cpf = re.sub( # basicamente o regex do c#
    r'[^0-9]', # faz com que substitua tudo que não seja números de 0 a 9 pelo valor passado
    '', # no caso, por nada, deixando apenas os valores numéricos.
    cpf_enviado)

# Método para recusar um cpf de um único número repetido várias vezes.
entrada_repetitiva = cpf == cpf[0] * len(cpf)
if entrada_repetitiva:
    print('Você digitou um valor sequencial (Ex.: 999.999.999-99)')
    sys.exit()


digitos = cpf[:9]
primeiro_index = 10
segundo_index = 11
resultado_1 = 0
resultado_2 = 0

try:
    if len(cpf) != 9: # Força IndexError caso a quantidade de caracteres passada for diferente de 9 caracteres
        raise IndexError()
    
    # Gera o primeiro dígito
    for digito in digitos:
        resultado_1 += int(digito) * primeiro_index
        primeiro_index -= 1
    primeiro_digito = (resultado_1 * 10) % 11
    primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
    digitos += str(primeiro_digito) # Insere o dígito na lista
    
    # Gera o segundo dígito
    for digito in digitos:
        resultado_2 += int(digito) * segundo_index
        segundo_index -= 1
    segundo_digito = (resultado_2 * 10) % 11
    segundo_digito = segundo_digito if segundo_digito <= 9 else 0
    digitos += str(segundo_digito) # Insere o dígito na lista
    
    print(f'Foi gerado o CPF conforme o valor passado: {digitos}')
        
except IndexError:
    print('Informe 9 dígitos.')
except:
    print('Erro desconhecido, contate o administrador.')
