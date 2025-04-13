"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"

    return saudar


# lembrando que se não inserir os parenteses ao retornar
# uma função, ele vai retornar o local da função na memória e não vai
# executá-la diretamente
# enquanto essa função não for executada, o python irá armazenar as
# variáveis passadas em um local da memória também.


falar_bom_dia = criar_saudacao("Bom dia")
falar_boa_noite = criar_saudacao("Boa noite")

print(
    falar_bom_dia("Luiz")
)  # O closure é quando você fecha os parenteses na variável onde será
# executada a função, dessa forma aqui. Isso faz com que o python execute
# a função.
print(
    falar_boa_noite("Luna")
)  # Isso permite que passamos argumentos em momentos futuros do código,
# tornando ele mais legível

for nome in [
    "Maria",
    "Joana",
    "Luiz",
]:  # um exemplo de como iterar o mesmo código com vários nomes diferentes
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
