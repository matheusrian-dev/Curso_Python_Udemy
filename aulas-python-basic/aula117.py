# Variáveis livres + nonlocals


def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        # Uma variável não pode ser acessada fora de seu escopo
        # por esse motivo é necessário explicitar para o python
        # que a mesma não é local.
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final

    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(f'Valor final: {final}')
