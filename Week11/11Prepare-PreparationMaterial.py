# OPENING FILES
open('filename.py')

# It is important to close the file; use the 'with' syntax
with open('filename.py') as file_variable:
    # Code to do someting with the file goes here
    print()
print('The file is closed now.')

# If you want a file to be saved into a variable, use the following:
with open('colors.txt') as color_file:
    # Code to do something with the color file goes here
    print()


# READING DATA FROM FILES
with open('colors.txt') as color_file:
    for line in color_file:
        # Code to do something with each line goes here
        print()


# PARSING STRINGS
old_line = 'this is here so there aren\'t code errors in my notes'
clean_line = old_line.strip()
# Removing extra whitespace

sentence = 'I will go and do'
words = sentence.split(' ') # You can use something other than a space to separate pieces of the string; ex. .split(',')
# The variable 'word's is now a list that contains each word.

# You can iterate through each word and do something with it, such as display it:
for word in words:
    print(word)


'''
VIDEO NOTES ~~~~~~~~~~~~~~~
'''
# SPLITTING STRINGS
colors = 'red green blue yellow'

color_parts = colors.split()
# color_parts = ['red', 'green', 'blue', 'yellow']

print(colors)
print(color_parts)

for color in color_parts:
    print(color)

second = color_parts[1]
print(second)


# REMOVING WHITESPACE
name = '\       Caitlyn Caldwell     \n'

# clean_name = name.strip()
name = name.strip()

print(f'---{name}---')
# print(f'---{clean_name}---')


# READING FILES AND PARSING STRINGS
with open('Week11\courses.txt') as courses_file:
    for line in courses_file:
        # line = 'CSE, 110,98.5'
        line = line.strip()

        parts = line.split(',')

        # parts = ['CSE 110', '98.5']
        name = parts[0]
        grade = float(parts[1])

        bonus_grade = grade + 3

        print(f'{name} - Grade: {grade}, after bonus: {bonus_grade}')

