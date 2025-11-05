🎯 Objetivo

Criar um sistema simples de gerenciamento de alunos, que permita:

Cadastrar alunos e suas notas.

Listar todos os alunos cadastrados.

Mostrar a média geral da turma.

Remover um aluno específico.

Encerrar o programa.

📋 Requisitos obrigatórios

Use tratamento de exceções (try/except) onde fizer sentido — principalmente na entrada de dados.

Guarde os alunos em uma lista de dicionários, ex:

alunos = [
    {'nome': 'João', 'nota': 8.5},
    {'nome': 'Maria', 'nota': 9.0}
]


Valide para que notas inválidas (como letras, números negativos ou acima de 10) gerem erro.

Estruture o menu em loop, permitindo repetir até o usuário escolher sair.