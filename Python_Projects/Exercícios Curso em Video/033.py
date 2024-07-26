# Write a code that informs the bigger and smaller number in 3

number_1 = int(input('Type the first number: '))
number_2 = int(input('Type the second number: '))
number_3 = int(input('Type the third number: '))

if number_1 > number_2:
    if number_1 > number_3:
        print('The number {} is the bigger'.format(number_1))

if number_2 > number_1:
    if number_2 > number_3:
        print('The number {} is the bigger'.format(number_2))

if number_3 > number_1:
    if number_3 > number_2:
        print('The number {} is the bigger'.format(number_3))


if number_1 < number_2:
    if number_1 < number_3:
        print('The number {} is the smaller'.format(number_1))

if number_2 < number_1:
    if number_2 < number_3:
        print('The number {} is the smaller'.format(number_2))

if number_3 < number_1:
    if number_3 < number_2:
        print('The number {} is the smaller'.format(number_3))

input() #wait