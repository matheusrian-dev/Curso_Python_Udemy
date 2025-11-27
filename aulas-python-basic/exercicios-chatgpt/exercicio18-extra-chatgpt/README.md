Projeto do Dia — “Sistema de Logs com Decorators + Gerenciamento de Usuários”
Objetivo

Criar um pequeno sistema de usuários com:

cadastro

listagem

busca

remoção

E usar decorators para:

Registrar logs automáticos de cada ação

Validar entradas antes da execução das funções

Módulo principal: main.py
Módulo com funções: functions.py
🎯 Requisitos
1. Crie um decorator chamado log_action

Ele deve:

imprimir qual função foi chamada

imprimir argumentos recebidos

imprimir o resultado (se houver)

Exemplo de saída:

[LOG] Função: add_user
[LOG] Args: ('Carlos',), Kwargs: {}
[LOG] Execução finalizada

2. Crie um decorator chamado validate_string

Ele deve:

receber como parâmetro o nome do argumento que deve ser string

verificar se o argumento é string antes de executar

se não for, levantar um TypeError

Uso no código:

@validate_string("name")
def add_user(name):
    ...

3. As funções do sistema

add_user(name)

list_users()

search_user(name)

remove_user(name)

Todos devem usar @log_action.

Os que recebem name devem usar também @validate_string("name").

4. Armazenamento

Use uma lista interna no módulo functions.py:

users = []