
# MODIFYING STRINGS

sentence = 'the cat IN THE hat'
print(sentence)
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('t'))
print(sentence.lower().count('t'))

# CUSTOM STRING FORMATING

first_name = 'Caitlyn'
last_name = 'Caldwell'
output = 'Hello, ' + first_name + ' ' + last_name
print(output)
output = 'Hello, {} {}'.format(first_name, last_name)
print(output)
output = 'Hello, {1} {0}'.format(first_name, last_name)
print(output)
output = f'Hello, {first_name} {last_name}'
print(output)
print('Hello,', first_name, last_name)

phrase = 'it\'s not easy'
print(phrase)