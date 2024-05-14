# ACCESSING ITEMS IN A LIST VIA THEIR INDEX
the_list = [
    'item1',
    'item2',
    'item2',
]

first = the_list[0] # gets the first item
second = the_list[1] # gets the second item

index = int(input('Which index would you like to get? '))
user_choice = the_list[index] # gets the item at the index the user typed


# FINDING THE SIZE OF THE LIST
books = [
    'Old Testament',
    'New Testament',
    'Book of Mormon',
    'Doctrine and Covenants',
    'Pearl of Great Price',
]

number_of_books = len(books) # len is short for length


# ITERATING THROUGH A LIST USING AN INDEX
for i in range(len(books)):
    book = books[i]
    print(book) # print each book to the screen


'''
A NOTE ABOUT VARIABLE NAMES:

It is common to use 'i' as the variable name when it comes to suing loops to iterate through numbers.
Then if you happen to have a second loop inside of it, it is common to use 'j' for that variable.
A third loop uses k. 

If you have more than 3 loops inside one another, typically you need to examine your code a little closer 
to see if there is a way to simplify your problem.
'''


# PRINTING INDEXES
for i in range(len(books)):
    book = books[i]
    print(f'{i}. {book}')


# WORKING WITH PARALLEL LISTS
names = []
numbers = []

# ...
# Code here that populates the two lists
# ...

for i in range(len(names)):
    name = names[i]
    number = numbers[i]

    print(f'{name} - {number}')
# Be very careful in cases like this that the two lists do not get out of sync


# REMOVING ITEMS FROM A LIST
# use the 'pop' function to pop the item out of the list

the_list.pop(3) # Removes the item at index 3
the_list.pop() # Removes the last item
# you tell the pop function the index of the item you want to remove. If you don't give an index, it will remove the last one

# When you remove an item from a certain index, all of the elements in the list that follow it will move up.
# (ex. If you remove the item at index 3, the item that was at index 4 will move to 3)
print()


# INDEXING WITH MULTIPLE LISTS
selections = [
    'water',
    'tots',
    'fries'
]

quantities = [
    2,
    4,
    4
]

selections.insert(1, 'salad')
quantities.insert(1, 1)

for i in range(len(selections)):
    print(f'{selections[i]} - {quantities[i]}')
print()