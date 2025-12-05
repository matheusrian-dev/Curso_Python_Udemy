✅ Projeto do Dia — Sistema de Gerenciamento de Biblioteca (Nível Intermediário)

Tempo estimado: 60–90 minutos
Conteúdo praticado:

Funções

Listas e dicionários

Arquivos JSON

Tratamento de erros

Decorators aplicado em funções reais

Validações

Estruturas de repetição e menus

Organização de código em módulos

🎯 Objetivo Geral

Criar um sistema simples de biblioteca onde o usuário pode:

Cadastrar livros

Listar livros

Buscar livro por título

Alterar informações de um livro

Emprestar / Devolver livro

Remover livro

Persistir tudo em JSON

🧱 Estrutura sugerida
biblioteca/
│
├── main.py
└── functions.py

🔥 Regras e Requisitos
✔ Um livro deve ter:
{
    "titulo": "Nome",
    "autor": "Nome",
    "ano": 2020,
    "status": "disponivel"  # ou "emprestado"
}

✔ Decorator obrigatório:

Crie um decorator chamado @require_title_input, que:

pergunta o título automaticamente ao usuário

injeta o valor como argumento na função decorada

evita repetição no main.py

📌 Exemplo:

@require_title_input
def search_book(title):
    ...


A função acima deve funcionar sem precisar passar title na chamada.

✔ Outro decorator opcional (mas recomendado):

@log_action, exibindo:

Nome da função

Mensagem antes e depois da execução

✔ Funcionalidades obrigatórias:
1. Cadastrar livro

Validar título, autor e ano

Impedir cadastros duplicados

Salvar no JSON

2. Listar livros

Exibir todos com formatação

Se lista vazia → mensagem apropriada

3. Buscar por título

Reaproveitando o decorator de título

Mostrar todas as informações do livro

4. Atualizar livro

Usuário pode alterar:

título

autor

ano

Ou voltar ao menu.

5. Emprestar / Devolver livro

Só permitir emprestar se status for "disponivel"

Só permitir devolver se status for "emprestado"

Regras de negócio simples, mas importantes.

6. Remover livro

Confirmar antes de excluir

Atualizar o JSON

7. JSON

Crie funções genéricas:

load_books()
save_books(lista)

🎁 Desafio Extra (opcional)

Crie um decorator:

@require_confirmation("Tem certeza que deseja continuar?")


Que pode ser usado nas funções de remoção ou empréstimo.