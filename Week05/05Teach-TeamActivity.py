# Grade Calculator

grade = float(input('\nWhat is your grade percentage? '))

'''
if grade >= 90:
    print('You have an A!')
    print('Congrats! You have passed the class!')
elif grade >= 80:
    print('You have a B.')
    print('Congrats! You have passed the class!')
elif grade >= 70:
    print('You have a C.')
    print('Congrats! You have passed the class!')
elif grade >=60:
    print('You have a D.')
    print('You have failed the class. Better luck next time!')
else:
    print('You have an F.')
    print('You have failed the class. Better luck next time!')

if letter in ('A', 'B', 'C'):
    print('You have passed the class! CONGRATS!')
else:
    print('You have failed the class. Better luck next time!\n')
'''

if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >=60:
    letter = 'D'
else:
    letter = 'F'

if grade <= 59:
    letter = letter 
elif (grade % 10) < 3:
    letter = letter + '-'
elif grade > 93:
    letter = letter
elif (grade % 10) >= 7:
    letter = letter + '+'

print(f'\nGrade: {letter}')

if grade >= 70:
    print('You have passed the class! CONGRATS!\n')
else:
    print('You have failed the class. Better luck next time!\n')
