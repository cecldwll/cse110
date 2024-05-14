# Loops

'''
There are two types of loops in python: 'while' loops and 'for' loops

    - 'while' loops continue while something is still true, or as long as it's true (or until it's no longer true)
'''

number = 0

# Keep looping as long as the number is less than 10
while number < 10:
    number = int(input('What is the number? '))

print('Finished with the loop.')

# Start with the number 1
number = 1

# Keep looping as long as the number is less than or equal to 5
while number <= 5:
    # Display the number
    print(f'The number is: {number}')

    # Update the number to be one more than it was
    number = number + 1

print('Finished with the loop.')

# --------------------------------------------------------------------------------------------------------------------

# Declaring Variables Before They are Used

'''
BAD EXAMPLE: This code does not define a value for the number before it is used

while number < 10: # ERROR: number is not defined yet
    number = int(input('What is the number? '))

print('Finished with the loop.')
'''

# GOOD EXAMPLE: This code correctly sets the variable to a value before it is used

number = 0

while number < 10:
    number = int(input('What is the number? '))

print('Finished with the loop.')

'''
BAD EXAMPLE: This code ssets the variable to a number that prevents the code from ever entering the loop

number = 25 # ERROR: This number is greater than 10, so the loop will not run

while number < 10: # This body of this loop will NEVER run
    number = int(input('What is the number? '))

    print('Finished with the loop')
'''

# OK EXAMPLE: This code sets the variable to a number that allows the loop to run
# But it is not great, because it sets it to a non-standard value of 6

number = 6 # This number is less than 10, so the loop will run, but it is not standard

while number < 10: # This body of this loop will run just fine
    number = int(input('What is the number? '))

print('Finished the loop.')

# GOOD EXAMPLE: This code sets the variable to a number that allows the loop to run
# It uses a standard initialization value of 0.

number = 0 # This number is less than 10, and is a standard value (-1 is also a common number to use)

while number < 10: # This body of this loop will run just fine
    number = int(input('What is the number? '))

print('Finished with the loop.')

# --------------------------------------------------------------------------------------------------------------------

# Variable Scope

'''
BAD EXAMPLE: This code uses the variable 'name' outside the loop where it was declared

number = 0

while number < 10:
    number = int(input('What is the number? '))
    name = input('What is your name?')

print(f'Your name is: {name}')
'''

# GOOD EXAMPLE: This code first declares the variable 'name' before the loop so that it can be used afterward

number = 0
name = ''

while number < 10:
    number = int(input('What is the number? '))
    name = input('What is your name?')

print(f'Your name is: {name}')

# --------------------------------------------------------------------------------------------------------------------

tip = float(input('What is the tip amount? '))

while tip < 0:
    print('Sorry, the tip cannot be negative.')
    tip = float(input('What is the tip amount? '))
    # Jump back to line 114

print(f'You have tipped an amount of ${tip:.2f}')

