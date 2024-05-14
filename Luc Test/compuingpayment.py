borrowed = int(input('Amount borrowed: '))
interest_rate = float(input('Interest rate: '))
num_of_payments = int(input('Number of payments: '))

payment_amount = (borrowed * interest_rate) / (1 - (1 + interest_rate) ** (-num_of_payments))

print(f'Payment amount: {payment_amount:.2f}')