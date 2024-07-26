# Develop a program that reads 4 values and keep them in a tuple. At the end, show:
# How many times the number 9 has appeared
# What's the first position of number 3
# What was the pair numbers

print('Type 4 numbers to analyses: ')
numbers = (int(input('> ')), int(input('> ')), int(input('> ')), int(input('> ')))

print(f'\nThere are {numbers.count(9)} numbers 9 in tuple,')
if 3 in numbers:
    print(f'the number 3 is in the position {numbers.index(3)+1} and')
print(f'the pair numbers are ', end='')

for i in numbers:
    if i % 2 == 0:
        print(i, end=' ')

input() #wait