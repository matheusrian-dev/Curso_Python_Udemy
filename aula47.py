"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format.html
https://docs.python.org/pt/3/tutorial/floatingpoint.html"""
import decimal #utilizado em último caso, quando se precisa realmente de precisão nos últimos dígitos de várias casas decimais.

#numero_1 = decimal.Decimal('0.1') # ao utilizar esse método, insira o valor como string ou int pois o tipo float gerará um número
#numero_2 = decimal.Decimal('0.7') # impreciso
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3) #retorna valores imprecisos em alguns casos
print(f'{numero_3:.2f}')
print(round(numero_3, 2)) #arredonda o valor pelo número de casas decimais passadas, ele ignora os 0's ao exibir
