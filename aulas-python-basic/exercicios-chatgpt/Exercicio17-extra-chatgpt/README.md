📘Gerenciador de Tarefas (To-Do List) com Prioridade e Persistência em JSON

Um sistema simples, mas extremamente útil, perfeito para entrevistas de vaga júnior (projetos CRUD com persistência de dados são muito valorizados).

🎯 Funcionalidades obrigatórias

Seu sistema deve permitir:

1. Adicionar tarefa

Cada tarefa deve ter:

título

descrição

nível de prioridade (baixa, média, alta)

status (pendente inicialmente)

2. Listar tarefas

Mostrar todas as tarefas assim:

Título: ...
Descrição: ...
Prioridade: ...
Status: ...
-----------------------------

3. Atualizar tarefa

Permitir alterar qualquer uma das informações:

título

descrição

prioridade

status (pendente → concluída ou vice-versa)

4. Remover tarefa
5. Buscar tarefa por título
6. Persistir tudo em arquivo JSON

Arquivo recomendado:

tasks.json


Use as mesmas ideias do seu projeto anterior:

load_tasks()

save_tasks()

💠 Regras e validações

Título não pode ser vazio.

Prioridade deve ser apenas:

baixa

media

alta

Mostrar mensagem quando nada for encontrado.

Usar estruturas claras e funções bem separadas.

📁 Sugestão de Estrutura
main.py
functions.py
tasks.json   (gerado automaticamente)