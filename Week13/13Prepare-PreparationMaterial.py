# Basics of Functions

# DEFINING FUNCTIONS
def your_function_name():
    # code here
    # for the
    # body of the function
    print()


# CALLING FUNCTIONS
# you can call the function by giving its name and including parentheses
your_function_name()


# EXAMPLE ^^
# first define the function
def print_message():
    print('Hello CSE 110 World!')

# call the function now
print_message() # Output: 'Hello CSE 110 World!'

# call it again here
print_message() # Output: 'Hello CSE 110 World!'


# PASSING PARAMETERS TO FUNCTIONS
# when you define a function, you can declare parameters
# parameters are values that it receives from the place that called it
def print_double(value):
    double_value = value * 2
    print(double_value)

print_double(12) # Output: '24'
print_double(3) # Output: '6'
print_double(42) # Output: '84'


# RETURNING VALUES
# the program will calculate and then return it instead of printing it
def get_double(value):
    double_value = value * 2
    return double_value

new_number = get_double(4) # the variable new_number would now have the value 8


# VARIABLE SCOPE
# variable names are only valid for the function they are defined in
def get_double(value):
    double_value = value * 2
    return double_value

new_number = get_double(4)

# ERROR: This does not work, because the variable 'double_value' is only alive during the body
# of the function. DOwn here, we have chosen to give the return value the name 'new_number'
# print(double_value) # BAD CODE

# the same concept holds true for parameters:
def print_message(the_message):
    print(the_message)

# it works just fine to use the same variable name as the function did...
the_message = 'Message 1'
print_message(the_message)

# but it so works to use a different variable...
user_message = 'Message 2'
print_message(user_message)


# STYLE
# most variables refer to things so it is most common to use nouns for them
# for example: price, name, response, etc

# functions do things or perform actions so it is more common to use verbs for their names
# for example: print_message, get_initials, open_file, display_error, etc


# Video Notes~~~

# INTRODUCING FUNCTIONS
# use functions instead of repeating code

'''
REPEATING CODE EX:

import datetime
# print timestamps to see how long sections take to run 

first_name = 'Susan'
print('task completed')
print(datetime.datetime.now())
print()

for x in range (0,10):
    print(x)
print('task completed')
print(datetime.datetime.now())
print()
'''
import datetime
# print the current time
def print_time():
    print('task completed')
    print(datetime.datetime.now())
    print()

first_name = 'Susan'
print_time()

for x in range(0,10):
    print(x)
print_time()

# Watch videos for more:
# https://www.youtube.com/watch?v=nrCAxXfRU28&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=30
# https://www.youtube.com/watch?v=sKW-zdYZNX4&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=32
