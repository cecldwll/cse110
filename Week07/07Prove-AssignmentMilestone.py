# Interactive Word Puzzle Game

secret = 'mosiah'
guess = ''
guess_num = 0

print('\nWelcome to the word guessing game!')

while secret != guess:
    guess = input('\nWhat is your guess? ')
    guess_num = guess_num + 1
    if secret != guess:
        print('Your guess was not correct.')

print('\nCongratulations! You guessed it!')
print(f'It took you {guess_num} guesses.\n')