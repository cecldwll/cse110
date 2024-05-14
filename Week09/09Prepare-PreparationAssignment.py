# CREATING LISTS
'''
- Lists are collections of variables
- To declare a list, use the square brackets []
'''
movies = ['Toy Story', 'Pride and Prejudice', 'Star Wars']
quiz_scores = [89.2, 78.5, 92.4, 93.8]
# you can mix types of variales in a list, but that is harder to work with so it is discouraged

# it is recommended to give list variables plural names
'''
While you can just use [], you can also use the longer form using the keyword 'list()'
for example: movies = list()
'''

# Avoid using list as your variable name like this:
list = [] # BAD EXAMPLE


# ADDING ITEMS TO A LIST
books = []

books.append('1 Nephi')
books.append('2 Nephi')
books.append('Jacob')
books.append('Enos')


# ITERATING THROUGH EACH ITEM IN A LIST
print('Your books are: ')

for book in books:
    print(book)


# WORKING WITH LISTS OF NUMBERS
receipts = [12.24, 18.50, 4.99, 21.75]

running_total = 0

for receipt in receipts:
    running_total += receipt

# Display the total
print(f'The total is {running_total:.2f}') # This displays: The total is: 57.48


# APPENDING WITH INPUT
clients = []

new_client = ''
while new_client.lower() != 'quit':
    new_client = input('What is the name of a client? ')
    clients.append(new_client)

for client in clients:
    print(client)


# IN CLASS LESSON

# Review from Last Week
word = 'words'

print(word[3])
print(word[2])
print(word[1])
print(word[0])

print()
for i in range(len(word)):
    print(f'{i} - {word[i]}')

# New Material
movies = [
    'Batman Begins',
    'Dune',
    'Reign of Fire',
    # 'La La Land'
]

movies.append('Iron Man')

print('Movie List: ')
for i in range(len(movies)):
    print(f'- {movies[i]}')
print()


# other options/styles
books = list()
books.append('Lord of the Rings')
print(books)


# Fast Fod Menu

selection = 0
menu = [
    '1 - Drinks',
    '2 - Sides',
    '3 - Entrees',
    '4 - Order Complete'
]

drinks = ['Water', 'Root Beer', 'Guarana']
sides = ['fries', 'nachos', 'salads']
selections = []

while selection != 4:
    print('What would you like to order? ')
    for item in menu:
        print(item)
    selection = int(input('Enter the item you would like to order (1-3): '))
    
    # Drinks
    if selection == 1:
        print('Drinks options are: ')
        for drink in drinks:
            print(f'- {drink}')
        drink_selection = input('What would you like to drink? ')
        selections.append(drink_selection)
    
    # Sides
    elif selection == 2:
        print('Side options are: ')
        for side in sides:
            print(f'- {side}')
        side_selection = input('What would you like for a side? ')
        selections.append(side_selection)

print()
print(selections)