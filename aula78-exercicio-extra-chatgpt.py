# Dado o seguinte conjunto:
nomes = {"Ana", "Carlos", "Bianca", "Ana", "Lucas", "Carlos"}

# 1. Imprima todos os nomes (sets não permitem repetições).
# 2. Adicione o nome "João".
# 3. Remova o nome "Bianca".
# 4. Verifique se "Lucas" está no conjunto.
for nome in nomes:
    print(nome)
nomes.add('João')
nomes.discard('Bianca')
if 'Lucas' in nomes:
    print('Há um Lucas no Set.')
else:
    print('Não há Lucas no Set.')
