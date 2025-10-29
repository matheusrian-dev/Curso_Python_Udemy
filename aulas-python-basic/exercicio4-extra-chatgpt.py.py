"""
Crie uma função chamada executar_operacao_nomeada que:

Recebe uma função lambda como primeiro parâmetro;

Pode receber tanto *args quanto **kwargs;

Executa a função recebida, repassando os *args e **kwargs pra ela;

Retorna o resultado.
"""


def executar_operacao_nomeada(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


resultado = executar_operacao_nomeada(
    lambda nome, idade: f'{nome} tem {idade} anos', nome='Matheus', idade=25
)
print(resultado)
