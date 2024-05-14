# List Indexes
shopping_list = []
item = ''

print('\nPlease enter the items of the shopping list (type \'quit\' to finish):')
while item.lower() != 'quit':
    item = input('Item: ')
    if item.lower() != 'quit':
        shopping_list.append(item)

print('\nThe shopping list is:')
for goods in shopping_list:
    print(goods.capitalize())

print('\nThe shopping list with indexes is:')
for i in range(len(shopping_list)):
    goods = shopping_list[i]
    print(f'{i}. {goods.capitalize()}')

change = int(input('\nWhat item would you like to change? '))
new_item = input('What is the new item? ')
shopping_list[change] = new_item

print('\nThe shopping list with indexes is:')
for i in range(len(shopping_list)):
    goods = shopping_list[i]
    print(f'{i}. {goods.capitalize()}')
print()