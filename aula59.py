"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançável.
O escopo local é o escopo onde apenas nomes
do mesmo local podem ser alcançados.
"""

# seria possível acessar a variável,
# transformando-a em global, porém é uma má prática.
x = 1


def escopo():
    # é possível definir uma variável local como global,
    # porém também é uma má prática.
    # global x
    # variável local não pode ser acessada fora da função.
    x = 10

    def outra_funcao():
        y = 2
        # como essa função está dentro da função(escopo)
        # onde a variável foi declarada, ela consegue acessar a variável.
        print(x, y)

    outra_funcao()
    # o contrário não acontece pois a variável(y) se torna local,
    # não sendo acessível fora do escopo onde foi criada.
    # print(y)
    print(x)
    # resumindo: escopos filhos conseguem acessar variáveis
    # dos pais mas o inverso não é possível.


print(x)
escopo()
# alterar uma variável dentro de um escopo interno
# não altera a mesma no externo,
# são variáveis distintas com o mesmo nome.
print(x)
