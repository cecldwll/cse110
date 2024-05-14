# Wordle

import random

random_words = ('peter', 'james', 'john', 'andrew', 'philip', 'judas', 'matthew', 'thomas', 'bartholomew', 'simon', 'mosiah', 'nephi', 'lehi', 'isaiah', 'noah')

secret = random.choice(random_words)
letternum = len(secret)
guess = ''
guess_num = 0
hint = '_ ' * len(secret)

print('\nWelcome to the word guessing game!')

print(f'\nYour hint is: {hint}')

while secret != guess:
    guess = input('\nWhat is your guess? ')
    guess = guess.lower()
    guess_num = guess_num + 1

    if len(secret) != len(guess):
        print('Sorry, the guess must have the same number of letters as the secret word.')

    elif secret != guess:
        print(f'\nYour hint is: ', end = '')
        for i in range(letternum):
            letter = secret[i]
            if guess[i] == letter:
                print(f"{guess[i].upper()} ", end="")
            elif guess[i] in secret:
                print(f"{guess[i].lower()} ", end="")
            else:
                print(f"_ ", end="")

print('\nCongratulations! You guessed it!')
print(f'It took you {guess_num} guesses.\n')
