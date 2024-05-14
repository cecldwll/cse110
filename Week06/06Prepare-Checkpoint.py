# Qualifying for a Loan

print('\nPlease give a rating from 1 - 10 for the following prompts. (1 being bad/small and 10 being good/large): ')
loan_size = int(input('How large is the loan? '))
credit = int(input('How good is your credit history? '))
income = int(input('How high is your income? '))
down_payment = int(input('How large is your down payment? '))

loan = False

if loan_size >= 5:
    if credit >= 7 and income >= 7:
        loan = True
    elif credit >= 7 or income >= 7:
        if down_payment >= 5:
            loan = True
        else:
            loan = False
    else:
        loan = False
else:
    if credit < 4:
        loan = False
    else:
        if income >= 7 or down_payment >= 7:
            loan = True
        elif income >= 4 and down_payment >=4:
            loan = True
        else:
            loan = False

if loan:
    print(f'\nLoan Size: {loan_size}, Credit: {credit}, Income: {income}, Down Payment: {down_payment}, Decision: \'YES\'\n')
else:
    print(f'\nLoan Size: {loan_size}, Credit: {credit}, Income: {income}, Down Payment: {down_payment}, Decision: \'NO\'\n')