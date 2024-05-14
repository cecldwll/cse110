# LOOPING THROUGH A LIST
items = ['crayon', 'scissors', 'paper', 'glitter glue', 'markers', 'pens']

for item in items:
    print(f'\nThe item is: {item}\n')

'''
The for loop syntax here is very clever. When you type for item in items:, the list variable, items must already exist, 
but the variable for each individual element of the list, in this case item, is defined right in that statement. 
In short, it's saying, "Go through each element of this list and assign a new variable item to be the value each time through.
'''


# LOOPING THROUGH NUMBERS
'''
Ways to Create Lists:

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
OR
numbers = range(10)
'''
# It is more common to just put the 'range' code right in your loop
for number in range(10):
    print(number)

# This loop will start with 100, and go up to, but not including 200
for i in range(100, 200):
    print(f'\n{i}')

# This loop will do the same thing, but this time, it will count by 10's
# The third value is used as a 'step size'
for i in range(100, 200, 10):
    print(f'\n{i}')


# LOOPS WITHIN LOOPS
for i in range(5):
    print(f'\n{i}')
    for j in range(10, 13):
        print(f'--{j}\n')


# LOOPING THROUGH STRINGS
first_name = 'Brigham'
for letter in first_name:
    print(f'The letter is: {letter}\n')


# ACCESSING LETTERS BY POSITION
first_name = 'Brigham'

# you can access a specific letter in a string by using the square brackets []
# !! Remember: the counts starts at 0 !!
fourth_letter = first_name[3]
print(f'{fourth_letter}\n') # outputs a 'g' on the screen


# ITERATING THROUGH EACH LETTER USING AN INDEX
word = 'book'
number_of_letters = 4

for index in range(number_of_letters):
    letter = word[index]
    print(f'Index: {index} Letter: {letter}')


# FINDING THE STRING LENGTH
# use the 'len' fuction
dog_name = input('\nWhat is your dog\'s name? ')
letter_count = len(dog_name)

print(f'Your dog\'s name has {letter_count} letters\n')


# COMBINING INDEXES AND LENGTHS
word = 'string'
number_of_letters = len(word) # Notice this can now work for any string

for index in range(number_of_letters):
    letter = word[index]
    print(f'Index: {index} Letter: {letter}')
print()


# PYTHON ENUMERATE
'''
Using a 'for' loop and the length of the string is a standard way to access both the index
and the letter. However, Python also has a way to access both of these variables directly
using a special function called 'enumerate'
'''
first_name = 'Brigham'

# Notice by using enumerate, we specify both i and letter
for i, letter in enumerate(first_name):
    print(f'The letter {letter} is at position {i}')
print()


# LOOPING WITH A CONDITION
names = ['Christoper', 'Susan']
index = 0
while index < len(names):
    print(names[index])
    # Change the condition
    index = index + 1


# MAKE SURE YOUR VARIABLES ARE DIFFERENT
# Bad Example (what not to do)
word = 'super'

print(word)
for word in word:
    print(word)
print(word)

print('done')

# ADDITIONAL CLASS NOTES
word = 'supers'

for letter in word:
    print(letter)

letter1 = word[0]
print(letter1)

for x in range(5):
    print(x)

print(len(word))
for i in range(len(word)):
    letter = word[i]
    print(f'{i} - {letter}')

x = 0
while x < len(word):
    letter = word[x]
    print(f'{x} - {letter}')
    x += 1 # same as x = x + 1

word1 = ''
word2 = ' '

while len(word1) != len(word2):
    word1 = input('What is the first word? ')
    word2 = input('What is the second word? ')

    if len(word1) != len(word2):
        print('The words must be the same length please try again.')

for i in range(len(word2)):
    print(f'{word1[i]}{word2[i]}', end='')
print()


print('done')

vowels = 'aeiou'
word = input('Give me a noun: ')

if word[0] in vowels:
    print(f'an {word}')
else:
    print(f'a {word}')