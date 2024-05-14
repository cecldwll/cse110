# Using Format Strings
car_count = 3
print(f'There are {car_count} cars on the road.')
print('There are {} cars on the road.'.format(car_count))

# https://docs.python.org/3/library/string.html

'''
Defining the Number of Decimals to Display

    - Put :.2f after the variable name
        - the colon (:) indicates that you are going to specify how to format it
        - the period (.) indicates that you are setting the precision or number of decimal places
        - the number (in this case 2) indicates that you would like that number of decimal places to be displayed
        - the f indicates that you want fixed-point notation

'''
cars = 3
people = 8
people_per_car = people / cars

print(f'There are {people_per_car:.1f} people in each car.')
print(f'There are {people_per_car:.2f} people in each car.')
print(f'There are {people_per_car:.3f} people in each car.')

# Scientific Notation
# using e indicates that you are using exponent notation
distance = 9 * 1205 * 18
print(f'The distance is: {distance:.3e} meters.')
print(f'The distance is: {distance:.6e} meters.')

# Thousands Grouping
# display it with commas (:,) or underscores (:_)
big_number = 123456789
print(f'The number is: {big_number}')
print(f'The number is: {big_number:,}')
print(f'The number is: {big_number:_}')

# Using the Math Library
# https://docs.python.org/3/library/math.html
import math
radius = 5
area = math.pi * (radius ** 2)
print(f'The area is: {area}')

'''
math.ceil(value)  = rounds value up to the next whole number, the 'ceiling'
math.floor(value) = rounds value down to the next whole number
math.exp(value)   = raises e to the power of value
math.sin(value)   = computes the trigonometry sine function of value in radians
'''

# Rounding
import math

num = 2.345
num_rounded = round(num, 2)

print(f'{num:.2f}')
print(num_rounded)
print(math.ceil(num))
print(math.floor(num))
print(math.ceil(num * 10) / 10)

# Placements
num = 2.5
print(f'Your number is: "{num:<25}"')
print(f'Your number is: "{num:>25}"')
print(f'Your number is: "{num:^25}"')


# Code to calculate commission on product sales
price = float(input('What was the sale price? '))
commission_rate = float(input('What was the commission (%)?'))
commission = price * commission_rate / 100

print(f'The sales man earned a commission of ${commission:,.2f}')