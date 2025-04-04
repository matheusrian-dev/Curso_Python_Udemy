# Entendendo o fluxo do interpretador em condicionais

condicao = False
condicao1 = False
condicao2 = False
condicao3 = False

if condicao: #exemplo de breakpoint. Observação: breakpoints em comentários não funcionam já que os comentários são ignorados ao ler o código.
    print('Condição 1 concluída')
elif condicao1:
    print('Condição 2 concluída')
elif condicao2:
    print('Condição 3 foi concluída')
elif condicao3:
    print('condição 4 foi concluída')
else:
    print('Nenhuma condição foi concluída')

if 10 == 10:
    print('Outro if')

    
print('Fora do if')