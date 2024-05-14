# Numbers can be stored in variables
pi = 3.14159
print(pi)


'''
Doing Math

+  =  Addition
-  =  Subtraction
*  =  Multiplication
/  =  Division
// =  Divide and drop remainder
%  =  Remainder or Modulus
** =  Exponent
'''

# If you combine strings with numbers, Python gets confused
# days_in_feb = 28
# print(days_in_feb + ' days in February')
days_in_feb = 28
print(str(days_in_feb) + ' days in February')


# This creates a new integer variable with the value of 10
# There is nothing magical about the "_num" in the variable name, it will just
# help us keep track of it
length_num = 50
width_num = 10

# If you add the numbers together, you would get the result you expect:
print(length_num + width_num) # This displays: 60

# You can convert the values to the strings "50" and "10" like this:
length_string = str(length_num)
width_string = str(width_num)

# The computer now thinks of these variable as two characters, the digit 5 followed
# by the digit 0, and the digit 1 followed by the digit 0.

# If you try to add the two strings together, it will concatenate them, or display
# one after the other:
print(length_string + width_string) # This displays: 5010

# Numbers stored as strings must be converted to numeric values before doing math
first_num = input('Enter first number ' )
second_num = input('Enter second number ')
print(int(first_num) + int(second_num))
print(float(first_num) + float(second_num))

# Using two lines:
people_string = input("How many people are in the room? ")
people_number = int(people_string)

# Using one line:
people_number = int(input("How many people are in the room? "))