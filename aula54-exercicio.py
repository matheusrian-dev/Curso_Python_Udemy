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
print('Sistema para Validação de CPF')
cpf = input('Insira um CPF (Apenas números):')
dez_digitos = cpf[:10]
i = 11
resultado = 0
try:
    for digito in dez_digitos:
        resultado += int(digito) * i
        i -= 1
    segundo_digito = (resultado * 10) % 11
    segundo_digito = segundo_digito if segundo_digito <= 9 else 0
    
    print(f'O segundo dígito do CPF é {segundo_digito}')
except ValueError:
    print('Digite um CPF válido (apenas números)')
except IndexError:
    print('Quantidade de números inseridos não coincide com as de um CPF válido.')
except:
    print('Erro desconhecido, contate o administrador.')