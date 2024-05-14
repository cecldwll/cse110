# Meal Price Calculator

cmeal = float(input('\nWhat is the price of a child\'s meal? '))
ameal = float(input('What is the price of an adult\'s meal? '))
child = int(input('How many children are there? '))
adult = int(input('How many adults are there? '))
tax = float(input('What is the sales tax rate? '))

subtotal = (cmeal * child) + (ameal * adult)
print(f'\nSubtotal: ${subtotal}')

