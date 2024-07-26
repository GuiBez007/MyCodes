# Create a program that reads the name, born year and work card and register (with age) in a dictionary.
# If the CTPS is different of ZERO, the dictionary will receive the hiring date and salary too.
# Calculate and add, in addition of age, in how many years the person will retire.

from datetime import date

person = {'name': input('NAME> ').strip().capitalize(),
          'age': date.today().year - int(input('BORN YEAR> ')),
          'workcard': int(input('WORK CARD [0 no have]> '))}

if person['workcard'] != 0:
    person['hiring year'] = int(input('HIRING YEAR> '))
    person['salary'] = float(input('SALARY> '))
    retire_with = (person['hiring year'] + 35) - (date.today().year) + person['age']

print('\nYour information')
for key, value in person.items():
    print(f'{key.upper()}: {value}')

if person['workcard'] != 0:
    if retire_with <= 0:
        print('You ever have the age to retire!')
    else:
        print(f'You\'ll retire with {retire_with} years old!')

input() #wait