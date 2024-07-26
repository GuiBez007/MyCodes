# Write a code that reads various integer numbers by the keyboard. At the end, show the average between
# all the values and what was the higher and the lower. The program must ask user if he wants or not
# to continue typing values.

_continue = 'S'
print('Type integer values below: ')
_sum = count = 0

while _continue != 'N':
    if count != 0:
        _continue = input('Do you want to continue?[S/N]: ').upper().strip()

    if _continue == 'S':
        number = int(input('> '))
        if count == 0:
            highest = lowest = number
        else:
            if number > highest:
                highest = number
            if number < lowest:
                lowest = number
        _sum = number
        count += 1

print('\n======== RESULTS ========\n'
      'The highest value is {};   \n'
      'The lowest value is {};    \n'
      'The average of all the {} values is {}.'.format(highest, lowest, count, _sum/count))

input() #wait