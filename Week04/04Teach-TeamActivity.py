# Speed of a Falling Object

'''
m = mass (kg)
g = acceleration due to gravity (9.8 m/s^2 on Earth, 24 m/s^2 on Jupiter)
t = time (seconds)
c = 1/2 p A C
p = density of fluid (1.3 kg/m^3 for air, 1000 kg/m^3 for water)
A = cross sectional area of projectile (square meters)
C = drag constant (0.5 for sphere, 1.1 for cylinder falling on it's side. You could look it up for other shapes)
exp = the number e(2.71828) to the given exponent. This can be computed in Python with the Math library function math.exp(value)
sqrt = the square root of the given expression. This can be computed in Python with the Math library function math.sqrt(value)
'''

print('\nWelcome to the velocity calculator. Please enter the following: \n')

import math

mass = float(input('Mass (in kg): '))
gravity = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))
time = float(input('Time (in seconds): '))
density = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
cross = float(input('Cross sectional area (in m^2): '))
drag = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))

c = (1 / 2) * density * cross * drag
print(f'\nThe inner value of c is: {c:.3f}')

velocity = math.sqrt((mass * gravity)/c) * (1 - math.exp((-math.sqrt(mass * gravity * c)/mass) * time))
print(f'The velocity after {time:.1f} seconds is: {velocity:.3f} m/s \n')

terminal_velocity = math.sqrt((mass * gravity) / c)
print(f'The terminal velocity would be {terminal_velocity:.3f} m/s\n')