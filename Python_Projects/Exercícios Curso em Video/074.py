# Write a code that will generate 5 random numbers and put them in a tuple. After this, show all the number list
# and the highest and lowest value.

from random import randint as r

numbers = (r(0, 100), r(0, 100), r(0, 100), r(0, 100), r(0, 100))
print(f'The tuple is composite by {numbers}')

lowest = highest = numbers[0]
for i in numbers:
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i

print('The highest number is {} and lowest {}.'.format(highest, lowest))

input() #wait