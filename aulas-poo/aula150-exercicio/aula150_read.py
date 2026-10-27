# arquivo feito para ler o arquivo aula150-file.json e criar uma nova
# instância da classe Pessoa com os dados salvos.

import json

from aula150_save import Pessoa

with open('aula150_file.json', 'r', encoding='utf8') as arquivo:
    dados = json.load(arquivo)

# O operador ** desempacota o dicionário, passando cada chave como nome
# de argumento e seu respectivo valor como valor de argumento.
pessoa = Pessoa(**dados)

print(vars(pessoa))
