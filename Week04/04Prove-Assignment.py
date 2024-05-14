# Meal Price Calculator

cmeal = float(input('\nWhat is the price of a child\'s meal? '))
ameal = float(input('What is the price of an adult\'s meal? '))
drink_price = float(input('What is the price of the drinks? '))
child = int(input('How many children are there? '))
adult = int(input('How many adults are there? '))
drinks = int(input('How many drinks do you want? '))
tax = float(input('What is the sales tax rate? '))

subtotal = (cmeal * child) + (ameal * adult) + (drink_price * drinks)
print(f'\nSubtotal: ${subtotal:.2f}')

sales_tax = (subtotal * tax) / 100
print(f'Sales Tax: ${sales_tax:.2f}')

total = subtotal + sales_tax
print(f'Total: ${total:.2f}')

tip = float(input('\nHow much would you like to tip? '))

final_total = total + tip
print(f'\nFinal Total: ${final_total:.2f}')

payment = float(input('\nWhat is the payment amount? '))
change = payment - final_total
print(f'Change: ${change:.2f}\n')

print('---------------------------------------------------')
print('\nTHANK YOU FOR CHOOSING OUR RESTAURANT!')

print(f'\nSubtotal: ${subtotal:.2f}')
print(f'Sales Tax: ${sales_tax:.2f}')
print(f'Total: ${total:.2f}')
print(f'\nTip: ${tip:.2f}')
print(f'\nFinal Total: ${final_total:.2f}')
print(f'\nPayment: ${payment:.2f}')
print(f'Change: ${change:.2f}\n')

print('HAVE A GOOD DAY!\n')
print('---------------------------------------------------')