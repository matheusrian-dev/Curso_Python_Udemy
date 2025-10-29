"""
3. Soma de Ímpares
Escreva uma função que receba uma lista de números
e retorne a soma dos números ímpares.
"""

# Minha solução
# def soma_impares(lista):
#     soma = 0
#     for numero in lista:
#         if numero % 2 != 0:
#             soma += numero
#     return soma


# Solução simplificada ChatGPT
def soma_impares(lista):
    return sum(numero for numero in lista if numero % 2 != 0)


print(soma_impares([1, 2, 3, 4, 5]))  # 9
