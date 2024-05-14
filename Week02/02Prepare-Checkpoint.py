# Formatting Strings

first = input('What is your first name?')
last = input('What is your last name?')
print(f'Your name is {last.capitalize()}, {first.capitalize()} {last.capitalize()}.')

'''
ALTERNATIVES:

print("Your name is " + last + ", " + first + " " + last + ".")
print("Your name is {}, {} {}.".format(last, first, last))
print("Your name is {0}, {1} {0}.".format(last, first))
'''