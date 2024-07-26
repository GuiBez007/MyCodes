# Write a program that allows user to type 7 numeric values and put it in an unic list with the even/odd numbers.
# At the end, show these values in ascending order.

numbers = [[], []]
print('Type 7 integer numbers below: ')
for i in range(7):
    number = int(input(f'N{i+1}> '))

    if number % 2 == 0:
        numbers[0].append(number)
    else:
        numbers[1].append(number)

print('\nEven: {} \nOdd: {}'.format(numbers[0], numbers[1]))

input() #wait