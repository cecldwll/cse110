fav_num = int((input('What is your favorite number? ')))
sum = 0

for i in range(0, fav_num + 1):
    sum = sum + i

print(f'The sum of the numbers from 0 to {fav_num} is: {sum}')