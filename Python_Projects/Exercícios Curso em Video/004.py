# Write a code that reads something and shows in the screen its primitive type and all possible information about it.

something = input('Type something: ')
print('Its primitive type is {}'.format(type(something)))
print('It\'s just spaces: {}'.format(something.isspace()))
print('It\'s a number: {}'.format(something.isnumeric()))
print('It\'s alphabetic: {}'.format(something.isalpha()))
print('It\'s alphanumeric: {}'.format(something.isalnum()))
print('It\'s in upper: {}'.format(something.isupper()))
print('It\'s in lower: {}'.format(something.islower()))
print('It\'s capitalized: {}'.format(something.istitle()))