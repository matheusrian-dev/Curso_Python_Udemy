🧩 Projeto prático #4 — Sistema de Controle de Estoque Simplificado
🎯 Objetivo

Criar um programa modular (com main.py e functions.py) que gerencie um pequeno estoque de produtos.
O usuário deve poder cadastrar, listar, atualizar e remover produtos, além de ver o valor total do estoque.

📁 Estrutura esperada

main.py → interface com o usuário (menu principal e laço principal)

functions.py → todas as funções lógicas (cada operação separada)

Armazenamento: utilize uma lista de dicionários, como nos projetos anteriores.

🧠 Requisitos funcionais

Cadastrar produto

Solicite: nome, quantidade e preço unitário.

Valide se os valores inseridos são válidos (float ou int positivos).

Gere um id incremental automático.

Listar produtos

Exiba todos os produtos cadastrados, mostrando:

ID | Nome | Quantidade | Preço Unitário | Valor Total


Atualizar produto

Peça o ID e permita editar quantidade e preço.

Se o ID não existir, informe o erro e volte ao menu.

Remover produto

Solicite confirmação antes de excluir.

Mostrar valor total do estoque

Some (quantidade × preço unitário) de todos os produtos.

Encerrar o programa

⚠️ Tratamento de exceções obrigatório

Use try/except para capturar:

ValueError (entrada não numérica)

KeyError (ID inexistente)

E evite except Exception genéricos — trate o que for previsível.