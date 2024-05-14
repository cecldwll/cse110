# Iterating Through Strings

print()

word = "commitment"
number_of_letters = 10
favorite_letter = input("What is your favorite letter? ")

for index in range (number_of_letters):
    letter = word[index]
    if letter == favorite_letter:
        print(f"{letter.lower()}", end="")
    else:
        print(f"_", end="")

print()

quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
letternum = 148
repeat = True

while repeat == True:
    num = int(input("Please enter a number: "))

    for index in range (letternum):
        letter = quote[index]
        if index%num == 0:
            print(f"{letter.upper()}", end="")
        else:
            print(f"{letter.lower()}", end="")
    
    print()
    repeat_question = input('Would you like to enter another number (yes/no)? ')
    if repeat_question.lower() == 'yes':
        repeat = True
    else:
        repeat = False
print()