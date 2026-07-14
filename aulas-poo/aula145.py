"""
Entendendo self em classes Python
Classe - Molde (geralmente sem dados)
Instância das classes (objeto) - Tem os dados
Uma classe pode gerar várias instâncias.
Na classe o slef é a própria instância.
"""


class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
fusca.acelerar()
Carro.acelerar(fusca)
# print(fusca.nome)

celta = Carro(nome='Celta')
celta.acelerar()
Carro.acelerar(celta)
# print(celta.nome)
