def computeTithing(amount):
    # amount = float(input('How much money to pay tithing on? '))
    tithe = amount * 0.1
    # print(f'Tithing for ${amount:.2f} is ${tithe:.2f}') # Function shouldn't care how to display result
    return tithe

# money = 100
money = float(input('How much money to pay tithing on? '))
tithing = computeTithing(money)
print(f'Tithing for {money} is ${tithing:.2f}')


def ask_yes_no(prompt, affirmative = 'y', negative = 'n'):
    # response = ''
    #while response != affirmative and response != negative:
    response = input(prompt + f' ({affirmative}/{negative}) ')
    if response.lower() == affirmative:
        return True
    elif response.lower() == negative:
        return False
    else:
        print(f'Please only type {affirmative} or {negative}')
        return ask_yes_no(prompt, affirmative, negative)

print('Welcone to the running decision maker!')
is_snowing = ask_yes_no('Is it snowing outside? ', 'y', 'no')

if is_snowing:
    print('DON\'T DO IT!')
else:
    temp = float(input('What is the temperature outside? '))

    is_raining = ask_yes_no('Is it raining? ')

    if temp > 50 or is_raining or is_snowing:
        print('Don\'t do it.')

    else:
        print('You should go running.')

print('done')