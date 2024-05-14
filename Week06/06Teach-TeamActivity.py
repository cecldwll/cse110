# Amusement Park Rides

ride = False
can_ride = 'Welcome to the ride. Please be safe and have fun!\n'
cannot_ride = 'Sorry you may not ride.\n'

age1 = int(input('\nWhat is the age of the first rider? '))
height1 = int(input('What is the height(in) of the first rider? '))

rider2 = input('Is there a second rider (yes/no)? ')

if rider2.lower() == 'yes':
    age2 = int(input('What is the age of the second rider? '))
    height2 = int(input('What is the height(in) of the second rider? '))

    if height1 < 36 or height2 < 36:
        ride = False
    else:
        if age1 >= 18 or age2 >= 18:
            ride = True
        else:
            if (age1 >= 12 and age1 <= 17) or (age2 >= 12 and age2 <= 17):
                golden_passport = input('Do any of the riders have a golden passport? (yes/no) ')
                if golden_passport.lower() == 'yes':
                    ride = True
                else:
                    if age1 >= 12 and age2 >= 12 and height1 >= 52 and height2 >= 52:
                        ride = True
                    elif (age1 >=14 and age2 >=16) or (age1 >= 16 and age2 >=14):
                        ride = True
                    else:
                        ride = False
            else:
                ride = False
else:
    if age1 >=18 and height1 >= 62:
        ride = True
    else:
        if age1 >= 12 and age1 <=17:
            golden_passport = input('Do you have a golden passport? (yes/no) ')
            if golden_passport.lower() == 'yes':
                ride = True
            else:
                ride = False

if ride:
    print(can_ride)
else:
    print(cannot_ride)