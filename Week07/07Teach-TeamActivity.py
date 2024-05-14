# Guess My Number Game

import random

guess_num = 0
repeat = True

while repeat:
    number = random.randint(1, 10)
    guess = 0
    while number != guess:
        guess = int(input('\nWhat is your guess? '))
        guess_num = guess_num + 1
        if number < guess:
            print('Lower')
        elif number > guess:
            print('Higher')
    
    print('\nYou guessed it.')
    print(f'It took you {guess_num} guesses.')

    repeat_string = input('\nWould you like to continue the game? (yes/no) ')
    if repeat_string.lower() == 'no':
        repeat = False
    elif repeat_string.lower() == 'yes':
        repeat = True
