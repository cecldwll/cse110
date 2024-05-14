# Shopping Cart

print('\nWelcome to the Shopping Cart Program!')

cart_items = []
cart_prices = []
action = 0

while action != 5:
    # Action options
    print('\nPlease select one of the following:')
    print(
    '1. Add item \n'
    '2. View cart \n'
    '3. Remove item \n'
    '4. Compute total \n'
    '5. Quit'
    )
    action = int(input('Please enter an action: '))
    
    # 1. Add item
    if action == 1:
        item = input('\nWhat item would you like to add? ')
        cart_items.append(item)
        price = float(input(f'What is the price of \'{item}\'? '))
        cart_prices.append(price)
        print(f'\'{item}\' has been added to the cart.')
    
    # 2. View cart
    elif action == 2:
        print('\nThe contents of the shopping cart are: ')
        for goods in range(len(cart_items)):
            name = cart_items[goods]
            number = cart_prices[goods]
            list_num = goods + 1
            print(f'{list_num}. {name.capitalize()} - ${number:.2f}')
            
    # 3. Remove item
    elif action == 3:
        remove_item = int(input('\nWhat item would you like to remove (item #)? '))
        remove_index = remove_item - 1
        cart_items.pop(remove_index)
        cart_prices.pop(remove_index)
        print('Item removed.')
        
    # 4. Compute total
    elif action == 4:
        total = sum(cart_prices)
        count = len(cart_items)
        print(f'\nYou have {count} item(s) in your shopping cart.')
        print(f'The total price of the item(s) in the shopping cart is ${total:.2f}')
        pay = input('\nWould you like to check out now (yes/no)? ')
        if pay.lower() == 'yes':
            print('\n~~~ Continuing to Checkout ~~~\n')
            exit()
            
print('\nThank you. Goodbye.\n')