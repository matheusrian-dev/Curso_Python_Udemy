# Exemplo de f-Strings
# Cálculo do IMC - peso / (altura x altura)
nome = 'Matheus Rian'
altura = 1.73
peso = 76
imc = (
    peso / altura**2
)  # ** seria como elevar a variável ao número que vem em seguida

# ao inserir f antes de uma string, é habilitado o uso de variáveis dentro
# delas através dos colchetes {}
# caso queira formatar números com ponto flutuante (float), insira : e .
# seguido de quantas casas decimais deseja e f no final
# como no exemplo abaixo:
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
