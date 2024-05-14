# Positive Number
num = int(input('\nPlease type a positive number: '))

while num < 0:
    print('Sorry that is a negative number. Please try again.')
    num = int(input('Please type a positive number: '))

print(f'The number is: {num}\n')

# Candy
candy = input('May I have a piece of candy? ')

while candy.lower() == 'no':
    candy = input('May I have a piece of candy? ')

print('Thank you.\n')

# Candy (different solution)
answer = ''

while answer != 'yes':
    answer = input('May I have a piece of candy? ')

print('Thank you.')