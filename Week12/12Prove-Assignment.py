# Data Analysis

lowest = 999999999999999999999999.9999999999
min = 99999999999999.99999999999
emin = 99999999999999.99999999999
highest = 0.00000
max = 0.000000
emax = 0.000000

year_choice = input('\nEnter the year of interest: ')
entity_choice = input('Enter a country of interest: ')

print()
with open('Week12/life-expectancy.csv') as dataset:
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

        # Year of Interest
        for i in range(len(year)):
            if year_choice == year[i]:
                average = sum(life_expectancy) / len(life_expectancy)

                for i in range(len(life_expectancy)):
                    interest_life_max = life_expectancy[i]
                    interest_entity_max = entity[i]
                    if max < interest_life_max:
                        max = interest_life_max
                        interest_max = interest_entity_max

                for i in range(len(life_expectancy)):
                    interest_life_min = life_expectancy[i]
                    interest_entity_min = entity[i]
                    if min > interest_life_min:
                        min = interest_life_min
                        interest_min = interest_entity_min

        # Entity of Interest
        for i in range(len(entity)):
            if entity_choice.lower() == entity[i].lower():
                eaverage = sum(life_expectancy) / len(life_expectancy)

                for i in range(len(life_expectancy)):
                    einterest_life_max = life_expectancy[i]
                    einterest_entity_max = entity[i]
                    if emax < einterest_life_max:
                        emax = einterest_life_max
                        einterest_max = einterest_entity_max

                for i in range(len(life_expectancy)):
                    einterest_life_min = life_expectancy[i]
                    einterest_entity_min = entity[i]
                    if emin > einterest_life_min:
                        emin = einterest_life_min
                        einterest_min = einterest_entity_min

    print(f'The overall max life expectancy is: {highest:.2f} from {high_entity} in {high_year}')
    print(f'The overall min life expectancy is: {lowest:.2f} from {low_entity} in {low_year}')

    print(f'\nFor the year: {year_choice}')
    print(f'The average life expectancy across all countries was {average:.2f}')
    print(f'The max life expectancy was in {interest_max} with {max:.2f}')
    print(f'The min life expectancy was in {interest_min} with {min:.2f}')
    
    print(f'\nFor the country: {entity_choice.title()}')
    print(f'The average life expectancy was {eaverage:.2f}')
    print(f'The max life expectancy was in {einterest_max} with {emax:.2f}')
    print(f'The min life expectancy was in {einterest_min} with {emin:.2f}')
print()