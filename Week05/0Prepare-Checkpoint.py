# Practicing If Statements

# Comparing Numbers
num1 = float(input('\nWhat is the first number? '))
num2 = float(input('What is the second number? '))

if num1 > num2:
    print('\nThe first number is greater.')
else:
    print('THe first number is not greater.')

if num1 == num2:
    print('The numbers are equal.')
else:
    print('The numbers are not equal.')

if num2 > num1:
    print('The second number is greater.')
else:
    print('The second number is not greater.')

# Comparing Strings
animal = input('\nWhat is your favorite animal? ')

if animal.lower() in ('ducks', 'duck'):
    print('\nThat\'s my favorite animal too!')
else:
    print('That one is not my favorite.\n')