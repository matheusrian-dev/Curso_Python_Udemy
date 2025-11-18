📝 Exercício de Fixação – Criando funções com valores “congelados” (closure)

Crie uma função chamada criar_contador que deve:

Receber um número inicial.

Criar e retornar uma função interna que:

incrementa esse número sempre que for chamada;

e retorna o valor atualizado.

Funcionamento esperado:
contador = criar_contador(10)

print(contador())  # 11
print(contador())  # 12
print(contador())  # 13

outro_contador = criar_contador(100)
print(outro_contador())  # 101
print(outro_contador())  # 102

print(contador())  # 14 (continua de onde parou)

Regras:

Você não deve usar classes, apenas funções.

A função interna deve acessar a variável da função externa através de closure.

A variável deve continuar existindo mesmo depois que a função externa terminar.

💡 Dica (sem entregar a solução)

Use algo assim dentro da função interna:

nonlocal variavel


Isso permite alterar a variável da função externa.

🎯 Objetivo do exercício

Você vai praticar:

Capturar variáveis dentro de um closure

Retornar funções internas

Manter estado entre chamadas

Entender escopo léxico

Usar nonlocal

Esse é um exercício perfeito para consolidar o que você acabou de aprender.