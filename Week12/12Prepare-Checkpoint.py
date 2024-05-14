# Finding Things in a List

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = 999
youngest_name = ''

for line in people:
    line = line.strip()
    parts = line.split()

    names = [parts[0]]
    ages = [int(parts[1])]

    for i in range(len(ages)):
        age_min = ages[i]
        name_min = names[i]
        
        if youngest_age > age_min:
            youngest_age = age_min
            youngest_name = name_min

print(f'{youngest_name} is the youngest and is {youngest_age} years old.')