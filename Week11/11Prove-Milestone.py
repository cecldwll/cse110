# Analyzing Life Expectancy Data

lowest = 999999999999999999999999.9999999999
highest = 0.00000

print()
with open('Week11/life-expectancy.csv') as dataset:
    header = dataset.readline()
    
    for line in dataset:
        parts = line.strip().split(',')

        entity = [parts[0]]
        code = [parts[1]]
        year = [parts[2]]
        life_expectancy = [float(parts[3])]

        for i in range(len(life_expectancy)):
            life_max = life_expectancy[i]
            entity_max = entity[i]
            year_max = year[i]
            if highest < life_max:
                highest = life_max
                high_entity = entity_max
                high_year = year_max
        
        for i in range(len(life_expectancy)):
            life_min = life_expectancy[i]
            entity_min = entity[i]
            year_min = year[i]
            if lowest > life_min:
                lowest = life_min
                low_entity = entity_min
                low_year = year_min

    print(f'The overall max life expectancy is: {highest} from {high_entity} in {high_year}')
    print(f'The overall min life expectancy is: {lowest} from {low_entity} in {low_year}')

print()