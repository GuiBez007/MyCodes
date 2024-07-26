# Write a program that has a list named numbers and 2 functions named draw() and sumEven(). The first function will
# draw 5 numbers and will put them in the list and the second function will show the sum between all even values
# drawn by the previous function.

from random import randint
numbers = []

def draw(times):
    for n in range(times):
        x = randint(2, 5)
        print('\nThe selected values is', end=' ')
        for i in range(x):
            numbers.append(randint(0, 50))
            print(numbers[i], end=' ')
        print()
        sumEven(numbers)


def sumEven(list):
    _sum = 0
    for i in range(len(list)):
        if list[i] % 2 == 0:
            _sum += list[i]
    list.clear()
    print(f'The sum of all even values is {_sum}!')


# main()
times = int(input('Inform how many sets you wanna see: '))
draw(times)

input() #wait