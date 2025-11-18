def criar_contador(numero_inicial):
    contador = numero_inicial

    def incrementar_contador():
        nonlocal contador
        contador += 1
        return contador

    return incrementar_contador


contador = criar_contador(5)

print(contador())
print(contador())
print(contador())

outro_contador = criar_contador(70)

print(outro_contador())
print(outro_contador())
print(outro_contador())
print(outro_contador())
print(outro_contador())
