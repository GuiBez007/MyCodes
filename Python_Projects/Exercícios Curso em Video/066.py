# Write a code that reads integer numbers. The program just will stop when the user types the value 999,
# that is the stop condition. At the end, show how many numbers was typed and what's the sum between them.

print('Type integer numbers below: ')
count = _sum = 0
while True:  # finally :)
    number = int(input('> '))
    if number == 999:
        break

    _sum += number
    count += 1

print('The sum of the {} informed values is {}.'.format(count, _sum))

input() #wait    