"""
Exercício - Calcular Segundo Dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros números do CPF e some ao primeiro dígito
multiplicando cada um dos valores por uma contagem regressiva
começando de 10

Ex.:  746.824.890-70 (746824890)
   11 10  9  8  7  6  5  4  3  2
   7   4  6  8  2  4  8  9  0  7
   70  36 48 56 12 20 32 27 0 14
   
Somar todos os resultados:
77+40+54+64+14+24+40+34+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
    
    O segundo dígito do CPF é 0
"""
# Calculo do primeiro digito passado pelo instrutor
# cpf = '74682489070'
# nove_digitos = cpf[:9]
# contador_regressivo = 10

# resultado = 0
# for digito in nove_digitos:
#     resultado += int(digito) * contador_regressivo
#     contador_regressivo -= 1
# primeiro_digito = (resultado * 10) % 11
# primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
# print(f'O primeiro dígito do CPF é {primeiro_digito}')
# Minha solução

# Método 1 para remover caracteres indesejados
#cpf_enviado = '746.824.890-70' \ # utilize o replace para remover caracteres simples como pontuações de alguns dados que precisam ser tratados. 
    #.replace('.', '') \
    #.replace(' ', '') \
    #.replace('-', '')

# Método 2 para remover caracteres indesejados
import re
import sys

print('Sistema para Validação de CPF')
cpf_enviado = input('Insira um CPF válido:')
cpf = re.sub( # basicamente o regex do c#
    r'[^0-9]', # faz com que substitua tudo que não seja números de 0 a 9 pelo valor passado
    '', # no caso, por nada, deixando apenas os valores numéricos.
    cpf_enviado)

# Método para recusar um cpf de um único número repetido 11 vezes.
entrada_repetitiva = cpf == cpf[0] * len(cpf)
if entrada_repetitiva:
    print('Você digitou um valor sequencial (Ex.: 999.999.999-99)')
    sys.exit()


dez_digitos = cpf[:10]
i = 11
resultado = 0

try:
    if len(cpf) != 11: # Força IndexError caso a quantidade de caracteres passada for diferente de 11 caracteres
        raise IndexError()

    for digito in dez_digitos:
        resultado += int(digito) * i
        i -= 1
    segundo_digito = (resultado * 10) % 11
    segundo_digito = segundo_digito if segundo_digito <= 9 else 0
    # print(f'O segundo dígito do CPF é {segundo_digito}')
    
    cpf_gerado = f'{cpf[:10]}{segundo_digito}'
    if cpf_gerado == cpf:
        print(f'O CPF {cpf_gerado} é válido.')
    else:
        print('CPF inválido.')
    
except ValueError:
    print('Digite um CPF válido')
except IndexError:
    print('Quantidade de números inseridos não coincide com as de um CPF válido.')
except:
    print('Erro desconhecido, contate o administrador.')
