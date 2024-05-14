# Multiple Lists
bank_accounts = []
balances = []
account_name = ''

print('\nEnter the names and balances of the bank accounts (type: quit when done)')
while account_name.lower() != 'quit':
    account_name = input('What is the name of this account? ')
    if account_name.lower() != 'quit':
        money = float(input('What is the balance? '))
        bank_accounts.append(account_name)
        balances.append(money)

print()
print('Account Information: ')
for i in range(len(bank_accounts)):
    print(f'{i}. {bank_accounts[i].capitalize()} - ${balances[i]:.2f}')
print()

total = sum(balances)
average = total / len(balances)
highest_balance = 0
for i in range(len(balances)):
    if highest_balance < balances[i]:
        highest_balance = balances[i]
        largest = bank_accounts[i]

print(f'Total: ${total:.2f}')
print(f'Average: ${average:.2f}')
print(f'Highest Balance: {largest.capitalize()} - ${highest_balance}')

update = 'yes'
while update.lower() == 'yes':
    update = input('\nDo you want to update an account? ')
    if update.lower() == 'yes':
        updated_index = int(input('What account index do you want to update? '))
        updated_amount = float(input('What is the new amount? '))
        balances[updated_index] = updated_amount

    print('\nAccount Information: ')
    for i in range(len(bank_accounts)):
        print(f'{i}. {bank_accounts[i].capitalize()} - ${balances[i]:.2f}')

print()
