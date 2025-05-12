"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = 'Olha só que, coisa interessante'
# boas práticas: criar dois valores para a lista, uma raw(crua)
# e uma fixed(corrigida) para que possa corrigir esse tipo de formatação
frase_divida_raw = frase.split(', ')
# se não for passado nenhum parâmetro,
# o split irá dividir a frase a cada espaço em branco

frase_divida_fixed = []
for i, frase in enumerate(frase_divida_raw):
    frase_divida_fixed.append(frase_divida_raw[i].strip())
    # o strip() corta os espaços no começo e do fim da string.
    # rstrip() -> corta só o da direita
    # lstrip() -> corta só o da esquerda.

print(frase_divida_raw)
print(frase_divida_fixed)

frases_unidas = ', '.join(
    frase_divida_fixed
)  # insira o divisor dos valores entre ''.
print(frases_unidas)
