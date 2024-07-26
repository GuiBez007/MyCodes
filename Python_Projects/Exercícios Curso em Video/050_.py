# Write a code that reads six integer numbers and show just the sum of pairs (ignore odds)

_sum = 0
for i in range(6):
    number = int(input('Type the {} number: '.format(i+1))) ###
    if number % 2 == 0:
        _sum += number
print('The sum of the pairs informed numbers is {}.'.format(_sum))

input() #wait

