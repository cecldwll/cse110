# READ
'''
file = open('sandbox.txt')

for line in file:
    print(line)

file.close()


with open('sandbox.txt') as file:

    header = file.readline()
    # print(header)

    for line in file:
        print(line)

print('done')

# SPLIT
text = 'My dog, loves fish'
parts = text.split(',')
# print(parts)


# STRIP
print(f'"{text}"')
print(f'"{text.strip()}"')


# USE BOTH SPILT AND STRIP
text = 'Fries, 2'
parts = text.split(',')

item = parts[0].strip()
qty = int(parts[1])
print(item)
print(qty * 2)
'''

# ALL TOGETHER, FILES, SPLIT, AND STRIP
with open('Week11/data.txt') as file:
    header = file.readline()
    h_parts = header.split(',')
    print(f'{h_parts[0]}: {h_parts[1].strip()}')

    for line in file:
        parts = line.strip().split(',')
        item = parts[0]
        qty = int(parts[1])

        print(f'{item}: {qty * 2}')