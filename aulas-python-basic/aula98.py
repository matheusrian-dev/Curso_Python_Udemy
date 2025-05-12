# Try, except, else e finally

try:
    a = 18
    b = '0'
    print('linha 1')
    # print(b - 1)
    c = a / b
    print('linha 2')
# Nunca é uma boa prática utilizar o except genérico por si só.
# cada except específico é uma classe que herda do except genérico.
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('Nome b não está definido.')
# É possível capturar mais de um tipo de exception de uma vez mas
# não é o recomendado. Use apenas no caso de explicitamente não
# precisar saber o tipo de erro, apenas tratar o conjunto.
except (TypeError, IndexError) as error:
    print('Erro de tipo/índice.')
    print(f'Name: {error.__class__.__name__}')
    print(f'MSG: {error}')
# Utilize a exception genérica apenas em sistemas mais robustos onde há uma
# cadeia de exception razoável para captar erros inesperados.
# Lembre-se sempre de buscar exibir o log para identificar qual o erro.
except Exception as e:
    print(f'Erro desconhecido: {e}')
# else é executado quando o código não gera exceções dentro do try.
else:
    print('Não deu erro')
# finally sempre será executado, o try sendo executado corretamente ou não.
finally:
    print('Continuar...')
