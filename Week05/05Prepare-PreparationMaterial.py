# Conditional Logic
price = float(input('Price: $'))

if price >= 1.00:
    tax = .07
    print(tax)
else:
    tax = 0
    print(tax)

if price >= 1.00:
    tax = .07
else:
    tax = 0
print(tax)

'''
>    greater than
<    less than
>=   greater than or equal to
<=   less than or equal to
==   is equal to
!=   is not equal to
'''

# string comparisons are case sensitive
country = 'CANADA'
if country.lower() == 'canada':
    print('Oh look a Canadian')
else:
    print('You are not from Canada')


# Handling Multiple Conditions
province = input('What province are you in? ')
if province == 'Alberta'\
    or province == 'Nunavut':
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15
print(tax)

# How OR statements are processed
'''
FC = First Condition
SC = Second Contition
C = Condition Evaluates as

FC = True  + SC = True  = C = True
FC = True  + SC = False = C = True
FC = False + SC = True  = C = True
FC = False + SC = False = C = False
'''

# If you have a list of possible values to check, you can use the IN operator
if province in ('Alberta', \
                'Nunavut', 'Yukon'):
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15
print(tax)

# If an action depends on a combination of conditions, you can nest if statements
country = input('What country are you from? ')

if country.capitalize() == 'Canada':
    province = input('What province are you from? ')
    if province.capitalize() in ('Alberta', \
                'Nunavut', 'Yukon'):
        tax = 0.05
    elif province.capitalize() == 'Ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0.0
print(tax)

# = is assigning a value to a variable, == is used to check if two variables are equal

# Running Decision Maker

print('Welcome to the running decision maker!\n')

is_snowing = input('Is it snowing outside? ')

if is_snowing.lower() == 'yes':
    print('DONT\'T DO IT!')
else:
    temp = float(input('What is the temperature outside? (F) '))

    if temp > 67:
        print('You REALLY should go running!')
    elif temp > 50:
        is_raining = input('Is it raining? ')
        if is_raining.lower() == 'yes':
            print('DON\'T DO IT!')
        else:
            print('You REALLY should go running!')
    else:
        print('DON\'T DO IT!')
    # print('\nYou REALLY should go running!')

print('done')