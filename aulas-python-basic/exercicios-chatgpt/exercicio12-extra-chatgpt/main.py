from functions import calculate, validate_number, validate_operator

try:
    number1 = validate_number(input('Insira o primeiro número: '))
    number2 = validate_number(input('Insira o segundo número: '))
    operator = input('Informe o tipo de operação (+, -, *, /): ')
    validate_operator(operator)
    result = calculate(number1, number2, operator)
    print(f'Resultado: {result}')
except ValueError:
    print('Operador inválido.')
except TypeError:
    print('O valor passado não é um número válido.')
except ZeroDivisionError:
    print('Não é possível realizar divisões por zero.')
finally:
    print('Até a próxima!')
