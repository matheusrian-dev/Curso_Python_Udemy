"""
Fatiamento de strings
 012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna quantidade de caracteres da str
"""
variavel = 'Olá mundo' #lembre-se: espaço em branco ocupa um índice como qualquer outro caractere!
#print(variavel[5]) #índice positivo
#print(variavel[-4]) #índice negativo
print(variavel[4:8]) #obs.: o indice final não é exibido, então se quiser exibir até o indice 7, por exemplo,
                     #deve-se inserir o índice 8 como índice final
print(variavel[4:]) #inicia no índice 4 e vai até o final
print(variavel[:5]) #vai do início da string e exibe até o índice 4
print(variavel[0:len(variavel):1]) # inícia do índice 0, vai até o valor retornado na função len e o intervalo de
                                   # checagem é de 1, ou seja, ele não vai pular nenhum caractere
print(variavel[0:9:2]) # para exemplificar, com o intervalo 2, ele lê um caractere e pula outro
print(variavel[-1:-10:-1]) #exemplo da leitura da string invertida utilizando índices negativos