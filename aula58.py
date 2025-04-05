"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja enviado
para o parâmetro, o valor padrão será usado.
Refator: editar o seu código;
"""

def soma (x, y, z=None): # Lembrando que 0 é considerado um valor falsy, então se referenciar um argumento como 0 diretamente, ele será visto como booleano
    if z is not None: # utilize o is ou is not para que o zero passado como argumento seja visualizado
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200, 0) # Caso o is ou is not não seja utilizado, o 0 no parâmetro z não será passado como um valor numérico e sim como um boolean
soma(y = 6, z= 13, x = 5)