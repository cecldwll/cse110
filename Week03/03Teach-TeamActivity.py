import math
pi = math.pi

square = float(input('\nWhat is the length of a side of the square (in cm)? '))
square_area = square * square
print(f'The area for the square is: {float(square_area)} cm squared or {float(square_area * 0.01)} m squared.')
lrectangle = float(input('What is the length of the rectangle (in cm)? '))
wrectangle = float(input('What is the width of the rectangle (in cm)? '))
rectangle = lrectangle * wrectangle
print(f'The area of the rectangle is: {float(rectangle)} cm squared or {float(rectangle * 0.01)} m squared.')
radius = float(input('What is the radius of the circle (in cm)? '))
circle = (radius ** 2) * pi
print(f'The area of the circle is: {float(circle)} cm squared or {float(circle * 0.01)} m squared.\n')

value = float(input('\nEnter a number: '))
print('Using this value: ')
vsquare = value * value
print(f'The area of a square would be: {vsquare}')
vcircle = (value ** 2) * pi
print(f'The area of a circle would be: {vcircle}')
vcube = value ** 3
print(f'The volume of a cube would be: {vcube}')
vsphere = (value ** 2) * pi * 4
print(f'The area of a sphere would be: {vsphere}\n')