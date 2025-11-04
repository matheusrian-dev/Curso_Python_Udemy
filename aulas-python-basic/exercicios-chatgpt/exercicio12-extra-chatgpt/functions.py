def calculate(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        if number2 == 0:
            raise ZeroDivisionError
        return number1 / number2


def validate_operator(operator):
    operators = ['+', '-', '*', '/']
    if operator in operators:
        return True
    raise ValueError


def validate_number(number):
    try:
        return float(number)
    except ValueError:
        raise TypeError
