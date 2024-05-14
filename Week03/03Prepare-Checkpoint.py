# Numeric Data Types

age = int(input('How old are you? '))
print(f'On your next birthday, you will be {age + 1}.')
print()

cartons = int(input('How many egg cartons do you have? '))
eggs = cartons * 12
print(f'You have {eggs} eggs.')
print()

cookies = int(input('How many cookies do you have? '))
people = int(input('How many people are there? '))
c_per_p = cookies / people
print(f'Each person may have {c_per_p} cookies.')
