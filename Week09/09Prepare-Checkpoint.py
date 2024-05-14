# Practicing Working With Lists

friends = []

name = ''
print()

while name.lower() != 'end':
    name = input('Type the name of a friend: ')
    friends.append(name)
print()

print('Your friends are:')
for friend in friends:
    if friend.lower() != 'end':
        print(f'{friend.capitalize()}')
    else:
        print()


'''
TEACHER'S VERSION:

friends = []

name = None

while name != 'end':
    name = input('TYpe the name of a friend: ')

    if name != 'end':
        friends.append(name)

print()
print('Your friends are:')

for friend in friends:
    print(friend)
'''