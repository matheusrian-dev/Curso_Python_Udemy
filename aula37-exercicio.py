"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra;
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta;
- Se a letra digitada estiver na palavra secreta, exiba a letra;
- Se a letra digitada não estiver na palavra secreta, exiba *.
Faça a contagem de tentativas do seu usuário.
"""
import os
play_again = True
while play_again:
    secret_word = 'betrayed'
    word_not_found = True
    number_of_tries = 0
    correct_letter = ''
    while word_not_found:
    
        letter_passed = input('Digite uma letra: ').lower() #utilizando o lower para caso o usuário insira uma letra maiúscula
    
        if len(letter_passed) != 1: # verifica se o usuário digito apenas e pelo menos uma letra.
            print('Digite uma letra apenas.')
            continue
    
        if letter_passed in secret_word: # verifica se a letra digitada está na palavra secreta, caso esteja, insere a mesma no grupo de
            correct_letter += letter_passed # letras corretas
        
        guessed_word = '' # palavra temporária que será exibida para o usuário enquanto está tentando acertar
        for secret_letter in secret_word: # loop que percorre a palavra secreta verificando em qual index cada letra correta se encaixa
            if secret_letter in correct_letter:
                guessed_word += secret_letter
            else:
                guessed_word += '*' # caso nenhuma letra coincida com as acertadas, insere um * no index para manter a ordem da palavra.
    
        print(guessed_word)
    
        number_of_tries += 1
        if guessed_word == secret_word:
            word_not_found = False
            continue

    os.system('cls')
    print(f'Parabéns você encontrou a palavra secreta!')
    print(f'Palavra secreta: {secret_word}')
    print(f'Quantidade de tentativas até obter a resposta correta: {number_of_tries}')
    answer = input('Gostaria de jogar novamente? S para sim e qualquer outra tecla para não: ')
    play_again_answer = answer.lower()
    if play_again_answer != 's':
        play_again = False
