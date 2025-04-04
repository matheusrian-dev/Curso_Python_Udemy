"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Exemplo:
Bom dia: 0 às 11, Boa tarde: 12 às 17 e Boa noite: 18 às 23
"""
horario = input('Digite a hora em número inteiro: ')
try:
    horario_int = int(horario)
    bom_dia = horario_int >= 0 and horario_int <= 11
    boa_tarde = horario_int >= 12 and horario_int <= 17
    boa_noite = horario_int >= 18 and horario_int <= 23
    if bom_dia:
        print('Bom dia')
    elif boa_tarde:
        print('Boa tarde')
    elif boa_noite:
        print('Boa noite')
    else:
        print('Hora inválida')
except:
    print('Hora inválida')