"""
Exercício - Calcular Primeiro Dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros números do CPF
multiplicando cada um dos valores por uma contagem regressiva
começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
   7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
   
Somar todos os resultados:
70+36+48+56+12+20+3+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
    
    O primeiro dígito do CPF é 7
    
"""
# Minha solução
print('Sistema para Validação de CPF')
cpf = input('Insira um CPF (Apenas números):')
i = 10
j = 0
somacpf = 0
try:
    while i >= 2:
        digitoatual = int(cpf[j]) 
        somacpf += digitoatual * i
        i -= 1
        j += 1
    result_parcial = somacpf * 10
    result_final = result_parcial % 11
    if result_final > 9:
        result_final = 0
    print(f'O primeiro dígito do CPF é {result_final}')
except ValueError:
    print('Digite um CPF válido (apenas números)')
except IndexError:
    print('Quantidade de números inseridos não coincide com as de um CPF válido.')
except:
    print('Erro desconhecido, contate o administrador.')

# Solução do Instrutor
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
