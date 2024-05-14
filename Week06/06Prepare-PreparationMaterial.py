# Complex Condition Checks

# TESTING MULTIPLE CONDITIONS
x = 6
y = 12
word = 'taco'

if x > 5 and y > 10:
    # This happens if both conditions are true
    print()
else:
    print()

if x > 5 or y > 10:
    # THis happens if either one of the conditions (or both!) are true
    print()
else:
    print()

# You can mix and match any expressions that evaluate to true:
if x > 5 and y > 10 and word == 'taco':
    # This happens if all three conditions are true
    print()
else:
    print()

# the 'and' condition takes precendence over the 'or' condition
# if you want to mix them and have the 'or' condition happen first, you need to use parentheses:
if (x > 5 or x < -5) and y > 10:
    # In this case, x can either be greater than 5 or less than negative 5, and y must always be greater than 10
    print()
else:
    print()

if x > 5 or x < -5 and y > 10:
    # Without parentheses, the x < -5 and y >10 conditions go together and both must be true, unless x >5, in which case the whole statement is true
    print()
else:
    print()

# TESTING MULTIPLE SIMILAR CONDITIONS
x = 6
first_name = 'Bob'
last_name = 'Scott'

# To check if x is either 5 or 6, you might be tempted to write:
if x == 5 or 6:
    # INCORRECT: This does not work!
    print()
else:
    print()

# You must write them both out:
if x == 5 or x == 6:
    # This is the correct way to check
    print()
else:
    print()

# To check if either first_name or last_name is Scott you might be tempted to write:
if first_name or last_name == 'Scott':
    # INCORRECT: This does not work!
    print()
else:
    print()

# You must write them both out:
if first_name == 'Scott' or last_name == 'Scott':
    # This is the correct way to check
    print()
else:
    print()

# TRUE AND FALSE VALUES

# Variables that are either true or false are a new data type called Boolean Variables

# Must use a capital T on True and a capital F on False
is_hot = True

# You can check the value of the variable directly
if is_hot:
    print('It\'s hot')
else:
    print()

# It works, but is redundant (and therefore bad practice) to check if it is True:
if is_hot == True:
    print('It\'s hot')
else:
    print()

# You can check if a boolean variable is not ture with the 'not' keyword
is_hot = True

# Using the 'not' keyword
if not is_hot:
    print('It is not hot')
else:
    print()

# It works, but is generally avoided to check if it is false:
if is_hot == False:
    print('It is not hot')
else:
    print()

'''
Boolean variables are typically named with words that indicate that it will only have two values, and help you understand what true means.
For example, if you want to have a boolean variable that determines whether someone is an adult, you would typically choose a name of 'is_adult'
rather than 'age' or even 'adult'

Common boolean variable names are 'is_xxx', 'has_xxx', 'can_xxx', etc
'''

'''
How 'and' statements are processed:

First Condition     Second Condition     Condition Evaluates as
True                True                 True
True                False                False
False               True                 False
False               False                False
'''