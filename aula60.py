"""
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançável.
O escopo local é o escopo onde apenas nomes do mesmo local podem
ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos externos.
A palavra global faz uma variável do escopo externo ser a mesma no
escopo interno.
"""

x = 1 # seria possível acessar a variável, transformando-a em global, porém é uma má prática.
def escopo():
    # global x # é possível definir uma variável local como global, porém também é uma má prática.
    x = 10 # variável local não pode ser acessada fora da função.
    def outra_funcao():
        y = 2
        print(x, y) # como essa função está dentro da função(escopo) onde a variável foi declarada, ela consegue acessar a variável. 
        
    outra_funcao()
    # print(y) # o contrário não acontece pois a variável(y) se torna local, não sendo acessível fora do escopo onde foi criada.
    print(x)
    # resumindo: escopos filhos conseguem acessar variáveis dos pais mas o inverso não é possível.

print(x)
escopo()
print(x) # alterar uma variável dentro de um escopo interno não altera a mesma no externo, são variáveis distintas com o mesmo nome.