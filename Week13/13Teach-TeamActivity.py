# Areas of Shapes Revisited

import math
pi = math.pi

shape = ''

def compute_area_square(value):
    area_square = value * value
    return area_square

def compute_area_rectangle(lrectangle, wrectangle):
    area_rectangle = lrectangle * wrectangle
    return area_rectangle

def compute_area_circle(radius):
    area_circle = (radius ** 2) * pi
    return area_circle

while shape.lower() != 'quit':
    shape = input('\nWhat shape do you want to compute the area of? ')
    if shape.lower() == 'square':
        # SQUARE
        value = float(input('Length of the side of a square: '))
        square_area = compute_area_square(value)
        print(f'The area of the square is {square_area:.2f}')
    elif shape.lower() == 'rectangle':
        # RECTANGLE
        lrectangle = float(input('What is the length of the rectangle? '))
        wrectangle = float(input('What is the width of the rectangle? '))
        rectangle_area = compute_area_rectangle(lrectangle, wrectangle)
        print(f'The area of the rectangle is {rectangle_area:.2f}')
    elif shape.lower() == 'circle':
        # CIRCLE
        radius = float(input('What is the radius of the circle? '))
        circle_area = compute_area_circle(radius)
        print(f'The area of the circle is {circle_area:.2f}')

print()


'''
# Stretch Challenge Answers

import math

def compute_area_square(side):
    area = compute_area_rectangle(side, side)
    return area

def compute_area_rectangle(length, width):
    return length * width

def compute_area_circle(radius):
    return math.pi * radius * radius

def compute_area(shape, value1, value2=0):
    area = -1

    if shape == "square":
        area = compute_area_square(value1)
    elif shape == "circle":
        area = compute_area_circle(value1)
    elif shape == "rectangle":
        area = compute_area_rectangle(value1, value2)
    
    return area


# The main program starts here...
shape = ""

while shape != "quit":
    shape = input("What shape do you have? ")

    # Convert it to lower case once, so we don't have to keep converting it
    shape = shape.lower()

    if shape == "square":
        side = float(input("What is the length of the side? "))
        area = compute_area(shape, side)
        print(f"The area is {area}")
    elif shape == "rectangle":
        length = float(input("What is the length? "))
        width = float(input("What is the width? "))
        area = compute_area(shape, length, width)
        print(f"The area is {area}")
    elif shape == "circle":
        radius = float(input("What is the radius? "))
        area = compute_area(shape, radius)
        print(f"The area is {area}")

'''