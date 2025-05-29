secret_word = 'ABACAXI'
lives = 6
MAX_LIVES = 6
game_won = False
game_lost = False
incorrect_guessed_letters = []
display_word = []

for letter in secret_word:
    display_word.append('_')

hangman_stages = ["""
             +---+
             |   |
                 |
                 |
                 |
                 |
          =========
          """,
          """
             +---+
             |   |
             O   |
                 |
                 |
                 |
          =========
          """,
          """
             +---+
             |   |
             O   |
             |   |
                 |
                 |
          =========
          """,
          """
             +---+
             |   |
             O   |
            /|   |
                 |
                 |
          =========
          """,
          """
             +---+
             |   |
             O   |
            /|\  |
                 |
                 |
          =========
          """,
          """
             +---+
             |   |
             O   |
            /|\  |
            /    |
                 |
          =========
          """,
          """
             +---+
             |   |
             O   |
            /|\  |
            / \  |
                 |
          =========
          """]

#funções Game
def input_player_guess():
    player_input = input('Digite uma letra: ')
    return player_input


def display_game_state(display_word, lives, incorrect_guessed_letters, hangman_stages):
    print(f"Palavra: {' '.join(display_word)}", '\r\n')

    print(f'Vidas Restantes: {lives}', '\r\n')

    print(f'Tentativas Incorretas: {', '.join(incorrect_guessed_letters)}', '\r\n')

    print(hangman_stages[MAX_LIVES - lives])
    
print('X===BEM=VINDO=AO=JOGO=DA=FORCA===X','\r\n')

display_game_state(display_word, lives, incorrect_guessed_letters, hangman_stages)

#Game Loop
while lives > 0 and not game_won:
    #Turno tentativa do jogador
    while True:
        player_input = input_player_guess()
        guess = player_input.upper()

        # checando se é 1 caracter somente
        if len(guess) != 1:
            print('Por favor, digite apenas uma letra!')
            continue  
        # checando se é uma letra do alfabeto
        if not guess.isalpha():
            print('Por favor, digite uma LETRA!(A-Z)') 
            continue   
        # checando se a letra já foi usada ou está em display_word
        if guess in incorrect_guessed_letters or guess in display_word:
            print(f'Você já usou a letra {guess}!')
            continue
        # a letra é válida, quebre o loop
        print(f'Você digitou {guess}!')
        break

    # checando se a letra está na palavra secreta    
    if guess in secret_word: #true
        print(f'Parabéns! {guess} está na palavra secreta!','\r\n')
        for index, letter_in_secret_word in enumerate(secret_word):
            if letter_in_secret_word == guess:
                display_word[index] = guess
    else:
        print(f'Desculpe, {guess} não está na plavra secreta!','\r\n')
        lives -= 1
        incorrect_guessed_letters.append(guess)

    #game board
    display_game_state(display_word, lives, incorrect_guessed_letters, hangman_stages)
    
    #verificação estado de derrota
    if lives == 0:
        game_lost = True
    
    #verificaçao da logica de vencer
    if '_' not in display_word:
        game_won = True
    
if game_won == True:
    print(f'Parabéns, Você Ganhou o Jogo! A Palavra era: {secret_word}! ')
    
else:
    print(f'Game Over! Você Foi Enforcado... A Palavra era: {secret_word}')
    
        