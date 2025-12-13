🧩 Sistema de Registro de Hábitos

Crie um programa em Python que permita o usuário registrar hábitos que ele deseja acompanhar diariamente.

O sistema deve rodar no terminal e possuir um menu simples.

1. Estrutura dos dados

Cada hábito deve ser armazenado com:

nome do hábito (string)

descrição (string, opcional)

dias_concluidos (lista contendo datas ou apenas contadores)

ativo (True/False) – caso o hábito seja arquivado

Você pode armazenar tudo em um dicionário, em memória.

2. Funcionalidades obrigatórias

O menu deve permitir:

(1) Adicionar um hábito

Pergunta pelo nome

Pergunta pela descrição (opcional)

Inicializa dias_concluidos como lista vazia

Define ativo=True

Validação:

Não permitir nomes repetidos.

(2) Marcar hábito como concluído no dia

Perguntar o nome do hábito

Registrar a data atual (use uma string tipo “2025-12-10”)

Não duplicar a mesma data

(3) Listar hábitos

Listar apenas hábitos ativos com:

nome

dias já concluídos

porcentagem de conclusão da semana (7 dias)

Exemplo de saída:

Hábito: Beber água 
Concluído: 3 dias | 42%

(4) Arquivar um hábito

Muda o campo ativo para False

Arquivados não aparecem na listagem normal

(5) Listar hábitos arquivados

Mostrar apenas nome e total de dias concluídos.

3. Regras adicionais

Todo o código deve estar organizado em funções, nada de código solto.

Tente deixar o menu mínimo, usando funções auxiliares sempre que possível.

Preocupe-se com clareza: variáveis descritivas, bons nomes, funções pequenas (Clean Code!).

⭐ Desafios opcionais

(Se quiser ir além)

Criar função de “desarquivar”

Exportar o banco para um arquivo .txt

Usar reduce para calcular alguma estatística

Criar relatório semanal impresso no terminal