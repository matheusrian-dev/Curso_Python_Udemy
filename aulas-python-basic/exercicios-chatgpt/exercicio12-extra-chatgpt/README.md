🧩 Desafio Rápido: Calculadora Segura

Objetivo:
Criar um pequeno programa que receba dois números e uma operação (+, -, *, /) e retorne o resultado, tratando exceções de forma limpa e organizada.

🧠 Requisitos:

Crie três funções:

valida_numero(valor) → deve garantir que o valor informado seja int ou float.

Caso contrário, levante um TypeError com uma mensagem clara.

valida_operador(op) → deve garantir que o operador esteja entre ['+', '-', '*', '/'].

Caso contrário, levante um ValueError.

calcular(n1, n2, op) → deve chamar as duas funções acima e realizar o cálculo.

Se o operador for '/' e o divisor for zero, levante ZeroDivisionError.

No main, use try/except para:

Tratar esses três tipos de erro (TypeError, ValueError, ZeroDivisionError).

Mostrar mensagens amigáveis ao usuário.

O programa deve rodar uma única vez (não precisa de loop).

💡 Exemplo de execução:
Digite o primeiro número: 10
Digite o segundo número: 0
Digite a operação (+, -, *, /): /

Erro: Você está tentando dividir por zero.

Digite o primeiro número: 8
Digite o segundo número: 2
Digite a operação (+, -, *, /): *
Resultado: 16
