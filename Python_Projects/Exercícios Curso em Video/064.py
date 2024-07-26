# Write a code that reads various integer numbers by the keyboard. The program just will stop when the user types
# the value 999, that is a stop condition. At the end, show how many numbers was typed and what's the sum of these.

count = _sum = number = 0

print('Type integer numbers below to sum them [999 to stop]: ')
while number != 999:
    number = int(input('> '))
    if number != 999:
        _sum += number
        count += 1
print('The sum of all these {} numbers is {}.'.format(count, _sum))

input() #wait