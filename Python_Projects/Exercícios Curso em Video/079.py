# Write a code that receive various numeric values and put them in a list. In case of the number even exist in list,
# he won't be added. At the end, show all unique typed values in ascending order.

count = 0
numbers = []

print('Type below how many numbers you wish[S to stop]: ')
while True:
    numbers.append(input('> ').strip())

    if numbers[count] in 'Ss':
        break
    elif numbers.count(numbers[count]) > 1:
        numbers.remove(numbers[count])
        count -= 1
    count += 1

print(f'The list in ascending order: \n{sorted(numbers[:-1])}')

input() #wait