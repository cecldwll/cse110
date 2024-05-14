# Shopping Cart
# add items, remove items, view contents, and see the total

print('\nWelcome to the Shopping Cart Program!\n')

cart_items = []
cart_prices = []
action = 0

while action != 5:
    # Action options
    print('\nPlease select one of the following:')
    print(
    '1. Add item \n'
    '3. Remove item \n'
    '4. Compute total \n'
    '5. Quit'
    )
    action = int(input('Please enter an action: '))
    
    # 1. Add item
    if action == 1:
        item = input('\nWhat item would you like to add? ')
        cart_items.append(item)
        print(f'\'{item}\' has been added to the cart.')
    
    # 2. View cart
    elif action == 2:
        print('\nThe contents of the shopping cart are: ')
        for goods in range(len(cart_items)):
            print(f'{cart_items[goods]}')
            
    # 3. Remove item
    elif action == 3:
        print('Remove item')
        
    # 4. Compute total
    elif action == 4:
        print('Compute total')
        

print('\nThank you. Goodbye.')