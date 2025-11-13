🧩 Projeto: Sistema de Gerenciamento de Contatos (com persistência em JSON)
🎯 Objetivo:

Criar um programa que permita cadastrar, listar, buscar, atualizar e remover contatos, armazenando todos os dados em um arquivo contacts.json.
O conteúdo do arquivo deve ser mantido entre execuções.

🧱 Requisitos técnicos:
📁 Estrutura de arquivos:

main.py → contém o menu principal e as chamadas das funções.

functions.py → contém toda a lógica do CRUD (Create, Read, Update, Delete).

contacts.json → criado automaticamente ao salvar o primeiro contato.

🧩 Funcionalidades obrigatórias:

Cadastrar contato

Solicitar: nome, telefone e e-mail.

Validar se já existe um contato com o mesmo nome.

Salvar no arquivo JSON (append).

Listar contatos

Mostrar todos os contatos cadastrados.

Exibir uma mensagem se o arquivo estiver vazio.

Buscar contato por nome

Perguntar o nome e mostrar as informações se encontrado.

Se não encontrado, exibir mensagem adequada.

Atualizar contato

Buscar o contato por nome.

Permitir alterar telefone e/ou e-mail.

Remover contato

Confirmar antes da exclusão.

Sair do programa

Exibir mensagem de encerramento.

⚙️ Detalhes técnicos esperados:

Utilizar json.load() e json.dump() para leitura e escrita.

Tratar exceções como:

FileNotFoundError (caso o JSON ainda não exista).

json.JSONDecodeError (caso o arquivo esteja corrompido ou vazio).

ValueError para entradas inválidas.

Usar clear_terminal() e confirmation_pause() como nas versões anteriores.