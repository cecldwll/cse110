# List of Numbers

numbers = []
num = 1

print('Enter a list of numbers, type 0 when finished.')

while num != 0:
    num = int(input('Enter number: '))
    numbers.append(num)

sum = 0

for num in numbers:
    sum += num
print(f'The sum is: {sum:.2f}')

count = len(numbers)
average = sum / count
print(f'The average is: {average:.2f}')

largest = numbers[0]
for i in range(len(numbers)):
    if largest < numbers[i]:
        largest = numbers[i]
print(f'The largest number is: {largest:.2f}')


smallest_positive_num = 999999999999999999999

for number in numbers:
    if number > 0 and number < smallest_positive_num:
        smallest_positive_num = number
print(f'The smallest positive number is: {smallest_positive_num:.2f}')

sort_numbers = [sorted(numbers)]
print('The sorted list is: ')
for sorted_num in sort_numbers:
    print(sorted_num)