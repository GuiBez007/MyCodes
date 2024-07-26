# Write a code that has a tuple totally full with a count by extensive, in range 0 - 20.
# The program must read a number by the keyboard (0-20) and show it in extensive.

numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
           'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')

while True:
    number = int(input('Type a number in range 0-20 to see it in extensive: '))
    if 0 <= number <= 20:
        print(f'The number {number} in extensive is {numbers[number]}. \n')
    else:
        break
print('Invalid! END!')

input() #wait