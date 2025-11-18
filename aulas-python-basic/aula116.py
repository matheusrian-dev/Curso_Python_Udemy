# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, *args_parciais):
    def interna(*args_finais):
        return funcao(*args_parciais, *args_finais)

    return interna


multiplica_por_dez = criar_funcao(multiplica, 10)
resultado_multiplica = multiplica_por_dez(2)

print(resultado_multiplica)

soma_com_cinco = criar_funcao(soma, 5)
resultado_soma = soma_com_cinco(2)

print(resultado_soma)
